# Loop Trace Reference

Use this reference when a GitHub-only runner needs observable decision history across milestone selection, PR work, CI feedback, review, repair, and stopping.

## Purpose

Loop Trace makes runner decisions auditable after the fact. The trace should answer what the runner saw, what it decided, what evidence supported the decision, and what action came next.

Loop Trace does not replace CI, review, or the feedback log. It links those signals together so review and repair loops can diagnose control-loop failures rather than guessing.

## Generated Repo File

Bootstrap should generate `docs/loop-trace.md`.

Recommended starting content:

````markdown
# Loop Trace

This file records observable runner events. Keep entries compact, factual, and evidence-backed.

## Metrics

| Metric | Value | Notes |
| --- | ---: | --- |
| selected_milestone | 0 | Count of milestone selection events. |
| branch_created | 0 | Count of branch creation events. |
| pr_opened | 0 | Count of opened PR events. |
| ci_observed | 0 | Count of CI observation events. |
| feedback_classified | 0 | Count of classified feedback events. |
| merge_attempted | 0 | Count of merge attempts. |
| progress_updated | 0 | Count of progress update events. |
| review_run | 0 | Count of review loop events. |
| harness_repair_run | 0 | Count of harness repair events. |
| hypothesis_updated | 0 | Count of hypothesis validation, invalidation, promotion, or rollback events. |
| stop | 0 | Count of stop events. |

## Events

```yaml
entries: []
```
````

## Trace Entry Format

Append entries in this shape:

```yaml
- id: T-0001
  timestamp: "YYYY-MM-DDTHH:MM:SSZ"
  event: selected_milestone
  milestone: M0
  branch: null
  pr: null
  actor: autonomous-runner
  evidence:
    files:
      - docs/progress.md
    checks: []
    feedback_ids: []
    hypothesis_ids: []
  decision:
    summary: "Selected the first TODO milestone from fresh progress."
    next_action: create_branch
    reason: "M0 is the first unblocked TODO row."
  state_after:
    progress_status: IN_PROGRESS
    blocking_feedback: false
```

Use monotonic identifiers in file order. If an exact timestamp is unavailable, use the best available UTC timestamp from the connector response or PR/check metadata and state that source in `evidence`.

## Required Events

The runner should append a trace entry when it:

- selects a milestone,
- creates a branch,
- opens a PR,
- observes CI,
- classifies feedback,
- attempts merge,
- updates progress,
- runs the Review and Renewal Loop,
- runs the Harness Repair Loop,
- validates, invalidates, promotes, or rolls back a hypothesis,
- stops.

## Metrics

Keep a small metrics table in `docs/loop-trace.md`. Update counts when adding entries. Reviews should use these metrics to detect missing evidence, repeated CI loops, repeated harness repairs, and stop conditions.

Minimum metrics:

| Metric | Meaning |
| --- | --- |
| `selected_milestone` | Number of milestone selection events. |
| `ci_observed` | Number of CI observation events. |
| `feedback_classified` | Number of feedback classifications. |
| `trace_gap` | Number of known missing or inconsistent trace events. |
| `harness_repair_run` | Number of harness repair attempts. |
| `hypothesis_updated` | Number of hypothesis lifecycle changes. |
| `stop` | Number of stop events. |

## Runner Rules

1. Append trace entries as part of the same PR or immediate progress PR whenever repository state changes.
2. Keep entries factual. Do not add speculative root causes to the trace; put root-cause analysis in feedback entries.
3. Link feedback IDs, PR numbers, check names, files, and hypothesis IDs when available.
4. Treat missing trace evidence as `trace_gap` feedback when the runner cannot explain a material decision.
5. Do not merge behavior-changing work when trace, feedback, CI, or review evidence is missing and cannot be repaired safely.
6. Keep trace updates scoped. Do not rewrite old trace entries except to repair malformed structure through a Harness Repair Loop.

## Review Usage

The Review and Renewal Loop should read `docs/loop-trace.md` before renewing the plan. It should summarize:

- coverage for required events,
- missing or inconsistent trace entries,
- repeated CI observation and feedback cycles,
- repeated harness repair cycles,
- active hypothesis outcomes,
- decisions that lack evidence.

A review may add a verification-hardening or harness-repair milestone when trace data shows a specific, verifiable gap. It must not add vague process work only to increase trace volume.
