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
import os
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


def _validate_probe_identity(draft: dict, probe: dict, draft_url: str, name: str) -> None:
    """Final-gate #1 (HIGH): an EMBEDDED probe object must be bound to the
    draft candidate exactly like the inherit path. The real producer emits
    the URL only at DRAFT level (admission/draft.py) — the probe carries
    only a pin — so the binding anchor is the REVISION identity:
    - a draft carrying probe evidence MUST itself carry a pin (corpus_pin
      or pin) — a pin-less draft is unattributable (candidate B could
      inherit candidate A's probe with no way to detect it);
    - ALL pins present on both sides must agree.
    A mismatched/missing binding is refused (candidate B must never be
    reviewed with candidate A's evidence)."""
    from regexproof.mine.exclusions import normalize_repo_url

    probe_url = normalize_repo_url(
        str(probe.get("candidate_url") or probe.get("url") or "")
    )
    if probe_url and draft_url and probe_url != draft_url:
        raise SystemExit(
            f"bulk-review: {name} embeds probe evidence for {probe_url!r} but "
            f"the draft candidate is {draft_url!r} — refusing mismatched "
            "embedded probe evidence"
        )
    probe_pins = {str(p) for p in (probe.get("corpus_pin"), probe.get("pin")) if p}
    draft_pins = {
        str(p) for p in (draft.get("corpus_pin"), draft.get("pin")) if p
    }
    if probe_pins and not draft_pins:
        raise SystemExit(
            f"bulk-review: {name} embeds probe evidence carrying pins "
            f"{sorted(probe_pins)} but the draft carries NO pin — the "
            "revision identity is unattributable, refusing (candidate B "
            "must never inherit candidate A's probe)"
        )
    if not probe_url and not probe_pins:
        # CodeRabbit #583: a probe with NEITHER a url NOR a pin carries no
        # identity at all — it cannot be bound to any candidate and must
        # not be used as evidence.
        raise SystemExit(
            f"bulk-review: {name} embeds probe evidence with NO url and NO "
            "pin — the evidence is unbounded to any revision, refusing "
            "(authoring requires bound probe evidence)"
        )
    all_pins = probe_pins | draft_pins
    if len(all_pins) > 1:
        raise SystemExit(
            f"bulk-review: {name} embedded probe pins {sorted(probe_pins)} "
            f"do not match draft pins {sorted(draft_pins)} for {draft_url} — "
            "refusing mismatched embedded probe evidence"
        )


