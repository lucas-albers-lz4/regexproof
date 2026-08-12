"""P3 tests: merge-probe-draft (module + CLI) + shell vocabulary coverage."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

import regexproof.admission.merge_probe as merge_probe_mod
from regexproof.admission.constructs import count_constructs
from regexproof.admission.merge_probe import merge_draft
from regexproof.admission.vocabulary import load_vocabulary

ROOT = Path(__file__).resolve().parents[1]


def _load_cli():
    spec = importlib.util.spec_from_file_location(
        "merge_probe_draft_cli",
        ROOT / "scripts" / "merge-probe-draft.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod

FIXTURE_DRAFT = {
    "schema_version": "1",
    "corpus": "openwrt_packages",
    "candidate_url": "https://github.com/openwrt/packages",
    "corpus_pin": None,
    "probe": {
        "regex_sites": 0,
        "regex_sites_per_file": {},
        "dialect": {"posix-shell": 0},
        "flags": {},
        "predicted_buckets": {},
        "security_boundary": "unknown",
    },
    "fields_remaining": ["conditions", "rationale"],
}


def _records(*items: tuple[str, str, str]) -> list[dict]:
    """Build ndjson-shaped records: (pattern, flags, file)."""
    return [
        {"pattern": p, "flags": f, "dialect": "posix-shell",
         "shell_flags": {"syntax": "bre"}, "file": fl, "line": i + 1}
        for i, (p, f, fl) in enumerate(items)
    ]


def test_merge_populates_sites_and_buckets():
    recs = _records(
        ("[[:alpha:]]+", "", "a.sh"),   # posix-class construct
        ("foo.*bar", "i", "b.sh"),      # -i -> (?i) bucket via flag folding
        ("a|b", "", "a.sh"),
    )
    merged = merge_draft(FIXTURE_DRAFT, recs)
    assert merged["probe"]["regex_sites"] == 3
    assert merged["probe"]["regex_sites_per_file"] == {"a.sh": 2, "b.sh": 1}
    buckets = merged["probe"]["predicted_buckets"]
    assert buckets, "predicted_buckets must be non-empty for a go draft"
    assert "posix-class" in buckets  # [[:alpha:]] construct mapped
    assert "inline-flag" in buckets  # the -i record landed in the (?i) bucket


def test_grep_i_folds_to_inline_flag_bucket():
    """The AC4 canonical case: a grep -i record with flags='i' produces the
    (?i)/inline-flag bucket (walk.py flag-folding path, not dropped)."""
    recs = _records(("syn_flood", "i", "x.sh"))
    merged = merge_draft(FIXTURE_DRAFT, recs)
    assert merged["probe"]["predicted_buckets"].get("inline-flag") == 1


def test_shell_construct_keys_covered_by_vocabulary():
    """P3 AC4: the constructs count_constructs emits for shell patterns must
    be present as construct_to_bucket entries (the LOADED artifact)."""
    vocab = load_vocabulary()
    mapping = vocab["construct_to_bucket"]
    # representative shell patterns exercising every _CONSTRUCT_PATTERNS key
    samples = [
        "[[:alnum:]]+",          # posix-class
        r"\(ab\)\1",             # backref
        "a(?=b)",                # lookaround
        r"a\Kb",                 # \K
        r"a\g{x}",               # \g{
        "(?i)foo",               # (?i)
    ]
    emitted = set()
    for pat in samples:
        emitted |= set(count_constructs(pat))
    missing = {k for k in emitted if k not in mapping}
    assert not missing, f"shell-emitted constructs missing from vocabulary: {missing}"
    assert emitted, "samples must emit at least one construct"


def test_empty_buckets_preflight_exits_nonzero(tmp_path, monkeypatch):
    """The under-report rule is ENFORCED: an empty-bucket merge refuses to
    emit a go-able draft (exit 2, no output file)."""
    m = _load_cli()

    (tmp_path / "draft.json").write_text(json.dumps(FIXTURE_DRAFT))
    (tmp_path / "r.ndjson").write_text(
        json.dumps({"pattern": "x", "flags": "", "file": "x.sh", "line": 1})
        + "\n")
    monkeypatch.setattr(merge_probe_mod, "predict_buckets", lambda *a, **k: {})
    rc = m.main([str(tmp_path / "draft.json"), "--ndjson",
                 str(tmp_path / "r.ndjson"), "-o", str(tmp_path / "out.json")])
    assert rc == 2
    assert not (tmp_path / "out.json").exists()


def test_cli_emits_merged_draft(tmp_path):
    m = _load_cli()

    (tmp_path / "draft.json").write_text(json.dumps(FIXTURE_DRAFT))
    (tmp_path / "r.ndjson").write_text(
        json.dumps({"pattern": "[[:alpha:]]", "flags": "i",
                    "file": "x.sh", "line": 1}) + "\n")
    rc = m.main([str(tmp_path / "draft.json"), "--ndjson",
                 str(tmp_path / "r.ndjson"), "-o", str(tmp_path / "out.json")])
    assert rc == 0
    merged = json.loads((tmp_path / "out.json").read_text())
    assert merged["probe"]["regex_sites"] == 1
    assert merged["probe"]["predicted_buckets"]
