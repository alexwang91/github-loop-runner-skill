# Handoff Decision Reference

Use this reference when bootstrap, review, repair, or stopper handling reaches a decision point where product development should not start automatically.

## Purpose

The skill's first responsibility is to create or prepare a GitHub repository, write the task plan into that repository, and produce an executable prompt for the agent that will do the development.

Bootstrap does not mean "start product development now." After bootstrap finishes, the runner must stop at a handoff decision and ask the user which execution mode they want.

## Decision Point

Run the Handoff Decision after:

- the bootstrap PR is opened or merged,
- the generated repository has runner docs, progress, plan, CI scaffold, and harness files,
- a review or stopper report says safe work can continue but human choice is needed,
- the user asks to hand work to another agent.

## User Choice

Ask the user to choose one of these modes:

1. **Current-agent development**: this same agent continues into the Loop Workflow and works on the first TODO milestone.
2. **External-agent development**: stop product development in this session and output a complete copy-paste prompt for another agent.

Default to external-agent handoff when the user's request was to create a repository and tasks for another agent.

## Required Output At Handoff

Report:

- target repository and base branch,
- bootstrap branch or PR URL when available,
- generated files,
- CI/check status when available,
- first TODO milestone from fresh progress,
- whether review, repair, or hypothesis validation is due,
- the question: "Do you want this agent to continue development, or should I hand this to another agent?"

If the user chooses external-agent development, output the complete prompt from `references/runner-prompt.md` with all placeholders filled.

## External Agent Prompt Requirements

The external-agent prompt must include:

- repository owner/name and base branch,
- GitHub-only operating rule,
- files to read first,
- progress selection rule,
- one milestone / one branch / one PR rule,
- CI-as-VERIFY rule,
- Feedback Taxonomy, Loop Trace, Harness Repair Loop, Hypothesis-Gated Renewal, and stopper rules,
- hard guardrails,
- exact first action: fetch runner files, report due review/repair/hypothesis state, then select the first TODO from fresh progress.

## Forbidden Behavior

Do not start product milestone implementation immediately after bootstrap unless the user explicitly chooses current-agent development.

Do not silently choose current-agent development merely because the connector can write code.

Do not output a vague prompt such as "continue the project." The external-agent prompt must be complete enough for another agent to start from a cold context.
