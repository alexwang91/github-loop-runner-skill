---
name: github-loop-runner
description: Use when the user wants to bootstrap or continue a GitHub-only autonomous development loop, initialize a repository from a product idea with agent instructions and runner docs, seed docs/autonomous-runner.md docs/progress.md docs/next-steps-plan.md, add review-and-renewal planning loops, structured feedback taxonomy, or drive milestone PRs with the GitHub connector and CI instead of local clone or package-manager access.
---

# GitHub Loop Runner

## Overview

Turn a product idea or existing GitHub repository into an autonomous, CI-verified milestone loop. The GitHub connector is the working surface: read files, write branches, open PRs, inspect CI, merge, update progress, classify feedback, periodically review completed work, renew the plan, then repeat.

Use this skill in four modes:

- **Bootstrap**: seed a repository with agent instructions, engineering principles, plan, progress, feedback taxonomy, loop trace, review loop, harness repair loop, loop hypotheses, stopper policy, and runner protocol.
- **Loop**: execute milestone PRs from an existing runner repository.
- **Review**: inspect completed work, summarize feedback trends, renew the plan, or decide whether the runner should stop.
- **Prompt**: produce the final copy-paste prompt for a GitHub-only runner.

## Capability Probe

Use the GitHub connector for repository operations. Do not ask the user to confirm the connector just because the skill starts. Probe capabilities quietly: if the connector is callable, continue; if the runtime has tool discovery, discover/load GitHub tools; if no GitHub read/write path exists, then report the missing capability.

Allowed GitHub operations include repository metadata, file fetch/search, branch creation, file create/update/delete, blob/tree/commit/ref writes, PR creation, PR metadata, changed-file listing, commit status/check inspection, auto-merge, and merge.

Do not use local `git clone`, local package managers, or local test commands for the target repository. In this skill, verification belongs to CI. If CI is unavailable and local verification is forbidden, mark the affected milestone `BLOCKED` with the missing verification channel.

The current connector may not expose a create-repository operation. If no create-repo tool exists, ask the user for an existing empty `owner/name` repository or for a repository where the GitHub App is installed. Do not pretend a repo was created.

## Source Workflow Map

Make these source skill systems visible in the generated repository. If equivalent skills are installed in the current runtime, use them while bootstrapping. If not, translate their workflow into repo docs so future agents can still follow it.

| Source | Translate into repo artifacts |
| --- | --- |
| `mattpocock/skills` | Alignment before building, shared project language, ADRs for hard decisions, and vertical-slice issues/milestones. Encode in `AGENTS.md`, `docs/development-principles.md`, and milestone wording. |
| `obra/superpowers` | Brainstorming, writing-plans, TDD, code review, and finishing-branch discipline. Encode as the "Workflow Discipline" agents follow before every milestone PR. |
| `multica-ai/andrej-karpathy-skills` | Think before coding, simplicity first, surgical changes, and goal-driven verification. Encode as guardrails in runner docs and PR checklist. |

## Optional Skill Invocation Map

If these skills are installed in the current runtime, invoke or follow them explicitly while bootstrapping and planning. If they are not installed, do not block; write their discipline into the generated repo docs.

| Phase | Prefer installed skill | Fallback encoded in repo docs |
| --- | --- | --- |
| Align product intent and terms | `$grill-with-docs` or `/grill-with-docs` | Clarify goal, vocabulary, open questions, and ADR-worthy decisions. |
| Slice the plan | `$to-issues` or `/to-issues` | Convert the plan into vertical milestone rows and acceptance criteria. |
| Brainstorm tradeoffs | `$brainstorming` or `/brainstorming` | Explore options before committing to the implementation shape. |
| Write implementation plan | `$writing-plans` or `/writing-plans` | Write concrete steps with verification for each milestone. |
| Behavior changes | `$test-driven-development` or `/test-driven-development` | Define the failing test, eval, or CI assertion before implementation. |
| Review PR work | `$requesting-code-review` or `/requesting-code-review` | Review diff against plan, acceptance criteria, and guardrails. |
| Finish branch | `$finishing-a-development-branch` or `/finishing-a-development-branch` | Merge only after CI is green, progress is updated, and no blocked guardrail remains. |

## Bootstrap Workflow

1. Resolve the target repository, base branch, and product idea.
2. Run the capability probe. Ask the user only for missing repository identity, GitHub App access, or an initialized empty repo when the connector cannot proceed.
3. Read `references/repo-scaffold.md`, `references/feedback-taxonomy.md`, `references/loop-trace.md`, `references/review-and-renewal-loop.md`, `references/harness-repair-loop.md`, `references/loop-hypotheses.md`, `references/stopper-policy.md`, and `references/loop-review-template.md`.
4. Convert the idea and workflow references into:
   - `AGENTS.md`
   - `docs/autonomous-runner.md`
   - `docs/progress.md`
   - `docs/next-steps-plan.md`
   - `docs/development-principles.md`
   - `docs/feedback-taxonomy.md`
   - `docs/feedback-log.md`
   - `docs/loop-trace.md`
   - `docs/review-and-renewal-loop.md`
   - `docs/harness-repair-loop.md`
   - `docs/loop-hypotheses.md`
   - `docs/stopper-policy.md`
   - `docs/loop-review.md`
   - `.github/pull_request_template.md`
   - `.github/workflows/verify.yml`
