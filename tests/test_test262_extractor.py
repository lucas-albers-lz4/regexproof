"""test262 extractor + manifest wiring (Wave-2 P5)."""

from __future__ import annotations

from pathlib import Path


from regexproof.batch import runner
from regexproof.extractors.test262 import EXPECTED_REGEXP_FILES, extract_test262_tree

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "batch" / "corpora" / "test262" / "sample"


def test_sample_extracts_records():
    assert SAMPLE.is_dir()
    meta = dict(runner.CORPUS_MANIFESTS["test262"])
    meta["path"] = SAMPLE
    meta["measure_scope"] = "sample"
    recs = runner._extract("test262", meta)
    assert len(recs) >= 1
    assert all(r["dialect"] == "ecma" for r in recs)


def test_expected_file_constant():
    assert EXPECTED_REGEXP_FILES == 1879


def test_full_tree_gate(tmp_path):
    # Tiny fake tree must fail expected-file gate when wired via extract_test262_tree.
    d = tmp_path / "RegExp"
    d.mkdir()
    (d / "a.js").write_text("/foo/", encoding="utf-8")
    recs, stats = extract_test262_tree(d, expected_files=1879)
    assert stats["files_seen"] == 1
    assert stats["files_ok"] is False
    assert len(recs) >= 1


def test_manifest_in_wave_corpora():
    assert "test262" in runner.WAVE_CORPORA
    assert runner.CORPUS_MANIFESTS["test262"]["extractor"] == "test262"
