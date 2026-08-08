"""Batch orchestrator: extract → triage → intent → (optional redos join) → report."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

from regexproof.batch.disclose import (  # noqa: E402
    assert_no_auto_publication,
    tag_disclosure,
    write_pr_dry_run,
)
from regexproof.batch.intent import (  # noqa: E402
    detect_intent_mismatches,
    detect_usage_mismatches,
)
from regexproof.batch.inventory import check_corpus_coverage, load_inventory  # noqa: E402
from regexproof.batch.report import write_markdown, write_ndjson  # noqa: E402
from regexproof.batch.triage import triage_records_from_compiled, write_triage_ndjson  # noqa: E402
from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler.normalize import normalize_inline_flags  # noqa: E402
from regexproof.extractors.js_babel import extract_js  # noqa: E402
from regexproof.extractors.python_ast import extract_python  # noqa: E402
from regexproof.extractors.rule_file import extract_rule_file  # noqa: E402
from regexproof.redos.join import join_findings  # noqa: E402

CORPUS_MANIFESTS: dict[str, dict[str, Any]] = {
    "gitleaks": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "pilots" / "gitleaks" / "config" / "gitleaks.toml",
        "dialect": "re2",
        "extractor": "rule_file",
        "repo": "gitleaks/gitleaks",
        "security_tool": True,
        "lift_inline": True,
    },
    "validatorjs": {
        "corpus_type": "validator",
        "path": ROOT / "pilots" / "validatorjs" / "src",
        "files": [
            "isAscii.js",
            "isAlpha.js",
            "isAlphanumeric.js",
            "isEmail.js",
            "isFQDN.js",
            "isURL.js",
            "alpha.js",
        ],
        "dialect": "ecma",
        "extractor": "js_dir",
        "repo": "validatorjs/validator.js",
        "security_tool": False,
        "lift_inline": False,
    },
    "detect-secrets": {
        "corpus_type": "rule_corpus",
        "path": ROOT / "pilots" / "detect-secrets" / "sample_plugins.py",
        "dialect": "py_re",
        "extractor": "python",
        "repo": "Yelp/detect-secrets",
        "security_tool": True,
        "lift_inline": False,
    },
}


def _extract(corpus: str, meta: dict[str, Any]) -> list[dict[str, Any]]:
    path: Path = meta["path"]
    if meta["extractor"] == "rule_file":
        source = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        return extract_rule_file(
            source, repo=meta["repo"], file=rel, dialect=meta["dialect"]
        )
    if meta["extractor"] == "js_dir":
        out: list[dict[str, Any]] = []
        for name in meta.get("files") or sorted(p.name for p in path.glob("*.js")):
            fp = path / name
            rel = str(fp.relative_to(ROOT))
            out.extend(extract_js(fp.read_text(encoding="utf-8"), repo=meta["repo"], file=rel))
        return out
    if meta["extractor"] == "js":
        source = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        return extract_js(source, repo=meta["repo"], file=rel)
    if meta["extractor"] == "python":
        source = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        return extract_python(source, repo=meta["repo"], file=rel)
    raise ValueError(meta["extractor"])


def _compile_all(records: list[dict[str, Any]], *, lift_inline: bool) -> list[dict[str, Any]]:
    out = []
    for rec in records:
        pattern = rec["pattern"]
        flags = rec.get("flags") or ""
        if lift_inline:
            pattern, flags = normalize_inline_flags(pattern, flags)
        if rec.get("unencodable_reason"):
            out.append(
                {
                    **rec,
                    "encodable": False,
                    "compile_reason": rec["unencodable_reason"],
                    "corpus": rec.get("repo"),
                }
            )
            continue
        cr = compile_pattern(pattern, flags, rec["dialect"], rec["call_kind"])
        out.append(
            {
                **rec,
                "pattern": pattern,
                "flags": flags,
                "encodable": cr.encodable,
                "compile_reason": cr.unencodable_reason,
                "corpus": rec.get("repo"),
            }
        )
    return out


def run_corpus(
    corpus: str,
    *,
    out_dir: Path,
    with_redos: bool = False,
    approval_path: Path | None = None,
) -> dict[str, Any]:
    meta = CORPUS_MANIFESTS[corpus]
    inventory = load_inventory(meta["corpus_type"])
    records = _extract(corpus, meta)
    compiled = _compile_all(records, lift_inline=bool(meta.get("lift_inline")))

    triage = triage_records_from_compiled(compiled)
    write_triage_ndjson(out_dir.parent / "triage" / f"{corpus}.ndjson", triage)

    findings: list[dict[str, Any]] = []
    # Inventory-driven shape markers (auto property stubs — encode deferred to Z3 job)
    for q in inventory["questions"]:
        findings.append(
            {
                "schema_version": "1",
                "regex_id": f"inventory:{q['id']}",
                "kind": "property",
                "corpus": corpus,
                "result": "planned",
                "site": f"inventory:{q['id']}",
                "pattern": "",
                "shape": q["shape"],
                "ground_truth_status": "N/A",
                "disclosure": None,
                "detail": {"question_id": q["id"], "threat": q["threat"]},
            }
        )

    findings.extend(detect_usage_mismatches(compiled))
    findings.extend(detect_intent_mismatches(compiled))

    redos_findings: list[dict[str, Any]] = []
    if with_redos:
        from regexproof.redos.runner import analyze_record

        for rec in compiled:
            if not rec.get("encodable"):
                continue
            # Cap ReDoS fan-out for CI time
            if len(redos_findings) >= 5:
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
                        "ground_truth_status": "N/A",
                        "disclosure": "private_first" if meta.get("security_tool") else None,
                        "detail": {"tool": f.get("tool"), "severity": f.get("severity")},
                    }
                )

    # Join Z3-side placeholders with redos (separate sections)
    z3_side = [{"regex_id": f["regex_id"], "result": f["result"]} for f in findings if f["kind"] != "redos"]
    joined = join_findings(z3_side, redos_findings)

    findings = tag_disclosure(findings, corpus=corpus)
    write_ndjson(out_dir / f"{corpus}.ndjson", findings)
    write_markdown(out_dir / f"{corpus}.md", corpus=corpus, findings=findings)

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
        "encodable": sum(1 for c in compiled if c.get("encodable")),
        "triage": len(triage),
        "findings": len(findings),
        "inventory_questions": len(inventory["questions"]),
        "join_regex_ids": len(joined.get("regex_ids") or []),
        "engine": {"python": platform.python_version()},
    }
    (out_dir / f"{corpus}_batch_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return summary


def measure_coreruleset(out_dir: Path) -> dict[str, Any]:
    """PCRE encodable-fraction gate on pinned CRS sample; go iff >= 0.30."""
    sample = ROOT / "batch" / "corpora" / "coreruleset" / "sample.rules"
    lines = [
        ln.strip()
        for ln in sample.read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    encodable = 0
    for i, pat in enumerate(lines):
        cr = compile_pattern(pat, "", "pcre", "search")
        if cr.encodable:
            encodable += 1
    n = len(lines) or 1
    fraction = encodable / n
    decision = "go" if fraction >= 0.30 else "no-go"
    report = {
        "schema_version": "1",
        "pilot": "coreruleset",
        "dialect": "pcre",
        "sample_size": len(lines),
        "encodable": encodable,
        "fraction": fraction,
        "go_no_go_threshold": 0.3,
        "decision": decision,
        "sample_path": str(sample.relative_to(ROOT)),
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "coreruleset_encodable_fraction.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report


def run_batch(
    corpora: list[str],
    *,
    out_dir: Path | None = None,
    with_redos: bool = False,
) -> dict[str, Any]:
    cov = check_corpus_coverage()
    if cov:
        raise SystemExit("inventory coverage failed: " + "; ".join(cov))

    out_dir = out_dir or (ROOT / "properties" / "generated")
    out_dir.mkdir(parents=True, exist_ok=True)
    (ROOT / "properties" / "triage").mkdir(parents=True, exist_ok=True)

    summaries = {}
    pair_counts = {}
    for name in corpora:
        summaries[name] = run_corpus(name, out_dir=out_dir, with_redos=with_redos)
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

    crs = measure_coreruleset(out_dir)
    if crs["decision"] == "go":
        pair_counts["coreruleset"] = {
            "admitted": 0,
            "dropped": 0,
            "note": "fraction gate go; no independent-spec R1 catalog in Phase 5",
        }
    else:
        pair_counts["coreruleset"] = {
            "admitted": 0,
            "note": f"excluded decision={crs['decision']} fraction={crs['fraction']}",
        }

    batch = {
        "schema_version": "1",
        "corpora": summaries,
        "pair_counts": pair_counts,
        "coreruleset": crs,
    }
    (out_dir / "batch_pair_counts.json").write_text(
        json.dumps(pair_counts, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (out_dir / "batch_summary.json").write_text(
        json.dumps(batch, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    # Byte-identical fingerprint of triage+ndjson names for reproducibility smoke
    blob = ""
    for name in sorted(corpora):
        for suffix in (f"{name}.ndjson",):
            p = out_dir / suffix
            blob += hashlib.sha256(p.read_bytes()).hexdigest() + "\n"
    (out_dir / "batch_repro.sha256").write_text(blob, encoding="utf-8")
    return batch


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="regexproof batch scanner (Phase 5 NDJSON contract)",
    )
    ap.add_argument(
        "--corpus",
        default="all",
        help="gitleaks|validatorjs|detect-secrets|all",
    )
    ap.add_argument("--out", type=Path, default=ROOT / "properties" / "generated")
    ap.add_argument("--with-redos", action="store_true")
    ap.add_argument(
        "--json-legacy",
        action="store_true",
        help="mutually exclusive legacy flag (rejected)",
    )
    args = ap.parse_args(argv)
    if args.json_legacy:
        print("error: --json-legacy is mutually exclusive with batch NDJSON", file=sys.stderr)
        return 2
    if args.corpus == "all":
        corpora = ["gitleaks", "validatorjs", "detect-secrets"]
    else:
        corpora = [args.corpus]
    run_batch(corpora, out_dir=args.out, with_redos=args.with_redos)
    print("batch ok:", ", ".join(corpora))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
