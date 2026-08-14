"""Batch orchestrator: extract → triage → intent → (optional redos join) → report."""

from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing
import platform
import sys
import time
from pathlib import Path
from typing import Any

import jsonschema

from regexproof.batch import budgets as _budgets
from regexproof.batch.budgets import (  # noqa: F401
    BudgetBreached,
    apply_address_space_cap,
    check_budget_mem,
    check_budget_patterns,
)
from regexproof.batch.compile_records import DEFAULT_WORKER_COUNT, compile_records
from regexproof.batch.crs_measure import (  # noqa: F401
    measure_coreruleset,
    measure_coreruleset_full,
    measure_coreruleset_sample,
)
from regexproof.batch.disclose import (
    assert_no_auto_publication,
    tag_disclosure,
    write_pr_dry_run,
)
from regexproof.batch.evidence import enforce_evidence_gates
from regexproof.batch.extract import (
    extract_corpus,
    extract_glob,
    validate_expected_roots,
)
from regexproof.batch.intent import (
    detect_intent_mismatches,
    detect_usage_mismatches,
)
from regexproof.batch.inventory import check_corpus_coverage, load_inventory
from regexproof.batch.manifests import (  # noqa: F401
    CORPUS_MANIFESTS,
    MAX_FILE_BYTES,
    ROOT,
    WAVE_CORPORA,
)
from regexproof.batch.report import write_markdown, write_ndjson
from regexproof.batch.synthesize import synthesize_compiled
from regexproof.batch.triage import triage_records_from_compiled, write_triage_ndjson
from regexproof.io_atomic import atomic_write_text
from regexproof.redos.join import join_findings
from regexproof.z3_pin import assert_z3_pinned

# One-release private aliases (#193) — prefer public names in new code.
_MAX_FILE_BYTES = MAX_FILE_BYTES
_extract = extract_corpus
_extract_glob = extract_glob

PILOT_CORPORA = ["gitleaks", "validatorjs", "detect-secrets"]
AGGREGATE_ARTIFACTS = (
    "batch_summary.json",
    "batch_pair_counts.json",
    "batch_repro.sha256",
)
_compile_all = compile_records
_validate_expected_roots = validate_expected_roots
_check_budget_patterns = check_budget_patterns
_check_budget_mem = check_budget_mem
_apply_address_space_cap = apply_address_space_cap
_LAST_ADDRESS_SPACE_CAP_APPLIED = None  # compat; prefer _budgets.LAST_ADDRESS_SPACE_CAP_APPLIED


def _discard_streamed_mirrors(
    compiled: list[tuple[dict[str, Any], Any, dict[str, Any] | None]],
) -> None:
    """C1 interim mirror-discard (issue #426 / wave C1).

    ``compile_records`` now returns/streams ``(row, mirror, meta)`` triples
    in-process for the P3 synthesis stage. Until synthesis lands, discard the
    mirror explicitly so the interim release keeps pre-P2 output exactly — the
    discard path is part of P2, never a silent pass-through that could later
    make synthesis no-op without anyone noticing.
    """
    for _row, _mirror, _meta in compiled:
        _ = _mirror
    # C1 fold (luna re-gate 3): the discard must actually release the Z3 ASTs
    # (and the triple list) — callers extract rows first, then discard, so
    # clearing here is safe and reclaims RSS.
    compiled.clear()


