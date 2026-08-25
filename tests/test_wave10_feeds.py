"""Wave 10 (#579): feed density evidence and query share without raising the day cap."""

from __future__ import annotations

import json
from pathlib import Path

from regexproof.mine.feeds import (
    FEED_QUERIES,
    SITE_MEDIAN_FLOOR,
    TARGET_QUERY_SHARE,
    evidence_allows_share,
    query_share_n,
    select_queries,
)
from regexproof.mine.features import _QUERY_FAMILY, _query_family
from regexproof.mine.queue import DEFAULT_DAILY_CAP
from regexproof.mine.search import DEFAULT_QUERY_BUDGET, SEARCH_QUERIES

ROOT = Path(__file__).resolve().parents[1]


def test_daily_mine_cap_not_raised():
    assert DEFAULT_DAILY_CAP == 10


def test_feed_queries_have_families():
    for fam, q in FEED_QUERIES:
        assert q in _QUERY_FAMILY
        assert _QUERY_FAMILY[q] == fam
        assert _query_family(q) == fam


def test_legacy_search_query_indices_unchanged():
    assert SEARCH_QUERIES[0].startswith("filename:gitleaks.toml")
    assert len(SEARCH_QUERIES) == 20


def test_select_queries_prepends_share_when_rules_clear_floor():
    legacy = ["legacy-a", "legacy-b"]
    feeds = [f"feed-{i}" for i in range(12)]
    out = select_queries(
        legacy,
        budget=30,
        family_medians={"rules": 176.0, "validators": 11.0},
        feed_queries=feeds,
    )
    share = query_share_n(30)
    assert share == 10
    assert out[:share] == feeds[:share]
    assert "legacy-a" in out
    assert evidence_allows_share({"rules": SITE_MEDIAN_FLOOR}) is True
    assert evidence_allows_share({"rules": SITE_MEDIAN_FLOOR - 1}) is False
    blocked = select_queries(
        legacy,
        budget=30,
        family_medians={"rules": 11.0},
        feed_queries=feeds,
    )
    assert blocked[0] == "legacy-a"


def test_committed_feed_density_artifact():
    art = json.loads(
        (ROOT / "properties" / "generated" / "feed_density.json").read_text(
            encoding="utf-8"
        )
    )
    assert art["daily_cap"]["raised"] is False
    assert art["daily_cap"]["DAILY_MINE_CAP_default"] == 10
    assert art["target_query_share"] == TARGET_QUERY_SHARE
    assert art["live_query_share_applied"] is True
    assert art["feed_query_share_n"] == query_share_n(DEFAULT_QUERY_BUDGET)
    assert art["families"]["rules"]["median_regex_sites"] >= SITE_MEDIAN_FLOOR
    assert art["families"]["validators"]["median_regex_sites"] < SITE_MEDIAN_FLOOR
    assert art["osv_witness"]["primary_drain"] is False
    assert "openwrt/luci" in art["exemplars"]
    assert "validatorjs/validator.js" in art["exemplars"]
