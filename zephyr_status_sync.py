"""Reconcile csv_logs.txt with the ACTUAL Pass/Fail status of each Zephyr execution.

For every Execution.Key whose latest csv_logs.txt line is PASSED/FAILED, GET the live execution
from Zephyr Essential and compare. If Zephyr says something different (someone changed it by
hand, a bug-fix re-run flipped it, ...), append a corrected line to csv_logs.txt (append-only;
the last line for a key wins, which is what gsheet_sync.py reads). Nothing in Zephyr, JIRA or the
sheet is written by this script; run gsheet_sync.py afterwards to push the corrected logs.

  python zephyr_status_sync.py            # reconcile all PASSED/FAILED keys, append corrections
  python zephyr_status_sync.py --dry-run  # print the plan, write nothing
  python zephyr_status_sync.py EI-E1033   # only that Execution.Key

Statuses are resolved live from GET /statuses?projectKey=EI (id -> name), nothing hardcoded.
Zephyr statuses other than Pass/Fail (Not Executed, WIP, Blocked...) are reported and left alone.
"""
import argparse
import json
import sys
from pathlib import Path

import requests

from gsheet_sync import load_env

ROOT = Path(__file__).resolve().parent
API = "https://prod-api.zephyr4jiracloud.com/v2"
WORD = {"pass": "PASSED", "fail": "FAILED"}


def token():
    cfg = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))
    for srv in cfg.get("mcpServers", {}).values():
        t = srv.get("env", {}).get("ZEPHYR_API_TOKEN")
        if t:
            return t
    sys.exit("ZEPHYR_API_TOKEN not found in .mcp.json")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("key", nargs="?")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    env = load_env()
    log = Path(env.get("CSV_LOGS") or ROOT / "csv_logs.txt")
    hdr = {"Authorization": f"Bearer {token()}"}

    r = requests.get(f"{API}/statuses", params={"projectKey": "EI", "maxResults": 100}, headers=hdr, timeout=30)
    r.raise_for_status()
    body = r.json()
    names = {s["id"]: s["name"] for s in (body.get("values", body) if isinstance(body, dict) else body)}

    latest = {}  # key -> (status, third field); last line wins
    for line in log.read_text(encoding="utf-8").splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 3:
            latest[parts[0]] = (parts[1], parts[2])
    todo = {k: v for k, v in latest.items() if v[0] in ("PASSED", "FAILED") and (not args.key or k == args.key)}
    if args.key and not todo:
        sys.exit(f"{args.key}: no PASSED/FAILED line in {log.name}")

    fixes, other, errors, same = [], [], [], 0
    for key, (status, extra) in todo.items():
        resp = requests.get(f"{API}/testexecutions/{key}", headers=hdr, timeout=30)
        if resp.status_code != 200:
            errors.append(f"{key} (HTTP {resp.status_code})")
            continue
        sid = resp.json().get("testExecutionStatus", {}).get("id")
        name = names.get(sid, f"id {sid}")
        actual = WORD.get(str(name).lower())
        if actual is None:
            other.append(f"{key}: Zephyr={name}, log={status}")
        elif actual == status:
            same += 1
        else:
            fixes.append((key, status, actual, extra))

    for key, old, new, extra in fixes:
        print(f"{key}: log {old} -> Zephyr {new}")
    if fixes and not args.dry_run:
        with log.open("a", encoding="utf-8", newline="\n") as f:
            if log.stat().st_size and not log.read_text(encoding="utf-8").endswith("\n"):
                f.write("\n")
            for key, _, new, extra in fixes:
                f.write(f"{key}, {new}, {extra}\n")
    print(f"checked {len(todo)}; matches {same}; {'would correct' if args.dry_run else 'corrected'} {len(fixes)}; "
          f"other Zephyr status (left alone) {other or 'none'}; fetch errors {errors or 'none'}")
    if fixes and not args.dry_run:
        print("Now run: python gsheet_sync.py --dry-run, then python gsheet_sync.py")


if __name__ == "__main__":
    main()
