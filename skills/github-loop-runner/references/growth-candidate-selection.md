# Growth Candidate Selection Reference

Use this reference during Long-Run Growth Review and deep review.

## Purpose

Long-run planning should not append the first backlog the model invents. The runner should generate multiple candidate milestone batches, score them, select one, and record why alternatives were rejected.

## Generated Repo File

Generate `docs/growth-candidates.md`.

## Candidate Generation

During deep review, generate at least three candidate batches when enough information exists:

- `product_surface_first`
- `verification_hardening_first`
- `operability_or_architecture_first`

Each candidate batch should contain 8-15 milestones unless the project state justifies fewer.

## Candidate Batch Format

```yaml
growth_candidate:
  id: C-0001
  review_id: R-0001
  strategy: product_surface_first
  milestones:
    - id: M12
      title: Add board empty-state onboarding
      category: product_surface
      impact: high
      reason_from_review: Missing first-run path.
      verification: CI smoke test and docs review.
      one_pr_fit: true
  score:
    product_impact: 5
    verification_strength: 4
    risk: 2
    novelty: 4
    one_pr_fit: 5
    dependency_safety: 5
  selected: true
  reason: Highest product impact with safe verification.
```

## Scoring Rules

Score from 1 to 5:

- product impact,
- verification strength,
- implementation risk,
- novelty versus existing backlog,
- one-PR fit,
- dependency safety.

Select the batch with the best balance of impact, verification, and safety.

## Rejection Rules

Reject candidates when they:

- duplicate existing TODO work,
- rely on unavailable access,
- contain vague cleanup,
- lack verification,
- require multi-PR work without splitting,
- lower existing guardrails.

## Runner Rules

1. Store selected and rejected candidates in `docs/growth-candidates.md`.
2. Append only the selected candidate batch to `docs/progress.md`.
3. Convert rejected candidate reasons into memory entries when useful.
4. If no candidate is good enough, run deep review again from a different perspective or request human input.
