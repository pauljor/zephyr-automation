---
description: Create JIRA bug tickets for every remaining failed Zephyr test case via the zephyr-bug-ticket-runner agent
---

Launch the `zephyr-bug-ticket-runner` agent (defined in `.claude/agents/zephyr-bug-ticket-runner.md`) to process every remaining unticketed `FAILED` item from `.claude/tasks/zephyr-bug-tickets.md`, one at a time, until none are left or it hits a blocker.
