# Architecture Overview

This document freezes the GitHub Loop Runner architecture at **GitHub Loop Engine v1**.

The project is intentionally **not** an agent OS, runtime DSL, or self-modifying CI framework. It is a stable GitHub-only loop engine for preparing a repository, handing work to an agent, and executing milestone PR loops safely.

## V1 Scope

GitHub Loop Engine v1 has four core responsibilities:

1. Prepare a repository with runner docs and progress state.
2. Stop at a Handoff Decision before product work starts.
3. Execute one milestone per branch/PR through GitHub connector APIs and CI.
4. Keep the loop safe and useful through operation state, coding skill gates, controlled research intake, feedback, trace, review, repair, and long-run backlog renewal.

## Core System Layers

### 1. Control Layer

Prevents unsafe or ambiguous work.

- Handoff Decision
- GitHub Operation Ledger
- Stopper Policy

### 2. Execution Layer

Runs the smallest useful GitHub loop.

- `SKILL.md` execution protocol
- `docs/progress.md` as state source
- GitHub connector operations
- one branch / one PR / CI / merge
- Every-PR Coding Skill Gate

### 3. Verification Layer

Keeps the loop auditable without turning CI into a runtime interpreter.

- CI as VERIFY
- `scripts/validate_skill.py`
- optional generated-repo sanity checks

### 4. Planning Layer

Keeps long-running work useful without unbounded expansion.

- Long-Run Growth Loop
- Controlled Research Intake
- Review and Renewal Loop
- Harness Repair Loop

### 5. Evidence Layer

Records why the runner acted.

- Feedback Taxonomy
- Loop Trace
- Loop Hypotheses
- research absorption and rejection records

## Loop Engineering Primitive Mapping

Stable v1 maps common loop-engineering primitives into a narrow GitHub-only model:

| Primitive | Stable v1 mapping | Boundary |
| --- | --- | --- |
| Automation | Human, GitHub, or external trigger | v1 does not own cron, webhook daemons, or schedulers. |
| Worktree | GitHub branch + PR isolation | local worktree managers are out of scope. |
| Skills | `SKILL.md` + references + Every-PR Coding Skill Gate | skills guide execution; they do not create a runtime DSL. |
| Plugins / MCP | GitHub connector + CI | no general MCP registry in v1. |
| Sub-agents | Maker/Checker discipline | no multi-agent runtime required. |
| Memory | Markdown state files: progress, trace, feedback, hypotheses, ledger | no database memory in v1. |

## Frozen Non-Goals

The following are explicitly out of scope for v1:

- general agent OS,
- runtime DSL expansion,
- self-modifying CI interpreter,
- manifest-as-program execution,
- unbounded protocol growth,
- local-first execution replacing CI,
- multi-agent orchestration beyond handoff prompts,
- broad research on every PR,
- scheduler or daemon ownership,
- general MCP registry,
- local worktree manager,
- database-backed memory.

## Stable Data Flow

1. Read `docs/progress.md`, handoff state, ledger state, feedback, and trace.
2. Apply long-run growth only when due.
3. Run research intake only when cadence or a bounded domain/architecture decision requires it.
4. Select the first TODO milestone.
5. Run the Every-PR Coding Skill Gate.
6. Declare GitHub operation state.
7. Create one clean branch and one PR.
8. Use CI as VERIFY.
9. Record feedback and trace.
10. Merge or block.
11. Re-read progress.

## Design Principle

The system prioritizes:

- clarity over abstraction,
- deterministic GitHub operations,
- explicit mutation control,
- CI-driven verification,
- `docs/progress.md` as the state source,
- useful long-run planning without busywork,
- controlled research absorption without scope drift,
- stopping before unsafe work.

## Change Policy

Future changes should preserve v1 scope. New protocols should be rejected unless they directly strengthen one of the four core responsibilities above.
