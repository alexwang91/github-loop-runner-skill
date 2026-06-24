---
name: github-loop-runner
description: Use when the user wants to bootstrap or continue a GitHub-only autonomous development loop with CI verification, docs/progress.md as state, Feedback Taxonomy, Loop Trace, Harness Repair Loop, Hypothesis-Gated Renewal, harness-layer root cause classification, and milestone PRs through the GitHub connector instead of local clone or package-manager access.
---

# GitHub Loop Runner

## Overview

Turn a product idea or existing repository into a GitHub-only milestone loop. The runner reads and writes through the GitHub connector, verifies through CI, uses `docs/progress.md` as the state source, records feedback and trace evidence, repairs harness defects, gates process changes through hypotheses, then repeats.

Load these references when bootstrapping or running:

- `references/repo-scaffold.md`
- `references/runner-prompt.md`
- `references/feedback-taxonomy.md`
- `references/loop-trace.md`
- `references/review-and-renewal-loop.md`
- `references/harness-repair-loop.md`
- `references/loop-hypotheses.md`
- `references/stopper-policy.md`
- `references/loop-review-template.md`

## Capability Probe

Use the GitHub connector for repository operations. Do not ask the user to confirm connector access when the connector is callable. If the connector cannot read or write the target repository, report the missing repository, permission, or GitHub App installation.

Allowed operations include repository metadata, file fetch/search, branch creation, file create/update, blob/tree/commit/ref writes, PR creation, PR metadata, changed-file listing, CI/check inspection, and merge.

Do not require local `git clone`, package managers, or local test commands for target-repo work. In this skill, CI is VERIFY. If CI is unavailable and no approved verification channel exists, mark the milestone `BLOCKED` with evidence.

## Source Workflow Map

| Source | Translate into repo artifacts |
| --- | --- |
| `mattpocock/skills` | Alignment before building, shared project language, ADRs, and vertical-slice milestones. |
| `obra/superpowers` | Brainstorming, writing-plans, TDD/eval-first, review, and finishing-branch discipline. |
| `multica-ai/andrej-karpathy-skills` | Think before coding, simplicity first, surgical changes, and explicit success criteria. |

## Optional Skill Invocation Map

| Phase | Prefer installed skill | Fallback encoded in repo docs |
| --- | --- | --- |
| Align product intent and terms | `$grill-with-docs` or `/grill-with-docs` | Clarify goal, vocabulary, open questions, and ADR-worthy decisions. |
| Slice the plan | `$to-issues` or `/to-issues` | Convert the plan into vertical milestone rows and acceptance criteria. |
| Brainstorm tradeoffs | `$brainstorming` or `/brainstorming` | Explore options before committing to the implementation shape. |
| Write implementation plan | `$writing-plans` or `/writing-plans` | Write concrete steps with verification for each milestone. |
| Behavior changes | `$test-driven-development` or `/test-driven-development` | Define the failing test, eval, or CI assertion before implementation. |
| Review PR work | `$requesting-code-review` or `/requesting-code-review` | Review diff against plan, acceptance criteria, trace evidence, and guardrails. |
| Finish branch | `$finishing-a-development-branch` or `/finishing-a-development-branch` | Merge only after CI is green, progress and loop trace are updated, and no blocker remains. |

## Bootstrap Workflow

1. Resolve the target repository, base branch, and product goal.
2. Run the Capability Probe.
3. Read all reference files listed above.
4. Generate `AGENTS.md`, runner docs, progress, plan, development principles, feedback taxonomy/log, Loop Trace, Review and Renewal Loop, Harness Repair Loop, loop hypotheses, stopper policy, loop review, PR template, and CI scaffold.
5. Open one bootstrap PR through the GitHub connector.
6. Let CI verify. Docs-only CI is acceptable only for bootstrap; the first product milestone must add stack-specific checks.

## Loop Workflow

