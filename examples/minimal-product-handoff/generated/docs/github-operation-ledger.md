# GitHub Operation Ledger

```yaml
operation_state:
  repo: example/task-board
  base_branch: main
  active_branch: null
  target_files: []
  current_step: no_branch
  next_action: create_branch
  completed_steps:
    create_branch: false
    fetch_target_files: false
    mutate_target_files: false
    create_pr: false
  mutation_budget:
    create_branch: 1
    create_pr: 1
    update_ref: 0
  forbidden_actions:
    - write_to_base_branch
    - create_second_branch
    - update_ref_without_rebase_plan
```

Use the safe sequence: declare state, create one branch, fetch target files, mutate target files, create one PR, observe CI, merge or block, then re-read progress.
