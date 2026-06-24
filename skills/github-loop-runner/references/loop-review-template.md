# Loop Review Template

Use this template for generated `docs/loop-review.md` files.

```markdown
# Loop Review

## Review Metadata

- Review ID:
- Date:
- Trigger:
- Base branch:
- Completed milestones since last review:
- Latest reviewed PR or commit:

## Completed Work Summary

-

## Feedback Trends Since Last Review

| Feedback type | Count | Notes |
| --- | ---: | --- |
| `verification_failure` | 0 |  |
| `weak_verification` | 0 |  |
| `trace_gap` | 0 |  |
| `harness_defect` | 0 |  |
| `hypothesis_invalidated` | 0 |  |
| `repair_validated` | 0 |  |
| `scope_violation` | 0 |  |
| `merge_blocked` | 0 |  |
| `regression` | 0 |  |
| `blocked_dependency` | 0 |  |
| `success` | 0 |  |

## Trace Coverage

| Required event | Present | Notes |
| --- | :---: | --- |
| selected_milestone |  |  |
| branch_created |  |  |
| pr_opened |  |  |
| ci_observed |  |  |
| feedback_classified |  |  |
| merge_attempted |  |  |
| progress_updated |  |  |
| review_run |  |  |
| harness_repair_run |  |  |
| hypothesis_updated |  |  |
| stop |  |  |

## Current State Assessment

- Product goal alignment:
- Verification health:
- Trace health:
- Plan freshness:
- Known blockers:

## Harness Repair Assessment

- Repair needed: no
- Trigger evidence:
- Root-cause layer:
- Repair scope:
- Validation criteria:

## Hypothesis Assessment

| Hypothesis | Status | Evidence | Decision |
| --- | --- | --- | --- |
|  |  |  |  |

## Feedback Decision

- Feedback type:
- Severity:
- Root-cause layer:
- Chosen next action:
- Reason:

## Stopper Assessment

- Hard stopper applies: no
- Soft stopper applies: no
- Reason:

## Decision

Choose one:

- continue
- continue_with_new_milestones
- blocked
- stop
```
