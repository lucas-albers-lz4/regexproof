"""P4 (#84): ``python_dir`` walks ``**/*.py`` like ``go_regexp`` / ``js_dir``."""

from __future__ import annotations

from pathlib import Path

from regexproof.batch.runner import CORPUS_MANIFESTS, _extract


def test_python_dir_extracts_multiple_files(tmp_path, monkeypatch):
    root = tmp_path / "plugins"
    root.mkdir()
    (root / "a.py").write_text("import re\nP = re.compile(r'abc')\n", encoding="utf-8")
    (root / "sub").mkdir()
    (root / "sub" / "b.py").write_text(
        "import re\nre.search(r'def', s)\n", encoding="utf-8"
    )
    (root / "skip.txt").write_text("re.compile(r'nope')\n", encoding="utf-8")

    meta = {
        "path": root,
        "glob": "**/*.py",
        "extractor": "python_dir",
        "repo": "test/detect-secrets",
        "dialect": "py_re",
    }
    # _extract resolves paths relative to package ROOT for site strings.
    recs = _extract("detect-secrets", meta)
    pats = sorted(r["pattern"] for r in recs if r.get("pattern"))
    assert pats == ["abc", "def"]
    assert all(r["dialect"] == "py_re" for r in recs)
    assert len(recs) == 2


def test_detect_secrets_manifest_is_python_dir():
    meta = CORPUS_MANIFESTS["detect-secrets"]
    assert meta["extractor"] == "python_dir"
    assert meta.get("corpus_pin")
    assert meta["path"].name == "plugins"


def test_python_dir_symlink_sites_are_repo_relative(tmp_path):
    """Symlink materialization must not bake absolute checkout paths into site."""
    from regexproof.batch.runner import ROOT, _extract_glob
    from regexproof.extractors.python_ast import extract_python

    real = tmp_path / "upstream" / "plugins"
    real.mkdir(parents=True)
    (real / "p.py").write_text("import re\nre.compile(r'xyz')\n", encoding="utf-8")
    link_parent = ROOT / "batch" / "corpora" / "detect-secrets"
    link = link_parent / "_test_plugins_symlink"
    if link.exists() or link.is_symlink():
        link.unlink()
    link.symlink_to(real)
    try:
        recs = _extract_glob(
            link,
            {"repo": "Yelp/detect-secrets"},
            glob="**/*.py",
            extract_fn=lambda src, rel: extract_python(
                src, repo="Yelp/detect-secrets", file=rel
            ),
        )
        assert len(recs) == 1
        site = recs[0]["site"]
        assert not site.startswith("/"), site
        assert "batch/corpora/detect-secrets/_test_plugins_symlink/" in site
    finally:
        if link.exists() or link.is_symlink():
            link.unlink()


def test_run_corpus_falls_back_to_sample_when_plugins_missing(tmp_path, monkeypatch):
    from regexproof.batch import runner as runner_mod

    meta = dict(runner_mod.CORPUS_MANIFESTS["detect-secrets"])
    missing = tmp_path / "no-plugins"
    meta["path"] = missing
    # Point sample at the committed mini pilot directory.
    sample = runner_mod.ROOT / "batch" / "corpora" / "detect-secrets" / "sample"
    assert sample.is_dir()

    calls: list[Path] = []

    real_extract = runner_mod._extract

    def wrap(corpus, m):
        calls.append(m["path"])
        return real_extract(corpus, m)

    monkeypatch.setitem(runner_mod.CORPUS_MANIFESTS, "detect-secrets", meta)
    monkeypatch.setattr(runner_mod, "_extract", wrap)
    out = tmp_path / "out"
    out.mkdir()
    # Avoid writing into properties/; monkeypatch OUT via out_dir arg.
    summary = runner_mod.run_corpus("detect-secrets", out_dir=out, emit_planned=False)
    assert calls and calls[0] == sample
    assert summary["findings"] >= 0
