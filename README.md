<div align="center">

<pre>
+------------------------------------------------------------+
| GITHUB LOOP RUNNER SKILL                                   |
| repo bootstrap | runner docs | CI loops | milestone PRs     |
+------------------------------------------------------------+
</pre>

# GitHub Loop Runner Skill

_A portable agent skill for bootstrapping and running GitHub-only autonomous development loops._

<p align="center">
  <a href="skills/github-loop-runner/SKILL.md"><img src="https://img.shields.io/badge/agent_skill-portable-111827?logo=openai&logoColor=white" alt="Portable agent skill"></a>
  <a href="https://github.com/alexwang91/github-loop-runner-skill/actions/workflows/validate.yml"><img src="https://github.com/alexwang91/github-loop-runner-skill/actions/workflows/validate.yml/badge.svg" alt="Validate skill"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/alexwang91/github-loop-runner-skill?logo=opensourceinitiative&logoColor=white" alt="License"></a>
  <a href="llms.txt"><img src="https://img.shields.io/badge/llms.txt-ready-blue?logo=readme&logoColor=white" alt="llms.txt ready"></a>
</p>

<p align="center">
  <a href="#get-started">Install</a> |
  <a href="#what-it-does">What it does</a> |
  <a href="#how-it-works">How it works</a> |
  <a href="#proof">Proof</a> |
  <a href="#documentation">Docs</a>
</p>

<p align="center"><sub>
  <b>AI agents / LLMs:</b> read <a href="llms.txt"><code>/llms.txt</code></a> for a compact index.
</sub></p>

</div>

GitHub Loop Runner helps an agent turn a rough product idea into a GitHub repository that can keep working through milestone PRs using only the GitHub connector and CI. It seeds runner docs, a progress file, a detailed plan, development principles, a feedback taxonomy, a review-and-renewal loop, a stopper policy, a PR template, and a validation workflow.

## What It Does

- **Bootstraps autonomous repos** - creates the files a GitHub-only runner needs: `AGENTS.md`, `docs/autonomous-runner.md`, `docs/progress.md`, `docs/next-steps-plan.md`, `docs/development-principles.md`, `docs/feedback-taxonomy.md`, `docs/feedback-log.md`, `docs/review-and-renewal-loop.md`, `docs/stopper-policy.md`, and `docs/loop-review.md`.
- **Runs milestone loops** - reads `docs/progress.md`, selects the first TODO, opens one PR, waits for CI, classifies feedback, merges, updates progress, then re-reads progress.
- **Structures feedback** - classifies CI results, PR review, merge blockers, scope drift, regressions, and stopper decisions into typed feedback with allowed and forbidden next actions.
- **Renews plans periodically** - runs a Review and Renewal Loop after configured intervals, when no TODO remains, or when work gets blocked, then adds only specific and verifiable new milestones.
- **Uses CI as verification** - designed for environments with no local clone, no package manager, and no local test runner.
- **Makes workflow sources explicit** - maps Matt Pocock skills, Superpowers, and Karpathy-style guidelines into repo docs and optional runtime invocations.
- **Avoids fake capabilities** - probes GitHub connector access quietly and asks only when repo access, app installation, or an initialized empty repo is missing.
- **Protects guardrails** - forbids dummy/noop files and weakening tests, evals, assertions, or acceptance criteria to get green.

## How It Works

```text
Product idea or existing repo
        |
        v
Probe GitHub connector capability
        |
        v
Bootstrap docs or read existing runner docs
        |
        v
Apply workflow discipline:
Matt alignment + Superpowers plan/TDD/review + Karpathy guardrails
        |
        v
One milestone -> one branch -> one PR -> CI feedback -> merge
        |
        v
Classify feedback and update feedback log
        |
        v
Update progress, then re-read progress
        |
        v
Run Review and Renewal Loop when due
        |
        v
Summarize feedback trends
        |
        v
Renew the plan or stop through the stopper policy
```

The skill has six layers:

- `SKILL.md` gives the agent the bootstrap, loop, review, feedback, and prompt procedure.
- `references/repo-scaffold.md` provides the generated repository file templates.
- `references/feedback-taxonomy.md` defines structured feedback types, severity, evidence, and next actions.
- `references/review-and-renewal-loop.md` defines the periodic plan review loop.
- `references/stopper-policy.md` defines when the loop should stop.
- `references/runner-prompt.md` provides the final copy-paste prompt for an autonomous GitHub-only runner.

## Get Started

Clone the repo:

```bash
git clone https://github.com/alexwang91/github-loop-runner-skill.git
cd github-loop-runner-skill
```

### Codex Native Install

Install into Codex on macOS or Linux:

```bash
mkdir -p ~/.codex/skills
cp -R skills/github-loop-runner ~/.codex/skills/
```

