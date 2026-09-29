"""Push PASSED/FAILED results from csv_logs.txt into column I of the shared Google Sheet.

Dynamic, nothing hardcoded: every run re-reads csv_logs.txt and the live sheet (column B
Execution.Key -> row), writes only column I ("Passed <date>" black on green fill / "Failed <date>" black on red fill),
and skips rows already showing the same result. Safe to re-run.

  python gsheet_sync.py            # one sync, then exit
  python gsheet_sync.py --watch    # sync now, then again every time csv_logs.txt changes
  python gsheet_sync.py --dry-run  # print the plan, write nothing
  python gsheet_sync.py --reformat # re-apply colors to rows already written (text/date kept)
  python gsheet_sync.py EI-E1033   # only that Execution.Key

Setup (one time): pip install requests; paste gsheet_webapp.gs into the sheet (Extensions ->
Apps Script), deploy it as a web app (Execute as: Me, Access: Anyone) and put the URL in
.env.local as GSHEET_WEBAPP_URL (with the GSHEET_TOKEN already generated there). Reading uses
the sheet's public CSV export; writing goes through the web app, which runs as the sheet owner.
"""
import argparse
import datetime
import json
import os
import re
import sys
import time
from pathlib import Path

import csv
import io

import requests

ROOT = Path(__file__).resolve().parent
# (font color, background) per result: black text on a green / red fill (matches the hand-made cells)
STYLE = {"Passed": ("#000000", "#00ff00"), "Failed": ("#000000", "#ff0000")}
WEBAPP_VERSION = 2  # must match VERSION in gsheet_webapp.gs
KEY_COL, STATUS_COL = 1, 8  # zero-based: column B, column I


def load_env():
    env = dict(os.environ)
    for name in (".env", ".env.local"):  # .env.local holds secrets and is gitignored
        f = ROOT / name
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                env.setdefault(k.strip(), v.strip().strip('"'))
    return env


def read_log(path):
    """Execution.Key -> 'Passed'/'Failed' (last line for a key wins; other statuses ignored)."""
    result = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 2:
            continue
        if parts[1] == "PASSED":
            result[parts[0]] = "Passed"
        elif parts[1] == "FAILED":
            result[parts[0]] = "Failed"
        else:
            result.pop(parts[0], None)  # e.g. SKIPPED: nothing to write
    return result


class Sheet:
    def __init__(self, env):
        for k in ("GSHEET_ID", "GSHEET_GID", "GSHEET_WEBAPP_URL", "GSHEET_TOKEN"):
            if not env.get(k):
                sys.exit(f"Missing {k} in .env / .env.local (see the setup notes in this file's docstring).")
        self.id, self.gid = env["GSHEET_ID"], env["GSHEET_GID"]
        self.url, self.token = env["GSHEET_WEBAPP_URL"], env["GSHEET_TOKEN"]

    def check_webapp(self):
        """Refuse to write through a stale deployment (it would set text colors but no fill)."""
        try:
            v = requests.get(self.url, timeout=60).json().get("v")
        except ValueError:
            v = None
        if v != WEBAPP_VERSION:
            sys.exit("The deployed web app is out of date. In Apps Script paste the current "
                     "gsheet_webapp.gs, then Deploy -> Manage deployments -> Edit -> Version: New version -> Deploy.")

    def read(self):
        """Current sheet rows via the public CSV export (no login needed to read)."""
        r = requests.get(f"https://docs.google.com/spreadsheets/d/{self.id}/export",
                         params={"format": "csv", "gid": self.gid}, timeout=60)
        r.raise_for_status()
        return list(csv.reader(io.StringIO(r.content.decode("utf-8"))))

    def write(self, updates):  # updates: [(row_1based, key, text, (font, background))] -> web-app response
        body = {"token": self.token, "gid": int(self.gid), "updates": [
            {"row": row, "key": key, "text": text, "color": fg, "background": bg}
            for row, key, text, (fg, bg) in updates]}
        r = requests.post(self.url, data=json.dumps(body), timeout=300)
        r.raise_for_status()
        try:
            resp = r.json()
        except ValueError:
            sys.exit("Web app did not return JSON (wrong URL, or not deployed as 'Anyone'?): " + r.text[:200])
        if not resp.get("ok"):
            sys.exit(f"Web app refused the update: {resp.get('error')}")
        return resp


def plan(results, rows, only=None, today=None, reformat=False):
    today = today or datetime.date.today()
    date = f"{today.month}/{today.day}/{today.year}"
    key_row = {r[KEY_COL].strip(): n for n, r in enumerate(rows, 1) if len(r) > KEY_COL}
    out = dict(write=[], skipped=0, missing=[], left_alone=[])
    for key, word in results.items():
        if only and key != only:
            continue
        n = key_row.get(key)
        if n is None:
            out["missing"].append(key)
            continue
        row = rows[n - 1]
        cur = (row[STATUS_COL] if len(row) > STATUS_COL else "").strip()
        if cur.startswith(word):
            if reformat:  # re-apply colors only, keep the existing text/date
                out["write"].append((n, cur, STYLE[word], key))
            else:
                out["skipped"] += 1
        elif cur and not re.match(r"(Passed|Failed)\b", cur):
            out["left_alone"].append((key, cur))
        else:
            out["write"].append((n, f"{word} {date}", STYLE[word], key))
    return out


def sync(sheet, log_path, only=None, dry=False, reformat=False):
    p = plan(read_log(log_path), sheet.read(), only, reformat=reformat)
    n_pass = sum(1 for _, t, *_ in p["write"] if t.startswith("Passed"))
    print(f"{time.strftime('%H:%M:%S')} write {len(p['write'])} ({n_pass} passed, "
          f"{len(p['write']) - n_pass} failed); already set {p['skipped']}; "
          f"not in sheet {p['missing'] or 0}; left alone {p['left_alone'] or 0}")
    if p["write"] and not dry:
        sheet.check_webapp()
        resp = sheet.write([(r, k, t, c) for r, t, c, k in p["write"]])
        # verify from the web app's own read-back of each cell, not just its ok flag
        got = {int(r): v for r, v in resp.get("values", {}).items()}
        bad = [k for r, t, _, k in p["write"] if got.get(r) != t]
        if resp.get("mismatched"):
            print("skipped (row no longer matches key):", resp["mismatched"])
        print("verified" if not bad else f"VERIFY FAILED for {bad}")
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("key", nargs="?", help="only this Execution.Key")
    ap.add_argument("--watch", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reformat", action="store_true", help="re-apply colors to already-set rows (text unchanged)")
    ap.add_argument("--interval", type=float, default=5.0, help="watch poll seconds")
    args = ap.parse_args()
    env = load_env()
    log = Path(env["CSV_LOGS"])
    log = log if log.is_absolute() else ROOT / log
    sheet = Sheet(env)
    sync(sheet, log, args.key, args.dry_run, args.reformat)
    if not args.watch:
        return
    print(f"watching {log} (Ctrl+C to stop)")
    last = log.stat().st_mtime_ns
    while True:
        time.sleep(args.interval)
        if log.stat().st_mtime_ns != last:
            time.sleep(2)  # debounce: let a bulk run finish appending
            last = log.stat().st_mtime_ns
            try:
                sync(sheet, log, args.key, args.dry_run)
            except Exception as e:  # keep watching; the next change retries
                print("sync failed:", e)


if __name__ == "__main__":
    main()
