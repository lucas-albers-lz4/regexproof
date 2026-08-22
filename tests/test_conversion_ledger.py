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


def test_wont_file_does_not_increment_existence_proofs(tmp_path: Path):
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
    upstream = tmp_path / "upstream.jsonl"
    upstream.write_text(
        json.dumps(
            {
                "id": "CU-011",
                "corpus": "openwrt_packages",
                "status": "wont_file",
                "kind": "counterexample_finder",
                "language_membership": True,
            }
        )
        + "\n",
        encoding="utf-8",
    )
    data = cl.aggregate(
        gen_dir=gen, upstream_path=upstream, security_tools=frozenset()
    )
    assert data["upstream"]["wont_file"] == 1
    assert data["funnel"]["existence_proofs"] == 0
    assert data["funnel"]["accepted_upstream"] == 0


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
    assert data["upstream"]["wont_file"] >= 1
    assert "CU-011" in {r["id"] for r in data["upstream_rows"]}
    assert "pipeline_accepted_per_gt" in data["rates"]
    assert "properties_asked_synthesized" in f
    assert f["properties_asked_distinct"] <= f["properties_asked"]
    assert f["properties_sat_distinct"] <= f["properties_sat"]
    assert f["properties_asked_synthesized"] >= 1
    assert "yara_split" in data
    assert "encodable_fraction_excluding_yara" in data["rates"]
    # --- #554 Phase A: wave hops, starvation signal, shape mix --------------
    pw = {w["wave_id"]: w for w in data["per_wave"]}
    assert set(pw) == {
        "openwrt_packages_w1",
        "openwrt_packages_w2",
        "openwrt_packages_w3",
        "openwrt_luci_w1",
    }
    for w in pw.values():
        assert w["properties_asked"] >= w["properties_sat"]
        assert w["properties_sat"] >= w["sat_ground_truthed"]
        assert 0.0 <= w["filed"] <= w["sat_ground_truthed"]
        assert w["accepted"] <= w["filed"]
        assert abs(sum(w["shape_mix"].values()) - 1.0) < 1e-9 or not w["shape_counts"]
    star = data["starvation"]
    assert star["formula"] == "backlog_weeks = demand_open / admission_per_week"
    assert star["mine_queue_cap"] > 0
    assert isinstance(star["history"], list) and star["history"]
    assert star["admission_window_end"] == star["history"][-1]["week_end"]
    assert data["queue_health"]["artifacts_present"] is False  # Phase C pending
    smc = data["shape_mix_by_corpus"]
    assert {"openwrt_packages", "openwrt_luci"} <= set(smc)
    assert (
        ROOT / "properties" / "generated" / "validatorjs-inventory.ndjson"
    ).is_file()
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


def _human_contract(**overrides):
    base = {
        "schema_version": "1",
        "site": "net/pbr/files/etc/init.d/pbr:354:is_hostname",
        "guarantee": "accepted hostname-label chars contain no semicolon",
        "input_source": "UCI policy dest",
        "trust": "config",
        "declared_domain": "hostname label alphabet, single char",
        "provenance": "human",
    }
    base.update(overrides)
    return base


