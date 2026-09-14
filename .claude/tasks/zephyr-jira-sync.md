# Task: Sync my Zephyr test cases with JIRA (auto-execute or mark automated)

## Purpose
Go through the Zephyr execution export CSV, find the rows that belong to me ("Paul"),
and for each one either:
- confirm it already has a JIRA ticket and record that on the Zephyr execution, or
- run the Zephyr test case myself and record the result on the Zephyr execution.

Every row's durable record now lives entirely on the Zephyr execution's
`comment` field — as of 2026-09-14 this task no longer comments on or
transitions the JIRA issue itself; JIRA is read-only (JQL search + `getJiraIssue`
only, to find the ticket key).

Every row processed gets logged to `CSV_LOGS` with a real automation status
(`PASSED`, `FAILED`, `SKIPPED`, `BLOCKED`) — see "Log format" below.

## Env vars used (from `.env` at repo root)
| Var | Meaning |
|---|---|
| `CSV_DATA_URL` | Local path to the Zephyr execution CSV (currently: `zeyphyr-automation/Zephr List of Assignments_2026_09-report - Sheet0.csv`) |
| `JIRA_URL` | The JIRA board to check/move tickets on (project `EI`, board 121) |
| `ZEPHYR_URL` | Human-facing link to the Zephyr Essential app inside Jira. **Not an API endpoint** — do not call it directly. See "Zephyr Essential API" below for the real base URL. |
| `CSV_LOGS` | Local log file to append processed rows to (`csv_logs.txt`) |
| `ZEPHYR_API_TOKEN` | Bearer token for the real Zephyr Essential REST API. Currently stored in `.mcp.json` (env for the now-unused `zephyr-scale` MCP entry — see note below). Generate a fresh one via Jira profile picture → **"Zephyr Essential API keys"** if it's missing/expired. |

## CSV column map (`CSV_DATA_URL`)
The file currently has 7 columns, no header row alias needed — use these positions:

| Col | Header | Meaning |
|---|---|---|
| A | `Jira.Project` | JIRA project key (e.g. `EI`) |
| B | `Execution.Key` | Zephyr execution id (e.g. `EI-E782`) — **this is what gets copied into the log** |
| C | `Test Cycle.Key` | Zephyr test cycle id |
| D | *(blank)* | unused |
| E | `Test Cycle.Name` | Test cycle name |
| F | `Test Case.Key` | Zephyr test case ticket number (e.g. `EI-T124`) — the one to execute in Zephyr |
| G | `Test Case.Name` | Test case scenario description — used to check for an existing JIRA ticket |

> Note: this CSV has no assignee/owner column. "My rows" are found by a plain
> case-insensitive substring search for `Paul` across **all cells in the row**, not
> a specific column. If the CSV format changes to add an assignee column, prefer
> matching on that column instead.

## Zephyr Essential API (read this before automating any Zephyr call)

Learned the hard way during the first real run of this task — read this before
reaching for an MCP tool or guessing at field names.

