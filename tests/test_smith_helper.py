"""Smith helper (#149): schema, author, materialize paths, batch aggregate guard."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import jsonschema
import pytest

from regexproof.batch.runner import AGGREGATE_ARTIFACTS, run_batch
from regexproof.batch.smith_support import clone_dest, inflation_hits, wave_checklist
from regexproof.schemas import smith_decision_schema

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "properties" / "generated"
AUTHOR = ROOT / "scripts" / "author-smith-decision.py"


def test_committed_smith_decisions_validate():
    schema = smith_decision_schema()
    paths = sorted(GENERATED.glob("*_smith_decision.json"))
    assert paths
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        jsonschema.validate(instance=data, schema=schema)


def test_clone_dest_disambiguates_hyphen_underscore():
    a = clone_dest("https://github.com/acme/yara-rules", "yara-rules")
    b = clone_dest("https://github.com/acme/yara_rules", "yara_rules")
    assert a != b
    assert "acme" in str(a).lower()


def test_inflation_hits_locale_and_vendor():
    hits = inflation_hits(
        {
            "src/app.js": 2,
            "locale/en.ts": 40,
            "vendor/jquery.js": 9,
            "blockchain_core/qt/locale/bitcoin_en.ts": 1113,
            "src/tests/unit.py": 1,
        }
    )
    assert any("locale/en.ts" in h for h in hits)
    assert any("vendor" in h for h in hits)
    assert any("qt/locale" in h for h in hits)
    assert not any("src/tests/unit.py" == h for h in hits)


def test_author_smith_decision_requires_flag(tmp_path: Path):
    gate = {
        "schema_version": "1",
        "corpus": "example",
        "candidate_url": "https://github.com/acme/example",
        "corpus_pin": "abc",
        "decision": "go",
        "probe": {"regex_sites": 10, "dialect": {"py_re": 10}},
    }
    frac = {
        "schema_version": "1",
        "pilot": "example",
        "sample_size": 10,
        "encodable": 9,
        "fraction": 0.9,
        "dialect": "py_re",
        "corpus_pin": "abc",
    }
    gpath = tmp_path / "example_gate_decision.json"
    fpath = tmp_path / "example_encodable_fraction.json"
    gpath.write_text(json.dumps(gate), encoding="utf-8")
    fpath.write_text(json.dumps(frac), encoding="utf-8")
    out = tmp_path / "example_smith_decision.json"
    proc = subprocess.run(
        [
            sys.executable,
            str(AUTHOR),
            "--gate",
            str(gpath),
            "--fraction",
            str(fpath),
            "--decision",
            "no-go",
            "--reason",
            "human said no-go despite high fraction",
            "-o",
            str(out),
            "--allow-outside-generated",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    rec = json.loads(out.read_text(encoding="utf-8"))
    jsonschema.validate(instance=rec, schema=smith_decision_schema())
    assert rec["smith_decision"] == "no-go"
    assert rec["regex_sites"] == 10
    assert rec["sites_by_bucket"] == {"py_re": 10}
    assert rec["additional_surface_outside_probe_scope"] == {}
    assert "WAVE_CORPORA" in proc.stderr


def test_author_smith_buckets_follow_fraction_not_full_probe(tmp_path: Path):
    gate = {
        "schema_version": "1",
        "corpus": "example",
        "candidate_url": "https://github.com/acme/example",
        "corpus_pin": "abc",
        "decision": "go",
        "probe": {"regex_sites": 20, "dialect": {"yara": 15, "posix-shell": 5}},
    }
    frac = {
        "schema_version": "1",
        "pilot": "example",
        "sample_size": 15,
        "encodable": 14,
        "fraction": 0.933,
        "dialect": "yara",
        "corpus_pin": "abc",
    }
    gpath = tmp_path / "example_gate_decision.json"
    fpath = tmp_path / "example_encodable_fraction.json"
    gpath.write_text(json.dumps(gate), encoding="utf-8")
    fpath.write_text(json.dumps(frac), encoding="utf-8")
    out = tmp_path / "example_smith_decision.json"
    proc = subprocess.run(
        [
            sys.executable,
            str(AUTHOR),
            "--gate",
            str(gpath),
            "--fraction",
            str(fpath),
            "--decision",
            "go",
            "--reason",
            "yara-only measure",
            "-o",
            str(out),
            "--allow-outside-generated",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    rec = json.loads(out.read_text(encoding="utf-8"))
    assert rec["sites_by_bucket"] == {"yara": 15}
    assert rec["additional_surface_outside_probe_scope"] == {"posix-shell": 5}


def test_author_smith_decision_missing_decision_exits(tmp_path: Path):
    gate = tmp_path / "g.json"
    frac = tmp_path / "f.json"
    gate.write_text("{}", encoding="utf-8")
    frac.write_text("{}", encoding="utf-8")
    proc = subprocess.run(
        [
            sys.executable,
            str(AUTHOR),
            "--gate",
            str(gate),
            "--fraction",
            str(frac),
            "--reason",
            "x",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0


def test_safe_corpus_slug_rejects_traversal():
    from regexproof.batch.smith_support import safe_corpus_slug

    with pytest.raises(ValueError):
        safe_corpus_slug("../x")
    with pytest.raises(ValueError):
        safe_corpus_slug("a/b")
    assert safe_corpus_slug("openmed") == "openmed"


def test_guess_extractor_uses_highest_count_dialect():
    from regexproof.batch.smith_support import guess_extractor

    extractor, glob, dialect = guess_extractor({"ecma": 67, "py_re": 1287})
    assert dialect == "py_re"
    assert extractor == "python_dir"
    assert glob
    with pytest.raises(ValueError, match="no extractor mapping"):
        guess_extractor({"unknown-dialect": 3})
    text = wave_checklist("openmed")
    assert "WAVE_CORPORA" in text
    assert "detect-secrets" in text


def test_run_batch_single_corpus_skips_pilot_aggregate(tmp_path: Path, monkeypatch):
    from regexproof.batch import runner as runner_mod

    committed = (
        runner_mod.ROOT / "properties" / "generated" / "detect-secrets_gate_decision.json"
    )
    out = tmp_path / "generated"
    out.mkdir()
    (out / committed.name).write_bytes(committed.read_bytes())
    scratch = tmp_path / "plugins"
    scratch.mkdir()
    (scratch / "rules.py").write_text(
        "SECRET = re.compile(r'[A-Z0-9]{20}')\n", encoding="utf-8"
    )
    monkeypatch.setitem(runner_mod.CORPUS_MANIFESTS["detect-secrets"], "path", scratch)
    run_batch(
        ["detect-secrets"],
        out_dir=out,
        with_redos=False,
        write_pilot_aggregate=False,
    )
    for name in AGGREGATE_ARTIFACTS:
        assert not (out / name).exists()
    assert (out / "detect-secrets.ndjson").is_file()


def test_write_pilot_aggregate_rejects_single_corpus(tmp_path: Path, monkeypatch):
    from regexproof.batch import runner as runner_mod

    committed = (
        runner_mod.ROOT / "properties" / "generated" / "detect-secrets_gate_decision.json"
    )
    out = tmp_path / "generated"
    out.mkdir()
    (out / committed.name).write_bytes(committed.read_bytes())
    scratch = tmp_path / "plugins"
    scratch.mkdir()
    (scratch / "rules.py").write_text(
        "SECRET = re.compile(r'[A-Z0-9]{20}')\n", encoding="utf-8"
    )
    monkeypatch.setitem(runner_mod.CORPUS_MANIFESTS["detect-secrets"], "path", scratch)
    with pytest.raises(SystemExit, match="write_pilot_aggregate"):
        run_batch(
            ["detect-secrets"],
            out_dir=out,
            with_redos=False,
            write_pilot_aggregate=True,
        )
