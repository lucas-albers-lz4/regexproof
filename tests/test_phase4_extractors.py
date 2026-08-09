"""Phase 4 full-scale extractor tests (TDD for #99).

Tests: pcre2 full-format, re2 upstream, cpython combined, busybox full.
Each extractor must: never crash on malformed input, bucket parse issues,
produce deterministic output.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from regexproof.extractors.busybox_tests import extract_busybox_tests
from regexproof.extractors.cpython_re_tests import (
    extract_cpython_combined,
    extract_cpython_re_tests,
    extract_cpython_test_re,
)
from regexproof.extractors.pcre2_testdata import extract_pcre2_testdata
from regexproof.extractors.re2_testdata import extract_re2_testdata

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


# ---------- pcre2_testdata ----------


class TestPcre2FullFormat:
    @pytest.fixture()
    def recs(self):
        src = (FIXTURES / "pcre2_testdata" / "full_format.txt").read_text(
            encoding="utf-8"
        )
        return extract_pcre2_testdata(
            src, repo="fixture/pcre2", file="full_format.txt"
        )

    def test_extracts_slash_delimited(self, recs):
        pats = [r["pattern"] for r in recs]
        assert "abc" in pats

    def test_extracts_flags(self, recs):
        flagged = [r for r in recs if r["pattern"] == "[a-z]+"]
        assert flagged and flagged[0]["flags"] == "i"

    def test_non_slash_delimiter(self, recs):
        pats = [r["pattern"] for r in recs]
        assert "foo|bar" in pats

    def test_hash_delimiter(self, recs):
        pats = [r["pattern"] for r in recs]
        assert "hello" in pats

    def test_modifier_list(self, recs):
        case_recs = [r for r in recs if r["pattern"] == "case_test"]
        assert case_recs
        assert "i" in case_recs[0]["flags"]
        assert "m" in case_recs[0]["flags"]

    def test_multi_line_continuation(self, recs):
        multi = [r for r in recs if "multi" in r["pattern"] and "line" in r["pattern"]]
        assert len(multi) >= 1

    def test_command_lines_skipped(self, recs):
        pats = [r["pattern"] for r in recs]
        assert not any("perltest" in p for p in pats)

    def test_escaped_delimiter(self, recs):
        esc = [r for r in recs if "foo" in r["pattern"] and "bar" in r["pattern"]]
        assert len(esc) >= 1

    def test_all_records_have_dialect(self, recs):
        assert all(r["dialect"] == "pcre" for r in recs)

    def test_parse_stats_bucketed(self, recs):
        if recs:
            stats = recs[0].get("_parse_stats", {})
            assert "a_parsed" in stats
            assert "b_skipped" in stats
            assert "c_errors" in stats

    def test_deterministic(self):
        src = (FIXTURES / "pcre2_testdata" / "full_format.txt").read_text(
            encoding="utf-8"
        )
        a = extract_pcre2_testdata(src, repo="r", file="f")
        b = extract_pcre2_testdata(src, repo="r", file="f")
        assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]

    def test_angle_bracket_delimiter(self, recs):
        angle = [r for r in recs if r["pattern"] == "anchored"]
        assert len(angle) >= 1

    def test_imsx_flags(self, recs):
        flagged = [r for r in recs if r["pattern"] == "\\d+"]
        assert flagged
        assert set(flagged[0]["flags"]) == {"i", "m", "s", "x"}


class TestPcre2NeverCrash:
    @pytest.mark.parametrize(
        "src",
        [
            "",
            "garbage\nmore garbage",
            "/unclosed",
            "/\\/\\/\\/",
            "///",
            "\x00\x01\x02",
            "#only commands\n#more commands",
            "!unclosed exclamation",
        ],
    )
    def test_no_crash(self, src):
        recs = extract_pcre2_testdata(src, repo="test", file="bad.txt")
        assert isinstance(recs, list)


class TestPcre2SampleCompat:
    def test_existing_sample(self):
        src = (
            ROOT / "batch" / "corpora" / "pcre2_testdata" / "sample" / "testinput_sample"
        ).read_text(encoding="utf-8")
        recs = extract_pcre2_testdata(src, repo="fixture/pcre2", file="testinput_sample")
        assert len(recs) >= 1
        assert all(r["dialect"] == "pcre" for r in recs)


# ---------- re2_testdata ----------


class TestRe2Upstream:
    @pytest.fixture()
    def recs(self):
        src = (FIXTURES / "re2_testdata" / "upstream_format.txt").read_text(
            encoding="utf-8"
        )
        return extract_re2_testdata(
            src, repo="fixture/re2", file="upstream_format.txt"
        )

    def test_extracts_extended(self, recs):
        pats = [r["pattern"] for r in recs]
        assert "[a-z]+" in pats

    def test_extracts_basic(self, recs):
        pats = [r["pattern"] for r in recs]
        assert any("[0-9]" in p for p in pats)

    def test_extracts_literal(self, recs):
        pats = [r["pattern"] for r in recs]
        assert "foo.bar" in pats

    def test_skips_comments(self, recs):
        pats = [r["pattern"] for r in recs]
        assert not any("This is a comment" in p for p in pats)

    def test_skips_directives(self, recs):
        pats = [r["pattern"] for r in recs]
        assert not any(p.startswith(":") for p in pats)

    def test_all_dialect_re2(self, recs):
        assert all(r["dialect"] == "re2" for r in recs)

    def test_parse_stats(self, recs):
        if recs:
            stats = recs[0].get("_parse_stats", {})
            assert stats["a_parsed"] > 0
            assert stats["b_skipped"] > 0

    def test_deterministic(self):
        src = (FIXTURES / "re2_testdata" / "upstream_format.txt").read_text(
            encoding="utf-8"
        )
        a = extract_re2_testdata(src, repo="r", file="f")
        b = extract_re2_testdata(src, repo="r", file="f")
        assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]


class TestRe2NeverCrash:
    @pytest.mark.parametrize(
        "src",
        [
            "",
            "no tabs here",
            "#\n#\n#",
            ":\n:\n:",
            "\t\t\t",
            "E\t\t\t",
            "\x00\x01",
        ],
    )
    def test_no_crash(self, src):
        recs = extract_re2_testdata(src, repo="test", file="bad.txt")
        assert isinstance(recs, list)


# ---------- cpython_re ----------


class TestCpythonReTests:
    def test_re_tests_table(self):
        src = (ROOT / "batch" / "corpora" / "cpython_re" / "re_tests.py").read_text(
            encoding="utf-8"
        )
        recs = extract_cpython_re_tests(
            src, repo="fixture/cpython", file="re_tests.py"
        )
        assert len(recs) >= 5

    def test_test_re_ast(self):
        src = (FIXTURES / "cpython_re" / "test_re_sample.py").read_text(
            encoding="utf-8"
        )
        recs = extract_cpython_test_re(
            src, repo="fixture/cpython", file="test_re_sample.py"
        )
        assert len(recs) >= 3
        pats = [r["pattern"] for r in recs if r["pattern"]]
        assert any("\\d{3}" in p for p in pats)

    def test_combined_extraction(self):
        sources = {
            "re_tests.py": (
                ROOT / "batch" / "corpora" / "cpython_re" / "re_tests.py"
            ).read_text(encoding="utf-8"),
            "test_re_sample.py": (
                FIXTURES / "cpython_re" / "test_re_sample.py"
            ).read_text(encoding="utf-8"),
        }
        recs = extract_cpython_combined(
            sources, repo="fixture/cpython", base_path="Lib/test"
        )
        assert len(recs) > 5

    def test_parse_stats(self):
        src = (ROOT / "batch" / "corpora" / "cpython_re" / "re_tests.py").read_text(
            encoding="utf-8"
        )
        recs = extract_cpython_re_tests(
            src, repo="fixture/cpython", file="re_tests.py"
        )
        if recs:
            stats = recs[0].get("_parse_stats", {})
            assert stats["a_parsed"] > 0

    def test_deterministic(self):
        src = (ROOT / "batch" / "corpora" / "cpython_re" / "re_tests.py").read_text(
            encoding="utf-8"
        )
        a = extract_cpython_re_tests(src, repo="r", file="f")
        b = extract_cpython_re_tests(src, repo="r", file="f")
        assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]


class TestCpythonNeverCrash:
    @pytest.mark.parametrize(
        "src",
        [
            "",
            "not python at all\n{{{",
            "('unclosed tuple",
            "tests = [('bad']",
            "\x00",
        ],
    )
    def test_re_tests_no_crash(self, src):
        recs = extract_cpython_re_tests(src, repo="test", file="bad.py")
        assert isinstance(recs, list)

    @pytest.mark.parametrize(
        "src",
        [
            "",
            "not python at all",
            "import re\n# no calls",
            "def f(): pass",
        ],
    )
    def test_test_re_no_crash(self, src):
        recs = extract_cpython_test_re(src, repo="test", file="bad.py")
        assert isinstance(recs, list)


# ---------- busybox ----------


class TestBusyboxFull:
    @pytest.fixture()
    def recs(self):
        src = (FIXTURES / "busybox_tests" / "full_format.tests").read_text(
            encoding="utf-8"
        )
        return extract_busybox_tests(
            src, repo="fixture/busybox", file="full_format.tests"
        )

    def test_extracts_grep_patterns(self, recs):
        pats = [r["pattern"] for r in recs]
        assert any("hello" in p for p in pats)
        assert any("[0-9]+" in p for p in pats)

    def test_extracts_sed_patterns(self, recs):
        pats = [r["pattern"] for r in recs]
        assert any("old" in p for p in pats)

    def test_extracts_awk_patterns(self, recs):
        pats = [r["pattern"] for r in recs]
        assert any("^[0-9]+$" in p for p in pats)

    def test_extracts_expr_patterns(self, recs):
        pats = [r["pattern"] for r in recs]
        assert any("foo" in p for p in pats)

    def test_extracts_direct_grep_sed(self, recs):
        pats = [r["pattern"] for r in recs]
        assert any("direct-pattern" in p for p in pats)

    def test_all_dialect_pcre(self, recs):
        assert all(r["dialect"] == "pcre" for r in recs)

    def test_parse_stats(self, recs):
        if recs:
            stats = recs[0].get("_parse_stats", {})
            assert "a_parsed" in stats
            assert stats["a_parsed"] > 0

    def test_deterministic(self):
        src = (FIXTURES / "busybox_tests" / "full_format.tests").read_text(
            encoding="utf-8"
        )
        a = extract_busybox_tests(src, repo="r", file="f")
        b = extract_busybox_tests(src, repo="r", file="f")
        assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]


class TestBusyboxNeverCrash:
    @pytest.mark.parametrize(
        "src",
        [
            "",
            "no patterns here",
            "testing incomplete",
            'testing "a" "b"',
            "\x00\x01\x02",
            "grep\nsed\nawk",
        ],
    )
    def test_no_crash(self, src):
        recs = extract_busybox_tests(src, repo="test", file="bad.tests")
        assert isinstance(recs, list)


class TestBusyboxSampleCompat:
    def test_sample_fixture(self):
        src = (
            ROOT / "batch" / "corpora" / "busybox" / "sample" / "sample.tests"
        ).read_text(encoding="utf-8")
        recs = extract_busybox_tests(
            src, repo="fixture/busybox", file="sample.tests"
        )
        assert len(recs) >= 2


# ---------- Budget enforcement ----------


class TestBudgetEnforcement:
    def test_budget_breach_raises(self):
        from regexproof.batch.runner import BudgetBreached, _check_budget_patterns

        with pytest.raises(BudgetBreached, match="max_patterns"):
            _check_budget_patterns(
                [{"pattern": "a"}] * 10,
                {"max_patterns": 5},
                "test_corpus",
            )

    def test_budget_within_limit(self):
        from regexproof.batch.runner import _check_budget_patterns

        _check_budget_patterns(
            [{"pattern": "a"}] * 5,
            {"max_patterns": 10},
            "test_corpus",
        )

    def test_budget_breach_has_fields(self):
        from regexproof.batch.runner import BudgetBreached

        exc = BudgetBreached("corp", "max_patterns", 5, 10)
        assert exc.corpus == "corp"
        assert exc.field == "max_patterns"
        assert exc.limit == 5
        assert exc.actual == 10

    def test_wave_corpora_set(self):
        from regexproof.batch.runner import WAVE_CORPORA

        assert "pcre2_testdata" in WAVE_CORPORA
        assert "re2_testdata" in WAVE_CORPORA
        assert "cpython_re" in WAVE_CORPORA
        assert "busybox" in WAVE_CORPORA

    def test_budget_fields_in_manifests(self):
        from regexproof.batch.runner import CORPUS_MANIFESTS, WAVE_CORPORA

        for name in sorted(WAVE_CORPORA):
            if name not in CORPUS_MANIFESTS:
                continue
            budget = CORPUS_MANIFESTS[name].get("budget", {})
            assert "max_patterns" in budget, f"{name} missing max_patterns"
            assert "max_wall_s" in budget, f"{name} missing max_wall_s"
            assert "max_mem_mb" in budget, f"{name} missing max_mem_mb"
            assert "max_disk_mb" in budget, f"{name} missing max_disk_mb"
