# Stopper Policy Reference

Use this reference to prevent an autonomous loop from creating low-value work or moving beyond the safe operating scope of the plan.

## Purpose

The runner should continue only while there is specific, useful, non-duplicative, verifiable work. It should stop when continuing would require missing access, weak verification, major scope expansion, or human product judgment.

## Hard Stoppers

When a hard stopper applies, stop and report the reason instead of adding more work.

- The GitHub connector cannot read or write the repository.
- CI cannot verify the work and no approved verification channel exists.
- A milestone needs sensitive access or live service setup that the runner does not have.
- A milestone changes a security boundary without explicit approval.
- The same CI failure remains after the configured fix attempts and the root cause is outside the current milestone.
- A merged milestone regresses and the runner cannot isolate a safe fix.
- The next step would perform a high-impact operation that the current plan did not approve.

## Soft Stoppers

When a soft stopper applies, run the Review and Renewal Loop once before stopping.

- No `TODO` rows remain.
- The review loop finds no meaningful new work.
- The configured maximum review cycles has been reached.
- The configured maximum PR or milestone count has been reached.
- The product goal appears satisfied.
- Remaining work is duplicated, vague, or unverifiable.

## Default Limits

Recommended defaults for generated repositories:

```yaml
stopper_policy:
  max_review_cycles: 5
  max_total_milestones: 30
  max_total_prs: 30
  stop_when_no_meaningful_new_work: true
  max_fix_attempts_per_milestone: 3
  max_ci_reruns_per_failure: 1
```

Generated repositories may change these values in `docs/stopper-policy.md`, but they should keep explicit limits.

## Stopper Report

When the runner stops, write or update `docs/loop-review.md` with:

- stopper reason
- completed work summary
- remaining blocked work
- unresolved human decisions
- safe next actions

Stopping is a valid successful outcome when no safe, useful, verifiable work remains.
