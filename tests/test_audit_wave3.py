"""Wave 3 audit fixes — fail-closed helpers, size skip, untimed subprocess (#171–#177)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

from regexproof.compiler.base import helper_gate_missing
from regexproof.fuzz.adapters import reject_untimed_subprocess_usage


def test_helper_gate_missing_shape():
    gate = helper_gate_missing("go-re2")
    assert gate == {
        "ok": False,
        "helper": "go-re2-missing",
        "error": "go-re2 helper unavailable",
    }


def test_re2_parse_fail_closed_when_helper_unavailable(monkeypatch):
    from regexproof.compiler import re2 as re2_mod

    def boom():
        raise FileNotFoundError("go")

    monkeypatch.setattr(re2_mod, "ensure_built", boom)
    gate = re2_mod.parse_with_helper("a+")
    assert gate.get("ok") is False
    assert gate.get("helper") == "go-re2-missing"
    cr = re2_mod.compile_re2("a+")
    assert cr.mirror is None
    assert cr.unencodable_reason == "helper-unavailable"


def test_ecma_parse_fail_closed_when_node_missing(monkeypatch):
    from regexproof.compiler import ecma as ecma_mod

    def raise_fnf(*_a, **_k):
        raise FileNotFoundError("node")

    monkeypatch.setattr(ecma_mod.subprocess, "run", raise_fnf)
    gate = ecma_mod._run_regexpp("a+", "")
    assert gate.get("ok") is False
    assert gate.get("helper") == "node-missing"
    cr = ecma_mod.compile_ecma("a+")
    assert cr.mirror is None
    assert cr.unencodable_reason == "helper-unavailable"


def test_ecma_timeout_maps_to_unencodable(monkeypatch):
    from regexproof.compiler import ecma as ecma_mod

    def raise_to(*_a, **_k):
        raise ecma_mod.subprocess.TimeoutExpired(cmd="node", timeout=30)

    monkeypatch.setattr(ecma_mod.subprocess, "run", raise_to)
    gate = ecma_mod._run_regexpp("a+", "")
    assert gate.get("ok") is False
    assert gate.get("unencodable_reason") == "timeout"
    cr = ecma_mod.compile_ecma("a+")
    assert cr.unencodable_reason == "timeout"


def test_read_capped_skips_oversized(tmp_path):
    """#365: non-glob extract paths must honor MAX_FILE_BYTES."""
    from regexproof.batch.extract import MAX_FILE_BYTES, _read_capped

    small = tmp_path / "ok.yml"
    small.write_text("id: x\nregex: a+\n", encoding="utf-8")
    big = tmp_path / "huge.yml"
    big.write_bytes(b"x" * (MAX_FILE_BYTES + 1))
    meta: dict = {}
    assert _read_capped(small, meta) is not None
    assert _read_capped(big, meta) is None
    assert meta["skipped_oversized"] == 1


def test_read_capped_raises_on_missing(tmp_path):
    """#365 follow-up: missing/unreadable must not look like an oversize skip."""
    from regexproof.batch.extract import _read_capped

    missing = tmp_path / "gone.yml"
    meta: dict = {}
    try:
        _read_capped(missing, meta)
        raise AssertionError("expected FileNotFoundError")
    except FileNotFoundError:
        pass
    assert meta.get("skipped_oversized") in (None, 0)


def test_test262_tree_skips_oversized(tmp_path):
    from regexproof.extractors.test262 import extract_test262_tree

    ok = tmp_path / "a.js"
    ok.write_text("var re = /abc/;\n", encoding="utf-8")
    big = tmp_path / "huge.js"
    big.write_bytes(b"x" * 2_000_001)
    _recs, stats = extract_test262_tree(
        tmp_path, expected_files=None, max_file_bytes=2_000_000
    )
    assert stats["skipped_oversized"] == 1
    assert stats["files_seen"] == 2


def test_extract_glob_skips_oversized(tmp_path):
    from regexproof.batch.runner import _MAX_FILE_BYTES, _extract_glob

    small = tmp_path / "ok.py"
    small.write_text("import re\nre.compile(r'abc')\n", encoding="utf-8")
    big = tmp_path / "huge.py"
    big.write_bytes(b"x" * (_MAX_FILE_BYTES + 1))

    meta: dict = {"repo": "test/size"}
    recs = _extract_glob(
        tmp_path,
        meta,
        glob="**/*.py",
        extract_fn=lambda src, rel: [{"pattern": "abc", "file": rel}],
    )
    assert meta["skipped_oversized"] == 1
    assert len(recs) == 1
    assert recs[0]["file"].endswith("ok.py")


def test_reject_untimed_subprocess_usage_clean_on_compilers():
    violations = reject_untimed_subprocess_usage()
    assert violations == [], violations


def test_pcre_parse_error_rejected_when_helper_present():
    """#361: PCRE2 parse-error must not be encoded into a Z3 mirror."""
    from regexproof.compiler.pcre import compile_pcre, helper_used_for_parse_and_replay

    if not helper_used_for_parse_and_replay():
        pytest.skip("pcre2 helper not available")
    cr = compile_pcre("a{2,1}")
    assert cr.encodable is False
    assert cr.unencodable_reason == "parse-error"


def test_pcre_fail_closed_when_helper_unavailable(monkeypatch):
    """#363: missing PCRE2 helper is Unencodable, not a silent encode."""
    from regexproof.compiler import pcre as pcre_mod

    monkeypatch.setattr(
        pcre_mod,
        "_helper_parse",
        lambda *_a, **_k: {
            "ok": False,
            "unencodable_reason": "pcre2-helper-unavailable",
            "helper": "none",
        },
    )
    cr = pcre_mod.compile_pcre("abc+")
    assert cr.mirror is None
    assert cr.unencodable_reason == "helper-unavailable"


def test_perl_fail_closed_when_helper_unavailable(monkeypatch):
    """#363: missing Perl helper is Unencodable, not a silent encode."""
    from regexproof.compiler import perl as perl_mod

    monkeypatch.setattr(
        perl_mod,
        "_helper_parse",
        lambda *_a, **_k: {
            "ok": False,
            "unencodable_reason": "perl-helper-unavailable",
            "helper": "none",
        },
    )
    cr = perl_mod.compile_perl("abc+")
    assert cr.mirror is None
    assert cr.unencodable_reason == "helper-unavailable"


def test_go_re2_env_must_stay_under_helpers(monkeypatch, tmp_path):
    from regexproof.compiler import re2 as re2_mod

    outside = tmp_path / "evil-bin"
    outside.write_text("#!", encoding="utf-8")
    monkeypatch.setenv("REGEXPROOF_GO_RE2", str(outside))
    with pytest.raises(ValueError, match="helpers/go-re2"):
        re2_mod._helper_bin()


def test_author_gate_output_containment(tmp_path):
    path = Path(__file__).resolve().parents[1] / "scripts" / "author-gate-decision.py"
    spec = importlib.util.spec_from_file_location("author_gate_decision", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    outside = tmp_path / "out.json"
    with pytest.raises(ValueError, match="properties/generated"):
        mod._resolve_output(outside, "demo", allow_outside=False)

    allowed = mod._resolve_output(outside, "demo", allow_outside=True)
    assert allowed == outside.resolve()
