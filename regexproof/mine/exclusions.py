"""Candidate exclusions for mining (P2 B3)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[2]
GENERATED = REPO_ROOT / "properties" / "generated"

EXCLUDE_OWNERS = frozenset(
    {
        "lucas-albers-lz4",
    }
)


def _owner_from_url(url: str) -> str | None:
    # https://github.com/owner/repo or git@github.com:owner/repo.git
    if url.startswith("git@"):
        try:
            path = url.split(":", 1)[1]
            return path.split("/")[0].lower()
        except IndexError:
            return None
    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) >= 1:
        return parts[0].lower().removesuffix(".git")
    return None


def normalize_repo_url(url: str) -> str:
    """Canonical https://github.com/owner/repo form (scheme/host/.git tolerant)."""
    u = url.strip()
    if u.startswith("git@"):
        try:
            path = u.split(":", 1)[1]
        except IndexError:
            return u.lower()
        parts = [p for p in path.split("/") if p]
        if len(parts) >= 2:
            owner, repo = parts[0], parts[1].removesuffix(".git")
            return f"https://github.com/{owner}/{repo}".lower()
        return path.removesuffix(".git").lower()
    parsed = urlparse(u)
    host = (parsed.hostname or "").lower()
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) >= 2:
        owner, repo = parts[0], parts[1].removesuffix(".git")
        if host.endswith("github.com") or not host:
            return f"https://github.com/{owner}/{repo}".lower()
        return f"https://{host}/{owner}/{repo}".lower()
    fallback = u.rstrip("/")
    if fallback.endswith(".git"):
        fallback = fallback[:-4]
    return fallback.lower()


def load_admitted_urls(generated_dir: Path | None = None) -> set[str]:
    d = generated_dir or GENERATED
    out: set[str] = set()
    for p in sorted(d.glob("*_gate_decision.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        url = data.get("candidate_url")
        if url:
            out.add(normalize_repo_url(str(url)))
    return out


def load_ledger_urls(ledger: dict[str, Any]) -> set[str]:
    return {
        normalize_repo_url(str(c.get("url")))
        for c in ledger.get("candidates", [])
        if c.get("url")
    }


def is_excluded(
    url: str,
    *,
    ledger: dict[str, Any] | None = None,
    admitted: set[str] | None = None,
    exclude_owners: frozenset[str] = EXCLUDE_OWNERS,
) -> str | None:
    """Return exclusion reason or None if allowed."""
    owner = _owner_from_url(url)
    if owner and owner in exclude_owners:
        return f"excluded-owner:{owner}"
    norm = normalize_repo_url(url)
    if admitted is not None and norm in admitted:
        return "already-admitted"
    if ledger is not None and norm in load_ledger_urls(ledger):
        return "already-ledgered"
    return None
