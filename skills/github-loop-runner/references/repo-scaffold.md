# Repo Scaffold Reference

Use this reference when bootstrapping a repository from a product idea. Fill templates with project-specific content; do not paste placeholders when the user has provided better detail.

## Required Files

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Standing instructions for coding agents. |
| `docs/autonomous-runner.md` | Persistent autonomous loop protocol. |
| `docs/progress.md` | Single source of truth for milestone state. |
| `docs/next-steps-plan.md` | Detailed milestone plan and acceptance criteria. |
| `docs/development-principles.md` | Engineering principles, Methodology Map, Skill Pack Map, and workflow discipline. |
| `docs/feedback-taxonomy.md` | Local feedback classification rules. |
| `docs/feedback-log.md` | Append-only feedback record. |
| `docs/loop-trace.md` | Observable runner event log. |
| `docs/review-and-renewal-loop.md` | Review protocol. |
| `docs/harness-repair-loop.md` | Harness repair protocol. |
| `docs/loop-hypotheses.md` | Hypothesis log for evidence-gated process changes. |
| `docs/stopper-policy.md` | Hard and soft stoppers. |
| `docs/loop-review.md` | Latest loop review. |
| `.github/pull_request_template.md` | Evidence checklist. |
| `.github/workflows/verify.yml` | CI verification scaffold. |

## Seed Generation Rules

- Make the base branch explicit in runner-facing docs.
- Keep `docs/progress.md` as the only milestone state source.
- Write vertical-slice milestones with observable acceptance criteria.
- Encode Matt Pocock alignment, Superpowers planning/TDD/review/finish, and Karpathy simplicity/surgical guardrails.
- Include optional invocation names for runtimes that have those skills installed.
- Do not create `noop`, `dummy`, `x`, `y`, or temporary filler files.
- Bootstrap CI may be docs-only; the first product milestone must add real stack checks.
- Generate feedback, trace, review, hypothesis, repair, and stopper files together.

## `AGENTS.md` Template

```markdown
# Agent Instructions

Read `docs/autonomous-runner.md`, `docs/progress.md`, `docs/next-steps-plan.md`, `docs/development-principles.md`, `docs/feedback-taxonomy.md`, `docs/loop-trace.md`, and `docs/loop-hypotheses.md` before development.

`docs/progress.md` is the state source. Pick the first TODO milestone, complete it through one PR into `<BASE_BRANCH>`, update that row to DONE, append trace and feedback evidence, then re-read progress.

## Workflow Discipline

Align, slice, plan, verify first, build surgically, review against evidence, and finish only after CI is green. Do not weaken tests, evals, assertions, or acceptance criteria.
```

## `docs/autonomous-runner.md` Template

```markdown
# Autonomous Runner Protocol

Goal: move each `docs/progress.md` row to DONE through one CI-verified PR into `<BASE_BRANCH>`.

## Soft Check

Quietly probe GitHub connector, CI, and optional local access. In GitHub-only mode, verification is CI.

## Autonomous Loop

1. Fetch progress, feedback log, loop trace, loop hypotheses, and stopper policy.
2. Decide whether review, harness repair, or hypothesis validation is due.
3. Select the first TODO row. Skip DONE, BLOCKED, DEFERRED, and CANCELLED.
4. Append trace events for selected_milestone, branch_created, pr_opened, ci_observed, feedback_classified, merge_attempted, progress_updated, review_run, harness_repair_run, hypothesis_updated, and stop.
5. Plan and implement the smallest vertical slice.
6. Use CI as VERIFY. Do not weaken tests or assertions.
7. Merge only after CI, progress, feedback, trace, and hypothesis evidence are complete.
8. Re-fetch progress before choosing the next milestone.
```

## `docs/progress.md` Template

```markdown
# Autonomous Progress

> Base branch: `<BASE_BRANCH>`.

## Status Legend

- TODO
- IN_PROGRESS
- DONE
- BLOCKED
- DEFERRED
- CANCELLED

## Progress

| Milestone | Description | Status |
| :--- | :--- | :--- |
| M0 | `<FIRST_VERTICAL_SLICE>` | TODO |
| M1 | `<SECOND_VERTICAL_SLICE>` | TODO |
```

