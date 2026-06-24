# Harness Repair Loop Reference

Use this reference when repeated failures point to the runner protocol, scaffold, checks, or control loop rather than only product code.

## Purpose

The Harness Repair Loop repairs the system that runs the work. It should keep product feature work separate from protocol fixes so the runner does not hide process failures inside feature PRs.

The execution loop builds product milestones. The Review and Renewal Loop updates plans. The Harness Repair Loop changes the harness only when evidence shows the runner protocol, generated docs, CI scaffold, PR template, feedback taxonomy, or state handling caused or amplified failure.

## Generated Repo File

When bootstrapping a target repository, generate:

- `docs/harness-repair-loop.md`: local rules for diagnosing and repairing harness defects.

## Trigger Conditions

Run the Harness Repair Loop when any of these conditions applies:

- two or more `trace_gap` entries,
- two or more `protocol_violation` entries,
- two or more `scope_violation` entries,
- repeated `weak_verification`,
- repeated `merge_blocked` caused by process, branch, or CI scaffold issues,
- inconsistent `docs/progress.md` state,
- missing or stale runner docs,
- review finds a repeated harness-layer root cause,
- a loop hypothesis about process behavior is invalidated.

## Inputs

Read these sources before proposing a repair:

- `docs/autonomous-runner.md`
- `docs/progress.md`
- `docs/next-steps-plan.md`
- `docs/feedback-taxonomy.md`
- `docs/feedback-log.md`
- `docs/loop-trace.md`
- `docs/review-and-renewal-loop.md`
- `docs/loop-hypotheses.md`, if it exists
- `docs/stopper-policy.md`
- recent PRs and CI/check results, when available through the connector

## Repair Scope

Allowed harness repairs include:

- runner docs,
- feedback taxonomy,
- loop trace format,
- review loop rules,
- stopper policy,
- PR template,
- CI scaffold,
- milestone slicing rules,
- generated plan templates,
- wording that prevents repeated protocol ambiguity.

## Forbidden Repairs

Do not include:

- product feature work,
- unrelated refactors,
- weakened verification,
- removed assertions or tests to get green,
- vague process text without validation criteria,
- dummy files or placeholder checks,
- changes that make `docs/progress.md` stop being the state source.

## Repair Steps

1. Identify the repeated failure pattern from feedback and trace evidence.
2. Classify the root cause layer with the Feedback Taxonomy.
3. Decide whether the issue is a harness defect or product-code defect.
4. If it is a harness defect, create or update a loop hypothesis describing the expected improvement.
5. Write the smallest repair that changes only harness files.
6. Open a dedicated harness repair PR when possible.
7. Verify the repair with CI and with the specific validation criterion from the hypothesis.
8. Record the result in `docs/loop-trace.md`, `docs/feedback-log.md`, and `docs/loop-hypotheses.md`.

## Validation Criteria

A harness repair is valid only when it has:

- evidence linking the repeated failure to a harness layer,
- a scoped change that does not include product feature work,
- a CI or review signal proving the harness files remain valid,
- a measurement window for the next loop events,
- a rollback condition if the repair does not improve the observed failure pattern.

## Output

The Harness Repair Loop should end with one decision:

- `repair_applied`: a scoped repair PR was merged or proposed,
- `repair_not_needed`: evidence points to product code or one-off failure,
- `blocked`: repair needs human decision or unavailable capability,
- `stop`: the harness cannot be repaired safely inside the current operating scope.
