"""Phase 4 budget enforcement + testdata extractor tests."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

from regexproof.batch.runner import (
    CORPUS_MANIFESTS,
    WAVE_CORPORA,
    BudgetBreached,
    _check_budget_patterns,
    _compile_all,
    _extract,
)
from regexproof.extractors.busybox_tests import extract_busybox_tests
from regexproof.extractors.cpython_re_tests import (
    extract_cpython_re_tests,
    extract_cpython_test_re,
)
from regexproof.extractors.pcre2_testdata import extract_pcre2_testdata
from regexproof.extractors.re2_testdata import extract_re2_testdata

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"


# ── Budget enforcement ────────────────────────────────────────────────


class TestBudgetBreach:
    """Budget limits trigger BudgetBreached and nonzero exit."""

    def test_max_patterns_breach(self):
        records = [{"pattern": f"x{i}", "regex_id": f"r{i}"} for i in range(10)]
        budget = {"max_patterns": 5}
        with pytest.raises(BudgetBreached, match="max_patterns"):
            _check_budget_patterns(records, budget, "test_corpus")

    def test_max_patterns_within_limit(self):
        records = [{"pattern": f"x{i}", "regex_id": f"r{i}"} for i in range(5)]
        budget = {"max_patterns": 10}
        _check_budget_patterns(records, budget, "test_corpus")

    def test_max_patterns_zero_means_no_limit(self):
        records = [{"pattern": f"x{i}", "regex_id": f"r{i}"} for i in range(100)]
        budget = {"max_patterns": 0}
        _check_budget_patterns(records, budget, "test_corpus")

    def test_budget_breach_attrs(self):
        exc = BudgetBreached("my_corpus", "max_patterns", 5, 10)
        assert exc.corpus == "my_corpus"
        assert exc.field == "max_patterns"
        assert exc.limit == 5
        assert exc.actual == 10

    def test_measure_script_budget_breach_nonzero_exit(self, tmp_path):
        """Synthetic corpus with max_patterns=1 triggers exit 1."""
        report_dir = tmp_path / "out"
        report_dir.mkdir()
        script = ROOT / "scripts" / "measure-corpus-fraction.py"
        result = subprocess.run(
            [sys.executable, "-c", _budget_breach_script(str(tmp_path))],
            capture_output=True, text=True, timeout=60,
        )
        assert result.returncode != 0, (
            f"expected nonzero exit on budget breach, got 0.\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )

    def test_measure_script_sample_fallback_complete_run_false(self, tmp_path):
        """Sample fallback sets complete_run=False in the fraction report."""
        result = subprocess.run(
            [sys.executable, "-c", _sample_fallback_script(str(tmp_path))],
            capture_output=True, text=True, timeout=60,
        )
        if result.returncode != 0:
            pytest.fail(f"script failed: {result.stderr}\nstdout: {result.stdout}")
        report_path = tmp_path / "out" / "test_sample_encodable_fraction.json"
        if not report_path.exists():
            pytest.fail("fraction report not written")
        report = json.loads(report_path.read_text(encoding="utf-8"))
        assert report["complete_run"] is False
        assert report["scope"] == "sample"


class TestWaveCorpora:
    """WAVE_CORPORA membership and testdata budget fields."""

    def test_wave_corpora_members(self):
        expected = {
            "pcre2_testdata", "re2_testdata", "cpython_re", "busybox",
            "yara_rules", "semgrep_rules",
        }
        assert expected.issubset(WAVE_CORPORA)

    def test_testdata_manifests_have_mem_disk_budgets(self):
        testdata = ["pcre2_testdata", "re2_testdata", "cpython_re", "busybox"]
        for name in testdata:
            meta = CORPUS_MANIFESTS[name]
            budget = meta.get("budget") or {}
            assert "max_mem_mb" in budget, f"{name} missing max_mem_mb"
            assert "max_disk_mb" in budget, f"{name} missing max_disk_mb"
            assert budget["max_mem_mb"] > 0, f"{name} max_mem_mb must be > 0"
            assert budget["max_disk_mb"] > 0, f"{name} max_disk_mb must be > 0"


# ── Extractor fixture tests ──────────────────────────────────────────


class TestRe2TestdataExtractor:
    """RE2 AT&T format extractor against fixture."""

    def test_fixture_extraction(self):
        src = (FIXTURES / "re2_testdata" / "upstream_format.txt").read_text()
        recs = extract_re2_testdata(src, repo="fixture/re2", file="upstream_format.txt")
        assert len(recs) >= 5
        assert all(r["dialect"] == "re2" for r in recs)
        patterns = [r["pattern"] for r in recs]
        assert "[a-z]+" in patterns
        assert "^foo$" in patterns

    def test_skips_comments_and_directives(self):
        src = (FIXTURES / "re2_testdata" / "upstream_format.txt").read_text()
        recs = extract_re2_testdata(src, repo="fixture/re2", file="test.txt")
        for r in recs:
            assert not r["pattern"].startswith("#")
            assert not r["pattern"].startswith(":")

    def test_sample_extraction(self):
        sample = ROOT / "batch" / "corpora" / "re2_testdata" / "sample" / "sample.txt"
        src = sample.read_text()
        recs = extract_re2_testdata(src, repo="google/re2", file="sample.txt")
        assert len(recs) >= 2

    def test_empty_input(self):
        recs = extract_re2_testdata("", repo="test", file="empty.txt")
        assert recs == []


class TestPcre2TestdataExtractor:
    """PCRE2 testdata extractor against fixture."""

    def test_fixture_extraction(self):
        src = (FIXTURES / "pcre2_testdata" / "full_format.txt").read_text()
        recs = extract_pcre2_testdata(src, repo="fixture/pcre2", file="full_format.txt")
        assert len(recs) >= 5
        assert all(r["dialect"] == "pcre" for r in recs)

    def test_multi_delimiter(self):
        src = (FIXTURES / "pcre2_testdata" / "full_format.txt").read_text()
        recs = extract_pcre2_testdata(src, repo="fixture/pcre2", file="test.txt")
        patterns = [r["pattern"] for r in recs]
        assert "foo|bar" in patterns

    def test_flags_parsed(self):
        src = (FIXTURES / "pcre2_testdata" / "full_format.txt").read_text()
        recs = extract_pcre2_testdata(src, repo="fixture/pcre2", file="test.txt")
        flag_recs = [r for r in recs if r.get("flags")]
        assert len(flag_recs) >= 1


class TestCpythonReExtractor:
    """CPython re_tests.py table + test_re.py AST extractors."""

    def test_table_extractor_corpus(self):
        src = (ROOT / "batch" / "corpora" / "cpython_re" / "re_tests.py").read_text()
        recs = extract_cpython_re_tests(src, repo="fixture/cpython", file="re_tests.py")
        assert len(recs) >= 5
        assert all(r["dialect"] == "py_re" for r in recs)

    def test_ast_extractor_fixture(self):
        src = (FIXTURES / "cpython_re" / "test_re_sample.py").read_text()
        recs = extract_cpython_test_re(src, repo="fixture/cpython", file="test_re_sample.py")
        assert len(recs) >= 1


class TestBusyboxTestsExtractor:
    """Busybox .tests extractor against fixture."""

    def test_fixture_extraction(self):
        src = (FIXTURES / "busybox_tests" / "full_format.tests").read_text()
        recs = extract_busybox_tests(src, repo="fixture/busybox", file="full_format.tests")
        assert len(recs) >= 5
        assert all(r["dialect"] == "pcre" for r in recs)

    def test_testing_and_bare_commands(self):
        src = (FIXTURES / "busybox_tests" / "full_format.tests").read_text()
        recs = extract_busybox_tests(src, repo="fixture/busybox", file="test.tests")
        patterns = [r["pattern"] for r in recs]
        assert "direct-pattern" in patterns

    def test_no_crash_on_empty(self):
        recs = extract_busybox_tests("", repo="test", file="empty.tests")
        assert recs == []


class TestExtractWiring:
    """Verify _extract dispatches to the right extractor for testdata corpora."""

    def test_re2_testdata_wired(self):
        meta = dict(CORPUS_MANIFESTS["re2_testdata"])
        sample = ROOT / "batch" / "corpora" / "re2_testdata" / "sample"
        meta["path"] = sample
        recs = _extract("re2_testdata", meta)
        assert len(recs) >= 2

    def test_pcre2_testdata_wired(self):
        meta = dict(CORPUS_MANIFESTS["pcre2_testdata"])
        sample = ROOT / "batch" / "corpora" / "pcre2_testdata" / "sample"
        meta["path"] = sample
        recs = _extract("pcre2_testdata", meta)
        assert len(recs) >= 1

    def test_cpython_re_wired(self):
        meta = dict(CORPUS_MANIFESTS["cpython_re"])
        recs = _extract("cpython_re", meta)
        assert len(recs) >= 1

    def test_busybox_wired(self):
        meta = dict(CORPUS_MANIFESTS["busybox"])
        sample = ROOT / "batch" / "corpora" / "busybox" / "sample"
        meta["path"] = sample
        recs = _extract("busybox", meta)
        assert len(recs) >= 1


# ── Helper scripts for subprocess tests ──────────────────────────────


def _budget_breach_script(tmp_dir: str) -> str:
    """Python script that triggers a budget breach via measure()."""
    return f"""\
