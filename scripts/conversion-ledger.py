#!/usr/bin/env python3
"""Aggregate scanner / rule_diff / upstream artifacts into a conversion ledger.

Heap's-law / singleton novelty saturates compiler coverage (new reject buckets,
new pattern types). This measure is the *product* funnel: sites → properties
asked → SAT → ground-truthed → disclosed → accepted upstream.

Input:
  properties/generated/*_batch_summary.json
  properties/generated/<corpus>.ndjson          (scanner findings)
  properties/generated/*-pr-dry-run.json
  properties/generated/*_rule_diff_report.json
  docs/conversion-upstream.jsonl                (human-curated last mile)
Output:
  properties/generated/conversion-ledger.{json,md}

Observational only. Regenerated in the golden CI job; drift fails the job.
Do not treat TIMEOUT / unknown as a pass. Toolkit VF-* rows in
docs/verified-findings.jsonl are out of this ledger (implementation traps,
not vulnerability counts).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

GEN_DIR = ROOT / "properties" / "generated"
UPSTREAM_PATH = ROOT / "docs" / "conversion-upstream.jsonl"
JSON_OUT = GEN_DIR / "conversion-ledger.json"
MD_OUT = GEN_DIR / "conversion-ledger.md"

SCHEMA_VERSION = "1"

PRODUCT_KINDS = frozenset(
    {"property", "counterexample_finder", "bug_demo", "rule_diff"}
)
CLASSIFICATION_KINDS = frozenset({"usage_mismatch", "intent_mismatch", "triage"})
HYGIENE_KINDS = frozenset({"mutation_guard"})
REDOS_KINDS = frozenset({"redos"})

SAT_RESULTS = frozenset({"sat", "gap"})
UNSAT_RESULTS = frozenset({"unsat"})
GT_PASS = frozenset({"reproduced", "PASS"})
RULE_DIFF_REPORT_GLOB = "*_rule_diff_report.json"
BATCH_SHAPE5_GLOB = "*_batch_shape5.json"
# Decided batch shape-5 outcomes that count as a property asked (#477).
BATCH_SHAPE5_ASKED = frozenset({"sat", "unsat", "sat_fullmatch_only"})
BATCH_SHAPE5_SAT = frozenset({"sat"})


def _load_security_tool_corpora() -> frozenset[str]:
    """Load SECURITY_TOOL_CORPORA without importing regexproof.batch (jsonschema)."""
    path = ROOT / "regexproof" / "batch" / "disclose.py"
    spec = importlib.util.spec_from_file_location("_rp_disclose", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return frozenset(mod.SECURITY_TOOL_CORPORA)


def is_scanner_ndjson(path: Path) -> bool:
    """True for batch scanner ``<corpus>.ndjson``, not inventories/probes/triage.

    Java sidecar probes are ``*_triage.ndjson`` / ``*-triage.ndjson``. Do not
    treat the substring ``triage`` as a ban — a corpus named ``triager`` is a
    valid scanner file.
    """
    name = path.name
    if not name.endswith(".ndjson"):
        return False
    stem = name[: -len(".ndjson")]
    if "-inventory" in stem or "frozen-ids" in stem:
        return False
    return not stem.endswith(("_triage", "-triage"))


def is_planned(rec: dict[str, Any]) -> bool:
    if rec.get("result") == "planned":
        return True
    rid = str(rec.get("regex_id") or "")
    return rid.startswith("inventory:")


def is_product_sat(rec: dict[str, Any]) -> bool:
    return rec.get("kind") in PRODUCT_KINDS and rec.get("result") in SAT_RESULTS


def is_ground_truthed(rec: dict[str, Any]) -> bool:
    if rec.get("ground_truth_status") in GT_PASS:
        return True
    gt = rec.get("ground_truth")
    if not isinstance(gt, dict):
        return False
    if gt.get("status") in GT_PASS:
        return True
    engines = [
        v
        for v in gt.values()
        if isinstance(v, dict) and "status" in v and "replay" in v
    ]
    return bool(engines) and all(e.get("status") in GT_PASS for e in engines)


def _ratio(num: int, den: int) -> float | None:
    if den == 0:
        return None
    return round(num / den, 6)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _iter_ndjson(path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


def load_upstream(path: Path | None = None) -> list[dict[str, Any]]:
    p = path if path is not None else UPSTREAM_PATH
    rows = _iter_ndjson(p)
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError(f"duplicate conversion-upstream id in {p}")
    return rows


def counts_as_conversion_asked(rec: dict[str, Any]) -> bool:
    """Conversion-wave rows count only when product_reportable + human.

    Kind alone would count smoke (agent_derived / incomplete contract).
    """
    from regexproof.harness.contract import product_reportable

    if rec.get("synthesized"):
        return False
    contract = rec.get("contract")
    if not isinstance(contract, dict) or str(contract.get("provenance") or "") != "human":
        return False
    return product_reportable(
        {
            "kind": rec.get("kind"),
            "domain": rec.get("domain"),
            "contract": contract,
        }
    )


# Conversion NDJSON joins asked/SAT/GT only. Do not merge scanner-inventory
# counters — those must stay equal to batch_summary findings.
_CONVERSION_FUNNEL_KEYS = (
    "properties_asked",
    "properties_asked_synthesized",
    "properties_asked_distinct",
    "properties_unsat",
    "properties_sat",
    "properties_sat_synthesized",
    "properties_sat_distinct",
    "sat_ground_truthed",
    "sat_unique_sites",
)


def classify_conversion_rows(rows: list[dict[str, Any]]) -> dict[str, int]:
    """Funnel buckets for ``*_conversion.ndjson`` (product_reportable gate)."""
    counts: Counter[str] = Counter(
        {
            "properties_asked": 0,
            "properties_asked_synthesized": 0,
            "properties_asked_distinct": 0,
            "properties_unsat": 0,
            "properties_sat": 0,
            "properties_sat_synthesized": 0,
            "properties_sat_distinct": 0,
            "sat_ground_truthed": 0,
            "sat_unique_sites": 0,
        }
    )
    sat_sites: set[tuple[str, str, str]] = set()
    asked_pairs: set[tuple[str, str]] = set()
    sat_pairs: set[tuple[str, str]] = set()
    for rec in rows:
        if not counts_as_conversion_asked(rec):
            continue
        qid = rec.get("question_id") or rec.get("name") or ""
        pair = (str(rec.get("site") or ""), str(qid))
        counts["properties_asked"] += 1
        asked_pairs.add(pair)
        result = rec.get("result")
        if result in UNSAT_RESULTS:
            counts["properties_unsat"] += 1
        elif result in SAT_RESULTS:
            counts["properties_sat"] += 1
            sat_pairs.add(pair)
            sat_sites.add(
                (
                    str(rec.get("corpus") or ""),
                    str(rec.get("regex_id") or ""),
                    str(rec.get("site") or ""),
                )
            )
            if is_ground_truthed(rec):
                counts["sat_ground_truthed"] += 1
    counts["sat_unique_sites"] = len(sat_sites)
    counts["properties_asked_distinct"] = len(asked_pairs)
    counts["properties_sat_distinct"] = len(sat_pairs)
    return dict(counts)


def scanner_ndjson_files(gen_dir: Path) -> list[Path]:
    """Batch scanner NDJSON: ``<corpus>.ndjson`` with a matching batch summary.

    Excludes inventories, frozen-id snapshots, Java-triage probes, and
    sidecar finding dumps (``crs_cross_engine_findings.ndjson``) whose SAT
    rows are counted from ``*_rule_diff_report.json`` instead.
    """
    summaries = {
        p.name[: -len("_batch_summary.json")]
        for p in gen_dir.glob("*_batch_summary.json")
        if p.name != "batch_summary.json"
    }
    out: list[Path] = []
    for path in sorted(gen_dir.glob("*.ndjson")):
        if not is_scanner_ndjson(path):
            continue
        stem = path.name[: -len(".ndjson")]
        if stem in summaries:
            out.append(path)
    # Special-case conversion-wave join: independent of a matching batch summary.
    # Do not broaden to a generic *.ndjson scan.
    for path in sorted(gen_dir.glob("*_conversion.ndjson")):
        if path not in out:
            out.append(path)
    return out


def classify_scanner_rows(
    rows: list[dict[str, Any]],
) -> dict[str, int]:
    """Count one scanner-NDJSON corpus (or a fixture list) into funnel buckets."""
    counts: Counter[str] = Counter(
        {
            "scanner_rows": 0,
            "planned_stubs": 0,
            "classification_rows": 0,
            "mutation_guards": 0,
            "redos_rows": 0,
            "other_rows": 0,
            "properties_asked": 0,
            "properties_asked_synthesized": 0,
            "properties_asked_distinct": 0,
            "properties_unsat": 0,
            "properties_sat": 0,
            "properties_sat_synthesized": 0,
            "properties_sat_distinct": 0,
            "scanner_rule_diff_sat": 0,
            "sat_ground_truthed": 0,
        }
    )
    sat_sites: set[tuple[str, str, str]] = set()
    asked_pairs: set[tuple[str, str]] = set()
    sat_pairs: set[tuple[str, str]] = set()
    for rec in rows:
        counts["scanner_rows"] += 1
        kind = rec.get("kind") or ""
        result = rec.get("result")
        if is_planned(rec):
            counts["planned_stubs"] += 1
            continue
        if kind in CLASSIFICATION_KINDS:
            counts["classification_rows"] += 1
            continue
        if kind in HYGIENE_KINDS:
            counts["mutation_guards"] += 1
            continue
        if kind in REDOS_KINDS:
            counts["redos_rows"] += 1
            continue
        if kind in PRODUCT_KINDS:
            qid = rec.get("question_id")
            if not qid and isinstance(rec.get("detail"), dict):
                qid = rec["detail"].get("question_id")
            pair = (str(rec.get("site") or ""), str(qid or ""))
            if rec.get("synthesized"):
                # Untargeted shape-1/2 synthesis is compiler smoke, not product (#479).
                counts["properties_asked_synthesized"] += 1
                if result in SAT_RESULTS:
                    counts["properties_sat_synthesized"] += 1
                continue
            counts["properties_asked"] += 1
            asked_pairs.add(pair)
            if result in UNSAT_RESULTS:
                counts["properties_unsat"] += 1
            elif result in SAT_RESULTS:
                counts["properties_sat"] += 1
                sat_pairs.add(pair)
                if kind == "rule_diff":
                    counts["scanner_rule_diff_sat"] += 1
                sat_sites.add(
                    (
                        str(rec.get("corpus") or ""),
                        str(rec.get("regex_id") or ""),
                        str(rec.get("site") or ""),
                    )
                )
                if is_ground_truthed(rec):
                    counts["sat_ground_truthed"] += 1
            continue
        counts["other_rows"] += 1
    counts["sat_unique_sites"] = len(sat_sites)
    counts["properties_asked_distinct"] = len(asked_pairs)
    counts["properties_sat_distinct"] = len(sat_pairs)
    return dict(counts)


def _count_disclosure(rows: list[dict[str, Any]]) -> tuple[int, int]:
    private = 0
    public_ok = 0
    for rec in rows:
        if is_planned(rec):
            continue
        if rec.get("kind") not in PRODUCT_KINDS | CLASSIFICATION_KINDS:
            continue
        d = rec.get("disclosure")
        if d == "private_first":
            private += 1
        elif d == "public_ok":
            public_ok += 1
    return private, public_ok


def _summarize_rule_diff_report(path: Path) -> dict[str, int]:
    data = _read_json(path)
    results = data.get("results") or []
    sat = 0
    sat_gt = 0
    unsat = 0
    guards = 0
    for rec in results:
        kind = rec.get("kind")
        result = rec.get("result")
        if kind == "mutation_guard":
            guards += 1
            continue
        if kind != "rule_diff":
            continue
        if result in SAT_RESULTS:
            sat += 1
            if is_ground_truthed(rec):
                sat_gt += 1
        elif result in UNSAT_RESULTS:
            unsat += 1
    return {
        "rows": len(results),
        "rule_diff_sat": sat,
        "rule_diff_sat_gt": sat_gt,
        "rule_diff_unsat": unsat,
        "mutation_guards": guards,
    }


def summarize_batch_shape5(path: Path) -> dict[str, int]:
    """Count decided batch shape-5 rows as product properties asked (#477)."""
    data = _read_json(path)
    rows = data.get("rows") if isinstance(data, dict) else None
    if not isinstance(rows, list):
        rows = []
    asked = 0
    sat = 0
    sat_gt = 0
    unsat = 0
    fullmatch_only = 0
    for rec in rows:
        if not isinstance(rec, dict):
            continue
        result = rec.get("result")
        if result not in BATCH_SHAPE5_ASKED:
            continue
        asked += 1
        if result in BATCH_SHAPE5_SAT:
            sat += 1
            if is_ground_truthed(rec):
                sat_gt += 1
        elif result in UNSAT_RESULTS:
            unsat += 1
        elif result == "sat_fullmatch_only":
            fullmatch_only += 1
    return {
        "properties_asked": asked,
        "properties_sat": sat,
        "properties_sat_gt": sat_gt,
        "properties_unsat": unsat,
        "sat_fullmatch_only": fullmatch_only,
        "executed_rows": len(rows),
    }


def _upstream_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    by_status: Counter[str] = Counter()
    lang = 0
    for rec in rows:
        by_status[str(rec.get("status") or "")] += 1
        if rec.get("language_membership"):
            lang += 1
    return {
        "rows": len(rows),
        "language_membership": lang,
        "fixed_upstream": by_status["fixed_upstream"],
        "filed_plan": by_status["filed_plan"],
        "false_positive": by_status["false_positive"],
        "out_of_scope_redos": by_status["out_of_scope_redos"],
        "private_first": by_status["private_first"],
        "wont_file": by_status["wont_file"],
        "accepted_upstream": by_status["fixed_upstream"],
        "existence_proofs": by_status["fixed_upstream"] + by_status["private_first"],
        "third_party_public": 0,
    }



def _is_yara_fraction(data: dict[str, Any], stem: str) -> bool:
    dialect = str(data.get("dialect") or "")
    if dialect == "yara":
        return True
    name = str(data.get("pilot") or data.get("corpus") or stem).lower()
    return "yara" in name


def yara_encodable_split(gen: Path) -> dict[str, Any]:
    """Encodable fraction with and without YARA corpora (#492)."""
    all_n = 0
    all_ok = 0
    yara_n = 0
    yara_ok = 0
    all_unenc_reasons: Counter[str] = Counter()
    yara_unenc_reasons: Counter[str] = Counter()
    for path in sorted(gen.glob("*_encodable_fraction.json")):
        data = _read_json(path)
        n = int(data.get("sample_size") or 0)
        ok = int(data.get("encodable") or 0)
        if n <= 0:
            continue
        reasons = data.get("reasons") or {}
        unenc: Counter[str] = Counter()
        for key, val in reasons.items():
            if key == "ok":
                continue
            unenc[str(key)] += int(val or 0)
        all_n += n
        all_ok += ok
        all_unenc_reasons.update(unenc)
        stem = path.name.replace("_encodable_fraction.json", "")
        if _is_yara_fraction(data, stem):
            yara_n += n
            yara_ok += ok
            yara_unenc_reasons.update(unenc)
    all_unenc = all_n - all_ok
    yara_unenc = yara_n - yara_ok
    non_yara_n = all_n - yara_n
    non_yara_ok = all_ok - yara_ok
    fw_all = int(all_unenc_reasons.get("fullword-boundary") or 0)
    fw_yara = int(yara_unenc_reasons.get("fullword-boundary") or 0)
    return {
        "fraction_all_n": all_n,
        "fraction_all_encodable": all_ok,
        "fraction_yara_n": yara_n,
        "fraction_yara_encodable": yara_ok,
        "fraction_excluding_yara_n": non_yara_n,
        "fraction_excluding_yara_encodable": non_yara_ok,
        "unencodable_all": all_unenc,
        "unencodable_yara": yara_unenc,
        "fullword_boundary_all": fw_all,
        "fullword_boundary_yara": fw_yara,
        "encodable_fraction_all": _ratio(all_ok, all_n),
        "encodable_fraction_excluding_yara": _ratio(non_yara_ok, non_yara_n),
        "encodable_fraction_yara": _ratio(yara_ok, yara_n),
        "yara_share_of_unencodable": _ratio(yara_unenc, all_unenc),
        "fullword_share_of_unencodable": _ratio(fw_all, all_unenc),
        "fullword_share_of_yara_unencodable": _ratio(fw_yara, yara_unenc),
    }


def aggregate(
    *,
    gen_dir: Path | None = None,
    upstream_path: Path | None = None,
    security_tools: frozenset[str] | None = None,
) -> dict[str, Any]:
    gen = gen_dir if gen_dir is not None else GEN_DIR
    tools = security_tools if security_tools is not None else _load_security_tool_corpora()
    upstream_rows = load_upstream(upstream_path)

    extracted = 0
    encodable = 0
    summary_findings = 0
    summary_triage = 0
    n_summaries = 0
    for path in sorted(gen.glob("*_batch_summary.json")):
        data = _read_json(path)
        if "extracted" not in data:
            continue
        n_summaries += 1
        extracted += int(data.get("extracted") or 0)
        encodable += int(data.get("encodable") or 0)
        summary_findings += int(data.get("findings") or 0)
        summary_triage += int(data.get("triage") or 0)

    scanner_files = scanner_ndjson_files(gen)
    all_rows: list[dict[str, Any]] = []
    conversion_rows: list[dict[str, Any]] = []
    per_corpus: dict[str, list[dict[str, Any]]] = defaultdict(list)
    conversion_by_corpus: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in scanner_files:
        rows = _iter_ndjson(path)
        if path.name.endswith("_conversion.ndjson"):
            conversion_rows.extend(rows)
            for rec in rows:
                conversion_by_corpus[str(rec.get("corpus") or path.stem)].append(rec)
        else:
            all_rows.extend(rows)
            for rec in rows:
                per_corpus[str(rec.get("corpus") or path.stem)].append(rec)

    classified = classify_scanner_rows(all_rows)
    conv = classify_conversion_rows(conversion_rows)
    for key in _CONVERSION_FUNNEL_KEYS:
        classified[key] = int(classified.get(key) or 0) + int(conv.get(key) or 0)
    private, public_ok = _count_disclosure(all_rows + conversion_rows)
    yara = yara_encodable_split(gen)

    dry_runs = 0
    dry_findings = 0
    dry_private = 0
    would_open = 0
    for path in sorted(gen.glob("*-pr-dry-run.json")):
        data = _read_json(path)
        dry_runs += 1
        dry_findings += int(data.get("finding_count") or 0)
        dry_private += int(data.get("private_first_count") or 0)
        if data.get("would_open_public_upstream_issue"):
            would_open += 1

    rule_diff: dict[str, dict[str, int]] = {}
    rd_sat = 0
    rd_sat_gt = 0
    for path in sorted(gen.glob(RULE_DIFF_REPORT_GLOB)):
        summary = _summarize_rule_diff_report(path)
        rule_diff[path.name] = summary
        rd_sat += summary["rule_diff_sat"]
        rd_sat_gt += summary["rule_diff_sat_gt"]

    # Scanner NDJSON already has some rule_diff rows (result=gap). Dedicated
    # reports are extra sources; do not add them into properties_asked.
    # Batch shape-5 JSON (*_batch_shape5.json) IS product asked (#477):
    # contracted version_diff / cross_engine pairs executed in batch.
    batch_shape5: dict[str, dict[str, int]] = {}
    shape5_asked = 0
    shape5_sat = 0
    shape5_sat_gt = 0
    shape5_unsat = 0
    for path in sorted(gen.glob(BATCH_SHAPE5_GLOB)):
        summary = summarize_batch_shape5(path)
        batch_shape5[path.name] = summary
        shape5_asked += summary["properties_asked"]
        shape5_sat += summary["properties_sat"]
        shape5_sat_gt += summary.get("properties_sat_gt", 0)
        shape5_unsat += summary["properties_unsat"]

    up = _upstream_counts(upstream_rows)

    sat_in_tools = 0
    sat_not_tools = 0
    asked_in_tools = 0
    asked_not_tools = 0
    for rec in all_rows:
        if is_planned(rec) or rec.get("kind") not in PRODUCT_KINDS:
            continue
        if rec.get("synthesized"):
            continue
        in_tool = rec.get("corpus") in tools
        if in_tool:
            asked_in_tools += 1
        else:
            asked_not_tools += 1
        if rec.get("result") in SAT_RESULTS:
            if in_tool:
                sat_in_tools += 1
            else:
                sat_not_tools += 1
    for rec in conversion_rows:
        if not counts_as_conversion_asked(rec):
            continue
        in_tool = rec.get("corpus") in tools
        if in_tool:
            asked_in_tools += 1
        else:
            asked_not_tools += 1
        if rec.get("result") in SAT_RESULTS:
            if in_tool:
                sat_in_tools += 1
            else:
                sat_not_tools += 1

    asked = classified.get("properties_asked", 0) + shape5_asked
    sat = classified.get("properties_sat", 0) + shape5_sat
    unsat = classified.get("properties_unsat", 0) + shape5_unsat
    gt = classified.get("sat_ground_truthed", 0) + shape5_sat_gt
    # CRS batch shape-5 is a security-tool corpus when present.
    if shape5_asked and "coreruleset_batch_shape5.json" in batch_shape5:
        asked_in_tools += batch_shape5["coreruleset_batch_shape5.json"]["properties_asked"]
        sat_in_tools += batch_shape5["coreruleset_batch_shape5.json"]["properties_sat"]
    funnel = {
        "batch_summaries": n_summaries,
        "sites_extracted": extracted,
        "sites_encodable": encodable,
        "batch_triage_rows": summary_triage,
        "batch_summary_findings": summary_findings,
        "scanner_ndjson_files": len(scanner_files),
        "scanner_rows": classified.get("scanner_rows", 0),
        "planned_stubs": classified.get("planned_stubs", 0),
        "classification_rows": classified.get("classification_rows", 0),
        "mutation_guards": classified.get("mutation_guards", 0),
        "redos_rows": classified.get("redos_rows", 0),
        "other_rows": classified.get("other_rows", 0),
        "properties_asked": asked,
        "properties_asked_synthesized": classified.get("properties_asked_synthesized", 0),
        "properties_asked_distinct": classified.get("properties_asked_distinct", 0)
        + shape5_asked,
        "properties_unsat": unsat,
        "properties_sat": sat,
        "properties_sat_synthesized": classified.get("properties_sat_synthesized", 0),
        "properties_sat_distinct": classified.get("properties_sat_distinct", 0)
        + shape5_sat,
        "sat_unique_sites": classified.get("sat_unique_sites", 0),
        "sat_ground_truthed": gt,
        "scanner_rule_diff_sat": classified.get("scanner_rule_diff_sat", 0),
        "batch_shape5_asked": shape5_asked,
        "batch_shape5_sat": shape5_sat,
        "rule_diff_report_sat": rd_sat,
        "rule_diff_report_sat_gt": rd_sat_gt,
        "disclosed_private_first": private,
        "disclosed_public_ok": public_ok,
        "pr_dry_runs": dry_runs,
        "pr_dry_run_findings": dry_findings,
        "pr_dry_run_private_first": dry_private,
        "would_open_public_upstream": would_open,
        "accepted_upstream": up["accepted_upstream"],
        "existence_proofs": up["existence_proofs"],
        "false_positives_filed": up["false_positive"],
        "third_party_public": up["third_party_public"],
    }
    rates = {
        "encodable_fraction": _ratio(encodable, extracted),
        "property_asked_per_encodable": _ratio(asked, encodable),
        "sat_per_property_asked": _ratio(sat, asked),
        "gt_per_sat": _ratio(gt, sat),
        "pipeline_accepted_per_gt": _ratio(up["accepted_upstream"], gt),
        "pipeline_accepted_per_extracted": _ratio(up["accepted_upstream"], extracted),
        # Aliases kept one release so older quotes fail the new names first.
        "accepted_per_gt": _ratio(up["accepted_upstream"], gt),
        "accepted_per_extracted": _ratio(up["accepted_upstream"], extracted),
        "encodable_fraction_all_inventories": yara["encodable_fraction_all"],
        "encodable_fraction_excluding_yara": yara["encodable_fraction_excluding_yara"],
        "encodable_fraction_yara": yara["encodable_fraction_yara"],
        "yara_share_of_unencodable": yara["yara_share_of_unencodable"],
        "fullword_share_of_unencodable": yara["fullword_share_of_unencodable"],
    }
    by_corpus = []
    for corpus in sorted(set(per_corpus) | set(conversion_by_corpus)):
        c = classify_scanner_rows(per_corpus.get(corpus) or [])
        conv = classify_conversion_rows(conversion_by_corpus.get(corpus) or [])
        asked = int(c.get("properties_asked") or 0) + int(conv.get("properties_asked") or 0)
        if asked == 0:
            continue
        by_corpus.append(
            {
                "corpus": corpus,
                "security_tool": corpus in tools,
                "scanner_rows": int(c.get("scanner_rows") or 0),
                "properties_asked": asked,
                "properties_unsat": int(c.get("properties_unsat") or 0)
                + int(conv.get("properties_unsat") or 0),
                "properties_sat": int(c.get("properties_sat") or 0)
                + int(conv.get("properties_sat") or 0),
                "sat_ground_truthed": int(c.get("sat_ground_truthed") or 0)
                + int(conv.get("sat_ground_truthed") or 0),
                "sat_unique_sites": int(c.get("sat_unique_sites") or 0)
                + int(conv.get("sat_unique_sites") or 0),
            }
        )
    by_corpus.sort(key=lambda r: (-r["properties_asked"], r["corpus"]))

    # Surface CRS batch shape-5 even when scanner NDJSON asked is still 0.
    for fname, summary in batch_shape5.items():
        if summary.get("properties_asked", 0) <= 0:
            continue
        corpus = fname[: -len("_batch_shape5.json")] if fname.endswith(
            "_batch_shape5.json"
        ) else fname
        sat_gt = int(summary.get("properties_sat_gt", 0))
        if any(row["corpus"] == corpus for row in by_corpus):
            for row in by_corpus:
                if row["corpus"] == corpus:
                    row["properties_asked"] += summary["properties_asked"]
                    row["properties_sat"] += summary["properties_sat"]
                    row["properties_unsat"] += summary["properties_unsat"]
                    row["sat_ground_truthed"] += sat_gt
            continue
        by_corpus.append(
            {
                "corpus": corpus,
                "security_tool": corpus in tools,
                "scanner_rows": 0,
                "properties_asked": summary["properties_asked"],
                "properties_unsat": summary["properties_unsat"],
                "properties_sat": summary["properties_sat"],
                "sat_ground_truthed": sat_gt,
                "sat_unique_sites": 0,
            }
        )
    by_corpus.sort(key=lambda r: (-r["properties_asked"], r["corpus"]))

    return {
        "schema_version": SCHEMA_VERSION,
        "measure": "conversion_ledger",
        "notes": [
            "Heap's-law / singleton novelty saturates compiler coverage, not this ledger.",
            "docs/verified-findings.jsonl VF-* rows are toolkit traps, not vulnerability counts.",
            "Classification rows (usage/intent/triage kinds) are not security bugs.",
            "Mutation guards prove harness sensitivity; they are not product findings.",
            "SAT + ground-truth is a candidate finding; accepted_upstream is the last mile.",
            "would_open_public_upstream must stay 0 without a human approval file (SECURITY.md).",
            "batch_shape5 contracted version_diff/cross_engine rows count as properties_asked.",
        ],
        "funnel": funnel,
        "rates": rates,
        "security_tool_split": {
            "properties_asked_in_tools": asked_in_tools,
            "properties_asked_not_tools": asked_not_tools,
            "properties_sat_in_tools": sat_in_tools,
            "properties_sat_not_tools": sat_not_tools,
        },
        "rule_diff_reports": rule_diff,
        "batch_shape5": batch_shape5,
        "yara_split": yara,
        "upstream": up,
        "upstream_rows": [
            {k: r[k] for k in ("id", "corpus", "status", "kind", "language_membership") if k in r}
            for r in sorted(upstream_rows, key=lambda x: x["id"])
        ],
        "by_corpus": by_corpus,
    }


def render_md(data: dict[str, Any]) -> str:
    f = data["funnel"]
    r = data["rates"]
    up = data["upstream"]
    split = data["security_tool_split"]

    def pct(val: float | None) -> str:
        if val is None:
            return "n/a"
        if val != 0 and abs(val) < 0.0001:
            return f"{val:.2e}"
        return f"{val:.4f}"

    def n(val: int) -> str:
        return f"{val:,}"

    lines = [
        "# Conversion ledger",
        "",
        "Product funnel: sites → properties asked → SAT → ground-truthed → "
        "disclosed → accepted upstream.",
        "",
        "Heap's-law / singleton novelty saturates **compiler coverage**. This "
        "artifact saturates **conversion**. TIMEOUT / `unknown` is not a pass. "
        "`docs/verified-findings.jsonl` VF-* rows are toolkit traps, not this numerator.",
        "",
        "## Funnel",
        "",
        "| stage | count |",
        "|---|---|",
        f"| sites extracted (batch summaries) | {n(f['sites_extracted'])} |",
        f"| sites encodable | {n(f['sites_encodable'])} |",
        f"| scanner NDJSON rows | {n(f['scanner_rows'])} |",
        f"| planned inventory stubs | {n(f['planned_stubs'])} |",
        f"| classification rows (usage/intent/triage kinds) | {n(f['classification_rows'])} |",
        f"| mutation guards (hygiene) | {n(f['mutation_guards'])} |",
        f"| properties asked (non-planned product kinds) | {n(f['properties_asked'])} |",
        f"| properties asked distinct `(site, question_id)` | {n(f['properties_asked_distinct'])} |",
        f"| properties UNSAT (holds in declared domain) | {n(f['properties_unsat'])} |",
        f"| properties SAT | {n(f['properties_sat'])} |",
        f"| properties SAT distinct `(site, question_id)` | {n(f['properties_sat_distinct'])} |",
        f"| SAT unique sites | {n(f['sat_unique_sites'])} |",
        f"| SAT ground-truthed (`reproduced` / `PASS`) | {n(f['sat_ground_truthed'])} |",
        f"| rule_diff report SAT (dedicated pilots) | {n(f['rule_diff_report_sat'])} |",
        f"| rule_diff report SAT + ground-truth | {n(f['rule_diff_report_sat_gt'])} |",
        f"| disclosed `private_first` (scanner product+classification, skip planned) | {n(f['disclosed_private_first'])} |",
        f"| disclosed `public_ok` | {n(f['disclosed_public_ok'])} |",
        f"| dry-run `private_first` (includes planned stubs) | {n(f['pr_dry_run_private_first'])} |",
        f"| dry-run would open public upstream | {n(f['would_open_public_upstream'])} |",
        f"| accepted upstream (curated `fixed_upstream`) | {n(f['accepted_upstream'])} |",
        f"| existence proofs (`fixed_upstream` + `private_first`) | {n(f['existence_proofs'])} |",
        f"| filed false positives | {n(f['false_positives_filed'])} |",
        f"| third-party public accepted | {n(f['third_party_public'])} |",
        "",
        "## Rates",
        "",
        "| rate | value |",
        "|---|---|",
        f"| encodable / extracted | {pct(r['encodable_fraction'])} |",
        f"| properties asked / encodable | {pct(r['property_asked_per_encodable'])} |",
        f"| SAT / properties asked | {pct(r['sat_per_property_asked'])} |",
        f"| ground-truthed / SAT | {pct(r['gt_per_sat'])} |",
        f"| pipeline accepted (incl. own-code) / SAT GT | {pct(r['pipeline_accepted_per_gt'])} |",
        f"| pipeline accepted / extracted | {pct(r['pipeline_accepted_per_extracted'])} |",
        f"| encodable / extracted excluding YARA inventories | {pct(r['encodable_fraction_excluding_yara'])} |",
        f"| YARA share of inventory unencodable | {pct(r['yara_share_of_unencodable'])} |",
        f"| `fullword-boundary` share of inventory unencodable | {pct(r['fullword_share_of_unencodable'])} |",
        "",
        "## Security-tool split (scanner product kinds)",
        "",
        f"Asked in tools: {split['properties_asked_in_tools']}. "
        f"Asked elsewhere: {split['properties_asked_not_tools']}. "
        f"SAT in tools: {split['properties_sat_in_tools']}. "
        f"SAT elsewhere: {split['properties_sat_not_tools']}.",
        "",
        "## Upstream (curated)",
        "",
        f"Rows: {up['rows']}. Language-membership: {up['language_membership']}. "
        f"fixed_upstream: {up['fixed_upstream']}. filed_plan: {up['filed_plan']}. "
        f"false_positive: {up['false_positive']}. out_of_scope_redos: {up['out_of_scope_redos']}. "
        f"private_first: {up['private_first']}. wont_file: {up['wont_file']}.",
        "",
        "Source: [`docs/conversion-upstream.jsonl`](../../docs/conversion-upstream.jsonl).",
        "",
        "## Corpora with properties asked",
        "",
        "| corpus | security tool | asked | unsat | sat | sat GT | unique SAT sites |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in data["by_corpus"]:
        lines.append(
            f"| {row['corpus']} | {str(row['security_tool']).lower()} | "
            f"{row['properties_asked']} | {row['properties_unsat']} | "
            f"{row['properties_sat']} | {row['sat_ground_truthed']} | "
            f"{row['sat_unique_sites']} |"
        )
    lines.append("")
    lines.extend(
        [
            "## Denominator notes",
            "",
            "`crs-inventory.ndjson` is the @rx-only CRS measure (346 rows) from "
            "`regexproof.batch.crs_measure`; it is **not** the batch corpus. "
            "`coreruleset-inventory.ndjson` + `coreruleset_batch_summary.json` "
            "are the batch extractor (338 extracted). Do not glob `crs-inventory` "
            "into the conversion ledger sample.",
            "",
            "Synthesis considers at most `synth_max_sites` (default 200, sort by "
            "`regex_id`) per corpus. Corpora with properties asked are listed "
            "in the table above; their batch summaries record `synth_max_sites`.",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--generated-dir",
        type=Path,
        default=GEN_DIR,
        help="Directory of batch/scanner artifacts (default: properties/generated)",
    )
    ap.add_argument(
        "--upstream",
        type=Path,
        default=UPSTREAM_PATH,
        help="Curated upstream JSONL (default: docs/conversion-upstream.jsonl)",
    )
    ap.add_argument(
        "--output-dir",
        type=Path,
        default=GEN_DIR,
        help="Directory for conversion-ledger.{json,md}",
    )
    args = ap.parse_args(argv)

    if not args.upstream.is_file():
        print(f"FATAL: upstream file missing: {args.upstream}", file=sys.stderr)
        return 2

    data = aggregate(gen_dir=args.generated_dir, upstream_path=args.upstream)

    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "conversion-ledger.json"
    md_path = out_dir / "conversion-ledger.md"
    json_path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_md(data), encoding="utf-8")

    f = data["funnel"]
    print(
        f"conversion-ledger -> {md_path} + {json_path}: "
        f"extracted={f['sites_extracted']} encodable={f['sites_encodable']} "
        f"asked={f['properties_asked']} sat={f['properties_sat']} "
        f"gt={f['sat_ground_truthed']} accepted={f['accepted_upstream']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
