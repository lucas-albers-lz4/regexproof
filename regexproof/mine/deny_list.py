"""Wave 9 (#578): post-walk probe deny-list (soft down-rank, never hard-reject).

Distinct from conversion ``wont_file`` / ``docs/conversion-upstream.jsonl``.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from regexproof.mine.exclusions import github_repo_slug

DENY_LIST_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "generated"
    / "probe_deny_list.json"
)
SCHEMA_VERSION = "1"


def load_deny_slugs(path: Path | None = None) -> set[str]:
    p = path if path is not None else DENY_LIST_PATH
    if not p.is_file():
        return set()
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    slugs = doc.get("slugs") if isinstance(doc, dict) else None
    if not isinstance(slugs, list):
        return set()
    return {str(s).lower() for s in slugs if str(s).strip()}


def slug_denied(url: str, slugs: set[str]) -> bool:
    slug = github_repo_slug(url).lower()
    return bool(slug) and slug in slugs


def build_deny_doc(decisions: list[dict[str, Any]]) -> dict[str, Any]:
    slugs: set[str] = set()
    for dec in decisions:
        probe = dec.get("probe") if isinstance(dec.get("probe"), dict) else {}
        related = dec.get("related") if isinstance(dec.get("related"), dict) else {}
        if related.get("probe_failure") or dec.get("probe_failure"):
            continue
        pin = str(dec.get("corpus_pin") or probe.get("pin") or "")
        if not pin.strip():
            continue
        sites_raw = probe.get("regex_sites")
        if type(sites_raw) is not int or sites_raw != 0:
            continue
        url = str(dec.get("candidate_url") or "")
        slug = github_repo_slug(url).lower()
        if slug:
            slugs.add(slug)
    return {
        "schema_version": SCHEMA_VERSION,
        "not_conversion_wont_file": True,
        "hard_reject": False,
        "note": (
            "Zero-surface post-walk signatures. Rank applies a soft "
            "deprioritize (sort tier) only. Distinct from conversion wont_file."
        ),
        "slugs": sorted(slugs),
    }
