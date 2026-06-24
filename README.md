<div align="center">

<pre>
+------------------------------------------------------------+
| GITHUB LOOP RUNNER SKILL                                   |
| product idea -> GitHub repo -> agent handoff -> PR loop     |
+------------------------------------------------------------+
</pre>

# GitHub Loop Runner Skill

_A portable agent skill for bootstrapping GitHub-only autonomous development handoffs._

<p align="center">
  <a href="https://github.com/alexwang91/github-loop-runner-skill/actions/workflows/validate.yml"><img src="https://github.com/alexwang91/github-loop-runner-skill/actions/workflows/validate.yml/badge.svg" alt="Validate skill"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="llms.txt"><img src="https://img.shields.io/badge/llms.txt-ready-blue?logo=readme&logoColor=white" alt="llms.txt ready"></a>
</p>

<p align="center">
  <a href="#get-started">Get Started</a> |
  <a href="#what-it-does">What It Does</a> |
  <a href="#how-it-works">How It Works</a> |
  <a href="#documentation">Docs</a> |
  <a href="llms.txt">llms.txt</a>
</p>

</div>

GitHub Loop Runner turns a product idea into a GitHub repository that teaches future agents how to keep working: plan the product, track progress, open milestone PRs, use CI as verification, classify feedback, repair the harness when the loop itself fails, and stop when safe progress is no longer possible.

The important behavior: bootstrap prepares the repository and then stops at a **Handoff Decision**. The user chooses whether the current agent continues development or whether another agent receives a complete copy-paste runner prompt.

It is designed for Codex, Claude Code, Hermes, OpenClaw, Goose, Cursor, Aider, Gemini CLI, and other instruction-aware agents that can read Markdown skills and operate through a GitHub connector.

## Get Started

Clone and validate the skill:

```bash
git clone https://github.com/alexwang91/github-loop-runner-skill.git
cd github-loop-runner-skill
python scripts/validate_skill.py
```

Install for Codex local skills:

```bash
mkdir -p ~/.codex/skills
cp -R skills/github-loop-runner ~/.codex/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\github-loop-runner" "$env:USERPROFILE\.codex\skills\github-loop-runner"
```

Invoke it with a product idea:

```text
Use $github-loop-runner to turn this product idea into a GitHub repo with autonomous runner docs, progress tracking, handoff decision, loop trace, feedback log, hypothesis log, harness repair protocol, and milestone PR loops:

<PRODUCT_IDEA>
```

If the GitHub connector can create repositories, the runner can use that path. If repository creation is unavailable, it asks for an initialized empty `owner/name` repository or a repository where the GitHub App is installed.

## What It Does

- **Bootstraps autonomous repos** - seeds `AGENTS.md`, `docs/autonomous-runner.md`, `docs/progress.md`, `docs/next-steps-plan.md`, development principles, CI, PR templates, and runner protocol files.
- **Stops for handoff** - after bootstrap, asks whether the current agent should continue development or whether another agent should receive the complete runner prompt.
- **Produces external-agent prompts** - fills a cold-start prompt with repository, base branch, bootstrap PR, first TODO milestone, required files, CI rules, feedback, trace, repair, hypothesis, and stopper rules.
- **Runs milestone PR loops only after selection** - selects the first TODO from `docs/progress.md`, creates one branch, opens one PR, waits for CI, merges only when safe, updates progress, then re-reads state.
- **Uses Feedback Taxonomy** - classifies CI, review, mergeability, scope, progress, trace, hypothesis, repair, review, handoff, and stopper observations into allowed and forbidden next actions.
- **Adds Loop Trace** - records auditable evidence for milestone selection, context reads, PRs, CI attempts, feedback IDs, merge attempts, handoff decisions, review decisions, and stopper outcomes.
- **Adds Harness Repair Loop** - repairs repeated runner, scaffold, CI, state, tool, verification, or governance failures without mixing product feature work into the repair.
- **Uses hypothesis-gated renewal** - turns durable process changes into measurable hypotheses with success criteria, measurement windows, and rollback rules.
- **Adds harness-layer root cause classification** - separates product-code failures from observation, context, planning, control-loop, tool-action, state-store, verification, governance, and unknown failures.
- **Preserves hard guardrails** - GitHub-only operation, CI verification, `docs/progress.md` as state source, no dummy files, and no weakening tests or acceptance criteria to get green.

## How It Works

```text
Product idea or existing repo
        |
        v
Probe GitHub connector and repo access
        |
        v
Bootstrap runner docs, plan, progress, CI, and harness protocol
        |
        v
Open bootstrap PR and report CI/check status
        |
        v
Handoff Decision
        |
        +--> Current agent continues into Loop Workflow
        |
        +--> External agent receives complete copy-paste runner prompt
        |
        v
Selected agent reads repo docs and selects first TODO milestone
        |
        v
One branch -> one PR -> CI -> feedback + trace -> merge
        |
        v
Update progress, review, repair harness, validate hypotheses, or stop
```

