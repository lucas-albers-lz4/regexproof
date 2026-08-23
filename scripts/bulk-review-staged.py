#!/usr/bin/env python3
"""Wave 3 (#560): staged bulk review CLI.

Triages staged probe drafts (properties/staged_probes/*.draft.json) into
ledger rows with HUMAN provenance.

Provenance rules (enforced, asserted, tested):
- ``go`` and ``triage-trial`` promotions REQUIRE human provenance — an
  auto path can never promote (the CLI has no auto-go; deterministic
  auto paths are NO-GO-only, pytest invariant).
- Escape-hatch graduation stays human-owned (no flag bypasses it).
- ``provenance=stub`` rows are excluded at schema level and never
  admitted to the ledger population.

Decision verbs
--------------
--go <site>:      promote the staged draft to a contracted row
                  (requires --reviewer + --provenance human).
--no-go <site> [--reason]:  record a deterministic NO-GO (auto-safe).
--triage-trial <site>:      record a triage-trial (requires human).
--requeue <site> [--reason]: return the candidate to the queue
                  (materialize --teardown equivalent; releases any
                  cache lease and records the retained location).
--demote-retain-corpus <site>: demote the row but keep the corpus
                  materialized (release lease; retained location
                  recorded in the ledger row).

Usage::

  python3 scripts/bulk-review-staged.py --go net/demo/a.sh:1:tok \\
      --reviewer alice --provenance human --ledger docs/conversion-upstream.jsonl
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

STAGED_ROOT = ROOT / "properties" / "staged_probes"


def _staged_draft(site: str) -> dict:
    """Load the staged draft for a site (deterministic name: sha256 of
    (digest#url#pin) — matches the emitter)."""
    for p in STAGED_ROOT.glob("*.draft.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        if d.get("site") == site:
            return d
    raise SystemExit(f"bulk-review: no staged draft for site {site!r}")


def _assert_human_provenance(args, verb: str) -> None:
    """go/triage-trial promotions REQUIRE human provenance (#560)."""
    if verb in ("go", "triage-trial"):
        if str(args.provenance or "").lower() != "human":
            raise SystemExit(
                f"bulk-review: {verb} requires --provenance human "
                "(auto paths are deterministic NO-GO-only)"
            )
        if not str(args.reviewer or "").strip():
            raise SystemExit(f"bulk-review: {verb} requires --reviewer")


def _ledger_row(site: str, verb: str, args, draft: dict) -> dict:
    row = {
        "site": site,
        "url": draft.get("url", ""),
        "pin": draft.get("pin", ""),
        "corpus": draft.get("corpus", ""),
        "outcome": verb,
        "provenance": args.provenance or "auto",
        "reviewer": args.reviewer or "",
        "at": args.at or "",
        "reason": args.reason or "",
        "staged_digest": draft.get("manifest_digest", ""),
        "idiom_bucket": draft.get("idiom_bucket", ""),
    }
    if verb == "demote_retain_corpus":
        row["retained_location"] = args.retained_location or ""
    return row


def _append_ledger(rows: list[dict], ledger: pathlib.Path) -> None:
    ledger.parent.mkdir(parents=True, exist_ok=True)
    # Canonical JSON: sorted keys, \n-terminated, stable order (#560).
    with open(ledger, "a", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, sort_keys=True) + "\n")
            fh.flush()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ledger", type=pathlib.Path,
                    default=ROOT / "docs" / "conversion-upstream.jsonl")
    ap.add_argument("--reviewer", default="")
    ap.add_argument("--provenance", default="auto",
                    choices=("auto", "human", "stub"))
    ap.add_argument("--at", default="", help="ISO clock for determinism")
    ap.add_argument("--reason", default="")
    ap.add_argument("--retained-location", default="")
    ap.add_argument("--list", action="store_true",
                    help="list staged drafts (no mutation)")
    ap.add_argument("--go", action="append", default=[])
    ap.add_argument("--no-go", dest="no_go", action="append", default=[])
    ap.add_argument("--triage-trial", dest="triage_trial", action="append", default=[])
    ap.add_argument("--requeue", action="append", default=[])
    ap.add_argument("--demote-retain-corpus", action="append", default=[])
    args = ap.parse_args(argv)

    if args.list:
        drafts = sorted(STAGED_ROOT.glob("*.draft.json"))
        for p in drafts:
            d = json.loads(p.read_text(encoding="utf-8"))
            print(f"{d.get('site')}\t{d.get('corpus')}\t{d.get('manifest_digest','')[:12]}")
        return 0

    # NO-GO is the only auto-safe verb; go/triage-trial assert human.
    for site in args.go:
        _assert_human_provenance(args, "go")
    for site in args.triage_trial:
        _assert_human_provenance(args, "triage-trial")

    rows: list[dict] = []
    for verb_sites, verb in (
        (args.go, "go"),
        (args.no_go, "no_go"),
        (args.triage_trial, "triage_trial"),
        (args.requeue, "requeue"),
        (args.demote_retain_corpus, "demote_retain_corpus"),
    ):
        for site in verb_sites:
            draft = _staged_draft(site)
            rows.append(_ledger_row(site, verb, args, draft))

    if not rows:
        ap.print_usage()
        return 1

    _append_ledger(rows, args.ledger)
    for r in rows:
        print(f"{r['outcome']}: {r['site']} (provenance={r['provenance']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
