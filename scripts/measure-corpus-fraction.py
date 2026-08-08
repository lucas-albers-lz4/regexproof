#!/usr/bin/env python3
"""Measure encodable fraction for a CORPUS_MANIFESTS entry.

Writes ``properties/generated/<corpus>_encodable_fraction.json`` and an
inventory NDJSON. Deterministic: sorted extract order, frozen regex_ids.

Usage:
  python scripts/measure-corpus-fraction.py --corpus trufflehog
  python scripts/measure-corpus-fraction.py --corpus ids_rules --assert-determinism
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import z3  # noqa: E402

from regexproof.batch.runner import (  # noqa: E402
    CORPUS_MANIFESTS,
    ROOT as BATCH_ROOT,
    _compile_all,
    _extract,
)

OUT = ROOT / "properties" / "generated"


def measure(corpus: str, *, assert_determinism: bool = False) -> dict:
    if corpus not in CORPUS_MANIFESTS:
        raise SystemExit(f"unknown corpus: {corpus}")
    meta = dict(CORPUS_MANIFESTS[corpus])
    path: Path = meta["path"]
    sample = ROOT / "batch" / "corpora" / corpus / "sample"
    scope = meta.get("measure_scope") or "full_corpus"
    if not path.exists() and sample.is_dir():
        meta["path"] = sample
        path = sample
        scope = "sample"
        print(f"NOTE: using sample corpus at {sample}", file=sys.stderr)
    if not path.exists():
        raise SystemExit(
            f"corpus path missing: {path} — see batch/corpora/{corpus}/README.md"
        )

    if "sample" in path.parts and not meta.get("measure_scope"):
        scope = "sample"

    if meta.get("corpus_type") == "inventory_only" or meta.get("extractor") == "rust_inventory":
        from regexproof.extractors.rust_inventory import write_rust_inventory

        OUT.mkdir(parents=True, exist_ok=True)
        report = write_rust_inventory(path, OUT / f"{corpus}_inventory_only.json")
        report["corpus"] = corpus
        report["corpus_pin"] = meta.get("corpus_pin")
        report["decision"] = "inventory_only"
        report["scope"] = "inventory_only"
        report["unclassified_parse_errors"] = 0
        # Also write a stub fraction-shaped row for matrix consumers that expect it.
        frac = {
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

    t0 = time.perf_counter()
    records = _extract(corpus, meta)
    compiled = _compile_all(
        records, lift_inline=bool(meta.get("lift_inline")), corpus_slug=corpus
    )
    if assert_determinism:
        again = _compile_all(
            _extract(corpus, meta),
            lift_inline=bool(meta.get("lift_inline")),
            corpus_slug=corpus,
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
    report = {
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
        "complete_run": True,
        "wall_s": round(wall, 3),
        "budget": meta.get("budget"),
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
        f"parse-error={unclassified} → {out_path.relative_to(ROOT)}"
    )
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", required=True, choices=sorted(CORPUS_MANIFESTS))
    ap.add_argument("--assert-determinism", action="store_true")
    args = ap.parse_args(argv)
    report = measure(args.corpus, assert_determinism=args.assert_determinism)
    # Soft warn on unclassified; hard-fail when measuring new wave corpora.
    wave = (
        "trufflehog",
        "ids_rules",
        "semgrep_rules",
        "pcre2_testdata",
        "re2_testdata",
        "cpython_re",
        "busybox",
    )
    if args.corpus in wave and report.get("unclassified_parse_errors"):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
