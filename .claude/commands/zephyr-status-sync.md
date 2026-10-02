---
description: Reconcile csv_logs.txt with the actual Zephyr execution status of each test case, then push the corrected results to column I of the Google Sheet
---

Make `CSV_LOGS` (`csv_logs.txt`) and the Google Sheet's column I agree with what Zephyr Essential **actually** says about each execution, with Zephyr as the source of truth. Script: `zephyr_status_sync.py` (repo root). Read-only against Zephyr and JIRA.

Argument (optional, `$ARGUMENTS`): an `Execution.Key` (e.g. `EI-E1033`) to reconcile just that one; otherwise every key whose latest log line is `PASSED`/`FAILED`.

## Steps

1. Run `python zephyr_status_sync.py --dry-run $ARGUMENTS` and show the plan: each `<key>: log X -> Zephyr Y` line plus the summary `checked N; matches M; would correct C; other Zephyr status ...; fetch errors ...`.
2. If there is anything to correct, run `python zephyr_status_sync.py $ARGUMENTS` (no confirmation needed — it only edits `csv_logs.txt`).
3. Push to the sheet: run `python gsheet_sync.py --dry-run $ARGUMENTS`, show its plan line, then `python gsheet_sync.py $ARGUMENTS` and report `verified` / `VERIFY FAILED` / `not in sheet` / `left alone` as-is (see `/zephyr-gsheet-update`).
4. Report: how many keys disagreed and which, any with a non-Pass/Fail Zephyr status (`Not Executed`, `WIP`, `Blocked` — left alone, listed for the user), any fetch errors, and the sheet result. Don't commit anything.

## Rules

- Zephyr wins: the key's existing log line is changed **in place** to the Zephyr-confirmed status (third field `JIRA:...` kept); nothing is appended, so no key gets a second line. Any key that already has several lines is collapsed to one (first position, latest content). This is the one sanctioned exception to the logs being append-only. `--dedupe` does just the collapse, offline.
- Only `PASSED`/`FAILED` log lines are checked; `SKIPPED`/`BLOCKED` are not touched.
- Status names are resolved live from `GET /statuses?projectKey=EI` — no hardcoded IDs.
- Never writes to Zephyr or JIRA. If the Zephyr token is expired (HTTP 401 on every key), stop and tell the user to regenerate it (Jira profile → "Zephyr Essential API keys") instead of working around it.