Install into Codex on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skills\github-loop-runner" "$env:USERPROFILE\.codex\skills\github-loop-runner"
```

Invoke:

```text
Use $github-loop-runner to turn this product idea into a GitHub repo with autonomous runner docs, progress tracking, structured feedback, review renewal, stopper policy, and milestone PR loops.
```

### Portable Import For Other Agents

For Claude Code, Hermes, OpenClaw, Goose, Cursor, Aider, Gemini CLI, and similar tools, import the same Markdown files as persistent project instructions:

```text
Use the GitHub Loop Runner skill at skills/github-loop-runner/SKILL.md.
If bootstrapping a repo, also load skills/github-loop-runner/references/repo-scaffold.md.
If enabling structured feedback, also load skills/github-loop-runner/references/feedback-taxonomy.md.
If enabling plan renewal, also load skills/github-loop-runner/references/review-and-renewal-loop.md and skills/github-loop-runner/references/stopper-policy.md.
If producing the final runner prompt, also load skills/github-loop-runner/references/runner-prompt.md.
```

## Workflow Sources

| Source | How this skill uses it |
|--------|------------------------|
| Matt Pocock skills | Alignment before building, shared language, ADRs, and vertical-slice issue shape. |
| Superpowers | Brainstorming, writing-plans, TDD/eval-first, review, and finishing-branch discipline. |
| Karpathy-style guidelines | Think before coding, simplicity first, surgical changes, and explicit success criteria. |

If those skills are installed in the runner, the prompt can invoke them by name. If not, the generated repo docs include fallback discipline so the loop still works.

## Proof

This repo includes a local validator and GitHub Actions workflow.

| Check | What It Verifies | Command |
|-------|------------------|---------|
| Skill structure | `SKILL.md`, `agents/openai.yaml`, and references exist | `python scripts/validate_skill.py` |
| Frontmatter | Skill name and trigger description are present | `python scripts/validate_skill.py` |
| Workflow maps | Matt Pocock, Superpowers, Karpathy, and optional invocations are present | `python scripts/validate_skill.py` |
| Runner prompt | GitHub-only, CI verification, progress loop, feedback taxonomy, review renewal, stopper policy, and guardrails are present | `python scripts/validate_skill.py` |
| Markdown fences | Code fences in Markdown files are balanced | `python scripts/validate_skill.py` |

## Compatibility

| Surface | Status | Notes |
|---------|:------:|-------|
| Codex local skills | Ready | Install under `~/.codex/skills/github-loop-runner` |
| GitHub connector workflows | Ready | Skill assumes repository operations happen through GitHub connector APIs |
| CI-only verification | Ready | Runner delegates verification to GitHub checks |
| Feedback Taxonomy | Ready | Runner classifies observations before selecting next actions |
| Review and Renewal Loop | Ready | Runner can review completed work and renew the plan before stopping |
| Claude Code, Hermes, OpenClaw, Goose, Cursor, Aider | Portable | Import as skills, rules, memory, or project context |
| Other agent skill systems | Portable | Adapt install path and invocation syntax |

## When To Use / When To Skip

**Great fit if you...**

- want a new repo that teaches agents how to keep working after the first PR
- need GitHub-only execution with no local clone or package-manager access
- want `docs/progress.md` to be the milestone state source for autonomous loops
- want CI, review, merge, and stopper outcomes to become structured feedback
- want the loop to review completed work and add only specific, verifiable new work before stopping
- want Matt/Superpowers/Karpathy discipline encoded directly into repo docs

**Skip it if you...**

- only need a one-shot code change
- require local test execution as the primary verification path
- do not have GitHub connector, GitHub App, or `gh` access to the target repository

## Documentation

| Start here | Go deeper |
|------------|-----------|
| [Skill workflow](skills/github-loop-runner/SKILL.md) | [Repo scaffold templates](skills/github-loop-runner/references/repo-scaffold.md) |
| [Runner prompt](skills/github-loop-runner/references/runner-prompt.md) | [Feedback taxonomy](skills/github-loop-runner/references/feedback-taxonomy.md) |
| [Review loop](skills/github-loop-runner/references/review-and-renewal-loop.md) | [Stopper policy](skills/github-loop-runner/references/stopper-policy.md) |
| [Loop review template](skills/github-loop-runner/references/loop-review-template.md) | [CI workflow](.github/workflows/validate.yml) |
| [Validation](scripts/validate_skill.py) | [Agent index](llms.txt) |

## Compared To

| | Scope | GitHub-only | Progress loop | Feedback taxonomy | Plan renewal | Skill methodology |
|-|-------|:-----------:|:-------------:|:-----------------:|:------------:|:----------------:|
| **GitHub Loop Runner Skill** | Repo bootstrap plus autonomous PR loop | Yes | Yes | Yes | Yes | Explicit |
| Generic project prompt | One prompt | Sometimes | No | No | No | Usually implicit |
| CI workflow template | Verification only | Yes | No | Partial | No | No |
| Agent memory file | Instructions only | Maybe | Manual | Manual | Manual | Depends |

## Contributing

Run the validator before opening a pull request:

```bash
python scripts/validate_skill.py
```

## License

MIT - see [LICENSE](LICENSE).
