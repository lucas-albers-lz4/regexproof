"""Wave 1 (#557): score-v1.5 tree-overlay allocator.

score-v1.5 = the v1 base + a FROZEN tree overlay (file-suffix counts + path
vocabulary from the tree probe). The overlay NEVER drives auto-NO-GO without
a walk — the walk is the boundary signal; tree counts only re-rank.
Live drain stays score-v1; v1.5 is evaluated offline per the P0 frozen
protocol and flips only if the bootstrap difference CI excludes 0."""

from __future__ import annotations

from regexproof.mine.score import (
    _TREE_OVERLAY_WEIGHTS,
    _normalize_allocator,
    _tree_overlay_signals,
    candidate_score,
    rank_candidates,
    score_version_for_allocator,
)

CAND = {
    "url": "https://github.com/openwrt/packages",
    "source_query": "security",
    "stars": 1200,
    "pushed_date": "2026-08-01",
    "capped": False,
}

COMPLETE_TREE = {
    "complete": True,
    "truncated": False,
    "security_boundary": "deterministic-true",
    "regex_file_type_counts": {".py": 40, ".yara": 12, ".json": 8},
    "path_count": 300,
}


def test_v1_reproduction_is_unchanged():
    """--allocator score-v1 must reproduce the v1 totals exactly (the v1.5
    branch must not disturb the base path)."""
    t1, b1 = candidate_score(CAND, today=None, allocator="score-v1")
    assert b1["score_version"] == "v1"
    assert t1 == 49.0  # boundary 50 + family 30... see weights: deterministic-true
    # v1.5 with no tree = v1 base minus the unavailable penalty.
    t15, b15 = candidate_score(CAND, today=None, allocator="score-v1.5")
    assert b15["tree_unavailable"] is True
    assert t15 == round(t1 + _TREE_OVERLAY_WEIGHTS["tree_unavailable"], 4)


def test_v15_with_complete_tree_adds_overlay():
    t1, _ = candidate_score(CAND, today=None, allocator="score-v1")
    t15, b15 = candidate_score(
        CAND, today=None, allocator="score-v1.5", tree_feature=COMPLETE_TREE
    )
    assert b15["tree_unavailable"] is False
    assert b15["tree_overlay_pts"] > 0
    assert t15 > t1
    assert "tree_yara" in b15["tree_signals"]
    assert "tree_python" in b15["tree_signals"]


def test_v15_truncated_probe_is_unavailable():
    truncated = {
        "complete": False,
        "truncated": True,
        "security_boundary": "unknown",
        "regex_file_type_counts": {},
        "path_count": 0,
        "reason": "truncated",
    }
    _, b15 = candidate_score(
        CAND, today=None, allocator="score-v1.5", tree_feature=truncated
    )
    assert b15["tree_unavailable"] is True
    assert b15["tree_overlay_pts"] == _TREE_OVERLAY_WEIGHTS["tree_unavailable"]


def test_v15_rank_deprioritizes_unavailable():
    other = dict(CAND)
    other["url"] = "https://github.com/other/repo2"
    ranked = rank_candidates(
        [other, CAND],
        today=None,
        allocator="score-v1.5",
        tree_features={("https://github.com/openwrt/packages", ""): COMPLETE_TREE},
    )
    # Tree-available candidate ranks above the unavailable one.
    assert ranked[0]["url"] == CAND["url"]
    assert ranked[1]["url"] == other["url"]


def test_tree_overlay_signals_frozen_shape():
    signals = _tree_overlay_signals(COMPLETE_TREE)
    assert set(signals) == set(_TREE_OVERLAY_WEIGHTS)
    assert signals["tree_regex_files_log"] > 0
    assert signals["tree_boundary_true"] == 1.0
    assert signals["tree_unavailable"] == 0.0


def test_allocator_normalization():
    assert _normalize_allocator("score-v1") == "score-v1"
    assert _normalize_allocator("v1.5") == "score-v1.5"
    assert _normalize_allocator("score-v2") == "score-v2"
    assert score_version_for_allocator("score-v1") == "v1"
    assert score_version_for_allocator("score-v1.5") == "v1.5"
    assert score_version_for_allocator("score-v2") == "v2"
    try:
        _normalize_allocator("nope")
        raise AssertionError("expected ValueError")
    except ValueError:
        pass


def test_tree_counts_never_drive_auto_no_go():
    """The overlay re-ranks; it must not change the v1 NO-GO semantics. A
    boundary-false candidate stays below a boundary-true one regardless of
    tree counts."""
    bad = dict(CAND)
    bad["url"] = "https://github.com/low/priority"
    # No tree for the bad one; rich tree for the good one.
    ranked = rank_candidates(
        [bad, CAND],
        today=None,
        allocator="score-v1.5",
        tree_features={("https://github.com/openwrt/packages", ""): COMPLETE_TREE},
    )
    assert ranked[0]["url"] == CAND["url"]