def resolve_corpus_path(corpus: str, meta: dict[str, Any]) -> dict[str, Any]:
    """Apply sample fallback / measure_scope path policy before extract (#196)."""
    meta = dict(meta)
    path: Path = meta["path"]
    sample_path = meta.get("sample_path") or ROOT / "batch" / "corpora" / corpus / "sample"
    if isinstance(sample_path, str):
        sample_path = Path(sample_path)
    path_usable = path.exists() and (path.is_file() or any(path.iterdir()))
    if not path_usable:
        if corpus in WAVE_CORPORA:
            if meta.get("measure_scope") == "sample" and isinstance(
                sample_path, Path
            ) and sample_path.exists():
                meta["path"] = sample_path
                print(
                    f"NOTE: {corpus} full corpus path missing ({path}); "
                    f"using sample at {sample_path}",
                    file=sys.stderr,
                )
            else:
                raise SystemExit(
                    f"HARD ERROR: {corpus} corpus path missing/empty ({path}) "
                    f"and measure_scope={meta.get('measure_scope')!r} "
                    f"(sample fallback only when measure_scope='sample')"
                )
        else:
            sample = ROOT / "batch" / "corpora" / corpus / "sample"
            if sample.is_dir():
                print(
                    f"NOTE: {corpus} corpus path missing/empty ({path}); "
                    f"falling back to sample at {sample}",
                    file=sys.stderr,
                )
                meta["path"] = sample
                meta["measure_scope"] = "sample"
            elif (ROOT / "properties" / "generated" / f"{corpus}_gate_decision.json").exists():
                # ADMITTED corpus, no tree AND no sample: FAIL CLOSED — a
                # 0-site run would read 'go' against an empty tree (luna
                # #276 -r3 finding #1: the dogfood_shell seam; the sample
                # fallback stays, the silent empty run does not)
                raise SystemExit(
                    f"HARD ERROR: {corpus} is ADMITTED (committed gate decision) "
                    f"but its corpus path is missing/empty ({path}) with no "
                    f"sample fallback — materialize the tree before batch runs "
                    f"(0-site silent pass blocked)"
                )
    if meta.get("measure_scope") == "sample":
        sp = meta.get("sample_path")
        if isinstance(sp, str):
            sp = Path(sp)
        if not isinstance(sp, Path):
            sp = sample_path if isinstance(sample_path, Path) else None
        if isinstance(sp, Path) and sp.exists():
            cur = meta["path"]
            if "sample" not in Path(cur).parts:
                meta["path"] = sp
                print(
                    f"NOTE: {corpus} measure_scope=sample; using {sp}",
                    file=sys.stderr,
                )
        elif not isinstance(sp, Path) or not sp.exists():
            raise SystemExit(
                f"HARD ERROR: {corpus} measure_scope=sample but sample path "
                f"missing ({sp})"
            )
    return meta


def extract_and_compile_corpus(
    corpus: str,
    meta: dict[str, Any],
    *,
    jobs: int | None = None,
    cache_dir: Path | str | None = None,
    cache_stats: dict[str, Any] | None = None,
) -> tuple[list[dict[str, Any]], list[tuple[dict[str, Any], Any, dict[str, Any] | None]]]:
    """Extract + compile with budget gate (#196). Gates before writes.

    ``compiled`` is the ``(row, mirror, meta)`` stream from ``compile_records``
    (C1) — rows stay lean; the mirror/metadata travel in-process for the P3
    synthesis stage.
    """
    _validate_expected_roots(corpus, meta)
    budget = meta.get("budget") or {}
    wall_t0 = time.monotonic()
    records = _extract(corpus, meta)
    if not records and corpus in WAVE_CORPORA:
        raise SystemExit(
            f"HARD ERROR: {corpus} extraction produced 0 records — "
            f"empty glob must not fake zero-pattern success"
        )
    try:
        compiled = _compile_all(
            records,
            lift_inline=bool(meta.get("lift_inline")),
            corpus_slug=corpus,
            budget=budget,
            wall_t0=wall_t0,
            jobs=jobs,
            cache_dir=cache_dir,
            cache_stats=cache_stats,
        )
    except BudgetBreached as exc:
        raise SystemExit(
            f"BUDGET BREACH ({corpus}): {exc.field} "
            f"limit={exc.limit} actual={exc.actual}"
        ) from exc
    return records, compiled



