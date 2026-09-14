---
description: Run the full Zephyr/JIRA sync across all remaining rows via the zephyr-jira-sync-runner agent
---

Launch the `zephyr-jira-sync-runner` agent (defined in `.claude/agents/zephyr-jira-sync-runner.md`) to process every remaining unprocessed row from `.claude/tasks/zephyr-jira-sync.md`, one row at a time, until none are left or it hits a blocker.
