"""Phase 1b extractor golden fixtures."""

from __future__ import annotations

from pathlib import Path

from regexproof.extractors.busybox_tests import extract_busybox_tests
from regexproof.extractors.cpython_re_tests import extract_cpython_re_tests
from regexproof.extractors.pcre2_testdata import extract_pcre2_testdata
from regexproof.extractors.rust_inventory import inventory_rust_regex

ROOT = Path(__file__).resolve().parents[1]


def test_pcre2_testdata_sample():
    src = (
        ROOT / "batch" / "corpora" / "pcre2_testdata" / "sample" / "testinput_sample"
    ).read_text(encoding="utf-8")
    recs = extract_pcre2_testdata(src, repo="fixture/pcre2", file="testinput_sample")
    assert len(recs) >= 1
    assert all(r["dialect"] == "pcre" for r in recs)


def test_cpython_re_tests_head():
    src = (ROOT / "batch" / "corpora" / "cpython_re" / "re_tests.py").read_text(
        encoding="utf-8"
    )
    recs = extract_cpython_re_tests(src, repo="fixture/cpython", file="re_tests.py")
    assert len(recs) >= 5


def test_busybox_tests_sample():
    src = (
        ROOT / "batch" / "corpora" / "busybox" / "sample" / "sample.tests"
    ).read_text(encoding="utf-8")
    recs = extract_busybox_tests(src, repo="fixture/busybox", file="sample.tests")
    assert len(recs) == 2


def test_rust_inventory_sample():
    root = ROOT / "batch" / "corpora" / "rust_regex" / "sample"
    report = inventory_rust_regex(root)
    assert report["scope"] == "inventory_only"
    assert report["extracted"] >= 1
