#!/usr/bin/env python3
"""Wave C (#558): stub emitter — cluster ranker → conversion queue.

The stub emitter is the cluster conversion ranker (Gate 2), NOT the probe
path: probes run before batch inventory and cannot honestly fill
``guarantee`` / ``input_source`` / ``trust`` / ``declared_domain``. Stubs
carry only cheap pre-probe signals and are validated against
``schemas/queue_stub.schema.json`` (``additionalProperties: false``,
``provenance=stub``) — queue-only by schema, never a contract, never an
increment of ``properties_asked``.

Usage::

  python3 scripts/emit-conversion-queue.py --ndjson properties/generated/\\
      openwrt_packages_conversion.ndjson --corpus openwrt_packages \\
      --wave-id ow_w1 --generation 1 --output properties/conversion_queue/\\
      openwrt_packages.json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
STUB_SCHEMA = ROOT / "schemas" / "queue_stub.schema.json"

# Ensure THIS checkout's regexproof is importable (subprocess runs may
# otherwise resolve an installed/other copy).
sys.path.insert(0, str(ROOT))


def _load_ranker():
    spec = importlib.util.spec_from_file_location(
        "rank_conversion", ROOT / "scripts" / "rank-conversion-candidates.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def validate_stub(row: dict) -> None:
    """Validate one stub row against the queue-stub schema. A stub with
    contract semantics (guarantee/input_source/trust/declared_domain) is
    REJECTED — those are human-adoption fields, not stub fields."""
    import jsonschema

    schema = json.loads(STUB_SCHEMA.read_text(encoding="utf-8"))
    try:
        jsonschema.validate(row, schema)
    except jsonschema.ValidationError as exc:
        raise SystemExit(f"stub emitter: invalid stub: {exc.message}") from exc
    for banned in ("guarantee", "input_source", "trust", "declared_domain"):
        if banned in row:
            raise SystemExit(
                f"stub emitter: stub carries contract field {banned!r} — "
                "contract semantics are human-adoption only"
            )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ndjson", type=pathlib.Path, required=True)
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--wave-id", required=True)
    ap.add_argument("--generation", type=int, default=0)
    ap.add_argument("-o", "--output", type=pathlib.Path, required=True)
    args = ap.parse_args(argv)

    ranker = _load_ranker()
    records = ranker.load_ndjson(args.ndjson)
    # Conversion rows are human-adopted candidate sites — the pattern-based
    # scanner drops do not apply (Luna r1 fold #1: the documented input must
    # not produce an empty queue). rank_sites keeps path/test-name drops.
    result = ranker.rank_sites(records, vocab=ranker.DEFAULT_VOCAB, limit=15)
    keep = result.get("keep", [])

    from regexproof.mine import conversion_queue as cq

    stubs = []
    for item in keep:
        stub = {
            "provenance": "stub",
            "corpus": args.corpus,
            "pin": str(item.get("pin") or item.get("corpus_pin") or ""),
            "site": str(item.get("site") or ""),
            "idiom_bucket": str(item.get("idiom_bucket") or "unclassified"),
            "suggested_shape": str(item.get("suggested_shape") or ""),
        }
        signals = {}
        for key in ("capture_group", "charset_class", "path_vocabulary", "trust_guess"):
            if item.get(key) is not None:
                signals[key] = item[key]
        if signals:
            stub["cheap_signals"] = signals
        if item.get("suggested_sink_question"):
            stub["suggested_sink_question"] = str(item["suggested_sink_question"])
        validate_stub(stub)
        stubs.append(stub)

    out = args.output.expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    # cq.emit writes <root>/<cluster>.json — root is the queue directory.
    cq.emit(
        args.corpus,
        wave_id=args.wave_id,
        generation=args.generation,
        ranked=stubs,
        root=out.parent,
    )
    print(f"stub queue -> {out}: {len(stubs)} stubs (schema-validated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
