# Loop Hypotheses Reference

Use this reference when the runner wants to change its operating process, review policy, verification strategy, or repair rule based on evidence rather than permanent speculation.

## Purpose

Hypothesis-Gated Renewal prevents permanent process changes from being added without evidence. The review loop may propose a change, but the runner should track it as a hypothesis until trace, feedback, CI, or review evidence validates it.

## Generated Repo File

Bootstrap should generate `docs/loop-hypotheses.md`.

Recommended starting content:

````markdown
# Loop Hypotheses

This file records temporary process hypotheses created by the Review and Renewal Loop or Harness Repair Loop.

## Entries

```yaml
entries: []
```
````

## Hypothesis Entry Format

Use this structure:

```yaml
- id: H-0001
  status: active
  created_at: "YYYY-MM-DDTHH:MM:SSZ"
  source: review_loop
  summary: "Short process hypothesis."
  expected_effect: "What should improve if the hypothesis is true."
  evidence_required:
    trace_events: []
    feedback_types: []
    ci_checks: []
    review_signals: []
  validation_rule: "Specific condition that promotes this hypothesis."
  invalidation_rule: "Specific condition that invalidates this hypothesis."
  rollback_rule: "Safe rollback if invalidated."
  linked_trace_ids: []
  linked_feedback_ids: []
  decision_history: []
```

Status values:

- `active`
- `validated`
- `invalidated`
- `promoted`
- `rolled_back`

## When To Create A Hypothesis

Create a hypothesis when review or repair proposes:

- a new milestone slicing rule,
- a stronger PR evidence requirement,
- a new trace event or metric,
- a change to review cadence,
- a CI scaffold change intended to improve runner reliability,
- a change in feedback classification rules,
- a process guardrail that should become permanent only after evidence.

Do not create hypotheses for ordinary product features, one-off fixes, or vague process preferences.

## Validation Rules

A hypothesis may become `validated` only when the evidence requirement is met. Use trace entries, feedback log entries, CI results, PR review signals, or loop-review conclusions. State the exact evidence before changing status.

## Invalidation Rules

A hypothesis becomes `invalidated` when its invalidation rule fires, when evidence contradicts the expected effect, or when it creates repeated harness defects. Classify the result as `hypothesis_invalidated` in the feedback log.

## Promotion Rules

Promote a hypothesis into durable runner docs only after it is validated and the promotion has a specific target file, acceptance criteria, and CI/review evidence. Record the promotion in `docs/loop-trace.md`.

## Rollback Rules

Every active hypothesis needs a rollback rule before it affects runner behavior. Roll back or mark blocked when the hypothesis is invalidated and the runner can safely restore the prior behavior. Stop when an invalidated active hypothesis has no safe rollback path.
