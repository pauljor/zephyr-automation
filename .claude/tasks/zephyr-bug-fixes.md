# Task: Fix a bug from a JIRA bug ticket

## Purpose

Close the loop that [[zephyr-bug-tickets]] opens: take a bug ticket that task already
created (logged in `BUG_TICKET_LOGS`), write the actual code fix in the app repo it
belongs to (`eruditiontx-client-mvp` for FrontEnd, `eruditiontx-services-mvp` for
BackEnd), confirm the fix by re-running the real Zephyr test case(s) that originally
failed, then record what happened: comment on the ticket, move it to **In Progress**,
and log it locally.

This task does **not** resolve/close the ticket — only a human should make that call.
"In Progress" just signals a fix attempt has been made and recorded; if the re-run still
fails, that's logged honestly too (see "Logging" below), not silently hidden.

Scope: one ticket per invocation, via `/zephyr-bug-fix-one`. No bulk agent yet (unlike
the other two tasks) — add one later the same way `zephyr-bug-bulk.md` was added after
`zephyr-bug-one.md` was proven, if this needs to run over many tickets at once.

## Env vars used (from `.env` at repo root)

| Var | Meaning |
|---|---|
| `BUG_TICKET_LOGS` | `bug_tickets_log.txt` — the source list of bug tickets [[zephyr-bug-tickets]] already created. This task reads it to know which JIRA keys exist and which Test Case.Key/Execution.Key rows back each one; it never mutates this file. |
| `JIRA_URL` | The board the ticket lives on (project `EI`, board 121). |
| `ZEPHYR_URL` | Base URL of the Zephyr Essential panel, for building test case links if needed in a comment. |
| `BUG_FIX_LOGS` | **New** — local log file (`bug_fixes_log.txt`, same folder as `CSV_LOGS`/`BUG_TICKET_LOGS`) this task appends to, one line per Zephyr test case re-run as part of a fix. Add to `.env` if missing: `BUG_FIX_LOGS=<repo>\zephyr-automation\bug_fixes_log.txt`. |

`ZEPHYR_API_TOKEN` (from `.mcp.json`, see `zephyr-jira-sync.md` → "Note on `.mcp.json`")
is used the same way as the other two tasks — direct REST calls to
`https://prod-api.zephyr4jiracloud.com/v2`, never through the `zephyr-scale` MCP tools.

## Picking which ticket to fix

1. Read `BUG_TICKET_LOGS`. Each line is `<Test Case.Key>, EXEC:<Execution.Key>,
   JIRA:<Bug ticket key>[, PREEXISTING]`.
2. **Group by the JIRA ticket key (3rd field), not by Test Case.Key.** A `PREEXISTING`
   line points at the same ticket as an earlier row — that's [[zephyr-bug-tickets]]'s
   consolidation mechanism, and one code fix closes the whole ticket, not each row
   separately. Build a map: JIRA key → every {Test Case.Key, Execution.Key} pair logged
   against it.
3. Read `BUG_FIX_LOGS` (create it if it doesn't exist yet) and collect every JIRA key
   already logged there (the `JIRA:` field on any line) — idempotency, same "appears
   anywhere, regardless of result" rule the other two logs use. A ticket already in
   `BUG_FIX_LOGS` has already had a fix attempt recorded (whether it passed or not);
   don't silently redo it.
4. `$ARGUMENTS` (optional): a JIRA bug ticket key (e.g. `EI-3455`). If given, target
   that ticket directly. If it isn't in `BUG_TICKET_LOGS`, or it's already in
   `BUG_FIX_LOGS`, report that and stop without doing anything. If omitted, pick the
   first JIRA key (in `BUG_TICKET_LOGS` order) not yet in `BUG_FIX_LOGS`. If none
   remain, report that everything already has a logged fix attempt and stop.

## Reading the ticket

`getJiraIssue` the target key and parse it per the shape [[zephyr-bug-tickets]] creates:

- **Summary**: `[BUG] [<Category>] <name>` — `Category` is `FrontEnd` or `BackEnd`,
  already decided at ticket-creation time. Use it as-is; don't re-derive it.
- **Description**:
  - `**Reason**` section — the STEPS/EXPECTED/ACTUAL content carried over from the
    Zephyr execution's comment. This is what's actually broken.
  - `**API**` line(s), BackEnd tickets only — one `METHOD path` per endpoint involved.
  - `**Zephyr Test Cases**` bulleted list — one or more
    `[<Test Case.Key> — <Test Case.Name>](<url>) — EXEC:<Execution.Key>` entries. This
    is the **authoritative** list of every execution to re-run once fixed — prefer it
    over the rows found in "Picking which ticket to fix" step 2 above, in case the
    ticket was consolidated more recently than `BUG_TICKET_LOGS` reflects.

## Locating and fixing the code

1. **BackEnd** (`eruditiontx-services-mvp`): start from the `**API**` line's
   `METHOD path` — grep for that route across the service's route definitions to find
   the handler and whatever logic it calls. Also find the failing automated test in
   `teacher-student-automation/service/tests/` (same lookup [[zephyr-bug-tickets]]'s
   "Determining the bug category" step used — by Test Case.Key or column G/summary
   keywords) and run it once, unmodified, against the live QA host
   (`https://eruditionsolutionsqa.com`, per `zephyr-jira-sync.md`) to reproduce the
   failure before touching anything.
2. **FrontEnd** (`eruditiontx-client-mvp`): find the failing test in
   `teacher-student-automation/client/tests/` (Page Object Model) the same way, run it
   once to reproduce, then trace from the page object into the actual
   component/hook/page in the client repo responsible for the behavior under test.
3. Read that subproject's own `CLAUDE.md` (`eruditiontx-services-mvp/CLAUDE.md` or
   `eruditiontx-client-mvp/CLAUDE.md`) before editing — follow its conventions, don't
   introduce a fix that conflicts with them.
