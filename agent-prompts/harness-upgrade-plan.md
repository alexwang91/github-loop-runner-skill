# Harness Upgrade Plan For Agent Workers

## Goal

Upgrade `github-loop-runner-skill` so future GitHub-only runners are more observable, diagnosable, and repairable.

This plan does not ask the agent to change the product promise. The runner must still work through GitHub connector operations and CI, with `docs/progress.md` as the milestone state source.

## Non-Negotiable Constraints

- Keep GitHub-only runner behavior.
- Keep CI as the verification channel.
- Keep `docs/progress.md` as the milestone state source.
- Treat `agent-prompts/` as temporary development scaffolding for this repository, not as final downstream runner behavior.
- Do not add local clone, local package-manager, or local test requirements to generated runner protocols.
- Do not weaken tests, assertions, evals, acceptance criteria, or guardrails.
- Do not add vague "cleanup", "polish", or churn-only work.
- Make each change small enough to review in a PR.

## Current Files To Read First

Read these files before editing:

- `README.md`
- `llms.txt`
- `scripts/validate_skill.py`
- `skills/github-loop-runner/SKILL.md`
- `skills/github-loop-runner/references/repo-scaffold.md`
- `skills/github-loop-runner/references/feedback-taxonomy.md`
- `skills/github-loop-runner/references/review-and-renewal-loop.md`
- `skills/github-loop-runner/references/stopper-policy.md`
- `skills/github-loop-runner/references/loop-review-template.md`
- `skills/github-loop-runner/references/runner-prompt.md`

Run this before editing:

```bash
python scripts/validate_skill.py
```

Expected:

```text
Skill validation passed
```

## Milestone 1: Add Loop Trace Protocol

Create `skills/github-loop-runner/references/loop-trace.md`.

Purpose: make runner decisions observable after the fact.

Required sections:

- `Loop Trace Reference`
- `Purpose`
- `Generated Repo File`
- `Trace Entry Format`
- `Required Events`
- `Metrics`
- `Runner Rules`
- `Review Usage`

The generated target-repo file should be `docs/loop-trace.md`.

Update:

- `skills/github-loop-runner/SKILL.md`
- `skills/github-loop-runner/references/repo-scaffold.md`
- `skills/github-loop-runner/references/runner-prompt.md`
- `scripts/validate_skill.py`

The runner should append trace entries when it selects a milestone, creates a branch, opens a PR, observes CI, classifies feedback, attempts merge, updates progress, runs review, or stops.

Verify:

```bash
python scripts/validate_skill.py
```

Suggested commit:

```bash
git add skills/github-loop-runner scripts/validate_skill.py
git commit -m "feat: add loop trace protocol"
```

## Milestone 2: Add Harness-Layer Root Cause Classification

Update `skills/github-loop-runner/references/feedback-taxonomy.md`.

Add allowed root-cause layers:

- `observation`
- `context`
- `planning`
- `control_loop`
- `tool_action`
- `state_store`
- `verification`
- `governance`
- `product_code`
- `unknown`

Add or update feedback types:

- `trace_gap`
- `harness_defect`
- `hypothesis_invalidated`
- `repair_validated`

Update:

- `skills/github-loop-runner/SKILL.md`
- `skills/github-loop-runner/references/loop-review-template.md`
- `scripts/validate_skill.py`

Verify:

```bash
python scripts/validate_skill.py
```

Suggested commit:

```bash
git add skills/github-loop-runner scripts/validate_skill.py
git commit -m "feat: classify feedback by harness layer"
```

## Milestone 3: Add Harness Repair Loop

Create `skills/github-loop-runner/references/harness-repair-loop.md`.

Purpose: make repeated runner-protocol failures repairable without mixing product work into the repair.

Required sections:

- `Harness Repair Loop Reference`
- `Purpose`
- `Trigger Conditions`
- `Inputs`
- `Repair Scope`
- `Forbidden Repairs`
- `Repair Steps`
- `Validation Criteria`
- `Output`

Allowed repair scope:

- runner docs
- feedback taxonomy
- loop trace format
- review loop rules
- stopper policy
- PR template
- CI scaffold
- milestone slicing rules

Forbidden repair scope:

- product feature work
- unrelated refactors
- weakened verification
- deleted tests to get green
- vague process text with no validation criteria

Update:

- `skills/github-loop-runner/SKILL.md`
- `skills/github-loop-runner/references/repo-scaffold.md`
- `skills/github-loop-runner/references/review-and-renewal-loop.md`
- `skills/github-loop-runner/references/runner-prompt.md`
- `scripts/validate_skill.py`

