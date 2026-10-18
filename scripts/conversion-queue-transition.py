#!/usr/bin/env python3
"""Apply source-bound claim, contract, and skip transitions to a conversion queue.

The queue library is the state machine. This CLI supplies authoritative gate,
ledger, contract, and wave evidence so an operator does not edit queue JSON by
hand.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from datetime import datetime, timezone
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.contract_adoption import (  # noqa: E402
    contract_is_adopted,
    verify_adoption_source,
)
from regexproof.mine import conversion_queue as cq  # noqa: E402
from regexproof.mine.corpus_lock import read_generation  # noqa: E402

ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
PIN_RE = re.compile(r"^[0-9a-f]{40}$")
URL_RE = re.compile(r"^https://github\.com/[^/\s]+/[^/\s]+$")


class TransitionError(ValueError):
    """Invalid or stale input to a queue transition."""


def _json_object(path: pathlib.Path, label: str) -> tuple[dict[str, Any], bytes]:
    try:
        raw = path.read_bytes()
        value = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        raise TransitionError(f"cannot read {label} {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise TransitionError(f"{label} must be a JSON object: {path}")
    return value, raw


def _cluster(value: str) -> str:
    if not ID_RE.fullmatch(value):
        raise TransitionError("cluster must be a plain identifier")
    return value


def _queue_site(cluster: str, site: str, root: pathlib.Path) -> tuple[dict[str, Any], dict[str, Any]]:
    queue = cq.load_queue(cluster, root=root)
    if queue.get("cluster") != cluster or not isinstance(queue.get("candidate_sites"), list):
        raise TransitionError(f"queue artifact for {cluster} has invalid identity or candidates")
    matches = [row for row in queue["candidate_sites"] if isinstance(row, dict) and row.get("site") == site]
    if len(matches) != 1:
        raise TransitionError(f"site must occur exactly once in queue {cluster}: {site}")
    return queue, matches[0]


def _decision(path: pathlib.Path, cluster: str) -> tuple[dict[str, Any], str, str, str]:
    value, raw = _json_object(path, "gate decision")
    if value.get("corpus") != cluster or value.get("decision") != "go":
        raise TransitionError(f"gate decision must be go for corpus {cluster}")
    probe = value.get("probe")
    probe_pin = probe.get("pin") if isinstance(probe, dict) else None
    pin = value.get("corpus_pin") or probe_pin
    url = value.get("candidate_url")
    if not isinstance(pin, str) or not PIN_RE.fullmatch(pin):
        raise TransitionError("gate decision has no valid 40-character source pin")
    if not isinstance(url, str) or not URL_RE.fullmatch(url):
        raise TransitionError("gate decision has no canonical GitHub candidate_url")
    return value, pin, url, hashlib.sha256(raw).hexdigest()


def _claim(args: argparse.Namespace) -> dict[str, Any]:
    cluster = _cluster(args.cluster)
    _, row = _queue_site(cluster, args.site, args.queue_dir)
    _, pin, url, decision_sha256 = _decision(args.gate_decision, cluster)
    if row.get("pin") != pin:
        raise TransitionError(
            f"queue source pin {row.get('pin')!r} does not match GO decision pin {pin!r}"
        )
    row_corpus = row.get("corpus")
    if row_corpus is not None and row_corpus != cluster:
        raise TransitionError("queue site corpus does not match the queue cluster")

    ledger, raw_ledger = _json_object(args.conversion_ledger, "conversion ledger")
    per_wave = ledger.get("per_wave")
    if not isinstance(per_wave, list):
        raise TransitionError("conversion ledger must contain a per_wave list")
    generation = read_generation(cluster, args.events_log)
    snapshot = {
        "now_iso": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n": len(per_wave),
        "conversion_ledger_sha256": hashlib.sha256(raw_ledger).hexdigest(),
        "gate_decision_sha256": decision_sha256,
        "repository_url": url,
        "source_pin": pin,
    }
    # The library rechecks generation, active wave, artifact generation, and
    # wave ID under the same lock used by wave_close.
    return cq.claim(
        cluster,
        args.site,
        corpus_status=cq.GATED_GO,
        ledger_state=snapshot,
        generation=generation,
        root=args.queue_dir,
        lock_log=args.events_log,
    )


def _contract(args: argparse.Namespace) -> dict[str, Any]:
    cluster = _cluster(args.cluster)
    _, row = _queue_site(cluster, args.site, args.queue_dir)
    contract, _ = _json_object(args.contract, "product contract")
    if contract.get("site") != args.site:
        raise TransitionError("contract.site must match --site")
    if contract.get("provenance") != "agent_derived" or not contract_is_adopted(contract):
        raise TransitionError("contract must carry a valid autonomous adoption record")
    adoption = contract.get("adoption") or {}
    snapshot = row.get("ledger_state_at_claim")
    if row.get("status") != "claimed" or not isinstance(snapshot, dict):
        raise TransitionError("contract requires a claimed row with a source snapshot")
    if (
        not snapshot.get("gate_decision_sha256")
        or adoption.get("source_pin") != row.get("pin")
        or adoption.get("source_pin") != snapshot.get("source_pin")
        or adoption.get("source_url", "").rstrip("/")
        != str(snapshot.get("repository_url") or "").rstrip("/")
    ):
        raise TransitionError("contract adoption source does not match the claim snapshot")
    try:
        verify_adoption_source(contract, args.checkout)
    except ValueError as exc:
        raise TransitionError(str(exc)) from exc
    return cq.contract(
        cluster,
        args.site,
        contract=contract,
        root=args.queue_dir,
        lock_log=args.events_log,
    )


def _skip(args: argparse.Namespace) -> dict[str, Any]:
    cluster = _cluster(args.cluster)
    _, row = _queue_site(cluster, args.site, args.queue_dir)
    if int(row.get("rank") or 999) > 15:
        raise TransitionError("only ranked top-15 sites may receive wave dispositions")
    if row.get("status") not in {"emitted", "claimed"}:
        raise TransitionError("skip requires an emitted or claimed top-15 site")
    note = args.note.strip()
    if not note:
        raise TransitionError("skip requires a non-empty evidence note")
    return cq.skip(
        cluster,
        args.site,
        reason=args.reason,
        note=note,
        root=args.queue_dir,
        lock_log=args.events_log,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)

    def common(command: argparse.ArgumentParser) -> None:
        command.add_argument("--cluster", required=True)
        command.add_argument("--site", required=True)
        command.add_argument("--queue-dir", type=pathlib.Path, default=ROOT / "properties" / "conversion_queue")
        command.add_argument("--events-log", type=pathlib.Path, default=ROOT / "properties" / "generated" / "corpus_events.jsonl")

    claim = commands.add_parser("claim", help="claim one top-15 site in an active GO wave")
    common(claim)
    claim.add_argument("--gate-decision", type=pathlib.Path, required=True)
    claim.add_argument("--conversion-ledger", type=pathlib.Path, default=ROOT / "properties" / "generated" / "conversion-ledger.json")

    contract = commands.add_parser("contract", help="advance a claimed site with its adopted contract")
    common(contract)
    contract.add_argument("--contract", type=pathlib.Path, required=True)
    contract.add_argument("--checkout", type=pathlib.Path, required=True)

    skip = commands.add_parser("skip", help="record a top-15 disposition in an active wave")
    common(skip)
    skip.add_argument("--reason", required=True, choices=sorted(cq.SKIP_REASONS))
    skip.add_argument("--note", required=True)

    args = parser.parse_args(argv)
    try:
        row = {"claim": _claim, "contract": _contract, "skip": _skip}[args.action](args)
    except (OSError, ValueError, SystemExit, KeyError, TypeError) as exc:
        message = str(exc)
        if message:
            print(f"conversion-queue-transition: {message}", file=sys.stderr)
        return 2
    print(json.dumps(row, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
