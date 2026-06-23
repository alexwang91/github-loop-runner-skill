---
name: github-loop-runner
description: Use when the user wants to bootstrap or continue a GitHub-only autonomous development loop, initialize a repository from a product idea with agent instructions and runner docs, seed docs/autonomous-runner.md docs/progress.md docs/next-steps-plan.md, or drive milestone PRs with the GitHub connector and CI instead of local clone or package-manager access.
---

# GitHub Loop Runner

## Overview

Turn a product idea or existing GitHub repository into an autonomous, CI-verified milestone loop. The GitHub connector is the working surface: read files, write branches, open PRs, inspect CI, merge, update progress, then repeat.

Use this skill in three modes:

- **Bootstrap**: the user has an idea and wants a GitHub repo seeded with agent instructions, engineering principles, plan, progress, and runner protocol.
- **Loop**: the repo already has `docs/autonomous-runner.md`, `docs/progress.md`, and `docs/next-steps-plan.md`, and the user wants autonomous milestone execution.
- **Prompt**: the user wants the final copy-paste prompt for a GitHub-only runner.

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

1. Resolve the target:
   - Repository: `owner/name`.
   - Base branch: use the repo default branch unless the user specifies one.
   - Product idea: clarify only missing facts that would change the milestone plan or repo identity.
2. Run the capability probe. Ask the user only for missing repo identity, GitHub App access, or an initialized empty repo when the connector cannot proceed.
3. Read `references/repo-scaffold.md`.
4. Convert the idea, Source Workflow Map, and Optional Skill Invocation Map into:
   - `AGENTS.md`
   - `docs/autonomous-runner.md`
   - `docs/progress.md`
   - `docs/next-steps-plan.md`
   - `docs/development-principles.md`
   - `.github/pull_request_template.md`
   - `.github/workflows/verify.yml`
5. Seed through the GitHub connector:
   - For an existing repo, create `bootstrap-agent-loop` from the base branch, write the files, and open one PR.
   - For an empty repo where branch creation fails, try `create_file` on the default branch if the connector supports it. If GitHub rejects writes because the repo has no initial branch, ask the user to initialize the repo with a README, then resume.
6. Run CI through the PR checks. The initial docs-only workflow is acceptable only for the bootstrap PR; the first product milestone must add real stack-specific checks.
7. Return the PR URL/status and a runner prompt generated from `references/runner-prompt.md`.

## Loop Workflow

1. Fetch `docs/autonomous-runner.md` and `docs/progress.md` from the base branch. Treat the runner doc as the standing protocol and `progress.md` as the only state source.
2. Fetch `docs/next-steps-plan.md` and `docs/development-principles.md` after identifying the next milestone, then read the matching milestone section and any directly referenced ADRs.
3. Find the first `TODO` row in `docs/progress.md`. Skip `DONE` and `BLOCKED`. Do not trust hard-coded milestone text from the user if the current file says otherwise.
4. If no `TODO` remains, stop and report whether all rows are `DONE` or some are `BLOCKED`.
5. For the selected milestone:
   - **PLAN**: apply the Workflow Discipline from `docs/development-principles.md`, then write the smallest vertical-slice plan from the milestone acceptance criteria.
   - **BRANCH**: create `m<N>-<slug>` from the latest base branch.
   - **BUILD**: edit only necessary files through the GitHub connector. Use structured file APIs; avoid temporary `noop`, `dummy`, `x`, `y`, or `tmp/*` files.
   - **VERIFY**: open or update the PR and use CI checks as the verification loop. If CI fails, fix the true cause. Never weaken tests, assertions, evals, or acceptance criteria to get green.
   - **MERGE**: merge only after required checks are green.
6. Ensure the milestone row becomes `DONE` on the base branch:
   - Prefer including the `docs/progress.md` status update in the milestone PR after implementation is verified, then let CI run green again before merge.
   - If the implementation PR was merged without the progress update, immediately create a small progress PR, merge it after CI, and only then continue.
7. Return to step 1. Re-fetch `docs/progress.md` from base before choosing the next milestone.

## Engineering Principles

Carry these into every bootstrap plan and loop execution:

- Align before building: extract the user's real goal, define terms, and record decisions when ambiguity matters.
- Work in vertical slices: each milestone should be independently reviewable, demoable, and verifiable.
- Use TDD or eval-first thinking where code behavior changes: define the failing or objective check before implementation.
- Keep code simple: avoid speculative abstractions, one-off frameworks, and broad rewrites.
- Make surgical changes: every changed line should trace to the current milestone.
- Treat CI/evals as specifications: red checks mean investigate and fix real behavior.
- Keep humans in the loop for trust boundaries, credentials, external sends, destructive actions, and large architectural pivots.

## Stop Conditions

Stop and report instead of forcing progress when:

- No GitHub connector path can read/write the repository.
- CI is missing or cannot report verification, and local verification is unavailable by design.
- The milestone requires credentials, production access, or an external provider that is not mockable.
- The change crosses a trust/security boundary not covered by the plan.
- CI remains red across multiple fix attempts and the root cause is outside the milestone.
- A previously `DONE` milestone regresses.

When blocked, update `docs/progress.md` only if you can do so safely through a PR. Mark the row `BLOCKED` and add a specific note describing the missing credential, tool, CI signal, or decision.

## Output Contract

For bootstrap work, report:

- Repository and branch/PR.
- Files seeded.
- CI status.
- The generated runner prompt or its location.

For loop work, report:

- Current milestone selected from fresh `docs/progress.md`.
- PR number/status and CI result.
- Whether `docs/progress.md` on base was updated.
- The next state after re-reading progress.

For prompt-only work, read `references/runner-prompt.md`, fill placeholders, and return the prompt directly.
