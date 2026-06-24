from pathlib import Path
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
README_FILE = REPO_ROOT / "README.md"
LLMS_FILE = REPO_ROOT / "llms.txt"

SKILL_DIR = REPO_ROOT / "skills" / "github-loop-runner"
SKILL_FILE = SKILL_DIR / "SKILL.md"
REFERENCES_DIR = SKILL_DIR / "references"
SCAFFOLD_FILE = REFERENCES_DIR / "repo-scaffold.md"
PROMPT_FILE = REFERENCES_DIR / "runner-prompt.md"
HANDOFF_FILE = REFERENCES_DIR / "handoff-decision.md"
FEEDBACK_FILE = REFERENCES_DIR / "feedback-taxonomy.md"
REVIEW_FILE = REFERENCES_DIR / "review-and-renewal-loop.md"
STOPPER_FILE = REFERENCES_DIR / "stopper-policy.md"
LOOP_REVIEW_FILE = REFERENCES_DIR / "loop-review-template.md"
LOOP_TRACE_FILE = REFERENCES_DIR / "loop-trace.md"
HARNESS_REPAIR_FILE = REFERENCES_DIR / "harness-repair-loop.md"
LOOP_HYPOTHESES_FILE = REFERENCES_DIR / "loop-hypotheses.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def read(path: Path) -> str:
    require(path.is_file(), f"Missing required file: {path.relative_to(REPO_ROOT)}")
    return path.read_text(encoding="utf-8")


