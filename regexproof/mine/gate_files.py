"""List ``*_gate_decision.json`` without APFS glob collapse."""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DECISION_GLOB = "*_gate_decision.json"


def git_ls_decision_paths(
    directory: Path, *, repo_root: Path | None = None
) -> list[Path] | None:
    """Tracked decision files under *directory*, or None to fall back to glob.

    Filesystem ``glob`` on a case-insensitive volume collapses
    ``Validator_gate_decision.json`` and ``validator_gate_decision.json``.
    ``git ls-files`` still lists both. Return None when *directory* is
    outside the repo (tests use ``tmp_path``) or git listing is empty.
    """
    root = (repo_root or REPO_ROOT).resolve()
    try:
        rel = directory.resolve().relative_to(root)
    except ValueError:
        return None
    spec = DECISION_GLOB if rel.as_posix() == "." else f"{rel.as_posix()}/{DECISION_GLOB}"
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z", "--", spec],
            check=False,
            capture_output=True,
        )
    except OSError:
        return None
    if proc.returncode != 0 or not proc.stdout:
        return None
    paths = [root / name.decode() for name in proc.stdout.split(b"\0") if name]
    if not paths:
        return None
    return sorted(paths, key=lambda path: path.name)


def list_gate_decision_paths(
    directory: Path, *, repo_root: Path | None = None
) -> list[Path]:
    """Tracked listing when possible; otherwise filesystem glob."""
    tracked = git_ls_decision_paths(directory, repo_root=repo_root)
    if tracked is not None:
        return tracked
    return sorted(directory.glob(DECISION_GLOB), key=lambda path: path.name)
