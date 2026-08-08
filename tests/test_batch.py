"""Phase 5 batch: inventory, triage, intent, disclose, runner smoke."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from regexproof.batch.disclose import assert_no_auto_publication, write_pr_dry_run
from regexproof.batch.intent import detect_intent_mismatches, detect_usage_mismatches
from regexproof.batch.inventory import check_corpus_coverage, load_inventory
from regexproof.batch.report import redact_witness
from regexproof.batch.runner import measure_coreruleset, run_batch
from regexproof.batch.triage import triage_records_from_compiled, write_triage_ndjson
from regexproof.schemas import (
    question_inventory_schema,
    scanner_finding_schema,
    triage_record_schema,
)

ROOT = Path(__file__).resolve().parents[1]


def test_inventory_schema_and_coverage():
    assert check_corpus_coverage() == []
    for ctype in ("rule_corpus", "validator"):
        inv = load_inventory(ctype)
        jsonschema.validate(inv, question_inventory_schema())


def test_triage_one_to_one_and_zero_item(tmp_path: Path):
    empty = triage_records_from_compiled(
        [{"regex_id": "a" * 32, "encodable": True, "dialect": "re2", "call_kind": "search", "site": "x:1:0"}]
    )
    assert empty == []
    path = tmp_path / "empty.ndjson"
    write_triage_ndjson(path, empty)
    assert path.read_text() == ""

    compiled = [
        {
            "regex_id": "b" * 32,
            "encodable": False,
            "compile_reason": "word-boundary",
            "dialect": "re2",
            "call_kind": "search",
            "site": "y:2:0",
            "pattern": r"\ba\b",
        }
    ]
    recs = triage_records_from_compiled(compiled)
    assert len(recs) == 1
    jsonschema.validate(recs[0], triage_record_schema())


def test_intent_fixtures_both_classes():
    data = json.loads((ROOT / "batch/fixtures/intent/expected.json").read_text())
    for case in data["cases"]:
        rec = case["record"]
        if case["class"] == "usage_mismatch":
            hits = detect_usage_mismatches([rec])
        else:
            hits = detect_intent_mismatches([rec])
        assert bool(hits) == case["expect_finding"], case["id"]


def test_redaction_corpus():
    samples = json.loads((ROOT / "batch/fixtures/redaction/corpus.json").read_text())["samples"]
    for s in samples:
        red = redact_witness(s)
        assert "ghp_" not in json.dumps(red)
        assert "AKIA" not in json.dumps(red)
        twice = redact_witness(red)
        assert twice == red


def test_pr_dry_run_no_auto_publish(tmp_path: Path):
    art = write_pr_dry_run(
        tmp_path / "pr.json",
        findings=[{"disclosure": "private_first", "kind": "rule_diff"}],
        approval_path=None,
    )
    assert_no_auto_publication(art)
    assert art["publish"] is False
    assert art["would_open_public_upstream_issue"] is False


def test_batch_runner_smoke(tmp_path: Path):
    out = tmp_path / "generated"
    batch = run_batch(["detect-secrets"], out_dir=out, with_redos=False)
    assert "detect-secrets" in batch["corpora"]
    ndjson = (out / "detect-secrets.ndjson").read_text().strip().splitlines()
    assert ndjson
    for line in ndjson:
        rec = json.loads(line)
        if rec["regex_id"].startswith("inventory:"):
            continue
        jsonschema.validate(rec, scanner_finding_schema())
    assert (out / "detect-secrets-pr-dry-run.json").is_file()
    triage_path = out.parent / "triage" / "detect-secrets.ndjson"
    assert triage_path.is_file()


def test_coreruleset_measurement(tmp_path: Path):
    report = measure_coreruleset(tmp_path)
    assert report["decision"] in ("go", "no-go")
    assert "fraction" in report
    assert (tmp_path / "coreruleset_encodable_fraction.json").is_file()


def test_json_legacy_rejected():
    from regexproof.batch.runner import main

    assert main(["--json-legacy"]) == 2
