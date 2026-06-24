# Start Harness Upgrade Prompt

Copy this prompt into a new agent session.

````markdown
Use `superpowers:using-superpowers` first. Then work in the repository `alexwang91/github-loop-runner-skill`.

Your job is to upgrade the repository by following `agent-prompts/harness-upgrade-plan.md`.

Before editing anything, read:

- `README.md`
- `llms.txt`
- `scripts/validate_skill.py`
- `skills/github-loop-runner/SKILL.md`
- every Markdown file under `skills/github-loop-runner/references/`

Then run:

```bash
python scripts/validate_skill.py
```

Expected result:

```text
Skill validation passed
```

Implementation rules:

- Follow `agent-prompts/harness-upgrade-plan.md` milestone by milestone.
- Make one small commit per milestone.
- Do not redesign the skill from scratch.
- Preserve the GitHub-only operating model.
- Preserve CI as the verification channel.
- Preserve `docs/progress.md` as the milestone state source.
- Do not add local clone, local package-manager, or local test requirements to generated runner protocols.
- Do not weaken tests, evals, assertions, acceptance criteria, or guardrails.
- Do not create vague cleanup or polish work.
- If a change affects runner behavior, update the validator phrase checks.
- After every milestone, run `python scripts/validate_skill.py` and fix failures before continuing.

Target changes:

1. Add loop trace protocol.
2. Add harness-layer root cause classification.
3. Add Harness Repair Loop.
4. Add hypothesis-gated renewal.
5. Strengthen PR evidence and stopper policy.
6. Update README, `llms.txt`, and validator coverage.

Final response should include:

- branch name
- commit list
- validator result
- changed files summary
- open risks
````
