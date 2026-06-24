# Long-Run Growth Loop Reference

Use this reference when the user wants the autonomous runner to keep expanding useful work instead of stopping after a small initial backlog.

## Purpose

Long-Run Growth Mode gives the runner an explicit long-horizon target. Before the configured minimum PR budget is reached, an empty TODO list is not a final stop condition. It is a mandatory trigger for deep review, backlog expansion, and plan renewal.

The goal is not to create busywork. The goal is to force periodic project-level evaluation, compare the current implementation with the initial product goal, identify meaningful gaps, generate more verifiable milestones, and keep the runner moving until repeated deep reviews show that no high- or medium-impact work remains.

## Default Policy

```yaml
long_run_growth:
  enabled: true
  target_merged_prs: 50
  minimum_merged_prs_before_final_stop: 40
  review_interval_prs: 5
  deep_review_interval_prs: 10
  minimum_open_todo_backlog: 12
  preferred_open_todo_backlog: 20
  expansion_batch_min: 8
  expansion_batch_max: 15
  stop_requires_consecutive_empty_deep_reviews: 3
```

Generated repositories may tune these values, but they should keep an explicit minimum PR budget and backlog floor.

## Core Rule

Before `minimum_merged_prs_before_final_stop` is reached, no TODO remaining is not a final stop condition. It is a mandatory trigger for Long-Run Growth Review.

The runner must expand the plan until the backlog floor is restored, unless a hard safety stopper applies.

## Trigger Conditions

Run Long-Run Growth Review when any condition applies:

- merged PR count reaches a multiple of `review_interval_prs`,
- merged PR count reaches a multiple of `deep_review_interval_prs`,
- open TODO count falls below `minimum_open_todo_backlog`,
- no TODO rows remain before the minimum PR budget is reached,
- review finds plan drift from the initial product goal,
- repeated feedback shows weak verification, scope drift, regressions, or blocked work,
- the user asks for longer autonomous continuation.

## Deep Review Questions

Every deep review must answer:

1. What was the initial product goal?
2. What has the repository actually implemented?
3. Where has the current implementation drifted from the initial plan?
4. Which user-visible flows are still missing or incomplete?
5. Which correctness, validation, error-handling, or state-transition gaps remain?
6. Which modules lack tests, fixtures, evals, build checks, or smoke checks?
7. Which docs, examples, onboarding paths, or release notes are missing?
8. Which operational gaps remain: logging, diagnostics, setup, deployment, release, rollback?
9. Which blocked items can move forward through mocks, fixtures, fake providers, or smaller slices?
10. Is the TODO backlog below the configured floor?
11. Which 8-15 new milestones should be appended now?

## Plan Expansion Categories

New milestones should be drawn from these categories:

| Category | Meaning |
| --- | --- |
| `product_surface` | user-visible flows, UI/API/CLI behavior, onboarding, examples |
| `correctness` | edge cases, validation, state transitions, regression tests |
| `verification` | tests, CI, evals, fixtures, coverage, smoke checks |
| `operability` | logging, diagnostics, failure messages, setup, release checks |
| `architecture` | module boundaries, duplicate logic, migration path, dependency simplification |
| `security_governance` | permission checks, secret handling, trust boundaries, safe defaults |
| `documentation` | user docs, developer docs, ADRs, examples, generated prompt docs |
| `harness_quality` | progress consistency, feedback quality, trace coverage, repair rules |

## Milestone Requirements

Every generated milestone must include:

- category,
- impact: high or medium unless explicitly justified,
- reason from deep review,
- acceptance criteria,
- verification path,
- expected changed files or areas,
- blocker status,
- whether it can fit in one PR.

Do not add milestones named cleanup, polish, improve quality, maybe refactor, miscellaneous, follow-up, or investigate later.

## Backlog Floor

The runner must keep enough future work available:

```yaml
backlog_policy:
  minimum_todo_count: 12
  preferred_todo_count: 20
  expansion_batch_min: 8
  expansion_batch_max: 15
```

If TODO count is below the floor, run plan expansion and append enough specific milestones to restore the backlog.

## Stop Candidate Loop

Final stopping is allowed only after the minimum PR budget has been reached and multiple empty deep reviews agree that no meaningful work remains.

Required empty reviews:

- product completeness review,
- correctness and verification review,
- operational readiness review.

A final stop candidate must confirm:

- total merged PRs are at or above the configured minimum,
- consecutive empty deep reviews meet the configured threshold,
- no high-impact product work remains,
- no medium-impact quality work remains,
- no safe blocker-removal work remains,
- no verification-hardening work remains.

## Forbidden Behavior

Do not treat a short initial plan as the whole project.

Do not stop at 10-15 PRs only because the initial TODO list ran out.

Do not add vague or unverifiable work merely to satisfy the PR budget.

Do not weaken hard safety stoppers. Credentials, live services, security boundaries, destructive operations, and missing GitHub access still require stopping or human input.
