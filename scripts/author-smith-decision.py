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


def _sites_by_bucket(gate: dict, fraction: dict) -> tuple[dict[str, int], dict[str, int]]:
    """Smith buckets follow the measured fraction; extra probe dialects are out of scope."""
    dialect_name = str(fraction.get("dialect") or "")
    n = int(fraction.get("sample_size") or 0)
    buckets: dict[str, int] = {}
    if dialect_name:
        buckets[dialect_name] = n
    extra: dict[str, int] = {}
    probe = gate.get("probe") if isinstance(gate.get("probe"), dict) else {}
    dialect = probe.get("dialect") if isinstance(probe.get("dialect"), dict) else {}
    for key, value in dialect.items():
        name = str(key)
        count = int(value)
        if name == dialect_name:
            continue
        extra[name] = count
    if not buckets and dialect:
        buckets = {str(k): int(v) for k, v in dialect.items()}
        extra = {}
    return buckets, extra


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
    ap.add_argument(
        "--allow-outside-generated",
        action="store_true",
        help="Permit --output outside properties/generated (default: refuse)",
    )
    args = ap.parse_args(argv)
    gate = load_json(args.gate)
    fraction = load_json(args.fraction)
    gate_corpus = str(gate.get("corpus") or "")
    frac_pilot = str(fraction.get("pilot") or "")
    frac_corpus = str(fraction.get("corpus") or "")
    if frac_pilot and frac_corpus and frac_pilot != frac_corpus:
        print(
            f"error: fraction pilot {frac_pilot!r} != corpus {frac_corpus!r}",
            file=sys.stderr,
        )
        return 2
    frac_name = frac_pilot or frac_corpus
    if gate_corpus and frac_name and gate_corpus != frac_name:
        print(
            f"error: gate corpus {gate_corpus!r} != fraction {frac_name!r}",
            file=sys.stderr,
        )
        return 2
    corpus = gate_corpus or frac_name
    if not corpus:
        print("error: gate/fraction missing corpus", file=sys.stderr)
        return 2
    try:
        corpus = safe_corpus_slug(corpus)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    buckets, extra = _sites_by_bucket(gate, fraction)
    record = {
        "schema_version": "1",
        "corpus": corpus,
        "corpus_pin": gate.get("corpus_pin") or fraction.get("corpus_pin"),
        "candidate_url": gate.get("candidate_url") or "",
        "smith_decision": args.decision,
        "supersedes": gate.get("decision"),
        "reason": args.reason,
        "regex_sites": int(fraction.get("sample_size") or 0),
        "sites_by_bucket": buckets,
        "additional_surface_outside_probe_scope": extra,
    }
    if jsonschema is None:
        print("error: jsonschema is required", file=sys.stderr)
        return 2
    jsonschema.validate(instance=record, schema=smith_decision_schema())
    generated = (ROOT / "properties" / "generated").resolve()
    out = (args.output or (generated / f"{corpus}_smith_decision.json")).resolve()
    if not args.allow_outside_generated and not out.is_relative_to(generated):
        print(
            f"error: output {out} is outside properties/generated; "
            "pass --allow-outside-generated to override",
            file=sys.stderr,
        )
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
