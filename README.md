# GitHub Loop Runner Skill

_A portable agent skill for bootstrapping and running GitHub-only autonomous development loops._

GitHub Loop Runner helps an agent turn a product idea or existing repository into a CI-verified milestone loop using the GitHub connector. It seeds runner docs, progress state, a plan, development principles, Feedback Taxonomy, feedback log, Loop Trace, Review and Renewal Loop, Harness Repair Loop, hypothesis-gated renewal, stopper policy, PR template, and validation workflow.

## What It Does

- Bootstraps autonomous repos with `AGENTS.md`, `docs/autonomous-runner.md`, `docs/progress.md`, `docs/next-steps-plan.md`, and harness docs.
- Runs milestone loops through one branch, one PR, CI, feedback classification, merge, progress update, and progress re-read.
- Uses Feedback Taxonomy to classify CI, review, mergeability, progress, trace, hypothesis, repair, review, and stopper observations.
- Adds Loop Trace so runner decisions have auditable event evidence.
- Adds Harness Repair Loop so repeated harness defects are repaired without mixing product feature work into the repair.
- Adds hypothesis-gated renewal so durable process changes require evidence before promotion.
- Adds harness-layer root cause classification across observation, context, planning, control loop, tool action, state store, verification, governance, product code, and unknown.
- Preserves GitHub-only operation, CI verification, and `docs/progress.md` as the state source.

## How It Works

```text
Idea or repo -> GitHub probe -> bootstrap/read runner docs -> select TODO -> PR + CI -> feedback + trace -> merge -> progress update -> review/repair/hypothesis/stopper loop
```

## Get Started

```bash
git clone https://github.com/alexwang91/github-loop-runner-skill.git
cd github-loop-runner-skill
python scripts/validate_skill.py
```

Invoke:

```text
Use $github-loop-runner to turn this product idea into a GitHub repo with autonomous runner docs, progress tracking, loop trace, feedback log, hypothesis log, harness repair protocol, and milestone PR loops.
```

## Workflow Sources

| Source | How this skill uses it |
| --- | --- |
| Matt Pocock skills | Alignment before building, shared language, ADRs, and vertical-slice issue shape. |
| Superpowers | Brainstorming, writing-plans, TDD/eval-first, review, and finishing-branch discipline. |
| Karpathy-style guidelines | Think before coding, simplicity first, surgical changes, and explicit success criteria. |

## Proof

| Check | Command |
| --- | --- |
| Skill structure, frontmatter, references, runner prompt, public docs, and Markdown fences | `python scripts/validate_skill.py` |

## Compatibility

| Surface | Status | Notes |
| --- | :---: | --- |
| Codex local skills | Ready | Install under `~/.codex/skills/github-loop-runner`. |
| GitHub connector workflows | Ready | Repository work happens through GitHub connector APIs. |
| CI-only verification | Ready | Runner delegates verification to GitHub checks. |
| Feedback Taxonomy | Ready | Runner classifies observations before selecting next actions. |
| Loop Trace | Ready | Runner records required decision events. |
| Harness Repair Loop | Ready | Runner repairs repeated harness defects without product-scope drift. |
| Hypothesis-Gated Renewal | Ready | Runner validates process changes before promotion. |
| Review and Renewal Loop | Ready | Runner reviews completed work and renews the plan before stopping. |

## When To Use / When To Skip

Use it when you need GitHub-only autonomous PR loops with CI verification, structured feedback, observability, repair, and plan renewal. Skip it for one-shot code changes, local-first verification workflows, or repositories without a working GitHub access path.

## Documentation

| Start here | Go deeper |
| --- | --- |
| [Skill workflow](skills/github-loop-runner/SKILL.md) | [Repo scaffold templates](skills/github-loop-runner/references/repo-scaffold.md) |
| [Runner prompt](skills/github-loop-runner/references/runner-prompt.md) | [Feedback taxonomy](skills/github-loop-runner/references/feedback-taxonomy.md) |
| [Loop Trace](skills/github-loop-runner/references/loop-trace.md) | [Harness Repair Loop](skills/github-loop-runner/references/harness-repair-loop.md) |
| [Review loop](skills/github-loop-runner/references/review-and-renewal-loop.md) | [Hypothesis log](skills/github-loop-runner/references/loop-hypotheses.md) |
| [Stopper policy](skills/github-loop-runner/references/stopper-policy.md) | [Loop review template](skills/github-loop-runner/references/loop-review-template.md) |
| [Validation](scripts/validate_skill.py) | [Agent index](llms.txt) |

## Compared To

| | Scope | GitHub-only | Progress loop | Feedback taxonomy | Plan renewal | Skill methodology |
| --- | --- | :---: | :---: | :---: | :---: | :---: |
| GitHub Loop Runner Skill | Repo bootstrap plus autonomous PR loop, trace, repair, and hypothesis gating | Yes | Yes | Yes | Yes | Explicit |
| Generic project prompt | One prompt | Sometimes | No | No | No | Usually implicit |
| CI workflow template | Verification only | Yes | No | Partial | No | No |
| Agent memory file | Instructions only | Maybe | Manual | Manual | Manual | Depends |

## Contributing

Run:

```bash
python scripts/validate_skill.py
```