def _load_draft(draft_path: pathlib.Path) -> dict:
    """Load a staged probe draft; refuse queue stubs structurally (Luna r1
    #2: provenance=stub is queue-only and can never be promoted).

    Luna r5 #1: batch-probe.py emits LIGHTWEIGHT review stubs (url/pin/
    corpus, NO probe object) — the author path requires probe evidence
    (conditions, security_boundary, predicted_buckets). Resolve the probe
    from the pipeline's probe-decision artifact for the same corpus
    (``{corpus}_probe_decision.json``, then ``{corpus}_gate_decision.json``)
    so the producer→reviewer workflow works without an undocumented
    conversion step. Fail closed when no probe evidence exists.
    """
    try:
        draft = json.loads(draft_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit(f"bulk-review: cannot read draft {draft_path}: {exc}") from exc
    if not isinstance(draft, dict):
        raise SystemExit(f"bulk-review: {draft_path.name} must be a JSON object")
    if str(draft.get("provenance") or "") == "stub":
        raise SystemExit(
            f"bulk-review: {draft_path.name} is a queue stub (provenance=stub) "
            "— stubs are queue-only and cannot be promoted"
        )
    # Final-gate #1 (HIGH): probe identity MUST be validated for BOTH paths —
    # an EMBEDDED probe object is not trusted by presence alone; candidate B
    # carrying candidate A's probe evidence must be refused exactly like the
    # inherit path refuses mismatched evidence.
    from regexproof.mine.exclusions import normalize_repo_url

    draft_url = normalize_repo_url(str(draft.get("candidate_url") or draft.get("url") or ""))
    embedded_probe = draft.get("probe")
    if isinstance(embedded_probe, dict):
        # Luna r4 #1: an EMPTY probe dict ({}) is still an object — it has
        # no identity and must be refused, not silently treated as absent
        # (which would fall through to authoring with no evidence at all).
        if not embedded_probe:
            raise SystemExit(
                f"bulk-review: {draft_path.name} embeds an EMPTY probe object "
                "— no evidence, refusing (authoring requires bound probe "
                "evidence)"
            )
        _validate_probe_identity(draft, embedded_probe, draft_url, draft_path.name)
    if "probe" not in draft or not isinstance(draft.get("probe"), dict):
        corpus = str(draft.get("corpus") or "")
        # Luna r6 #1: probe evidence MUST be bound to the draft candidate —
        # corpus filename alone is not identity. Require the artifact's
        # candidate_url (+ pin when the draft carries one) to match, else
        # fail closed (a draft could otherwise inherit URL/pin A's evidence
        # while claiming to review URL/pin B).
        from regexproof.mine.exclusions import normalize_repo_url

        draft_url = normalize_repo_url(str(draft.get("candidate_url") or draft.get("url") or ""))
        probe_evidence: dict | None = None
        for candidate in (GEN / f"{corpus}_probe_decision.json",
                          GEN / f"{corpus}_gate_decision.json"):
            if not candidate.is_file():
                continue
            try:
                art = json.loads(candidate.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            art_url = normalize_repo_url(str(art.get("candidate_url") or ""))
            if not art_url or (draft_url and art_url != draft_url):
                continue  # wrong candidate — never inherit
            art_probe = art.get("probe")
            if not isinstance(art_probe, dict) or not art_probe:
                continue
            # Luna r7: pin binding checks EVERY pin on both sides — the
            # artifact's corpus_pin AND probe.pin, against the draft's
            # corpus_pin AND pin. If any pins are present, ALL of them must
            # agree; a single conflicting pin (even when another matches)
            # means evidence from a different revision — refuse.
            art_pins = {str(p) for p in (art.get("corpus_pin"), art_probe.get("pin"))
                        if p}
            draft_pins = {str(p) for p in (draft.get("corpus_pin"), draft.get("pin"))
                          if p}
            if art_pins and not draft_pins:
                # Luna r2 #1: pinned evidence must never be inherited by a
                # pin-less draft — the revision identity is unattributable
                # (same rule as the embedded-probe path).
                raise SystemExit(
                    f"bulk-review: {candidate.name} probe evidence carries "
                    f"pins {sorted(art_pins)} but the draft carries NO pin — "
                    f"the revision identity is unattributable, refusing to "
                    "inherit probe evidence"
                )
            all_pins = art_pins | draft_pins
            if len(all_pins) > 1:
                raise SystemExit(
                    f"bulk-review: {candidate.name} probe pins {sorted(art_pins)} "
                    f"do not match draft pins {sorted(draft_pins)} for "
                    f"{draft_url} — refusing to inherit mismatched probe evidence"
                )
            probe_evidence = art_probe
            break
        if probe_evidence is None:
            raise SystemExit(
                f"bulk-review: {draft_path.name} has no probe object and no "
                f"probe evidence for corpus {corpus!r} at url {draft_url!r} — "
                "run probe-corpus-admission.py first (authoring requires "
                "probe evidence)"
            )
        draft = dict(draft)
        draft["probe"] = probe_evidence
        # batch-probe stubs carry top-level url; the author path requires
        # candidate_url.
        if not draft.get("candidate_url") and draft.get("url"):
            draft["candidate_url"] = draft["url"]
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
                path=registry_path,  # Luna r4: release MUST target the same
                                     # registry that active_leases read
            )


def _reviewer_required(args, verb: str) -> None:
    if not str(args.reviewer or "").strip():
        raise SystemExit(f"bulk-review: {verb} requires --reviewer")


def _resume_pending_installs(ledger_path: pathlib.Path, gen: pathlib.Path) -> bool:
    """Complete any `.pending` decision journals whose ledger state is
    already filed (Luna r10/r11: a crash between the ledger commit and
    os.replace left the journal behind).

    Draft-INDEPENDENT (runs before _load_draft — a missing or changed
    draft cannot block the retry). Each journal's payload is verified
    against the ledger (candidate exists + filed state matches the
    payload's decision); a candidate now flagged re_evaluate=true is NEVER
    reinstated (human re-resolution is mandatory, r11 #2); install failure
    keeps the journal with a controlled error (r11 #1). Returns True when
    any install completed.
    """
    from regexproof.mine.ledger import load_ledger

    ledger = load_ledger(ledger_path)
    installed = 0
    for pending in sorted(gen.glob("*_gate_decision.json.pending")):
        out_path = pending.with_name(pending.name[: -len(".pending")])
        try:
            payload = json.loads(pending.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pending.unlink(missing_ok=True)  # corrupt journal — clean, fail-closed
            continue
        if not isinstance(payload, dict):
            # Luna r12: json.loads accepts [], null, strings, numbers —
            # .get() would crash the scanner (and it runs BEFORE draft
            # loading, so one malformed journal blocks every invocation).
            pending.unlink(missing_ok=True)
            continue
        url = str(payload.get("candidate_url") or "")
        decision = str(payload.get("decision") or "")
        if not url or decision not in ("go", "no-go", "triage-trial"):
            pending.unlink(missing_ok=True)  # unverifiable payload — stale
            continue
        cand = find_candidate(ledger, url)
        if cand is None:
            pending.unlink(missing_ok=True)  # candidate gone — stale
            continue
        audit_obj = cand.get("audit") or {}
        if not isinstance(audit_obj, dict):
            pending.unlink(missing_ok=True)
            continue
        if audit_obj.get("re_evaluate"):
            # r11 #2: never reinstate a decision the sampler flagged for
            # mandatory human re-review.
            raise SystemExit(
                f"bulk-review: refusing to install {pending.name}: candidate "
                f"{url} is now re_evaluate=true — human re-review required"
            )
        filed = (
            (decision == "no-go" and audit_obj.get("auto_filed") is True)
            or (decision != "no-go" and audit_obj.get("promoted_via") == "bulk-review")
        )
        if not filed:
            pending.unlink(missing_ok=True)  # ledger no longer filed — stale
            continue
        try:
            os.replace(pending, out_path)  # r11 #1: controlled failure
        except OSError as exc:
            raise SystemExit(
                f"bulk-review: journal install failed for {pending.name}: {exc} "
                "— re-run to retry (journal retained)"
            ) from exc
        installed += 1
        print(f"resumed: {url} -> {out_path.name} ({decision})")
    return installed > 0


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
    ap.add_argument(
        "--active-minutes",
        type=float,
        default=None,
        help="Stopwatch active minutes for this human-reviewed survivor "
        "(Wave 6). Appended to operator_minutes.jsonl; never the freeze.",
    )
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--go", action="store_true")
    group.add_argument("--no-go", dest="no_go", action="store_true")
    group.add_argument("--triage-trial", dest="triage_trial", action="store_true")
    group.add_argument("--requeue", action="store_true")
    group.add_argument("--demote-retain-corpus", action="store_true")
    args = ap.parse_args(argv)

    if args.active_minutes is not None and args.active_minutes < 0:
        raise SystemExit("bulk-review: --active-minutes must be >= 0")
    if args.active_minutes is not None and (args.no_go or args.requeue or args.demote_retain_corpus):
        raise SystemExit(
            "bulk-review: --active-minutes applies only to --go / --triage-trial"
        )

    # Luna r11 #4: complete any pending journals BEFORE loading the draft —
    # a retry after a crash between the ledger commit and os.replace must
    # not depend on the draft still being present.
    if _resume_pending_installs(args.ledger, GEN):
        if args.active_minutes is not None:
            print(
                "bulk-review: pending install resumed (draft-independent); "
                "--active-minutes was NOT recorded. Append a stopwatch row "
                "via regexproof.mine.operator_minutes.append_row after you "
                "know the installed candidate.",
                file=sys.stderr,
            )
        print("bulk-review: resumed pending install(s); run again for new work")
        return 0

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

    # Ledger prechecks — READ-ONLY, before any artifact is written
    # (CodeRabbit #573: a filing decision that fails after persisting the
    # artifact must not leave the candidate flagged with no decision file).
    if decision == "no-go":
        # Auto no-go goes through mark_auto_filed(), which rejects candidates
        # flagged re_evaluate=true (Luna r3). Precheck read-only so the
        # refusal happens BEFORE the artifact exists (Luna r4: writing first
        # left an ACTIVE decision after a refusal — the sync applied it).
        from regexproof.mine.ledger import load_ledger

        cand = find_candidate(load_ledger(args.ledger), url)
        if cand is None:
            raise SystemExit(f"bulk-review: auto-filing refused: {url} not in ledger")
        audit_obj = cand.get("audit") or {}
        if isinstance(audit_obj, dict) and audit_obj.get("re_evaluate"):
            raise SystemExit(
                "bulk-review: auto-filing refused: candidate flagged "
                "re_evaluate=true (routes to human review)"
            )
    else:
        from regexproof.mine.ledger import load_ledger

        if find_candidate(load_ledger(args.ledger), url) is None:
            raise SystemExit(
                f"bulk-review: {url} not in ledger — cannot author {decision}"
            )

    # Persist the artifact via temp + os.replace: the decision file is
    # written to `<name>.pending`, the ledger updates run, and ONLY on
    # success is it atomically renamed into place (Luna r9: an in-place
    # write followed by rollback could DELETE a prior valid decision on a
    # retry, and a non-ValueError failure left the artifact active). A
    # `.pending` file is invisible to sync_gate_decisions (glob is
    # *_gate_decision.json), so no crash window can apply an unproven
    # decision.
    out_path = default_output_path(corpus, repo_root=ROOT)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pending = out_path.with_name(out_path.name + ".pending")
    if pending.exists():
        pending.unlink(missing_ok=True)  # stale journal — the scanner already
                                         # resumed anything filed

    pending.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    def _rollback_pending() -> None:
        try:
            pending.unlink(missing_ok=True)
        except OSError:
            pass

    if decision == "no-go":
        try:
            audit.mark_auto_filed(
                args.ledger, url,
                clock=clock if clock is not None else None,
            )
        except Exception as exc:
            _rollback_pending()
            raise SystemExit(f"bulk-review: auto-filing refused: {exc}") from exc
    else:
        # Luna r5 #2: human decisions must CLEAR the re-review state
        # (re_evaluate / needs_human_review / auto_filed) — ensure_candidate_audit
        # alone left a resolved candidate still flagged, blocking later
        # auto-filing and leaving stale sampler state.
        try:
            audit.mark_human_resolved(
                args.ledger, url, decision=decision,
                clock=clock if clock is not None else None,
            )
        except Exception as exc:
            _rollback_pending()
            raise SystemExit(
                f"bulk-review: human-resolved update failed for {url}: {exc}"
            ) from exc
        promote_updates = {
            "promoted_via": "bulk-review",
            "promoted_at": (_utc_ts(at_dt) if at_dt is not None else _utc_ts()),
        }
        try:
            audit.ensure_candidate_audit(
                args.ledger, url, updates=promote_updates,
            )
        except Exception as exc:
            # Luna r2 P0: a missing ledger candidate must FAIL CLOSED — a
            # decision written without audit provenance is not sampler-eligible
            # and must not look like a successful promotion.
            _rollback_pending()
            raise SystemExit(
                f"bulk-review: ledger promotion failed for {url}: {exc} — "
                "audit provenance missing (no decision was installed)"
            ) from exc

    # All ledger updates succeeded — atomically install the decision. On
    # failure the .pending journal is KEPT so a re-run can resume (Luna
    # r10); the ledger already records the decision, so re-running the same
    # command completes the install without re-authoring.
    try:
        os.replace(pending, out_path)
    except OSError as exc:
        raise SystemExit(
            f"bulk-review: ledger updated but artifact install failed for "
            f"{url}: {exc} — re-run to retry (pending journal retained)"
        ) from exc
    print(f"{decision}: {url} -> {out_path.name} (provenance=human)" if decision != "no-go"
          else f"no_go: {url} -> {out_path.name} (provenance=auto)")
    if decision in ("go", "triage-trial") and args.active_minutes is not None:
        from regexproof.mine.operator_minutes import append_row

        pin = str(draft.get("corpus_pin") or draft.get("pin") or "")
        append_row(
            url=url,
            pin=pin,
            decision=decision,
            source="stopwatch",
            active_minutes=args.active_minutes,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
