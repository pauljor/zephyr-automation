---
description: Fix exactly ONE JIRA bug ticket's underlying defect, confirm via re-run, then stop
---

Follow the workflow defined in `.claude/tasks/zephyr-bug-fixes.md` in this repo, but fix **only a single bug ticket** on this invocation, then stop. Do not loop over multiple tickets.

Argument (optional, `$ARGUMENTS`): a JIRA bug ticket key (e.g. `EI-3455`) to target a specific ticket. If omitted, pick the first unprocessed ticket per step 3 below.

Steps:

1. Read `.claude/tasks/zephyr-bug-fixes.md` for the full spec (env vars, ticket parsing, code-location logic, close-out steps, log format).
2. Read `BUG_TICKET_LOGS`. Group its rows by the JIRA ticket key (3rd field, `JIRA:<key>`) — a `PREEXISTING` row points at the same ticket as an earlier row (consolidation), so build one map entry per distinct JIRA key listing every {Test Case.Key, Execution.Key} pair logged against it.
3. Read `BUG_FIX_LOGS` (create it if it doesn't exist yet, path from the `BUG_FIX_LOGS` env var — add it to `.env` first if missing: `BUG_FIX_LOGS=<repo>\zephyr-automation\bug_fixes_log.txt`) and collect every JIRA key already logged there (any line's `JIRA:` field).
   - If `$ARGUMENTS` was given: use that key directly. If it isn't in `BUG_TICKET_LOGS`, or it's already in `BUG_FIX_LOGS`, report that and stop without doing anything.
   - If no argument: pick the first JIRA key (in `BUG_TICKET_LOGS` order) from step 2 that is NOT yet in `BUG_FIX_LOGS`. If none remain, report that every ticket already has a logged fix attempt and stop.
4. `getJiraIssue` the target ticket. Parse the summary for its category (`[BUG] [FrontEnd|BackEnd] <name>` — use as-is, don't re-derive) and the description for its `**Reason**` (STEPS/EXPECTED/ACTUAL), `**API**` line(s) if BackEnd, and `**Zephyr Test Cases**` list — that list is authoritative for which executions to re-run in step 6, taking priority over what step 2 found if the ticket was consolidated more recently.
5. Locate and fix the defect per the spec's "Locating and fixing the code" section:
   - **BackEnd** (`eruditiontx-services-mvp`): trace the `**API**` line's `METHOD path` to its route handler; also find and run the matching test in `teacher-student-automation/service/tests/` once, unmodified, against `https://eruditionsolutionsqa.com` to reproduce the failure first.
   - **FrontEnd** (`eruditiontx-client-mvp`): find and run the matching test in `teacher-student-automation/client/tests/` first to reproduce, then trace into the relevant component/hook/page.
   - Read that subproject's own `CLAUDE.md` before editing. Make the minimal fix for the gap between EXPECTED and ACTUAL. **Leave it as an uncommitted working-tree change** — do not commit or push automatically; name the exact file(s) changed in the final summary.
6. For **every** execution in step 4's `**Zephyr Test Cases**` list: re-run its automated test for real against the live QA host, then `PUT https://prod-api.zephyr4jiracloud.com/v2/testexecutions/<Execution.Key>` with `{"statusName": "Pass"|"Fail", "comment": "<STEPS/EXPECTED/ACTUAL HTML per zephyr-jira-sync.md's template, ACTUAL reflecting this re-run's real result>"}`. Re-`GET` to confirm `testExecutionStatus.id` actually changed (`14539939`=Pass, `14539940`=Fail) before trusting it — if it didn't, treat that one execution as unconfirmed/blocked rather than guessing a result.
7. Once every execution's real result is confirmed (whether all passed or not):
   - **Comment** on the ticket covering **Issue** (root cause), **Solution** (what was changed, or what was tried and what's still broken if a re-run still fails), and **Remarks** (edge cases, follow-ups, which executions if any still fail).
   - **Transition** the ticket to **In Progress**: call `getTransitionsForJiraIssue`, find the transition whose target status name is `In Progress` (case-insensitive; the id isn't hardcoded in the spec yet — note it there once confirmed), and apply it. `getJiraIssue` again and confirm `fields.status.name` is exactly `"In Progress"`; if not, flag it as unresolved in the summary but continue to the logging step regardless (the code fix and comment already happened and are worth recording).
8. Append one line per execution from step 6 to `BUG_FIX_LOGS`: `JIRA:<Bug ticket key>, EXEC:<Execution.Key>, TESTCASE:<Test Case.Key>, RESULT:PASSED|FAILED` — only after step 7 has run, not before. If step 5/6 never reached a confirmable result (code location couldn't be traced, a Zephyr write never took, etc.), don't log anything for this ticket — report the blocker per the spec's "If something doesn't fit" instead.
9. **No confirmation needed before commenting/transitioning/logging.** Proceed straight through once the code fix is made and verified; report what was done (ticket key, category, file(s) changed, per-execution re-run results, transition outcome) in the final summary, after the fact. Committing/pushing the code change is a separate step — ask the user before doing either.
10. Stop after this one ticket. Do not automatically continue to the next one — run `/zephyr-bug-fix-one` again for the next item.
