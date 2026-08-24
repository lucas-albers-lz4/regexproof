#!/usr/bin/env python3
"""Author a schema-valid corpus gate decision from a probe draft (P3 / P3b).

Usage:
  python scripts/author-gate-decision.py DRAFT --human --decision go --rationale '...'
  python scripts/author-gate-decision.py DRAFT --auto -o out.json
  python scripts/author-gate-decision.py DRAFT --llm-draft -o out.json
  python scripts/author-gate-decision.py --audit-sample --ledger PATH --week YYYY-Www
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.admission.author import (  # noqa: E402  # ROOT bootstrap above
    AuthorError,
    author_auto,
    author_human,
    default_output_path,
    emit_decision_text,
    load_probe_draft,
)
from regexproof.admission.auto_nogo import AutoNoGoError  # noqa: E402  # ROOT bootstrap above
from regexproof.admission.llm_client import (  # noqa: E402  # ROOT bootstrap above
    OpencodeDeepseekClassifier,
    RetryingClassifier,
    StaticClassifier,
)
from regexproof.admission.llm_draft import author_llm_draft  # noqa: E402  # ROOT bootstrap above
from regexproof.admission.templates import TemplateError  # noqa: E402  # ROOT bootstrap above
from regexproof.mine.audit import (  # noqa: E402  # ROOT bootstrap above
    append_model_call,
    mark_auto_filed,
    mark_human_resolved,
    mark_llm_template_fired,
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


def _audit_clock(now: date | None):
    if now is None:
        return None

    def _clock() -> datetime:
        return datetime(now.year, now.month, now.day, tzinfo=timezone.utc)

    return _clock


def _resolve_output(
    output: Path | None,
    corpus: str,
    *,
    allow_outside: bool,
) -> Path:
    """Default under properties/generated; explicit --output must stay there unless opted out."""
    generated = (ROOT / "properties" / "generated").resolve()
    if output is None:
        return default_output_path(corpus, repo_root=ROOT)
    out = output.expanduser().resolve()
    if not allow_outside and not out.is_relative_to(generated):
        raise ValueError(
            f"error: --output must be under properties/generated (got {out}); "
            "pass --allow-outside-generated to override"
        )
    return out


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
        "--llm-draft",
        action="store_true",
        help="LLM classify-then-template draft (never auto-files / never approves)",
    )
    ap.add_argument(
        "--audit-sample",
        action="store_true",
        help="Weekly audit sampler over auto-filed ledger entries",
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
    ap.add_argument(
        "--allow-outside-generated",
        action="store_true",
        help="Permit --output outside properties/generated (default: refuse)",
    )
    ap.add_argument("--ledger", type=Path, help="Candidate ledger path")
    ap.add_argument(
        "--active-minutes",
        type=float,
        default=None,
        help="Stopwatch active minutes for a human-reviewed survivor (Wave 6)",
    )
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
    ap.add_argument(
        "--classify-label",
        default=None,
        help="Test seam: fixed classifier label (skips live model)",
    )
    ap.add_argument(
        "--classify-fail-times",
        type=int,
        default=0,
        help="Test seam: fail the first N classify calls before succeeding",
    )
    args = ap.parse_args(argv)

    if args.active_minutes is not None and (
        args.active_minutes < 0 or not math.isfinite(args.active_minutes)
    ):
        ap.error("--active-minutes must be a finite number >= 0")
    if args.active_minutes is not None and not args.human:
        ap.error("--active-minutes applies only to --human go/triage-trial")
    if args.active_minutes is not None and args.human and args.decision is None:
        ap.error("--human requires --decision")
    if args.active_minutes is not None and args.decision not in ("go", "triage-trial"):
        ap.error("--active-minutes applies only to --human go/triage-trial")

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
            generated_dir=ROOT / "properties" / "generated",
        )
        sys.stdout.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
        return 0

    modes = sum(bool(x) for x in (args.human, args.auto, args.llm_draft))
    if modes != 1:
        ap.error(
            "exactly one of --human, --auto, or --llm-draft is required "
            "(or --audit-sample)"
        )
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
    clock = _audit_clock(decision_date)

    if args.llm_draft:
        test_seam = args.classify_label is not None or args.classify_fail_times > 0
        if test_seam:
            inner = StaticClassifier(
                args.classify_label,
                fail_times=args.classify_fail_times,
            )
            sleep_fn = lambda _s: None  # noqa: E731 — tests must not sleep 60s
        else:
            inner = OpencodeDeepseekClassifier()
            sleep_fn = time.sleep
        classifier = RetryingClassifier(inner, sleep_fn=sleep_fn)

        outcome = author_llm_draft(
            draft,
            classifier,
            related=related,
            decision_date=decision_date,
        )
        url = str(draft.get("candidate_url") or "")
        if ledger_path is not None and url and outcome.classification is not None:
            try:
                append_model_call(
                    ledger_path,
                    url,
                    outcome.classification.as_audit_call(),
                    clock=clock,
                )
            except ValueError as e:
                print(f"warning: model_call log skipped: {e}", file=sys.stderr)

        if outcome.needs_human_review or outcome.decision is None:
            print(f"error: {outcome.reason}", file=sys.stderr)
            if ledger_path is not None and url:
                try:
                    mark_needs_human_review(
                        ledger_path, url, reason=outcome.reason, clock=clock
                    )
                except ValueError:
                    pass
            return 1

        decision = outcome.decision
        try:
            out = _resolve_output(
                args.output,
                str(decision["corpus"]),
                allow_outside=args.allow_outside_generated,
            )
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 1
        if ledger_path is not None and url:
            try:
                mark_llm_template_fired(
                    ledger_path,
                    url,
                    template_fired=str(outcome.template_fired),
                    clock=clock,
                )
            except ValueError as e:
                print(f"error: ledger update failed: {e}", file=sys.stderr)
                return 1
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(emit_decision_text(decision), encoding="utf-8")
        print(str(out))
        return 0

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

    try:
        out = _resolve_output(
            args.output,
            str(decision["corpus"]),
            allow_outside=args.allow_outside_generated,
        )
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1

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
    print(str(out))
    if (
        args.human
        and args.active_minutes is not None
        and str(decision.get("decision") or "") in ("go", "triage-trial")
    ):
        from regexproof.mine.operator_minutes import append_row

        try:
            append_row(
                url=str(decision.get("candidate_url") or draft.get("candidate_url") or ""),
                pin=str(decision.get("corpus_pin") or draft.get("corpus_pin") or ""),
                decision=str(decision.get("decision")),
                source="stopwatch",
                active_minutes=args.active_minutes,
                decision_date=str(decision.get("decision_date") or ""),
            )
        except Exception as exc:
            print(f"warning: stopwatch row not recorded: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
