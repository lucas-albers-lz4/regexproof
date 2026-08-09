"""YARA extractor tests + regex_id domain component tests."""

from __future__ import annotations

from pathlib import Path

import jsonschema
import pytest

from regexproof.extractors.yara import extract_yara
from regexproof.regex_id import DEFAULT_DOMAIN, make_regex_id
from regexproof.schemas import extractor_schema

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "yara"


def _validate(recs):
    schema = extractor_schema()
    for r in recs:
        jsonschema.validate(r, schema)


class TestYaraExtractor:
    def test_ascii_regex_extraction(self):
        src = (FIXTURES / "sample_ascii.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_ascii.yar")
        assert len(recs) >= 2
        for r in recs:
            assert r["dialect"] == "yara"
            assert r["domain"] == "ascii"
            assert r["call_kind"] == "search"
        _validate(recs)

    def test_wide_only_domain(self):
        src = (FIXTURES / "sample_wide.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_wide.yar")
        wide_only = [r for r in recs if r["domain"] == "wide" and "kernel32" in r["pattern"]]
        assert len(wide_only) == 1
        _validate(recs)

    def test_ascii_wide_emits_two_variants(self):
        src = (FIXTURES / "sample_wide.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_wide.yar")
        va_recs = [r for r in recs if "VirtualAlloc" in r["pattern"]]
        domains = {r["domain"] for r in va_recs}
        assert domains == {"ascii", "wide"}
        assert va_recs[0]["regex_id"] != va_recs[1]["regex_id"]
        _validate(recs)

    def test_nocase_flag(self):
        src = (FIXTURES / "sample_nocase.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_nocase.yar")
        for r in recs:
            assert "i" in r["flags"]
        _validate(recs)

    def test_fullword_flag(self):
        src = (FIXTURES / "sample_fullword.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_fullword.yar")
        for r in recs:
            assert "W" in r["flags"]
        _validate(recs)

    def test_unsupported_modifiers_rejected(self):
        src = (FIXTURES / "sample_unsupported.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_unsupported.yar")
        assert all(r.get("unencodable_reason", "").startswith("unsupported-modifier:") for r in recs)
        _validate(recs)

    def test_combined_modifiers(self):
        src = (FIXTURES / "sample_combined.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_combined.yar")
        assert len(recs) >= 2
        nc_wide = [r for r in recs if "RunDLL32" in r["pattern"]]
        assert len(nc_wide) >= 2
        domains = {r["domain"] for r in nc_wide}
        assert "ascii" in domains
        assert "wide" in domains
        for r in nc_wide:
            assert "i" in r["flags"]
        _validate(recs)

    def test_schema_validation(self):
        src = (FIXTURES / "sample_ascii.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_ascii.yar")
        _validate(recs)


class TestRegexIdDomain:
    def test_default_domain_unchanged(self):
        """Default domain (ascii) should produce same ID as v1 (no domain)."""
        id_default = make_regex_id(
            repo="test/repo",
            pattern="abc",
            flags="",
            dialect="py_re",
            call_kind="search",
            site="a.py:1:0",
        )
        id_ascii = make_regex_id(
            repo="test/repo",
            pattern="abc",
            flags="",
            dialect="py_re",
            call_kind="search",
            site="a.py:1:0",
            domain="ascii",
        )
        assert id_default == id_ascii

    def test_wide_domain_distinct(self):
        """Wide domain should produce different ID from ascii."""
        id_ascii = make_regex_id(
            repo="test/repo",
            pattern="abc",
            flags="",
            dialect="yara",
            call_kind="search",
            site="r.yar:1:0",
            domain="ascii",
        )
        id_wide = make_regex_id(
            repo="test/repo",
            pattern="abc",
            flags="",
            dialect="yara",
            call_kind="search",
            site="r.yar:1:0",
            domain="wide",
        )
        assert id_ascii != id_wide

    def test_domain_in_record(self):
        """Records should include the domain field."""
        src = (FIXTURES / "sample_ascii.yar").read_text()
        recs = extract_yara(src, repo="fixture/yara", file="sample_ascii.yar")
        for r in recs:
            assert "domain" in r
            assert r["domain"] in ("ascii", "wide")

    def test_invalid_domain_rejected(self):
        with pytest.raises(ValueError):
            make_regex_id(
                repo="t", pattern="x", flags="", dialect="py_re",
                call_kind="search", site="a:1:0", domain="bogus",
            )

    def test_yara_dialect_valid(self):
        """yara should be accepted as a valid dialect."""
        rid = make_regex_id(
            repo="test/repo",
            pattern="abc",
            flags="",
            dialect="yara",
            call_kind="search",
            site="r.yar:1:0",
        )
        assert len(rid) == 32
