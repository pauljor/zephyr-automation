"""Reconcile csv_logs.txt with the ACTUAL Pass/Fail status of each Zephyr execution.

For every Execution.Key whose latest csv_logs.txt line is PASSED/FAILED, GET the live execution
from Zephyr Essential and compare. If Zephyr says something different (someone changed it by
hand, a bug-fix re-run flipped it, ...), the key's EXISTING line is changed in place to the Zephyr
status (no appended duplicate). Any key that has several lines is also compacted to one line, at
its first position, carrying the latest line's content. Nothing in Zephyr, JIRA or the sheet is
written by this script; run gsheet_sync.py afterwards to push the corrected logs.

  python zephyr_status_sync.py            # reconcile all PASSED/FAILED keys, fix lines in place
  python zephyr_status_sync.py --dry-run  # print the plan, write nothing
  python zephyr_status_sync.py --dedupe   # only collapse duplicate keys in the log (no Zephyr calls)
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


def rewrite(log, fixes):
    """Apply {key: (status, extra)} fixes in place and collapse duplicate keys (first position,
    latest content). Returns the number of duplicate lines removed."""
    lines = log.read_text(encoding="utf-8").splitlines()
    final = {}  # key -> final line text (last line wins, then fixes)
    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 3:
            final[parts[0]] = line
    for key, (status, extra) in fixes.items():
        final[key] = f"{key}, {status}, {extra}"
    out, seen = [], set()
    for line in lines:
        key = line.split(",")[0].strip()
        if key not in final:  # blank / malformed line: keep as is
            out.append(line)
        elif key not in seen:
            seen.add(key)
            out.append(final[key])
    with log.open("w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    return len(lines) - len(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("key", nargs="?")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--dedupe", action="store_true", help="only collapse duplicate keys, no Zephyr calls")
    args = ap.parse_args()

    env = load_env()
    log = Path(env.get("CSV_LOGS") or ROOT / "csv_logs.txt")
    if args.dedupe:
        print(f"removed {rewrite(log, {})} duplicate line(s)")
        return
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
    removed = 0
    if not args.dry_run:
        removed = rewrite(log, {k: (new, extra) for k, _, new, extra in fixes})
    print(f"checked {len(todo)}; matches {same}; {'would correct' if args.dry_run else 'corrected in place'} {len(fixes)}; duplicates removed {removed}; "
          f"other Zephyr status (left alone) {other or 'none'}; fetch errors {errors or 'none'}")
    if (fixes or removed) and not args.dry_run:
        print("Now run: python gsheet_sync.py --dry-run, then python gsheet_sync.py")


if __name__ == "__main__":
    main()