def run_corpus(
    corpus: str,
    *,
    out_dir: Path,
    with_redos: bool = False,
    approval_path: Path | None = None,
    require_ground_truth: bool = False,
    fail_planned: bool = False,
    redos_timeout_s: float | None = None,
    emit_planned: bool = True,
    synthesize: bool = False,
    synth_diff_fuzz_sample: int | None = None,
    jobs: int | None = None,
    cache_dir: Path | str | None = None,
) -> dict[str, Any]:
    meta = CORPUS_MANIFESTS[corpus]
    if meta.get("corpus_type") == "inventory_only":
        from regexproof.extractors.rust_inventory import write_rust_inventory

        path: Path = meta["path"]
        out_dir.mkdir(parents=True, exist_ok=True)
        report = write_rust_inventory(path, out_dir / f"{corpus}_inventory_only.json")
        # Empty findings NDJSON so run_batch repro hashing still finds the file.
        write_ndjson(out_dir / f"{corpus}.ndjson", [])
        write_markdown(
            out_dir / f"{corpus}_batch.md",
            corpus=corpus,
            findings=[],
        )
        summary = {
            "corpus": corpus,
            "findings": 0,
            "encodable": report.get("extracted"),
            "decision": "inventory_only",
            "detail": report,
            "cache": {"hits": 0, "misses": 0, "entries": 0, "hit_rate": 0.0},
            "cache_hit_rate": 0.0,
        }
        atomic_write_text(
            out_dir / f"{corpus}_batch_summary.json",
            json.dumps(summary, indent=2, sort_keys=True) + "\n",
        )
        return summary
    meta = resolve_corpus_path(corpus, meta)
    inventory = load_inventory(meta["corpus_type"])
    cache_stats: dict[str, Any] = {}
    records, compiled = extract_and_compile_corpus(
        corpus,
        meta,
        jobs=jobs,
        cache_dir=cache_dir,
        cache_stats=cache_stats,
    )

    rows = [pair[0] for pair in compiled]
    synthesis = None
    if synthesize:
        synthesis = synthesize_compiled(
            corpus,
            compiled,
            inventory,
            meta,
            diff_fuzz_sample=synth_diff_fuzz_sample,
        )
    # C1 (issue #426): rows stay lean (no AST); release streamed mirrors after
    # the opt-in P3 consumer has completed.
    _discard_streamed_mirrors(compiled)

    triage = triage_records_from_compiled(rows)
    write_triage_ndjson(out_dir.parent / "triage" / f"{corpus}.ndjson", triage)

    findings: list[dict[str, Any]] = []
    # Inventory-driven shape markers (auto property stubs — encode deferred to Z3 job)
    if emit_planned:
        for q in inventory["questions"]:
            if synthesis is not None and q["id"] in synthesis.executed_questions:
                continue
            findings.append(
                {
                    "schema_version": "1",
                    "regex_id": f"inventory:{q['id']}",
                    "kind": "property",
                    "corpus": corpus,
                    "result": "planned",
                    "ground_truth_status": "planned",
                    "site": f"inventory:{q['id']}",
                    "pattern": "",
                    "shape": q["shape"],
                    "disclosure": None,
                    "detail": {"question_id": q["id"], "threat": q["threat"]},
                }
            )

    if synthesis is not None:
        findings.extend(synthesis.findings)

    findings.extend(detect_usage_mismatches(rows))
    findings.extend(detect_intent_mismatches(rows))

    redos_findings: list[dict[str, Any]] = []
    redos_incomplete = False
    if with_redos:
        from regexproof.redos.runner import analyze_record

        budget_s = redos_timeout_s
        if budget_s is None:
            budget_s = (meta.get("budget") or {}).get("redos_wall_s", 120)
        t0 = time.monotonic()
        for rec in rows:
            if not rec.get("encodable"):
                continue
            if budget_s is not None and (time.monotonic() - t0) >= float(budget_s):
                redos_incomplete = True
                break
            for f in analyze_record(rec, triage=False):
                redos_findings.append(f)
                findings.append(
                    {
                        "schema_version": "1",
                        "regex_id": f["regex_id"],
                        "kind": "redos",
                        "corpus": corpus,
                        "result": f["result"],
                        "site": f.get("site") or "",
                        "pattern": f.get("pattern") or "",
                        "shape": None,
                        "disclosure": "private_first" if meta.get("security_tool") else None,
                        "engine_versions": (
                            {str(f.get("tool")): str(f.get("tool_version"))}
                            if f.get("tool")
                            else None
                        ),
                        "detail": {"tool": f.get("tool"), "severity": f.get("severity")},
                    }
                )
            # Re-check after each record so a slow analyze_record still trips the gate.
            if budget_s is not None and (time.monotonic() - t0) >= float(budget_s):
                redos_incomplete = True
                break

    if redos_incomplete:
        findings.append(
            {
                "schema_version": "1",
                "regex_id": f"redos-incomplete:{corpus}",
                "kind": "redos",
                "corpus": corpus,
                "result": "incomplete",
                "site": f"redos-timeout:{redos_timeout_s or (meta.get('budget') or {}).get('redos_wall_s', 120)}",
                "pattern": "",
                "shape": None,
                "disclosure": "private_first" if meta.get("security_tool") else None,
                "detail": {
                    "error": "ReDoS fan-out truncated by wall-clock timeout gate",
                    "redos_timeout_s": redos_timeout_s
                    or (meta.get("budget") or {}).get("redos_wall_s", 120),
                    "findings_emitted": len(redos_findings),
                },
            }
        )

    # Join Z3-side placeholders with redos (separate sections)
    z3_side = [{"regex_id": f["regex_id"], "result": f["result"]} for f in findings if f["kind"] != "redos"]
    joined = join_findings(z3_side, redos_findings)

    findings = tag_disclosure(findings, corpus=corpus)
    enforce_evidence_gates(
        findings,
        require_ground_truth=require_ground_truth,
        fail_planned=fail_planned,
    )
    write_ndjson(out_dir / f"{corpus}.ndjson", findings)
    # Keep Phase 3 shape-5 report at {corpus}.md; batch uses a distinct path.
    write_markdown(out_dir / f"{corpus}_batch.md", corpus=corpus, findings=findings)

    dry = write_pr_dry_run(
        out_dir / f"{corpus}-pr-dry-run.json",
        findings=findings,
        approval_path=approval_path,
    )
    assert_no_auto_publication(dry)

    summary = {
        "schema_version": "1",
        "corpus": corpus,
        "corpus_type": meta["corpus_type"],
        "extracted": len(records),
        "encodable": sum(1 for c in rows if c.get("encodable")),
        "triage": len(triage),
        "findings": len(findings),
        "inventory_questions": len(inventory["questions"]),
        "join_regex_ids": len(joined.get("regex_ids") or []),
        "engine": {"python": platform.python_version()},
        "redos_findings": len(redos_findings),
        "redos_incomplete": redos_incomplete,
        "complete_run": not redos_incomplete,
        "address_space_cap": _budgets.LAST_ADDRESS_SPACE_CAP_APPLIED,
        "cache": {
            "hits": int(cache_stats.get("hits", 0)),
            "misses": int(cache_stats.get("misses", 0)),
            "entries": int(cache_stats.get("entries", 0)),
            "hit_rate": float(cache_stats.get("hit_rate", 0.0)),
        },
        "cache_hit_rate": float(cache_stats.get("hit_rate", 0.0)),
    }
    if synthesis is not None:
        summary["synthesis"] = synthesis.stats
    atomic_write_text(
        out_dir / f"{corpus}_batch_summary.json",
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
    )
    if redos_incomplete:
        raise SystemExit(
            f"evidence gate failed: ReDoS report incomplete "
            f"(timeout_s={redos_timeout_s or (meta.get('budget') or {}).get('redos_wall_s', 120)}); "
            "raise --redos-timeout-s / corpus budget.redos_wall_s for a complete run "
            f"(partial findings written to {out_dir / f'{corpus}.ndjson'})"
        )
    return summary


