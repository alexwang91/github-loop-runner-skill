# Stable v1 Freeze

GitHub Loop Runner is frozen as **GitHub Loop Engine v1**.

## Decision

The project will converge on a stable, minimal GitHub loop engine instead of continuing toward an agent OS, runtime DSL, or self-modifying CI framework.

Controlled Research Intake is allowed inside v1 because it strengthens review, backlog renewal, and code quality without adding a new runtime plane. It is not an automation engine.

## V1 Core

The stable core is:

1. Handoff Decision after bootstrap.
2. GitHub Operation Ledger before write actions.
3. `docs/progress.md` as the milestone state source.
4. One branch, one PR, one milestone.
5. CI as VERIFY.
6. Every-PR Coding Skill Gate.
7. Feedback and Loop Trace for evidence.
8. Long-Run Growth for useful backlog renewal.
9. Controlled Research Intake for cadence-based external learning.
10. Harness Repair for runner/process defects.
11. Stopper Policy for unsafe or unverifiable work.

## Frozen Non-Goals

Do not expand v1 toward:

- general agent OS,
- runtime DSL,
- self-modifying CI interpreter,
- unbounded protocol growth,
- local-first execution replacing CI,
- multi-agent orchestration beyond handoff prompts,
- broad research on every PR,
- scheduler or daemon ownership,
- general MCP registry,
- local worktree manager,
- database-backed memory.

## Change Admission Rule

A future change is allowed only if it strengthens one of the v1 core responsibilities without adding a new architectural plane.

Allowed examples:

- clearer operation ledger checks,
- better progress consistency validation,
- simpler runner prompt wording,
- README and example cleanup,
- safer stopper conditions,
- tighter research absorption rules,
- clearer coding skill gate evidence.

Rejected examples:

- more generalized runtime execution,
- CI-as-interpreter features,
- new DSL syntax,
- recursive self-modification loops,
- additional agent orchestration layers,
- automatic broad web search for every ordinary PR,
- turning research intake into a scheduler, crawler, or MCP registry.

## Stability Contract

The stable contract is:

```text
product idea or existing repo
  -> bootstrap runner docs
  -> stop for handoff
  -> select first TODO
  -> declare operation state
  -> run coding skill gate
  -> create one branch and one PR
  -> use CI as VERIFY
  -> update feedback, trace, and progress
  -> run review/repair/growth/research intake only when due
  -> re-read state
```

The project should optimize this contract for reliability and clarity, not broaden it.
