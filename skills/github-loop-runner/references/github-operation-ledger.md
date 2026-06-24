# GitHub Operation Ledger Reference

Use this reference before any GitHub write operation in a generated repository.

## Purpose

GitHub connector actions are individual API calls, not a persistent shell session. The runner must keep an explicit operation ledger so it does not repeat branch setup, lose the active branch, write to the wrong branch, or call ref-moving operations without a clear reason.

This protocol prevents repeated branch preparation, accidental base-branch writes, stale file SHA writes, and unsafe branch repair attempts.

## Generated Repo File

Generate `docs/github-operation-ledger.md`.

## Ledger Rule

Every GitHub write action must be preceded by an explicit operation state.

The operation state must include:

- repository,
- base branch,
- active branch,
- target files,
- current step,
- next action,
- completed mutation steps,
- forbidden actions,
- file SHA source when updating existing files.

## Operation State Format

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

## State Machine

| State | Allowed next actions | Disallowed actions |
| --- | --- | --- |
| `no_branch` | create branch once | update file, create PR, merge |
| `branch_ready` | fetch target files or create new files | create the same branch again, move refs |
| `files_fetched` | update target files using fetched SHA | create branch again, move refs |
| `files_mutated` | create PR once | create second branch |
| `pr_opened` | observe CI and PR state | move refs unless a rebase plan exists |
| `ci_observed` | fix target files, merge, or block | rebuild branch without a ledger entry |
| `merged_or_blocked` | re-read progress | continue writing old branch |

## Branch Rules

- Create one milestone branch once.
- If the branch already exists and is safe, use it; do not create it again.
- If branch state is uncertain, do not repair it by moving refs. Quarantine it and create a new clean branch from the base branch.
- Do not write to the base branch for milestone work.
- Do not use multiple active branches for one milestone slice.

## Ref Movement Rules

Default: moving refs is not allowed.

A ref move is allowed only when all are true:

- the runner has a named rebase or fast-forward plan,
- source SHA and target SHA are known,
- the operation ledger says the current step is ref alignment,
- the operation is recorded in loop trace,
- Agent Judge Loop can review it before merge.

If these conditions are missing, use a clean branch rather than moving an existing ref.

## Mutation Loop Stopper

Repeated branch or ref actions are blocking feedback.

Trigger when any of these occur:

- create branch is attempted more than once for the same milestone branch,
- a ref move is attempted without a rebase or fast-forward plan,
- branch state is unknown after a write action,
- the runner tries to write before declaring active branch and target files,
- the runner prepares branches repeatedly but does not reach file mutation.

Required action:

1. Stop the mutation sequence.
2. Classify feedback as protocol violation or tool action failure.
3. Record the unsafe branch state.
4. Continue only from a clean branch or after human review.

## Safe Single-Slice Sequence

Use this order for ordinary work:

1. declare operation state,
2. create branch once,
3. fetch target files,
4. update or create target files,
5. create PR once,
6. observe CI,
7. merge or block,
8. re-read progress.

## Agent Judge Checks

Agent Judge Loop should check:

- active branch declared,
- target files declared,
- branch created at most once,
- existing file SHA came from a fetch on the active branch,
- no base-branch write occurred,
- ref movement was not used unless explicitly justified,
- mutation sequence reached the intended next step.
