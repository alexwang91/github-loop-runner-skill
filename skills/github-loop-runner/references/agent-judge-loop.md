# Agent Judge Loop Reference

Use this reference when a generated repository needs process-level evaluation in addition to CI.

## Purpose

CI verifies code and checks. The Agent Judge Loop evaluates whether the runner followed the operating protocol.

The judge does not replace CI. It checks loop hygiene, evidence quality, scope control, progress consistency, handoff compliance, long-run policy compliance, feedback classification, and trace completeness.

## Generated Repo File

Generate `docs/agent-judge-loop.md`.

## When To Run

Run the judge:

- before merge,
- after CI changes state,
- after a growth review or deep review,
- after a harness repair,
- before marking a milestone DONE,
- before final review eligibility.

## Judge Dimensions

| Dimension | Question |
| --- | --- |
| `milestone_selection` | Was the first eligible TODO selected from fresh progress? |
| `scope_control` | Did the PR stay inside the selected milestone? |
| `evidence_quality` | Are acceptance criteria mapped to CI or review evidence? |
| `ci_usage` | Was CI treated as VERIFY? |
| `feedback_classification` | Were meaningful observations classified? |
| `trace_completeness` | Were required trace events recorded? |
| `progress_consistency` | Does progress reflect merged work? |
| `handoff_compliance` | Was product work gated by the handoff decision? |
| `long_run_policy_compliance` | Were backlog and review cadence checked? |
| `harness_safety` | Did repair work avoid product scope and preserve guardrails? |

## Judge Report Format

```yaml
judge_report:
  id: J-0001
  milestone: M0
  pr: 1
  verdict: pass
  scores:
    milestone_selection: 5
    scope_control: 5
    evidence_quality: 5
    ci_usage: 5
    feedback_classification: 5
    trace_completeness: 5
    progress_consistency: 5
    handoff_compliance: 5
    long_run_policy_compliance: 5
    harness_safety: 5
  findings: []
  required_actions: []
```

## Verdicts

- `pass`: merge or continue is allowed if CI and other gates pass.
- `needs_repair`: run Harness Repair Loop before continuing.
- `needs_review`: run Review and Renewal Loop before continuing.
- `block_merge`: do not merge until required actions are complete.

## Rules

1. A judge verdict of `block_merge` blocks merge.
2. A missing judge report before merge is a trace or evidence gap.
3. Judge findings must become feedback entries when meaningful.
4. Repeated low scores should trigger Harness Repair Loop or Review and Renewal Loop.
