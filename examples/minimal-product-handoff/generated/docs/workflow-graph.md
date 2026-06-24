# Workflow Graph

```yaml
workflow_graph:
  project_loop:
    - bootstrap
    - handoff_decision
    - long_run_growth_review
    - deep_review
    - growth_candidate_selection
    - runner_memory_compaction
    - final_review_candidate
  milestone_loop:
    - progress_read
    - memory_read
    - milestone_selection
    - codebase_localization
    - implementation
    - ci_observation
    - feedback_classification
    - agent_judge
    - progress_update
    - loop_trace_update
  repair_loop:
    - repair_trigger
    - root_cause_classification
    - harness_repair
    - judge_review
    - return_to_project_loop
```
