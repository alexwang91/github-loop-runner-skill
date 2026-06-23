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


def main() -> None:
    readme = read(README_FILE)
    llms = read(LLMS_FILE)
    skill = read(SKILL_FILE)
    scaffold = read(SCAFFOLD_FILE)
    prompt = read(PROMPT_FILE)
    openai_yaml = read(OPENAI_YAML)

    fm = frontmatter(skill)
    require("name: github-loop-runner" in fm, "Skill frontmatter must name github-loop-runner")
    require("GitHub-only" in fm and "autonomous" in fm, "Skill description must cover GitHub-only autonomous triggers")
    require("references/repo-scaffold.md" in skill, "SKILL.md must reference repo-scaffold.md")
    require("references/runner-prompt.md" in skill, "SKILL.md must reference runner-prompt.md")
    require("$github-loop-runner" in openai_yaml, "openai.yaml default prompt must invoke the skill")
    require("value: \"github\"" in openai_yaml, "openai.yaml must declare GitHub dependency")

    required_skill_phrases = [
        "Capability Probe",
        "Source Workflow Map",
        "Optional Skill Invocation Map",
        "$grill-with-docs",
        "$to-issues",
        "$brainstorming",
        "$writing-plans",
        "$test-driven-development",
        "$requesting-code-review",
        "$finishing-a-development-branch",
    ]
    for phrase in required_skill_phrases:
        require(phrase in skill, f"SKILL.md missing phrase: {phrase}")

    required_scaffold_sections = [
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
    ]
    for section in required_scaffold_sections:
        require(section in scaffold, f"Scaffold missing section: {section}")

    required_prompt_phrases = [
        "GitHub-only runner",
        "Quietly probe GitHub connector capability",
        "docs/progress.md",
        "source workflow discipline",
        "Matt Pocock",
        "Superpowers",
        "Karpathy",
        "Use CI as VERIFY",
        "Do not weaken tests",
    ]
    for phrase in required_prompt_phrases:
        require(phrase in prompt, f"Runner prompt missing phrase: {phrase}")

    required_readme_sections = [
        "What It Does",
        "How It Works",
        "Get Started",
        "Workflow Sources",
        "Proof",
        "Compatibility",
        "Compared To",
    ]
    for section in required_readme_sections:
        require(section in readme, f"README missing section: {section}")

    require("github-loop-runner" in llms, "llms.txt must mention github-loop-runner")

    for path, text in [
        (README_FILE, readme),
        (LLMS_FILE, llms),
        (SKILL_FILE, skill),
        (SCAFFOLD_FILE, scaffold),
        (PROMPT_FILE, prompt),
    ]:
        assert_balanced_fences(path, text)

    require("[TODO" not in skill, "SKILL.md contains unresolved placeholder syntax")
    print("Skill validation passed")


if __name__ == "__main__":
    main()