## `docs/next-steps-plan.md` Template

```markdown
# Next Steps Plan

## Product Goal

`<ONE_PARAGRAPH_PRODUCT_GOAL>`

## Methodology Map

- Matt Pocock skills: alignment, shared language, ADRs, vertical-slice issues.
- Superpowers: brainstorm -> plan -> TDD/eval-first -> review -> finish.
- Karpathy guidelines: think before coding, simplicity first, surgical changes.

## Optional Skill Invocation Map

| Phase | Optional invocation | Fallback |
| --- | --- | --- |
| Align | `$grill-with-docs` or `/grill-with-docs` | Clarify goal and terms. |
| Slice | `$to-issues` or `/to-issues` | Create vertical milestones. |
| Brainstorm | `$brainstorming` or `/brainstorming` | Explore options. |
| Plan | `$writing-plans` or `/writing-plans` | Write concrete steps. |
| Behavior changes | `$test-driven-development` or `/test-driven-development` | Define the failing check first. |
| Review | `$requesting-code-review` or `/requesting-code-review` | Review diff and evidence. |
| Finish | `$finishing-a-development-branch` or `/finishing-a-development-branch` | Merge after CI and state updates. |
```

## `docs/development-principles.md` Template

```markdown
# Development Principles

## Skill Pack Map

| Source skill family | What to do in this repo |
| --- | --- |
| Matt Pocock | Align intent, establish language, write ADRs, slice vertically. |
| Superpowers | Brainstorm, plan, TDD/eval-first, review, finish. |
| Karpathy | State assumptions, keep simple, touch necessary files only. |

## Optional Runtime Invocations

Use `$grill-with-docs`, `$to-issues`, `$brainstorming`, `$writing-plans`, `$test-driven-development`, `$requesting-code-review`, and `$finishing-a-development-branch` only when installed.

## Workflow Discipline

Align, slice, plan, verify first, build surgically, review, finish.
```

## `docs/loop-trace.md` Template

````markdown
# Loop Trace

## Metrics

| Metric | Value | Notes |
| --- | ---: | --- |
| selected_milestone | 0 |  |
| branch_created | 0 |  |
| pr_opened | 0 |  |
| ci_observed | 0 |  |
| feedback_classified | 0 |  |
| merge_attempted | 0 |  |
| progress_updated | 0 |  |
| review_run | 0 |  |
| harness_repair_run | 0 |  |
| hypothesis_updated | 0 |  |
| stop | 0 |  |

## Events

```yaml
entries: []
```
````

## `docs/loop-hypotheses.md` Template

````markdown
# Loop Hypotheses

```yaml
entries: []
```
````

## `.github/pull_request_template.md` Template

```markdown
## Milestone

- Progress row:
- Base branch:

## What changed

-

## Acceptance evidence

| Acceptance criterion | CI/review evidence |
| --- | --- |
|  |  |

## Verification

- [ ] CI is green.
- [ ] Acceptance criteria mapped to CI or review evidence.
- [ ] `docs/progress.md` is updated to DONE or a progress PR is linked.

## Loop evidence

- [ ] loop trace updated.
- [ ] feedback entries linked when applicable.
- [ ] root-cause layer classified for blocking feedback.
- [ ] active hypotheses updated when applicable.
- [ ] harness repair considered when failures repeat.

## Guardrails

- [ ] No weakened tests, evals, assertions, or acceptance criteria.
- [ ] No unrelated refactors.
- [ ] No dummy/noop/temp filler files.
```

## `.github/workflows/verify.yml` Template

```yaml
name: verify
on:
  pull_request:
  push:
    branches: ["<BASE_BRANCH>"]
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
          test -f docs/feedback-taxonomy.md
          test -f docs/feedback-log.md
          test -f docs/loop-trace.md
          test -f docs/review-and-renewal-loop.md
          test -f docs/harness-repair-loop.md
          test -f docs/loop-hypotheses.md
          test -f docs/stopper-policy.md
          ! find . -maxdepth 4 -type f \( -name noop -o -name dummy -o -name x -o -name y \) | grep .
```

Replace this workflow with stack-specific checks once code exists.