4. Make the minimal code change that resolves the gap between EXPECTED and ACTUAL from
   the ticket's Reason section. This is a real fix, not a throwaway patch.
5. **Leave the change as an edited working tree in that subproject.** Don't commit or
   push it automatically — this environment's standing rule is to only commit when the
   user explicitly asks, and a fix here should get a human look at the diff first. Name
   the exact file(s) changed in the final summary so that's easy.

## Confirming the fix

For **every** execution listed in the ticket's `**Zephyr Test Cases**` section (not
just the row that was used to pick the ticket, if it had more than one):

1. Re-run the matching automated test for real against the live QA host.
2. `PUT https://prod-api.zephyr4jiracloud.com/v2/testexecutions/<Execution.Key>` with
   `{"statusName": "Pass"|"Fail", "comment": "<STEPS/EXPECTED/ACTUAL HTML per
   zephyr-jira-sync.md's template, ACTUAL reflecting this re-run's real outcome>"}`
   — the real, current result, not the assumed "it's fixed now" outcome.
3. Re-`GET` the execution and confirm `testExecutionStatus.id` actually changed
   (`14539939` = Pass, `14539940` = Fail) before trusting it, same rule as every other
   Zephyr write in this repo. If the write doesn't take, don't guess — treat this one
   execution like a `BLOCKED` row (see "If something doesn't fit" below) rather than
   logging an unconfirmed result.

If some executions on the ticket now pass and others still fail, record each one's
real result independently in "Logging" below — don't round up to "fixed" just because
some passed.

## Closing the loop on the JIRA ticket

Once every execution on the ticket has been re-run and its real result confirmed
(regardless of whether all of them passed):

1. **Comment** on the ticket (`addCommentToJiraIssue`/equivalent), covering:
   - **Issue** — what was actually wrong (root cause), in your own words.
   - **Solution** — what code change was made (file(s) touched, in plain terms), or,
     if any re-run still fails, what was tried and what's still broken.
   - **Remarks** — anything a reviewer should know: edge cases considered, follow-ups,
     why this approach, which re-runs (if any) still failed.
2. **Transition** the ticket to **In Progress**: call `getTransitionsForJiraIssue` on
   the ticket and find the transition whose target status name is `In Progress`
   (case-insensitive) — don't hardcode a transition id here, unlike
   `zephyr-bug-tickets.md`'s confirmed id `8` for "BUG - Blocked by Defect", this one
   hasn't been confirmed against a real ticket yet (see "Resolved" below — update this
   spec with the real id once a live run confirms it, the same way that one was
   documented).
3. `getJiraIssue` again and confirm `fields.status.name` is exactly `"In Progress"`. If
   it isn't, don't force it further — still do the logging below (the code fix and
   comment are real and worth recording), but flag the status transition as unresolved
   in the final summary.

## Logging (`BUG_FIX_LOGS`)

One line per execution re-run as part of this ticket's fix (so a consolidated ticket
covering more than one Zephyr test case produces multiple lines, all sharing the same
JIRA key), appended (not overwritten), space after each comma:

```
JIRA:<Bug ticket key>, EXEC:<Execution.Key>, TESTCASE:<Test Case.Key>, RESULT:<PASSED|FAILED>
```

e.g. `JIRA:EI-3455, EXEC:EI-E1033, TESTCASE:EI-T356, RESULT:PASSED`.

`RESULT` is the real, re-`GET`-confirmed outcome from "Confirming the fix" above — a
`FAILED` line here is an honest record that this fix attempt didn't resolve that
execution, not something to round up. It still counts toward idempotency (see "Picking
which ticket to fix" step 3) so a later run doesn't silently retry the whole ticket; a
`FAILED` result needs a human to pick the ticket back up (it's already commented and
in "In Progress", so it's visible on the board).

Only write these lines after the JIRA comment + transition attempt in "Closing the
loop" above, not before — if that step never runs (e.g. the fix couldn't be located,
see "If something doesn't fit"), nothing should be logged.

## If something doesn't fit

Don't guess past a blocker. If the ticket can't be parsed into the expected
summary/description shape, the code location can't be confidently traced from the
`**API**` line or the failing test, a Zephyr `PUT` doesn't actually change status on
re-`GET`, or the JIRA comment/transition calls error out — stop processing that ticket,
report exactly what happened (JIRA key, which execution(s), what failed), and do
**not** write a `BUG_FIX_LOGS` line for it, so a later run doesn't skip it.

## Resolved (previously "open items to confirm")

- **"In Progress" transition id**: not yet confirmed against a real ticket — the first
  live run of this task should look it up via `getTransitionsForJiraIssue`, use it, and
  this line should be updated with the confirmed id (the way `zephyr-bug-tickets.md`
  documents `id: "8"` for "BUG - Blocked by Defect") once verified.

## Notes

- Downstream of [[zephyr-bug-tickets]]: reads `BUG_TICKET_LOGS` only, never mutates it
  or re-runs anything from that task's own workflow.
- Downstream of [[zephyr-jira-sync]] by extension, for the same reason
  `zephyr-bug-tickets.md` is: `FAILED` rows there are what eventually produce the
  tickets this task fixes.
- Committing/pushing the code fix is a separate, explicit step for the user to ask for
  once they've reviewed the diff — this task's job stops once the fix is verified
  (or honestly recorded as still failing) and the ticket is updated.
