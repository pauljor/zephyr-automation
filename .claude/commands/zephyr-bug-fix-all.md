---
description: Fix the defect behind EVERY failed Zephyr test case logged FAILED in csv_logs.txt (FrontEnd or BackEnd), one at a time, applying the /zephyr-bug-fix-one logic to each
---

Fix every failed Zephyr test case in `CSV_LOGS` (`csv_logs.txt`), sequentially, applying **exactly the `/zephyr-bug-fix-one` logic** (`.claude/commands/zephyr-bug-fix-one.md`, steps 1–10 and its Blockers section) to each target. Read that command and `.claude/tasks/zephyr-bug-fixes.md` in full first; they are authoritative for mechanics (Zephyr REST, locating/fixing code, drift check, PR citation, HTML comment template, column J write, log format). This command only adds the batching, selection and stop rules below.

Usage: `/zephyr-bug-fix-all` — no arguments. Optional `$ARGUMENTS`: `--dry-run` = only print the work list (Selection steps 1–4) and stop.

This runs **inline in the main session** (no subagent).

## Selection (the work list)

1. Read `csv_logs.txt`; collect every line whose status is `FAILED` (`<Execution.Key>, FAILED, ...`). That file is the only source of *which* executions are failures — don't re-derive failures from Zephyr or the CSV.
2. Parse `test_cases.csv` (Python `csv`): map each `Execution.Key` (col B) to its Test Case.Key (col F) and name (col G). **Group by Test Case.Key** — one fix pass per test case covers all of its failed executions (a test case's other executions, even if not FAILED in `CSV_LOGS`, are covered by the same local check, as in fix-one step 1).
3. Drop any test case whose executions **all** already appear in `BUG_FIX_LOGS` (`bug_fixes_log.txt`, any result). Those are done; a previously logged `FAILED` is retried only by an explicit `/zephyr-bug-fix-one <key>`.
4. Classify each remaining test case FrontEnd/BackEnd per fix-one step 3 (where its test lives). Print the work list — test case, executions, name, category — and, if `--dry-run`, stop here. Empty list → report "nothing to fix" and stop.

## Per item (strictly one at a time, never parallel)

For each test case in CSV row order, run fix-one steps 2–9 (step 5 = local verification) in full: read state → reproduce → minimal fix → verify locally → trace PR if already fixed → write Problem/Solution/Remarks + status to Zephyr (re-`GET` to confirm) → `python gsheet_sync.py --fixed <Execution.Key>` for real Passes → append to `BUG_FIX_LOGS` (`JIRA:NONE, EXEC:<key>, TESTCASE:<key>, RESULT:PASSED|FAILED`). Print one line per item as you go (test case, category, result); don't wait for confirmation on Zephyr/gsheet/log writes.

## Verification is local

Per fix-one step 5, every item (FrontEnd or BackEnd) is verified **locally** with a before/after check; nothing is pushed or deployed, and fixes stay uncommitted. There is no BackEnd pause point. Mention in each Zephyr comment's Remarks that verification was local and QA still needs the deploy.

## Stop rules

- A **blocker** (fix-one "Blockers": unresolvable target/category, untraceable code, Zephyr write that doesn't confirm, sheet write that fails verification) stops that item, writes **no** `BUG_FIX_LOGS` line for it, and is recorded — then **stop the whole run** and report it; don't skip silently past it. Items finished before it keep their results.
- A confirmed `Fail` (including the deliberate-design-decision case) is not a blocker: it gets its comment, a `FAILED` log line, no column J mark, and the run continues.
- If `gsheet_sync.py` says the web app is out of date, tell the user the redeploy step once and continue.

## Summary

At the end report: items processed / total, per test case — category, before→after status per execution, files changed (always uncommitted; nothing is pushed), PR cited if already fixed, column J written or not; confirmed-still-failing items; files changed awaiting commit/deploy; and the blocker (item + reason) if the run stopped early.
