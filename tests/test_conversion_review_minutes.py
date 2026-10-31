from __future__ import annotations

import pytest

from regexproof.mine.conversion_review_minutes import (
    ConversionReviewError,
    append_row,
    load_rows,
)


def test_distinct_questions_at_same_site_have_distinct_review_identity(tmp_path):
    log = tmp_path / "reviews.jsonl"
    common = {
        "corpus": "openwrt_packages",
        "pin": "a" * 40,
        "wave_id": "wave-one",
        "idiom_bucket": "hostname-label",
        "site": "net/pbr/files/etc/init.d/pbr:354:is_hostname",
        "outcome": "contracted",
        "active_minutes": 3.5,
        "path": log,
    }
    first = append_row(**common, rank=1, question_id="no-semicolon")
    second = append_row(**common, rank=2, question_id="no-space")

    rows = load_rows(log)
    assert len(rows) == 2
    assert {(row["site"], row["question_id"]) for row in rows} == {
        (first["site"], "no-semicolon"),
        (second["site"], "no-space"),
    }


def test_duplicate_site_question_review_is_rejected(tmp_path):
    log = tmp_path / "reviews.jsonl"
    common = {
        "corpus": "openwrt_packages",
        "pin": "a" * 40,
        "wave_id": "wave-one",
        "idiom_bucket": "hostname-label",
        "site": "net/pbr/files/etc/init.d/pbr:354:is_hostname",
        "rank": 1,
        "outcome": "contracted",
        "active_minutes": 3.5,
        "question_id": "no-semicolon",
        "path": log,
    }
    append_row(**common)
    with pytest.raises(ConversionReviewError, match="duplicate completed review"):
        append_row(**common)


def test_aggregate_sha256_corpus_pin_is_accepted(tmp_path):
    row = append_row(
        corpus="dogfood_shell",
        pin="sha256:" + "b" * 64,
        wave_id="dogfood-wave",
        idiom_bucket="normalize",
        site="openwrt-feed/luci-app-fwlive/root/usr/libexec/rpcd/fwlive:97:normalize_log_prefix",
        rank=1,
        outcome="skipped_out_of_scope",
        active_minutes=1.5,
        question_id="DF-dogfood-shell-normalize-fixpoint",
        path=tmp_path / "reviews.jsonl",
    )
    assert row["pin"] == "sha256:" + "b" * 64
