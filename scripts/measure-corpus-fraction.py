#!/usr/bin/env python3
"""Measure encodable fraction for a CORPUS_MANIFESTS entry.

Writes ``properties/generated/<corpus>_encodable_fraction.json`` and an
inventory NDJSON. Deterministic: sorted extract order, frozen regex_ids.

Budget enforcement: max_patterns, max_wall_s, max_mem_mb, max_disk_mb are
checked; breach → complete_run=false, exit 1.

Usage:
  python scripts/measure-corpus-fraction.py --corpus trufflehog
  python scripts/measure-corpus-fraction.py --corpus ids_rules --assert-determinism
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform

import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import z3  # noqa: E402

from regexproof.batch.runner import (  # noqa: E402
    CORPUS_MANIFESTS,
    WAVE_CORPORA,
    BudgetBreached,
    _compile_all,
    _extract,
)

OUT = ROOT / "properties" / "generated"


def _disk_usage_mb(path: Path) -> float:
    """Estimate disk usage of path tree in MB (best-effort)."""
    try:
        total = 0
        if path.is_file():
            total = path.stat().st_size
        elif path.is_dir():
            for fp in path.rglob("*"):
                if fp.is_file():
                    total += fp.stat().st_size
        return total / (1024 * 1024)
    except Exception:  # noqa: BLE001
        return 0.0


def _rss_mb() -> int:
    """Current process RSS in MB (best-effort)."""
    try:
        import resource
        usage = resource.getrusage(resource.RUSAGE_SELF)
        return int(usage.ru_maxrss / 1024)
    except Exception:  # noqa: BLE001
        return 0


def _check_budgets(
    budget: dict[str, Any],
    *,
    corpus: str,
    n_patterns: int,
    wall_s: float,
    path: Path,
) -> list[str]:
    """Return list of breach descriptions (empty = ok)."""
    breaches: list[str] = []

    max_pat = budget.get("max_patterns")
    if max_pat is not None and max_pat > 0 and n_patterns > max_pat:
        breaches.append(f"max_patterns: limit={max_pat} actual={n_patterns}")

    max_wall = budget.get("max_wall_s")
    if max_wall is not None and wall_s > max_wall:
        breaches.append(f"max_wall_s: limit={max_wall} actual={wall_s:.1f}")

    max_mem = budget.get("max_mem_mb")
    if max_mem is not None:
        rss = _rss_mb()
        if rss > max_mem:
            breaches.append(f"max_mem_mb: limit={max_mem} actual={rss}")

    max_disk = budget.get("max_disk_mb")
    if max_disk is not None and path.exists():
        disk = _disk_usage_mb(path)
        if disk > max_disk:
            breaches.append(f"max_disk_mb: limit={max_disk} actual={disk:.1f}")

    return breaches


def measure(corpus: str, *, assert_determinism: bool = False) -> dict:
    if corpus not in CORPUS_MANIFESTS:
        raise SystemExit(f"unknown corpus: {corpus}")
    meta = dict(CORPUS_MANIFESTS[corpus])
    path: Path = meta["path"]
    sample_path = meta.get("sample_path")
    if isinstance(sample_path, str):
        sample_path = Path(sample_path)
    if sample_path is None:
        sample_path = ROOT / "batch" / "corpora" / corpus / "sample"

    scope = meta.get("measure_scope") or "full_corpus"
    complete_run = True
    path_usable = path.exists() and (path.is_file() or any(path.iterdir()))

    if not path_usable:
        if corpus in WAVE_CORPORA and scope != "sample":
            raise SystemExit(
                f"HARD ERROR: {corpus} corpus path missing/empty ({path}) "
                f"and measure_scope={scope!r} (not 'sample') — "
                f"no sample fallback allowed for wave corpora in full mode"
            )
        if isinstance(sample_path, Path) and sample_path.exists():
            meta["path"] = sample_path
            path = sample_path
            scope = "sample"
            complete_run = False
            print(
                f"NOTE: {corpus} corpus path missing/empty; "
                f"using sample at {sample_path}",
                file=sys.stderr,
            )
        else:
            raise SystemExit(
                f"corpus path missing: {path} — see batch/corpora/{corpus}/README.md"
            )

    if "sample" in path.parts and not meta.get("measure_scope"):
        scope = "sample"
        complete_run = False

    if meta.get("measure_scope") == "sample":
        scope = "sample"
        complete_run = False
        # Prefer explicit sample_path when declared sample scope.
        sp = meta.get("sample_path")
        if isinstance(sp, str):
            sp = Path(sp)
        if isinstance(sp, Path) and sp.exists():
            meta["path"] = sp
            path = sp
        elif sample_path.exists() and path != sample_path:
            # Keep configured path if it already points under sample/.
            if "sample" not in path.parts:
                meta["path"] = sample_path
                path = sample_path

    if meta.get("corpus_type") == "inventory_only" or meta.get("extractor") == "rust_inventory":
        from regexproof.extractors.rust_inventory import write_rust_inventory

        OUT.mkdir(parents=True, exist_ok=True)
        report = write_rust_inventory(path, OUT / f"{corpus}_inventory_only.json")
        report["corpus"] = corpus
        report["corpus_pin"] = meta.get("corpus_pin")
        report["decision"] = "inventory_only"
        report["scope"] = "inventory_only"
        report["unclassified_parse_errors"] = 0
        frac: dict[str, Any] = {
            "schema_version": "1",
            "corpus": corpus,
            "corpus_pin": meta.get("corpus_pin"),
            "decision": "inventory_only",
            "fraction": None,
            "encodable": report.get("extracted"),
            "sample_size": report.get("extracted"),
            "reasons": {},
            "scope": "inventory_only",
            "unclassified_parse_errors": 0,
        }
        (OUT / f"{corpus}_encodable_fraction.json").write_text(
            json.dumps(frac, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(
            f"{corpus}: inventory_only extracted={report.get('extracted')} "
            f"→ properties/generated/{corpus}_inventory_only.json"
        )
        return frac

    budget = meta.get("budget") or {}
    t0 = time.perf_counter()
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
        )
    except BudgetBreached as exc:
        wall = time.perf_counter() - t0
        report = _write_breach_report(
            corpus, meta, scope, path, wall,
            breach=str(exc), n_patterns=len(records),
        )
        return report

    if assert_determinism:
        again = _compile_all(
            _extract(corpus, meta),
            lift_inline=bool(meta.get("lift_inline")),
            corpus_slug=corpus,
            budget=budget,
        )
        a = [c.get("regex_id") for c in compiled]
        b = [c.get("regex_id") for c in again]
        if a != b:
            raise SystemExit("FAIL: non-deterministic extraction (regex_id order)")

    wall = time.perf_counter() - t0
    reasons = Counter((c.get("compile_reason") or "ok") for c in compiled)
    enc = sum(1 for c in compiled if c.get("encodable"))
    n = len(compiled) or 1
    fraction = enc / n
    decision = "go" if fraction >= 0.30 else "no-go"
    unclassified = reasons.get("parse-error", 0)

    breaches = _check_budgets(
        budget,
        corpus=corpus,
        n_patterns=len(compiled),
        wall_s=wall,
        path=path,
    )
    if breaches:
        complete_run = False

    inv_path = OUT / f"{corpus}-inventory.ndjson"
    OUT.mkdir(parents=True, exist_ok=True)
    with inv_path.open("w", encoding="utf-8") as fh:
        for c in compiled:
            fh.write(
                json.dumps(
                    {
                        "regex_id": c.get("regex_id"),
                        "site": c.get("site"),
                        "pattern": c.get("pattern"),
                        "flags": c.get("flags") or "",
                        "dialect": c.get("dialect"),
                        "call_kind": c.get("call_kind"),
                        "encodable": bool(c.get("encodable")),
                        "compile_reason": c.get("compile_reason"),
                        "corpus": corpus,
                    },
                    sort_keys=True,
                )
                + "\n"
            )

    compiler_commit = (
        hashlib.sha1(
            (ROOT / "regexproof" / "compiler" / "simple_parse.py")
            .read_bytes()
        ).hexdigest()[:12]
    )
    report: dict[str, Any] = {
        "schema_version": "1",
        "pilot": corpus,
        "scope": scope,
        "corpus_pin": meta.get("corpus_pin"),
        "commit": meta.get("commit"),
        "compiler_fingerprint": compiler_commit,
        "dialect": meta.get("dialect"),
        "sample_size": len(compiled),
        "encodable": enc,
        "fraction": round(fraction, 4),
        "go_no_go_threshold": 0.3,
        "decision": decision,
        "decision_rule": "go iff encodable/sample_size >= 0.3",
        "reasons": dict(sorted(reasons.items())),
        "unclassified_parse_errors": unclassified,
        "complete_run": complete_run,
        "wall_s": round(wall, 3),
        "budget": budget if budget else None,
        "budget_breaches": breaches if breaches else None,
        "inventory_path": str(inv_path.relative_to(ROOT)),
        "engine_versions": {
            "python": platform.python_version(),
            "z3": z3.get_version_string(),
        },
        "path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
    }
    if unclassified:
        report["decision_note"] = (
            f"{unclassified} unclassified parse-error rows — Phase 1 requires zero"
        )
    out_path = OUT / f"{corpus}_encodable_fraction.json"
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"{corpus}: {enc}/{len(compiled)} = {fraction:.4f} decision={decision} "
        f"parse-error={unclassified} complete_run={complete_run} → {out_path.relative_to(ROOT)}"
    )
    if breaches:
        print(
            f"BUDGET BREACH ({corpus}): {'; '.join(breaches)}",
            file=sys.stderr,
        )
    return report


def _write_breach_report(
    corpus: str,
    meta: dict[str, Any],
    scope: str,
    path: Path,
    wall: float,
    *,
    breach: str,
    n_patterns: int,
) -> dict[str, Any]:
    """Write a fraction report with complete_run=False for a budget breach."""
    OUT.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "schema_version": "1",
        "pilot": corpus,
        "scope": scope,
        "corpus_pin": meta.get("corpus_pin"),
        "dialect": meta.get("dialect"),
        "sample_size": n_patterns,
        "encodable": 0,
        "fraction": 0.0,
        "go_no_go_threshold": 0.3,
        "decision": "no-go",
        "decision_rule": "budget breach → no-go",
        "reasons": {},
        "unclassified_parse_errors": 0,
        "complete_run": False,
        "wall_s": round(wall, 3),
        "budget": meta.get("budget"),
        "budget_breaches": [breach],
        "engine_versions": {
            "python": platform.python_version(),
            "z3": z3.get_version_string(),
        },
        "path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
    }
    out_path = OUT / f"{corpus}_encodable_fraction.json"
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"BUDGET BREACH ({corpus}): {breach}", file=sys.stderr)
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", required=True, choices=sorted(CORPUS_MANIFESTS))
    ap.add_argument("--assert-determinism", action="store_true")
    args = ap.parse_args(argv)
    report = measure(args.corpus, assert_determinism=args.assert_determinism)
    if args.corpus in WAVE_CORPORA and report.get("unclassified_parse_errors"):
        return 2
    if report.get("budget_breaches"):
        return 1
    # Declared sample scope may set complete_run=false without being a failure.
    # Only fail incomplete runs that were unexpected fallbacks / breaches.
    if (
        not report.get("complete_run", True)
        and report.get("scope") != "sample"
        and not report.get("budget_breaches")
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
