#!/usr/bin/env python3
"""Two-run byte-identical batch reproducibility gate (Phase 6).

Also: single-corpus extraction determinism for Wave-3 corpora::

  python scripts/ci-batch-repro.py --corpus dompurify
  python scripts/ci-batch-repro.py --corpus isemail
  python scripts/ci-batch-repro.py --corpus email_addresses
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Cumulative-MCR fold (M3): the two-run comparison covers EVERY committed
# batch output (per-corpus NDJSON, batch Markdown, per-corpus summaries,
# encodable fractions, PR dry-runs, triage NDJSON, aggregates) — a fixed
# six-file list let other committed artifacts drift undetected.
COMPARE_SUFFIXES = (".ndjson", ".json", ".md", ".sha256")


def _fingerprint(out_dir: Path) -> dict[str, str]:
    digests = {}
    for path in sorted(out_dir.rglob("*")):
        if path.is_file() and path.suffix in COMPARE_SUFFIXES:
            digests[str(path.relative_to(out_dir))] = hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
    return digests


def _run_batch(out_dir: Path, *, synthesize: bool = False) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    # Admission gate: batch runs require committed decision artifacts for rule
    # corpora. The reproducibility check exercises extraction determinism, not
    # admission, so copy the committed decisions into the sandbox out_dir
    # (same pattern as tests/test_batch.py::test_batch_runner_smoke).
    committed = ROOT / "properties" / "generated"
    for path in committed.glob("*_gate_decision.json"):
        (out_dir / path.name).write_bytes(path.read_bytes())
    cmd = [
        sys.executable,
        "-m",
        "regexproof.batch",
        "--corpus",
        "all",
        "--out",
        str(out_dir),
    ]
    if synthesize:
        # P3 fold (luna gate 1): the two-run reproducibility check must also
        # regenerate the synthesized rows, or a synthesis regression passes
        # CI while the golden job's --synthesize step catches it.
        cmd.append("--synthesize")
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        shell=False,
        check=False,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise SystemExit(proc.returncode)


def _extract_determinism(corpus: str) -> int:
    """Two-run extraction must yield identical regex_id sequences."""
    from regexproof.batch.extract import extract_corpus
    from regexproof.batch.manifests import CORPUS_MANIFESTS

    if corpus not in CORPUS_MANIFESTS:
        print(f"unknown corpus: {corpus}", file=sys.stderr)
        return 2
    meta = dict(CORPUS_MANIFESTS[corpus])
    a = [r["regex_id"] for r in extract_corpus(corpus, meta)]
    b = [r["regex_id"] for r in extract_corpus(corpus, meta)]
    if a != b:
        print(f"FAIL: non-deterministic extraction for {corpus}", file=sys.stderr)
        return 1
    if not a:
        print(f"FAIL: {corpus} extracted 0 records", file=sys.stderr)
        return 1
    print(f"{corpus} extraction determinism ok (n={len(a)})")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--corpus",
        default="all",
        help="all (default two-run batch) or a single CORPUS_MANIFESTS name",
    )
    ap.add_argument(
        "--synthesize",
        action="store_true",
        help="P3: regenerate the synthesized rows in both runs",
    )
    args = ap.parse_args(argv)
    if args.corpus != "all":
        return _extract_determinism(args.corpus)

    with tempfile.TemporaryDirectory(prefix="regexproof-repro-") as tmp:
        base = Path(tmp)
        a = base / "run1" / "generated"
        b = base / "run2" / "generated"
        _run_batch(a, synthesize=args.synthesize)
        _run_batch(b, synthesize=args.synthesize)
        fa = _fingerprint(a)
        fb = _fingerprint(b)
        if fa != fb:
            for k in sorted(set(fa) | set(fb)):
                if fa.get(k) != fb.get(k):
                    print(f"MISMATCH {k}: {fa.get(k)} != {fb.get(k)}", file=sys.stderr)
            return 1
    print("batch reproducibility ok (byte-identical across two runs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
