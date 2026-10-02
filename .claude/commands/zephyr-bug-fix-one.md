---
description: Fix the defect behind ONE failed Zephyr test case (EI-Txxx / EI-Exxxx), comment Problem/Solution/Remarks on it, mark column J of the gsheet "Bug fixed <date>"
---

Fix the failed Zephyr test case named by `$ARGUMENTS`, then stop. One test case per invocation; never loop.

Usage: `/zephyr-bug-fix-one <EI-XXXX>` — the Zephyr **test case key** (`EI-T356`) or **execution key** (`EI-E1033`).  No argument → ask for one and stop; this command no longer auto-picks.

Read `.claude/tasks/zephyr-bug-fixes.md` for the shared mechanics (Zephyr REST details, "Locating and fixing the code", "Confirming the fix", "Finding the responsible PR/commit"); the steps below are authoritative where they differ. JIRA is not touched by this command at all.

## Steps

1. **Resolve the target.** Parse `test_cases.csv` (`TEST_DATA_URL`, Python `csv`): column B = `Execution.Key`, column F = `Test Case.Key`, column G = name. A test-case key may map to several executions (different cycles) — collect them all; an execution key maps to exactly one row. Not found → report and stop.
2. **Read the current state.** `GET https://prod-api.zephyr4jiracloud.com/v2/testexecutions/<Execution.Key>` (`Authorization: Bearer <ZEPHYR_API_TOKEN>`, token in `.mcp.json`; never the `zephyr-scale` MCP tools) for each execution. `testExecutionStatus.id` `14539939` = Pass, `14539940` = Fail. Keep the existing `comment` — its STEPS/EXPECTED/ACTUAL is the **problem statement**.
   - If an execution is already Pass **and** its comment carries a human's dated reasoning, don't overwrite it and don't re-run it: treat it as already fixed, go to step 6 for the PR citation, and carry on to steps 7–8 (the comment is *added to*, see step 7).
   - If none of them is Fail and none is already-fixed-with-reasoning, re-run the test live first (step 3's reproduce); if it passes, it's "already fixed" too.
3. **Reproduce.** Category comes from where the matching test lives: `teacher-student-automation/service/tests/` = BackEnd (`eruditiontx-services-mvp`), `client/tests/` = FrontEnd (`eruditiontx-client-mvp`). Run that test once, unmodified, against the live QA host (`https://eruditionsolutionsqa.com`) and confirm it fails the way the comment says. Can't find the test or can't tell the category → BLOCKED (see "Blockers").
4. **Fix.** Per the spec's "Locating and fixing the code": read the subproject's own `CLAUDE.md`, trace from the test to the responsible code, make the **minimal** change closing the gap between EXPECTED and ACTUAL. Leave it **uncommitted** and name the file(s) in the summary. If the gap is a deliberate, documented design decision (spec: "When the gap is a deliberate design decision, not a bug"), change nothing — it's a confirmed honest `Fail` that still goes through steps 7–9.
5. **Verify locally (standing rule, set 2026-10-02).** Don't push/deploy to QA to verify. For BackEnd, call the changed service method/route in `eruditiontx-services-mvp` with the DB/Auth mocked (or run its unit tests), once with the fix stashed (must show the original failure) and once with it (must show the expected behavior); for FrontEnd, run the client's own tests/build or the changed component in isolation. That local before/after is the confirmation. Executions already fixed from step 2 need no re-run. Say plainly in **Remarks** that the verification was local and the change is uncommitted/not deployed.
6. **Already fixed?** For executions that passed without a code change from this run, find the responsible commit/PR per the spec ("Finding the responsible PR/commit") — hash, PR link, author, paraphrase. If nothing plausible turns up, say "already passing, cause untraced"; never invent a citation.
7. **Write the result and the comment to Zephyr** — this is the "comment on the test case". For every execution, `PUT /testexecutions/<Execution.Key>` with `{"statusName": "Pass"|"Fail", "comment": "<HTML>"}` where the comment is **raw HTML** (not markdown) with exactly these three sections, after the previous STEPS/EXPECTED/ACTUAL block (keep it; don't discard history):
   ```html
   <p><b>Problem:</b> root cause — what was wrong and why (from the EXPECTED/ACTUAL gap).</p>
   <p><b>Solution:</b> what changed — file(s) and plain-language description; or the PR/commit citation if already fixed; or the design decision it conflicts with.</p>
   <p><b>Remarks:</b> edge cases, follow-ups, uncommitted/needs-review status, related test cases sharing the root cause, any execution still failing.</p>
   <p><i>Fixed &lt;M/D/YYYY&gt;</i></p>
   ```
   Use the real locally-verified result for the status (Pass only if the local before/after confirmed the fix). Re-`GET` and confirm `testExecutionStatus.id` and that `comment` contains `Problem:` before trusting the write (a `200` alone proves nothing). Unconfirmed → BLOCKED for that execution.
8. **Update the Google Sheet, column J.** For each execution whose result is now **Pass** (real, confirmed): run `python gsheet_sync.py --fixed <Execution.Key>` from the repo root (`--dry-run` first). It writes `Bug fixed <M/D/YYYY>` (today, black text on an orange fill) into column J ("FAILED - FIXED - RETESTED") only, leaves column I alone, and reports `verified`. Executions still failing are **not** marked. Needs the web app redeployed at version 4 (orange fill on column J) (`gsheet_webapp.gs`); if the script says it's out of date, tell the user the exact redeploy step and continue — don't block the rest.
9. **Log.** After steps 7–8, append one line per execution to `BUG_FIX_LOGS`: `JIRA:NONE, EXEC:<key>, TESTCASE:<key>, RESULT:PASSED|FAILED`. Append only; this command does not use the log to refuse re-runs (an explicit key means run it).
10. **Summary and stop**: target resolved (test case → executions), category, before/after status per execution, files changed (uncommitted unless approved), PR cited if already fixed, whether column J was written, and any BLOCKED items.

## Blockers

Don't guess past one. If the target can't be resolved, the test or code can't be traced, a Zephyr write doesn't confirm, or the sheet write fails to verify: stop that execution, report exactly what happened, and write **no** `BUG_FIX_LOGS` line for it. A confirmed `Fail` (including the design-decision case) is not a blocker — it still gets the comment (Problem/Solution/Remarks), a `FAILED` log line, and no column J mark.

## No confirmation needed

Zephyr comment/status writes, gsheet column J, and logging proceed straight through once the real result is known. Committing/pushing application code is not part of this command; if the user asks for it later, no `Co-Authored-By: Claude` line.