def frontmatter(markdown: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", markdown, re.DOTALL)
    require(match is not None, "SKILL.md must start with YAML frontmatter")
    return match.group(1)


def assert_balanced_fences(path: Path, text: str) -> None:
    inside = False
    fence_len = 0
    start_line = 0

    for line_number, line in enumerate(text.splitlines(), start=1):
        opener = re.match(r"^(`{3,}|~{3,})", line)
        if not inside and opener:
            inside = True
            fence_len = len(opener.group(1))
            start_line = line_number
            continue

        if inside:
            closer = re.match(r"^(`{3,}|~{3,})\s*$", line)
            if closer and len(closer.group(1)) >= fence_len:
                inside = False
                fence_len = 0
                start_line = 0

    require(not inside, f"Unclosed Markdown fence in {path.relative_to(REPO_ROOT)} starting on line {start_line}")


def require_phrases(label: str, text: str, phrases: list[str]) -> None:
    for phrase in phrases:
        require(phrase in text, f"{label} missing phrase: {phrase}")


def main() -> None:
    readme = read(README_FILE)
    llms = read(LLMS_FILE)
    skill = read(SKILL_FILE)
    scaffold = read(SCAFFOLD_FILE)
    prompt = read(PROMPT_FILE)
    handoff = read(HANDOFF_FILE)
    feedback = read(FEEDBACK_FILE)
    review = read(REVIEW_FILE)
    stopper = read(STOPPER_FILE)
    loop_review = read(LOOP_REVIEW_FILE)
    loop_trace = read(LOOP_TRACE_FILE)
    harness_repair = read(HARNESS_REPAIR_FILE)
    loop_hypotheses = read(LOOP_HYPOTHESES_FILE)
    openai_yaml = read(OPENAI_YAML)

    fm = frontmatter(skill)
    require("name: github-loop-runner" in fm, "Skill frontmatter must name github-loop-runner")
    require("GitHub-only" in fm and "autonomous" in fm, "Skill description must cover GitHub-only autonomous triggers")
    for reference_name in [
        "repo-scaffold.md",
        "runner-prompt.md",
        "handoff-decision.md",
        "feedback-taxonomy.md",
        "review-and-renewal-loop.md",
        "stopper-policy.md",
        "loop-review-template.md",
        "loop-trace.md",
        "harness-repair-loop.md",
        "loop-hypotheses.md",
    ]:
        require(f"references/{reference_name}" in skill, f"SKILL.md must reference {reference_name}")
    require("$github-loop-runner" in openai_yaml, "openai.yaml default prompt must invoke the skill")
    require("value: \"github\"" in openai_yaml, "openai.yaml must declare GitHub dependency")

    require_phrases("SKILL.md", skill, [
        "Capability Probe",
        "Source Workflow Map",
        "Optional Skill Invocation Map",
        "Handoff Decision",
        "Feedback Taxonomy",
        "Loop Trace",
        "Harness Repair Loop",
        "Hypothesis-Gated Renewal",
        "harness-layer root cause classification",
        "Review and Renewal Loop",
        "Stop Conditions",
        "$grill-with-docs",
        "$to-issues",
        "$brainstorming",
        "$writing-plans",
        "$test-driven-development",
        "$requesting-code-review",
        "$finishing-a-development-branch",
    ])

    require_phrases("Scaffold", scaffold, [
        "Required Files",
        "Seed Generation Rules",
        "Handoff Decision",
        "Workflow Discipline",
        "`docs/autonomous-runner.md` Template",
        "`docs/progress.md` Template",
        "Methodology Map",
        "Optional Skill Invocation Map",
        "Skill Pack Map",
        "Optional Runtime Invocations",
        "`docs/development-principles.md` Template",
        "`docs/loop-trace.md` Template",
        "`docs/loop-hypotheses.md` Template",
        "`.github/workflows/verify.yml` Template",
        "loop trace updated",
        "root-cause layer classified",
        "active hypotheses updated",
        "handoff decision respected",
    ])

    require_phrases("Runner prompt", prompt, [
        "GitHub-only development runner",
        "Quietly probe GitHub connector capability",
        "docs/progress.md",
        "Handoff Decision Prompt",
        "Feedback Taxonomy",
        "Loop Trace",
        "Harness Repair Loop",
        "Hypothesis-Gated Renewal",
        "stopper policy",
        "Matt Pocock",
        "Superpowers",
        "Karpathy",
        "Use CI as VERIFY",
        "Do not weaken tests",
    ])

    require_phrases("Handoff reference", handoff, [
        "Handoff Decision Reference",
        "Purpose",
        "Decision Point",
        "User Choice",
        "Required Output At Handoff",
        "External Agent Prompt Requirements",
        "Forbidden Behavior",
    ])

    require_phrases("Feedback reference", feedback, [
        "Feedback Taxonomy Reference",
        "Feedback Sources",
        "Feedback Types",
        "Severity Levels",
        "Root-Cause Layers",
        "harness-layer root cause classification",
        "trace_gap",
        "harness_defect",
        "hypothesis_invalidated",
        "repair_validated",
        "Feedback Entry Format",
        "Allowed Action Map",
        "Runner Rules",
    ])

    require_phrases("Review reference", review, [
        "Review and Renewal Loop Reference",
        "Trigger Conditions",
        "Feedback Trends Since Last Review",
        "Hypothesis-Gated Renewal",
        "Review Steps",
        "Allowed Plan Updates",
        "Forbidden Plan Updates",
        "Harness Repair Loop",
    ])

    require_phrases("Stopper reference", stopper, [
        "Stopper Policy Reference",
        "Hard Stoppers",
        "Soft Stoppers",
        "Default Limits",
        "Stopper Report",
        "missing trace evidence",
        "repeated harness defects",
        "invalidated active hypothesis",
        "inconsistent progress state",
    ])

    require_phrases("Loop review template", loop_review, [
        "Feedback Trends Since Last Review",
        "Trace Coverage",
        "Harness Repair Assessment",
        "Hypothesis Assessment",
        "Feedback Decision",
        "Stopper Assessment",
        "Decision",
    ])

    require_phrases("Loop trace reference", loop_trace, [
        "Loop Trace Reference",
        "Purpose",
        "Generated Repo File",
        "Trace Entry Format",
        "Required Events",
        "Metrics",
        "Runner Rules",
        "Review Usage",
        "docs/loop-trace.md",
    ])

    require_phrases("Harness repair reference", harness_repair, [
        "Harness Repair Loop Reference",
        "Purpose",
        "Trigger Conditions",
        "Inputs",
        "Repair Scope",
        "Forbidden Repairs",
        "Repair Steps",
        "Validation Criteria",
        "Output",
    ])

    require_phrases("Loop hypotheses reference", loop_hypotheses, [
        "Loop Hypotheses Reference",
        "Purpose",
        "Generated Repo File",
        "Hypothesis Entry Format",
        "When To Create A Hypothesis",
        "Validation Rules",
        "Invalidation Rules",
        "Promotion Rules",
        "Rollback Rules",
        "docs/loop-hypotheses.md",
    ])

    require_phrases("README", readme, [
        "What It Does",
        "How It Works",
        "Get Started",
        "Workflow Sources",
        "Proof",
        "Compatibility",
        "Compared To",
        "Handoff Decision",
        "Feedback Taxonomy",
        "Loop Trace",
        "Harness Repair Loop",
        "hypothesis-gated renewal",
        "harness-layer root cause classification",
        "Review and Renewal Loop",
    ])

    require("github-loop-runner" in llms, "llms.txt must mention github-loop-runner")
    require("loop trace" in llms, "llms.txt must mention loop trace")
    require("feedback log" in llms, "llms.txt must mention feedback log")
    require("hypothesis log" in llms, "llms.txt must mention hypothesis log")
    require("harness repair protocol" in llms, "llms.txt must mention harness repair protocol")

    for path, text in [
        (README_FILE, readme),
        (LLMS_FILE, llms),
        (SKILL_FILE, skill),
        (SCAFFOLD_FILE, scaffold),
        (PROMPT_FILE, prompt),
        (HANDOFF_FILE, handoff),
        (FEEDBACK_FILE, feedback),
        (REVIEW_FILE, review),
        (STOPPER_FILE, stopper),
        (LOOP_REVIEW_FILE, loop_review),
        (LOOP_TRACE_FILE, loop_trace),
        (HARNESS_REPAIR_FILE, harness_repair),
        (LOOP_HYPOTHESES_FILE, loop_hypotheses),
    ]:
        assert_balanced_fences(path, text)

    require("[TODO" not in skill, "SKILL.md contains unresolved placeholder syntax")
    print("Skill validation passed")


if __name__ == "__main__":
    main()
