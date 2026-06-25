from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_FILE = REPO_ROOT / "config" / "skill_manifest.json"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def load_manifest() -> dict:
    if not MANIFEST_FILE.is_file():
        fail("Missing manifest")
    return json.loads(read(MANIFEST_FILE))


def main() -> None:
    manifest = load_manifest()

    # Minimal evaluation stack validation (manifest completeness check)
    required_refs = manifest.get("references", [])

    if not required_refs:
        fail("Manifest has no references")

    # Ensure core planes exist in architecture expectation
    required_ids = {r["id"] for r in required_refs}

    expected = {
        "github_operation_ledger",
        "long_run_growth",
        "feedback_taxonomy",
        "loop_trace",
        "agent_judge_loop",
        "runner_memory",
        "codebase_localization",
        "workflow_graph",
    }

    missing = expected - required_ids
    if missing:
        fail(f"Missing evaluation stack components in manifest: {missing}")

    print("Evaluation stack validation passed (manifest-driven)")


if __name__ == "__main__":
    main()