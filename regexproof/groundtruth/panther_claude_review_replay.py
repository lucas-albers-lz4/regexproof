"""Exact-pin replay of Panther's staged-file Claude review filter."""

from __future__ import annotations

import hashlib
import importlib.util
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

PIN = "0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a"
REPOSITORY = "https://github.com/panther-labs/panther-analysis"
SOURCE_FILE = ".scripts/claude_review.py"
EXCLUDE_PATTERN = r"\.env$|\.pem$|\.key$|credentials\.json|secrets\.json|\.secret"
SOURCE_HASHES = {
    ".scripts/claude_review.py": "bb84d899da9cd10d82712610419f7802d84900541fd1e1c48a94223a12bc4024",
    ".claude/commands/pr-review.md": "3c6db4056e157cacf208037c6c00650bf2957b2b49d3c53934b8c43c51423ca0",
    ".scripts/pre-commit-wrapper.sh": "05c210b497e357fca50f41231b74dad46ee3c8b9360d314b3e95fcb7722e4a8d",
    "Makefile": "c217b722a6d10114d1543f120f3813f3e2c4d44f5a56c8192d015a7a0b377b71",
}


def source_root() -> Path:
    configured = os.environ.get("PANTHER_CLAUDE_REVIEW_REPLAY_SOURCE")
    if configured:
        return Path(configured).expanduser().resolve()
    return (
        Path(tempfile.gettempdir())
        / "regexproof-pinned-sources"
        / f"panther-analysis-{PIN}"
    )


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=not binary,
        timeout=20,
        check=True,
        shell=False,
    )
    return completed.stdout if binary else completed.stdout.strip()


def verify_checkout(root: Path) -> dict[str, Any]:
    """Authenticate the clean pinned files used by the path-filter contract."""
    root = root.expanduser().resolve()
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"Panther checkout is missing or a symlink: {root}")
    head = _git(root, "rev-parse", "HEAD")
    if head != PIN:
        raise ValueError(f"Panther checkout HEAD {head!r} does not match {PIN}")
    status = _git(root, "status", "--porcelain", "--untracked-files=all")
    if status:
        raise ValueError("Panther checkout must be clean")
    observed: dict[str, str] = {}
    for relative, expected in SOURCE_HASHES.items():
        current = root / relative
        if current.is_symlink() or not current.is_file():
            raise ValueError(f"pinned Panther source is missing or a symlink: {relative}")
        committed = _git(root, "show", f"{PIN}:{relative}", binary=True)
        if current.read_bytes() != committed:
            raise ValueError(f"Panther working file differs from pinned bytes: {relative}")
        digest = hashlib.sha256(committed).hexdigest()
        if digest != expected:
            raise ValueError(f"Panther source hash mismatch for {relative}: {digest}")
        observed[relative] = digest
    return {"head": head, "source_sha256": observed}


def _load_module(root: Path, pattern_override: str | None) -> Any:
    source = root / SOURCE_FILE
    name = f"regexproof_pinned_panther_review_{PIN}"
    spec = importlib.util.spec_from_file_location(name, source)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned Panther review helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if module.EXCLUDE_PATTERNS.pattern != EXCLUDE_PATTERN:
        raise ValueError("pinned Panther exclusion regex differs from inventory")
    if pattern_override is not None:
        module.EXCLUDE_PATTERNS = re.compile(pattern_override)
    return module


def _run_git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        timeout=15,
        check=True,
        shell=False,
    )
    return completed.stdout.strip()


def run_review_filter(
    paths: list[str],
    *,
    checkout: Path | None = None,
    pattern_override: str | None = None,
) -> dict[str, Any]:
    """Stage synthetic paths and replay exact get_changed_files/read_file_contents."""
    root = (checkout or source_root()).expanduser().resolve()
    source = verify_checkout(root)
    if not paths or any(not isinstance(path, str) or not path for path in paths):
        raise ValueError("at least one non-empty staged path is required")

    with tempfile.TemporaryDirectory(prefix="regexproof-panther-review-") as temp:
        repo = Path(temp) / "repo"
        repo.mkdir()
        _run_git(repo, "init", "--quiet")
        _run_git(repo, "config", "user.email", "regexproof@example.invalid")
        _run_git(repo, "config", "user.name", "regexproof fixture")
        (repo / "README.md").write_text("fixture repository\n", encoding="utf-8")
        _run_git(repo, "add", "README.md")
        _run_git(repo, "commit", "--quiet", "-m", "fixture base")

        sentinel_by_path: dict[str, str] = {}
        for index, relative in enumerate(paths):
            relative_path = Path(relative)
            if (
                relative_path.is_absolute()
                or not relative_path.parts
                or ".." in relative_path.parts
                or "\\" in relative
            ):
                raise ValueError(f"invalid fixture repository path: {relative!r}")
            target = repo / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.is_symlink():
                raise ValueError(f"fixture path is a symlink: {relative}")
            sentinel = f"PANTHER_SYNTHETIC_MARKER_{index:03d}"
            target.write_text(f"# synthetic staged fixture\n{sentinel}\n", encoding="ascii")
            sentinel_by_path[relative] = sentinel
        _run_git(repo, "add", "--", *paths)

        module = _load_module(root, pattern_override)
        module.REPO_ROOT = repo
        selected = module.get_changed_files()
        prompt = module.read_file_contents(selected)
        return {
            "source": source,
            "paths": {
                path: {
                    "selected_for_review": path in selected,
                    "sentinel_in_prompt": sentinel_by_path[path] in prompt,
                }
                for path in paths
            },
            "selected_paths": selected,
            "claude_invoked": False,
            "network_used": False,
        }


def secret_path_reaches_prompt(path: str) -> bool:
    try:
        result = run_review_filter([path])
    except (OSError, subprocess.SubprocessError, ValueError, RuntimeError):
        return False
    observation = result["paths"][path]
    return bool(observation["selected_for_review"] and observation["sentinel_in_prompt"])


def mutated_exclusion_allows_secret_py(_witness: dict[str, Any] | None = None) -> bool:
    try:
        result = run_review_filter(["password.secret.py"], pattern_override=r"^$")
    except (OSError, subprocess.SubprocessError, ValueError, RuntimeError):
        return False
    observation = result["paths"]["password.secret.py"]
    return bool(observation["selected_for_review"] and observation["sentinel_in_prompt"])


__all__ = [
    "EXCLUDE_PATTERN",
    "PIN",
    "REPOSITORY",
    "SOURCE_FILE",
    "SOURCE_HASHES",
    "mutated_exclusion_allows_secret_py",
    "run_review_filter",
    "secret_path_reaches_prompt",
    "source_root",
    "verify_checkout",
]
