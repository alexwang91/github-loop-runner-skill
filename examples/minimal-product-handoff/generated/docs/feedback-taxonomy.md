# Feedback Taxonomy

## Feedback Sources

parser, protocol, git_diff, ci, pr_review, mergeability, progress_state, loop_trace, review_loop, harness_repair, loop_hypothesis, stopper_policy.

## Feedback Types

verification_failure, weak_verification, trace_gap, harness_defect, review_failure, merge_blocked, regression, success, no_meaningful_work.

## Severity Levels

info, warning, blocking, terminal.

## Root-Cause Layers

observation, context, planning, control_loop, tool_action, state_store, verification, governance, product_code, unknown.

## Runner Rules

Classify meaningful observations before deciding the next action.
