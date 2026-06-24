# Agent Prompts

These files are handoff prompts for agents that will work on this repository.

Use them when an agent should read the repository first, then implement the harness-observability upgrade in small PR-ready steps.

## Files

| File | Purpose |
| --- | --- |
| `harness-upgrade-plan.md` | Plan for upgrading this skill with loop trace, harness repair, and hypothesis-gated renewal. |
| `start-harness-upgrade.md` | Copy-paste startup prompt for another agent. |

## How To Use

Give the agent `start-harness-upgrade.md` first. It instructs the agent to read the repository files and then follow `harness-upgrade-plan.md`.

The agent should not skip repository reading, validation, or small-step verification.
