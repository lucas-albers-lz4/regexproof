"""Flagged admission probe draft emitter (P1 A5 / umbrella C2)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from regexproof.admission.boundary import BoundarySignals, classify_boundary
from regexproof.admission.serialize import dumps_pinned
from regexproof.admission.walk import _SKIP_DIR_NAMES, walk_repo

# Exact list from umbrella C2 — fields the author script must fill.
FIELDS_REMAINING: list[str] = [
    "decision",
    "rationale",
    "conditions[].met",
    "conditions[].evidence",
    "decision_basis",
    "escape_hatch_applied",
    "related",
    "decision_date",
]


def _readme_text(root: Path) -> str:
    root_resolved = root.resolve()
    for name in ("README.md", "README.rst", "README", "readme.md"):
        p = root / name
        if p.is_symlink():
            continue
        if not p.is_file():
            continue
        try:
            resolved = p.resolve()
            if not resolved.is_relative_to(root_resolved):
                continue
            return resolved.read_text(encoding="utf-8", errors="replace")[:4000]
        except OSError:
            return ""
    return ""


def build_boundary_signals(
    *,
    repo_name: str,
    root: Path | None = None,
    topics: tuple[str, ...] = (),
) -> BoundarySignals:
    description = ""
    paths: list[str] = []
    if root is not None:
        description = _readme_text(root)
        # Sample path strings for path_substring signals (skip .git / vendor / …).
        try:
            paths = [
                str(p.relative_to(root))
                for p in sorted(root.rglob("*"))
                if not p.is_symlink()
                and p.is_file()
                and not any(part in _SKIP_DIR_NAMES for part in p.parts)
            ][:200]
        except OSError:
            paths = []
    return BoundarySignals(
        repo_name=repo_name,
        topics=topics,
        paths=tuple(paths),
        description=description,
    )


def build_draft(
    root: Path | str,
    *,
    pin: str,
    repo_name: str | None = None,
    candidate_url: str = "",
    topics: tuple[str, ...] = (),
) -> dict[str, Any]:
    """Build a flagged (non-schema-valid) probe draft for *root* at *pin*."""
    root_p = Path(root).resolve()
    name = repo_name or root_p.name
    walked = walk_repo(root_p, repo_name=name)
    boundary = classify_boundary(
        build_boundary_signals(repo_name=name, root=root_p, topics=topics)
    )
    return {
        "draft": True,
        "schema_version": "1",
        "corpus": name,
        "candidate_url": candidate_url or f"local://{name}",
        "corpus_pin": pin,
        "probe": {
            "regex_sites": walked["regex_sites"],
            "regex_sites_per_file": walked["regex_sites_per_file"],
            "dialect": walked["dialect"],
            "flags": walked["flags"],
            "construct_counts": walked["construct_counts"],
            "predicted_buckets": walked["predicted_buckets"],
            "security_boundary": boundary,
            "pin": pin,
        },
        "fields_remaining": list(FIELDS_REMAINING),
    }


def emit_draft_text(draft: dict[str, Any]) -> str:
    return dumps_pinned(draft)
