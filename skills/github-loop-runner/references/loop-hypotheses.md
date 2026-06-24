# Loop Hypotheses Reference

Use this reference when the runner proposes a durable process rule, harness repair, verification-hardening milestone, or plan renewal based on feedback trends.

## Purpose

Loop Hypotheses prevent untested process changes from becoming permanent memory. The runner should treat a new rule or harness repair as a falsifiable hypothesis with evidence, expected outcome, validation window, and rollback condition.

## Generated Repo File

When bootstrapping a target repository, generate:

- `docs/loop-hypotheses.md`: structured records for proposed, active, validated, invalidated, and rolled-back loop hypotheses.

## Hypothesis Entry Format

Each hypothesis should use this structure:

```yaml
hypothesis:
  id: H-0001
  date: "YYYY-MM-DD"
  source_feedback_ids:
    - F-0001
  source_trace_ids:
    - T-0001
  hypothesis: "Short falsifiable statement."
  change_applied: "Specific runner, scaffold, plan, or verification change."
  expected_outcome: "Measurable improvement expected."
  measurement_window: "Next 2 milestone PRs"
  success_criteria:
    - "No repeated scope_violation feedback in the measurement window."
  rollback_condition:
    - "If the same failure repeats twice, revert or revise the change."
  status: proposed
  result: ""
```

Allowed `status` values:

- `proposed`
- `active`
- `validated`
- `invalidated`
- `rolled_back`

## When To Create A Hypothesis

Create or update a hypothesis when the runner:

- adds a verification-hardening milestone,
- changes runner protocol,
- changes feedback taxonomy,
- changes review cadence,
- changes milestone slicing rules,
- applies a Harness Repair Loop decision,
- adds a durable rule based on repeated feedback,
- renews the plan because a feedback trend suggests a process improvement.

Do not create a hypothesis for obvious typo fixes, broken links, malformed Markdown, or one-off clerical corrections.

## Validation Rules

Before a hypothesis can become `validated`, the runner must record:

- the source feedback and trace evidence,
- the change applied,
- the measurement window,
- the observed outcome,
- why the outcome supports the hypothesis.

## Invalidation Rules

Mark a hypothesis `invalidated` when:

- the same failure repeats inside the measurement window,
- the change increases scope violations, weak verification, trace gaps, or merge blockers,
- the change cannot be measured,
- the change conflicts with the stopper policy or state source rules.

## Promotion Rules

Promote a validated hypothesis into durable runner guidance only when:

- the measurement window completed,
- evidence supports the expected outcome,
- the change is specific and non-duplicative,
- no stronger contradictory feedback exists.

## Rollback Rules

Roll back or revise a hypothesis when:

- it is invalidated,
- it creates new blocking feedback,
- it weakens verification,
- it makes progress state ambiguous,
- it requires unavailable tools or credentials.

Rollback should be recorded in `docs/loop-trace.md`, `docs/feedback-log.md`, and `docs/loop-hypotheses.md`.