def check_admission_gates(
    corpora: list[str],
    *,
    out_dir: Path,
) -> list[str]:
    """Return violation messages for missing/invalid corpus admission decisions.

    The corpus admission gate (sweep/corpus-admission-gate.md): every
    rule_corpus / validator corpus in CORPUS_MANIFESTS must have a
    ``<corpus>_gate_decision.json`` at ``out_dir`` (default
    ``properties/generated``), valid against ``gate_decision.schema.json``,
    with decision in ``go`` / ``triage-trial``. Testdata and inventory-only
    corpora are pipeline inputs, not scanned repos, so they are exempt.

    Missing or invalid artifacts hard-fail (never silent): a corpus with no
    admission record is not a corpus we are allowed to run.
    """
    from regexproof.schemas import load_schema

    schema = load_schema("gate_decision.schema.json")
    violations: list[str] = []
    for name in corpora:
        meta = CORPUS_MANIFESTS.get(name)
        if meta is None:
            violations.append(f"{name}: not in CORPUS_MANIFESTS")
            continue
        if meta.get("corpus_type") in ("testdata", "inventory_only"):
            continue
        path = out_dir / f"{name}_gate_decision.json"
        if not path.exists():
            violations.append(
                f"{name}: admission decision missing ({path.name}); "
                "run the admission probe and commit the decision artifact "
                "(sweep/corpus-admission-gate.md)"
            )
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            violations.append(f"{name}: admission decision unreadable: {exc}")
            continue
        try:
            jsonschema.validate(instance=data, schema=schema)
        except jsonschema.ValidationError as exc:
            violations.append(f"{name}: admission decision fails schema: {exc.message}")
            continue
        decision = data.get("decision")
        if decision not in ("go", "triage-trial"):
            violations.append(
                f"{name}: admission decision={decision!r}; "
                "go or triage-trial required (no-go corpora are not run)"
            )
    return violations


