"""Wave-3 Phase 5 (#116): perl_tre + go_regexp_tests + v8_mjsunit."""

from __future__ import annotations

from pathlib import Path

import pytest

from regexproof.batch.runner import (
    CORPUS_MANIFESTS,
    WAVE_CORPORA,
    _extract,
    check_admission_gates,
)
from regexproof.extractors.go_regexp import extract_go_regexp
from regexproof.extractors.go_regexp_tests import (
    EXPECTED_GO_REGEXP_TEST_FILES,
    extract_go_regexp_tests,
    extract_go_regexp_tests_tree,
)
from regexproof.extractors.perl_re_tests import (
    EXPECTED_PERL_RE_FILES,
    extract_perl_re_tests_table,
    extract_perl_re_tree,
    extract_perl_t_file,
)
from regexproof.extractors.v8_mjsunit import (
    EXPECTED_V8_MJSUNIT_FILES,
    extract_v8_mjsunit_tree,
)

ROOT = Path(__file__).resolve().parents[1]
PERL_SAMPLE = ROOT / "batch" / "corpora" / "perl_tre" / "sample"
GO_SAMPLE = ROOT / "batch" / "corpora" / "go_regexp_tests" / "sample"
V8_SAMPLE = ROOT / "batch" / "corpora" / "v8_mjsunit" / "sample"
GO_FIXTURE = ROOT / "tests" / "fixtures" / "go_regexp" / "sample_basic.go"


# ── Manifest / admission ──────────────────────────────────────────────


@pytest.mark.parametrize("name", ["perl_tre", "go_regexp_tests", "v8_mjsunit"])
def test_manifest_testdata_and_wave(name):
    assert name in CORPUS_MANIFESTS
    assert name in WAVE_CORPORA
    meta = CORPUS_MANIFESTS[name]
    assert meta["corpus_type"] == "testdata"
    budget = meta["budget"]
    assert budget["max_patterns"] > 0
    assert budget["max_wall_s"] > 0
    assert budget["max_mem_mb"] > 0
    assert budget["max_disk_mb"] > 0
    assert meta.get("expected_files")


def test_testdata_exempt_from_admission_gate(tmp_path):
    """testdata corpora must not require gate_decision artifacts."""
    assert check_admission_gates(
        ["perl_tre", "go_regexp_tests", "v8_mjsunit"], out_dir=tmp_path
    ) == []


def test_expected_file_constants():
    assert EXPECTED_PERL_RE_FILES == 81
    assert EXPECTED_GO_REGEXP_TEST_FILES == 9
    assert EXPECTED_V8_MJSUNIT_FILES == 91


# ── Perl ──────────────────────────────────────────────────────────────


class TestPerlReTests:
    def test_table_extracts_and_marks_compile_errors(self):
        src = (PERL_SAMPLE / "re_tests").read_text(encoding="utf-8")
        recs = extract_perl_re_tests_table(
            src, repo="Perl/perl5", file="t/re/re_tests"
        )
        assert len(recs) >= 3
        assert all(r["dialect"] == "perl" for r in recs)
        bad = [r for r in recs if r["pattern"] == "a[b-a]"]
        assert bad and bad[0].get("unencodable_reason") == "expected-compile-error"
        ok = [r for r in recs if r["pattern"] == "abc"]
        assert ok and not ok[0].get("unencodable_reason")
        stats = recs[0]["_parse_stats"]
        assert stats["c_errors"] == 0

    def test_t_file_qr_and_match(self):
        src = (PERL_SAMPLE / "pat_sample.t").read_text(encoding="utf-8")
        recs = extract_perl_t_file(src, repo="Perl/perl5", file="t/re/pat_sample.t")
        pats = {r["pattern"] for r in recs}
        assert "a+b?c+" in pats
        assert "d.f" in pats

    def test_unencodable_reasons_explicit(self):
        src = "qr/$foo+/\nqr''\n"
        recs = extract_perl_t_file(src, repo="r", file="x.t")
        reasons = {r.get("unencodable_reason") for r in recs}
        assert "composite-pattern" in reasons or "empty-pattern" in reasons
        for r in recs:
            if not r.get("unencodable_reason") and not r["pattern"]:
                pytest.fail("empty pattern without reason")

    def test_deterministic(self):
        src = (PERL_SAMPLE / "re_tests").read_text(encoding="utf-8")
        a = extract_perl_re_tests_table(src, repo="r", file="f")
        b = extract_perl_re_tests_table(src, repo="r", file="f")
        assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]

    def test_tree_fail_closed_count(self, tmp_path):
        d = tmp_path / "re"
        d.mkdir()
        (d / "re_tests").write_text("__END__\nabc\tabc\ty\t-\t-\n", encoding="utf-8")
        recs, stats = extract_perl_re_tree(d, expected_files=81)
        assert stats["files_seen"] == 1
        assert stats["files_ok"] is False
        assert len(recs) >= 1

    def test_tree_missing_root(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="missing"):
            extract_perl_re_tree(tmp_path / "nope")

    def test_sample_extract_via_runner(self):
        meta = dict(CORPUS_MANIFESTS["perl_tre"])
        meta["path"] = PERL_SAMPLE
        meta["measure_scope"] = "sample"
        recs = _extract("perl_tre", meta)
        assert len(recs) >= 3


# ── Go ────────────────────────────────────────────────────────────────


