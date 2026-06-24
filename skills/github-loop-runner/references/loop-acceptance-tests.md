# Loop Acceptance Tests Reference

Use this reference to define tests for the runner loop itself.

## Purpose

A generated repository should verify that its runner harness exists and that key loop invariants are represented. These tests are not product tests. They are harness acceptance checks.

## Generated Repo File

Generate `docs/loop-acceptance-tests.md`.

## Acceptance Checks

The generated repo should be able to check:

- bootstrap created required runner files,
- handoff decision exists before product work,
- external-agent prompt can be produced from repo state,
- long-run growth policy exists,
- progress has at least one TODO milestone,
- feedback log exists,
- loop trace contains required event names,
- PR template asks for evidence, trace, feedback, judge, localization, memory, and long-run policy,
- workflow checks required runner files,
- no final review is eligible before long-run policy allows it.

## Example Check List

```yaml
loop_acceptance:
  required_files: true
  handoff_present: true
  long_run_policy_present: true
  progress_has_todo: true
  feedback_log_present: true
  loop_trace_events_present: true
  pr_template_has_evidence_gates: true
  workflow_checks_runner_files: true
```

## Rules

1. Loop acceptance checks should run in CI when practical.
2. Failure means the generated harness is incomplete.
3. Fix harness acceptance failures before product milestone work.
