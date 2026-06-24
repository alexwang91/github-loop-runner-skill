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
| `scope_violation` | 0 |  |
| `merge_blocked` | 0 |  |
| `regression` | 0 |  |
| `blocked_dependency` | 0 |  |
| `trace_gap` | 0 |  |
| `harness_defect` | 0 |  |
| `hypothesis_invalidated` | 0 |  |
| `success` | 0 |  |

## Harness Root Cause Trends

| Layer | Count | Repeated evidence | Proposed response |
| --- | ---: | --- | --- |
| `observation` | 0 |  |  |
| `context` | 0 |  |  |
| `planning` | 0 |  |  |
| `control_loop` | 0 |  |  |
| `tool_action` | 0 |  |  |
| `state_store` | 0 |  |  |
| `verification` | 0 |  |  |
| `governance` | 0 |  |  |
| `product_code` | 0 |  |  |
| `unknown` | 0 |  |  |

## Loop Trace Summary

| Metric | Value | Notes |
| --- | ---: | --- |
| Milestone PRs reviewed | 0 |  |
| CI attempts | 0 |  |
| Fix attempts | 0 |  |
| Merge attempts | 0 |  |
| Missing trace evidence | 0 |  |
| Repeated non-product root-cause layers | 0 |  |

## Hypothesis Results Since Last Review

| Hypothesis | Status | Evidence | Decision |
| --- | --- | --- | --- |
|  |  |  |  |

## Harness Repair Candidates

| Candidate | Evidence | Root-cause layer | Decision |
| --- | --- | --- | --- |
|  |  | unknown | repair_not_needed |

## Current State Assessment

- Product goal alignment:
- Verification health:
- Plan freshness:
- Known blockers:

## Gaps Found

| Gap | Evidence | Proposed action |
| --- | --- | --- |
|  |  |  |

## Risks Found

| Risk | Evidence | Decision |
| --- | --- | --- |
|  |  |  |

## Plan Updates Applied

| Update | Target file | Reason |
| --- | --- | --- |
|  |  |  |

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

## Next Runner Action

- 
```
