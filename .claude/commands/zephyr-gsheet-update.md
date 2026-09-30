---
description: Sync PASSED/FAILED results from csv_logs.txt into column I of the shared Google Sheet ("Passed <date>" black on green fill / "Failed <date>" black on red fill)
---

Run `gsheet_sync.py` (repo root) to push the results in `CSV_LOGS` (`csv_logs.txt`) into **column I only** of the shared Google Sheet. Nothing is hardcoded: the script re-reads the log and the live sheet on every run, maps `Execution.Key` (column B) → row itself, and skips rows that already show the same result. It never mutates any log, Zephyr, or JIRA.

Argument (optional, `$ARGUMENTS`): an `Execution.Key` (e.g. `EI-E1033`) to sync just that row; `--watch` to keep running and re-sync every time `csv_logs.txt` changes; `--dry-run` to print the plan without writing; `--reformat` to re-apply colors to rows already written (text/date unchanged); `--redate` to rewrite rows already showing the right result but a date that differs from the log line's commit date.

## Steps

1. Confirm setup exists (one time — see the script's docstring): `GSHEET_ID`/`GSHEET_GID` in `.env`, `GSHEET_TOKEN` + `GSHEET_WEBAPP_URL` in the gitignored `.env.local`, `gsheet_webapp.gs` deployed as a web app on the sheet (Execute as: Me, Access: Anyone), and `pip install requests`. If `GSHEET_WEBAPP_URL` is empty or the script says the web app didn't return JSON/refused the token, stop and tell the user the exact remaining step — don't work around it.
2. Run `python gsheet_sync.py --dry-run $ARGUMENTS` first and show the plan line: `write N (P passed, F failed); already set S; not in sheet [...]; left alone [...]`.
3. Run `python gsheet_sync.py $ARGUMENTS` (no confirmation needed — it edits one display column and re-runs are safe). Expect `verified` at the end: the web app reads each cell back after writing and the script checks it holds the intended text. Report `VERIFY FAILED` keys, `not in sheet` keys and `left alone` cells (`Not Executed`/free text is never overwritten) as-is; don't claim success for rows that didn't verify.
4. Colors are set by the web app (`Passed` → black text on green fill #00ff00; `Failed` → black text on red fill #ff0000); they can't be seen in the CSV export, so if asked to confirm them, screenshot a few rows in the sheet.

## Rules

- Column I only. Only `PASSED`/`FAILED` log lines are written; `SKIPPED` and others are ignored. The last log line for a key wins.
- Date is the commit date of the `csv_logs.txt` line that holds the result (`git blame`, committer date in the commit's timezone), `M/D/YYYY` (matches existing cells like `Passed 9/28/2026`). A line not committed yet falls back to today's date.
- Already `Passed`/`Failed` matching the log → left as is (keeps the original date, unless `--redate`); the opposite word → overwritten with the new result.
- Never commit the service-account key (`gsheet-service-account.json` is in `.gitignore`).
