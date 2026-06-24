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
| `docs/handoff-decision.md` | Records the choice between current-agent development and external-agent handoff. |
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
- Bootstrap CI may be docs-only; the first product milestone must add real stack checks.
- Generate feedback, trace, handoff, review, hypothesis, repair, and stopper files together.
- After bootstrap, stop at the Handoff Decision before product milestone implementation starts.

## `AGENTS.md` Template

Agents should read `docs/autonomous-runner.md`, `docs/progress.md`, `docs/next-steps-plan.md`, `docs/development-principles.md`, `docs/feedback-taxonomy.md`, `docs/loop-trace.md`, `docs/handoff-decision.md`, and `docs/loop-hypotheses.md` before development.

`docs/progress.md` is the state source. Select the first TODO milestone only after the Handoff Decision has selected current-agent development or after another agent receives the complete external-agent prompt.

## Workflow Discipline

Align, slice, plan, verify first, build surgically, review against evidence, and finish only after CI is green. Keep changes scoped to the current milestone and preserve acceptance evidence.

## `docs/autonomous-runner.md` Template

Goal: move each `docs/progress.md` row to DONE through one CI-verified PR into `<BASE_BRANCH>` after the Handoff Decision has selected the development mode.

Required sections:

- Handoff Decision
- Soft Check
- Autonomous Loop
- Guardrails
- Stop Conditions

Autonomous Loop summary:

1. Fetch progress, feedback log, loop trace, handoff decision, loop hypotheses, and stopper policy.
2. Confirm that current-agent development or external-agent handoff has been selected.
3. Decide whether review, harness repair, or hypothesis validation is due.
4. Select the first TODO row. Skip DONE, BLOCKED, DEFERRED, and CANCELLED.
5. Append trace events for selected_milestone, branch_created, pr_opened, ci_observed, feedback_classified, merge_attempted, progress_updated, review_run, harness_repair_run, hypothesis_updated, handoff_decision, and stop.
6. Plan and implement the smallest vertical slice.
7. Use CI as VERIFY.
8. Merge only after CI, progress, feedback, trace, and hypothesis evidence are complete.
9. Re-fetch progress before choosing the next milestone.

## `docs/handoff-decision.md` Template

Recommended starting state:

```yaml
handoff:
  status: pending
  chosen_mode: null
  decided_at: null
  decided_by: null
  external_agent_prompt_generated: false
  bootstrap_pr: null
  first_todo_milestone: null
```

Allowed modes:

- `current_agent_development`: the current agent may enter the loop workflow.
- `external_agent_development`: the current agent outputs a complete prompt for another agent and stops product development in this session.

## `docs/progress.md` Template

Required sections:

- base branch
- status legend with TODO, IN_PROGRESS, DONE, BLOCKED, DEFERRED, CANCELLED
- progress table with milestone id, description, and status

## `docs/next-steps-plan.md` Template

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

## `docs/development-principles.md` Template

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

## `docs/loop-trace.md` Template

Trace metrics should include selected_milestone, branch_created, pr_opened, ci_observed, feedback_classified, merge_attempted, progress_updated, review_run, harness_repair_run, hypothesis_updated, handoff_decision, and stop.

## `docs/loop-hypotheses.md` Template

Start with an empty hypothesis log. Each hypothesis needs validation, invalidation, promotion, and rollback rules.

## `.github/pull_request_template.md` Template

Required checklist items:

- CI is green.
- Acceptance criteria mapped to CI or review evidence.
- `docs/progress.md` is updated to DONE or a progress PR is linked.
- loop trace updated.
- feedback entries linked when applicable.
- root-cause layer classified for blocking feedback.
- active hypotheses updated when applicable.
- handoff decision respected when applicable.
- harness repair considered when failures repeat.
- no unrelated refactors.
- no dummy/noop/temp filler files.

## `.github/workflows/verify.yml` Template

The initial workflow must check that the generated runner docs exist, including:

- `AGENTS.md`
- `docs/autonomous-runner.md`
- `docs/progress.md`
- `docs/next-steps-plan.md`
- `docs/development-principles.md`
- `docs/feedback-taxonomy.md`
- `docs/feedback-log.md`
- `docs/loop-trace.md`
- `docs/handoff-decision.md`
- `docs/review-and-renewal-loop.md`
- `docs/harness-repair-loop.md`
- `docs/loop-hypotheses.md`
- `docs/stopper-policy.md`

Replace this workflow with stack-specific checks once code exists.
