# Repo Scaffold Reference

Use this reference when bootstrapping a repository from a product idea. Fill templates with project-specific content; do not paste placeholders or generic milestones when the user has provided better detail.

## Required Files

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Standing instructions for coding agents that open the repo. |
| `docs/autonomous-runner.md` | Persistent autonomous loop protocol. |
| `docs/progress.md` | Single source of truth for milestone state. |
| `docs/next-steps-plan.md` | Detailed milestone plan with acceptance criteria. |
| `docs/development-principles.md` | Engineering principles, source skill map, and milestone workflow discipline. |
| `.github/pull_request_template.md` | PR checklist that reinforces CI, progress, and no dummy files. |
| `.github/workflows/verify.yml` | Initial CI verification. Replace or extend with real stack checks as soon as code exists. |

Optional: add `docs/decisions/` ADRs when the project has durable architecture decisions.

## Seed Generation Rules

- Make the base branch explicit in every runner-facing doc.
- Make `docs/progress.md` the only state source.
- Write milestones as vertical slices, not layers. A good milestone has user-visible behavior, tests/evals, and acceptance criteria.
- Include source links for external skill inspirations instead of vendoring entire third-party repos.
- Make the source skill systems visible: Matt Pocock skills shape alignment/shared language/vertical issues; Superpowers shapes brainstorm/plan/TDD/review/finish; Karpathy guidelines shape simplicity/surgical/goal-driven guardrails.
- Include optional invocation names for runtimes that have those skills installed, but keep a fallback prose discipline so GitHub-only runners without those plugins still work.
- Put the "Workflow Discipline" in `AGENTS.md`, `docs/autonomous-runner.md`, and `docs/development-principles.md`.
- Do not create `noop`, `dummy`, `x`, `y`, or temporary filler files.
- For the bootstrap PR, a docs-only CI workflow is acceptable. For the first product milestone, add real checks for the project stack.

## `AGENTS.md` Template

```markdown
# Agent Instructions

Before doing development work, read:

1. `docs/autonomous-runner.md`
2. `docs/progress.md`
3. `docs/next-steps-plan.md`
4. `docs/development-principles.md`

`docs/progress.md` is the only state source. Pick the first `⬜ TODO` milestone, complete it through one PR into `<BASE_BRANCH>`, update that row to `✅ DONE`, then re-read progress before continuing.

Use GitHub connector APIs when local clone or package-manager access is unavailable. In GitHub-only mode, verification is CI.

## Workflow Discipline

Before each milestone PR:

1. Align like `mattpocock/skills`: clarify the user's real goal, name domain terms, and record durable decisions as ADRs when needed.
2. Slice like `mattpocock/skills/to-issues`: milestone work must be a thin vertical slice, not a layer-only task.
3. Plan like `obra/superpowers`: brainstorm tradeoffs, write a concrete implementation plan, then execute against it.
4. Verify like Superpowers TDD: define the failing test, eval, or CI acceptance signal before changing behavior.
5. Review and finish like Superpowers: inspect the PR against the plan, fix real issues, merge only after CI is green.
6. Guard like Karpathy guidelines: think before coding, keep it simple, make surgical changes, and loop against explicit success criteria.

Do not weaken tests, evals, assertions, or acceptance criteria to make CI green. Do not create dummy/noop files. Keep changes scoped to the current milestone.
```

## `docs/autonomous-runner.md` Template

