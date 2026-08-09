"""SpamAssassin .cf extractor tests (Wave 3 / #113)."""

from __future__ import annotations

from pathlib import Path

import jsonschema

from regexproof.extractors.spamassassin import extract_spamassassin
from regexproof.schemas import extractor_schema

SAMPLE_DIR = (
    Path(__file__).resolve().parents[1]
    / "batch"
    / "corpora"
    / "spamassassin"
    / "sample"
)


def _extract_all() -> list[dict]:
    recs: list[dict] = []
    for fp in sorted(SAMPLE_DIR.glob("*.cf")):
        src = fp.read_text(encoding="utf-8")
        recs.extend(
            extract_spamassassin(
                src, repo="apache/spamassassin", file=fp.name
            )
        )
    return recs


def _validate(recs):
    schema = extractor_schema()
    for r in recs:
        jsonschema.validate(r, schema)


def test_extract_sample_fixtures():
    recs = _extract_all()
    assert len(recs) >= 8
    for r in recs:
        assert r["dialect"] == "perl"
        assert r["call_kind"] == "search"
        assert r["rule_kind"] in ("body", "header", "uri", "rawbody")
        assert r["rule_name"]
    names = {r["rule_name"] for r in recs}
    assert "PLAIN_TOKEN" in names
    assert "CASE_INSENS" in names
    assert "POSIX_ALPHA" in names
    assert "K_RESET" in names
    assert "TRAILING_ALT" in names
    assert "SUBJECT_SPAM" in names
    assert "EVAL_SKIP" not in names
    case = next(r for r in recs if r["rule_name"] == "CASE_INSENS")
    assert "i" in case["flags"]
    posix = next(r for r in recs if r["rule_name"] == "POSIX_ALPHA")
    assert r"[[:alpha:]]" in posix["pattern"]
    k = next(r for r in recs if r["rule_name"] == "K_RESET")
    assert r"\K" in k["pattern"]
    _validate(recs)


def test_extract_deterministic():
    a = _extract_all()
    b = _extract_all()
    assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]
    assert [r["pattern"] for r in a] == [r["pattern"] for r in b]
    # Sorted file walk keeps order stable across runs.
    assert [r["file"] for r in a] == sorted(r["file"] for r in a)


def test_mbrace_delimiter():
    recs = _extract_all()
    mbrace = next(r for r in recs if r["rule_name"] == "MBRACE")
    assert mbrace["pattern"] == r"[[:digit:]]+"


def test_backslash_continuation_no_space():
    src = "body CONT /alpha\\\nbeta/\n"
    recs = extract_spamassassin(src, repo="apache/spamassassin", file="cont.cf")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "alphabeta"


def test_mbrace_nested_quantifier_not_truncated():
    src = "body NEST m{foo.{0,5}bar}\n"
    recs = extract_spamassassin(src, repo="apache/spamassassin", file="nest.cf")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "foo.{0,5}bar"