5. Seed the files through the GitHub connector on a bootstrap branch and open one PR.
6. Run CI through the PR checks. The initial docs-only workflow is acceptable only for the bootstrap PR; the first product milestone must add real stack-specific checks.
7. Return the PR URL/status and a runner prompt generated from `references/runner-prompt.md`.

## Loop Workflow

1. Fetch `docs/autonomous-runner.md`, `docs/progress.md`, `docs/feedback-taxonomy.md`, `docs/feedback-log.md`, `docs/loop-trace.md`, `docs/review-and-renewal-loop.md`, `docs/harness-repair-loop.md`, `docs/loop-hypotheses.md`, and `docs/stopper-policy.md` from the base branch. Treat the runner doc as the standing protocol, `progress.md` as the milestone state source, and `loop-trace.md` as evidence rather than state.
2. Determine whether the Review and Renewal Loop is due before selecting implementation work. A review is due when the configured number of milestones has completed, no `TODO` remains, a milestone is blocked or repeatedly fails CI, repeated harness-layer failures appear, a higher-risk release step is next, or the user asks for review.
3. If review is due, run the Review and Renewal Loop: summarize completed work, summarize feedback trends, summarize loop trace evidence, evaluate active hypotheses, compare repo state against the product goal, detect gaps and blockers, update `docs/loop-review.md`, update the plan only with specific verifiable milestones, and apply the stopper policy.
4. If the stopper policy says to stop, classify the stopper result using `docs/feedback-taxonomy.md`, append it to `docs/feedback-log.md` when possible, stop, and report the reason. If the review adds work, re-fetch `docs/progress.md` before selecting a milestone.
5. If repeated feedback or trace evidence points to `observation`, `context`, `planning`, `control_loop`, `tool_action`, `state_store`, `verification`, or `governance` root-cause layers, run the Harness Repair Loop before adding more feature work. Harness repair should be a dedicated PR when possible and must not include product feature changes.
6. Fetch `docs/next-steps-plan.md` and `docs/development-principles.md` after identifying the next milestone, then read the matching milestone section and any directly referenced ADRs.
7. Find the first `TODO` row in `docs/progress.md`. Skip `DONE`, `BLOCKED`, `DEFERRED`, and `CANCELLED`. Do not trust hard-coded milestone text from the user if the current file says otherwise.
8. If no `TODO` remains after a final review, stop and report whether all rows are `DONE`, blocked, or intentionally complete with no meaningful new work.
9. Append a `docs/loop-trace.md` entry when selecting the milestone.
10. For the selected milestone:
   - **PLAN**: apply the Workflow Discipline from `docs/development-principles.md`, then write the smallest vertical-slice plan from the milestone acceptance criteria.
   - **BRANCH**: create `m<N>-<slug>` from the latest base branch.
   - **BUILD**: edit only necessary files through the GitHub connector. Use structured file APIs; avoid temporary `noop`, `dummy`, `x`, `y`, or `tmp/*` files.
   - **VERIFY**: open or update the PR and use CI checks as the verification loop. After each CI result, classify feedback with `docs/feedback-taxonomy.md`, include the harness root-cause layer, append the entry to `docs/feedback-log.md`, append an event to `docs/loop-trace.md`, and choose only allowed next actions. If CI fails, fix the true cause. Never weaken tests, assertions, evals, or acceptance criteria to get green.
   - **REVIEW**: classify PR review comments, scope drift, weak verification, and merge blockers before deciding the next action.
   - **MERGE**: merge only after required checks are green and no blocking feedback remains.
11. Ensure the milestone row becomes `DONE` on the base branch and that `docs/loop-trace.md` links the milestone, PR, CI result, feedback IDs, and progress update.
12. Return to step 1. Re-fetch `docs/progress.md` from base before choosing the next milestone.

## Feedback Taxonomy

Feedback Taxonomy is the local control protocol for observations. Use `docs/feedback-taxonomy.md` to classify every meaningful PR update, CI result, review result, merge attempt, review-loop decision, and stopper decision.

A feedback entry should record source, type, severity, milestone, evidence, root cause, harness root-cause layer, allowed next actions, forbidden next actions, and the runner decision. Blocking feedback must be resolved or marked blocked before the runner advances. Terminal feedback stops the runner with a report.

During the Review and Renewal Loop, read `docs/feedback-log.md` and `docs/loop-trace.md` and summarize patterns such as repeated CI failures, scope violations, weak verification, trace gaps, merge blockers, regressions, harness defects, invalidated hypotheses, and successful patterns. Use these trends to decide whether to add verification-hardening, blocker-removal, regression-fix, or harness-repair milestones.

## Loop Trace

