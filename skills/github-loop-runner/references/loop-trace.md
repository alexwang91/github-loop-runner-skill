# Loop Trace Reference

Use this reference when a GitHub-only runner needs an append-only record of what happened in each autonomous loop.

## Purpose

Loop Trace makes runner decisions observable after the fact. It records which milestone was selected, which context was read, what action was taken, what CI or review signal was observed, which feedback entries were created, and what the runner decided next.

`docs/feedback-log.md` explains why an observation matters. `docs/loop-trace.md` explains what the runner actually did.

## Generated Repo File

When bootstrapping a target repository, generate:

- `docs/loop-trace.md`: append-only trace entries for milestone, review, repair, and stopper events.

## Trace Entry Format

Each meaningful runner event should append one entry:

```yaml
trace:
  id: T-0001
  timestamp: "YYYY-MM-DDTHH:MM:SSZ"
  milestone: M0
  branch: m0-example
  pr: 1
  phase: select_milestone
  context_files_read:
    - docs/progress.md
    - docs/next-steps-plan.md
  actions_taken:
    - "Selected the first TODO milestone from fresh base branch state."
  files_changed: []
  ci_checks: []
  feedback_ids: []
  decision:
    action: continue
    reason: "Milestone has a clear acceptance criterion and CI path."
  next_action: create_branch
  attempt_counts:
    ci_attempts: 0
    fix_attempts: 0
    review_cycles: 0
  elapsed_time_estimate: unknown
```

## Required Events

Append a trace entry when the runner:

- selects a milestone,
- creates or updates a branch,
- opens or updates a PR,
- observes CI, review, mergeability, or stopper output,
- classifies feedback,
- applies a fix after feedback,
- attempts a merge,
- updates progress,
- runs the Review and Renewal Loop,
- runs the Harness Repair Loop,
- creates, validates, invalidates, or rolls back a loop hypothesis,
- stops or marks work blocked.

## Metrics

Trace entries should preserve enough operational metrics for review:

- CI attempts per milestone,
- fix attempts per milestone,
- review cycles,
- merge attempts,
- blocked time when known,
- elapsed time estimate when known,
- repeated feedback type counts,
- repeated harness root-cause layers.

When exact token, call, or time cost is unavailable, record `unknown` instead of inventing a number.

## Runner Rules

1. Treat `docs/progress.md` as the state source; treat `docs/loop-trace.md` as evidence, not state.
2. Append trace entries after meaningful events. Do not rewrite history except to fix malformed trace syntax in the same PR.
3. Link trace entries to feedback IDs when feedback was classified.
4. Do not claim a milestone is complete if no trace entry links the selected milestone, PR, CI result, and progress update.
5. If the runner cannot update `docs/loop-trace.md`, classify a `trace_gap` feedback entry and proceed only if the gap is non-blocking for the current milestone.

## Review Usage

During the Review and Renewal Loop, use `docs/loop-trace.md` to summarize:

- completed milestones since the last review,
- repeated CI or merge attempts,
- repeated feedback types,
- repeated harness root-cause layers,
- missing evidence,
- candidate Harness Repair Loop triggers,
- active hypothesis validation windows.
