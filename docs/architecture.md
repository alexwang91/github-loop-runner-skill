# Architecture Overview

This document freezes the GitHub Loop Runner architecture at **GitHub Loop Engine v1**.

The project is intentionally **not** an agent OS, runtime DSL, or self-modifying CI framework. It is a stable GitHub-only loop engine for preparing a repository, handing work to an agent, and executing milestone PR loops safely.

## V1 Scope

GitHub Loop Engine v1 has four core responsibilities:

1. Prepare a repository with runner docs and progress state.
2. Stop at a Handoff Decision before product work starts.
3. Execute one milestone per branch/PR through GitHub connector APIs and CI.
4. Keep the loop safe through operation state, feedback, trace, review, repair, and long-run backlog renewal.

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

### 3. Verification Layer

Keeps the loop auditable without turning CI into a runtime interpreter.

- CI as VERIFY
- `scripts/validate_skill.py`
- optional generated-repo sanity checks

### 4. Planning Layer

Keeps long-running work useful without unbounded expansion.

- Long-Run Growth Loop
- Review and Renewal Loop
- Harness Repair Loop

### 5. Evidence Layer

Records why the runner acted.

- Feedback Taxonomy
- Loop Trace
- Loop Hypotheses

## Frozen Non-Goals

The following are explicitly out of scope for v1:

- general agent OS,
- runtime DSL expansion,
- self-modifying CI interpreter,
- manifest-as-program execution,
- unbounded protocol growth,
- local-first execution replacing CI,
- multi-agent orchestration beyond handoff prompts.

## Stable Data Flow

1. Read `docs/progress.md`, handoff state, ledger state, feedback, and trace.
2. Apply long-run growth only when due.
3. Select the first TODO milestone.
4. Declare GitHub operation state.
5. Create one clean branch and one PR.
6. Use CI as VERIFY.
7. Record feedback and trace.
8. Merge or block.
9. Re-read progress.

## Design Principle

The system prioritizes:

- clarity over abstraction,
- deterministic GitHub operations,
- explicit mutation control,
- CI-driven verification,
- `docs/progress.md` as the state source,
- useful long-run planning without busywork,
- stopping before unsafe work.

## Change Policy

Future changes should preserve v1 scope. New protocols should be rejected unless they directly strengthen one of the four core responsibilities above.
