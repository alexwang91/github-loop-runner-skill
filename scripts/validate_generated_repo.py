from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_ROOT = REPO_ROOT / "examples" / "minimal-product-handoff" / "generated"
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

    if not EXAMPLE_ROOT.is_dir():
        fail("Missing example generated repo")

    for f in manifest.get("generated_repo", {}).get("required_files", []):
        if not (EXAMPLE_ROOT / f).is_file():
            fail(f"Missing generated repo file: {f}")

    print("Generated repo validation passed (manifest-driven)")


if __name__ == "__main__":
    main()