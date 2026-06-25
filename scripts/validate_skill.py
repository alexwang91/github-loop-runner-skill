from pathlib import Path
import sys
import json

REPO_ROOT = Path(__file__).resolve().parents[1]

README_FILE = REPO_ROOT / "README.md"
LLMS_FILE = REPO_ROOT / "llms.txt"
SKILL_FILE = REPO_ROOT / "skills" / "github-loop-runner" / "SKILL.md"
MANIFEST_FILE = REPO_ROOT / "config" / "skill_manifest.json"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"Missing file: {path.relative_to(REPO_ROOT)}")
    return path.read_text(encoding="utf-8")


def load_manifest() -> dict:
    if not MANIFEST_FILE.is_file():
        fail("Missing config/skill_manifest.json")
    return json.loads(read(MANIFEST_FILE))


def main() -> None:
    manifest = load_manifest()

    skill = read(SKILL_FILE)
    read(README_FILE)
    read(LLMS_FILE)

    # Validate references existence
    for ref in manifest.get("references", []):
        file_path = REPO_ROOT / ref["file"]
        if not file_path.is_file():
            fail(f"Missing reference file: {ref['file']}")

    # Validate required generated repo files
    for f in manifest.get("generated_repo", {}).get("required_files", []):
        if not (REPO_ROOT / f).is_file():
            fail(f"Missing required generated repo file: {f}")

    # Minimal sanity checks for SKILL.md
    if "github-loop-runner" not in skill:
        fail("SKILL.md missing skill name")

    print("Skill validation passed (manifest-driven)")


if __name__ == "__main__":
    main()