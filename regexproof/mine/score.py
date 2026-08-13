"""Deterministic mine candidate allocators.

Metadata-only ranking for queue drain / day-cap admit and the rank CLI.
Recompute every time — do not persist scores on disk.
"""

from __future__ import annotations

import math
import re
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from regexproof.admission.boundary import BoundarySignals, classify_boundary
from regexproof.mine.search import SEARCH_QUERIES

SCORE_VERSION = "v1"
ALLOCATORS = ("score-v1", "score-v2")
SCORE_V2_WEIGHTS_PATH = Path(__file__).resolve().with_name("score_v2_weights.json")

# Family weights locked in #148 plan.
_FAMILY_WEIGHTS: dict[str, float] = {
    "security": 30.0,
    "rules": 25.0,
    "validators": 20.0,
    "testdata": 5.0,
    "other": 10.0,
}

# Map exact SEARCH_QUERIES strings → family (order matches search.py comments).
_QUERY_FAMILY: dict[str, str] = {
    SEARCH_QUERIES[0]: "security",
    SEARCH_QUERIES[1]: "security",
    SEARCH_QUERIES[2]: "security",
    SEARCH_QUERIES[3]: "validators",
    SEARCH_QUERIES[4]: "validators",
    SEARCH_QUERIES[5]: "rules",
    SEARCH_QUERIES[6]: "rules",
    SEARCH_QUERIES[7]: "rules",
    SEARCH_QUERIES[8]: "testdata",
    SEARCH_QUERIES[9]: "testdata",
    SEARCH_QUERIES[10]: "security",   # .gitleaks.toml
    SEARCH_QUERIES[11]: "security",   # .trufflehog.yml/.toml
    SEARCH_QUERIES[12]: "security",   # secretlintrc
    SEARCH_QUERIES[13]: "rules",      # semgrep.yml/yaml (semgrep = rules family)
    SEARCH_QUERIES[14]: "security",   # secrets.yml/yaml
    SEARCH_QUERIES[15]: "rules",      # index.yar
    SEARCH_QUERIES[16]: "rules",      # path:signatures extension:yar
    SEARCH_QUERIES[17]: "rules",      # rules.yar path:rules
    SEARCH_QUERIES[18]: "validators", # validator.py/validators.py path:src
    SEARCH_QUERIES[19]: "testdata",   # regex_test.go / regexp_test.go
}

_BOUNDARY_WEIGHTS: dict[str, float] = {
    "deterministic-true": 50.0,
    "unknown": 0.0,
    "deterministic-false": -40.0,
}


def _repo_slug(url: str) -> str:
    """Return ``owner/repo`` (or last path segment) from a GitHub-ish URL."""
    u = (url or "").strip()
    if u.startswith("git@"):
        try:
            path = u.split(":", 1)[1]
        except IndexError:
            return u
        parts = [p for p in path.split("/") if p]
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1].removesuffix('.git')}"
        return path.removesuffix(".git")
    parsed = urlparse(u)
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1].removesuffix('.git')}"
    if parts:
        return parts[0].removesuffix(".git")
    return u


def _query_family(source_query: str) -> str:
    q = (source_query or "").strip()
    if q in _QUERY_FAMILY:
        return _QUERY_FAMILY[q]
    # Fuzzy fallback if query text drifted slightly
    ql = q.lower()
    if "gitleaks" in ql or "detect-secrets" in ql or "trufflehog" in ql or "secretlint" in ql or "secrets." in ql:
        return "security"
    if "semgrep" in ql or "yara" in ql or "secrule" in ql or "extension:yar" in ql or ".yar" in ql or "yar " in ql:
        return "rules"
    if "validator" in ql:
        return "validators"
    if "testdata" in ql or "re_tests" in ql or "test_re" in ql or "regex_test" in ql or "regexp_test" in ql:
        return "testdata"
    return "other"


def _parse_pushed(pushed: str) -> date | None:
    s = (pushed or "").strip()
    if not s:
        return None
    # Accept YYYY-MM-DD or full ISO timestamps.
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", s)
    if not m:
        return None
    try:
        return date.fromisoformat(m.group(1))
    except ValueError:
        return None


def _recency_points(pushed: str, *, today: date | None = None) -> float:
    d = _parse_pushed(pushed)
    if d is None:
        return 0.0
    today = today or datetime.now(timezone.utc).date()
    age = (today - d).days
    if age < 0:
        age = 0
    if age <= 365:
        return 15.0
    if age <= 365 * 3:
        return 5.0
    return 0.0


