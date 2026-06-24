# Codebase Localization Reference

Use this reference before editing product code in a generated repository.

## Purpose

Before implementation, the runner should identify the smallest relevant code area. This reduces scope drift, unrelated edits, and weak verification.

## Generated Repo File

Generate `docs/codebase-localization.md`.

## When To Run

Run localization before each implementation PR, before large refactors, and before regression fixes.

## Localization Record Format

```yaml
localization:
  id: L-0001
  milestone: M0
  candidate_files:
    - path: src/app.ts
      reason: likely app entrypoint
      confidence: medium
  selected_files:
    - path: src/app.ts
      reason: smallest file that can satisfy acceptance criteria
  rejected_files:
    - path: src/theme.css
      reason: out of scope for this milestone
  related_tests:
    - path: tests/app.test.ts
      reason: verifies app entrypoint
  decision:
    summary: edit app entrypoint and add smoke test only
    scope_risk: low
```

## Required Fields

- milestone,
- candidate files,
- selected files,
- rejected files when applicable,
- related tests or verification files,
- decision summary,
- scope risk.

## Rules

1. Do not edit files that were not selected unless new evidence is added.
2. If localization confidence is low, inspect more files before implementation.
3. If selected files exceed the milestone scope, split the milestone.
4. Link localization records from PR descriptions and loop trace.
5. Weak or missing localization should become feedback.
