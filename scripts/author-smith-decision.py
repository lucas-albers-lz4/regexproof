#!/usr/bin/env python3
"""Write a schema-valid *_smith_decision.json. Decision is a required flag.

Usage:
  python scripts/author-smith-decision.py --gate GATE.json --fraction FRAC.json \\
      --decision go --reason '151/179 = 0.8436 on first-party PII regexes'
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.admission.serialize import dumps_pinned  # noqa: E402
from regexproof.batch.smith_support import load_json, safe_corpus_slug, wave_checklist  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.schemas import smith_decision_schema  # noqa: E402

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None  # type: ignore[assignment]


def _sites_by_bucket(gate: dict, fraction: dict) -> dict[str, int]:
    probe = gate.get("probe") if isinstance(gate.get("probe"), dict) else {}
    dialect = probe.get("dialect") if isinstance(probe.get("dialect"), dict) else {}
    if dialect:
        return {str(k): int(v) for k, v in dialect.items()}
    dialect_name = str(fraction.get("dialect") or "unknown")
    n = int(fraction.get("sample_size") or 0)
    return {dialect_name: n}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gate", type=Path, required=True)
    ap.add_argument("--fraction", type=Path, required=True)
    ap.add_argument(
        "--decision",
        required=True,
        choices=("go", "no-go", "triage-continues"),
        help="required; never inferred from fraction",
    )
    ap.add_argument("--reason", required=True)
    ap.add_argument("-o", "--output", type=Path)
    args = ap.parse_args(argv)
    gate = load_json(args.gate)
    fraction = load_json(args.fraction)
    corpus = str(gate.get("corpus") or fraction.get("pilot") or "")
    if not corpus:
        print("error: gate/fraction missing corpus", file=sys.stderr)
        return 2
    try:
        corpus = safe_corpus_slug(corpus)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    record = {
        "schema_version": "1",
        "corpus": corpus,
        "corpus_pin": gate.get("corpus_pin") or fraction.get("corpus_pin"),
        "candidate_url": gate.get("candidate_url") or "",
        "smith_decision": args.decision,
        "supersedes": gate.get("decision"),
        "reason": args.reason,
        "regex_sites": int(fraction.get("sample_size") or 0),
        "sites_by_bucket": _sites_by_bucket(gate, fraction),
        "additional_surface_outside_probe_scope": {},
    }
    if jsonschema is None:
        print("error: jsonschema is required", file=sys.stderr)
        return 2
    jsonschema.validate(instance=record, schema=smith_decision_schema())
    generated = (ROOT / "properties" / "generated").resolve()
    if args.output:
        out = args.output
    else:
        out = generated / f"{corpus}_smith_decision.json"
        resolved = out.resolve()
        if generated not in resolved.parents and resolved.parent != generated:
            print(f"error: output escapes properties/generated: {resolved}", file=sys.stderr)
            return 2
    atomic_write_text(out, dumps_pinned(record))
    print(out)
    print(wave_checklist(corpus), file=sys.stderr)
    frac = fraction.get("fraction")
    if frac is not None:
        print(
            f"fraction={frac} (informational; smith_decision={args.decision!r} was flagged)",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
