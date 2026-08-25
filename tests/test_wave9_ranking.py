"""Wave 9 (#578): root-dir / density / deny-list screens + offline surrogate."""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

from regexproof.mine.deny_list import build_deny_doc, slug_denied
from regexproof.mine.density import density_query, materialize_density_hits
from regexproof.mine.root_dir import root_dir_deprioritized, root_names_from_paths
from regexproof.mine.score import (
    _TREE_OVERLAY_WEIGHTS,
    candidate_score,
    rank_candidates,
    wave9_deprioritize,
)
from regexproof.mine.surrogate import SURROGATE_FEATURE_NAMES, skip_class_label
from regexproof.mine.tree import summarize_tree

ROOT = Path(__file__).resolve().parents[1]
TODAY = date(2026, 8, 22)

CAND_A = {
    "url": "https://github.com/acme/gitleaks",
    "source_query": "filename:gitleaks.toml",
    "stars": 1200,
    "pushed_date": "2026-08-01",
    "capped": False,
}
CAND_B = {
    "url": "https://github.com/acme/vendor-tests",
    "source_query": "filename:gitleaks.toml",
    "stars": 1200,
    "pushed_date": "2026-08-01",
    "capped": False,
}


def test_root_names_and_deprioritize():
    names = root_names_from_paths(["tests/foo.py", "docs/a.md", "vendor/x.js"])
    assert names == ["docs", "tests", "vendor"]
    assert root_dir_deprioritized(names) is True
    assert root_dir_deprioritized(["src", "lib", "tests"]) is False
    assert root_dir_deprioritized([]) is False
    # Root-level files are not directories (README.md is not a root dir).
    assert root_names_from_paths(["README.md", "tests/a.py", "LICENSE"]) == ["tests"]
    assert root_dir_deprioritized(root_names_from_paths(["README.md", "tests/a.py"])) is True


def test_summarize_tree_records_root_dir_names():
    result = summarize_tree(
        {
            "truncated": False,
            "tree": [
                {"path": "src/sanitizer.py", "type": "blob"},
                {"path": "README.md", "type": "blob"},
            ],
        },
        "acme/tool",
        "PIN",
    )
    assert result.root_dir_names == ("src",)
    assert result.as_dict()["root_dir_names"] == ["src"]
    assert "root_dir_names" not in summarize_tree(
        {"truncated": True, "tree": []}, "acme/tool", "PIN"
    ).as_dict()


def test_v1_totals_unchanged_with_wave9_flags():
    t, b = candidate_score(CAND_A, today=TODAY, allocator="score-v1")
    assert b["score_version"] == "v1"
    assert b["wave9_soft"]["root_dir_deprioritized"] is False
    assert b["wave9_soft"]["deny_list"] is False
    tree = {
        "complete": True,
        "truncated": False,
        "security_boundary": "deterministic-true",
        "regex_file_type_counts": {".py": 1},
        "path_count": 3,
        "root_dir_names": ["tests", "docs", "vendor"],
    }
    t2, b2 = candidate_score(
        CAND_A, today=TODAY, allocator="score-v1", tree_feature=tree
    )
    assert t2 == t
    assert b2["wave9_soft"]["root_dir_deprioritized"] is True
    historical = {
        "complete": True,
        "truncated": False,
        "security_boundary": "deterministic-true",
        "regex_file_type_counts": {".py": 1},
        "path_count": 3,
    }
    _, b_hist = candidate_score(
        CAND_A, today=TODAY, allocator="score-v1", tree_feature=historical
    )
    assert b_hist["wave9_soft"]["root_dir_deprioritized"] is False
    walked = dict(CAND_A)
    walked["regex_sites_per_file"] = {
        "tests/a.py": 1,
        "docs/b.md": 1,
        "vendor/x.js": 1,
    }
    _, b_walk = candidate_score(walked, today=TODAY, allocator="score-v1")
    assert b_walk["wave9_soft"]["root_dir_deprioritized"] is True


def test_overlay_weights_still_match_freeze():
    freeze = json.loads(
        (ROOT / "properties" / "generated" / "phase0_freeze.json").read_text(
            encoding="utf-8"
        )
    )
    canonical = json.dumps(_TREE_OVERLAY_WEIGHTS, sort_keys=True).encode("utf-8")
    assert hashlib.sha256(canonical).hexdigest() == freeze["eval"]["score_v15_overlay"]["sha256"]


def test_root_dir_is_soft_tier_not_a_drop():
    src_tree = {
        "complete": True,
        "truncated": False,
        "security_boundary": "deterministic-true",
        "regex_file_type_counts": {".py": 40},
        "path_count": 100,
        "root_dir_names": ["src", "lib"],
        "probed_pin": "",
    }
    test_tree = {
        **src_tree,
        "root_dir_names": ["tests", "docs", "vendor"],
    }
    ranked = rank_candidates(
        [CAND_B, CAND_A],
        today=TODAY,
        allocator="score-v1",
        tree_features={
            ("https://github.com/acme/gitleaks", ""): src_tree,
            ("https://github.com/acme/vendor-tests", ""): test_tree,
        },
    )
    assert [c["url"] for c in ranked] == [CAND_A["url"], CAND_B["url"]]
    assert len(ranked) == 2


