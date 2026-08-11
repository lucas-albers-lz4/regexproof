#!/usr/bin/env python3
"""regexproof harness skeleton — property registry + mutation guards.

Thin CLI shim over ``regexproof.harness`` (#192). Full contract docs live on
the package and in AGENTS.md / docs/REPORTING.md.

Usage:
  python3 z3-verify.py --list
  python3 z3-verify.py --all
  python3 z3-verify.py P1 P2 P1-mutated
  python3 z3-verify.py --all --require-ground-truth
  python3 z3-verify.py --all --json          # NDJSON (one object per line)
  python3 z3-verify.py --all --json-legacy   # one-release JSON array mode
  python3 z3-verify.py --check-mutation-coverage

Exit code: 0 = all pass; 1 = any FAIL/TIMEOUT/coverage gap;
2 = unknown property names / flag conflict on the CLI; 3 = wrong z3-solver version.

--require-ground-truth: any SAT (counterexample) result MUST have replayed
its witness against the real implementation via the property's ground_truth
callback. A SAT result without a callback (or a witness that fails to
reproduce) is a hard failure — an unverified counterexample is never
reported as a vulnerability.

--json: emit one NDJSON object per property (schema_version, result, witness,
ground-truth, domain, wall_ms, engine_versions, not_proven). Same facts as
the human output — the two reports can never disagree. Partial streams remain
valid if a later property fails. Mutually exclusive with --json-legacy.

--json-legacy: emit a single JSON array of the same records (one-release
compat). Mutually exclusive with --json.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Checkout bootstrap (match scripts/batch-scan.py) — fix-wave #71.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from regexproof.harness.cli import main

if __name__ == "__main__":
    sys.exit(main())
