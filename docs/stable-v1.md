# Stable v1 Freeze

GitHub Loop Runner is frozen as **GitHub Loop Engine v1**.

## Decision

The project will converge on a stable, minimal GitHub loop engine instead of continuing toward an agent OS, runtime DSL, or self-modifying CI framework.

## V1 Core

The stable core is:

1. Handoff Decision after bootstrap.
2. GitHub Operation Ledger before write actions.
3. `docs/progress.md` as the milestone state source.
4. One branch, one PR, one milestone.
5. CI as VERIFY.
6. Feedback and Loop Trace for evidence.
7. Long-Run Growth for useful backlog renewal.
8. Harness Repair for runner/process defects.
9. Stopper Policy for unsafe or unverifiable work.

## Frozen Non-Goals

Do not expand v1 toward:

- general agent OS,
- runtime DSL,
- self-modifying CI interpreter,
- unbounded protocol growth,
- local-first execution replacing CI,
- multi-agent orchestration beyond handoff prompts.

## Change Admission Rule

A future change is allowed only if it strengthens one of the v1 core responsibilities without adding a new architectural plane.

Allowed examples:

- clearer operation ledger checks,
- better progress consistency validation,
- simpler runner prompt wording,
- README and example cleanup,
- safer stopper conditions.

Rejected examples:

- more generalized runtime execution,
- CI-as-interpreter features,
- new DSL syntax,
- recursive self-modification loops,
- additional agent orchestration layers.

## Stability Contract

The stable contract is:

```text
product idea or existing repo
  -> bootstrap runner docs
  -> stop for handoff
  -> select first TODO
  -> declare operation state
  -> create one branch and one PR
  -> use CI as VERIFY
  -> update feedback, trace, and progress
  -> run review/repair/growth only when due
  -> re-read state
```

The project should optimize this contract for reliability and clarity, not broaden it.