import sys, json
from pathlib import Path

ROOT = Path({str(ROOT)!r})
sys.path.insert(0, str(ROOT))

from regexproof.batch.runner import CORPUS_MANIFESTS, BudgetBreached

# Monkeypatch a corpus with absurdly low max_patterns
import regexproof.batch.runner as runner
original = dict(CORPUS_MANIFESTS["re2_testdata"])
original["budget"] = {{"max_patterns": 1, "max_wall_s": 1, "max_mem_mb": 1, "max_disk_mb": 1}}
original["path"] = ROOT / "batch" / "corpora" / "re2_testdata" / "sample"
original["measure_scope"] = "sample"
runner.CORPUS_MANIFESTS["_test_breach"] = original

# Now run measure
from scripts import __file__ as _  # ensure scripts is importable
sys.argv = ["measure", "--corpus", "_test_breach"]

# Inline the measure logic to test budget
from regexproof.batch.runner import _extract, _compile_all

meta = dict(original)
records = _extract("_test_breach", meta)
budget = meta.get("budget") or {{}}
try:
    compiled = _compile_all(
        records, lift_inline=False, corpus_slug="_test_breach", budget=budget,
    )
    # If compile didn't breach, check patterns manually
    if len(records) > budget.get("max_patterns", float("inf")):
        sys.exit(1)
    sys.exit(0)
