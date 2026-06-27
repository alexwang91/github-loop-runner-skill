# Controlled Research Intake Reference

Use this reference when a long-running GitHub loop should learn from external papers, high-quality repositories, official docs, or benchmark reports without drifting away from the current milestone discipline.

## Purpose

Research intake keeps the loop fresh and useful. It should improve backlog quality, coding discipline, and verification strategy.

It must not turn GitHub Loop Engine v1 into a scheduler, agent OS, runtime DSL, general MCP registry, or multi-agent orchestrator.

## Core Rule

External research is input to review and planning, not a direct license to change code.

Research findings must pass through:

```text
source
  -> note
  -> candidate idea
  -> relevance and risk check
  -> verification path
  -> accepted or rejected backlog item
  -> milestone PR
```

## Every-PR Coding Skill Gate

Every implementation PR should apply the coding discipline encoded by the project skills and references:

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

This gate represents the stable v1 application of Matt-style alignment and vertical slicing, Superpowers-style brainstorm -> plan -> verification -> review -> finish, and Karpathy-style simplicity and surgical changes.

## Research Cadence

Research is controlled by cadence:

```yaml
research_intake:
  every_n_prs: 5
  deep_review_every_n_prs: 10
  on_new_domain_or_architecture_decision: true
```

Do not run broad external research for every PR. Ordinary PRs should run the coding skill gate and stay scoped to the selected milestone.

## Allowed Sources

Prefer:

- recent research papers,
- high-quality GitHub repositories,
- official documentation,
- benchmark reports,
- well-maintained examples from reputable projects.

Avoid low-signal sources unless the user explicitly asks for them.

## Absorption Record

Record useful external ideas before adding them to the backlog:

```yaml
absorption_record:
  source: paper-or-repo-url
  idea: concise idea
  why_relevant: why it matters to this repository
  expected_benefit: expected improvement
  risk: low | medium | high
  verification_path: how the idea can be tested or reviewed
  accepted: true
  target_milestone: V7-17
```

Rejected ideas should also be recorded when they are likely to be rediscovered later.

## Admission Rules

An external idea may enter the backlog only when it has:

- clear relevance to the product goal or runner quality,
- a bounded implementation path,
- a verification path,
- no conflict with the current stable v1 scope,
- no requirement for unsupported runtime infrastructure.

## Forbidden Behavior

Do not:

- search broadly on every PR,
- let research interrupt an active milestone PR,
- directly implement ideas from papers or repositories without an absorption record,
- add scheduler, MCP registry, local worktree manager, database memory, or sub-agent runtime features to v1,
- expand beyond stable v1 non-goals without an explicit future-version decision.

## Stable v1 Mapping

| Loop Engineering primitive | Stable v1 mapping |
| --- | --- |
| Automation | Human, GitHub, or external trigger only. No built-in scheduler. |
| Worktree | GitHub branch and PR isolation. No local worktree manager. |
| Skills | `SKILL.md` and references. |
| Plugins / MCP | GitHub connector and CI only. |
| Sub-agents | Maker/Checker discipline as a process mode, not a runtime. |
| Memory | Markdown state: progress, trace, feedback, hypotheses, ledger. |

## Maker / Checker Discipline

Maker mode:

- select the milestone,
- declare operation state,
- plan the slice,
- implement the smallest useful change,
- open the PR with evidence.

Checker mode:

- inspect the diff,
- verify CI,
- check acceptance criteria,
- check progress, trace, feedback, and operation ledger state,
- decide merge, repair, or block.

This discipline may be performed by one agent. It does not require a multi-agent runtime.