1. Fetch `docs/autonomous-runner.md`, `docs/progress.md`, `docs/feedback-taxonomy.md`, `docs/feedback-log.md`, `docs/loop-trace.md`, `docs/review-and-renewal-loop.md`, `docs/harness-repair-loop.md`, `docs/loop-hypotheses.md`, and `docs/stopper-policy.md`.
2. Decide whether review, repair, or hypothesis validation is due before selecting implementation work.
3. Run the Review and Renewal Loop when no TODO remains, the review interval is reached, CI or feedback repeats, trace evidence is missing, a hypothesis needs a decision, or the user asks.
4. Run the Harness Repair Loop when repeated `trace_gap`, `protocol_violation`, `weak_verification`, `harness_defect`, missing PR evidence, or inconsistent state appears. Repair only runner docs, feedback taxonomy, loop trace format, review loop rules, stopper policy, PR template, CI scaffold, or milestone slicing rules.
5. Apply Stop Conditions. If stopping, classify feedback, append trace evidence when possible, and report the reason.
6. Re-fetch `docs/progress.md`, select the first `TODO`, and skip `DONE`, `BLOCKED`, `DEFERRED`, and `CANCELLED`.
7. Append a Loop Trace event for milestone selection, branch creation, PR open, CI observation, feedback classification, merge attempt, progress update, review, repair, hypothesis lifecycle event, and stop.
8. Create one branch and one PR for the milestone.
9. Use CI as VERIFY. For every meaningful observation, classify feedback with root-cause layer, allowed next actions, and forbidden next actions.
10. Merge only after CI is green, PR evidence is complete, feedback blockers are resolved, active hypotheses are updated, and progress plus loop trace are current.
11. Re-read `docs/progress.md` before the next milestone.

## Feedback Taxonomy

Feedback Taxonomy controls the runner's next actions. Record source, type, severity, evidence, root cause, harness-layer root cause classification, allowed next actions, forbidden next actions, and runner decision. Classify CI, review, mergeability, progress state, trace gaps, harness defects, hypothesis outcomes, review-loop decisions, and stopper decisions.

## Loop Trace

Loop Trace records observable runner events in `docs/loop-trace.md`. Required events include milestone selection, branch creation, PR open, CI observation, feedback classification, merge attempt, progress update, review, harness repair, hypothesis lifecycle changes, and stop. Missing material trace evidence becomes `trace_gap` feedback.

## Review and Renewal Loop

Review completed milestones, feedback trends, trace coverage, product-goal fit, verification strength, active hypotheses, blockers, and stopper status. Add only specific, useful, non-duplicative, verifiable milestones. Do not add vague cleanup, polish, placeholders, or churn-only work.

## Harness Repair Loop

The Harness Repair Loop repairs repeated runner-harness failures without mixing product feature work into the repair. A valid repair cites evidence, classifies a root-cause layer, changes only allowed harness files, preserves GitHub-only CI verification, and validates through CI or review evidence.

## Hypothesis-Gated Renewal

Hypothesis-Gated Renewal prevents permanent process changes without evidence. Record active hypotheses in `docs/loop-hypotheses.md`, including validation rules, invalidation rules, promotion rules, and rollback rules. Promote only after evidence validates the hypothesis; roll back or stop when evidence invalidates it.

## Engineering Principles

- Align before building.
- Work in vertical slices.
- Use TDD or eval-first thinking where behavior changes.
- Keep code simple.
- Make surgical changes.
- Treat CI/evals as specifications.
- Classify feedback before reacting.
- Keep trace evidence current.
- Gate durable process changes through hypotheses.
- Keep humans in the loop for access, live services, and large architectural pivots.

## Stop Conditions

Stop and report instead of forcing progress when:

- No GitHub connector path can read/write the repository.
- CI is missing or cannot verify work.
- CI exists but required PR or trace evidence is missing and cannot be repaired safely.
- The next step requires access or approval outside the current plan.
- CI remains red after configured fix attempts and the root cause is outside scope.
- Repeated harness defects cannot be safely repaired.
- An active hypothesis is invalidated and no rollback path exists.
- `docs/progress.md` is inconsistent with merged work and cannot be repaired safely.
- A previously `DONE` milestone regresses.
- Review finds no meaningful, non-duplicative, verifiable new work.

## Output Contract

For bootstrap work, report repository, branch/PR, files seeded, CI status, and the runner prompt or its location.

For loop work, report selected milestone, feedback classifications and root-cause layers, review/repair status, trace events, hypothesis changes, PR status, CI result, progress update, and next state after re-reading progress.

For review-only work, report trigger, completed work, feedback trends, trace coverage, gaps, hypotheses, harness repairs, plan updates, and stopper decision.

For prompt-only work, read `references/runner-prompt.md`, fill placeholders, and return the prompt directly.
