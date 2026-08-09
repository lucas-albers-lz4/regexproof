#!/usr/bin/env python3
"""Two-run byte-identical batch reproducibility gate (Phase 6)."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Artifacts compared across two runs (sorted regex_id NDJSON + summaries).
COMPARE_SUFFIXES = (
    "detect-secrets.ndjson",
    "gitleaks.ndjson",
    "validatorjs.ndjson",
    "batch_pair_counts.json",
    "batch_summary.json",
    "batch_repro.sha256",
)


def _fingerprint(out_dir: Path) -> dict[str, str]:
    digests = {}
    for name in COMPARE_SUFFIXES:
        path = out_dir / name
        if not path.is_file():
            raise FileNotFoundError(path)
        digests[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digests


def _run_batch(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    # Admission gate: batch runs require committed decision artifacts for rule
    # corpora. The reproducibility check exercises extraction determinism, not
    # admission, so copy the committed decisions into the sandbox out_dir
    # (same pattern as tests/test_batch.py::test_batch_runner_smoke).
    committed = ROOT / "properties" / "generated"
    for path in committed.glob("*_gate_decision.json"):
        (out_dir / path.name).write_bytes(path.read_bytes())
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "regexproof.batch",
            "--corpus",
            "all",
            "--out",
            str(out_dir),
        ],
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


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="regexproof-repro-") as tmp:
        base = Path(tmp)
        a = base / "run1" / "generated"
        b = base / "run2" / "generated"
        _run_batch(a)
        _run_batch(b)
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
