<div align="center">

<pre>
+------------------------------------------------------------+
| GITHUB LOOP ENGINE V1                                     |
| product idea -> GitHub repo -> handoff -> safe PR loop     |
+------------------------------------------------------------+
</pre>

# GitHub Loop Runner Skill

_A stable GitHub-only loop engine for bootstrapping autonomous development handoffs._

<p align="center">
  <a href="https://github.com/alexwang91/github-loop-runner-skill/actions/workflows/validate.yml"><img src="https://github.com/alexwang91/github-loop-runner-skill/actions/workflows/validate.yml/badge.svg" alt="Validate skill"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="llms.txt"><img src="https://img.shields.io/badge/llms.txt-ready-blue?logo=readme&logoColor=white" alt="llms.txt ready"></a>
</p>

</div>

GitHub Loop Runner is frozen as **GitHub Loop Engine v1**. Its job is intentionally narrow: turn a product idea or existing repository into a GitHub-only autonomous development handoff, then run one safe milestone PR loop at a time.

It is not an agent OS, runtime DSL, CI interpreter, or general multi-agent orchestration platform. Those directions are explicit non-goals for v1.

## Stable v1 Core

| Core responsibility | Mechanism |
| --- | --- |
| Prepare the repository | Bootstrap runner docs, progress, plan, PR template, and CI scaffold. |
| Stop before product work | Handoff Decision. |
| Track milestone state | `docs/progress.md` as the state source. |
| Prevent unsafe GitHub writes | GitHub Operation Ledger. |
| Execute work | One milestone, one branch, one PR. |
| Verify work | CI as VERIFY. |
| Keep evidence | Feedback Log and Loop Trace. |
| Continue useful long runs | Long-Run Growth Mode. |
| Repair runner defects | Harness Repair Loop. |
| Stop safely | Stopper Policy. |

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

Invoke it with a product idea:

```text
Use $github-loop-runner to turn this product idea into a GitHub repo with runner docs, progress tracking, handoff decision, operation ledger, long-run growth policy, feedback log, loop trace, harness repair protocol, and milestone PR loops:

<PRODUCT_IDEA>
```

If the GitHub connector can create repositories, the runner can use that path. If repository creation is unavailable, it asks for an initialized empty `owner/name` repository or a repository where the GitHub App is installed.

## How It Works

```text
Product idea or existing repo
        |
        v
Probe GitHub connector and repo access
        |
        v
Bootstrap runner docs, progress, plan, CI, and protocol files
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
Selected agent reads repo docs
        |
        v
Read progress + declare operation state
        |
        v
One branch -> one PR -> CI -> feedback + trace -> merge or block
        |
        v
Re-read progress and continue only when safe
```

## Stable Loop Contract

```text
read progress
  -> select first TODO
  -> declare GitHub operation state
  -> create one branch once
  -> fetch target files
  -> update/create target files
  -> create one PR once
  -> observe CI
  -> merge or block
  -> update feedback, trace, and progress
  -> re-read state
```

## Documentation

| Document | Purpose |
| --- | --- |
| [Stable v1 freeze](docs/stable-v1.md) | Scope, non-goals, and change admission rules. |
| [Architecture](docs/architecture.md) | v1 system layers and data flow. |
| [Skill workflow](skills/github-loop-runner/SKILL.md) | Main execution protocol. |
| [Repo scaffold](skills/github-loop-runner/references/repo-scaffold.md) | Generated repo templates. |
| [Runner prompt](skills/github-loop-runner/references/runner-prompt.md) | External agent prompt reference. |
| [GitHub Operation Ledger](skills/github-loop-runner/references/github-operation-ledger.md) | Write-operation state and branch/ref safety. |
| [Long-Run Growth Loop](skills/github-loop-runner/references/long-run-growth-loop.md) | Backlog floor and review cadence. |
| [Feedback taxonomy](skills/github-loop-runner/references/feedback-taxonomy.md) | Feedback classification. |
| [Loop Trace](skills/github-loop-runner/references/loop-trace.md) | Evidence log protocol. |
| [Harness Repair Loop](skills/github-loop-runner/references/harness-repair-loop.md) | Repair protocol for runner defects. |
| [Stopper policy](skills/github-loop-runner/references/stopper-policy.md) | Safe stopping conditions. |

## Proof

This repository ships a minimal v1 validator and GitHub Actions workflow.

| Check | What it proves | Command |
| --- | --- | --- |
| Skill structure | Manifest, skill file, README, llms index, and references exist. | `python scripts/validate_skill.py` |
| Generated repo example | Example generated repo has required v1 state files. | `python scripts/validate_generated_repo.py` |
| Stable v1 scope | Manifest declares v1 frozen scope and non-goals. | `python scripts/validate_evaluation_stack.py` |

## Compatibility

| Surface | Status | Notes |
| --- | :---: | --- |
| Codex local skills | Ready | Install under `~/.codex/skills/github-loop-runner`. |
| GitHub connector workflows | Ready | Repository work is performed through GitHub connector APIs. |
| CI-only verification | Ready | Generated runners delegate verification to GitHub checks. |
| Agent handoff | Ready | Bootstrap can stop and output a full prompt for another agent. |
| Long-run growth | Ready | Generated runners periodically review and renew backlog. |
| Runtime DSL / agent OS | Not a goal | Explicitly out of scope for v1. |
| Local-first execution | Not the default | CI remains the verification channel for GitHub-only loops. |

## When To Use / When To Skip

Use it if you want a stable GitHub PR loop that another agent can safely continue.

Skip it if you need a general runtime framework, local-first execution, or unconstrained multi-agent orchestration.

## Contributing

Before opening a PR:

```bash
python scripts/validate_skill.py
python scripts/validate_generated_repo.py
python scripts/validate_evaluation_stack.py
```

Future changes must preserve [Stable v1 freeze](docs/stable-v1.md).

## License

MIT - see [LICENSE](LICENSE).
