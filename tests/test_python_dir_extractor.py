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
