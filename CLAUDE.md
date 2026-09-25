# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is **not a coding project in itself** — there is no build/lint/test command for this
repo directly. It's a Claude Code task/agent workflow whose job is to keep Zephyr Essential
test executions (in Jira project `EI`, board 121) in sync with JIRA, turn genuine test
failures into JIRA bug tickets, and fix those bugs in the actual application repos. All
behavior is defined by markdown specs under `.claude/tasks/`, invoked via slash commands and
agents — read the relevant spec in full before doing anything Zephyr/JIRA-related here; this
file only orients you to which spec to read and how the pieces fit together.

This repo is one of four independent sibling projects under the `teacher-student/` workspace
root (see the root `CLAUDE.md`). It cross-references `teacher-student-automation` — when a
row needs a fresh test, one gets written/run there following that repo's own conventions
(Service Object Model for `service/`, Page Object Model for `client/`).

## The three tasks

| Task | Spec | Commands | Agent (bulk) |
|---|---|---|---|
| Sync Zephyr executions with JIRA | `.claude/tasks/zephyr-jira-sync.md` | `/zephyr-sync-one` (one row), `/zephyr-sync-all` | `zephyr-jira-sync-runner` |
| Turn `FAILED` rows into JIRA bug tickets | `.claude/tasks/zephyr-bug-tickets.md` | `/zephyr-bug-one [key]` (one ticket), `/zephyr-bug-bulk` | `zephyr-bug-ticket-runner` |
| Fix a bug ticket's underlying defect | `.claude/tasks/zephyr-bug-fixes.md` | `/zephyr-bug-fix-one [key]` (via `BUG_TICKET_LOGS`), `/zephyr-bug-fix-mine [key]` (via JIRA: status `"BUG - Blocked by Defect"` + assignee = me) | *(none yet)* |

Each task is downstream of the one before it: bug-ticket creation only *reads* `CSV_LOGS`
(never mutates it or re-runs anything from the sync spec) and only acts on rows the sync
task already logged as `FAILED`; bug-fixing only *reads* `BUG_TICKET_LOGS` and only acts on
tickets that task already created. Run them in order: sync → bug-ticket → bug-fix.

The bug-fix task is the odd one out — the other two are pure JIRA/Zephyr bookkeeping, but
this one actually edits application source in `eruditiontx-client-mvp`/
`eruditiontx-services-mvp`, leaves the change uncommitted for review, then re-runs the real
test and records whatever the honest result is (even if the fix didn't fully take).

Both bulk agents (sync and bug-ticket) process **one row/item at a time, never in
parallel** — that constraint is in the agent definitions themselves (`.claude/agents/*.md`),
not just the spec prose. The bug-fix task has no bulk agent yet — it's single-item only for
now, via either of its two entry points: `/zephyr-bug-fix-one` (walks `BUG_TICKET_LOGS`) or
`/zephyr-bug-fix-mine` (walks the JIRA board directly, so it also catches bug tickets that
landed in "BUG - Blocked by Defect" some other way — e.g. created by hand). Both share the
same close-out logic (`zephyr-bug-fixes.md`, "Reading the ticket" onward) and the same
`BUG_FIX_LOGS` idempotency; only how the target ticket gets picked differs.

## Key facts that matter across all three tasks

- **Source data**: `test_cases.xlsx` (binary Excel, `TEST_DATA_URL`/`TEST_DATA_SHEET` env
  vars, sheet `All Assignments_List`). Never `Read` it as text — load it via a short Python
  + `openpyxl` script through Bash. Column D (assignee) header exports blank but holds real
  names; "my rows" means column D exactly `Paul` (case-insensitive).
- **Zephyr Essential has no MCP support.** Neither the community `mcp-zephyr-scale` package
  nor SmartBear's official one works against this Jira site (it's Zephyr Essential, not
  Zephyr Scale/Standard/Advanced). Call the real REST API directly instead:
  `https://prod-api.zephyr4jiracloud.com/v2`, `Authorization: Bearer <ZEPHYR_API_TOKEN>`.
  The `zephyr-scale` MCP entry in `.mcp.json` exists only as a place the token happens to
  live — its tools don't work here and shouldn't be called.
- **A `200` from a Zephyr `PUT` is not proof of a write.** The API silently no-ops unknown
  fields. Always re-`GET` after any `PUT /testexecutions/{key}` and confirm the field you
  changed actually changed before trusting it or logging a result.
- **Three append-only local logs**, all idempotency sources (a row/item counts as done if
  its key appears anywhere in the file, any status/result):
  - `CSV_LOGS` (`csv_logs.txt`) — one line per sync-task row: `<Execution.Key>, <STATUS>, <JIRA:key|JIRA:NONE|REASON:...>`.
  - `BUG_TICKET_LOGS` (`bug_tickets_log.txt`) — one line per bug ticket created: `<Test Case.Key>, EXEC:<key>, JIRA:<new key>[, PREEXISTING]`.
  - `BUG_FIX_LOGS` (`bug_fixes_log.txt`) — one line per execution re-run as part of a fix: `JIRA:<bug ticket key>, EXEC:<key>, TESTCASE:<key>, RESULT:PASSED|FAILED`.
  Never overwrite these files; only append.
- **JIRA is read-only for the sync task** (JQL search + `getJiraIssue` only) — it records
  everything on the Zephyr execution's `comment` field instead, which is **raw HTML, not
  markdown** (a literal `**bold**`/backtick/`\n` string renders as one flattened text run).
  The bug-ticket task is the one that actually creates/mutates JIRA issues.
- **Board placement is independent of status.** A newly created bug ticket can have the
  exactly correct workflow status and still be invisible on the board until manually moved
  from Backlog → Board via the browser (`claude-in-chrome`) — there's no confirmed API for
  this move; see "Getting the ticket onto the Board" in `zephyr-bug-tickets.md`.
- All three tasks stop and log a `BLOCKED`/unresolved item rather than guessing past
  ambiguity (ambiguous JQL match, unconfirmed write, unresolvable FrontEnd/BackEnd category,
  a code fix that can't be traced or re-confirmed, etc.) — never silently retry or paper over
  a blocker.

Don't take any of the above as a substitute for the specs themselves — env var names, exact
request/response shapes, HTML comment templates, and field IDs are documented there in full
and are easy to get subtly wrong from a summary.