def run_batch(
    corpora: list[str],
    *,
    out_dir: Path | None = None,
    with_redos: bool = False,
    require_ground_truth: bool = False,
    fail_planned: bool = False,
    redos_timeout_s: float | None = None,
    emit_planned: bool = True,
    synthesize: bool = False,
    synth_diff_fuzz_sample: int | None = None,
    jobs: int | None = None,
    cache_dir: Path | str | None = None,
    write_pilot_aggregate: bool | None = None,
) -> dict[str, Any]:
    cov = check_corpus_coverage()
    if cov:
        raise SystemExit("inventory coverage failed: " + "; ".join(cov))

    out_dir = out_dir or (ROOT / "properties" / "generated")
    admission = check_admission_gates(corpora, out_dir=out_dir)
    if admission:
        raise SystemExit("admission gate failed: " + "; ".join(admission))

    out_dir.mkdir(parents=True, exist_ok=True)
    (ROOT / "properties" / "triage").mkdir(parents=True, exist_ok=True)
    if write_pilot_aggregate is None:
        write_pilot_aggregate = set(corpora) == set(PILOT_CORPORA)
    if write_pilot_aggregate and set(corpora) != set(PILOT_CORPORA):
        raise SystemExit(
            "error: write_pilot_aggregate requires exactly the three "
            f"pilot corpora {PILOT_CORPORA}"
        )

    summaries = {}
    pair_counts = {}
    for name in corpora:
        summaries[name] = run_corpus(
            name,
            out_dir=out_dir,
            with_redos=with_redos,
            require_ground_truth=require_ground_truth,
            fail_planned=fail_planned,
            redos_timeout_s=redos_timeout_s,
            emit_planned=emit_planned,
            synthesize=synthesize,
            synth_diff_fuzz_sample=synth_diff_fuzz_sample,
            jobs=jobs,
            cache_dir=cache_dir,
        )
        cache = summaries[name].get("cache") or {}
        print(
            f"{name}: cache hit rate {float(cache.get('hit_rate', 0.0)):.1%} "
            f"({cache.get('hits', 0)}/{cache.get('entries', 0)})"
        )
        # Pair-at-scale: reuse Phase-3 discovery when catalog exists
        if name == "gitleaks":
            from regexproof.rule_diff.pairs import discover_pairs

            specs = ROOT / "pilots" / "gitleaks" / "canonical_specs" / "catalog.json"
            toml = ROOT / "pilots" / "gitleaks" / "config" / "gitleaks.toml"
            d = discover_pairs(toml_path=toml, specs_path=specs)
            pair_counts[name] = {
                "admitted": d["admitted_count"],
                "dropped": d["dropped_count"],
            }
        else:
            pair_counts[name] = {"admitted": 0, "dropped": 0, "note": "no independent-spec catalog"}

    if write_pilot_aggregate or "coreruleset" in corpora:
        crs = measure_coreruleset(out_dir)
    else:
        crs = {
            "decision": "skipped",
            "fraction": None,
            "scope": "not-measured",
            "note": "single-corpus Smith run; pass write_pilot_aggregate to measure CRS",
        }
    if crs["decision"] == "go":
        pair_counts["coreruleset"] = {
            "admitted": 0,
            "dropped": 0,
            "note": "fraction gate go; CRS rule-derived adapter is Phase-2 rule_diff",
            "scope": crs.get("scope"),
            "fraction": crs.get("fraction"),
        }
    else:
        pair_counts["coreruleset"] = {
            "admitted": 0,
            "note": f"excluded decision={crs['decision']} fraction={crs['fraction']}",
            "scope": crs.get("scope"),
        }

    batch = {
        "schema_version": "1",
        "corpora": summaries,
        "pair_counts": pair_counts,
        "coreruleset": {
            k: crs[k]
            for k in crs
            if k != "records"  # keep batch_summary compact; full report on disk
        },
    }
    total_hits = sum(
        int((summary.get("cache") or {}).get("hits", 0))
        for summary in summaries.values()
    )
    total_entries = sum(
        int((summary.get("cache") or {}).get("entries", 0))
        for summary in summaries.values()
    )
    batch["cache_hit_rate"] = total_hits / total_entries if total_entries else 0.0
    if not write_pilot_aggregate:
        return batch
    atomic_write_text(
        out_dir / "batch_pair_counts.json",
        json.dumps(pair_counts, indent=2, sort_keys=True) + "\n",
    )
    atomic_write_text(
        out_dir / "batch_summary.json",
        json.dumps(batch, indent=2, sort_keys=True) + "\n",
    )

    # Byte-identical fingerprint of triage+ndjson names for reproducibility smoke
    blob = ""
    for name in sorted(corpora):
        for suffix in (f"{name}.ndjson",):
            p = out_dir / suffix
            blob += hashlib.sha256(p.read_bytes()).hexdigest() + "\n"
    atomic_write_text(out_dir / "batch_repro.sha256", blob)
    return batch


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="regexproof batch scanner (Phase 5 NDJSON contract)",
    )
    ap.add_argument(
        "--corpus",
        default="all",
        help="gitleaks|validatorjs|detect-secrets|coreruleset|all",
    )
    ap.add_argument("--out", type=Path, default=ROOT / "properties" / "generated")
    ap.add_argument(
        "--write-pilot-aggregate",
        action="store_true",
        help="write batch_summary.json / pair counts / repro sha "
        "(implied for --corpus all; omit on single-corpus Smith runs)",
    )
    ap.add_argument("--with-redos", action="store_true")
    ap.add_argument(
        "--synthesize",
        action="store_true",
        help="synthesize validator shape-1/2 properties (off by default)",
    )
    ap.add_argument(
        "--synth-diff-fuzz-sample",
        type=int,
        default=None,
        help="seeded differential-fuzz samples per wide/shape-2 site",
    )
    ap.add_argument(
        "--jobs",
        type=int,
        default=DEFAULT_WORKER_COUNT,
        help=f"compile worker processes (default: {DEFAULT_WORKER_COUNT}, max: 8)",
    )
    ap.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help="mirror cache directory (default: .cache/mirrors)",
    )
    ap.add_argument(
        "--redos-timeout-s",
        type=float,
        default=None,
        help="wall-clock ReDoS fan-out budget in seconds (per corpus); "
        "truncation emits incomplete and fails the gate. "
        "Falls back to corpus budget.redos_wall_s when unset.",
    )
    ap.add_argument(
        "--redos-cap",
        type=int,
        default=None,
        help=argparse.SUPPRESS,  # removed: use --redos-timeout-s
    )
    ap.add_argument(
        "--require-ground-truth",
        action="store_true",
        help="hard-fail SAT Z3 findings without reproduced ground_truth_status; "
        "TIMEOUT/unknown always hard-fails",
    )
    ap.add_argument(
        "--fail-planned",
        action="store_true",
        help="hard-fail inventory planned stubs (lists unexecuted question IDs)",
    )
    ap.add_argument(
        "--no-planned",
        action="store_true",
        help="omit inventory planned stubs from findings",
    )
    ap.add_argument(
        "--json-legacy",
        action="store_true",
        help="mutually exclusive legacy flag (rejected)",
    )
    args = ap.parse_args(argv)
    try:
        multiprocessing.set_start_method("spawn")
    except RuntimeError:
        # Embedders/tests may have selected a context already.  The compile
        # path still requests an explicit spawn context for every pool.
        pass
    assert_z3_pinned()
    if args.json_legacy:
        print("error: --json-legacy is mutually exclusive with batch NDJSON", file=sys.stderr)
        return 2
    if args.redos_cap is not None:
        print(
            "error: --redos-cap was removed; use --redos-timeout-s (wall-clock gate)",
            file=sys.stderr,
        )
        return 2
    if args.synth_diff_fuzz_sample is not None and args.synth_diff_fuzz_sample < 0:
        print("error: --synth-diff-fuzz-sample must be non-negative", file=sys.stderr)
        return 2
    if args.jobs < 1:
        print("error: --jobs must be at least 1", file=sys.stderr)
        return 2
    if args.corpus == "all":
        # coreruleset is opt-in: its corpus is an external pinned clone, not
        # committed (see batch/corpora/coreruleset/README.md).
        corpora = ["gitleaks", "validatorjs", "detect-secrets"]
    else:
        corpora = [args.corpus]
    run_batch(
        corpora,
        out_dir=args.out,
        with_redos=args.with_redos,
        require_ground_truth=args.require_ground_truth,
        fail_planned=args.fail_planned,
        redos_timeout_s=args.redos_timeout_s,
        emit_planned=not args.no_planned,
        synthesize=args.synthesize,
        synth_diff_fuzz_sample=args.synth_diff_fuzz_sample,
        jobs=args.jobs,
        cache_dir=args.cache_dir,
        write_pilot_aggregate=(
            True if args.corpus == "all" else args.write_pilot_aggregate
        ),
    )
    print("batch ok:", ", ".join(corpora))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