def test_deny_list_never_drops_and_deprioritizes():
    slugs = {"acme/vendor-tests"}
    assert slug_denied(CAND_B["url"], slugs) is True
    ranked = rank_candidates(
        [CAND_B, CAND_A],
        today=TODAY,
        allocator="score-v1",
        deny_slugs=slugs,
    )
    assert ranked[0]["url"] == CAND_A["url"]
    assert ranked[1]["url"] == CAND_B["url"]
    t, b = candidate_score(CAND_B, today=TODAY, deny_slugs=slugs)
    assert t == candidate_score(CAND_B, today=TODAY)[0]
    assert wave9_deprioritize(b["wave9_soft"]) is True


def test_empty_code_search_is_soft_only_and_none_is_not_empty():
    ranked = rank_candidates(
        [CAND_B, CAND_A],
        today=TODAY,
        density_hits={
            "https://github.com/acme/gitleaks": 12,
            "https://github.com/acme/vendor-tests": 0,
        },
    )
    assert ranked[0]["url"] == CAND_A["url"]
    t, b = candidate_score(
        CAND_B, today=TODAY, code_search_hits=None
    )
    assert b["wave9_soft"]["code_search_empty"] is False
    _, b0 = candidate_score(CAND_B, today=TODAY, code_search_hits=0)
    assert b0["wave9_soft"]["code_search_empty"] is True
    assert t == candidate_score(CAND_B, today=TODAY)[0]


def test_density_rate_limit_omits_zero(monkeypatch):
    from regexproof.mine import density as dens
    from regexproof.mine.search import RateLimitError

    def boom(*_a, **_k):
        raise RateLimitError("rate limit")

    monkeypatch.setattr(dens, "search_code", boom)
    hits, calls = materialize_density_hits(object(), [CAND_A], budget=1)
    assert calls == 1
    key = "https://github.com/acme/gitleaks"
    assert key in hits
    assert hits[key] is None
    assert density_query("acme/gitleaks").startswith("repo:acme/gitleaks ")


def test_density_auth_degrades(monkeypatch):
    from regexproof.mine import density as dens
    from regexproof.mine.search import AuthError

    def boom(*_a, **_k):
        raise AuthError("401")

    monkeypatch.setattr(dens, "search_code", boom)
    hits, calls = materialize_density_hits(object(), [CAND_A], budget=1)
    assert calls == 1
    assert hits["https://github.com/acme/gitleaks"] is None


def test_build_deny_doc_zero_surface_only():
    doc = build_deny_doc(
        [
            {
                "candidate_url": "https://github.com/acme/empty",
                "corpus_pin": "abc123",
                "probe": {"regex_sites": 0, "pin": "abc123"},
            },
            {
                "candidate_url": "https://github.com/acme/missing-sites",
                "probe": {},
            },
            {
                "candidate_url": "https://github.com/acme/full",
                "probe": {"regex_sites": 12},
            },
            {
                "candidate_url": "https://github.com/acme/clone-fail",
                "corpus_pin": "",
                "probe": {"regex_sites": 0, "pin": ""},
                "related": {"probe_failure": "git clone/checkout error"},
            },
        ]
    )
    assert doc["hard_reject"] is False
    assert doc["not_conversion_wont_file"] is True
    assert doc["slugs"] == ["acme/empty"]


def test_surrogate_features_exclude_walked_sites():
    assert all("probe" not in n for n in SURROGATE_FEATURE_NAMES)
    assert "tree_root_deprioritized" in SURROGATE_FEATURE_NAMES
    assert skip_class_label("no-go", 50) == 1
    assert skip_class_label("no-go", 51) == 0
    assert skip_class_label("go", 0) == 0
    assert skip_class_label("no-go", None) == 0
    assert skip_class_label("no-go", 0.2) == 0


def test_v15_root_deprioritize_still_beats_unavailable():
    complete_flagged = {
        "complete": True,
        "truncated": False,
        "security_boundary": "deterministic-true",
        "regex_file_type_counts": {".py": 40, ".yara": 12},
        "path_count": 300,
        "root_dir_names": ["tests", "docs", "vendor"],
    }
    high_base = {
        "url": "https://github.com/huge/security-tool",
        "source_query": "security",
        "stars": 50000,
        "pushed_date": "2026-08-01",
        "capped": False,
    }
    ranked = rank_candidates(
        [high_base, CAND_A],
        today=TODAY,
        allocator="score-v1.5",
        tree_features={("https://github.com/acme/gitleaks", ""): complete_flagged},
    )
    assert ranked[0]["url"] == CAND_A["url"]


def test_committed_surrogate_is_offline_only():
    art = json.loads(
        (ROOT / "properties" / "generated" / "ranking_surrogate.json").read_text(
            encoding="utf-8"
        )
    )
    freeze = json.loads(
        (ROOT / "properties" / "generated" / "phase0_freeze.json").read_text(
            encoding="utf-8"
        )
    )
    assert art["live_rollout"] is False
    assert art["do_not_roll_out_score_v2"] is True
    assert art["hard_reject"] is False
    assert art["live_drain"].startswith("score-v1")
    assert art["freeze_snapshot_sha256"] == freeze["dataset"]["snapshot_sha256"]
    assert art["test_once"]["auc"] == 0.847273
    assert art["test_once"]["skip_rate"] == 0.782979
    assert art["test_once"]["threshold"] == 0.5
    deny = json.loads(
        (ROOT / "properties" / "generated" / "probe_deny_list.json").read_text(
            encoding="utf-8"
        )
    )
    assert deny["hard_reject"] is False
    assert deny["not_conversion_wont_file"] is True
    assert len(deny["slugs"]) == 99
