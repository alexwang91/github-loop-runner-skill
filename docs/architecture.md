# Architecture Overview

This document defines the system architecture of the GitHub Loop Runner skill.

## System Layers

### 1. Control Plane
Responsible for safe execution control and stopping conditions.

- Handoff Decision
- GitHub Operation Ledger
- Stopper Policy

### 2. Execution Plane
Responsible for performing GitHub-based development loops.

- SKILL.md execution protocol
- progress.md as single state source
- GitHub connector operations
- CI as VERIFY

### 3. Evaluation Plane
Responsible for correctness and process quality.

- Feedback Taxonomy
- Loop Trace
- Agent Judge Loop
- Loop Acceptance Tests

### 4. Planning Plane
Responsible for long-term expansion and backlog management.

- Long-Run Growth Loop
- Growth Candidate Selection
- Review and Renewal Loop

### 5. Memory Plane
Responsible for durable learning and compression.

- Runner Memory
- Loop Hypotheses

### 6. Localization Plane
Responsible for scoping changes before execution.

- Codebase Localization

## Data Flow

1. Read progress + ledger + trace
2. Apply long-run growth policy
3. Localize target scope
4. Execute single vertical slice PR
5. Run CI as VERIFY
6. Update feedback + trace + memory
7. Re-evaluate planning state

## Design Principle

The system prioritizes:

- single source of truth (progress.md)
- explicit mutation control (operation ledger)
- long-run backlog sustainability
- CI-driven verification
- strict GitHub-only execution boundary
