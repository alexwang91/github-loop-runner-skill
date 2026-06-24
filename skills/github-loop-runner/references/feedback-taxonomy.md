# Feedback Taxonomy Reference

Use this reference when a GitHub-only runner needs structured observations after PR updates, CI checks, reviews, merge attempts, review-loop decisions, or stopper decisions.

## Purpose

Feedback Taxonomy turns raw observations into a controlled next-action protocol.

The runner should not react to a failed check, review comment, merge blocker, or review-loop result with free-form improvisation. It should classify the observation, record evidence, choose an allowed next action, and avoid forbidden actions.

## Generated Repo Files

When bootstrapping a target repository, generate these files:

- `docs/feedback-taxonomy.md`: the local feedback classification rules.
- `docs/feedback-log.md`: the append-only structured feedback record.

`docs/loop-review.md` should summarize feedback trends since the last review.

## Feedback Sources

- `parser`: the runner action or review output cannot be parsed.
- `protocol`: the runner violated the repo protocol or state rules.
- `git_diff`: the PR diff or changed-file set is out of scope.
- `ci`: CI, test, lint, typecheck, build, or eval results.
- `pr_review`: human or agent review feedback.
- `mergeability`: conflict, required check, required review, or permission status.
- `progress_state`: `docs/progress.md` or equivalent state consistency.
- `loop_trace`: missing, malformed, or contradictory `docs/loop-trace.md` evidence.
- `loop_hypothesis`: validation, invalidation, promotion, or rollback of `docs/loop-hypotheses.md` entries.
- `review_loop`: gaps, risks, or renewal decisions from the Review and Renewal Loop.
- `harness_repair`: decisions from the Harness Repair Loop.
- `stopper_policy`: stop or block decisions from `docs/stopper-policy.md`.

## Feedback Types

| Type | Default severity | Meaning | Default next action |
| --- | --- | --- | --- |
| `invalid_action` | blocking | Runner output is incomplete or cannot be parsed. | Rewrite the action with required fields. |
| `protocol_violation` | blocking | Runner skipped or violated the repo protocol. | Correct the protocol issue. |
| `scope_violation` | blocking | PR changes exceed the current milestone scope. | Reduce scope or split work. |
| `verification_failure` | blocking | CI, test, lint, typecheck, build, or eval failed. | Fix the true cause. |
| `weak_verification` | warning/blocking | Checks pass but do not prove the milestone. | Strengthen verification. |
| `review_failure` | blocking | PR does not satisfy acceptance criteria or review. | Revise the PR. |
| `merge_blocked` | blocking | Merge is blocked by conflict, checks, review, or permission. | Resolve the merge blocker. |
| `blocked_dependency` | blocking | Work needs unavailable access, service setup, or human decision. | Mark blocked. |
| `regression` | blocking | Previously completed work regressed. | Fix regression before new feature work. |
| `trace_gap` | warning/blocking | Required loop evidence is missing, stale, malformed, or contradictory. | Restore trace evidence or classify the gap. |
| `harness_defect` | blocking | Runner protocol, scaffold, CI harness, state handling, or tooling caused or amplified failure. | Run the Harness Repair Loop. |
| `hypothesis_invalidated` | blocking | A process or repair hypothesis failed its measurement window or rollback condition. | Roll back or revise the hypothesis. |
| `repair_validated` | info | A harness repair improved the measured outcome. | Promote or retain the repair. |
| `success` | info | PR merged, CI green, and progress updated. | Continue loop. |
| `no_meaningful_work` | terminal | Review found no useful verifiable work. | Stop with report. |

## Severity Levels

- `info`: record the observation and continue.
- `warning`: continue only if the risk is tracked for the next review.
- `blocking`: do not merge or advance until the feedback is resolved or marked blocked.
- `terminal`: stop the runner and write a final review report.

`weak_verification` is a warning for bootstrap or docs-only work. It is blocking when runtime behavior changed but no meaningful test, eval, build, or review check proves completion.

## Harness Root Cause Layers

Use `root_cause.layer` to classify where the failure primarily belongs:

| Layer | Meaning |
| --- | --- |
| `observation` | The runner lacked or misread evidence, logs, diffs, or CI output. |
| `context` | The runner read stale, missing, excessive, or misleading context. |
| `planning` | The milestone, acceptance criteria, or implementation plan was poorly sliced. |
| `control_loop` | The runner skipped loop steps, review triggers, retries, or stopper rules. |
| `tool_action` | GitHub connector, branch, commit, PR, merge, or file operation failed or was misused. |
| `state_store` | `docs/progress.md`, `docs/feedback-log.md`, `docs/loop-trace.md`, or related state/evidence files became inconsistent. |
| `verification` | CI, tests, evals, or review checks were missing, weak, flaky, or misconfigured. |
| `governance` | Permissions, trust boundaries, credentials, security, or human approval gates blocked safe progress. |
| `product_code` | The product implementation itself caused the failure. |
| `unknown` | Evidence is insufficient to classify the layer. |