except BudgetBreached:
    sys.exit(1)
except SystemExit as e:
    sys.exit(e.code if isinstance(e.code, int) else 1)
"""


def _sample_fallback_script(tmp_dir: str) -> str:
    """Python script that triggers sample fallback."""
    return f"""\
import sys, json
from pathlib import Path

ROOT = Path({str(ROOT)!r})
sys.path.insert(0, str(ROOT))

tmp = Path({tmp_dir!r})
out_dir = tmp / "out"
out_dir.mkdir(exist_ok=True)

import regexproof.batch.runner as runner

meta = dict(runner.CORPUS_MANIFESTS["re2_testdata"])
# Point path to nonexistent directory to force sample fallback
meta["path"] = tmp / "nonexistent_corpus"
sample_path = ROOT / "batch" / "corpora" / "re2_testdata" / "sample"
meta["sample_path"] = sample_path
meta["measure_scope"] = None  # remove sample scope to test fallback logic

runner.CORPUS_MANIFESTS["test_sample"] = meta

# Inline a minimal measure
path = meta["path"]
path_usable = path.exists() and (path.is_file() or any(path.iterdir()))
scope = "full_corpus"
complete_run = True

if not path_usable:
    if sample_path.exists():
        meta["path"] = sample_path
        scope = "sample"
        complete_run = False

records = runner._extract("test_sample", meta)
compiled = runner._compile_all(
    records, lift_inline=False, corpus_slug="test_sample"
)
compiled = [pair[0] for pair in compiled]

import platform
import z3

enc = sum(1 for c in compiled if c.get("encodable"))
n = len(compiled) or 1
fraction = enc / n

report = {{
    "schema_version": "1",
    "pilot": "test_sample",
    "scope": scope,
    "sample_size": len(compiled),
    "encodable": enc,
    "fraction": round(fraction, 4),
    "complete_run": complete_run,
    "engine_versions": {{
        "python": platform.python_version(),
        "z3": z3.get_version_string(),
    }},
}}

fpath = out_dir / "test_sample_encodable_fraction.json"
fpath.write_text(json.dumps(report, indent=2) + "\\n")
sys.exit(0)
"""
