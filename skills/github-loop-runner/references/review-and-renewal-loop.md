# Review and Renewal Loop Reference

Use this reference when bootstrapping or continuing a GitHub-only autonomous runner that should not stop simply because the initial plan ran out.

## Purpose

The Review and Renewal Loop is a planning loop above ordinary milestone execution. It compares completed work, feedback trends, trace coverage, hypotheses, and product goal fit before adding work or stopping.

## Trigger Conditions

Run review when:

- the configured number of milestones has completed,
- `docs/progress.md` has no TODO rows,
- a milestone is blocked or repeatedly fails CI,
- feedback repeats `verification_failure`, `scope_violation`, `weak_verification`, `trace_gap`, `harness_defect`, `merge_blocked`, or `regression`,
- Loop Trace is missing required events or decisions lack evidence,
- an active hypothesis reaches validation or invalidation,
- the next step touches release readiness, deployment readiness, credentials, external providers, data removal, or trust boundaries,
- the user asks for review, plan renewal, or stop assessment.

## Inputs

Read `docs/autonomous-runner.md`, `docs/progress.md`, `docs/next-steps-plan.md`, `docs/development-principles.md`, `docs/feedback-taxonomy.md`, `docs/feedback-log.md`, `docs/loop-trace.md`, `docs/harness-repair-loop.md`, `docs/loop-hypotheses.md`, `docs/stopper-policy.md`, and `docs/loop-review.md` when present.

## Review Steps

1. Summarize completed milestones since the last review.
2. Summarize Feedback Trends Since Last Review.
3. Summarize Loop Trace coverage and missing evidence.
4. Compare repo state against the product goal.
5. Check whether verification and PR evidence remain meaningful.
6. Evaluate active hypotheses and apply Hypothesis-Gated Renewal.
7. Detect missing tests, missing docs, stale plan items, blockers, duplicated work, weak acceptance criteria, architecture drift, harness defects, and inconsistent progress state.
8. Decide whether the plan needs new milestones, split milestones, blocked milestones, cancelled milestones, Harness Repair Loop, or hypothesis validation.
9. Classify the decision with the Feedback Taxonomy.
10. Apply the Stopper Policy.
11. Update `docs/loop-review.md`.
12. Update plan, progress, and hypotheses only when the change is specific, useful, and verifiable.

## Feedback Trends Since Last Review

```markdown
## Feedback Trends Since Last Review

| Feedback type | Count | Notes |
| --- | ---: | --- |
| `verification_failure` | 0 |  |
| `weak_verification` | 0 |  |
| `trace_gap` | 0 |  |
| `harness_defect` | 0 |  |
| `hypothesis_invalidated` | 0 |  |
| `repair_validated` | 0 |  |
| `scope_violation` | 0 |  |
| `merge_blocked` | 0 |  |
| `regression` | 0 |  |
| `success` | 0 |  |
```

## Hypothesis-Gated Renewal

Record proposed durable process changes in `docs/loop-hypotheses.md` until trace, feedback, CI, or review evidence validates them. Invalidate and roll back when evidence contradicts the expected effect.

## Allowed Plan Updates

The review loop may add a specific milestone, split work, reorder work, mark work BLOCKED, DEFERRED, or CANCELLED, add verification hardening, add regression fix work, add Harness Repair Loop work, or add hypothesis validation.

## Forbidden Plan Updates

Do not add vague cleanup, polish, improve quality, maybe refactor, investigate later, placeholder tests, dummy files, trace noise, or permanent harness rules without evidence.

## Harness Repair Loop

Run the Harness Repair Loop before product work when review finds repeated protocol failures, trace gaps, missing PR evidence, inconsistent progress state, or harness defects.

## Decision Values

- `continue`
- `continue_with_new_milestones`
- `blocked`
- `stop`
