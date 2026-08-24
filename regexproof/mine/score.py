"""Deterministic mine candidate allocators.

Metadata-only ranking for queue drain / day-cap admit and the rank CLI.
Recompute every time — do not persist scores on disk.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

from regexproof.admission.boundary import BoundarySignals, classify_boundary
from regexproof.mine.root_dir import root_dir_deprioritized, root_names_from_paths
from regexproof.mine.deny_list import slug_denied
from regexproof.mine.features import (  # noqa: F401
    _QUERY_FAMILY,
    _parse_pushed,
    _query_family,
    _recency_points,
    _repo_slug,
    _stars_points,
)

SCORE_VERSION = "v1"
ALLOCATORS = ("score-v1", "score-v1.5", "score-v2")
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

# Tree-overlay weights for score-v1.5 (#550 Phase 1 / Item II, REVISION 8).
# FROZEN in Phase 0: feature definitions + weights are committed here and
# referenced by the Phase 0 freeze artifact; Phase 1's offline eval consumes
# the P0 freeze (fails closed on hash mismatch) and records the flip
# decision. The overlay is additive on top of the v1 base — tree counts
# NEVER drive auto-NO-GO without a walk (the walk is the boundary signal).
_TREE_OVERLAY_WEIGHTS: dict[str, float] = {
    "tree_regex_files_log": 6.0,
    "tree_python": 4.0,
    "tree_javascript": 3.0,
    "tree_yara": 5.0,
    "tree_shell": 3.0,
    "tree_config": 2.0,
    "tree_path_log": 1.0,
    "tree_boundary_true": 8.0,
    "tree_boundary_false": -6.0,
    "tree_unavailable": -5.0,
}

_TREE_PYTHON_SUFFIXES = {".py", ".pyi"}
_TREE_JS_SUFFIXES = {".js", ".mjs", ".cjs", ".ts", ".tsx"}
_TREE_CONFIG_SUFFIXES = {".json", ".yaml", ".yml", ".toml", ".ini", ".conf"}
_TREE_YARA_SUFFIXES = {".yar", ".yara"}
_TREE_SHELL_SUFFIXES = {".sh", ".bash", ".zsh"}


def _tree_overlay_signals(tree_feature: dict[str, Any] | None) -> dict[str, float]:
    """Extract the frozen v1.5 tree-overlay signals from a tree probe.

    ``tree_feature`` is the TreeProbeResult dict (or None when no probe ran).
    A missing/incomplete/truncated probe yields ``tree_unavailable=1`` and
    zero for the file-type signals — the deprioritized tier."""
    signals: dict[str, float] = {name: 0.0 for name in _TREE_OVERLAY_WEIGHTS}
    if not isinstance(tree_feature, dict):
        signals["tree_unavailable"] = 1.0
        return signals
    complete = tree_feature.get("complete") is True and tree_feature.get("truncated") is not True
    boundary = str(tree_feature.get("security_boundary") or "unknown")
    signals["tree_boundary_true"] = 1.0 if boundary == "deterministic-true" else 0.0
    signals["tree_boundary_false"] = 1.0 if boundary == "deterministic-false" else 0.0
    if not complete:
        signals["tree_unavailable"] = 1.0
        return signals
    counts = tree_feature.get("regex_file_type_counts")
    counts = counts if isinstance(counts, dict) else {}

    def _scaled_log(value: int | None) -> float:
        if value is None or value <= 0:
            return 0.0
        import math

        return round(math.log1p(float(value)), 4)

    signals["tree_regex_files_log"] = _scaled_log(
        sum(max(0, int(v or 0)) for v in counts.values())
    )
    signals["tree_python"] = _scaled_log(
        sum(int(counts.get(s) or 0) for s in _TREE_PYTHON_SUFFIXES)
    )
    signals["tree_javascript"] = _scaled_log(
        sum(int(counts.get(s) or 0) for s in _TREE_JS_SUFFIXES)
    )
    signals["tree_config"] = _scaled_log(
        sum(int(counts.get(s) or 0) for s in _TREE_CONFIG_SUFFIXES)
    )
    signals["tree_yara"] = _scaled_log(
        sum(int(counts.get(s) or 0) for s in _TREE_YARA_SUFFIXES)
    )
    signals["tree_shell"] = _scaled_log(
        sum(int(counts.get(s) or 0) for s in _TREE_SHELL_SUFFIXES)
    )
    signals["tree_path_log"] = _scaled_log(tree_feature.get("path_count"))
    return signals


def _root_names_for_screen(
    cand: dict[str, Any], tree_feature: dict[str, Any] | None
) -> list[str]:
    """Depth-1 names from a fresh tree summary, else walked file paths.

    Historical ``mine-tree-features.json`` rows omit ``root_dir_names``.
    Missing names are *unknown*, not a deprioritize.
    """
    if isinstance(tree_feature, dict):
        names = tree_feature.get("root_dir_names") or ()
        if names:
            return [str(n) for n in names]
    probe = cand.get("probe") if isinstance(cand.get("probe"), dict) else {}
    files = probe.get("regex_sites_per_file")
    if not isinstance(files, dict):
        files = cand.get("regex_sites_per_file")
    if isinstance(files, dict) and files:
        return root_names_from_paths(files)
    return []


def wave9_soft_flags(
    cand: dict[str, Any],
    tree_feature: dict[str, Any] | None,
    *,
    deny_slugs: set[str] | None = None,
    code_search_hits: int | None = None,
) -> dict[str, bool]:
    """Wave 9 (#578) screens: never drop a candidate, only flag deprioritize.

    ``code_search_hits is None`` means the density probe did not run or
    degraded (rate-limit) — that is *not* an empty-hit signal.
    Historical tree summaries without ``root_dir_names`` do not flag.
    """
    names = _root_names_for_screen(cand, tree_feature)
    root = bool(names) and root_dir_deprioritized(names)
    denied = bool(deny_slugs) and slug_denied(str(cand.get("url") or ""), deny_slugs)
    return {
        "root_dir_deprioritized": bool(root),
        "deny_list": bool(denied),
        "code_search_empty": code_search_hits == 0,
    }


def wave9_deprioritize(flags: dict[str, bool]) -> bool:
    return bool(
        flags.get("root_dir_deprioritized")
        or flags.get("deny_list")
        or flags.get("code_search_empty")
    )


def _v1_base_score(
    cand: dict[str, Any], *, today: date | None
) -> tuple[float, dict[str, Any]]:
    """The score-v1 base (boundary + family + stars + recency + capped)."""
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


def candidate_score(
    cand: dict[str, Any],
    *,
    today: date | None = None,
    allocator: str = "score-v1",
    tree_feature: dict[str, Any] | None = None,
    deny_slugs: set[str] | None = None,
    code_search_hits: int | None = None,
) -> tuple[float, dict[str, Any]]:
    """Return ``(total, breakdown)`` for a ledger/queue candidate row.

    Wave 9 screens are recorded on ``breakdown["wave9_soft"]`` and never
    mutate the numeric total (v1 pin 49.0 / frozen v1.5 overlay stay put).
    """
    allocator = _normalize_allocator(allocator)
    hits = code_search_hits
    if hits is None:
        raw = cand.get("code_search_hits")
        hits = int(raw) if isinstance(raw, int) else None
    flags = wave9_soft_flags(
        cand,
        tree_feature,
        deny_slugs=deny_slugs,
        code_search_hits=hits,
    )
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
            "wave9_soft": flags,
        }
        return total, breakdown

    base_total, base = _v1_base_score(cand, today=today)
    if allocator == "score-v1":
        base["allocator"] = allocator
        base["score_version"] = "v1"
        base["wave9_soft"] = flags
        return base_total, base

    # score-v1.5: v1 base + frozen tree overlay (#550 Phase 1 / Item II).
    signals = _tree_overlay_signals(tree_feature)
    overlay_pts = sum(
        _TREE_OVERLAY_WEIGHTS[name] * signals[name] for name in _TREE_OVERLAY_WEIGHTS
    )
    total = round(base_total + overlay_pts, 4)
    breakdown = {
        "allocator": allocator,
        "score_version": "v1.5",
        **base,
        "tree_unavailable": signals["tree_unavailable"] == 1.0,
        "tree_signals": {k: v for k, v in signals.items() if v != 0.0},
        "tree_overlay_pts": round(overlay_pts, 4),
        "wave9_soft": flags,
        "total": total,
    }
    return total, breakdown


def rank_candidates(
    cands: list[dict[str, Any]],
    *,
    today: date | None = None,
    allocator: str = "score-v1",
    tree_features: dict[tuple[str, str], dict[str, Any]] | None = None,
    deny_slugs: set[str] | None = None,
    density_hits: dict[str, int | None] | None = None,
) -> list[dict[str, Any]]:
    """Return a new list sorted highest score first; ties by ``url`` ascending.

    For score-v1.5, tree-available rows form a HARD upper tier: a candidate
    with a complete tree probe always outranks one without, regardless of
    base score (the design's deprioritized-tier rule). Within each tier,
    sort by total score descending.

    Wave 9 (#578) adds a *soft* inner tier (root-dir / deny-list / empty
    code-search). Soft-deprioritized rows still appear — they are never
    dropped from the pool.
    """
    allocator = _normalize_allocator(allocator)

    def _hits_for(c: dict[str, Any]) -> int | None:
        if density_hits is None:
            raw = c.get("code_search_hits")
            return int(raw) if isinstance(raw, int) else None
        url = str(c.get("url") or "")
        if url in density_hits:
            return density_hits[url]
        from regexproof.mine.exclusions import normalize_repo_url

        return density_hits.get(normalize_repo_url(url))

    def _score(c: dict[str, Any]) -> tuple[float, dict[str, Any], dict[str, Any] | None]:
        tree = _tree_feature_for_candidate(c, tree_features)
        total, breakdown = candidate_score(
            c,
            today=today,
            allocator=allocator,
            tree_feature=tree,
            deny_slugs=deny_slugs,
            code_search_hits=_hits_for(c),
        )
        return total, breakdown, tree

    if allocator != "score-v1.5":
        def sort_key(c: dict[str, Any]) -> tuple[int, float, str]:
            total, breakdown, _tree = _score(c)
            soft = 1 if wave9_deprioritize(breakdown.get("wave9_soft") or {}) else 0
            return (soft, -total, str(c.get("url") or ""))

        return sorted(cands, key=sort_key)

    def v15_sort_key(c: dict[str, Any]) -> tuple[int, int, float, str]:
        total, breakdown, _tree = _score(c)
        available = not bool(breakdown.get("tree_unavailable"))
        soft = 1 if wave9_deprioritize(breakdown.get("wave9_soft") or {}) else 0
        # Tier 0 = tree-available (hard upper), tier 1 = unavailable.
        # Soft deprioritize is inner: available+flagged still beats unavailable.
        return (0 if available else 1, soft, -total, str(c.get("url") or ""))

    return sorted(cands, key=v15_sort_key)


def _normalize_allocator(value: str) -> str:
    value = str(value or "score-v1").strip().lower()
    if value in {"v1", "score-v1"}:
        return "score-v1"
    if value in {"v1.5", "score-v1.5"}:
        return "score-v1.5"
    if value in {"v2", "score-v2"}:
        return "score-v2"
    raise ValueError(
        f"unknown allocator {value!r}; expected score-v1, score-v1.5 or score-v2"
    )


def score_version_for_allocator(value: str) -> str:
    norm = _normalize_allocator(value)
    if norm == "score-v2":
        return "v2"
    if norm == "score-v1.5":
        return "v1.5"
    return "v1"


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
