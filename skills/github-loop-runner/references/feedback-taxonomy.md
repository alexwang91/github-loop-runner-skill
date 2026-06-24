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
- `review_loop`: gaps, risks, or renewal decisions from the Review and Renewal Loop.
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
| `success` | info | PR merged, CI green, and progress updated. | Continue loop. |
| `no_meaningful_work` | terminal | Review found no useful verifiable work. | Stop with report. |

## Severity Levels

- `info`: record the observation and continue.
- `warning`: continue only if the risk is tracked for the next review.
- `blocking`: do not merge or advance until the feedback is resolved or marked blocked.
- `terminal`: stop the runner and write a final review report.

`weak_verification` is a warning for bootstrap or docs-only work. It is blocking when runtime behavior changed but no meaningful test, eval, build, or review check proves completion.

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
| `success` | `mark_done`, `update_feedback_log`, `continue_loop`, `check_review_due` | none |
| `no_meaningful_work` | `stop_with_loop_review` | `create_vague_cleanup`, `create_placeholder_milestone` |

## Runner Rules

1. Classify feedback after each PR update, CI result, review result, merge attempt, review-loop decision, or stopper decision.
2. Append the structured entry to `docs/feedback-log.md` when the repository has that file.
3. Do not continue past `blocking` feedback unless the next action resolves that feedback or marks the milestone blocked with evidence.
4. Do not continue past `terminal` feedback.
5. Do not weaken tests, assertions, evals, or acceptance criteria to convert failure into success.
6. During the Review and Renewal Loop, summarize feedback trends since the last review before adding new milestones.
7. New milestones created from feedback must be specific, useful, non-duplicative, and verifiable.

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
