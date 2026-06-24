from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
README_FILE = REPO_ROOT / "README.md"
LLMS_FILE = REPO_ROOT / "llms.txt"

SKILL_DIR = REPO_ROOT / "skills" / "github-loop-runner"
SKILL_FILE = SKILL_DIR / "SKILL.md"
SCAFFOLD_FILE = SKILL_DIR / "references" / "repo-scaffold.md"
PROMPT_FILE = SKILL_DIR / "references" / "runner-prompt.md"
FEEDBACK_FILE = SKILL_DIR / "references" / "feedback-taxonomy.md"
REVIEW_FILE = SKILL_DIR / "references" / "review-and-renewal-loop.md"
STOPPER_FILE = SKILL_DIR / "references" / "stopper-policy.md"
LOOP_REVIEW_FILE = SKILL_DIR / "references" / "loop-review-template.md"
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
    feedback = read(FEEDBACK_FILE)
    review = read(REVIEW_FILE)
    stopper = read(STOPPER_FILE)
    loop_review = read(LOOP_REVIEW_FILE)
    openai_yaml = read(OPENAI_YAML)

    fm = frontmatter(skill)
    require("name: github-loop-runner" in fm, "Skill frontmatter must name github-loop-runner")
    require("GitHub-only" in fm and "autonomous" in fm, "Skill description must cover GitHub-only autonomous triggers")
    require("references/repo-scaffold.md" in skill, "SKILL.md must reference repo-scaffold.md")
    require("references/runner-prompt.md" in skill, "SKILL.md must reference runner-prompt.md")
    require("references/feedback-taxonomy.md" in skill, "SKILL.md must reference feedback-taxonomy.md")
    require("references/review-and-renewal-loop.md" in skill, "SKILL.md must reference review-and-renewal-loop.md")
    require("references/stopper-policy.md" in skill, "SKILL.md must reference stopper-policy.md")
    require("references/loop-review-template.md" in skill, "SKILL.md must reference loop-review-template.md")
    require("$github-loop-runner" in openai_yaml, "openai.yaml default prompt must invoke the skill")
    require("value: \"github\"" in openai_yaml, "openai.yaml must declare GitHub dependency")

    require_phrases("SKILL.md", skill, [
        "Capability Probe",
        "Source Workflow Map",
        "Optional Skill Invocation Map",
        "Feedback Taxonomy",
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
        "Workflow Discipline",
        "`docs/autonomous-runner.md` Template",
        "`docs/progress.md` Template",
        "Methodology Map",
        "Optional Skill Invocation Map",
        "Skill Pack Map",
        "Optional Runtime Invocations",
        "`docs/development-principles.md` Template",
        "`.github/workflows/verify.yml` Template",
    ])

    require_phrases("Runner prompt", prompt, [
        "GitHub-only runner",
        "Quietly probe GitHub connector capability",
        "docs/progress.md",
        "Feedback Taxonomy",
        "Review and Renewal Loop",
        "stopper policy",
        "source workflow discipline",
        "Matt Pocock",
        "Superpowers",
        "Karpathy",
        "Use CI as VERIFY",
        "Do not weaken tests",
    ])

    require_phrases("Feedback reference", feedback, [
        "Feedback Taxonomy Reference",
        "Feedback Sources",
        "Feedback Types",
        "Severity Levels",
        "Feedback Entry Format",
        "Allowed Action Map",
        "Runner Rules",
    ])

    require_phrases("Review reference", review, [
        "Review and Renewal Loop Reference",
        "Trigger Conditions",
        "Feedback Trends Since Last Review",
        "Review Steps",
        "Allowed Plan Updates",
        "Forbidden Plan Updates",
    ])

    require_phrases("Stopper reference", stopper, [
        "Stopper Policy Reference",
        "Hard Stoppers",
        "Soft Stoppers",
        "Default Limits",
        "Stopper Report",
    ])

    require_phrases("Loop review template", loop_review, [
        "Feedback Trends Since Last Review",
        "Feedback Decision",
        "Stopper Assessment",
        "Decision",
    ])

    require_phrases("README", readme, [
        "What It Does",
        "How It Works",
        "Get Started",
        "Workflow Sources",
        "Proof",
        "Compatibility",
        "Compared To",
        "Feedback Taxonomy",
        "Review and Renewal Loop",
    ])

    require("github-loop-runner" in llms, "llms.txt must mention github-loop-runner")

    for path, text in [
        (README_FILE, readme),
        (LLMS_FILE, llms),
        (SKILL_FILE, skill),
        (SCAFFOLD_FILE, scaffold),
        (PROMPT_FILE, prompt),
        (FEEDBACK_FILE, feedback),
        (REVIEW_FILE, review),
        (STOPPER_FILE, stopper),
        (LOOP_REVIEW_FILE, loop_review),
    ]:
        assert_balanced_fences(path, text)

    require("[TODO" not in skill, "SKILL.md contains unresolved placeholder syntax")
    print("Skill validation passed")


if __name__ == "__main__":
    main()
