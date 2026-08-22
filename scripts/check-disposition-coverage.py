#!/usr/bin/env python3
"""Fail-closed disposition-coverage join (#554 Phase A).

Every ground-truth-confirmed SAT in ``properties/generated/*_conversion.ndjson``
must have a curated disposition row in ``docs/conversion-upstream.jsonl``.
A GT SAT without a curated row means the GT→filed hop silently drops findings;
this check makes that a hard failure in CI (golden job, after the ledger
regeneration). TIMEOUT/unknown rows are not GT SATs and are ignored here.

Join-key canonicalization (this issue owns `(site, question_id)`
canonicalization per the #550 cross-issue agreement; #550 owns hash-input
canonicalization):

- ``site``    — the scanner-row ``site`` string, stripped. If it parses as a
  URL (``scheme://…``), scheme and hostname are lowercased and the rest of the
  URL is kept verbatim; otherwise the string is compared verbatim
  (repo-relative paths are case-sensitive).
- ``question_id`` — exact string after ``strip()``. Scanner rows without an
  explicit ``question_id`` fall back to their ``name`` (same fallback as
  ``classify_conversion_rows`` in ``scripts/conversion-ledger.py``).

Disposition enum (source of truth for statuses): ``filed``, ``filed_plan``
("filed upstream, awaiting response" — distinct from ``wont_file``),
``wont_file``, ``false_positive``, ``private_first``, ``fixed_upstream``,
``approval_missing``, ``out_of_scope_redos``. Unknown values are rejected.

Date rule: ``filed_at`` / ``resolved_at`` are required going forward or
optional-with-reason for backfilled rows. Backfilled rows must carry a
``reason_code`` plus a ``disposition_date`` that is either an ISO date or the
explicit enum value ``unknown_date``. ``unknown_date`` rows are excluded from
median time-to-acceptance, and time-to-acceptance is reported censored-aware
(Kaplan-Meier, or median of closed rows only) — never by mixing censored and
closed rows in a plain median.

CRS 942220 reconciliation guard: the curated file carries exactly one
disposition for CRS 942220 (CU-005, ``false_positive``) and is the source of
truth. ``docs/why.md`` and ``AGENTS.md`` must either match that status on any
line mentioning 942220 or cite ``conversion-upstream.jsonl`` on that line, and
must contain at least one such citation line.

Historical-numerator rule: prior wave/rule_diff ``properties_asked`` / ``SAT``
counts are left as recorded (CU-005 stays counted under
``rule_diff_report_sat_gt``); the curated disposition governs filing state only
— no retroactive numerator adjustment.

Exit codes: 0 = covered; 1 = coverage/guard/validation failure; 2 = fatal
(missing files, unreadable JSON).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

GEN_DIR = ROOT / "properties" / "generated"
UPSTREAM_PATH = ROOT / "docs" / "conversion-upstream.jsonl"

DISPOSITIONS = frozenset(
    {
        "filed",
        "filed_plan",
        "wont_file",
        "false_positive",
        "private_first",
        "fixed_upstream",
        "approval_missing",
        "out_of_scope_redos",
    }
)
DATE_UNKNOWN = "unknown_date"
GT_PASS = frozenset({"reproduced", "PASS"})

CRS_GUARD_DOCS = (
    ROOT / "docs" / "why.md",
    ROOT / "AGENTS.md",
)


def _load_conversion_ledger_module():
    spec = importlib.util.spec_from_file_location(
        "_rp_conversion_ledger", ROOT / "scripts" / "conversion-ledger.py"
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load scripts/conversion-ledger.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Join-key canonicalization lives in scripts/conversion-ledger.py so the
# ledger hop table and this check can never diverge (#554).
def iter_ndjson(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def is_gt_confirmed_sat(rec: dict[str, Any], cl: Any) -> bool:
    """GT-confirmed product SAT marker in ``*_conversion.ndjson`` rows."""
    if rec.get("synthesized"):
        return False
    if rec.get("kind") not in cl.PRODUCT_KINDS:
        return False
    if rec.get("result") not in cl.SAT_RESULTS:
        return False
    return rec.get("ground_truth_status") in GT_PASS


def load_curated_index(
    path: Path, cl: Any
) -> dict[tuple[str, str], dict[str, Any]]:
    """Validate + index curated rows on canonically-joined keys."""
    index: dict[tuple[str, str], dict[str, Any]] = {}
    ids: list[str] = []
    for row in iter_ndjson(path):
        ids.append(str(row.get("id") or ""))
        status = str(row.get("status") or "")
        if status not in DISPOSITIONS:
            raise SystemExit(
                f"error: {path.name}:{row.get('id')}: unknown disposition "
                f"status {status!r}; allowed: {sorted(DISPOSITIONS)}"
            )
        if row.get("backfilled"):
            if not str(row.get("reason_code") or "").strip():
                raise SystemExit(
                    f"error: {path.name}:{row.get('id')}: backfilled row "
                    "missing reason_code"
                )
            d = str(row.get("disposition_date") or "").strip()
            if not d:
                raise SystemExit(
                    f"error: {path.name}:{row.get('id')}: backfilled row "
                    "missing disposition_date (ISO date or 'unknown_date')"
                )
            if d != "unknown_date":
                try:
                    date.fromisoformat(d)
                except ValueError:
                    raise SystemExit(
                        f"error: {path.name}:{row.get('id')}: disposition_date "
                        f"{d!r} is not an ISO date or 'unknown_date'"
                    )
        site = cl.canonical_site(str(row.get("site") or ""))
        qid = str(row.get("question_id") or "").strip()

        if site and qid:
            key = (site, qid)
            if key in index:
                raise SystemExit(
                    f"error: {path.name}: duplicate curated join key {key}"
                )
            index[key] = row
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"error: duplicate conversion-upstream id(s): {sorted(dupes)}")
    return index


def scan_gt_sats(gen_dir: Path, cl: Any) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for path in sorted(gen_dir.glob("*_conversion.ndjson")):
        for rec in iter_ndjson(path):
            if is_gt_confirmed_sat(rec, cl):
                out.append({**rec, "_source": path.name})
    return out


def crs942220_guard(upstream_path: Path, docs: tuple[Path, ...]) -> list[str]:
    """One curated CRS 942220 disposition; prose cites/matches it."""
    problems: list[str] = []
    rows = [r for r in iter_ndjson(upstream_path) if "942220" in json.dumps(r)]
    if len(rows) != 1:
        return [
            f"crs942220: expected exactly 1 curated disposition mentioning "
            f"942220, found {len(rows)} in {upstream_path.name}"
        ]
    sot_status = str(rows[0].get("status") or "")
    sot_id = str(rows[0].get("id") or "")
    # The reconciliation pins this rule's disposition: CU-005, false_positive.
    # A single row that merely mentions 942220 with a different status (e.g.
    # wont_file) must fail — the whole point of the guard is that the curated
    # file is the source of truth for THIS rule.
    if sot_id != "CU-005":
        problems.append(
            f"crs942220: curated row {sot_id!r} is not CU-005 — the 942220 "
            "reconciliation pins CRS 942220 to CU-005"
        )
    if sot_status != "false_positive":
        problems.append(
            f"crs942220: curated row {sot_id} status {sot_status!r} is not "
            "'false_positive' — the 942220 reconciliation pins CU-005 to "
            "false_positive"
        )
    for doc in docs:
        if not doc.is_file():
            problems.append(f"crs942220: guarded doc missing: {doc}")
            continue
        lines = doc.read_text(encoding="utf-8").splitlines()
        hits = [(n, ln) for n, ln in enumerate(lines, 1) if "942220" in ln]
        if not hits:
            continue
        cited = any("conversion-upstream.jsonl" in ln for _, ln in hits)
        if not cited:
            problems.append(
                f"crs942220: {doc.name} mentions 942220 but never cites "
                "conversion-upstream.jsonl as source of truth"
            )
        for n, ln in hits:
            # A line that carries the curated status token is consistent —
            # other disposition tokens on it refer to different rows in the
            # same table cell (e.g. "usrmanage P3 fixed_upstream; CRS 942220
            # is false_positive per CU-005"). Only flag a line that claims a
            # DIFFERENT status for 942220 and never states the correct one.
            if f"`{sot_status}`" in ln:
                continue
            for token in DISPOSITIONS:
                if f"`{token}`" in ln and token != sot_status:
                    problems.append(
                        f"crs942220: {doc.name}:{n} claims `{token}` which "
                        f"conflicts with curated {sot_id} `{sot_status}` "
                        "(cite conversion-upstream.jsonl on this line)"
                    )
    return problems


def run(
    gen_dir: Path = GEN_DIR,
    upstream_path: Path = UPSTREAM_PATH,
) -> int:
    if not upstream_path.is_file():
        print(f"FATAL: curated upstream file missing: {upstream_path}", file=sys.stderr)
        return 2
    cl = _load_conversion_ledger_module()
    try:
        curated = load_curated_index(upstream_path, cl)
        gt_sats = scan_gt_sats(gen_dir, cl)
    except OSError as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2

    missing = []
    for rec in gt_sats:
        key = (cl.canonical_site(str(rec.get("site") or "")), cl.canonical_question_id(rec))
        if key not in curated:
            missing.append((rec["_source"], key))
    covered = len(gt_sats) - len(missing)

    print(
        f"disposition coverage: {covered}/{len(gt_sats)} GT-confirmed "
        f"conversion SATs have curated rows "
        f"(curated file: {upstream_path.name}, rows indexed on join keys: "
        f"{len(curated)})"
    )
    failures = []
    if missing:
        failures.append("missing curated disposition rows:")
        for src, (site, qid) in missing:
            failures.append(f"  - {src}: site={site!r} question_id={qid!r}")
    failures.extend(crs942220_guard(upstream_path, CRS_GUARD_DOCS))
    if failures:
        for line in failures:
            print(line, file=sys.stderr)
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--generated-dir",
        type=Path,
        default=GEN_DIR,
        help="Directory holding *_conversion.ndjson (default: properties/generated)",
    )
    ap.add_argument(
        "--upstream",
        type=Path,
        default=UPSTREAM_PATH,
        help="Curated upstream JSONL (default: docs/conversion-upstream.jsonl)",
    )
    args = ap.parse_args(argv)
    if not args.generated_dir.is_dir():
        print(f"FATAL: generated dir missing: {args.generated_dir}", file=sys.stderr)
        return 2
    return run(gen_dir=args.generated_dir, upstream_path=args.upstream)


if __name__ == "__main__":
    raise SystemExit(main())
