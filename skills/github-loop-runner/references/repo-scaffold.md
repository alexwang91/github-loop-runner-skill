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
| `docs/github-operation-ledger.md` | GitHub write-operation state and branch/ref safety. |
| `docs/long-run-growth-loop.md` | Long-run review cadence, backlog floor, expansion policy, and final review criteria. |
| `docs/research-intake.md` | Controlled external research cadence and absorption rules. |
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
- Include an Every-PR Coding Skill Gate in generated runner docs.
- Include optional invocation names for runtimes that have those skills installed.
- Bootstrap CI may be docs-only; the first product milestone must add real stack checks.
- Generate operation ledger, feedback, trace, handoff, long-run growth, controlled research intake, review, hypothesis, repair, and stopper files together.
- After bootstrap, stop at the Handoff Decision before product milestone implementation starts.
- Long-Run Growth Mode should keep a backlog floor and run growth/deep reviews before final review eligibility.
- Controlled Research Intake should feed review and backlog renewal, not interrupt ordinary PR work.

## `AGENTS.md` Template

Agents should read `docs/autonomous-runner.md`, `docs/progress.md`, `docs/next-steps-plan.md`, `docs/development-principles.md`, `docs/github-operation-ledger.md`, `docs/long-run-growth-loop.md`, `docs/research-intake.md`, `docs/feedback-taxonomy.md`, `docs/loop-trace.md`, `docs/handoff-decision.md`, and `docs/loop-hypotheses.md` before development.

`docs/progress.md` is the state source. Select the first TODO milestone only after the Handoff Decision has selected current-agent development or after another agent receives the complete external-agent prompt.

Before choosing work, apply `docs/long-run-growth-loop.md`: report merged PR count, TODO backlog count, growth review due, deep review due, and final review eligibility. Declare operation state before GitHub write actions. Run the Every-PR Coding Skill Gate. Run `docs/research-intake.md` only when research cadence is due or a bounded domain/architecture decision needs external evidence.

## Workflow Discipline

Align, slice, plan, verify first, build surgically, review against evidence, and finish only after CI is green. Keep changes scoped to the current milestone and preserve acceptance evidence. External research must become notes, candidate ideas, rejected ideas, or accepted backlog items with verification paths before implementation.

## `docs/autonomous-runner.md` Template

Goal: move each `docs/progress.md` row to DONE through one CI-verified PR into `<BASE_BRANCH>` after the Handoff Decision has selected the development mode.

Required sections:

- Handoff Decision
- GitHub Operation Ledger
- Long-Run Growth Mode
- Controlled Research Intake
- Every-PR Coding Skill Gate
- Soft Check
- Autonomous Loop
- Guardrails
- Stop Conditions

Autonomous Loop summary:

1. Fetch progress, operation ledger, feedback log, loop trace, handoff decision, long-run growth policy, research intake policy, loop hypotheses, and stopper policy.
2. Confirm that current-agent development or external-agent handoff has been selected.
3. Apply Long-Run Growth Mode: check PR count, backlog floor, growth review, deep review, and final review eligibility.
4. Run Controlled Research Intake only when cadence is due, before deep review, or for a bounded new domain or architecture decision.
5. Decide whether review, harness repair, or hypothesis validation is due.
6. Select the first TODO row. Skip DONE, BLOCKED, DEFERRED, and CANCELLED.
7. Run the Every-PR Coding Skill Gate.
8. Declare GitHub Operation Ledger state before write actions.
9. Append trace events for selected_milestone, operation_state, coding_skill_gate, branch_created, pr_opened, ci_observed, feedback_classified, merge_attempted, progress_updated, research_intake, growth_review, deep_review, review_run, harness_repair_run, hypothesis_updated, handoff_decision, and stop.
10. Plan and implement the smallest vertical slice.
11. Use CI as VERIFY.
12. Merge only after CI, progress, feedback, trace, operation state, and hypothesis evidence are complete.
13. Re-fetch progress before choosing the next milestone.

## `docs/github-operation-ledger.md` Template

Start with explicit operation state and zero direct base-branch write budget. Ordinary milestone work should create one branch and one PR.

## `docs/long-run-growth-loop.md` Template

Recommended defaults:

```yaml
long_run_growth:
  enabled: true
  target_merged_prs: 50
  minimum_merged_prs_before_final_review: 40
  review_interval_prs: 5
  deep_review_interval_prs: 10
  minimum_open_todo_backlog: 12
  preferred_open_todo_backlog: 20
  expansion_batch_min: 8
  expansion_batch_max: 15
  empty_deep_reviews_before_final_review: 3
```

Before final review eligibility, an empty TODO list should trigger growth review and plan expansion unless a hard safety stopper applies.

## `docs/research-intake.md` Template

Recommended cadence:

```yaml
research_intake:
  every_n_prs: 5
  deep_review_every_n_prs: 10
  on_new_domain_or_architecture_decision: true
```

Research sources may include recent papers, high-quality GitHub repositories, official documentation, benchmark reports, and well-maintained examples. Research findings must be recorded as notes, candidate backlog items, or rejected ideas before implementation. Broad research is not required for ordinary PRs.

## Every-PR Coding Skill Gate

```yaml
coding_skill_gate:
  goal_clarified: true
  acceptance_criteria_defined: true
  vertical_slice: true
  implementation_plan_written: true
  verification_first: true
  minimal_diff: true
  review_before_merge: true
  progress_updated: true
```

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
- Controlled Research Intake: external ideas enter through notes, candidates, rejections, and verification paths.

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
| Research Intake | Absorb external evidence through review cadence and verification paths. |

## Optional Runtime Invocations

Use `$grill-with-docs`, `$to-issues`, `$brainstorming`, `$writing-plans`, `$test-driven-development`, `$requesting-code-review`, and `$finishing-a-development-branch` only when installed.

## Workflow Discipline

Align, slice, plan, verify first, build surgically, review, finish. Run research intake only when due; do not let external inspiration interrupt the active milestone PR.

## `docs/loop-trace.md` Template

Trace metrics should include selected_milestone, operation_state, coding_skill_gate, branch_created, pr_opened, ci_observed, feedback_classified, merge_attempted, progress_updated, research_intake, growth_review, deep_review, review_run, harness_repair_run, hypothesis_updated, handoff_decision, and stop.

## `docs/loop-hypotheses.md` Template

Start with an empty hypothesis log. Each hypothesis needs validation, invalidation, promotion, and rollback rules.

## `.github/pull_request_template.md` Template

Required checklist items:

- CI is green.
- Acceptance criteria mapped to CI or review evidence.
- Every-PR Coding Skill Gate completed.
- `docs/progress.md` is updated to DONE or a progress PR is linked.
- operation state declared and safe.
- loop trace updated.
- feedback entries linked when applicable.
- research intake records linked when applicable.
- root-cause layer classified for blocking feedback.
- active hypotheses updated when applicable.
- long-run growth policy checked when applicable.
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
- `docs/github-operation-ledger.md`
- `docs/long-run-growth-loop.md`
- `docs/research-intake.md`
- `docs/feedback-taxonomy.md`
- `docs/feedback-log.md`
- `docs/loop-trace.md`
- `docs/handoff-decision.md`
- `docs/review-and-renewal-loop.md`
- `docs/harness-repair-loop.md`
- `docs/loop-hypotheses.md`
- `docs/stopper-policy.md`

Replace this workflow with stack-specific checks once code exists.