```markdown
# Autonomous Runner Protocol

> Persistent instruction for autonomous coding agents.
> State source: `docs/progress.md`.
> Milestone details: `docs/next-steps-plan.md`.

## Role

You are the autonomous engineering runner for `<OWNER>/<REPO>`.

Goal: move every row in `docs/progress.md` to `✅ DONE`, one milestone PR at a time, merged into `<BASE_BRANCH>`.

Use these principles: vertical slices, simple design, surgical changes, tests/evals as specifications, CI as verifier, human approval for trust boundaries.

## Soft Check

At startup, quietly probe available capabilities without stopping the whole run. Do not ask the user to confirm GitHub connector access when it is already callable:

- GitHub connector for repository read/write, PRs, CI status, and merge.
- CI checks on PRs.
- Local clone/package-manager access only if explicitly available outside GitHub-only mode.

If local verification is unavailable but GitHub connector and CI work, continue and let CI verify. If no GitHub write path exists, mark affected work `⏸️ BLOCKED` with the missing permission.

## Autonomous Loop

1. Fetch `docs/progress.md` from `<BASE_BRANCH>`.
2. Select the first `⬜ TODO` row. Skip `✅ DONE` and `⏸️ BLOCKED`.
3. If no `⬜ TODO` remains, stop and report final state.
4. Fetch `docs/next-steps-plan.md` and `docs/development-principles.md`; read the selected milestone section and workflow discipline.
5. Plan the smallest vertical slice that satisfies the milestone acceptance criteria.
6. Create branch `m<N>-<slug>` from `<BASE_BRANCH>`.
7. Implement only this milestone.
8. Open a PR into `<BASE_BRANCH>`.
9. Use CI checks as VERIFY. Fix real failures. Do not weaken assertions or tests.
10. After CI is green, ensure `docs/progress.md` marks the milestone `✅ DONE`.
11. Merge the PR after CI is green.
12. Return to step 1 and re-fetch progress before choosing the next milestone.

## Guardrails

- One milestone, one vertical-slice PR.
- No unrelated refactors.
- No dummy/noop/temp filler files.
- No direct production sends, destructive actions, or credential use without explicit approval.
- Mock unstable external providers by default. Gate real integrations with opt-in environment flags.
- Keep CI/evals meaningful. Red is a real signal.

## Stop Conditions

Stop and report when all remaining milestones are blocked, CI cannot verify, credentials are required, a trust boundary changes, or a merged milestone regresses.
```

## `docs/progress.md` Template

```markdown
# Autonomous Progress

> Single source of truth for the runner.
> Protocol: `docs/autonomous-runner.md`.
> Milestone details: `docs/next-steps-plan.md`.
> Base branch: `<BASE_BRANCH>`.

## Status Legend

- `⬜ TODO` - not started.
- `🔄 IN_PROGRESS` - actively being worked. Use at most one.
- `✅ DONE` - merged into `<BASE_BRANCH>` and CI green.
- `⏸️ BLOCKED` - cannot proceed. Add a note below with the missing tool, credential, CI signal, or decision.

## Progress

| Milestone | Description | Status |
| :--- | :--- | :--- |
| M0 | `<FIRST_VERTICAL_SLICE>` | ⬜ TODO |
| M1 | `<SECOND_VERTICAL_SLICE>` | ⬜ TODO |
| M2 | `<THIRD_VERTICAL_SLICE>` | ⬜ TODO |

## Notes

- Add blocked reasons and durable decisions here.
```

## `docs/next-steps-plan.md` Template

```markdown
# Next Steps Plan

## Product Goal

`<ONE_PARAGRAPH_PRODUCT_GOAL>`

## Methodology Map

- Matt Pocock skills: use alignment, shared language, ADRs, and vertical-slice issues.
- Superpowers: use brainstorm -> plan -> TDD/eval-first -> review -> finish discipline.
- Karpathy guidelines: think before coding, simplicity first, surgical changes, goal-driven execution.

## Optional Skill Invocation Map

If the runner has these skills installed, use them. If not, apply the fallback discipline written here.

| Phase | Optional invocation | Fallback |
| --- | --- | --- |
| Align product intent and terms | `$grill-with-docs` or `/grill-with-docs` | Clarify goal, vocabulary, open questions, and ADR-worthy decisions. |
| Slice the plan | `$to-issues` or `/to-issues` | Convert the plan into vertical milestones and acceptance criteria. |
| Brainstorm tradeoffs | `$brainstorming` or `/brainstorming` | Explore options before choosing the implementation shape. |
| Write the implementation plan | `$writing-plans` or `/writing-plans` | Write concrete steps with verification per milestone. |
| Behavior changes | `$test-driven-development` or `/test-driven-development` | Define the failing test, eval, or CI assertion before implementation. |
| Review PR work | `$requesting-code-review` or `/requesting-code-review` | Review diff against plan, acceptance criteria, and guardrails. |
| Finish branch | `$finishing-a-development-branch` or `/finishing-a-development-branch` | Merge only after CI is green and progress is updated. |

## Principles

- Build vertical slices that can be reviewed and verified independently.
- Prefer simple, direct code over speculative abstractions.
- Use tests, evals, or CI checks as acceptance criteria.
- Keep humans in the loop for credentials, external sends, destructive actions, and security boundaries.

## Milestones

### M0 - `<FIRST_VERTICAL_SLICE>`

**Goal**: `<WHAT_USER_CAN_DO_AFTER_THIS_SLICE>`

**Build**:
- `<END_TO_END_CHANGE>`

**Acceptance**:
- [ ] `<OBSERVABLE_CRITERION>`
- [ ] `<TEST_OR_CI_CRITERION>`

**Verification**:
- `<CI_COMMAND_OR_WORKFLOW_EXPECTATION>`

### M1 - `<SECOND_VERTICAL_SLICE>`

Repeat the same structure.
```

