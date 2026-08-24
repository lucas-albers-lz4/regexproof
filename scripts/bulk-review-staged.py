#!/usr/bin/env python3
"""Wave 3 (#560): staged bulk review CLI.

Drives the REAL pipeline for staged probe drafts:
- go / triage-trial → ``author_human`` (schema-validated: conditions,
  rationale, decision_basis, escape_hatch; fork-duplicate refusal; jsonschema
  gate). HUMAN provenance + reviewer REQUIRED.
- no-go → ``author_auto`` (deterministic below-scale; never emits
  go/triage-trial/repo-moved on the auto path — pytest invariant).
- Decisions are written to ``properties/generated/<corpus>_gate_decision.json``
  via the shared output path, and the candidate ledger's audit object records
  ``promoted_via: "bulk-review"`` + ``promoted_at`` so the weekly audit sampler
  includes bulk-CLI-promoted decisions (and excludes provenance=stub at
  schema level).
- requeue → transition_candidate(to="queued") + archive the gate decision
  (read-only sync cannot reapply it) + release any cache lease.
- demote-retain-corpus → release the cache lease; retained location recorded
  in the ledger row; the corpus stays materialized.

Usage::

  python3 scripts/bulk-review-staged.py --draft path/to/draft.json \\
      --go --reviewer alice --rationale '...' --conditions-ok \\
      --ledger properties/generated/candidate-ledger.json

  python3 scripts/bulk-review-staged.py --draft path/to/draft.json \\
      --no-go   # deterministic auto path, no reviewer needed

  python3 scripts/bulk-review-staged.py --draft path/to/draft.json \\
      --requeue --reason audit-sampler-fail
"""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from regexproof.admission.author import (  # noqa: E402
    CONDITION_IDS,
    AuthorError,
    author_auto,
    author_human,
    default_output_path,
)
from regexproof.mine import audit, lease_registry, transition  # noqa: E402
from regexproof.mine.ledger import find_candidate  # noqa: E402

GEN = ROOT / "properties" / "generated"