class TestGoRegexpTests:
    def test_sample_mustcompile_and_tables(self):
        src = (GO_SAMPLE / "sample_test.go").read_text(encoding="utf-8")
        recs = extract_go_regexp_tests(
            src, repo="golang/go", file="src/regexp/sample_test.go"
        )
        pats = {r["pattern"] for r in recs}
        assert "[a-z]{3,8}" in pats
        assert "^abcdefg" in pats
        assert "a*" in pats
        assert all(r["dialect"] == "re2" for r in recs)

    def test_findtest_match_text_not_compile_error(self):
        """Second-field text like 'error' must not tag expected-compile-error."""
        src = (
            "package regexp\n"
            "var findTests = []struct{ pat, text string }{\n"
            '	{`ok`, "contains error word"},\n'
            "}\n"
        )
        recs = extract_go_regexp_tests(src, repo="r", file="f.go")
        by_pat = {r["pattern"]: r for r in recs}
        assert "ok" in by_pat
        assert by_pat["ok"].get("unencodable_reason") is None

    def test_string_error_table_and_brace_in_pattern(self):
        src = (
            "package regexp\n"
            "var badRe = []stringError{\n"
            '	{`[`, "error parsing regexp"},\n'
            "}\n"
            "var goodRe = []string{\n"
            '	`a{1}`,\n'
            '	`x}y`,\n'
            "}\n"
        )
        recs = extract_go_regexp_tests(src, repo="r", file="f.go")
        by_pat = {r["pattern"]: r for r in recs}
        assert by_pat["["].get("unencodable_reason") == "expected-compile-error"
        assert "a{1}" in by_pat
        assert "x}y" in by_pat
        assert by_pat["x}y"].get("unencodable_reason") is None

    def test_does_not_break_go_regexp_fixture(self):
        src = GO_FIXTURE.read_text(encoding="utf-8")
        legacy = extract_go_regexp(src, repo="fixture", file="sample_basic.go")
        assert len(legacy) == 2
        # Extended path still sees the same MustCompile sites.
        extended = extract_go_regexp_tests(
            src, repo="fixture", file="sample_basic.go"
        )
        legacy_pats = {r["pattern"] for r in legacy}
        assert legacy_pats <= {r["pattern"] for r in extended}

    def test_deterministic(self):
        src = (GO_SAMPLE / "sample_test.go").read_text(encoding="utf-8")
        a = extract_go_regexp_tests(src, repo="r", file="f")
        b = extract_go_regexp_tests(src, repo="r", file="f")
        assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]

    def test_tree_fail_closed_count(self, tmp_path):
        d = tmp_path / "regexp"
        d.mkdir()
        (d / "x_test.go").write_text(
            'package regexp\nvar _ = MustCompile(`abc`)\n', encoding="utf-8"
        )
        recs, stats = extract_go_regexp_tests_tree(d, expected_files=9)
        assert stats["files_seen"] == 1
        assert stats["files_ok"] is False
        assert len(recs) >= 1

    def test_tree_missing_root(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="missing"):
            extract_go_regexp_tests_tree(tmp_path / "nope")

    def test_sample_extract_via_runner(self):
        meta = dict(CORPUS_MANIFESTS["go_regexp_tests"])
        meta["path"] = GO_SAMPLE
        meta["measure_scope"] = "sample"
        recs = _extract("go_regexp_tests", meta)
        assert len(recs) >= 2


# ── V8 ────────────────────────────────────────────────────────────────


class TestPerlEmbeddedNul:
    def test_nul_pattern_does_not_crash_helper(self):
        from regexproof.compiler import compile_pattern

        r = compile_pattern("a\x00b", "", "perl", "search")
        assert not r.encodable
        assert r.unencodable_reason == "embedded-nul"

    def test_helper_errors_are_named_buckets(self):
        from regexproof.compiler.perl import _classify_perl_helper_error

        assert _classify_perl_helper_error('Invalid [] range "z-a" in regex') == "bad-range"
        assert _classify_perl_helper_error("Unmatched ( in regex") == "unmatched-paren"
        assert _classify_perl_helper_error("Sequence (?^d...) not recognized") == "inline-flag"
        assert _classify_perl_helper_error("") == "malformed-pattern"


class TestMemBudgetHelpers:
    def test_check_budget_mem_nonnegative(self):
        from regexproof.batch.runner import _check_budget_mem

        assert _check_budget_mem() >= 0

    def test_address_space_cap_is_best_effort(self):
        from regexproof.batch.runner import _apply_address_space_cap

        # Must not raise even if the platform rejects setrlimit.
        _apply_address_space_cap({"max_mem_mb": 1024})


class TestV8Mjsunit:
    def test_sample_precise(self):
        meta = dict(CORPUS_MANIFESTS["v8_mjsunit"])
        meta["path"] = V8_SAMPLE
        meta["measure_scope"] = "sample"
        recs = _extract("v8_mjsunit", meta)
        pats = {r["pattern"] for r in recs}
        assert "\\s" in pats or r"\s" in pats
        assert "foo[0-9]+" in pats
        assert "phantom" not in pats
        assert "also-phantom" not in pats
        assert all(r["dialect"] == "ecma" for r in recs)

    def test_tree_fail_closed_count(self, tmp_path):
        d = tmp_path / "mjsunit"
        d.mkdir()
        (d / "regexp.js").write_text("/foo/", encoding="utf-8")
        recs, stats = extract_v8_mjsunit_tree(d, expected_files=91)
        assert stats["files_seen"] == 1
        assert stats["files_ok"] is False
        assert len(recs) >= 1

    def test_tree_missing_root(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="missing"):
            extract_v8_mjsunit_tree(tmp_path / "nope")

    def test_runner_fail_closed_missing_rules(self):
        meta = dict(CORPUS_MANIFESTS["v8_mjsunit"])
        meta["path"] = ROOT / "batch" / "corpora" / "v8_mjsunit" / "missing_rules"
        with pytest.raises((FileNotFoundError, SystemExit)):
            _extract("v8_mjsunit", meta)
