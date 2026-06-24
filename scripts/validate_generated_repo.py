from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "AGENTS.md",
    "docs/autonomous-runner.md",
    "docs/progress.md",
    "docs/next-steps-plan.md",
    "docs/development-principles.md",
    "docs/long-run-growth-loop.md",
    "docs/feedback-taxonomy.md",
    "docs/feedback-log.md",
    "docs/loop-trace.md",
    "docs/handoff-decision.md",
    "docs/review-and-renewal-loop.md",
    "docs/harness-repair-loop.md",
    "docs/loop-hypotheses.md",
    "docs/stopper-policy.md",
    "docs/loop-review.md",
    "docs/agent-judge-loop.md",
    "docs/growth-candidates.md",
    "docs/runner-memory.md",
    "docs/codebase-localization.md",
    "docs/workflow-graph.md",
    "docs/loop-acceptance-tests.md",
    ".github/pull_request_template.md",
    ".github/workflows/verify.yml",
]

VALID_STATUSES = {"TODO", "IN_PROGRESS", "DONE", "BLOCKED", "DEFERRED", "CANCELLED"}
REQUIRED_TRACE_EVENTS = [
    "selected_milestone",
    "branch_created",
    "pr_opened",
    "ci_observed",
    "feedback_classified",
    "merge_attempted",
    "progress_updated",
    "growth_review",
    "deep_review",
    "review_run",
    "harness_repair_run",
    "hypothesis_updated",
    "handoff_decision",
    "stop",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def read(root: Path, relative_path: str) -> str:
    path = root / relative_path
    require(path.is_file(), f"missing file: {relative_path}")
    return path.read_text(encoding="utf-8")


def parse_progress_rows(progress: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in progress.splitlines():
        if not line.startswith("|"):
            continue
        if "---" in line or "Milestone" in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        milestone, description, status = cells[:3]
        if re.match(r"^M[0-9]+$", milestone):
            rows.append({"milestone": milestone, "description": description, "status": status})
    return rows


def count_status(rows: list[dict[str, str]], status: str) -> int:
    return sum(1 for row in rows if row["status"] == status)


def require_phrases(label: str, text: str, phrases: list[str]) -> None:
    for phrase in phrases:
        require(phrase in text, f"{label} missing phrase: {phrase}")


def validate_generated_repo(root: Path) -> None:
    for relative_path in REQUIRED_FILES:
        require((root / relative_path).is_file(), f"missing required generated file: {relative_path}")

    agents = read(root, "AGENTS.md")
    progress = read(root, "docs/progress.md")
    long_run = read(root, "docs/long-run-growth-loop.md")
    handoff = read(root, "docs/handoff-decision.md")
    feedback_log = read(root, "docs/feedback-log.md")
    loop_trace = read(root, "docs/loop-trace.md")
    judge = read(root, "docs/agent-judge-loop.md")
    candidates = read(root, "docs/growth-candidates.md")
    memory = read(root, "docs/runner-memory.md")
    localization = read(root, "docs/codebase-localization.md")
    workflow_graph = read(root, "docs/workflow-graph.md")
    loop_acceptance = read(root, "docs/loop-acceptance-tests.md")
    pr_template = read(root, ".github/pull_request_template.md")
    workflow = read(root, ".github/workflows/verify.yml")

    require_phrases("AGENTS.md", agents, [
        "docs/progress.md",
        "docs/long-run-growth-loop.md",
        "docs/agent-judge-loop.md",
        "docs/growth-candidates.md",
        "docs/runner-memory.md",
        "docs/codebase-localization.md",
        "docs/workflow-graph.md",
        "docs/loop-acceptance-tests.md",
        "docs/handoff-decision.md",
    ])

    rows = parse_progress_rows(progress)
    require(rows, "docs/progress.md must contain at least one milestone row")
    invalid_statuses = sorted({row["status"] for row in rows if row["status"] not in VALID_STATUSES})
    require(not invalid_statuses, f"docs/progress.md contains invalid statuses: {invalid_statuses}")
    require(count_status(rows, "TODO") >= 1, "docs/progress.md should contain at least one TODO milestone")

    require_phrases("docs/long-run-growth-loop.md", long_run, [
        "target_merged_prs",
        "minimum_merged_prs_before_final_review",
        "review_interval_prs",
        "deep_review_interval_prs",
        "minimum_open_todo_backlog",
        "expansion_batch_min",
        "expansion_batch_max",
    ])

    require("status: pending" in handoff, "docs/handoff-decision.md should start with pending handoff state")
    require("chosen_mode: null" in handoff, "docs/handoff-decision.md should not preselect a mode")

    require("entries: []" in feedback_log or "entries:" in feedback_log, "docs/feedback-log.md should contain an entries collection")
    require("entries: []" in loop_trace or "entries:" in loop_trace, "docs/loop-trace.md should contain an entries collection")
    for event in REQUIRED_TRACE_EVENTS:
        require(event in loop_trace, f"docs/loop-trace.md missing required event or metric: {event}")

    require_phrases("docs/agent-judge-loop.md", judge, ["milestone_selection", "scope_control", "trace_completeness", "long_run_policy_compliance"])
    require_phrases("docs/growth-candidates.md", candidates, ["product_impact", "verification_strength", "dependency_safety"])
    require_phrases("docs/runner-memory.md", memory, ["compaction_interval_prs", "entries"])
    require_phrases("docs/codebase-localization.md", localization, ["candidate files", "selected files", "scope risk"])
    require_phrases("docs/workflow-graph.md", workflow_graph, ["project_loop", "milestone_loop", "repair_loop"])
    require_phrases("docs/loop-acceptance-tests.md", loop_acceptance, ["required_files", "judge_loop_present", "memory_present", "localization_present"])

    require_phrases("pull request template", pr_template, [
        "CI is green",
        "loop trace updated",
        "feedback entries linked",
        "long-run growth policy checked",
        "handoff decision respected",
    ])

    for relative_path in REQUIRED_FILES:
        if relative_path.startswith(".github/"):
            continue
        require(relative_path in workflow, f"verify workflow should check {relative_path}")

    print(f"Generated repo validation passed: {root}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a generated GitHub Loop Runner repository scaffold.")
    parser.add_argument("root", nargs="?", default=".", help="Path to generated repository root")
    args = parser.parse_args()
    validate_generated_repo(Path(args.root).resolve())


if __name__ == "__main__":
    main()
