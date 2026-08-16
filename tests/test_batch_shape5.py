"""Shape-5 batch admission and search/pad SAT gate (#477)."""

from __future__ import annotations

from regexproof.rule_diff.batch_shape5 import admit_shape5_for_batch, filter_batch_pairs
from regexproof.rule_diff.search_replay import search_pad_confirms_gap


def test_sibling_family_not_admitted():
    pair = {
        "pair_kind": "sibling_family",
        "provenance": "sibling_family",
        "family_contract": {"R1": "a", "R2": "b", "provenance": "cross_engine"},
    }
    assert admit_shape5_for_batch(pair) is False


def test_version_diff_requires_family_contract():
    pair = {
        "pair_kind": "version_diff",
        "provenance": "version_diff",
        "family_contract": {"R1": "old", "R2": "new", "provenance": "version_diff"},
    }
    assert admit_shape5_for_batch(pair) is True
    pair["family_contract"] = {}
    assert admit_shape5_for_batch(pair) is False


def test_filter_drops_gitleaks_independent_spec():
    pairs = [
        {"provenance": "independent-spec", "family_contract": {"R1": "a", "R2": "b", "provenance": "human"}},
        {
            "provenance": "cross_engine",
            "family_contract": {"R1": "pcre", "R2": "re2", "provenance": "cross_engine"},
        },
    ]
    out = filter_batch_pairs(pairs)
    assert len(out) == 1
    assert out[0]["provenance"] == "cross_engine"


def test_search_pad_confirms_unanchored_gap():
    assert search_pad_confirms_gap(r"^keep-alive", r"keep-alive", "keep-alive")
    assert not search_pad_confirms_gap(r"keep-alive", r"keep-alive", "keep-alive")