Loop Trace is the local observability protocol. Use `docs/loop-trace.md` to append evidence for selected milestones, context read, branch and PR actions, CI results, feedback IDs, decisions, attempt counts, review-loop triggers, harness repair decisions, hypothesis updates, and stopper decisions.

`docs/loop-trace.md` is evidence, not state. Do not choose milestones from it. Continue to use `docs/progress.md` as the state source.

## Review and Renewal Loop

The Review and Renewal Loop is a planning loop, not a feature implementation loop. It keeps the runner from stopping only because the original plan ran out or because the original plan became stale.

During review, read the latest progress, feedback log, loop trace, loop hypotheses, recent merged PRs where available, current plan, development principles, CI/check history where available, and any generated review file. Produce or update `docs/loop-review.md` with:

- review metadata: trigger, date, base branch, completed milestones since last review,
- completed work summary,
- feedback trends since the last review,
- loop trace summary,
- hypothesis results since the last review,
- harness repair candidates,
- current state assessment,
- gaps, regressions, blockers, and verification weaknesses,
- plan updates applied,
- stopper assessment,
- decision: continue, continue with new milestones, blocked, or stop.

Only add renewed work when it is specific, verifiable, non-duplicative, and useful. Durable process changes, verification-hardening milestones, and harness repairs should be linked to `docs/loop-hypotheses.md` unless they fix a simple malformed reference or typo. Do not create vague cleanup, polish, churn, placeholders, dummy tests, or work whose only purpose is to keep the loop alive.

## Harness Repair Loop

The Harness Repair Loop fixes the runner protocol, scaffold, CI harness, PR template, feedback taxonomy, review loop, stopper policy, or milestone slicing rules when evidence shows repeated harness-layer failure. It is not product feature work.

Run the Harness Repair Loop when repeated `trace_gap`, `protocol_violation`, `scope_violation`, `weak_verification`, process-caused `merge_blocked`, inconsistent progress state, invalidated process hypotheses, or repeated non-product root-cause layers appear. Prefer a dedicated harness repair PR and record the repair in `docs/loop-trace.md`, `docs/feedback-log.md`, and `docs/loop-hypotheses.md`.

## Hypothesis-Gated Renewal

Hypothesis-Gated Renewal means new durable process guidance starts as a falsifiable hypothesis. When the runner adds a harness repair, verification-hardening milestone, review-cadence change, feedback taxonomy change, or milestone-slicing rule, record the hypothesis in `docs/loop-hypotheses.md` with source evidence, expected outcome, measurement window, success criteria, and rollback condition.

Review active hypotheses before adding more work. Promote validated hypotheses into durable runner guidance, invalidate or roll back hypotheses that repeat the same failure pattern, and stop rather than keeping unmeasurable process changes.

## Engineering Principles

Carry these into every bootstrap plan and loop execution:

- Align before building: extract the user's real goal, define terms, and record decisions when ambiguity matters.
- Work in vertical slices: each milestone should be independently reviewable, demoable, and verifiable.
- Use TDD or eval-first thinking where code behavior changes: define the failing or objective check before implementation.
- Keep code simple: avoid speculative abstractions, one-off frameworks, and broad rewrites.
- Make surgical changes: every changed line should trace to the current milestone.
- Treat CI/evals as specifications: red checks mean investigate and fix real behavior.
- Classify feedback before reacting: observations become allowed or forbidden next actions through the taxonomy.
- Keep humans in the loop for sensitive access, live services, security boundaries, and large architectural pivots.

## Stop Conditions

Stop and report instead of forcing progress when:

- No GitHub connector path can read/write the repository.
- CI is missing or cannot report verification, and local verification is unavailable by design.
- The milestone requires sensitive access or a live service that is not mockable.
- The change crosses a security boundary not covered by the plan.
- CI remains red across multiple fix attempts and the root cause is outside the milestone.
- A previously `DONE` milestone regresses.
- Required trace evidence is missing and cannot be safely reconstructed.
- Repeated harness defects cannot be repaired inside the current operating scope.
- An active process hypothesis is invalidated and no rollback path exists.
- The Review and Renewal Loop finds no meaningful, non-duplicative, verifiable new work.

When blocked, update `docs/progress.md` only if you can do so safely through a PR. Mark the row `BLOCKED`, classify the feedback, and add a specific note describing the missing tool, CI signal, or decision.

## Output Contract

For bootstrap work, report repository, branch/PR, files seeded, CI status, and the generated runner prompt or its location.

For loop work, report the current milestone selected from fresh `docs/progress.md`, feedback classification summary with harness root-cause layers, loop trace updates, whether a Review and Renewal Loop or Harness Repair Loop ran, PR number/status, CI result, whether progress was updated, and the next state after re-reading progress.

For review-only work, report the review trigger, completed work since the last review, feedback trends, loop trace summary, hypothesis results, harness repair candidates, gaps and blockers found, plan updates made or proposed, and stopper decision.

For prompt-only work, read `references/runner-prompt.md`, fill placeholders, and return the prompt directly.
