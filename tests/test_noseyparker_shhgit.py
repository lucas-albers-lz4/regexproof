"""Nosey Parker + shhgit extractor / Wave-3 P3 tests (#114)."""

from __future__ import annotations

from pathlib import Path

import jsonschema
import pytest

from regexproof.compiler.re2 import compile_re2, parse_with_helper
from regexproof.compiler.xflag_strip import strip_verbose_x
from regexproof.extractors.noseyparker import extract_noseyparker
from regexproof.extractors.shhgit import extract_shhgit
from regexproof.schemas import extractor_schema

ROOT = Path(__file__).resolve().parents[1]
NP_SAMPLE = ROOT / "batch" / "corpora" / "noseyparker" / "sample"
SHH_SAMPLE = ROOT / "batch" / "corpora" / "shhgit" / "sample"


def _validate(recs):
    schema = extractor_schema()
    for r in recs:
        jsonschema.validate(r, schema)


def test_noseyparker_sample_strips_x():
    src = (NP_SAMPLE / "sample_xflag.yml").read_text(encoding="utf-8")
    recs = extract_noseyparker(src, repo="praetorian-inc/noseyparker", file="sample_xflag.yml")
    assert len(recs) >= 2
    verbose = next(r for r in recs if r.get("rule_id") == "np.sample.1")
    assert "(?x" not in verbose["pattern"]
    assert "x" not in verbose["flags"]
    assert "SAMPLE_TOKEN" in verbose["pattern"]
    assert " " not in verbose["pattern"].replace(r"\s", "")
    case = next(r for r in recs if r.get("rule_id") == "np.sample.2")
    assert "i" in case["flags"]
    assert case["dialect"] == "re2"
    assert case["call_kind"] == "search"
    _validate(recs)


def test_noseyparker_deterministic():
    src = (NP_SAMPLE / "sample_xflag.yml").read_text(encoding="utf-8")
    a = extract_noseyparker(src, repo="praetorian-inc/noseyparker", file="sample_xflag.yml")
    b = extract_noseyparker(src, repo="praetorian-inc/noseyparker", file="sample_xflag.yml")
    assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]


def test_shhgit_flags_i_and_rsa_sample():
    src = (SHH_SAMPLE / "config.yaml").read_text(encoding="utf-8")
    recs = extract_shhgit(src, repo="eth0izzle/shhgit", file="config.yaml")
    assert len(recs) >= 2
    rsa = next(r for r in recs if r["pattern"] == "^.*_rsa$")
    assert rsa["flags"] == "i"
    assert rsa["dialect"] == "re2"
    assert rsa["call_kind"] == "search"
    # match: entries are not regex sites
    assert all(r["pattern"] != ".pem" for r in recs)
    _validate(recs)

    gate = parse_with_helper(rsa["pattern"])
    if str(gate.get("helper") or "").endswith("-missing"):
        pytest.skip("go-re2 helper missing")
    from regexproof.compiler.re2 import ensure_built
    import subprocess

    binary = ensure_built()
    proc = subprocess.run(
        [str(binary), "match", rsa["pattern"], "i"],
        input="FOO_RSA",
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0


def test_shhgit_deterministic():
    src = (SHH_SAMPLE / "config.yaml").read_text(encoding="utf-8")
    a = extract_shhgit(src, repo="eth0izzle/shhgit", file="config.yaml")
    b = extract_shhgit(src, repo="eth0izzle/shhgit", file="config.yaml")
    assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]


def test_shhgit_yaml_double_quote_unescape():
    """Double-quoted YAML escapes must match yaml.Unmarshal (\\\" → \")."""
    # File bytes as in upstream config.yaml (double-quoted scalar with \\\").
    src = (
        "signatures:\n"
        "  - part: 'contents'\n"
        '    regex: "(?i)artifactory.{0,50}(\\\\\\"|\'|`)?[a-zA-Z0-9=]{112}'
        '(\\\\\\"|\'|`)?"\n'
        "    name: 'Artifactory'\n"
    )
    recs = extract_shhgit(src, repo="eth0izzle/shhgit", file="config.yaml")
    assert len(recs) == 1
    art = recs[0]
    # YAML \\\" → \" in the pattern (one backslash + quote).
    assert '(\\"|\'|`)?' in art["pattern"]
    assert r'(\\\"' not in art["pattern"]
    # Leading (?i) lifted into flags.
    assert not art["pattern"].startswith("(?i")
    assert "i" in art["flags"]


def test_shhgit_all_parts_are_search():
    """Go MatchString/Match are substring membership for every part."""
    src = """
signatures:
  - part: 'contents'
    regex: 'EAACEdEose0cBA[0-9A-Za-z]+'
    name: 'Facebook Access Token'
  - part: 'filename'
    regex: '^.*_rsa$'
    name: 'Private key'
  - part: 'path'
    regex: '\\.?ssh/config$'
    name: 'SSH config'
"""
    recs = extract_shhgit(src, repo="eth0izzle/shhgit", file="config.yaml")
    assert {r["call_kind"] for r in recs} == {"search"}


def test_noseyparker_sibling_guard_skips_top_level_pattern():
    """A top-level pattern: must not attach to the previous rule."""
    src = """
rules:
- name: First
  id: np.first.1
  pattern: 'first_token'

pattern: 'orphan_top_level'

- name: Second
  id: np.second.1
  pattern: 'second_token'
"""
    recs = extract_noseyparker(src, repo="praetorian-inc/noseyparker", file="sib.yml")
    pats = [r["pattern"] for r in recs]
    assert "orphan_top_level" not in pats
    assert "first_token" in pats
    assert "second_token" in pats


def test_mutation_unstripped_x_rejected():
    raw = "(?x) a b"
    stripped, _ = strip_verbose_x(raw)
    assert stripped == "ab"
    gate = parse_with_helper(raw)
    if not str(gate.get("helper") or "").endswith("-missing"):
        assert gate.get("ok") is False
    bad = compile_re2(raw, flags="")
    # Pattern still contains (?x — go-re2 parse-error path
    assert bad.mirror is None
    assert compile_re2(stripped, flags="x").unencodable_reason == "x-flag-unstripped"


def test_wave_corpora_and_security_tool():
    from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
    from regexproof.batch.runner import CORPUS_MANIFESTS, WAVE_CORPORA

    assert "noseyparker" in WAVE_CORPORA
    assert "shhgit" in WAVE_CORPORA
    assert "noseyparker" in SECURITY_TOOL_CORPORA
    assert "shhgit" in SECURITY_TOOL_CORPORA
    assert CORPUS_MANIFESTS["noseyparker"]["extractor"] == "noseyparker"
    assert CORPUS_MANIFESTS["shhgit"]["extractor"] == "shhgit"