def test_conversion_ndjson_increments_asked_without_batch_summary(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    row = {
        "schema_version": "1",
        "kind": "property",
        "result": "unsat",
        "regex_id": "a" * 32,
        "corpus": "openwrt_packages",
        "site": "net/pbr/files/etc/init.d/pbr:354:is_hostname",
        "domain": "hostname label alphabet, single char",
        "ground_truth_status": None,
        "contract": _human_contract(),
        "synthesized": False,
        "product_reportable": True,
    }
    (gen / "openwrt_packages_conversion.ndjson").write_text(
        json.dumps(row) + "\n", encoding="utf-8"
    )
    upstream = tmp_path / "upstream.jsonl"
    upstream.write_text("", encoding="utf-8")
    data = cl.aggregate(
        gen_dir=gen, upstream_path=upstream, security_tools=frozenset()
    )
    assert data["funnel"]["properties_asked"] == 1
    assert data["funnel"]["properties_unsat"] == 1
    assert data["funnel"]["scanner_rows"] == 0
    assert data["funnel"]["batch_summary_findings"] == 0


def test_conversion_agent_derived_and_incomplete_do_not_increment(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    agent = {
        "schema_version": "1",
        "kind": "property",
        "result": "unsat",
        "regex_id": "b" * 32,
        "corpus": "openwrt_packages",
        "site": "x:1:0",
        "domain": "ascii",
        "contract": _human_contract(provenance="agent_derived"),
        "synthesized": False,
    }
    incomplete = {
        "schema_version": "1",
        "kind": "property",
        "result": "unsat",
        "regex_id": "c" * 32,
        "corpus": "openwrt_packages",
        "site": "y:1:0",
        "domain": "ascii",
        "contract": _human_contract(guarantee=""),
        "synthesized": False,
    }
    (gen / "demo_conversion.ndjson").write_text(
        json.dumps(agent) + "\n" + json.dumps(incomplete) + "\n",
        encoding="utf-8",
    )
    upstream = tmp_path / "upstream.jsonl"
    upstream.write_text("", encoding="utf-8")
    data = cl.aggregate(
        gen_dir=gen, upstream_path=upstream, security_tools=frozenset()
    )
    assert data["funnel"]["properties_asked"] == 0


def test_conversion_version_diff_does_not_increment(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    row = {
        "schema_version": "1",
        "kind": "property",
        "result": "unsat",
        "regex_id": "d" * 32,
        "corpus": "openwrt_packages",
        "site": "z:1:0",
        "domain": "ascii",
        "contract": _human_contract(provenance="version_diff"),
        "synthesized": False,
    }
    (gen / "demo_conversion.ndjson").write_text(json.dumps(row) + "\n", encoding="utf-8")
    upstream = tmp_path / "upstream.jsonl"
    upstream.write_text("", encoding="utf-8")
    data = cl.aggregate(
        gen_dir=gen, upstream_path=upstream, security_tools=frozenset()
    )
    assert data["funnel"]["properties_asked"] == 0


# --- #554 Phase A: wave hops, starvation, shape mix -------------------------


def _wave_row(**overrides):
    row = {
        "schema_version": "1",
        "kind": "property",
        "result": "sat",
        "regex_id": "a" * 32,
        "corpus": "openwrt_packages",
        "site": "net/pbr/files/etc/init.d/pbr:354:is_hostname",
        "question_id": "hostname-no-semicolon",
        "domain": "hostname label alphabet, single char",
        "ground_truth_status": None,
        "contract": _human_contract(),
        "synthesized": False,
        "product_reportable": True,
        "wave_id": "openwrt_packages_w1",
        "idiom_bucket": "validator-charsets-and-captures",
        "shape": 1,
    }
    row.update(overrides)
    return row


def test_classify_wave_rows_hop_funnel_and_shape_mix():
    rows = [
        _wave_row(result="unsat", shape=1),
        _wave_row(
            regex_id="b" * 32,
            result="sat",
            ground_truth_status="reproduced",
            shape=3,
            kind="counterexample_finder",
        ),
        _wave_row(
            regex_id="c" * 32,
            wave_id="openwrt_packages_w2",
            idiom_bucket="image-and-ddns-json",
            ground_truth_status=None,  # SAT but not yet GT
            shape=4,
        ),
    ]
    waves = cl.classify_wave_rows(rows)
    w1 = waves[("openwrt_packages_w1", "validator-charsets-and-captures")]
    assert w1["properties_asked"] == 2
    assert w1["properties_sat"] == 1
    assert w1["sat_ground_truthed"] == 1
    assert w1["filed"] == 0 and w1["accepted"] == 0
    assert w1["shape_counts"] == {"1": 1, "3": 1}
    w2 = waves[("openwrt_packages_w2", "image-and-ddns-json")]
    assert w2["properties_asked"] == 1
    assert w2["properties_sat"] == 1
    assert w2["sat_ground_truthed"] == 0
    # shape_mix is derived in aggregate(); here only buckets are counted.


def test_join_wave_dispositions_filed_and_accepted_hops():
    rows = [
        _wave_row(result="sat", ground_truth_status="reproduced"),
        _wave_row(
            regex_id="d" * 32,
            site="net/other/files/usr/bin/oth:9:f",
            question_id="other-question",
            result="sat",
            ground_truth_status="reproduced",
            wave_id="openwrt_luci_w1",
            idiom_bucket="form-validator-alphabets",
        ),
    ]
    idx = {}
    for r, curated in zip(
        rows,
        [
            {"status": "fixed_upstream"},
            {"status": "wont_file", "filed_at": "2026-08-01"},
        ],
    ):
        idx[
            (
                cl.canonical_site(str(r["site"])),
                cl.canonical_question_id(r),
            )
        ] = dict(curated)
    waves = cl.classify_wave_rows(rows)
    cl.join_wave_dispositions(waves, rows, idx)
    w1 = waves[("openwrt_packages_w1", "validator-charsets-and-captures")]
    assert w1["filed"] == 1 and w1["accepted"] == 1  # fixed_upstream
    wl = waves[("openwrt_luci_w1", "form-validator-alphabets")]
    # wont_file + filed_at counts as filed, never accepted.
    assert wl["filed"] == 1 and wl["accepted"] == 0


def test_join_wave_dispositions_ignores_ungrounded_sat():
    rows = [_wave_row(ground_truth_status=None)]
    idx = {
        (
            cl.canonical_site(rows[0]["site"]),
            cl.canonical_question_id(rows[0]),
        ): {"status": "filed"}
    }
    waves = cl.classify_wave_rows(rows)
    cl.join_wave_dispositions(waves, rows, idx)
    w = next(iter(waves.values()))
    assert w["properties_sat"] == 1
    assert w["filed"] == 0  # GT gate: filing join only over GT-confirmed SATs


def test_corpus_key_from_url_and_closed_wave_corpora(tmp_path: Path):
    assert cl.corpus_key_from_url("https/git.openwrt.org/pkg/luci.git") == "luci"
    assert cl.corpus_key_from_url("https://x/y/Packages/") == "packages"
    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "banip_conversion_wave.md").write_text("# closed\n")
    assert cl.closed_wave_corpora(gen) == {"banip"}


def test_admission_per_week_window_is_artifact_clock():
    dates = ["2026-08-20", "2026-08-14", "2026-08-13", "2026-08-21"]
    count, end = cl.admission_per_week(dates)
    assert count == 2  # 08-20 and 08-21 inside [08-15, 08-21]
    assert end == "2026-08-21"
    assert cl.admission_per_week([]) == (0, None)


def test_starvation_metrics_stock_flow_units(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    gates = {
        "c1": ("go", "2026-08-20"),
        "c2": ("go", "2026-08-14"),
        "c3": ("no-go", "2026-08-19"),  # not an admission
        "c4": ("go", "2026-08-05"),  # outside window
    }
    for slug, (decision, d) in gates.items():
        (gen / f"{slug}_gate_decision.json").write_text(
            json.dumps({"decision": decision, "decision_date": d}) + "\n"
        )
    (gen / "c1_conversion_wave.md").write_text("# closed\n")  # c1 corpus closed
    ledger = tmp_path / "candidate-ledger.json"
    ledger.write_text(
        json.dumps(
            {
                "candidates": [
                    {"url": "https://x/c1.git", "status": "gated:go"},
                    {"url": "https://x/c1.git", "status": "gated:go"},  # dupe url
                    {"url": "https://x/c2.git", "status": "gated:go"},
                    {"url": "https://x/c3.git", "status": "new"},  # not gated:go
                ]
            }
        )
        + "\n"
    )
    queue = tmp_path / "mine-queue.json"
    queue.write_text(json.dumps({"items": list(range(7))}) + "\n")

    s = cl.starvation_metrics(gen, ledger, queue_path=queue, queue_cap=100)
    # demand: c1 deduped AND closed; c3 not gated:go → only c2 open.
    assert s["demand_open_gated_go_no_closed_wave"] == 1
    assert s["admission_per_week"] == 2  # c1 (08-20) + c2 (08-14) in [08-14, 08-20]
    assert s["admission_window_end"] == "2026-08-20"
    assert s["backlog_weeks"] == 0.5  # 1 / 2
    assert s["mine_queue_pressure"] == 0.07  # 7 items / cap 100
    assert s["alert_backlog_increasing"] is False
    assert len(s["history"]) == 1  # first run appends exactly one entry


def test_starvation_history_stable_within_week_and_alert_after_two_rises(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    (gen / "g_gate_decision.json").write_text(
        json.dumps({"decision": "go", "decision_date": "2026-08-20"}) + "\n"
    )
    ledger = tmp_path / "candidate-ledger.json"
    ledger.write_text(json.dumps({"candidates": []}) + "\n")

    prior = [
        {"week_end": "2026-08-06", "demand_open": 10, "admission_per_week": 5, "backlog_weeks": 2.0},
        {"week_end": "2026-08-13", "demand_open": 30, "admission_per_week": 5, "backlog_weeks": 6.0},
        {"week_end": "2026-08-20", "demand_open": 40, "admission_per_week": 5, "backlog_weeks": 8.0},
    ]
    s1 = cl.starvation_metrics(gen, ledger, prior_history=prior, queue_cap=100)
    # Same week_end as the last carried entry: NO duplicate append (rerun-stable),
    # and the two consecutive rises across windows trip the alert.
    assert len(s1["history"]) == 3
    assert s1["consecutive_increases"] == 2
    assert s1["alert_backlog_increasing"] is True

    falling = prior[:-1] + [
        {"week_end": "2026-08-20", "demand_open": 40, "admission_per_week": 20, "backlog_weeks": 2.0}
    ]
    s2 = cl.starvation_metrics(gen, ledger, prior_history=falling, queue_cap=100)
    assert s2["alert_backlog_increasing"] is False


def test_contract_queue_health_absent_until_phase_c(tmp_path: Path):
    gen = tmp_path / "generated"
    gen.mkdir()
    qh = cl.contract_queue_health(gen)
    assert qh["artifacts_present"] is False
    assert qh["emitted"] == 0

    qdir = tmp_path / "conversion_queue"
    qdir.mkdir()
    (qdir / "a.json").write_text(
        json.dumps({"status": "emitted", "created_at": "2026-08-19T00:00:00Z"}) + "\n"
    )
    (qdir / "b.json").write_text(json.dumps({"status": "skipped:duplicate"}) + "\n")
    qh2 = cl.contract_queue_health(gen)
    assert qh2["artifacts_present"] is True
    assert qh2["emitted"] == 1
    assert qh2["skipped"] == 1
    assert qh2["median_age_days"] is not None
