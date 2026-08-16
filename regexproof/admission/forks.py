"""Fork/duplicate detection at admission (#481)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

KNOWN_INTERPRETER_PARENTS = frozenset(
    {
        "python/cpython",
        "stackless-dev/stackless",
    }
)


def normalize_github_repo(url_or_name: str) -> str:
    s = (url_or_name or "").strip().rstrip("/")
    s = s.removeprefix("https://github.com/")
    s = s.removeprefix("http://github.com/")
    s = s.removeprefix("git@github.com:")
    if s.endswith(".git"):
        s = s[:-4]
    return s.lower()


def parent_full_name(meta: dict[str, Any]) -> str:
    parent = meta.get("parent")
    if isinstance(parent, dict):
        name = parent.get("full_name") or ""
        if name:
            return str(name)
    return str(meta.get("parent_full_name") or "")


def load_go_repo_names(generated_dir: Path) -> set[str]:
    names: set[str] = set()
    for path in sorted(generated_dir.glob("*_gate_decision.json"), key=lambda p: p.name):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if data.get("decision") != "go":
            continue
        url = str(data.get("candidate_url") or "")
        if url:
            names.add(normalize_github_repo(url))
    return names


def fork_duplicate_reason(
    meta: dict[str, Any],
    *,
    go_repos: set[str],
) -> str | None:
    """Return a NO-GO reason if this candidate is a duplicate fork."""
    if not meta.get("fork"):
        return None
    parent = parent_full_name(meta)
    parent_key = normalize_github_repo(parent) if parent else ""
    self_name = normalize_github_repo(
        str(meta.get("full_name") or meta.get("url") or "")
    )
    if parent_key and parent_key in go_repos:
        return f"fork of already-GO parent {parent_key}"
    if parent_key in KNOWN_INTERPRETER_PARENTS:
        return f"interpreter fork of {parent_key} — duplicate class"
    if self_name.endswith("/cpython") or self_name.split("/")[-1] == "cpython":
        if "python/cpython" in go_repos or parent_key == "python/cpython":
            return "CPython fork — duplicate class"
        return "CPython-named fork — duplicate class"
    return None