def _stars_points(stars: int) -> float:
    return float(min(25, math.floor(8 * math.log10(max(0, stars) + 1))))


def candidate_score(
    cand: dict[str, Any],
    *,
    today: date | None = None,
    allocator: str = "score-v1",
    tree_feature: dict[str, Any] | None = None,
) -> tuple[float, dict[str, Any]]:
    """Return ``(total, breakdown)`` for a ledger/queue candidate row."""
    allocator = _normalize_allocator(allocator)
    if allocator == "score-v2":
        from regexproof.mine.score_v2 import linear_score, load_weights

        model = load_weights(SCORE_V2_WEIGHTS_PATH)
        # P8 (luna gate 1): recency features must use the artifact's FIT
        # date, not the runtime's clock — a refit with a later date would
        # otherwise score inconsistently with training.
        fit_date = today if today is not None else model.get("date")
        total = linear_score(cand, model, today=fit_date, tree_feature=tree_feature)
        breakdown: dict[str, Any] = {
            "allocator": allocator,
            "score_version": "v2",
            "total": total,
            "feature_set": model.get("feature_set", "v2"),
        }
        return total, breakdown

    url = str(cand.get("url") or "")
    slug = _repo_slug(url)
    repo_name = slug.split("/")[-1] if slug else ""
    boundary = classify_boundary(BoundarySignals(repo_name=repo_name))
    boundary_pts = _BOUNDARY_WEIGHTS.get(boundary, 0.0)

    family = _query_family(str(cand.get("source_query") or ""))
    family_pts = _FAMILY_WEIGHTS.get(family, _FAMILY_WEIGHTS["other"])

    stars = int(cand.get("stars") or 0)
    stars_pts = _stars_points(stars)

    recency_pts = _recency_points(str(cand.get("pushed_date") or ""), today=today)

    capped = bool(cand.get("capped"))
    capped_pts = -10.0 if capped else 0.0

    total = boundary_pts + family_pts + stars_pts + recency_pts + capped_pts
    breakdown: dict[str, Any] = {
        "allocator": allocator,
        "score_version": "v1",
        "boundary": boundary,
        "boundary_pts": boundary_pts,
        "family": family,
        "family_pts": family_pts,
        "stars": stars,
        "stars_pts": stars_pts,
        "recency_pts": recency_pts,
        "capped": capped,
        "capped_pts": capped_pts,
        "total": total,
    }
    return total, breakdown


def rank_candidates(
    cands: list[dict[str, Any]],
    *,
    today: date | None = None,
    allocator: str = "score-v1",
    tree_features: dict[tuple[str, str], dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Return a new list sorted highest score first; ties by ``url`` ascending."""

    allocator = _normalize_allocator(allocator)

    def sort_key(c: dict[str, Any]) -> tuple[float, str]:
        total, _ = candidate_score(
            c,
            today=today,
            allocator=allocator,
            tree_feature=_tree_feature_for_candidate(c, tree_features),
        )
        return (-total, str(c.get("url") or ""))

    return sorted(cands, key=sort_key)


def _normalize_allocator(value: str) -> str:
    value = str(value or "score-v1").strip().lower()
    if value in {"v1", "score-v1"}:
        return "score-v1"
    if value in {"v2", "score-v2"}:
        return "score-v2"
    raise ValueError(f"unknown allocator {value!r}; expected score-v1 or score-v2")


def score_version_for_allocator(value: str) -> str:
    return "v2" if _normalize_allocator(value) == "score-v2" else "v1"


def _tree_feature_for_candidate(
    cand: dict[str, Any],
    tree_features: dict[tuple[str, str], dict[str, Any]] | None,
) -> dict[str, Any] | None:
    if tree_features is None:
        value = cand.get("tree_probe")
        return value if isinstance(value, dict) else None
    url = str(cand.get("url") or "")
    pin = str(cand.get("pin_probed") or "")
    if not url:
        return None
    normalized = url
    if normalized.startswith("https://github.com/"):
        normalized = normalized.rstrip("/")
    value = tree_features.get((normalized, pin))
    if value is not None:
        return value
    # Callers using normalize_repo_url can provide canonical keys; keep the
    # direct lookup above fast for the common tracked-artifact form.
    from regexproof.mine.exclusions import normalize_repo_url

    value = tree_features.get((normalize_repo_url(url), pin))
    return value if isinstance(value, dict) else None
