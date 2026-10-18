#!/usr/bin/env python3
"""Wave B (#556): record a filing/approval disposition for a curated row.

The human-approval filing path for GT-confirmed SATs. Appends or updates a
row in ``docs/conversion-upstream.jsonl`` with a disposition (status +
reason + dates) validated against the same rules the coverage checker
enforces, so a recorded decision can never make CI fail.

Usage::

  python3 scripts/record-filing-decision.py --id CU-015 \\
      --status filed --reason "opened upstream issue" --filed-at 2026-08-23

  # fixed_upstream can record via --resolved-at (checker accepts either):
  python3 scripts/record-filing-decision.py --id CU-001 \\
      --status fixed_upstream --reason "upstream fixed" --resolved-at 2026-08-23

  # approval_missing REQUIRES an escape (never a dead-end label):
  python3 scripts/record-filing-decision.py --id CU-016 \\
      --status approval_missing --approval-escape approval_present \\
      --approval-ref .approvals/CU-016.json
  python3 scripts/record-filing-decision.py --id CU-016 \\
      --status approval_missing --approval-escape wont_file \\
      --reason-code "maintainer declined; in-repo mitigation"

Exit 0 on success; nonzero with a message when the row is unknown or the
disposition violates the schema.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
CURATED = ROOT / "docs" / "conversion-upstream.jsonl"

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
FILING_STATUSES = frozenset({"filed", "filed_plan", "private_first", "fixed_upstream"})
APPROVAL_ESCAPES = frozenset({"approval_present", "wont_file"})


def load_rows(path: pathlib.Path) -> list[dict]:
    if not path.is_file():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def find_row(rows: list[dict], row_id: str) -> dict | None:
    for r in rows:
        if str(r.get("id") or "") == row_id:
            return r
    return None


def validate_disposition(
    row_id: str,
    status: str,
    filed_at: str,
    resolved_at: str,
    reason: str,
    reason_code: str,
    approval_escape: str,
    approval_ref: str,
) -> None:
    if status not in DISPOSITIONS:
        sys.exit(f"error: unknown disposition status {status!r}; allowed: {sorted(DISPOSITIONS)}")
    filed_at = filed_at.strip()
    resolved_at = resolved_at.strip()
    reason = reason.strip()
    reason_code = reason_code.strip()
    approval_escape = approval_escape.strip()
    approval_ref = approval_ref.strip()
    # The checker accepts filed_at OR resolved_at for filing statuses.
    if status in FILING_STATUSES and not filed_at and not resolved_at:
        sys.exit(
            f"error: {row_id}: filing status {status!r} requires --filed-at "
            "or --resolved-at (ISO date)"
        )
    for label, val in (("--filed-at", filed_at), ("--resolved-at", resolved_at)):
        if val:
            try:
                date.fromisoformat(val)
            except ValueError:
                sys.exit(
                    f"error: {row_id}: {label} {val!r} is not an ISO date "
                    "(the coverage checker rejects it — record a valid date)"
                )
    reason_required = not (
        status == "approval_missing"
        and approval_escape == "approval_present"
        and approval_ref
    )
    if reason_required and not reason and not reason_code:
        sys.exit(f"error: {row_id}: provide --reason or --reason-code")
    if status == "approval_missing":
        if approval_escape not in APPROVAL_ESCAPES:
            sys.exit(
                f"error: {row_id}: approval_missing requires --approval-escape "
                f"({sorted(APPROVAL_ESCAPES)})"
            )
        if approval_escape == "approval_present" and not approval_ref:
            sys.exit(
                f"error: {row_id}: approval-escape approval_present requires "
                "--approval-ref (approval file path or issue/PR reference)"
            )
        if approval_escape == "wont_file" and not reason_code:
            sys.exit(
                f"error: {row_id}: approval-escape wont_file requires --reason-code"
            )


def load_gt_sat(site: str, question_id: str, generated_dir: pathlib.Path) -> dict:
    """Return the unique GT-confirmed SAT matching the requested join key."""
    checker_path = pathlib.Path(__file__).with_name("check-disposition-coverage.py")
    spec = importlib.util.spec_from_file_location("_filing_coverage_checker", checker_path)
    if spec is None or spec.loader is None:
        sys.exit("error: cannot load disposition coverage checker")
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    cl = checker._load_conversion_ledger_module()
    requested = (cl.canonical_site(site), question_id.strip())
    matches = []
    for source in sorted(generated_dir.glob("*_conversion.ndjson")):
        for row in checker.iter_ndjson(source):
            key = (cl.canonical_site(str(row.get("site") or "")), cl.canonical_question_id(row))
            if key == requested and checker.is_gt_confirmed_sat(row, cl):
                matches.append((row, source.name))
    if len(matches) != 1:
        sys.exit(
            f"error: expected exactly one GT-confirmed SAT for site/question_id; "
            f"found {len(matches)} (generated dir {generated_dir})"
        )
    row, _source = matches[0]
    return row


def next_curated_id(rows: list[dict]) -> str:
    numbers = []
    for row in rows:
        candidate = str(row.get("id") or "")
        if candidate.startswith("CU-") and candidate[3:].isdigit():
            numbers.append(int(candidate[3:]))
    return f"CU-{max(numbers, default=0) + 1:03d}"


def upsert_row(rows: list[dict], row: dict, *, on_duplicate: str = "update") -> list[dict]:
    """Insert or update, keeping the row at its existing position."""
    for i, existing in enumerate(rows):
        if str(existing.get("id") or "") == str(row.get("id") or ""):
            if on_duplicate == "update":
                merged = dict(existing)
                merged.update({k: v for k, v in row.items() if v is not None})
                rows[i] = merged
            return rows
    rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--id", help="Existing curated row id (CU-xxx); omit with --site/--question-id to add a new GT SAT")
    ap.add_argument("--site", help="Canonical scanner site for creating/updating a GT SAT disposition")
    ap.add_argument("--question-id", help="Stable property question/name for --site")
    ap.add_argument("--class", dest="corpus_class", choices=("own_code", "third_party", "third_party_security_tool"), help="Human-reviewed corpus classification required when creating a new row")
    ap.add_argument("--generated-dir", type=pathlib.Path, default=ROOT / "properties" / "generated", help=argparse.SUPPRESS)
    ap.add_argument("--status", required=True, help="Disposition status")
    ap.add_argument("--reason", default="", help="Human-readable reason")
    ap.add_argument("--reason-code", default="", help="Machine reason code (required for some escapes)")
    ap.add_argument("--filed-at", default="", help="ISO filing date (required for filing statuses unless --resolved-at)")
    ap.add_argument("--resolved-at", default="", help="ISO resolution date (alternative filing-status date; checker accepts either)")
    ap.add_argument("--approval-escape", default="", choices=sorted(APPROVAL_ESCAPES))
    ap.add_argument("--approval-ref", default="", help="Approval file path or issue/PR ref")
    ap.add_argument("--curated", type=pathlib.Path, default=CURATED, help=argparse.SUPPRESS)
    args = ap.parse_args(argv)

    path = args.curated.expanduser().resolve()
    rows = load_rows(path)
    if args.id:
        if args.site or args.question_id:
            sys.exit("error: use either --id or --site/--question-id, not both")
        existing = find_row(rows, args.id)
        if existing is None:
            sys.exit(f"error: no curated row with id {args.id!r} in {path.name}")
        row_id = args.id
        base_row = existing
    else:
        if not args.site or not args.question_id:
            sys.exit("error: provide --id or both --site and --question-id")
        sat = load_gt_sat(args.site, args.question_id, args.generated_dir.expanduser().resolve())
        requested_key = (args.site.strip(), args.question_id.strip())
        matching_existing = [
            row for row in rows
            if (str(row.get("site") or "").strip(), str(row.get("question_id") or "").strip()) == requested_key
        ]
        if len(matching_existing) > 1:
            sys.exit("error: multiple curated rows already match the supplied site/question_id")
        if matching_existing:
            base_row = matching_existing[0]
            row_id = str(base_row.get("id") or "")
        else:
            if not args.corpus_class:
                sys.exit("error: creating a new disposition requires --class (human-reviewed corpus classification)")
            base_row = {
                "id": next_curated_id(rows),
                "corpus": sat.get("corpus"),
                "kind": sat.get("kind"),
                "language_membership": True,
                "site": str(sat.get("site") or "").strip(),
                "question_id": str(sat.get("question_id") or sat.get("name") or "").strip(),
                "wave_id": sat.get("wave_id"),
                "idiom_bucket": sat.get("idiom_bucket"),
                "issue": None,
                "class": args.corpus_class,
                "summary": str(sat.get("domain") or sat.get("name") or sat.get("question_id") or ""),
            }
            row_id = base_row["id"]

    validate_disposition(
        row_id,
        args.status,
        args.filed_at,
        args.resolved_at,
        args.reason,
        args.reason_code,
        args.approval_escape,
        args.approval_ref,
    )

    update: dict = {**base_row, "id": row_id, "status": args.status}
    if args.reason.strip():
        update["reason"] = args.reason.strip()
    if args.reason_code.strip():
        update["reason_code"] = args.reason_code.strip()
    if args.filed_at.strip():
        update["filed_at"] = args.filed_at.strip()
    if args.resolved_at.strip():
        update["resolved_at"] = args.resolved_at.strip()
    if args.approval_escape.strip():
        update["approval_escape"] = args.approval_escape.strip()
    if args.approval_ref.strip():
        update["approval_ref"] = args.approval_ref.strip()
    rows = upsert_row(rows, update)

    path.write_text(
        "".join(json.dumps(r, sort_keys=True) + "\n" for r in rows),
        encoding="utf-8",
    )
    print(f"recorded {row_id}: {args.status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
