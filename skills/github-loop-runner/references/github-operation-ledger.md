# GitHub Operation Ledger Reference

Use this reference before any GitHub write operation in a generated repository.

## Purpose

GitHub connector actions are individual API calls, not a persistent shell session. The runner must keep an explicit operation state so it does not repeat branch setup, lose the active branch, write to the wrong branch, or move refs without a clear reason.

This protocol is part of the stable v1 core. It is not a runtime DSL.

## Generated Repo File

Generate `docs/github-operation-ledger.md`.

## Operation State

Every GitHub write action must be preceded by an operation state:

```yaml
operation_state:
  repo: owner/name
  base_branch: main
  active_branch: feature-branch
  target_files:
    - docs/next-steps-plan.md
  current_step: fetch_target_files
  next_action: update_file
  completed_steps:
    create_branch: true
    fetch_target_files: true
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

## Safe Sequence

1. Declare operation state.
2. Create one branch once.
3. Fetch target files.
4. Update or create target files.
5. Create one PR once.
6. Observe CI.
7. Merge or block.
8. Re-read progress.

## Stopper

Repeated branch or ref preparation is blocking feedback. If branch state is uncertain, stop the mutation sequence and continue only from a clean branch or after human review.