Repeated non-`product_code` layers should trigger review for a possible Harness Repair Loop.

## Feedback Entry Format

Each meaningful observation should produce one structured entry in `docs/feedback-log.md`.

```yaml
feedback:
  id: F-0001
  timestamp: "YYYY-MM-DDTHH:MM:SSZ"
  source: ci
  type: verification_failure
  severity: blocking
  milestone: M0
  branch: m0-example
  pr: 1
  summary: "Short factual summary."
  evidence:
    checks: []
    files: []
    review_comments: []
  root_cause:
    layer: verification
    category: unknown
    confidence: low
    explanation: "What the evidence supports."
  allowed_next_actions: []
  forbidden_next_actions: []
  runner_decision:
    action: inspect_failure
    reason: "Why this action is allowed."
```

## Allowed Action Map

| Feedback type | Allowed actions | Forbidden actions |
| --- | --- | --- |
| `invalid_action` | `rewrite_action_with_required_fields` | `open_pr`, `mark_done` |
| `protocol_violation` | `correct_protocol`, `update_progress_consistently` | `merge_pr`, `skip_progress_update` |
| `scope_violation` | `revert_unrelated_changes`, `split_into_new_milestone` | `merge_as_is` |
| `verification_failure` | `inspect_ci_failure`, `fix_true_cause`, `add_missing_in_scope_test`, `mark_blocked_if_dependency_missing` | `weaken_test`, `remove_assertion`, `mark_done` |
| `weak_verification` | `add_stronger_test`, `add_eval`, `add_build_or_lint_check`, `create_verification_hardening_milestone` | `claim_complete_without_evidence` |
| `review_failure` | `revise_pr`, `update_docs_if_required`, `split_scope` | `dismiss_feedback_without_reason` |
| `merge_blocked` | `resolve_conflict`, `wait_for_required_check`, `request_required_review`, `mark_blocked_if_permission_missing` | `bypass_required_check` |
| `blocked_dependency` | `mark_blocked`, `create_mockable_followup`, `request_human_input` | `fake_integration` |
| `regression` | `create_regression_fix_milestone`, `revert_regressing_change`, `add_regression_test` | `continue_new_feature_work` |
| `trace_gap` | `restore_trace_evidence`, `append_corrective_trace_entry`, `run_review_if_evidence_missing`, `mark_blocked_if_trace_required` | `claim_complete_without_trace`, `mark_done` |
| `harness_defect` | `run_harness_repair_loop`, `create_harness_repair_pr`, `link_repair_hypothesis` | `hide_repair_in_feature_pr`, `continue_feature_work_without_repair` |
| `hypothesis_invalidated` | `roll_back_hypothesis`, `revise_hypothesis`, `run_harness_repair_loop`, `stop_if_no_safe_rollback` | `promote_hypothesis`, `ignore_failed_measurement` |
| `repair_validated` | `promote_repair_guidance`, `record_validated_hypothesis`, `continue_loop` | `remove_successful_repair_without_reason` |
| `success` | `mark_done`, `update_feedback_log`, `continue_loop`, `check_review_due` | none |
| `no_meaningful_work` | `stop_with_loop_review` | `create_vague_cleanup`, `create_placeholder_milestone` |

## Runner Rules

1. Classify feedback after each PR update, CI result, review result, merge attempt, review-loop decision, or stopper decision.
2. Include `root_cause.layer` before choosing next actions. Use `unknown` only when evidence is insufficient.
3. Append the structured entry to `docs/feedback-log.md` when the repository has that file.
4. Do not continue past `blocking` feedback unless the next action resolves that feedback or marks the milestone blocked with evidence.
5. Do not continue past `terminal` feedback.
6. Do not weaken tests, assertions, evals, or acceptance criteria to convert failure into success.
7. During the Review and Renewal Loop, summarize feedback trends and harness root-cause layers since the last review before adding new milestones.
8. Repeated non-`product_code` root-cause layers should trigger the Harness Repair Loop.
9. New milestones created from feedback must be specific, useful, non-duplicative, and verifiable.

## Feedback Log Template

Generated `docs/feedback-log.md` should start with:

````markdown
# Feedback Log

This file records structured observations from the autonomous runner.

## Entries

```yaml
entries: []
```
````
