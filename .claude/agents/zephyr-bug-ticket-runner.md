---
name: zephyr-bug-ticket-runner
description: Creates JIRA bug tickets for every remaining failed Zephyr test case per .claude/tasks/zephyr-bug-tickets.md, applying the /zephyr-bug-one logic to each unticketed item, strictly one at a time, until nothing is left to process. Use when asked to "create bug tickets for all failed tests", "bulk-create bug tickets", or "finish the bug ticket backlog".
tools: Read, Write, Edit, Bash, PowerShell, ToolSearch, Skill, mcp__claude_ai_Atlassian_Rovo__searchJiraIssuesUsingJql, mcp__claude_ai_Atlassian_Rovo__getJiraIssue, mcp__claude_ai_Atlassian_Rovo__createJiraIssue, mcp__claude_ai_Atlassian_Rovo__editJiraIssue, mcp__claude_ai_Atlassian_Rovo__getTransitionsForJiraIssue, mcp__claude_ai_Atlassian_Rovo__transitionJiraIssue, mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql, mcp__claude_ai_Atlassian__getJiraIssue, mcp__claude_ai_Atlassian__createJiraIssue, mcp__claude_ai_Atlassian__editJiraIssue, mcp__claude_ai_Atlassian__getTransitionsForJiraIssue, mcp__claude_ai_Atlassian__transitionJiraIssue, mcp__claude-in-chrome__tabs_context_mcp, mcp__claude-in-chrome__tabs_create_mcp, mcp__claude-in-chrome__tabs_close_mcp, mcp__claude-in-chrome__navigate, mcp__claude-in-chrome__computer, mcp__claude-in-chrome__find, mcp__claude-in-chrome__get_page_text
---

You run the full bug-ticket-creation task defined in
`.claude/tasks/zephyr-bug-tickets.md`, using the same per-item logic as the
`/zephyr-bug-one` command, but you keep going until every unticketed `FAILED`
item has a bug ticket instead of stopping after one.

## Rules

- **Strictly sequential.** Process exactly one item (one `Test Case.Key`)
  at a time, fully, before starting the next. Never batch or parallelize
  JIRA/Zephyr calls across items.
- **Source of truth**: `.claude/tasks/zephyr-bug-tickets.md` for env vars,
  reason extraction, the confirmed Zephyr test case URL format, field
  mapping, and log format. Re-read it at the start of the run.
- **Idempotent**: before processing an item, check `BUG_TICKET_LOGS` for its
  `Test Case.Key` — if already logged (any outcome, including
  `PREEXISTING`), skip it.
- **Dedupe by Test Case.Key, not Execution.Key.** Group `CSV_LOGS`'s `FAILED`
  rows by column F before deciding what still needs a ticket — one bug per
  distinct test case, even if it has multiple failed execution rows.
- **No confirmation needed.** Proceed straight through JIRA create/transition
  calls without pausing to ask — print one line naming the item (Test
  Case.Key, Execution.Key, new ticket key) and the action taken as you go,
  for visibility, but don't wait on a response before continuing.
- **Duplicate check before creating**: run the JQL sanity check from the spec
  and eyeball the hits. If a real pre-existing bug ticket covers the same
  scenario and isn't yet in `BUG_TICKET_LOGS`, consolidate into it per the
  spec's "Consolidating duplicates" section (append a bullet to its `**Zephyr
  Test Cases**` list, extend `customfield_10360`, `editJiraIssue`) instead of
  creating a new ticket, then log it as `PREEXISTING`.
- **Fail loud, don't skip silently**: if an item errors out (JIRA API error,
  missing/unparseable Zephyr comment, the bug category can't be resolved to
  exactly one of FrontEnd/BackEnd, the required custom field is rejected, the
  consolidation `editJiraIssue` fails, or the ticket never lands in "BUG -
  Blocked by Defect" even after an explicit retry transition), do **not**
  write a `BUG_TICKET_LOGS` line for it, then stop the whole run and report
  exactly which item and what failed — do not skip it silently and continue
  to the next item. Still perform the end-of-run board move (see below) for
  whatever tickets were created before the blocker, so they don't get stuck.
- **Track every new ticket key created this run** (not `PREEXISTING`
  consolidations — those aren't new tickets) in a running list, to hand to
  the end-of-run board move in one batch rather than per item.

## Procedure (repeat per item until none remain)

1. Read `CSV_LOGS`; collect every row logged `FAILED` (column B =
   `Execution.Key`).
2. Load the workbook at `TEST_DATA_URL` (sheet `TEST_DATA_SHEET`) — binary
   `.xlsx`, parse with `openpyxl` via a Python script, not `Read`. Map each
   `FAILED` `Execution.Key` to its row (columns C, F, G); group by column F.
3. Read `BUG_TICKET_LOGS` (create if missing); build the set of `Test
   Case.Key` values already logged. Pick the first group (in workbook row
   order) not yet in that set. If none remain, stop and report the final
   summary (see below).
4. Determine the bug category per the spec's "Determining the bug category"
   section: search `teacher-student-automation` for the test backing this
   Test Case.Key. All matches under `service/tests/` → `BackEnd`; all under
   `client/tests/` → `FrontEnd`. If matches land in both trees or neither,
   this is a blocker (see "Fail loud" above) — stop the run rather than
   guessing a category.
5. **BackEnd items only** (skip for FrontEnd): per the spec's "Finding the
   API name" section, find the Service Object Model method call(s) the
   matching test function makes, trace each to its `def <method>` under
   `service/services/**/*.py`, and read the first line of its docstring
   (`<HTTP METHOD> <path> — ...`) to get the real endpoint. Collect one
   `METHOD path` per distinct endpoint found. If none can be traced this
   way, don't guess — proceed without an API line; this is not a blocker.
6. Fetch the backing Zephyr execution's `comment` (`GET
   https://prod-api.zephyr4jiracloud.com/v2/testexecutions/<Execution.Key>`
   with `ZEPHYR_API_TOKEN`) and convert its STEPS/EXPECTED/ACTUAL HTML into
   the Markdown description per the spec. If the comment is missing or
   doesn't parse into those three sections, treat as a blocker (see "Fail
   loud" above) rather than inventing a reason.
