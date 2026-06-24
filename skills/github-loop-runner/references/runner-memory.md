# Runner Memory Reference

Use this reference when a generated repository is expected to run across many PRs.

## Purpose

Long-running agents need compact memory. Feedback logs and loop traces can grow too large. Runner Memory stores durable facts, repeated patterns, rejected approaches, useful decisions, and unresolved blockers in a compact format.

## Generated Repo File

Generate `docs/runner-memory.md`.

## Memory Cycle

Use a write, manage, read loop:

1. Write useful facts after PRs, reviews, judge reports, repairs, and candidate selection.
2. Manage memory every configured interval by compacting repeated events into stable lessons.
3. Read relevant memory before milestone selection, growth review, deep review, codebase localization, harness repair, and final review.

## Default Policy

```yaml
runner_memory:
  compaction_interval_prs: 5
  read_before:
    - milestone_selection
    - growth_review
    - deep_review
    - codebase_localization
    - harness_repair
    - final_review
```

## Memory Entry Format

```yaml
memory_entry:
  id: MEM-0001
  type: repeated_failure
  source_refs:
    feedback: [F-0001]
    trace: [T-0001]
    judge: [J-0001]
  summary: CI failures repeatedly came from missing smoke checks.
  durable_lesson: Add smoke checks before marking UI flow milestones complete.
  applies_to:
    - verification
    - product_surface
  read_before:
    - milestone_selection
    - growth_review
```

## Memory Types

- `product_goal`
- `architecture_decision`
- `successful_pattern`
- `repeated_failure`
- `rejected_approach`
- `unresolved_blocker`
- `verification_lesson`
- `harness_lesson`

## Rules

1. Do not copy the full trace into memory.
2. Keep memory compact and actionable.
3. Link memory to source feedback, trace, judge, candidate, or review IDs.
4. Read relevant memory before generating new milestones.
5. Update memory after every 5 merged PRs by default.
