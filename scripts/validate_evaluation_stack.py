from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REFERENCES = REPO_ROOT / "skills" / "github-loop-runner" / "references"
SCHEMAS = REPO_ROOT / "schemas"
EXAMPLE = REPO_ROOT / "examples" / "minimal-product-handoff" / "generated"

REFERENCE_FILES = {
    "agent-judge-loop.md": ["Agent Judge Loop Reference", "Judge Dimensions", "Judge Report Format", "Verdicts"],
    "growth-candidate-selection.md": ["Growth Candidate Selection Reference", "Candidate Generation", "Candidate Batch Format", "Scoring Rules"],
    "runner-memory.md": ["Runner Memory Reference", "Memory Cycle", "Memory Entry Format", "Memory Types"],
    "codebase-localization.md": ["Codebase Localization Reference", "Localization Record Format", "Required Fields", "Rules"],
    "workflow-graph.md": ["Workflow Graph Reference", "Default Graph", "Node Record Format", "Rules"],
    "loop-acceptance-tests.md": ["Loop Acceptance Tests Reference", "Acceptance Checks", "Example Check List", "Rules"],
}

SCHEMA_FILES = [
    "judge-report.schema.json",
    "growth-candidate.schema.json",
    "runner-memory.schema.json",
    "code-area-map.schema.json",
]

EXAMPLE_FILES = [
    "docs/agent-judge-loop.md",
    "docs/growth-candidates.md",
    "docs/runner-memory.md",
    "docs/codebase-localization.md",
    "docs/workflow-graph.md",
    "docs/loop-acceptance-tests.md",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def read(path: Path) -> str:
    require(path.is_file(), f"Missing file: {path.relative_to(REPO_ROOT)}")
    return path.read_text(encoding="utf-8")


def validate_references() -> None:
    for filename, phrases in REFERENCE_FILES.items():
        text = read(REFERENCES / filename)
        for phrase in phrases:
            require(phrase in text, f"{filename} missing phrase: {phrase}")


def validate_schemas() -> None:
    for filename in SCHEMA_FILES:
        path = SCHEMAS / filename
        parsed = json.loads(read(path))
        require(isinstance(parsed, dict), f"Schema must be an object: {filename}")
        require("$schema" in parsed, f"Schema missing $schema: {filename}")
        require("title" in parsed, f"Schema missing title: {filename}")


def validate_example_files() -> None:
    for filename in EXAMPLE_FILES:
        require((EXAMPLE / filename).is_file(), f"Example missing {filename}")

    workflow = read(EXAMPLE / ".github" / "workflows" / "verify.yml")
    for filename in EXAMPLE_FILES:
        require(filename in workflow, f"Example workflow does not check {filename}")


def run_generated_repo_validator() -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "validate_generated_repo.py"), str(EXAMPLE)],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        fail("Generated repo validator failed")
    if result.stdout:
        print(result.stdout.strip())


def main() -> None:
    validate_references()
    validate_schemas()
    validate_example_files()
    run_generated_repo_validator()
    print("Evaluation stack validation passed")


if __name__ == "__main__":
    main()