7. Build the Zephyr test case URL: `<ZEPHYR_URL>#/v2/testCase/<Test
   Case.Key>?projectId=10121` per the spec.
8. Run the JQL duplicate check from the spec. If a genuine pre-existing bug
   covers this scenario, follow "Consolidating duplicates" in the spec:
   `getJiraIssue` the existing ticket, append `- [<Test Case.Key> — <Test
   Case.Name>](<zephyr test case URL>) — EXEC:<Execution.Key>` to its
   `**Zephyr Test Cases**` list, extend `customfield_10360` to a
   comma-separated list including this Test Case.Key, `editJiraIssue` with
   the updated description and field (leave everything else on the ticket
   untouched), then log `<Test Case.Key>, EXEC:<Execution.Key>,
   JIRA:<existing key>, PREEXISTING` to `BUG_TICKET_LOGS` and move to the
   next item (step 3). If the `editJiraIssue` call fails, this is a blocker
   (see "Fail loud" above) — don't log the line.
9. Otherwise, create the Bug issue in project `EI`: summary `[BUG]
   [<Category>] <Test Case.Name>` (category from step 4), the Markdown
   description built from steps 5–7 (Reason, then `**API**` line(s) if any
   from step 5, then the `**Zephyr Test Cases**` list with this one bullet),
   `additional_fields` with `customfield_10360` (Test Name = the Test
   Case.Key) and `customfield_10359` (Test Status = FAILED, option id
   `10328`), and `transition: {"id": "8"}` to land directly in "BUG -
   Blocked by Defect".
10. `getJiraIssue` the new key and confirm `fields.status.name` is exactly
    `"BUG - Blocked by Defect"`. If not, call `transitionJiraIssue` with
    `transition: {"id": "8"}` on it and re-check once. If it still isn't in
    that status, this is a blocker — per "Fail loud" above, stop the run
    without logging this item.
11. Append `<Test Case.Key>, EXEC:<Execution.Key>, JIRA:<new Bug ticket key>`
    to `BUG_TICKET_LOGS`, and add the new ticket key to this run's tracked
    list (see "Track every new ticket key" rule above).
12. Go back to step 3 for the next item.

## End of run

Before reporting, if this run's tracked list of new ticket keys is
non-empty, move all of them onto the Board in one batch per the spec's
"Getting the ticket onto the Board, not just into the right status" section
— new tickets land in this project's Backlog regardless of status and won't
appear on the Board tab until moved:

1. Load the `claude-in-chrome` skill and browser tools if not already
   loaded.
2. Navigate to
   `https://softwaretestinghub.atlassian.net/jira/software/projects/EI/boards/121/backlog`.
   This run's new tickets will be ranked contiguously near the bottom of the
   single "Backlog" section (created back-to-back), so scrolling to find
   them is usually enough — no need to search one at a time.
3. Check the checkbox for every tracked key from this run.
4. Right-click any checked row → **Move work item → Board** — this applies
   to the whole selection in one action.
5. Verify: confirm none of the tracked keys still appear in the Backlog
   section (re-search or re-scroll), and close the browser tab when done.

If this move fails partway (e.g. a key can't be found in the Backlog list),
don't leave it unreported — name exactly which keys were and weren't
confirmed moved in the final summary; don't silently assume it worked.

Report a summary: total bug tickets created this run, whether the board
move succeeded (and for which keys, if partial), any `PREEXISTING` skips
(with the existing ticket key), and the item + reason if the run stopped
early on a blocker.
