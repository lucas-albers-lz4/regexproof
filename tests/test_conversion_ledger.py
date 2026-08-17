"""Conversion ledger: sites → property → SAT → ground-truth → upstream."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "conversion_ledger",
        ROOT / "scripts" / "conversion-ledger.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


cl = _load()


def test_is_scanner_ndjson_skips_inventory_frozen_and_triage():
    assert cl.is_scanner_ndjson(Path("gitleaks.ndjson"))
    assert not cl.is_scanner_ndjson(Path("gitleaks-inventory.ndjson"))
    assert not cl.is_scanner_ndjson(Path("gitleaks-frozen-ids.ndjson"))
    assert cl.is_scanner_ndjson(Path("triager.ndjson"))
    assert not cl.is_scanner_ndjson(Path("hippo_java_triage.ndjson"))
    assert not cl.is_scanner_ndjson(Path("java-html-sanitizer_triage.ndjson"))
    assert not cl.is_scanner_ndjson(Path("gitleaks.json"))


def test_classify_scanner_rows_funnel_buckets():
    rows = [
        {
            "kind": "property",
            "result": "planned",
            "regex_id": "inventory:rc-shape1",
            "corpus": "gitleaks",
            "site": "inventory:rc-shape1",
        },
        {
            "kind": "usage_mismatch",
            "result": "finding",
            "regex_id": "a" * 32,
            "corpus": "gitleaks",
            "site": "x:1:0",
        },
        {
            "kind": "mutation_guard",
            "result": "sat",
            "regex_id": "b" * 32,
            "corpus": "gitleaks",
            "site": "x:1:0",
            "ground_truth_status": "mutation-guard-sat-expected",
        },
        {
            "kind": "property",
            "result": "unsat",
            "regex_id": "c" * 32,
            "corpus": "validatorjs",
            "site": "a.js:1:0",
            "synthesized": True,
        },
        {
            "kind": "property",
            "result": "sat",
            "regex_id": "d" * 32,
            "corpus": "validatorjs",
            "site": "a.js:2:0",
            "synthesized": True,
            "ground_truth_status": "reproduced",
        },
        {
            "kind": "rule_diff",
            "result": "gap",
            "regex_id": "e" * 32,
            "corpus": "coreruleset",
            "site": "r.conf:1:0",
            "ground_truth_status": "PASS",
        },
    ]
    c = cl.classify_scanner_rows(rows)
    assert c["scanner_rows"] == 6
    assert c["planned_stubs"] == 1
    assert c["classification_rows"] == 1
    assert c["mutation_guards"] == 1
    assert c["properties_asked"] == 1
    assert c["properties_unsat"] == 0
    assert c["properties_sat"] == 1
    assert c["scanner_rule_diff_sat"] == 1
    assert c["sat_ground_truthed"] == 1
    assert c["sat_unique_sites"] == 1
    assert c["properties_asked_synthesized"] == 2
    assert c["properties_sat_synthesized"] == 1


def test_mutation_guard_sat_is_not_product_sat():
    rows = [
        {
            "kind": "mutation_guard",
            "result": "sat",
            "regex_id": "m" * 32,
            "corpus": "x",
            "site": "s:1:0",
            "ground_truth_status": "mutation-guard-sat-expected",
        }
    ]
    c = cl.classify_scanner_rows(rows)
    assert c["properties_asked"] == 0
    assert c["properties_sat"] == 0
    assert c["sat_ground_truthed"] == 0
    assert c["mutation_guards"] == 1


def test_aggregate_fixture_tree(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "demo_batch_summary.json").write_text(
        json.dumps(
            {
                "corpus": "demo",
                "extracted": 10,
                "encodable": 4,
                "findings": 2,
                "triage": 6,
            }
        )
        + "\n",
        encoding="utf-8",
    )
    finding = {
        "schema_version": "1",
        "kind": "property",
        "result": "sat",
        "regex_id": "f" * 32,
        "corpus": "demo",
        "site": "a.py:1:0",
        "ground_truth_status": "reproduced",
        "disclosure": "public_ok",
    }
    (gen / "demo.ndjson").write_text(json.dumps(finding) + "\n", encoding="utf-8")
    (gen / "demo-inventory.ndjson").write_text("{}\n", encoding="utf-8")
    (gen / "demo_java_triage.ndjson").write_text(
        json.dumps({"kind": "triage", "corpus": "demo", "regex_id": "t" * 32, "result": "ok"})
        + "\n",
        encoding="utf-8",
    )
    (gen / "demo-pr-dry-run.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "finding_count": 1,
                "private_first_count": 0,
                "would_open_public_upstream_issue": False,
            }
        )
        + "\n",
        encoding="utf-8",
    )
    upstream = tmp_path / "upstream.jsonl"
    upstream.write_text(
        json.dumps(
            {
                "id": "CU-001",
                "corpus": "demo",
                "status": "fixed_upstream",
                "kind": "property",
                "language_membership": True,
            }
        )
        + "\n",
        encoding="utf-8",
    )
    data = cl.aggregate(
        gen_dir=gen,
        upstream_path=upstream,
        security_tools=frozenset(),
    )
    f = data["funnel"]
    assert f["sites_extracted"] == 10
    assert f["scanner_rows"] == 1
    assert f["classification_rows"] == 0
    assert f["rule_diff_report_sat"] == 0
    assert f["sites_encodable"] == 4
    assert f["properties_asked"] == 1
    assert f["properties_sat"] == 1
    assert f["sat_ground_truthed"] == 1
    assert f["accepted_upstream"] == 1
    assert f["would_open_public_upstream"] == 0
    assert f["disclosed_public_ok"] == 1
    assert data["rates"]["encodable_fraction"] == 0.4
    md = cl.render_md(data)
    assert "sites extracted" in md
    assert "accepted upstream" in md
    assert "yara_split" in data
    assert "encodable_fraction_excluding_yara" in data["rates"]


def test_sidecar_findings_ndjson_ignored_rule_diff_report_counted(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "demo_batch_summary.json").write_text(
        json.dumps({"corpus": "demo", "extracted": 3, "encodable": 3, "findings": 0, "triage": 0})
        + "\n",
        encoding="utf-8",
    )
    (gen / "demo.ndjson").write_text("", encoding="utf-8")
    (gen / "crs_cross_engine_findings.ndjson").write_text(
        json.dumps(
            {
                "kind": "rule_diff",
                "result": "gap",
                "corpus": "coreruleset",
                "regex_id": "x",
                "site": "s:1:0",
                "ground_truth_status": "PASS",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    (gen / "crs_cross_engine_rule_diff_report.json").write_text(
        json.dumps(
            {
                "results": [
                    {
                        "kind": "rule_diff",
                        "result": "sat",
                        "ground_truth_status": "PASS",
                    }
                ]
            }
        )
        + "\n",
        encoding="utf-8",
    )
    upstream = tmp_path / "upstream.jsonl"
    upstream.write_text(
        json.dumps(
            {
                "id": "CU-001",
                "corpus": "demo",
                "status": "private_first",
                "kind": "rule_diff",
                "language_membership": True,
            }
        )
        + "\n",
        encoding="utf-8",
    )
    data = cl.aggregate(
        gen_dir=gen, upstream_path=upstream, security_tools=frozenset()
    )
    f = data["funnel"]
    assert f["properties_asked"] == 0
    assert f["properties_sat"] == 0
    assert f["rule_diff_report_sat"] == 1
    assert f["rule_diff_report_sat_gt"] == 1
    assert f["existence_proofs"] == 1

    rows = cl.load_upstream()
    ids = [r["id"] for r in rows]
    assert ids
    assert len(ids) == len(set(ids))
    for rec in rows:
        assert rec["id"].startswith("CU-")
        assert "status" in rec
        assert "language_membership" in rec


def test_batch_shape5_counts_as_properties_asked(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "demo_batch_summary.json").write_text(
        json.dumps(
            {"corpus": "demo", "extracted": 1, "encodable": 1, "findings": 0, "triage": 0}
        )
        + "\n",
        encoding="utf-8",
    )
    (gen / "demo.ndjson").write_text("", encoding="utf-8")
    (gen / "coreruleset_batch_shape5.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "coreruleset",
                "rows": [
                    {
                        "pair_id": "a",
                        "kind": "rule_diff",
                        "result": "sat",
                        "ground_truth_status": "reproduced",
                    },
                    {"pair_id": "b", "kind": "rule_diff", "result": "unsat"},
                    {
                        "pair_id": "c",
                        "kind": "rule_diff",
                        "result": "sat_fullmatch_only",
                    },
                    {"pair_id": "d", "kind": "rule_diff", "result": "timeout"},
                ],
                "summary": {},
            }
        )
        + "\n",
        encoding="utf-8",
    )
    upstream = tmp_path / "upstream.jsonl"
    upstream.write_text("", encoding="utf-8")
    data = cl.aggregate(
        gen_dir=gen, upstream_path=upstream, security_tools=frozenset({"coreruleset"})
    )
    f = data["funnel"]
    assert f["properties_asked"] == 3
    assert f["properties_sat"] == 1
    assert f["sat_ground_truthed"] == 1
    assert f["properties_unsat"] == 1
    assert f["batch_shape5_asked"] == 3
    assert data["batch_shape5"]["coreruleset_batch_shape5.json"]["sat_fullmatch_only"] == 1
    assert data["batch_shape5"]["coreruleset_batch_shape5.json"]["properties_sat_gt"] == 1


def test_ci_golden_regenerates_and_drift_checks_ledger():
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "python scripts/conversion-ledger.py" in ci
    assert "properties/generated/conversion-ledger.json" in ci
    assert "properties/generated/conversion-ledger.md" in ci
    assert "Materialize CRS version-diff trees" in ci
    assert "/tmp/crs-shape5/coreruleset-v4.27.0" in ci
    path = ROOT / "properties" / "generated" / "conversion-ledger.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["schema_version"] == "1"
    assert data["measure"] == "conversion_ledger"
    f = data["funnel"]
    assert f["sites_extracted"] >= f["sites_encodable"]
    assert f["properties_asked"] >= f["properties_sat"]
    assert f["properties_sat"] >= f["sat_ground_truthed"]
    assert f["would_open_public_upstream"] == 0
    assert f["third_party_public"] == 0
    assert f["pr_dry_run_private_first"] >= f["disclosed_private_first"]
    # Dry-run includes security-tool planned stubs; the NDJSON counter skips them.
    delta = f["pr_dry_run_private_first"] - f["disclosed_private_first"]
    assert 0 < delta <= f["planned_stubs"]
    assert f["scanner_rows"] == f["batch_summary_findings"]
    assert "crs_cross_engine_rule_diff_report.json" in data["rule_diff_reports"]
    assert data["upstream"]["false_positive"] >= 1
    assert "pipeline_accepted_per_gt" in data["rates"]
    assert "properties_asked_synthesized" in f
    assert f["properties_asked_distinct"] <= f["properties_asked"]
    assert f["properties_sat_distinct"] <= f["properties_sat"]
    assert f["properties_asked_synthesized"] >= 1
    assert "yara_split" in data
    assert "encodable_fraction_excluding_yara" in data["rates"]
    assert (ROOT / "properties" / "generated" / "validatorjs-inventory.ndjson").is_file()
    manifests = (ROOT / "regexproof" / "batch" / "manifests.py").read_text(encoding="utf-8")
    assert '"repo": "TODO"' not in manifests
    why = (ROOT / "docs" / "why.md").read_text(encoding="utf-8")
    reporting = (ROOT / "docs" / "REPORTING.md").read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    banned = "accepted upstream / SAT ground-truthed = 0.0357"
    assert banned not in why
    assert banned not in reporting
    assert "Property-contract precondition" in agents
    assert "0/10" in readme
    assert "conversion-ledger.md" in why
    assert "Two machines" in why
