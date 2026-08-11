#!/usr/bin/env python3
"""Phase 3 re-measure helper (shipped in Phase 2): same manifests, frozen regex_ids.

Compares current compiler output to a frozen inventory NDJSON of regex_ids
and writes a delta table under properties/generated/.

Usage:
  python scripts/remeasure-frozen-ids.py --corpus gitleaks \\
    --baseline properties/generated/gitleaks-inventory.ndjson
  python scripts/remeasure-frozen-ids.py --corpus gitleaks --write-baseline
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import z3  # noqa: E402

from regexproof.batch.compile_records import compile_records
from regexproof.batch.extract import extract_corpus
from regexproof.batch.measure import compiler_fingerprint  # noqa: E402
from regexproof.batch.manifests import CORPUS_MANIFESTS  # noqa: E402

OUT = ROOT / "properties" / "generated"


def _compiler_fingerprint() -> str:
    return compiler_fingerprint()



def _load_ids(path: Path) -> list[str]:
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rid = row.get("regex_id")
        if rid:
            ids.append(rid)
    return ids


def measure(corpus: str) -> tuple[list[dict], dict]:
    meta = dict(CORPUS_MANIFESTS[corpus])
    path: Path = meta["path"]
    sample = ROOT / "batch" / "corpora" / corpus / "sample"
    if not path.exists() and sample.exists():
        meta["path"] = sample
    records = extract_corpus(corpus, meta)
    compiled = compile_records(
        records, lift_inline=bool(meta.get("lift_inline")), corpus_slug=corpus
    )
    enc = sum(1 for c in compiled if c.get("encodable"))
    n = len(compiled) or 1
    summary = {
        "corpus": corpus,
        "corpus_pin": meta.get("corpus_pin"),
        "sample_size": len(compiled),
        "encodable": enc,
        "fraction": round(enc / n, 4),
        "reasons": dict(Counter((c.get("compile_reason") or "ok") for c in compiled)),
        "compiler_fingerprint": _compiler_fingerprint(),
        "z3_version": getattr(z3, "get_version_string", lambda: "?")(),
        "python": platform.python_version(),
    }
    return compiled, summary


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--baseline", type=Path, help="frozen inventory NDJSON")
    ap.add_argument(
        "--write-baseline",
        action="store_true",
        help="write current inventory as the frozen baseline",
    )
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    if args.corpus not in CORPUS_MANIFESTS:
        raise SystemExit(f"unknown corpus: {args.corpus}")

    t0 = time.perf_counter()
    compiled, summary = measure(args.corpus)
    summary["wall_s"] = round(time.perf_counter() - t0, 3)
    OUT.mkdir(parents=True, exist_ok=True)

    inv_path = OUT / f"{args.corpus}-inventory.ndjson"
    with inv_path.open("w", encoding="utf-8") as fh:
        for c in compiled:
            fh.write(json.dumps(c, sort_keys=True) + "\n")

    if args.write_baseline:
        base = args.baseline or (OUT / f"{args.corpus}-frozen-ids.ndjson")
        with base.open("w", encoding="utf-8") as fh:
            for c in compiled:
                fh.write(
                    json.dumps(
                        {
                            "regex_id": c["regex_id"],
                            "pattern": c.get("pattern"),
                            "encodable": c.get("encodable"),
                            "compile_reason": c.get("compile_reason") or "ok",
                        },
                        sort_keys=True,
                    )
                    + "\n"
                )
        print(f"wrote baseline {base} ({len(compiled)} ids)")
        return 0

    baseline = args.baseline or (OUT / f"{args.corpus}-frozen-ids.ndjson")
    if not baseline.exists():
        raise SystemExit(
            f"missing baseline {baseline}; run with --write-baseline first"
        )
    frozen = _load_ids(baseline)
    by_id = {c["regex_id"]: c for c in compiled}
    missing = [i for i in frozen if i not in by_id]
    extra = [c["regex_id"] for c in compiled if c["regex_id"] not in set(frozen)]
    flipped_to_enc: list[str] = []
    flipped_to_unenc: list[str] = []
    base_rows = {}
    for line in baseline.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        base_rows[row["regex_id"]] = row
    for rid, brow in base_rows.items():
        cur = by_id.get(rid)
        if cur is None:
            continue
        be, ce = bool(brow.get("encodable")), bool(cur.get("encodable"))
        if (not be) and ce:
            flipped_to_enc.append(rid)
        elif be and (not ce):
            flipped_to_unenc.append(rid)

    delta = {
        "schema_version": "1",
        "corpus": args.corpus,
        "baseline": str(baseline),
        "frozen_ids": len(frozen),
        "current_ids": len(compiled),
        "missing_from_current": missing,
        "extra_in_current": extra,
        "flipped_unencodable_to_encodable": flipped_to_enc,
        "flipped_encodable_to_unencodable": flipped_to_unenc,
        "non_lazy_needle_moved": len(flipped_to_enc) > 0,
        "current": summary,
    }
    out = args.out or (OUT / f"{args.corpus}_remeasure_delta.json")
    if args.out is None and out.is_file():
        try:
            prev = json.loads(out.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            prev = {}
        if prev.get("superseded"):
            raise SystemExit(
                f"{out} is a SUPERSEDED stub — pass --out <path> "
                f"(e.g. properties/generated/{args.corpus}_p4_extract_delta.json)"
            )
    out.write_text(json.dumps(delta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"{args.corpus}: fraction={summary['fraction']} "
        f"flipped_to_enc={len(flipped_to_enc)} missing={len(missing)} → {out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
