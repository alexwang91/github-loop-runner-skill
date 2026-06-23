# Review and Renewal Loop Reference

Use this reference when bootstrapping or continuing a GitHub-only autonomous runner that should not stop simply because the initial plan ran out.

## Purpose

The Review and Renewal Loop is a planning loop that runs above the ordinary milestone execution loop.

The execution loop completes known milestones. The review loop checks whether the plan still matches the product goal, whether completed work created new gaps, and whether new specific milestones should be added before the runner stops.

## Trigger Conditions

Run a review when any of these conditions applies:

- The configured number of milestones has completed since the last review. Default: 3.
- `docs/progress.md` has no remaining `TODO` rows.
- A milestone is blocked or fails CI repeatedly.
- The next planned milestone touches release readiness, deployment readiness, credentials, external providers, data removal, or a trust boundary.
- The user asks for a review, plan renewal, or stop assessment.

## Inputs

Read these sources before renewing the plan:

- `docs/autonomous-runner.md`
- `docs/progress.md`
- `docs/next-steps-plan.md`
- `docs/development-principles.md`
- `docs/stopper-policy.md`
- `docs/loop-review.md`, if it exists
- Recent merged PRs and CI/check results, when the connector exposes them

## Review Steps

1. Summarize completed milestones since the last review.
2. Compare the current repo state against the product goal.
3. Check whether verification remains meaningful.
4. Detect missing tests, missing docs, stale plan items, blocked items, duplicated work, weak acceptance criteria, and architecture drift.
5. Decide whether the plan needs new milestones, reordered milestones, split milestones, blocked milestones, or cancelled milestones.
6. Apply the Stopper Policy.
7. Update `docs/loop-review.md`.
8. Update `docs/next-steps-plan.md` and `docs/progress.md` only when the new work is specific, useful, and verifiable.

## Allowed Plan Updates

The review loop may make these updates:

- Add a new milestone with explicit acceptance criteria.
- Split a large milestone into smaller vertical slices.
- Reorder milestones when dependencies changed.
- Mark a milestone `BLOCKED` with a concrete reason.
- Mark a stale milestone `DEFERRED` or `CANCELLED` with a reason.
- Add a verification-hardening milestone when current checks are too weak.

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

## Decision Values

Each review ends with one decision:

- `continue`: existing TODO work remains valid.
- `continue_with_new_milestones`: the review added new specific work.
- `blocked`: the next safe step needs human input or a missing capability.
- `stop`: no meaningful, non-duplicative, verifiable work remains, or a stopper applies.
