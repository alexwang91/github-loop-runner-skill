# GitHub Operation Ledger

Record GitHub write-operation state before each write action.

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

## Safe Single-Slice Sequence

1. declare operation state
2. create branch once
3. fetch target files
4. update or create target files
5. create PR once
6. observe CI
7. merge or block
8. re-read progress

## Mutation Loop Stopper

Repeated branch or ref actions are blocking feedback and require stopping the write sequence before continuing.
