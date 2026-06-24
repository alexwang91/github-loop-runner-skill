# Harness Repair Loop Reference

Use this reference when repeated runner-protocol failures show that the autonomous harness needs repair before product work can safely continue.

## Purpose

The Harness Repair Loop makes runner-protocol failures repairable without mixing product feature work into the repair. It handles failures in the operating harness: instructions, state files, feedback rules, trace shape, review rules, stopper rules, PR evidence, CI scaffold, and milestone slicing.

A harness repair is not a product milestone. It is a bounded change to the runner system that must preserve GitHub-only operation, CI verification, progress state, and guardrails.

## Trigger Conditions

Run the Harness Repair Loop when any of these conditions appears:

- repeated `protocol_violation`, `trace_gap`, `weak_verification`, `merge_blocked`, or `harness_defect` feedback,
- missing or malformed `docs/progress.md`, `docs/feedback-log.md`, `docs/loop-trace.md`, or `docs/loop-hypotheses.md`,
- inconsistent status between merged PRs and `docs/progress.md`,
- PRs repeatedly lack evidence required by the template,
- CI scaffold cannot verify the generated repository shape,
- review finds stale or contradictory runner instructions,
- active hypotheses cannot be validated because the harness lacks the needed trace or feedback signal.

## Inputs

Read these before repairing:

- `docs/autonomous-runner.md`
- `docs/progress.md`
- `docs/next-steps-plan.md`
- `docs/development-principles.md`
- `docs/feedback-taxonomy.md`
- `docs/feedback-log.md`
- `docs/loop-trace.md`
- `docs/review-and-renewal-loop.md`
- `docs/loop-hypotheses.md`
- `docs/stopper-policy.md`
- `.github/pull_request_template.md`
- `.github/workflows/verify.yml`
- recent PR metadata, changed files, CI/check results, and review comments when available.

## Repair Scope

Allowed repair scope:

- runner docs,
- feedback taxonomy,
- loop trace format,
- review loop rules,
- stopper policy,
- PR template,
- CI scaffold,
- milestone slicing rules.

## Forbidden Repairs

Forbidden repair scope:

- product feature work,
- unrelated refactors,
- weakened verification,
- deleted tests to get green,
- vague process text with no validation criteria,
- changes that require local clone, local package-manager, or local test execution in GitHub-only mode,
- changes that hide or discard blocking evidence.

## Repair Steps

1. Identify the exact harness failure and cite evidence from feedback, trace, PR, CI, or progress state.
2. Classify the failure with `docs/feedback-taxonomy.md`, using the most specific feedback type and root-cause layer.
3. Decide whether a repair is safe within the allowed repair scope.
4. Plan the smallest repair PR. Keep product code out of the branch unless the CI scaffold requires a minimal fixture that is explicitly part of harness validation.
5. Update only the required harness files.
6. Update `docs/loop-trace.md` with a `harness_repair_run` event.
7. Update `docs/feedback-log.md` with `harness_defect` before repair and `repair_validated` only after evidence passes.
8. Run CI through the PR checks.
9. Merge only after CI is green and PR evidence maps the repair to the original failure.
10. Re-read `docs/progress.md` before returning to product milestones.

## Validation Criteria

A valid harness repair must show:

- the specific failure mode,
- the affected harness files,
- the root-cause layer,
- the validation evidence,
- the preserved GitHub-only and CI-only runner contract,
- no weakened tests, evals, assertions, or acceptance criteria,
- no product feature work mixed into the repair.

## Output

Report:

- repair trigger,
- files changed,
- feedback IDs and trace IDs linked,
- root-cause layer,
- CI/check result,
- whether `repair_validated` was logged,
- next safe runner action.
