# Workflow Graph Reference

Use this reference to make the runner's control flow explicit.

## Purpose

A long-running agent should know which workflow node it is executing. Workflow Graph separates project-level planning from milestone-level implementation and makes transitions auditable.

## Generated Repo File

Generate `docs/workflow-graph.md`.

## Default Graph

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

## Node Record Format

```yaml
workflow_node:
  id: W-0001
  node: milestone_selection
  inputs:
    - docs/progress.md
  outputs:
    - selected milestone M0
  next_node: codebase_localization
```

## Rules

1. Record node transitions in Loop Trace when they affect control flow.
2. Project-loop work should not implement product code directly.
3. Milestone-loop work should not change long-run policy unless review approved it.
4. Repair-loop work should return to the project or milestone loop after judge review.
