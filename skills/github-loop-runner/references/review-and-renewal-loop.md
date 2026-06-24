# Review and Renewal Loop Reference

Use this reference when bootstrapping or continuing a GitHub-only autonomous runner that should not stop simply because the initial plan ran out.

## Purpose

The Review and Renewal Loop is a planning loop that runs above the ordinary milestone execution loop.

The execution loop completes known milestones and records structured feedback plus loop trace evidence. The review loop checks whether the plan still matches the product goal, whether completed work created new gaps, whether feedback trends reveal repeated failure modes, whether active hypotheses were validated or invalidated, whether harness repair is needed, and whether new specific milestones should be added before the runner stops.

## Trigger Conditions

Run a review when any of these conditions applies:

- The configured number of milestones has completed since the last review. Default: 3.
- `docs/progress.md` has no remaining `TODO` rows.
- A milestone is blocked or fails CI repeatedly.
- Feedback shows repeated `verification_failure`, `scope_violation`, `weak_verification`, `merge_blocked`, or `regression` entries.
- Feedback shows repeated `trace_gap`, `harness_defect`, or `hypothesis_invalidated` entries.
- Loop trace shows repeated attempts, missing evidence, or repeated non-`product_code` root-cause layers.
- The next planned milestone touches release readiness, deployment readiness, credentials, external providers, data removal, or a trust boundary.
- The user asks for a review, plan renewal, or stop assessment.

## Inputs

Read these sources before renewing the plan:

- `docs/autonomous-runner.md`
- `docs/progress.md`
- `docs/next-steps-plan.md`
- `docs/development-principles.md`
- `docs/feedback-taxonomy.md`
- `docs/feedback-log.md`, if it exists
- `docs/loop-trace.md`, if it exists
- `docs/harness-repair-loop.md`, if it exists
- `docs/loop-hypotheses.md`, if it exists
- `docs/stopper-policy.md`
- `docs/loop-review.md`, if it exists
- Recent merged PRs and CI/check results, when the connector exposes them

## Review Steps

1. Summarize completed milestones since the last review.
2. Summarize feedback trends since the last review, including repeated failures, blockers, weak verification, trace gaps, harness defects, regressions, and successful patterns.
3. Summarize Loop Trace Summary evidence: selected milestones, PRs, CI attempts, fix attempts, merge attempts, missing evidence, and repeated root-cause layers.
4. Evaluate Hypothesis Results Since Last Review: validate, invalidate, promote, roll back, or keep active each hypothesis whose measurement window has evidence.
5. Identify Harness Repair Candidates before adding feature milestones.
6. Compare the current repo state against the product goal.
7. Check whether verification remains meaningful.
8. Detect missing tests, missing docs, stale plan items, blocked items, duplicated work, weak acceptance criteria, and architecture drift.
9. Decide whether the plan needs new milestones, reordered milestones, split milestones, blocked milestones, cancelled milestones, verification hardening, or harness repair.
10. Classify the review decision with the Feedback Taxonomy.
11. Apply the Stopper Policy.
12. Update `docs/loop-review.md`.
13. Update `docs/next-steps-plan.md`, `docs/progress.md`, and `docs/loop-hypotheses.md` only when the new work is specific, useful, measurable, and verifiable.

## Feedback Trend Summary

Each review should include a section like this:

```markdown
## Feedback Trends Since Last Review

| Feedback type | Count | Notes |
| --- | ---: | --- |
| `verification_failure` | 0 |  |
| `weak_verification` | 0 |  |
| `scope_violation` | 0 |  |
| `merge_blocked` | 0 |  |
| `regression` | 0 |  |
| `success` | 0 |  |
| `trace_gap` | 0 |  |
| `harness_defect` | 0 |  |
| `hypothesis_invalidated` | 0 |  |
```

## Loop Trace Summary

Each review should include a section like this:

```markdown
## Loop Trace Summary

| Metric | Value | Notes |
| --- | ---: | --- |
| Milestone PRs reviewed | 0 |  |
| CI attempts | 0 |  |
| Fix attempts | 0 |  |
| Merge attempts | 0 |  |
| Missing trace evidence | 0 |  |
| Repeated non-product root-cause layers | 0 |  |
```

## Hypothesis Results Since Last Review

Each review should evaluate active hypotheses:

```markdown
## Hypothesis Results Since Last Review

| Hypothesis | Status | Evidence | Decision |
| --- | --- | --- | --- |
| H-0001 | active |  | keep_active |
```

## Harness Repair Candidates

Before adding feature milestones, decide whether failures should repair the harness:

```markdown
## Harness Repair Candidates

| Candidate | Evidence | Root-cause layer | Decision |
| --- | --- | --- | --- |
|  |  | unknown | repair_not_needed |
```

Use feedback trends to choose plan updates. For example:

- Repeated `verification_failure` may justify splitting the milestone or adding an in-scope test fixture.
- Repeated `weak_verification` may justify a verification-hardening milestone.
- Repeated `scope_violation` may justify smaller milestone slices.
- Repeated `trace_gap` may justify strengthening trace requirements or PR evidence.
- Repeated `harness_defect` should trigger the Harness Repair Loop before more feature work.
- `hypothesis_invalidated` should trigger rollback, revision, harness repair, or stopper assessment.
- A `regression` should block new feature work until fixed.
- `no_meaningful_work` should trigger the Stopper Policy.

## Allowed Plan Updates

The review loop may make these updates:

- Add a new milestone with explicit acceptance criteria.
- Split a large milestone into smaller vertical slices.
- Reorder milestones when dependencies changed.
- Mark a milestone `BLOCKED` with a concrete reason.
- Mark a stale milestone `DEFERRED` or `CANCELLED` with a reason.
- Add a verification-hardening milestone when current checks are too weak.
- Add a regression-fix milestone when feedback shows completed work regressed.
- Add a harness-repair milestone or PR when repeated evidence points to the runner protocol, state handling, CI scaffold, PR template, or loop rules.
- Create, validate, invalidate, promote, or roll back loop hypotheses.

## Forbidden Plan Updates

Do not create work whose only purpose is to keep the loop running. Do not add vague tasks such as:

- cleanup
- polish
- improve quality
- maybe refactor
- investigate later
- add placeholder tests
- add dummy files
- rewrite without measurable value

Every renewed milestone must have observable acceptance criteria and a clear verification path.

Durable process changes must be hypothesis-gated. Record the source evidence, expected outcome, measurement window, success criteria, and rollback condition in `docs/loop-hypotheses.md` unless the change only fixes a malformed reference or typo.

## Decision Values

Each review ends with one decision:

- `continue`: existing TODO work remains valid.
- `continue_with_new_milestones`: the review added new specific work.
- `blocked`: the next safe step needs human input or a missing capability.
- `stop`: no meaningful, non-duplicative, verifiable work remains, or a stopper applies.
