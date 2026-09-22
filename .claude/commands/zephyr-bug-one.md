---
description: Create exactly ONE JIRA bug ticket from a failed Zephyr test case, then stop
---

Follow the workflow defined in `.claude/tasks/zephyr-bug-tickets.md` in this repo, but create **only a single bug ticket** on this invocation, then stop. Do not loop over multiple items.

Argument (optional, `$ARGUMENTS`): a `Test Case.Key` (e.g. `EI-T356`) or `Execution.Key` (e.g. `EI-E1033`) to target a specific failed item. If omitted, pick the first unprocessed failed item per step 4 below.

Steps:

1. Read `.claude/tasks/zephyr-bug-tickets.md` for the full spec (env vars, reason extraction, URL format, field mapping, log format).
2. Read `CSV_LOGS` and collect every row logged `FAILED` (first field = `Execution.Key`).
3. Load the workbook at `TEST_DATA_URL` (sheet `TEST_DATA_SHEET`) — binary `.xlsx`, parse with `openpyxl` via a Python script, not `Read`. Map each `FAILED` `Execution.Key` from step 2 to its row (columns C, F, G). Group by column F (`Test Case.Key`) — one bug ticket per distinct test case, not per execution row.
4. Read `BUG_TICKET_LOGS` (create it if it doesn't exist yet) and collect the set of `Test Case.Key` values already logged there.
   - If `$ARGUMENTS` was given: resolve it to a `Test Case.Key` (directly if it looks like `EI-T...`, or via its `Execution.Key`'s row if it looks like `EI-E...`). If that key is already in `BUG_TICKET_LOGS`, report that and stop without creating anything.
   - If no argument: pick the first `Test Case.Key` (in workbook row order) from step 3's groups that is NOT yet in `BUG_TICKET_LOGS`. If none remain, report that everything is already ticketed and stop.
5. Determine the bug category per the spec's "Determining the bug category" section: search `teacher-student-automation` for the test backing this Test Case.Key. All matches under `service/tests/` → `BackEnd`; all under `client/tests/` → `FrontEnd`. If matches land in both trees or neither, stop — this item is unresolvable, report it and don't create a ticket.
6. **BackEnd items only**: per the spec's "Finding the API name" section, find the Service Object Model method call(s) the matching test function makes, trace each to its `def <method>` under `service/services/**/*.py`, and read the first line of its docstring (`<HTTP METHOD> <path> — ...`) to get the real endpoint. Collect one `METHOD path` per distinct endpoint found; if none can be traced this way, don't guess — proceed without an API line. Skip this step entirely for FrontEnd items.
7. Fetch the Zephyr execution's `comment` (`GET https://prod-api.zephyr4jiracloud.com/v2/testexecutions/<Execution.Key>` with `ZEPHYR_API_TOKEN`) for the one execution row backing this test case, and convert its STEPS/EXPECTED/ACTUAL HTML into the Markdown description per the spec.
8. Build the Zephyr test case URL: `<ZEPHYR_URL>#/v2/testCase/<Test Case.Key>?projectId=10121` per the spec.
9. Before creating, run the JQL sanity check from the spec (`project = EI AND issuetype = Bug AND text ~ "..."` on a few words from column G) and eyeball the hits for a pre-existing duplicate not yet in `BUG_TICKET_LOGS`. If a real duplicate exists, follow the spec's "Consolidating duplicates" section instead of creating a new ticket: `getJiraIssue` the existing ticket, append a bullet for this item to its `**Zephyr Test Cases**` list, extend `customfield_10360` to include this Test Case.Key, `editJiraIssue` with the updated description and field, then log it as `PREEXISTING` per the spec and stop.
10. Create the Bug issue in project `EI` per the spec: summary `[BUG] [<Category>] <Test Case.Name>` (category from step 5), the Markdown description built from steps 6–8 (Reason, then `**API**` line(s) if any from step 6, then the `**Zephyr Test Cases**` list with this one bullet), `additional_fields` with `customfield_10360` (Test Name = the Test Case.Key) and `customfield_10359` (Test Status = FAILED, option id `10328`), and `transition: {"id": "8"}` to land directly in "BUG - Blocked by Defect".
11. `getJiraIssue` the new key and confirm `fields.status.name` is exactly `"BUG - Blocked by Defect"`. If not, call `transitionJiraIssue` with `transition: {"id": "8"}` on it and re-check. If it still isn't in that status, report the ticket as created but flag the column placement as unresolved — do not write a `BUG_TICKET_LOGS` line in that case (see spec's "If something doesn't fit").
12. On success, append `<Test Case.Key>, EXEC:<Execution.Key>, JIRA:<new Bug ticket key>` to `BUG_TICKET_LOGS`.
13. **No confirmation needed before creating.** Proceed straight through the JIRA create/transition calls without pausing to ask — report which item (Test Case.Key, Execution.Key, category, API endpoint(s) if any, new ticket key and its URL) was processed in the final summary, after the fact.
14. Stop after this one ticket. Do not automatically continue to the next item — run `/zephyr-bug-one` again for the next one, or `/zephyr-bug-bulk` to process all remaining.
