#!/usr/bin/env python3
"""Author a schema-valid corpus gate decision from a probe draft (P3 / #132).

Usage:
  python scripts/author-gate-decision.py DRAFT --human --decision go --rationale '...'
  python scripts/author-gate-decision.py DRAFT --auto -o out.json
  python scripts/author-gate-decision.py --audit-sample --ledger PATH --week YYYY-Www
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.admission.author import (
    AuthorError,
    author_auto,
    author_human,
    default_output_path,
    emit_decision_text,
    load_probe_draft,
)
from regexproof.admission.auto_nogo import AutoNoGoError
from regexproof.admission.templates import TemplateError
from regexproof.mine.audit import (
    mark_auto_filed,
    mark_human_resolved,
    mark_needs_human_review,
    run_audit_sampler,
)


def _parse_evidence(items: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in items:
        if "=" not in raw:
            raise SystemExit(f"error: --evidence expects ID=TEXT, got {raw!r}")
        cid, text = raw.split("=", 1)
        out[cid.strip()] = text
    return out


def _parse_related(raw: str | None) -> dict | None:
    if raw is None:
        return None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise SystemExit(f"error: --related must be JSON: {e}") from e
    if not isinstance(data, dict):
        raise SystemExit("error: --related must be a JSON object")
    return data


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "probe_draft",
        nargs="?",
        type=Path,
        help="Path to flagged probe draft JSON",
    )
    ap.add_argument("--human", action="store_true", help="Human authoring mode")
    ap.add_argument("--auto", action="store_true", help="Restricted auto-NO-GO mode")
    ap.add_argument(
        "--audit-sample",
        action="store_true",
        help="Weekly audit sampler over auto-filed ledger entries",
    )
    ap.add_argument(
        "--llm-draft",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    ap.add_argument(
        "--decision",
        choices=["go", "no-go", "triage-trial"],
        help="Admission decision (human mode)",
    )
    ap.add_argument("--rationale", default=None, help="Free-form rationale")
    ap.add_argument(
        "--template",
        default=None,
        choices=["new-surface", "security-boundary", "below-scale", "repo-moved"],
        help="Deterministic rationale template",
    )
    ap.add_argument(
        "--met",
        action="append",
        default=[],
        metavar="ID",
        help="Mark condition met (repeatable)",
    )
    ap.add_argument(
        "--evidence",
        action="append",
        default=[],
        metavar="ID=TEXT",
        help="Evidence override for a condition",
    )
    ap.add_argument(
        "--decision-basis",
        choices=["admission_conditions", "grandfathered", "escape_hatch"],
        default=None,
    )
    ap.add_argument(
        "--escape-hatch",
        action="store_true",
        help="Set escape_hatch_applied=true",
    )
    ap.add_argument("--related", default=None, help="JSON object for related metadata")
    ap.add_argument("-o", "--output", type=Path, help="Write decision JSON here")
    ap.add_argument("--ledger", type=Path, help="Candidate ledger path")
    ap.add_argument(
        "--now",
        default=None,
        help="Inject decision_date as YYYY-MM-DD (determinism)",
    )
    ap.add_argument("--week", default=None, help="ISO week YYYY-Www for --audit-sample")
    ap.add_argument("--seed", type=int, default=None, help="RNG seed for sampler")
    ap.add_argument(
        "--fail-url",
        action="append",
        default=[],
        metavar="URL",
        help="Simulate sampler failure for URL (repeatable)",
    )
    args = ap.parse_args(argv)

    if args.llm_draft:
        print(
            "error: --llm-draft is deferred to #134 (P3b); not available in P3 v1",
            file=sys.stderr,
        )
        return 2

    if args.audit_sample:
        if not args.ledger:
            ap.error("--audit-sample requires --ledger")
        if not args.week:
            ap.error("--audit-sample requires --week YYYY-Www")
        ledger_path = args.ledger.expanduser().resolve()
        result = run_audit_sampler(
            ledger_path,
            week=args.week,
            seed=args.seed,
            fail_urls=set(args.fail_url),
        )
        sys.stdout.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
        return 0

    modes = sum(bool(x) for x in (args.human, args.auto))
    if modes != 1:
        ap.error("exactly one of --human or --auto is required (or --audit-sample)")
    if not args.probe_draft:
        ap.error("probe draft path is required")

    draft_path = args.probe_draft.expanduser().resolve()
    try:
        draft = load_probe_draft(draft_path)
    except (OSError, json.JSONDecodeError, AuthorError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    decision_date = date.fromisoformat(args.now) if args.now else None
    related = _parse_related(args.related)
    ledger_path = args.ledger.expanduser().resolve() if args.ledger else None

    try:
        if args.auto:
            decision = author_auto(draft, decision_date=decision_date)
        else:
            if not args.decision:
                ap.error("--human requires --decision")
            decision = author_human(
                draft,
                decision=args.decision,
                rationale=args.rationale,
                template=args.template,
                met=set(args.met),
                evidence=_parse_evidence(args.evidence),
                decision_basis=args.decision_basis,
                escape_hatch_applied=args.escape_hatch,
                related=related,
                decision_date=decision_date,
            )
    except AutoNoGoError as e:
        print(f"error: {e}", file=sys.stderr)
        if ledger_path is not None:
            url = str(draft.get("candidate_url") or "")
            if url:
                try:
                    mark_needs_human_review(ledger_path, url, reason=str(e))
                except ValueError:
                    pass
        return 1
    except (AuthorError, TemplateError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    out = (
        args.output.expanduser().resolve()
        if args.output
        else default_output_path(str(decision["corpus"]), repo_root=ROOT)
    )

    # Ledger first when requested so we never exit 0 with a written decision
    # but a failed auto_filed / human_resolved sync.
    if ledger_path is not None:
        url = str(decision.get("candidate_url") or "")
        if not url:
            print("error: decision missing candidate_url for ledger update", file=sys.stderr)
            return 1
        try:
            if args.auto:
                mark_auto_filed(ledger_path, url, template_fired="below-scale")
            else:
                mark_human_resolved(
                    ledger_path, url, decision=str(decision.get("decision"))
                )
        except ValueError as e:
            print(f"error: ledger update failed: {e}", file=sys.stderr)
            return 1

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(emit_decision_text(decision), encoding="utf-8")

    # Print absolute output path for runners / review dispatch.
    print(str(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
