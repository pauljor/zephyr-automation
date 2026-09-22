# Task: Create JIRA bug tickets from failed Zephyr test cases

## Purpose

Turn genuine test failures already recorded by the [[zephyr-jira-sync]] task into
real JIRA bug tickets on the same board (`JIRA_URL`, project `EI`, board 121),
so failures don't just sit as a `FAILED` line in `CSV_LOGS` — they become
actionable defects.

A "failed item" is any row in `CSV_LOGS` logged with status `FAILED` (see
`zephyr-jira-sync.md` → "Log format"). `BLOCKED` rows are **not** in scope —
those are process failures (ambiguous match, API error), not confirmed
product bugs.

Every bug ticket created by this task:
- Is issue type **Bug** in project **EI**.
- Contains the **same failure reason** that's on the Zephyr execution's
  `comment` field (the STEPS/EXPECTED/ACTUAL record left by the sync task).
- **Links the Zephyr test case** (a real, clickable URL to the test case
  inside the Zephyr Essential panel, not just the bare key).
- Lands in the **"BUG - Blocked by Defect"** column on the board.

## Env vars used (from `.env` at repo root)

| Var | Meaning |
|---|---|
| `TEST_DATA_URL` | The Zephyr execution export workbook (binary `.xlsx`) — same file the sync task reads. See "Loading `TEST_DATA_URL`" in `zephyr-jira-sync.md`. |
| `TEST_DATA_SHEET` | Worksheet name inside `TEST_DATA_URL` (`All Assignments_List`). |
| `CSV_LOGS` | The sync task's log (`csv_logs.txt`) — this is where `FAILED` rows are found. This task never writes to `CSV_LOGS`; it only reads it. |
| `JIRA_URL` | The board bug tickets get created against (project `EI`, board 121). |
| `ZEPHYR_URL` | Base URL of the Zephyr Essential panel inside Jira — used to build the test case deep link (see "Zephyr test case URL" below). |
| `BUG_TICKET_LOGS` | **New** — local log file (`bug_tickets_log.txt`, same folder as `CSV_LOGS`) this task appends to, one line per bug ticket created. Not present in `.env` before 2026-09-22; add it if missing: `BUG_TICKET_LOGS=<repo>\zephyr-automation\bug_tickets_log.txt`. |

## Finding the failed items

1. Read `CSV_LOGS`. Collect every line whose status field is exactly `FAILED`
   — first field is the `Execution.Key` (column B), e.g. `EI-E1033, FAILED,
   JIRA:NONE`.
