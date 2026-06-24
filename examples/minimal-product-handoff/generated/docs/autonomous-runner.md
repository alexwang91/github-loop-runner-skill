# Autonomous Runner Protocol

Goal: move each `docs/progress.md` row to DONE through one CI-verified PR into `main` after the Handoff Decision has selected the development mode.

## Handoff Decision

Read `docs/handoff-decision.md` before product work.

## Long-Run Growth Mode

Read `docs/long-run-growth-loop.md` before selecting work. Report merged PR count, TODO backlog count, growth review due, deep review due, and final review eligibility.

## Soft Check

Use the GitHub connector and CI. Do not rely on local repository commands for verification.

## Autonomous Loop

1. Fetch progress, feedback log, loop trace, handoff decision, long-run growth policy, loop hypotheses, and stopper policy.
2. Confirm development mode.
3. Apply Long-Run Growth Mode.
4. Select the first TODO row.
5. Open one PR.
6. Use CI as VERIFY.
7. Update progress, feedback, trace, and hypotheses.
8. Re-fetch progress.

## Guardrails

One milestone, one PR. Keep evidence current. Do not weaken acceptance criteria.

## Stop Conditions

Use `docs/stopper-policy.md` and `docs/long-run-growth-loop.md` together.