The important split is simple:

| File | Role |
| --- | --- |
| `docs/progress.md` | Milestone state source. |
| `docs/next-steps-plan.md` | Product plan and acceptance criteria. |
| `docs/handoff-decision.md` | Records whether development continues here or is handed to another agent. |
| `docs/feedback-log.md` | Structured observations and decisions. |
| `docs/loop-trace.md` | Event evidence for what the runner did. |
| `docs/loop-hypotheses.md` | Measurable process changes and rollback rules. |
| `docs/harness-repair-loop.md` | Repair protocol for repeated harness defects. |

## Proof

This repository ships a validator and GitHub Actions workflow.

| Check | What it proves | Command |
| --- | --- | --- |
| Skill structure | Required skill, reference, prompt, metadata, and docs files exist. | `python scripts/validate_skill.py` |
| Prompt integrity | Runner prompt contains GitHub-only, CI, handoff, feedback, trace, repair, hypothesis, and stopper rules. | `python scripts/validate_skill.py` |
| Markdown hygiene | README, skill files, and reference files have balanced code fences. | `python scripts/validate_skill.py` |

## Compatibility

| Surface | Status | Notes |
| --- | :---: | --- |
| Codex local skills | Ready | Install under `~/.codex/skills/github-loop-runner`. |
| GitHub connector workflows | Ready | Repository work is performed through GitHub connector APIs. |
| CI-only verification | Ready | Generated runners delegate verification to GitHub checks. |
| Agent handoff | Ready | Bootstrap can stop and output a full prompt for another agent. |
| Claude Code / Hermes / OpenClaw / Goose / Cursor / Aider / Gemini CLI | Portable | Import the Markdown skill and reference files as project instructions, rules, or memory. |
| Local-first test execution | Not the default | This skill intentionally treats CI as the verification channel for GitHub-only loops. |

## Workflow Sources

| Source | How this skill uses it |
| --- | --- |
| Matt Pocock skills | Alignment before building, shared project language, ADR-worthy decisions, and vertical-slice milestone shape. |
| Superpowers | Brainstorming, writing-plans, TDD/eval-first, review, and finishing-branch discipline. |
| Karpathy-style guidelines | Think before coding, keep it simple, make surgical changes, and drive toward explicit success criteria. |

## When To Use / When To Skip

**Great fit if you...**

- want to turn a product idea into a GitHub repo that future agents can continue autonomously,
- want bootstrap to stop and ask whether to continue here or hand off to another agent,
- need a complete cold-start prompt for a separate development agent,
- need GitHub-only execution with CI as verification,
- want progress, feedback, trace, repair, hypotheses, and stopper rules written into the repo itself,
- want one milestone per PR with clear acceptance criteria and reviewable state.

**Skip it if you...**

- only need a one-shot code change,
- require local test execution as the primary verification path,
- do not have a GitHub connector, GitHub App, or repository access path,
- want an agent to bypass CI, weaken checks, or keep inventing work after the product goal is satisfied.

## Documentation

| Start here | Go deeper |
| --- | --- |
| [Skill workflow](skills/github-loop-runner/SKILL.md) | [Repo scaffold templates](skills/github-loop-runner/references/repo-scaffold.md) |
| [Runner prompt](skills/github-loop-runner/references/runner-prompt.md) | [Handoff decision](skills/github-loop-runner/references/handoff-decision.md) |
| [Feedback taxonomy](skills/github-loop-runner/references/feedback-taxonomy.md) | [Loop Trace](skills/github-loop-runner/references/loop-trace.md) |
| [Harness Repair Loop](skills/github-loop-runner/references/harness-repair-loop.md) | [Review and Renewal Loop](skills/github-loop-runner/references/review-and-renewal-loop.md) |
| [Loop hypotheses](skills/github-loop-runner/references/loop-hypotheses.md) | [Stopper policy](skills/github-loop-runner/references/stopper-policy.md) |
| [Loop review template](skills/github-loop-runner/references/loop-review-template.md) | [Validation](scripts/validate_skill.py) |
| [Agent index](llms.txt) |  |

## Compared To

| | Scope | GitHub-only | Agent handoff | Progress loop | Feedback taxonomy | Trace / repair | Plan renewal |
| --- | --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **GitHub Loop Runner Skill** | Repo bootstrap, handoff prompt, and autonomous PR loop | Yes | Yes | Yes | Yes | Yes | Yes |
| Generic project prompt | One prompt | Sometimes | Manual | No | No | No | No |
| CI workflow template | Verification only | Yes | No | No | Partial | No | No |
| Agent memory file | Instructions only | Maybe | Manual | Manual | Manual | Manual | Manual |

## Contributing

Before opening a PR:

```bash
python scripts/validate_skill.py
```

## License

MIT - see [LICENSE](LICENSE).