## `docs/development-principles.md` Template

```markdown
# Development Principles

This repo borrows discipline from these public skill collections:

- `mattpocock/skills`: small composable skills, alignment before building, shared language, ADRs, vertical issues.
- `obra/superpowers`: brainstorm, plan, TDD, review, and finish through explicit workflows.
- `multica-ai/andrej-karpathy-skills`: think before coding, simplicity first, surgical changes, goal-driven execution.

## Skill Pack Map

| Source skill family | What to do in this repo |
| --- | --- |
| Matt Pocock `grill-with-docs` / domain modeling | Clarify ambiguous product intent, establish project vocabulary, and write ADRs for durable choices. |
| Matt Pocock `to-issues` | Break plans into independently reviewable vertical slices. |
| Superpowers `brainstorming` / `writing-plans` | Explore options, then write executable milestone plans with clear verification. |
| Superpowers `test-driven-development` | For behavior changes, define a failing test/eval/CI assertion before implementation. |
| Superpowers review/finish flow | Review PRs against the plan, fix real issues, and finish only after verification is green. |
| Karpathy guidelines | State assumptions, choose simple designs, touch only necessary files, and loop toward explicit success criteria. |

## Optional Runtime Invocations

Use these only when the current agent runtime has the corresponding skills installed:

- `$grill-with-docs` or `/grill-with-docs` before turning a vague idea into a durable plan.
- `$to-issues` or `/to-issues` when converting a plan into vertical milestones.
- `$brainstorming` or `/brainstorming` before choosing an implementation approach.
- `$writing-plans` or `/writing-plans` before editing code.
- `$test-driven-development` or `/test-driven-development` before behavior-changing implementation.
- `$requesting-code-review` or `/requesting-code-review` before declaring a PR ready.
- `$finishing-a-development-branch` or `/finishing-a-development-branch` before merge/progress handoff.

## Workflow Discipline

For every milestone:

1. Align: restate the goal, assumptions, project terms, and decisions.
2. Slice: choose one end-to-end milestone path that produces observable value.
3. Plan: list implementation steps with verification for each.
4. Verify first: add or identify the test, eval, or CI check that will prove completion.
5. Build surgically: make the smallest scoped change that satisfies the plan.
6. Review: compare the diff to the plan and acceptance criteria.
7. Finish: merge only after CI is green, update `docs/progress.md`, then re-read progress.

## Working Rules

1. Clarify ambiguity that changes the plan. State assumptions when proceeding.
2. Break work into vertical slices with visible acceptance criteria.
3. Define verification before implementation when behavior changes.
4. Keep changes small and scoped to the current milestone.
5. Delete dead code only when the current milestone makes it dead, or when explicitly requested.
6. Treat CI and evals as specifications. Do not weaken them to pass.
7. Use mocks or gated integration tests for unstable external services.
8. Require human approval for credentials, external sends, destructive actions, and trust-boundary changes.
```

## `.github/pull_request_template.md` Template

```markdown
## Milestone

- Progress row:
- Base branch:

## What changed

-

## Verification

- [ ] CI is green.
- [ ] Required tests/evals/checks are meaningful for this milestone.
- [ ] `docs/progress.md` is updated to `✅ DONE` for this milestone, or a follow-up progress PR is linked.

## Guardrails

- [ ] No weakened tests, evals, assertions, or acceptance criteria.
- [ ] No unrelated refactors.
- [ ] No dummy/noop/temp filler files.
- [ ] Trust boundaries and external integrations remain gated or approved.
```

## `.github/workflows/verify.yml` Template

```yaml
name: verify

on:
  pull_request:
  push:
    branches:
      - "<BASE_BRANCH>"

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Verify runner docs
        run: |
          test -f AGENTS.md
          test -f docs/autonomous-runner.md
          test -f docs/progress.md
          test -f docs/next-steps-plan.md
          test -f docs/development-principles.md
          ! find . -maxdepth 4 -type f \( -name noop -o -name dummy -o -name x -o -name y \) | grep .
```

Replace this workflow with stack-specific checks once code exists, for example typecheck, tests, build, lint, and evals.
