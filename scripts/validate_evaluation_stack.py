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
    refs = manifest.get("references", [])

    if manifest.get("skill", {}).get("release") != "v1":
        fail("Manifest must declare release v1")

    if manifest.get("skill", {}).get("stability") != "frozen":
        fail("Manifest must declare frozen stability")

    if not refs:
        fail("Manifest has no references")

    ids = {r["id"] for r in refs}
    expected_core = {
        "github_operation_ledger",
        "long_run_growth",
        "research_intake",
        "feedback_taxonomy",
        "loop_trace",
        "loop_hypotheses",
        "harness_repair_loop",
        "review_and_renewal_loop",
        "stopper_policy",
    }

    missing = expected_core - ids
    if missing:
        fail(f"Missing stable v1 core components in manifest: {sorted(missing)}")

    required_refs = [r for r in refs if r.get("required", True)]
    for ref in required_refs:
        path = REPO_ROOT / ref["file"]
        if not path.is_file():
            fail(f"Missing required reference file: {ref['file']}")

    non_goals = set(manifest.get("scope", {}).get("non_goals", []))
    required_non_goals = {
        "general agent OS",
        "runtime DSL expansion",
        "self-modifying CI interpreter",
        "unbounded protocol growth",
    }

    missing_non_goals = required_non_goals - non_goals
    if missing_non_goals:
        fail(f"Missing stable v1 non-goals: {sorted(missing_non_goals)}")

    print("Stable v1 validation passed")


if __name__ == "__main__":
    main()
