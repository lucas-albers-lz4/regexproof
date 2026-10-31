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
    REJECTED — those are adoption-record fields, not stub fields. Its pin
    identifies the corpus snapshot only; it does not indicate human review."""
    import jsonschema

    pin = row.get("pin")
    if not isinstance(pin, str) or not pin.strip():
        raise SystemExit("stub emitter: pin must be a nonblank corpus snapshot identity")
    schema = json.loads(STUB_SCHEMA.read_text(encoding="utf-8"))
    try:
        jsonschema.validate(row, schema)
    except jsonschema.ValidationError as exc:
        raise SystemExit(f"stub emitter: invalid stub: {exc.message}") from exc
    for banned in ("guarantee", "input_source", "trust", "declared_domain"):
        if banned in row:
            raise SystemExit(
                f"stub emitter: stub carries contract field {banned!r} — "
                "contract fields belong in an adopted property contract"
            )


def resolve_corpus_pin(corpus: str) -> str:
    """Resolve the immutable snapshot identity from the batch manifest.

    Conversion NDJSON rows often have no pin of their own. The queue binds
    those sites to the configured corpus snapshot; it never invents a pin or
    treats the binding as evidence of human review.
    """
    from regexproof.mine.conversion_queue import corpus_snapshot_pin

    try:
        return corpus_snapshot_pin(corpus)
    except SystemExit as exc:
        raise SystemExit(f"stub emitter: {exc}") from exc


def check_item_pin(item: dict, corpus_pin: str, *, site: str) -> None:
    """Reject row-level pins that disagree with the canonical corpus pin."""
    observed = []
    for key in ("pin", "corpus_pin"):
        value = item.get(key)
        if value is None:
            continue
        if not isinstance(value, str) or not value.strip():
            raise SystemExit(
                f"stub emitter: row {site!r} has blank/invalid {key}; refusing pin fallback"
            )
        observed.append((key, value.strip()))
    distinct = {value for _, value in observed}
    if len(distinct) > 1:
        raise SystemExit(
            f"stub emitter: row {site!r} has conflicting pin and corpus_pin values"
        )
    if distinct and next(iter(distinct)) != corpus_pin:
        key, value = observed[0]
        raise SystemExit(
            f"stub emitter: row {site!r} {key} {value!r} conflicts with "
            f"corpus manifest pin {corpus_pin!r}"
        )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ndjson", type=pathlib.Path, required=True)
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--wave-id", required=True)
    ap.add_argument("--generation", type=int, default=0)
    ap.add_argument(
        "--clock-iso", default="",
        help="ISO clock for deterministic created_at (ledger artifact clock; "
             "never datetime.now() — CodeRabbit #569)",
    )
    ap.add_argument("-o", "--output", type=pathlib.Path, required=True)
    args = ap.parse_args(argv)

    # Corpus name must be a plain cluster id — a path-like value (/, \\, ..)
    # would make cq.emit write outside out.parent (CodeRabbit #569).
    if (
        args.corpus in {".", ".."}
        or "/" in args.corpus
        or "\\" in args.corpus
        or not args.corpus.strip()
    ):
        ap.error(f"invalid --corpus {args.corpus!r}: must be a plain cluster name")

    ranker = _load_ranker()
    records = ranker.load_ndjson(args.ndjson)
    corpus_pin = resolve_corpus_pin(args.corpus)
    # Check source records before ranking: the ranker currently coalesces
    # pin/corpus_pin, which could otherwise hide contradictory provenance.
    for record in records:
        row_corpus = record.get("corpus")
        if row_corpus != args.corpus:
            raise SystemExit(
                f"stub emitter: row {record.get('site')!r} belongs to corpus "
                f"{row_corpus!r}, not --corpus {args.corpus!r}"
            )
        check_item_pin(record, corpus_pin, site=str(record.get("site") or ""))
        question_id = record.get("question_id") or record.get("name")
        if not isinstance(question_id, str) or not question_id.strip():
            raise SystemExit(
                f"stub emitter: row {record.get('site')!r} has no canonical "
                "question_id/name"
            )
    # Conversion rows are adopted contract candidate sites — the pattern-based
    # scanner drops do not apply (Luna r1 fold #1: the documented input must
    # not produce an empty queue). rank_sites keeps path/test-name drops.
    result = ranker.rank_sites(records, vocab=ranker.DEFAULT_VOCAB, limit=15)
    keep = result.get("keep", [])

    from regexproof.mine import conversion_queue as cq

    stubs = []
    for item in keep:
        site = str(item.get("site") or "")
        check_item_pin(item, corpus_pin, site=site)
        question_id = item.get("question_id")
        if isinstance(question_id, str):
            question_id = question_id.strip()
        if not question_id:
            raise SystemExit(f"stub emitter: row {site!r} has no question identity")
        source_identity = cq.materialized_source_identity(args.corpus, site)
        stub = {
            "provenance": "stub",
            "corpus": args.corpus,
            "pin": corpus_pin,
            "site": site,
            "question_id": question_id,
            "idiom_bucket": str(item.get("idiom_bucket") or "unclassified"),
            "suggested_shape": str(item.get("suggested_shape") or ""),
            **source_identity,
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
    # Final-gate #5 (MEDIUM): the output MUST be the canonical
    # <cluster>.json name — the scheduler and queue consumers read
    # <root>/<cluster>.json; a custom filename would move the artifact
    # where no consumer looks (queue invisible to scheduler blocking).
    canonical = out.parent / f"{args.corpus}.json"
    if out != canonical:
        raise SystemExit(
            f"emit-conversion-queue: --output must be the canonical "
            f"{canonical} (got {out}) — queue consumers read "
            "<root>/<cluster>.json"
        )
    out.parent.mkdir(parents=True, exist_ok=True)
    # cq.emit writes <root>/<cluster>.json — root is the queue directory.
    queue_root = out.parent
    cq.emit(
        args.corpus,
        wave_id=args.wave_id,
        generation=args.generation,
        ranked=stubs,
        root=queue_root,
        clock_iso=args.clock_iso or None,
    )
    print(f"stub queue -> {out}: {len(stubs)} stubs (schema-validated)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
