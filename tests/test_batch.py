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


def test_intent_no_substring_false_positive_on_curl():
    hits = detect_intent_mismatches(
        [
            {
                "regex_id": "c" * 32,
                "pattern": ".*",
                "context_snippet": "curl-auth-header",
                "file": "gitleaks.toml",
                "site": "x:1:0",
                "name": "curl-auth-header",
                "corpus_slug": "gitleaks",
            }
        ]
    )
    assert hits == []


def test_markdown_section_headers_unique(tmp_path: Path):
    from regexproof.batch.report import write_markdown

    findings = [
        {
            "regex_id": "d" * 32,
            "kind": "intent_mismatch",
            "result": "finding",
            "site": "a:1:0",
            "pattern": ".*",
            "ground_truth_status": "N/A",
            "disclosure": None,
            "detail": {"keyword": "email"},
        },
        {
            "regex_id": "d" * 32,
            "kind": "intent_mismatch",
            "result": "finding",
            "site": "a:1:0",
            "pattern": ".*",
            "ground_truth_status": "N/A",
            "disclosure": None,
            "detail": {"keyword": "url"},
        },
    ]
    path = tmp_path / "out.md"
    write_markdown(path, corpus="t", findings=findings)
    text = path.read_text()
    assert "ground_truth_status: \"N/A\"" in text or 'ground_truth_status: "N/A"' in text


def test_markdown_emits_contracted_finding_fields(tmp_path: Path):
    from regexproof.batch.report import write_markdown

    findings = [
        {
            "schema_version": "1",
            "regex_id": "a" * 32,
            "kind": "rule_diff",
            "corpus": "gitleaks",
            "dialect": "re2",
            "call_kind": "search",
            "shape": 5,
            "result": "sat",
            "family": "RD-example",
            "domain": "ascii",
            "wall_ms": 12.5,
            "ground_truth_status": "reproduced",
            "engine_versions": {"python": "3.12.0", "z3": "5.0.0"},
            "disclosure": "private_first",
            "site": "x.toml:1:0",
            "pattern": "AKIA[0-9A-Z]{16}",
            "detail": {},
        }
    ]
    path = tmp_path / "gitleaks_batch.md"
    write_markdown(path, corpus="gitleaks", findings=findings)
    text = path.read_text()
    assert path.name.endswith("_batch.md")
    for key in (
        "regex_id:",
        "dialect: re2",
        "call_kind: search",
        "shape: 5",
        "result: sat",
        "family: RD-example",
        "domain: ascii",
        "wall_ms: 12.5",
        "ground_truth_status: reproduced",
        "engine_versions:",
        "disclosure: private_first",
        "site:",
        'schema_version: "1"',
    ):
        assert key in text, key
    # Must not be written as the Phase-3 shape-5 path.
    assert not (tmp_path / "gitleaks.md").exists()


def test_redaction_corpus():
    samples = json.loads((ROOT / "batch/fixtures/redaction/corpus.json").read_text())["samples"]
    for s in samples:
        red = redact_witness(s)
        assert "ghp_" not in json.dumps(red)
        assert "AKIA" not in json.dumps(red)
        twice = redact_witness(red)
        assert twice == red


def test_redact_witness_recurses_lists_and_nested_dicts():
    """fix-wave #71: nested containers must not leak secrets."""
    leaked = {
        "value": ["ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ012345"],
        "nested": {"token": "AKIAIOSFODNN7EXAMPLE"},
    }
    red = redact_witness(leaked)
    dump = json.dumps(red)
    assert "ghp_" not in dump
    assert "AKIA" not in dump
    assert red["value"][0].startswith("<redacted len=")
    assert red["nested"]["token"].startswith("<redacted len=")
    assert redact_witness(red) == red


def test_triage_timeout_kind():
    """fix-wave #71: timeout via result and/or compile_reason → kind=timeout."""
    for rec in (
        {
            "regex_id": "c" * 32,
            "encodable": False,
            "compile_reason": "timeout",
            "result": "timeout",
            "dialect": "ecma",
            "call_kind": "search",
            "site": "z:1:0",
            "pattern": "a+",
        },
        {
            "regex_id": "d" * 32,
            "encodable": False,
            "compile_reason": "timeout",
            "dialect": "pcre",
            "call_kind": "search",
            "site": "z:2:0",
            "pattern": "a+",
        },
        {
            "regex_id": "e" * 32,
            "encodable": False,
            "result": "timeout",
            "dialect": "re2",
            "call_kind": "search",
            "site": "z:3:0",
            "pattern": "a+",
        },
    ):
        rows = triage_records_from_compiled([rec])
        assert len(rows) == 1
        assert rows[0]["reason_kind"] == "timeout"
        jsonschema.validate(rows[0], triage_record_schema())


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
    assert (out / "detect-secrets_batch.md").is_file()
    assert not (out / "detect-secrets.md").exists()
    triage_path = out.parent / "triage" / "detect-secrets.ndjson"
    assert triage_path.is_file()
    corpora = {json.loads(line)["corpus"] for line in ndjson}
    assert corpora == {"detect-secrets"}


def test_coreruleset_measurement(tmp_path: Path):
    report = measure_coreruleset(tmp_path)
    assert report["decision"] in ("go", "no-go")
    assert "fraction" in report
    assert (tmp_path / "coreruleset_encodable_fraction.json").is_file()


def test_json_legacy_rejected():
    from regexproof.batch.runner import main

    assert main(["--json-legacy"]) == 2
