"""Pinned materialization and wave admission for funnel #615."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import jsonschema

from regexproof.batch.manifests import CORPUS_MANIFESTS, WAVE_CORPORA
from regexproof.schemas import smith_decision_schema

ROOT = Path(__file__).resolve().parents[1]
CORPUS_ROOT = ROOT / "batch" / "corpora" / "dogfood_shell"


def test_dogfood_shell_snapshot_is_nonempty_and_wave_admitted():
    assert "dogfood_shell" in WAVE_CORPORA
    assert CORPUS_MANIFESTS["dogfood_shell"]["path"] == CORPUS_ROOT / "rules"
    assert any((CORPUS_ROOT / "rules").rglob("*.sh"))


def test_dogfood_shell_source_provenance_matches_materialized_bytes():
    pin_path = CORPUS_ROOT / "source-pins.json"
    files_path = CORPUS_ROOT / "source-files.json"
    pin_digest = hashlib.sha256(pin_path.read_bytes()).hexdigest()
    assert CORPUS_MANIFESTS["dogfood_shell"]["corpus_pin"] == f"sha256:{pin_digest}"

    pins = json.loads(pin_path.read_text(encoding="utf-8"))
    manifest = json.loads(files_path.read_text(encoding="utf-8"))
    rows = manifest["files"]
    assert manifest["materialized_files"] == len(rows) == 260
    assert {row["path"] for row in rows} == {
        p.relative_to(CORPUS_ROOT / "rules").as_posix()
        for p in (CORPUS_ROOT / "rules").rglob("*")
        if p.is_file()
    }
    for row in rows:
        repo = row["path"].split("/", 1)[0]
        assert row["source_url"] == pins["repositories"][repo]["url"]
        assert row["source_commit"] == pins["repositories"][repo]["commit"]
        data = (CORPUS_ROOT / "rules" / row["path"]).read_bytes()
        assert len(data) == row["bytes"]
        assert hashlib.sha256(data).hexdigest() == row["sha256"]

    provenance = json.loads(
        (CORPUS_ROOT / "measurement-provenance.json").read_text(encoding="utf-8")
    )
    assert provenance["source_pins_sha256"] == pin_digest
    assert provenance["source_files_sha256"] == hashlib.sha256(
        files_path.read_bytes()
    ).hexdigest()
    assert provenance["materialized_shell_files"] == len(rows)


def test_dogfood_shell_licenses_are_preserved():
    manifest = json.loads((CORPUS_ROOT / "licenses.json").read_text(encoding="utf-8"))
    for row in manifest["files"]:
        data = (CORPUS_ROOT / "licenses" / row["file"]).read_bytes()
        assert len(data) == row["bytes"]
        assert hashlib.sha256(data).hexdigest() == row["sha256"]
    assert "zero shell files" in manifest["note"]


def test_dogfood_shell_measurement_and_smith_decision_are_recorded():
    fraction = json.loads(
        (ROOT / "properties/generated/dogfood_shell_encodable_fraction.json")
        .read_text(encoding="utf-8")
    )
    assert fraction["corpus_pin"] == CORPUS_MANIFESTS["dogfood_shell"]["corpus_pin"]
    assert fraction["sample_size"] == 977
    assert fraction["encodable"] == 910
    assert fraction["fraction"] == 0.9314
    assert fraction["complete_run"] is True
    assert fraction["unclassified_parse_errors"] == 0
    assert fraction["budget_breaches"] is None
    assert fraction["decision"] == "go"
    assert fraction["scope"] == "full_corpus"
    assert fraction["reasons"]["dynamic-shell-expansion"] == 40

    inventory = [
        json.loads(line)
        for line in (ROOT / "properties/generated/dogfood_shell-inventory.ndjson")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip()
    ]
    assert len(inventory) == fraction["sample_size"]
    reasons = Counter(row.get("compile_reason") or "ok" for row in inventory)
    assert dict(sorted(reasons.items())) == fraction["reasons"]

    decision = json.loads(
        (ROOT / "properties/generated/dogfood_shell_smith_decision.json")
        .read_text(encoding="utf-8")
    )
    jsonschema.validate(instance=decision, schema=smith_decision_schema())
    assert decision["corpus_pin"] == fraction["corpus_pin"]
    assert decision["regex_sites"] == fraction["sample_size"]
    assert decision["smith_decision"] == "go"
