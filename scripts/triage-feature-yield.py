#!/usr/bin/env python3
"""Aggregate unencodable_reason across triage NDJSON into a compiler-feature-yield table.

D5: for each missing compiler feature (an ``unencodable_reason`` value), count
the *sites unlocked* if that feature were implemented, weighted by corpus
admission status (GO corpora count more). The artifact decides the next
compiler wave — it lands early, is observational only, and is regenerated
deterministically in the golden CI job.

Input:  ``properties/triage/*.ndjson``  (one row per unencodable site)
Cross:  ``properties/generated/*_gate_decision.json``  (corpus -> admission decision)
Output: ``properties/generated/compiler-feature-yield.{md,json}``

The ``corpus`` key in each triage row is the corpus name (matching the gate
decision's ``corpus`` field). When ``corpus`` is absent, the NDJSON filename
(stripped of ``.ndjson``) is used as the corpus identifier.

Weighting (admission-status weight):
  go              = 3   (live, scanned corpora — highest unlock value)
  triage-trial    = 2   (security-boundary trial — conditional)
  no-go           = 1   (below-scale / rejected — still real surface)
  (absent/unknown) = 1   (fail-closed default)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

TRIAGE_GLOB = ROOT / "properties" / "triage" / "*.ndjson"
GEN_DIR = ROOT / "properties" / "generated"
MD_OUT = GEN_DIR / "compiler-feature-yield.md"
JSON_OUT = GEN_DIR / "compiler-feature-yield.json"

# Admission status -> weight. GO corpora count more (D5 spec).
ADMISSION_WEIGHTS = {
    "go": 3,
    "triage-trial": 2,
    "no-go": 1,
}
DEFAULT_WEIGHT = 1


def _triage_inputs_hash(triage_files: list[Path]) -> str:
    """Content hash of the sorted triage NDJSON inputs (stable provenance).

    NOT the repo HEAD: the artifact is regenerated in CI where HEAD differs
    from the committing HEAD, and a self-referential pinned_head made the D5
    drift check fail on every commit (luna gate 1 re-review). The content
    hash is stable across clones and commits unless the triage corpus itself
    changes.
    """
    h = hashlib.sha256()
    for f in sorted(triage_files):
        h.update(f.name.encode("utf-8"))
        h.update(b"\0")
        h.update(f.read_bytes())
    return h.hexdigest()[:16]


def _load_gate_decisions() -> dict[str, str]:
    """Map corpus -> decision for every ``*_gate_decision.json`` in properties/generated."""
    decisions: dict[str, str] = {}
    for path in sorted(GEN_DIR.glob("*_gate_decision.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        corpus = data.get("corpus", "")
        decision = data.get("decision", "no-go")
        if corpus:
            decisions[corpus] = decision
    return decisions


def _corpus_admission(
    record: dict, filename_corpus: str, gate_decisions: dict[str, str]
) -> str:
    """Resolve the admission decision for a triage row.

    Prefer the ``corpus`` field on the row; fall back to the NDJSON filename
    (the corpus identity). Missing gates default to ``no-go`` (weight 1).
    """
    corpus = record.get("corpus") or filename_corpus
    return gate_decisions.get(corpus, "no-go")


def aggregate(triage_files: list[Path] | None = None) -> dict:
    """Aggregate unencodable reasons across triage NDJSON files.

    Returns a dict with provenance, per-reason tables, and summary stats.
    Deterministic: all dicts are sorted, all Counters are built from sorted input.
    """
    if triage_files is None:
        triage_files = sorted(TRIAGE_GLOB.parent.glob("*.ndjson"))

    gate_decisions = _load_gate_decisions()

    # unencodable_reason -> weighted site count (float, for fractional weights)
    weighted: dict[str, float] = defaultdict(float)
    # unencodable_reason -> raw site count
    raw_count: Counter[str] = Counter()
    # rows with no unencodable_reason — reported separately, not as features
    unknown_rows = 0
    # unencodable_reason -> per-corpus weighted counts
    per_corpus: dict[str, dict[str, float]] = defaultdict(
        lambda: defaultdict(float)
    )
    # unencodable_reason -> per-corpus raw counts
    per_corpus_raw: dict[str, Counter] = defaultdict(Counter)
    # unencodable_reason -> per-dialect raw counts
    per_dialect: dict[str, Counter] = defaultdict(Counter)
    # corpus-level stats
    corpus_stats: dict[str, dict] = defaultdict(
        lambda: {"rows": 0, "weighted": 0.0, "reasons": Counter()}
    )

    for path in triage_files:
        filename_corpus = path.stem  # filename without .ndjson
        lines = path.read_text(encoding="utf-8").splitlines()
        for line in lines:
            if not line.strip():
                continue
            rec = json.loads(line)
            reason = rec.get("unencodable_reason") or "(unknown)"
            dialect = rec.get("dialect") or "(unknown)"
            decision = _corpus_admission(rec, filename_corpus, gate_decisions)
            weight = ADMISSION_WEIGHTS.get(decision, DEFAULT_WEIGHT)

            if reason == "(unknown)":
                # Rows with no unencodable_reason are not a compiler feature —
                # report them separately instead of ranking "(unknown)" as an
                # unlockable feature (luna gate 1).
                unknown_rows += 1
                continue
            weighted[reason] += weight
            raw_count[reason] += 1
            per_corpus[reason][decision] += weight
            per_corpus_raw[reason][decision] += 1
            per_dialect[reason][dialect] += 1

            cs = corpus_stats[decision]
            cs["rows"] += 1
            cs["weighted"] += weight
            cs["reasons"][reason] += 1

    # Build sorted output (deterministic: sort by reason name for tie-breaking)
    reasons_sorted = sorted(raw_count.keys(), key=lambda r: (-weighted[r], -raw_count[r], r))

    rows = []
    for reason in reasons_sorted:
        rows.append({
            "unencodable_reason": reason,
            "sites_unlocked": raw_count[reason],
            "sites_weighted": round(weighted[reason], 2),
            "per_corpus": dict(sorted(per_corpus[reason].items())),
            "per_corpus_raw": dict(sorted(per_corpus_raw[reason].items())),
            "per_dialect": dict(sorted(per_dialect[reason].items())),
        })

    corpus_summary = {}
    for decision in sorted(corpus_stats.keys()):
        st = corpus_stats[decision]
        corpus_summary[decision] = {
            "rows": st["rows"],
            "sites_weighted": round(st["weighted"], 2),
            "reasons": dict(sorted(st["reasons"].items())),
        }

    provenance = {
        "input_file_count": len(triage_files),
        "triage_inputs_hash": _triage_inputs_hash(triage_files),
        "gate_decision_count": len(gate_decisions),
    }

    return {
        "schema_version": "1",
        "provenance": provenance,
        "weights": ADMISSION_WEIGHTS,
        "total_rows": sum(raw_count.values()),
        "unknown_reason_rows": unknown_rows,
        "total_weighted": round(sum(weighted.values()), 2),
        "rows": rows,
        "corpus_summary": corpus_summary,
    }


def render_md(data: dict) -> str:
    """Render the yield table as markdown (deterministic, sorted)."""
    prov = data["provenance"]
    lines = [
        "# Compiler feature-yield artifact (D5)",
        "",
        f"<!-- provenance: {prov['input_file_count']} triage files, "
        f"inputs {prov['triage_inputs_hash'][:12]}, "
        f"{prov['gate_decision_count']} gate decisions -->",
        "",
        "Sites unlocked per missing compiler feature, aggregated across",
        "`properties/triage/*.ndjson` and weighted by corpus admission status",
        "(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.",
        "",
        f"- Input files: {prov['input_file_count']}",
        f"- Triage inputs hash: `{prov['triage_inputs_hash']}`",
        f"- Gate decisions: {prov['gate_decision_count']}",
        f"- Total unencodable rows: {data['total_rows']}",
        f"- Total weighted sites: {data['total_weighted']}",
        "",
        "| # | unencodable_reason | sites | weighted | "
        "per-corpus (decision:weighted) | top dialects |",
        "|---|---|---|---|---|---|",
    ]
    for i, row in enumerate(data["rows"], 1):
        pc = ", ".join(f"{d}:{v}" for d, v in row["per_corpus"].items())
        if not pc:
            pc = "—"
        top_d = ", ".join(
            f"{d}:{c}" for d, c in sorted(row["per_dialect"].items(), key=lambda x: -x[1])[:4]
        )
        lines.append(
            f"| {i} | `{row['unencodable_reason']}` | {row['sites_unlocked']} | "
            f"{row['sites_weighted']} | {pc} | {top_d} |"
        )
    lines += [
        "",
        "## Corpus admission weighting",
        "",
        "| decision | weight | rows | weighted sites |",
        "|---|---|---|---|",
    ]
    for dec in sorted(data["corpus_summary"].keys()):
        cs = data["corpus_summary"][dec]
        lines.append(
            f"| {dec} | {data['weights'].get(dec, DEFAULT_WEIGHT)} | "
            f"{cs['rows']} | {cs['sites_weighted']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--triage-glob",
        default=str(TRIAGE_GLOB),
        help="Glob for triage NDJSON files (default: properties/triage/*.ndjson)",
    )
    ap.add_argument(
        "--output-dir",
        type=Path,
        default=GEN_DIR,
        help="Directory for compiler-feature-yield.{md,json} (default: properties/generated)",
    )
    args = ap.parse_args(argv)

    glob_str = args.triage_glob
    glob_parent = Path(glob_str).parent
    glob_pattern = Path(glob_str).name
    files = sorted(glob_parent.glob(glob_pattern))
    if not files:
        print(f"FATAL: no triage files matched {args.triage_glob}", file=sys.stderr)
        return 2

    data = aggregate(triage_files=files)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / "compiler-feature-yield.md"
    json_path = out_dir / "compiler-feature-yield.json"

    json_path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_md(data), encoding="utf-8")

    print(
        f"feature-yield -> {md_path} + "
        f"{json_path}: "
        f"{len(data['rows'])} features, {data['total_rows']} sites, "
        f"{data['total_weighted']} weighted"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
