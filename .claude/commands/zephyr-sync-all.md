---
description: Run the full Zephyr/JIRA sync across all remaining rows via the zephyr-jira-sync-runner agent, then log Passed/Failed <date executed> to the Google Sheet
---

Argument (optional, `$ARGUMENTS`): a limit such as `execute 24 items only`. If present, pass it to the agent as a hard cap on rows processed this run; otherwise there is no cap.

## Steps

1. **Sync.** Launch the `zephyr-jira-sync-runner` agent (defined in `.claude/agents/zephyr-jira-sync-runner.md`) to process every remaining unprocessed row from `.claude/tasks/zephyr-jira-sync.md`, one row at a time, until none are left, the cap is reached, or it hits a blocker. Wait for it to finish and note the execution keys it appended to `CSV_LOGS` this run.
2. **Log results to the Google Sheet.** Once the agent completes (even if it stopped on a `BLOCKED` row or hit the cap), follow the `/zephyr-gsheet-update` steps (`.claude/commands/zephyr-gsheet-update.md`) so column I shows `Passed <date executed>` / `Failed <date executed>` for the rows just processed:
   - Run `python gsheet_sync.py --dry-run` and show the plan line.
   - Run `python gsheet_sync.py` (no confirmation needed; re-runs are safe).
   - Do this **before committing** `csv_logs.txt`, so the date is today's, the execution date. The script dates each result by the commit date of its log line and falls back to today for uncommitted lines. If the new lines were somehow already committed on an earlier day, pass `--redate`.
   - Only `PASSED`/`FAILED` lines are written; `SKIPPED`/`BLOCKED` are ignored by design.
3. **Setup problems don't undo the sync.** If gsheet setup is missing (`GSHEET_WEBAPP_URL` empty, web app refusing the token, `requests` not installed), do not work around it. Report the exact remaining step and that the sync itself is complete and logged; the user can rerun `/zephyr-gsheet-update` later.
4. **Report** the agent's summary (rows by status, blockers, any side effects it flagged) plus the sheet result: rows written (passed/failed), `VERIFY FAILED` keys, `not in sheet` keys and `left alone` cells, as-is. Do not claim success for rows that didn't verify.

The sheet step only edits column I; it never mutates `CSV_LOGS`, Zephyr, or JIRA.