Verify:

```bash
python scripts/validate_skill.py
```

Suggested commit:

```bash
git add skills/github-loop-runner scripts/validate_skill.py
git commit -m "feat: add harness repair loop"
```

## Milestone 4: Add Hypothesis-Gated Renewal

Create `skills/github-loop-runner/references/loop-hypotheses.md`.

Purpose: prevent permanent process changes from being added without evidence.

Required sections:

- `Loop Hypotheses Reference`
- `Purpose`
- `Generated Repo File`
- `Hypothesis Entry Format`
- `When To Create A Hypothesis`
- `Validation Rules`
- `Invalidation Rules`
- `Promotion Rules`
- `Rollback Rules`

The generated target-repo file should be `docs/loop-hypotheses.md`.

Update:

- `skills/github-loop-runner/references/review-and-renewal-loop.md`
- `skills/github-loop-runner/references/repo-scaffold.md`
- `skills/github-loop-runner/references/runner-prompt.md`
- `skills/github-loop-runner/references/loop-review-template.md`
- `scripts/validate_skill.py`

Verify:

```bash
python scripts/validate_skill.py
```

Suggested commit:

```bash
git add skills/github-loop-runner scripts/validate_skill.py
git commit -m "feat: add hypothesis-gated renewal"
```

## Milestone 5: Strengthen PR Evidence And Stopper Policy

Update the generated PR template in `repo-scaffold.md` so PRs record:

- loop trace updated
- feedback entries linked when applicable
- root-cause layer classified for blocking feedback
- acceptance criteria mapped to CI or review evidence
- active hypotheses updated when applicable
- harness repair considered when failures repeat

Update `stopper-policy.md` with stopper cases for:

- missing CI and missing trace evidence
- repeated harness defects with no safe repair
- invalidated active hypothesis with no rollback path
- inconsistent progress state that cannot be repaired safely

Update `runner-prompt.md` so the runner stops or runs review when evidence is missing.

Verify:

```bash
python scripts/validate_skill.py
```

Suggested commit:

```bash
git add skills/github-loop-runner scripts/validate_skill.py
git commit -m "feat: require loop evidence in PRs"
```

## Milestone 6: Update Public Docs

Update:

- `README.md`
- `llms.txt`
- `scripts/validate_skill.py`

README should mention:

- Loop Trace
- Harness Repair Loop
- hypothesis-gated renewal
- harness-layer root cause classification

`llms.txt` should mention:

- `agent-prompts/`
- loop trace
- feedback log
- hypothesis log
- harness repair protocol

Verify:

```bash
python scripts/validate_skill.py
```

Suggested commit:

```bash
git add README.md llms.txt scripts/validate_skill.py
git commit -m "docs: describe harness observability loop"
```

## Milestone 7: Remove Temporary Agent Prompts After The Upgrade Is Encoded

Run this milestone only after Milestones 1-6 are complete and the final runner behavior is fully encoded in:

- `skills/github-loop-runner/SKILL.md`
- `skills/github-loop-runner/references/repo-scaffold.md`
- `skills/github-loop-runner/references/runner-prompt.md`
- `skills/github-loop-runner/references/feedback-taxonomy.md`
- `skills/github-loop-runner/references/review-and-renewal-loop.md`
- `skills/github-loop-runner/references/stopper-policy.md`
- `skills/github-loop-runner/references/loop-review-template.md`

Purpose: remove scaffolding that was only needed to upgrade this skill repository.

Delete:

- `agent-prompts/README.md`
- `agent-prompts/harness-upgrade-plan.md`
- `agent-prompts/start-harness-upgrade.md`

Update:

- `README.md` to remove the temporary Agent Prompts section, unless the maintainers still want public development prompts.
- `llms.txt` to remove `agent-prompts/` references.
- `scripts/validate_skill.py` to remove checks that require `agent-prompts/`.

Verify:

```bash
python scripts/validate_skill.py
```

Suggested commit:

```bash
git add README.md llms.txt scripts/validate_skill.py
git rm -r agent-prompts
git commit -m "chore: remove temporary harness upgrade prompts"
```

## Final Verification

Run:

```bash
python scripts/validate_skill.py
git status --short
```

Open a PR with:

```text
Title: Add harness observability and repair loop protocol
```

The PR body should include:

- files added
- files changed
- validator result
- summary of loop trace, root-cause taxonomy, harness repair, and hypothesis-gated renewal
- any risks or follow-up work