2. Load the workbook (`TEST_DATA_URL` / `TEST_DATA_SHEET`) the same way
   `zephyr-jira-sync.md` does (binary `.xlsx`, parse with `openpyxl` via a
   Python script, don't `Read` it as text). Build a lookup from column B
   (`Execution.Key`) to the full row, so each `FAILED` key from step 1 maps to
   its `Test Cycle.Key` (C), `Test Case.Key` (F), and `Test Case.Name` (G).
3. **Dedupe by Test Case.Key (column F), not by Execution.Key.** The same
   test case can be executed more than once across cycles — if two `FAILED`
   rows share the same column F value, they're the same underlying defect and
   must produce exactly **one** bug ticket, not two. Group the `FAILED` rows
   from step 1 by column F before deciding what still needs a ticket.

## Getting the failure reason from the Zephyr execution

The reason lives on the Zephyr execution's `comment` field — the same
STEPS/EXPECTED/ACTUAL HTML record the sync task wrote (see
`zephyr-jira-sync.md` → "Recording the automation"). Fetch it with:

```
GET https://prod-api.zephyr4jiracloud.com/v2/testexecutions/<Execution.Key>
Authorization: Bearer <ZEPHYR_API_TOKEN>
```

(Same token, same base URL, same "no MCP tool works for Zephyr Essential"
caveat as the sync task — see `zephyr-jira-sync.md` → "Zephyr Essential API".)

The response's `comment` field is raw HTML with three sections in order:
`<p><strong>STEPS</strong></p><ol>...</ol>`, `<p><strong>EXPECTED</strong></p>
<ul>...</ul>`, `<p><strong>ACTUAL</strong></p><ul>...</ul>` (the last `<li>`
under ACTUAL is the plain-language explanation of what actually went wrong —
this is "the reason"). Convert this HTML to Markdown for the bug description
(the JIRA `createJiraIssue` tool accepts Markdown and turns it into real ADF
formatting):
- `<p><strong>X</strong></p>` → `**X**` on its own line
- `<ol><li>...</li></ol>` → numbered list (`1. ...`, `2. ...`)
- `<ul><li>...</li></ul>` → bulleted list (`- ...`)
- Strip any remaining tags verbatim; don't invent content that isn't in the
  comment.

Carry over **all three sections**, not just ACTUAL — STEPS and EXPECTED give
the ticket the same context a human reading the Zephyr execution would have.
If the execution has no comment, or the comment doesn't parse into these
three sections, stop and treat that item as unresolvable (see "If something
doesn't fit" below) rather than inventing a reason.

## Determining the bug category (FrontEnd vs BackEnd)

The summary's second bracket (see "Creating the bug ticket" below) names
where the bug lives. Don't guess this from the wording of column G — resolve
it from the automated test that actually produced the `FAILED` result, the
same way `zephyr-jira-sync.md` already draws this line for that repo:
`teacher-student-automation/service/tests/` is backend/API coverage,
`teacher-student-automation/client/tests/` is frontend/UI coverage
(Playwright, Page Object Model).

1. Search `teacher-student-automation` for a test file referencing this
   item's `Test Case.Key` (e.g. `EI-T356`) or, if the key alone doesn't hit,
   a couple of distinctive keywords from column G.
2. If every match found is under `service/tests/` → category = `BackEnd`.
3. If every match found is under `client/tests/` → category = `FrontEnd`.
4. If matches turn up in **both** trees, or in **neither** — don't guess.
   Treat this one item as unresolvable (see "If something doesn't fit"
   below): report the item and skip it rather than picking a category with
   no real signal behind it.

This lookup will almost always succeed cleanly here: a `FAILED` row only
exists because the sync task already ran a real test for it, so the test
file is expected to exist in exactly one of the two trees.

## Finding the API name (BackEnd items only)

A `BackEnd` bug ticket also names the underlying API endpoint(s) the
scenario exercises, so triage doesn't have to go spelunking through the
automation repo to find it. Skip this section entirely for `FrontEnd` items.

1. In the `service/tests/` file found above, locate the specific test
   function matching this item (same match used to confirm the category —
   its docstring or name lines up with column G).
2. Within that test function's body, find the Service Object Model method
   call(s) it makes on a `*Service` instance — e.g. `student.grade_average(...)`,
   `teacher.report_violation(...)`. These are the calls that actually hit the
   backend; ignore fixture/setup helper calls that aren't part of the
   scenario under test.
3. For each distinct method name found, locate its definition under
   `service/services/**/*.py` (`def <method_name>(...)`) and read the first
   line of its docstring. This repo's own convention documents every service
   method as `"""<HTTP METHOD> <path> — <description>"""` (e.g. `"""GET
   /v1/student/assignment/{class_code}/grade/average/fetch — the student's
   average grade..."""`). Take just the `<HTTP METHOD> <path>` portion —
   don't paraphrase or shorten the path.
4. If the test calls more than one endpoint (e.g. a setup call plus the call
   actually under test), list every distinct one found in step 2/3 — don't
   assume only one is "the" endpoint.
5. If a method call can't be traced to a docstring following the `METHOD
   path — ...` convention (e.g. the test calls `requests`/an HTTP client
   directly instead of a Service Object Model method), don't guess a path —
   omit the `**API**` line entirely for that ticket rather than putting an
   unconfirmed endpoint on it. Unlike an unresolved category, this is not a
   blocker for the rest of the ticket.

## The Zephyr test case URL

Confirmed by opening a real test case in the browser (not guessed): clicking
a test case inside the Zephyr Essential panel produces a URL of the form

```
<ZEPHYR_URL>#/v2/testCase/<Test Case.Key>?projectId=<projectId>
```

e.g. for `EI-T356`:
```
https://softwaretestinghub.atlassian.net/jira/software/projects/EI/apps/628ce3d4-ed20-4ac9-91aa-6c6ab21a770a/1f1570b7-1896-4331-a997-66cd076264f1#/v2/testCase/EI-T356?projectId=10121
```

`projectId` is the Jira **numeric** project id for `EI`, not the project key
— confirmed as `10121` at time of writing (from
`getJiraProjectIssueTypesMetadata`/`getVisibleJiraProjects`). If this task is
ever pointed at a different project, re-derive `projectId` the same way
rather than assuming `10121`, and re-confirm the URL pattern still holds by
opening one real test case in the browser (`claude-in-chrome`) the same way
this was first confirmed — don't guess a different deep-link shape without
checking.

## Creating the bug ticket

Project `EI`, issue type **Bug**. Use `createJiraIssue`
(`mcp__claude_ai_Atlassian_Rovo__createJiraIssue` or the `Atlassian`
equivalent) with `cloudId: "softwaretestinghub.atlassian.net"`.

- **`summary`**: `[BUG] [<Category>] <Test Case.Name>` — the first bracket
  is always literally `[BUG]`; the second is `[FrontEnd]` or `[BackEnd]` per
  "Determining the bug category" above; then column G verbatim. e.g. `[BUG]
  [BackEnd] Fetching a class average grade with a malformed class code is
  rejected`. Don't add any further tags (role, severity, area) beyond these
  two brackets — column G already carries the scenario description.
- **`description`** (Markdown), in this order:
  1. `**Reason**` heading, then the STEPS/EXPECTED/ACTUAL content converted
     from the Zephyr comment per above.
  2. **BackEnd items only**: an `**API**` line per distinct endpoint found in
     "Finding the API name" above, e.g. `**API**: `GET
     /v1/student/assignment/{class_code}/grade/average/fetch`` (backtick-code
     the `METHOD path`, one line per endpoint if there's more than one).
     Omit this entirely for `FrontEnd` items, and omit it for a `BackEnd`
     item where the endpoint couldn't be resolved (see step 5 there).
  3. A `**Zephyr Test Case**` line: `[<Test Case.Key> — <Test Case.Name>](<zephyr test case URL>)`.
  4. A `**Zephyr Execution**` line with the raw `Execution.Key` (e.g.
     `EI-E1033`) for traceability back to `CSV_LOGS` — plain text, not a
     link (executions have no confirmed deep-link URL, unlike test cases).
- **`additional_fields`**: `{"customfield_10360": "<Test Case.Key>"}` — this
  is the **required** "Test Name" field on this project's Bug issue type
  (confirmed via `getJiraIssueTypeMetaWithFields`; every other field on the
  create screen is optional). Using the Zephyr key here is this task's own
  convention for traceability, not an existing documented standard — if a
  human reviewer says this field should hold something else, update this
  spec rather than silently diverging per-ticket. Also set
  `"customfield_10359": {"id": "10328"}` (the "Test Status" field's `FAILED`
  option) since it's directly relevant and already exists on this issue
  type.
- **`transition`**: `{"id": "8"}` — the global workflow transition straight
  to status **"BUG - Blocked by Defect"** (status id `10697`), confirmed via
  `getTransitionsForJiraIssue` against multiple existing Bug issues in this
  project (it's marked `isGlobal: true`, available from every status, so it
  should apply immediately on creation). This is what places the ticket on
  the board's "BUG - Blocked by Defect" column.

**Verify the column placement.** Right after creation, `getJiraIssue` the new
key and confirm `fields.status.name` is exactly `"BUG - Blocked by Defect"`.
If it isn't (the `transition` param during creation is a newer/less-proven
path than a normal post-creation transition), call `transitionJiraIssue` with
`transition: {"id": "8"}` on the new issue directly, then re-`getJiraIssue`
to confirm. If it still isn't in that status after the explicit transition,
don't force it further — log the ticket as created but flag the column
placement as unresolved (see "If something doesn't fit" below).

## Recording what was done (`BUG_TICKET_LOGS`)

Append one line per bug ticket successfully created (not overwritten), space
after each comma, labeled fields in this order:

```
<Test Case.Key>, EXEC:<Execution.Key>, JIRA:<new Bug ticket key>
```

e.g. `EI-T356, EXEC:EI-E1033, JIRA:EI-3455`. If a test case had more than one
`FAILED` execution row (see dedupe above), the log line still lists only the
one execution key that triggered the ticket — that's enough to trace back
into `CSV_LOGS`/the workbook. This mirrors the labeled-field style
`CSV_LOGS` already uses (`<key>, <STATUS>, JIRA:<ticket key>`).

**Idempotency**: before creating a ticket for a Test Case.Key, check whether
it already appears as the first field of a line in `BUG_TICKET_LOGS` — if so,
skip it, a ticket already exists. This is the same idempotency pattern
`CSV_LOGS` uses for the sync task.

Also do a quick JQL sanity check before creating
(`project = EI AND issuetype = Bug AND text ~ "<a few distinctive words from
column G>"`) and eyeball the hits — `BUG_TICKET_LOGS` is the authoritative
record for *this task's own* idempotency, but a bug for the same scenario
could already exist from manual triage outside this task entirely. If a
clearly-matching bug ticket already exists and isn't in `BUG_TICKET_LOGS`,
don't create a duplicate — log it as `<Test Case.Key>, EXEC:<Execution.Key>,
JIRA:<existing key>, PREEXISTING` and move on.

## If something doesn't fit

Don't guess past a blocker. If the Zephyr execution has no usable comment, the
bug category can't be resolved to exactly one of FrontEnd/BackEnd (see
"Determining the bug category" above), the JIRA create call errors, the
required custom field rejects the value, or the column-placement verification
never succeeds — stop processing that one item, report exactly what happened
(Test Case.Key, Execution.Key, what failed), and do **not** write a
`BUG_TICKET_LOGS` line for it (so a later run retries it rather than silently
skipping it forever).

## Notes

- This task only reads `CSV_LOGS` — it never mutates the Zephyr execution or
  re-runs anything from `zephyr-jira-sync.md`. It's a downstream step: sync
  first (to get real `FAILED` results), then this task turns those into
  tickets.
- Test cases in this Jira site are Zephyr Essential (Zephyr Squad Cloud)
  entities, not Jira issues — there is no native Jira issue link between a
  Bug and a test case (`createIssueLink` only links two Jira issues). The
  Markdown link in the description is the only linking mechanism used here.