def _utc_ts(dt: datetime.datetime | None = None) -> str:
    """Canonical audit timestamp: aware UTC, %Y-%m-%dT%H:%M:%SZ
    (CodeRabbit #573: utcnow() is deprecated on 3.12 and isoformat() of a
    naive datetime diverges from ensure_candidate_audit's format)."""
    if dt is not None:
        return dt.replace(tzinfo=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_draft(draft_path: pathlib.Path) -> dict:
    """Load a staged probe draft; refuse queue stubs structurally (Luna r1
    #2: provenance=stub is queue-only and can never be promoted)."""
    from regexproof.admission.author import load_probe_draft

    draft = load_probe_draft(draft_path)
    if str(draft.get("provenance") or "") == "stub":
        raise SystemExit(
            f"bulk-review: {draft_path.name} is a queue stub (provenance=stub) "
            "— stubs are queue-only and cannot be promoted"
        )
    return draft


def _url_of(draft: dict) -> str:
    url = str(draft.get("candidate_url") or draft.get("url") or "")
    if not url:
        raise SystemExit("bulk-review: draft has no candidate_url/url")
    return url


def _release_lease(url: str, cache_root: pathlib.Path | None = None) -> None:
    """Release EVERY live lease for the URL (Luna r2 High: leases require
    the exact pin AND owning PID — release(url, '', 0) matches nothing, so
    normal leases would linger until stale cleanup). Honors a custom
    --cache-root (Luna r3 Medium: batch-probe --cache-root stores leases at
    <cache-root>/leases.json, NOT the default cache/leases.json)."""
    registry_path = (cache_root / "leases.json") if cache_root else None
    leases = lease_registry.active_leases(path=registry_path)
    for lease in leases:
        if str(lease.get("url") or "") == url:
            lease_registry.release(
                url, str(lease.get("pin") or ""),
                owner_pid=int(lease.get("owner_pid") or -1),
            )


def _reviewer_required(args, verb: str) -> None:
    if not str(args.reviewer or "").strip():
        raise SystemExit(f"bulk-review: {verb} requires --reviewer")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--draft", type=pathlib.Path, required=True,
                    help="staged probe draft JSON (probe-shaped)")
    ap.add_argument("--ledger", type=pathlib.Path,
                    default=GEN / "candidate-ledger.json")
    ap.add_argument("--reviewer", default="")
    ap.add_argument("--rationale", default=None)
    ap.add_argument("--decision-basis", default=None)
    ap.add_argument("--conditions-ok", action="store_true",
                    help="mark ALL admission conditions met (human go)")
    ap.add_argument("--evidence", action="append", default=[],
                    help="--evidence <cid>=<value> for each met condition "
                         "(required by the author path)")
    ap.add_argument("--escape-hatch", action="store_true",
                    help="explicit escape-hatch graduation (human-owned)")
    ap.add_argument("--at", default="",
                    help="ISO decision clock for determinism")
    ap.add_argument("--reason", default="")
    ap.add_argument("--retained-location", default="")
    ap.add_argument("--cache-root", type=pathlib.Path, default=None,
                    help="cache root whose leases.json holds this probe's "
                         "lease (batch-probe --cache-root)")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--go", action="store_true")
    group.add_argument("--no-go", dest="no_go", action="store_true")
    group.add_argument("--triage-trial", dest="triage_trial", action="store_true")
    group.add_argument("--requeue", action="store_true")
    group.add_argument("--demote-retain-corpus", action="store_true")
    args = ap.parse_args(argv)

    draft = _load_draft(args.draft)
    url = _url_of(draft)
    corpus = str(draft.get("corpus") or "")

    # Validate --at ONCE, before the verb branches (CodeRabbit #573): a
    # malformed value must fail early and consistently — not as an authoring
    # traceback, and never reaching audit timestamps as a raw string.
    at_dt = None
    if args.at:
        try:
            at_dt = datetime.datetime.strptime(args.at, "%Y-%m-%dT%H:%M:%S")
        except ValueError as exc:
            raise SystemExit(
                f"bulk-review: --at must be ISO YYYY-MM-DDTHH:MM:SS ({exc})"
            ) from exc
    # Audit Clock expects datetime (UTC); author decision_date expects date.
    clock = (lambda: at_dt.replace(tzinfo=datetime.timezone.utc)) if at_dt else None

    if args.requeue:
        # Requeue: transition via the P2-owned API + archive the decision so
        # the read-only sync cannot reapply it (Luna r1 #1). The archive
        # must match by DECISION CONTENT (candidate_url), not filename —
        # filename globs are ambiguous (Luna r3: '*{safe}_gate_decision.json'
        # archived unrelated 'other_acme_packages_gate_decision.json').
        transition.transition_candidate(
            args.ledger, url, to="queued", reason=args.reason or "bulk-review-requeue",
        )
        # CodeRabbit #573: --requeue --retained-location ... must NOT be
        # silently dropped — record it on the ledger row when provided.
        if args.retained_location:
            from regexproof.mine.ledger import load_ledger, save_ledger

            ledger = load_ledger(args.ledger)
            cand = find_candidate(ledger, url)
            if cand is None:
                raise SystemExit(
                    f"bulk-review: requeue refused — {url} not in ledger"
                )
            cand["retained_location"] = args.retained_location
            save_ledger(args.ledger, ledger)
        from regexproof.mine.exclusions import normalize_repo_url

        archived = 0
        target = normalize_repo_url(url)
        for f in sorted(GEN.glob("*_gate_decision.json")):
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if normalize_repo_url(str(d.get("candidate_url") or "")) != target:
                continue
            f.rename(f.with_name(f.name.replace("_gate_decision.json", ".gate_decision.requeued.json")))
            archived += 1
        _release_lease(url, cache_root=args.cache_root)
        print(f"requeue: {url} archived={archived}")
        return 0

    if args.demote_retain_corpus:
        # Demote: release the cache lease; corpus stays materialized; the
        # retained location is recorded in the ledger row (Luna r1 #1).
        from regexproof.mine.ledger import load_ledger, save_ledger

        ledger = load_ledger(args.ledger)
        cand = find_candidate(ledger, url)
        if cand is None:
            raise SystemExit(
                f"bulk-review: demote refused — {url} not in ledger "
                "(Luna r2: demotion must not silently succeed without "
                "required state)"
            )
        cand["status"] = "demoted"
        if args.retained_location:
            cand["retained_location"] = args.retained_location
        else:
            raise SystemExit(
                "bulk-review: demote requires --retained-location (the "
                "retained location must be recorded in the ledger row)"
            )
        audit_obj = cand.setdefault("audit", {})
        if not isinstance(audit_obj, dict):
            raise SystemExit("bulk-review: candidate audit must be an object")
        audit_obj["demoted_at"] = (
            _utc_ts(at_dt) if at_dt is not None else _utc_ts()
        )
        save_ledger(args.ledger, ledger)
        _release_lease(url, cache_root=args.cache_root)
        print(f"demote_retain_corpus: {url} retained={args.retained_location}")
        return 0

    # go / triage-trial / no-go — the schema-valid authoring path.
    decision = "go" if args.go else ("triage-trial" if args.triage_trial else "no-go")
    if decision in ("go", "triage-trial"):
        _reviewer_required(args, decision)
        if not args.rationale:
            raise SystemExit(f"bulk-review: {decision} requires --rationale")
        if not args.conditions_ok:
            raise SystemExit(
                f"bulk-review: {decision} requires --conditions-ok (all "
                "admission conditions met by a human reviewer)"
            )
        try:
            evidence: dict[str, str] = {}
            for item in args.evidence:
                if "=" not in item:
                    raise SystemExit(
                        f"bulk-review: --evidence must be cid=value, got {item!r}"
                    )
                cid, _, value = item.partition("=")
                evidence[cid] = value
            out = author_human(
                draft,
                decision=decision,
                rationale=args.rationale,
                decision_basis=args.decision_basis or "admission_conditions",
                met=set(CONDITION_IDS) if args.conditions_ok else set(),
                evidence=evidence,
                escape_hatch_applied=args.escape_hatch,
                decision_date=(clock().date() if clock else None),
            )
        except AuthorError as exc:
            raise SystemExit(f"bulk-review: authoring refused: {exc}")
    else:
        try:
            out = author_auto(
                draft,
                decision_date=(clock().date() if clock else None),
                generated_dir=GEN,
            )
        except AuthorError as exc:
            raise SystemExit(f"bulk-review: auto authoring refused: {exc}")

    # Persist the schema-validated decision + audit-promote the ledger row.
    out_path = default_output_path(corpus, repo_root=ROOT)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    # Only HUMAN decisions (go/triage-trial) are bulk-promoted — auto no-go
    # is deterministic and must NOT join the sampler population via
    # promoted_via (Luna r2: promotion provenance is for human decisions).
    # Auto no-go goes through mark_auto_filed(), which rejects candidates
    # flagged re_evaluate=true (Luna r3: a direct auto_filed=True write
    # bypassed the mandatory human re-review gate).
    if decision != "no-go":
        promote_updates = {
            "promoted_via": "bulk-review",
            "promoted_at": (_utc_ts(at_dt) if at_dt is not None else _utc_ts()),
        }
    else:
        try:
            audit.mark_auto_filed(
                args.ledger, url,
                clock=clock if clock is not None else None,
            )
        except ValueError as exc:
            raise SystemExit(f"bulk-review: auto-filing refused: {exc}") from exc
        print(f"no_go: {url} -> {out_path.name} (provenance=auto)")
        return 0
    try:
        audit.ensure_candidate_audit(
            args.ledger, url, updates=promote_updates,
        )
    except ValueError as exc:
        # Luna r2 P0: a missing ledger candidate must FAIL CLOSED — a
        # decision written without audit provenance is not sampler-eligible
        # and must not look like a successful promotion.
        raise SystemExit(
            f"bulk-review: ledger promotion failed for {url}: {exc} — "
            "decision written but NOT promoted (audit provenance missing)"
        ) from exc

    print(f"{decision}: {url} -> {out_path.name} (provenance=human)" if decision != "no-go"
          else f"no_go: {url} -> {out_path.name} (provenance=auto)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
