"""Deterministic mine candidate allocators.

Metadata-only ranking for queue drain / day-cap admit and the rank CLI.
Recompute every time — do not persist scores on disk.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

from regexproof.admission.boundary import BoundarySignals, classify_boundary
from regexproof.mine.features import (  # noqa: F401
    _QUERY_FAMILY,
    _parse_pushed,
    _query_family,
    _recency_points,
    _repo_slug,
    _stars_points,
)

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

_BOUNDARY_WEIGHTS: dict[str, float] = {
    "deterministic-true": 50.0,
    "unknown": 0.0,
    "deterministic-false": -40.0,
}


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