- **No MCP server works with Zephyr Essential.** Not the community
  `mcp-zephyr-scale` npm package, not SmartBear's own official `@smartbear/mcp`
  (local or remote `https://zephyr.mcp.smartbear.com/mcp`). SmartBear's own docs
  say outright: *"Zephyr MCP client is available on Zephyr Standard and Advanced
  plans only. Zephyr Essential is not supported."* This Jira site uses **Zephyr
  Essential** (confirmed via the token-generator page being titled "Zephyr
  Essential API keys" / "Zephyr Essential API Access Tokens"), not Zephyr Scale —
  don't waste time re-trying MCP tools named `zephyr-scale`/`zephyr-*`; call the
  REST API directly instead (`curl` via Bash, or `requests` in a Python test).
- **Base URL**: `https://prod-api.zephyr4jiracloud.com/v2` — NOT
  `api.zephyrscale.smartbear.com` (that's the Zephyr Scale API and will reject
  any Zephyr Essential token with `401 {"error":"Invalid JWT"}` no matter how
  many times you regenerate it — the two products are different backends
  entirely, even though a generic-looking SmartBear "Zephyr" doc page can make
  them look interchangeable).
- **Auth**: header `Authorization: Bearer <ZEPHYR_API_TOKEN>`. Generate the
  token in Jira: profile picture (top right) → **"Zephyr Essential API keys"**
  (NOT "Zephyr Scale API Access Tokens" — visually similar page, wrong product).
- **Full API reference**: the real OpenAPI/Swagger spec is published at
  `https://api.swaggerhub.com/apis/smartbear-public/zephyr-squad-cloud-api/2.9`
  and is fetchable directly as raw JSON with `curl` — no login, no JS
  rendering. This is far faster than the human-facing docs portal at
  `developer.smartbear.com/zephyr-squad/...`, which is a login-gated,
  JS-rendered SPA that plain `curl`/`WebFetch` cannot read (needs a real
  browser or the Claude in Chrome extension). Pull the spec first for any new
  Zephyr endpoint need — grep `spec.paths` for the resource, then
  `spec.components.schemas.<SchemaName>` for the exact body shape, rather than
  guessing field names against live data.
- **Key endpoints actually used by this task**:
  - `GET /testcases/{key}` — test case detail (column F, e.g. `EI-T2`).
  - `GET /testexecutions/{key}` — execution detail (column B, e.g. `EI-E1537`);
    `testExecutionStatus.id` in the response tells you the current status.
  - `PUT /testexecutions/{key}` — **the only way to record a result or leave a
    note.** Body is `{"statusName": "Pass" | "Fail", "comment": "<why>"}` when
    recording a real test run. **The field is `statusName` (a plain string) —
    NOT `status`, `statusId`, `testExecutionStatusId`, or
    `testExecutionStatus`.** Those all silently return `HTTP 200` and do
    nothing (the API accepts unknown fields without error and just no-ops
    them), so a green status code is not proof the write worked — always
    re-`GET` after a `PUT` and confirm `testExecutionStatus.id` actually
    changed before trusting a status write.
    For the "already automated" case (see "If a matching JIRA ticket is
    found" below), send `{"comment": "..."}` with **no `statusName`** — the
    execution's Pass/Fail status is left alone since no test was actually
    run. This comment-only shape hasn't been exercised by a real run yet:
    re-`GET` after the `PUT` and confirm the `comment` field itself actually
    changed. If it didn't (or the API 400s without `statusName` present),
    don't guess at a workaround — treat the row as `BLOCKED` and report it,
    same as any other unconfirmed write.
  - `GET /statuses?projectKey=EI` — look up status IDs/names if needed (e.g.
    `Pass` = id `14539939`, `Fail` = id `14539940` at time of writing — but
    prefer sending `statusName` as a string over hardcoding IDs since IDs are
    project-specific).
  - **There is no "add comment" endpoint for test cases, and no
    attachment/file-upload endpoint at all** (confirmed against the full
    API spec — only weblinks, issue links, and text test-steps exist on a
    test case). Comments only exist on test *executions* — see "Recording
    the automation" below for how that single comment field is used to
    carry the full record, not just the Pass/Fail note.

## Recording the automation

Every processed row gets recorded as a comment on the Zephyr execution — the
same `PUT /testexecutions/<column B>` call, just with a different `comment`
body depending on which branch fired:

- **Matching JIRA ticket found**: a short one-line "already automated" note
  naming the ticket (see "If a matching JIRA ticket is found" below) — sent
  with **no `statusName`**, since no test was actually run.
- **No matching JIRA ticket**: the fuller STEPS/EXPECTED/ACTUAL comment below,
  sent together with `statusName: "Pass"|"Fail"` from the real test run.

This is not a separate step/API call in either case: Zephyr Essential has no
comment endpoint for test cases and no attachment endpoint anywhere, so the
execution's `comment` field is the only real place a durable, human-readable
record can live — and (as of 2026-09-14) this task no longer comments on or
transitions the JIRA issue itself, so this is now the *only* record of either
outcome, not just a supplement to a JIRA-side comment.

**The `comment` field is raw HTML, not markdown.** The Zephyr Squad Swagger
schema documents it as a plain string (`"Comment": {"type": "string", ...}`),
and the app's own comment editor is an HTML-based rich-text widget — it
renders `<p>`/`<b>`/`<ol>`/`<ul>`/`<li>`/`<code>` tags properly, but a plain
string containing markdown syntax (`**bold**`, backtick spans, `\n` line
breaks) gets inserted as one literal, unformatted text run: the markdown
characters show up literally and all line breaks collapse to a single space
(confirmed by testing — see `comment-format.txt` at the repo root for the
target look, and the git history of this file for the markdown attempt that
produced a flattened wall of text instead).

**When a matching JIRA ticket is found**, the comment is a single short line,
no STEPS/EXPECTED/ACTUAL sections:

```html
<p>JIRA <code>&lt;ticket key&gt;</code> Already Automated</p>
```

e.g. `<p>JIRA <code>EI-3435</code> Already Automated</p>` — this branch never
ran a test, it's just recording that another ticket already covers the
scenario.

**When no matching JIRA ticket is found**, the `comment` body must cover
exactly these three sections, in order, as literal HTML (no line
breaks/indentation needed in the JSON string — it's rendered, not read as
source):

```html
<p><b>STEPS</b></p>
<ol>
<li><first action the automation takes, wrap literal values in code tags></li>
<li><next action></li>
...
</ol>
<p><b>EXPECTED</b></p>
<ul>
<li><first expected outcome, from column G / the test's own intent></li>
<li><next expected outcome></li>
...
</ul>
<p><b>ACTUAL</b></p>
<ul>
<li>Test: <code>&lt;test file name&gt;</code></li>
<li>Result: <b>PASSED</b> or <b>FAILED</b></li>
<li><code>&lt;pytest one-line summary, e.g. "1 passed in 4.90s"&gt;</code></li>
<li><what actually happened when it ran just now - status codes, key
    response values, which assertions passed or failed, one bullet each></li>
</ul>
```

Wrap identifiers, filenames, and literal values (endpoints, status codes,
field names, test file names) in `<code>` tags, and bold the PASSED/FAILED
result with `<b>` — otherwise keep it plain ASCII prose inside the `<li>`/`<p>`
text. A comment containing `::`, curly braces, or an em dash has triggered a
`400 "Invalid Payload"` from this API before (see "Zephyr Essential API"
above) — none of those appear in the HTML template above, so it's safe. Pull
STEPS from the test's own docstring/body rather than re-deriving them, and
ACTUAL from the just-completed run's real output (status codes, assertion
results) — not from what you expect it to say.

## Steps

1. **Load the CSV** from `CSV_DATA_URL`.
2. **Filter to my rows**: keep only rows where the string `Paul` (case-insensitive)
   appears anywhere in the row's cells.
3. For each matching row, **check column G** (Test Case.Name) against the JIRA
   board at `JIRA_URL`:
   - Run a JQL search scoped to the board's project (e.g. `project = EI`) for an
     issue whose summary matches or closely contains the column G text. The
     Atlassian Rovo MCP tools work fine for this — `searchJiraIssuesUsingJql`
     and `getJiraIssue` are the only two needed now (this task is read-only
     against JIRA as of 2026-09-14; see below) — pass the Jira site hostname
     (e.g. `softwaretestinghub.atlassian.net`) as `cloudId`, no lookup needed.
     A `text ~ "..."` or `summary ~ "..."` JQL query is a reasonable starting
     point, but review hits manually — it can return loosely related tickets
     (bugs/tasks that merely share a few keywords) rather than a real match
     for the scenario.
   - **If a matching JIRA ticket is found** (ticket already exists):
     a. Record it on the **Zephyr execution**, not the JIRA issue: `PUT
        https://prod-api.zephyr4jiracloud.com/v2/testexecutions/<column B>`
        with body `{"comment": "<p>JIRA <code>&lt;ticket key&gt;</code>
        Already Automated</p>"}` (see "Recording the automation" above) — e.g.
        `<p>JIRA <code>EI-3435</code> Already Automated</p>`. No `statusName`
        in this call (no test was run, so the execution's status is left
        as-is), and no comment or transition on the JIRA issue itself — this
        task doesn't mutate JIRA at all anymore, only reads from it to get
        the ticket key.
     b. Re-`GET` the execution and confirm the `comment` field actually
        changed before trusting the write (same rule as every other Zephyr
        `PUT` — a `200` isn't proof). If it didn't take, treat the row as
        `BLOCKED` (see below) rather than logging a comment that isn't really
        there.
     c. Append to `CSV_LOGS`: `<column B value>, SKIPPED, JIRA:<ticket key>`
        (e.g. `EI-E1600, SKIPPED, JIRA:EI-3435`) — `SKIPPED` because the Zephyr
        execution itself was never run (the existing ticket is the coverage);
        the third field records which ticket was found, so the log itself
        shows at a glance which rows already had JIRA coverage vs. which
        needed a fresh test.
   - **If no matching JIRA ticket is found**:
     a. Check whether an automated test already covers this exact scenario in
        `teacher-student-automation` (`service/tests/` for API behavior,
        `client/tests/` for UI behavior) — search by keywords from column G,
        not just the ticket/test-case id (Zephyr test case ids like `EI-T2`
        don't map to file names in that repo).
     a2. **Before writing a new test, check `CSV_LOGS` to avoid duplicating one
        that already exists.** The same Test Case.Key (column F) can appear
        across multiple rows/executions (e.g. re-run in a later test cycle) —
        cross-reference the Execution.Keys already logged (any status) in `CSV_LOGS`
        back against the CSV to see if any of them share this row's column F
        value. If one does, a test was very likely already authored for it
        during that earlier row (check the comment left on its Zephyr
        execution, or just re-search the automation repo for column F's key
        alongside column G's keywords) — reuse/re-run that existing test for
        this row's result rather than authoring a second one.
     b. **If no automated test exists (neither found in-repo nor via a prior
        `CSV_LOGS` row for the same column F), write one** rather than guessing at a
        result or doing this by hand: follow that repo's own conventions (see
        `teacher-student-automation/CLAUDE.md` — Service Object Model for
        `service/`, Page Object Model for `client/`; add any missing endpoint
        to `config/endpoints.py` and service method rather than hardcoding a
        URL in the test). This is a real coverage gap-fill, not throwaway
        script — commit-worthy.
     c. **Run it for real** against the automation suite's default target,
        `https://eruditionsolutionsqa.com` (live QA host, from the repo's root
        `.env` `API_BASE_URL`) — this is reachable and has real data/DB access.
        Avoid spinning up the **local** `eruditiontx-services-mvp` backend
        against the **production** MongoDB host for this (`DB_HOST` in that
        repo's `.env`) unless you've confirmed the environment you're in can
        actually reach it — a sandboxed/CI-like environment may get its
        connection forcibly reset (IP not allowlisted on the DB side), which
        surfaces as a confusing `beanie.exceptions.CollectionWasNotInitialized`
        / `500` on login rather than an obvious network error.
     d. Record the actual Pass/Fail result **and** the structured record on
        the Zephyr execution in one call: `PUT
        https://prod-api.zephyr4jiracloud.com/v2/testexecutions/<column B>`
        with body `{"statusName": "Pass"|"Fail", "comment": "<STEPS/EXPECTED/
        ACTUAL, per "Recording the automation" above>"}`. Re-`GET` to
        confirm `testExecutionStatus.id` actually changed (compare against
        `GET /statuses?projectKey=EI`: `Pass` = id `14539939`, `Fail` = id
        `14539940` at time of writing) — if it did **not** change, the write
        silently no-op'd; treat this row as `BLOCKED` (see below) rather than
        logging a result you haven't actually confirmed.
     e. Append to `CSV_LOGS`: `<column B value>, PASSED, JIRA:NONE` or
        `<column B value>, FAILED, JIRA:NONE` — whichever the confirmed
        `testExecutionStatus` actually is. A `FAILED` row is a genuine bug
        find, not a process error: log it and move on to the next row, don't
        treat it as blocked. The third field (`JIRA:NONE`) records that no
        JIRA ticket existed for this scenario (as opposed to the `JIRA:<key>`
        case above), so the log itself shows at a glance which rows required
        writing/running a test.
   - **If the row can't be resolved automatically** (JQL search returns more
     than one plausible match with no clear winner, no transition looks like
     an obvious "Done" target, a JIRA/Zephyr API call errors out, or a Zephyr
     `PUT` doesn't actually take per 3d above): append
     `<column B value>, BLOCKED, REASON:<short description>` to `CSV_LOGS`
     (e.g. `EI-E1700, BLOCKED, REASON:ambiguous JQL match EI-3401/EI-3402`),
     then stop the run and report the row for manual review. Don't guess past
     a blocker — a `BLOCKED` row stays logged as-is (not silently retried by a
     later run) until a human resolves it and updates/removes that log line.
4. Continue until all matching rows are processed.

## Log format (`CSV_LOGS`)
One line per processed row, appended (not overwritten), with a space after
each comma:
```
<Execution.Key from column B>, <STATUS>, <JIRA:<ticket key>|JIRA:NONE|REASON:<short reason>>
```
Older rows may carry a 4th field (`TESTCASE:<key>`/`TESTCASE:FAILED`) from a
prior process version that attached a separate GIF capture to the test case
via weblink — that mechanism is retired (see "Recording the automation"
above; the structured record now lives in the execution's own `comment`
field, set in the same `PUT` as the Pass/Fail status). Don't add the 4th
field to new rows; its absence isn't a sign anything went wrong.

`<STATUS>` is the real automation outcome, one of:
- **`PASSED`** — a test was run for real against the live QA host and Zephyr
  confirmed a Pass (`testExecutionStatus.id` = `14539939`, re-`GET`-verified).
- **`FAILED`** — same, but Zephyr confirmed a Fail (id `14539940`). This
  records a genuine product bug, not a process failure — it's a normal,
  expected outcome of this task, not something to "fix" by re-guessing.
- **`SKIPPED`** — an existing JIRA ticket already covered the scenario; the
  ticket was closed instead of running anything, so the Zephyr execution
  itself was left untouched.
- **`BLOCKED`** — the row couldn't be resolved automatically (ambiguous JIRA
  match, no obvious "Done" transition, an API error, or a Zephyr `PUT` that
  didn't actually change status on re-`GET`). Logged so a later run doesn't
  silently retry it, but it needs a human to resolve and then update/remove
  the line.
- **`NOT EXECUTED`** — not produced by the live workflow; reserved for
  historical rows (logged before this status convention existed) that were
  re-verified and found to still be sitting at Zephyr's own native default
  status ("Not Executed", id `14539937`) with no real result to record. A
  fresh row that would hit this should be logged `BLOCKED` instead, so it
  gets a human's attention rather than sitting silently unexecuted.

The third field:
- `JIRA:<ticket key>` (e.g. `JIRA:EI-3435`) pairs with `SKIPPED` — the ticket
  that was found and closed.
- `JIRA:NONE` pairs with `PASSED`/`FAILED`/`NOT EXECUTED` — no ticket existed,
  so a test was written/reused/run instead.
- `REASON:<short description>` pairs with `BLOCKED` — a one-line note on why
  the row couldn't be resolved.

**Idempotency**: a row counts as already processed if its column-B value
appears anywhere in `CSV_LOGS`, regardless of status — `BLOCKED` included.

Rows logged under the old two-field convention (`<key>,DONE,JIRA:...`, no
distinct status) predate this convention (migrated 2026-09-13 — see git
history for the exact backfill: `JIRA:<key>` rows became `SKIPPED`,
`JIRA:NONE` rows were re-verified against Zephyr's real
`testExecutionStatus` and became `PASSED`/`FAILED` accordingly).

## Resolved (previously "open items to confirm")

- **JQL matching**: a `text ~ "..."` / `summary ~ "..."` JQL query on `project =
  EI` works and is a fine starting point — but always eyeball the hits, since
  it happily returns tangentially-related tickets on shared keywords rather
  than a genuine match.
- **Recording Zephyr Passed/Failed**: confirmed — `PUT
  .../testexecutions/{key}` with `{"statusName": "Pass"|"Fail"}` (see "Zephyr
  Essential API" section above). A `comment` in the same body is also applied
  and shows up on the execution.
- **JIRA mutations retired (2026-09-14)**: this task no longer comments on or
  transitions the JIRA issue when a match is found (see "If a matching JIRA
  ticket is found" above) — the "Done" lane/transition question this bullet
  used to track no longer applies. JIRA is read-only for this task now (JQL
  search + `getJiraIssue` only); the durable record moved entirely to the
  Zephyr execution's `comment` field.

## Note on `.mcp.json`
The repo-root `.mcp.json` currently has a `zephyr-scale` MCP server entry
(`mcp-zephyr-scale` npm package) with a `ZEPHYR_API_TOKEN` env var. That MCP
server only ever talks to the Zephyr **Scale** API and cannot work against this
Jira site's Zephyr **Essential** instance no matter what token is put there —
it's kept only because `ZEPHYR_API_TOKEN` is a convenient place the real token
currently lives; the MCP tools it exposes should not be used for this task.
Prefer calling the real API directly (`curl`/`requests` against
`https://prod-api.zephyr4jiracloud.com/v2`) using that same token value.
