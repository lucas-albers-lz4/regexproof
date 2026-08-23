"""Wave C (#558): conversion review queue artifact.

Cluster-ranked candidate sites with a SINGLE status vocabulary
(``emitted`` / ``claimed`` / ``contracted`` / ``skipped_*``). Later states
are derived joins over the queue + ledger — the queue never re-encodes
ledger truth. Stubs (``provenance=stub``) are QUEUE-ONLY, schema-enforced
(``schemas/queue_stub.schema.json``): a stub never increments
``properties_asked`` (it is not a contract).

Guards (acceptance criteria):
- top-15 requirement: a claim must target a ranked candidate within the
  top-15 of its cluster, or be refused;
- claims refused on non-``gated:go`` corpora;
- wave close-out requires skip reasons for every non-contracted top-15
  candidate;
- ``ledger_state_at_claim`` + per-corpus ``wave_generation`` are recorded
  so the queue is replayable against a specific ledger/lock snapshot.
"""

from __future__ import annotations

import json
import pathlib
from typing import Any

QUEUE_ROOT = pathlib.Path("properties/conversion_queue")

STATUSES = frozenset(
    {
        "emitted",
        "claimed",
        "contracted",
        "skipped_unreachable",
        "skipped_out_of_scope",
        "skipped_no_response",
        "skipped_duplicate",
    }
)
GATED_GO = "gated:go"

# Skip-reason vocabulary (Luna r3 #3): forced close-out accepts ONLY these
# reasons — an arbitrary nonblank string must not satisfy the requirement.
SKIP_REASONS = frozenset(
    {
        "unreachable",
        "out_of_scope",
        "no_response",
        "duplicate",
    }
)


def queue_path(cluster: str) -> pathlib.Path:
    return QUEUE_ROOT / f"{cluster}.json"


def empty_queue(cluster: str, *, generation: int, wave_id: str) -> dict[str, Any]:
    return {
        "schema_version": "1",
        "cluster": cluster,
        "wave_id": wave_id,
        "wave_generation": generation,
        "candidate_sites": [],
    }


def load_queue(cluster: str, root: pathlib.Path | None = None) -> dict[str, Any]:
    path = (pathlib.Path(root) if root is not None else QUEUE_ROOT) / f"{cluster}.json"
    if not path.is_file():
        raise SystemExit(f"conversion_queue: no queue artifact for {cluster}")
    return json.loads(path.read_text(encoding="utf-8"))


def emit(
    cluster: str,
    *,
    wave_id: str,
    generation: int,
    ranked: list[dict[str, Any]],
    root: pathlib.Path | None = None,
) -> pathlib.Path:
    """Create the queue artifact from a ranked candidate list (Gate 2).

    ``ranked`` items carry at minimum ``site``; stub fields
    (``provenance=stub``, idiom bucket, cheap signals) are validated
    against the stub schema by the emitter's caller. ``wave_id`` must be
    NONBLANK — an unbound artifact would bypass the wave-binding check at
    claim time (Luna r4 #2)."""
    if not str(wave_id or "").strip():
        raise SystemExit(
            "conversion_queue: emit refused — wave_id must be nonblank (an "
            "unbound artifact would bypass claim-time wave binding)"
        )
    q = empty_queue(cluster, generation=generation, wave_id=wave_id)
    for i, item in enumerate(ranked, start=1):
        row = {
            "rank": i,
            "site": str(item.get("site") or ""),
            "status": "emitted",
            "reasons": [],
        }
        for key in (
            "corpus",
            "pin",
            "idiom_bucket",
            "provenance",
            "suggested_shape",
            "suggested_sink_question",
            "capture_group",
            "charset_class",
            "path_vocabulary",
            "trust_guess",
        ):
            if key in item:
                row[key] = item[key]
        q["candidate_sites"].append(row)
    path = (pathlib.Path(root) if root is not None else QUEUE_ROOT) / f"{cluster}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(q, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _row(q: dict[str, Any], site: str) -> dict[str, Any]:
    for r in q["candidate_sites"]:
        if r["site"] == site:
            return r
    raise SystemExit(f"conversion_queue: site {site!r} not in queue {q['cluster']}")


def _queue_lock_path(cluster: str, root: pathlib.Path | None = None) -> pathlib.Path:
    return (pathlib.Path(root) if root is not None else QUEUE_ROOT) / f"{cluster}.json.lock"


def _with_queue_lock(cluster: str, root: pathlib.Path | None, lock_log, fn):
    """Serialize queue read-modify-write on the corpus lock's SINGLE
    primitive — the events log flock (Luna r3 #1: a separate per-cluster
    lock would not exclude ``wave_close``, so a claim could persist after
    the wave closed)."""
    from regexproof.mine.corpus_lock import events_lock

    return events_lock(cluster, fn, log=lock_log)


def claim(
    cluster: str,
    site: str,
    *,
    corpus_status: str,
    ledger_state: dict[str, Any],
    generation: int,
    wave_id: str = "",
    root: pathlib.Path | None = None,
    lock_log: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Claim a site for review. Refused unless: the corpus is ``gated:go``,
    the site is within the top-15, the site is currently ``emitted``, and —
    when a lock provider is available — the corpus has an ACTIVE wave whose
    generation matches the caller's snapshot (Luna r1 #3). The lock
    validation and the queue write happen under ONE flock (Luna r2 #2: a
    close racing between validation and write can no longer strand a claim
    after the wave closed)."""

    def _claim() -> dict[str, Any]:
        q = load_queue(cluster, root)
        if corpus_status != GATED_GO:
            raise SystemExit(
                f"conversion_queue: claim refused — corpus {cluster} is "
                f"{corpus_status!r}, not {GATED_GO!r}"
            )
        row = _row(q, site)
        if int(row.get("rank") or 999) > 15:
            raise SystemExit(
                f"conversion_queue: claim refused — {site} is rank "
                f"{row.get('rank')} (top-15 requirement)"
            )
        if row["status"] != "emitted":
            raise SystemExit(
                f"conversion_queue: claim refused — {site} status is "
                f"{row['status']!r}, not 'emitted'"
            )
        # Lock validation INSIDE the queue lock (Luna r2 #2): the wave
        # cannot close between this check and the write below.
        from regexproof.mine.corpus_lock import wave_status, read_generation, _active_wave_id

        status = wave_status(cluster, lock_log)
        if status != "active":
            raise SystemExit(
                f"conversion_queue: claim refused — corpus {cluster} wave_status "
                f"is {status!r}, not 'active' (claims ride an open wave)"
            )
        current = read_generation(cluster, lock_log)
        if current != generation:
            raise SystemExit(
                f"conversion_queue: claim refused — {cluster} generation is "
                f"{current}, not the caller's {generation} (stale snapshot)"
            )
        # Wave binding (Luna r2 #1 / r3 #2 / r4 #2): the ARTIFACT's wave is
        # authoritative and REQUIRED nonblank — an unbound artifact cannot
        # be claimed at all, and a caller-supplied wave_id cannot override.
        active = _active_wave_id(cluster, lock_log)
        artifact_wave = str(q.get("wave_id") or "")
        if not artifact_wave:
            raise SystemExit(
                f"conversion_queue: claim refused — queue {cluster} has no "
                "wave binding (emit requires a nonblank wave_id)"
            )
        if active and artifact_wave != active:
            raise SystemExit(
                f"conversion_queue: claim refused — queue {cluster} is bound "
                f"to wave {artifact_wave!r} but active wave is {active!r}"
            )
        row["status"] = "claimed"
        row["claimed_at"] = ledger_state.get("now_iso", "")
        row["ledger_state_at_claim"] = ledger_state
        row["wave_generation_at_claim"] = generation
        row["wave_id"] = artifact_wave
        _write(q, root)
        return row

    return _with_queue_lock(cluster, root, lock_log, _claim)


def contract(
    cluster: str,
    site: str,
    *,
    contract: dict[str, Any],
    root: pathlib.Path | None = None,
    lock_log: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Adopt a contract for a claimed site. Contract fields are validated
    by the caller against the contract schema; ``provenance=stub`` rows
    NEVER contract (they must be re-ranked / human-adopted first)."""

    def _contract() -> dict[str, Any]:
        q = load_queue(cluster, root)
        row = _row(q, site)
        if row["status"] != "claimed":
            raise SystemExit(
                f"conversion_queue: contract refused — {site} status is "
                f"{row['status']!r}, not 'claimed'"
            )
        if (row.get("provenance") or "human") == "stub":
            raise SystemExit(
                f"conversion_queue: contract refused — {site} is a stub "
                "(provenance=stub); stubs never become contracts directly"
            )
        row["status"] = "contracted"
        row["contract"] = contract
        _write(q, root)
        return row

    return _with_queue_lock(cluster, root, lock_log, _contract)


def skip(
    cluster: str,
    site: str,
    *,
    reason: str,
    note: str = "",
    root: pathlib.Path | None = None,
    lock_log: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Skip a site with a reason (skipped_<reason> vocabulary). A row that
    is already ``contracted`` can NEVER be skipped — that would strand a
    live contract (Luna r1 #11: transition safety)."""
    reason = str(reason or "").strip()
    if reason not in SKIP_REASONS:
        raise SystemExit(
            f"conversion_queue: unknown skip reason {reason!r}; allowed: "
            f"{sorted(SKIP_REASONS)}"
        )
    status = f"skipped_{reason}"
    def _skip() -> dict[str, Any]:
        q = load_queue(cluster, root)
        row = _row(q, site)
        if row["status"] == "contracted":
            raise SystemExit(
                f"conversion_queue: skip refused — {site} is contracted; a live "
                "contract cannot be reverted to a skip state"
            )
        row["status"] = status
        row["reasons"].append({"reason": reason, "note": note})
        _write(q, root)
        return row

    return _with_queue_lock(cluster, root, lock_log, _skip)


def non_contracted_top15(q: dict[str, Any]) -> list[dict[str, Any]]:
    """Top-15 candidates that are neither contracted nor skipped — wave
    close-out requires skip reasons for these."""
    return [
        r
        for r in q["candidate_sites"]
        if int(r.get("rank") or 999) <= 15
        and r["status"] not in ("contracted",)
        and not r["status"].startswith("skipped_")
    ]


def _write(q: dict[str, Any], root: pathlib.Path | None = None) -> None:
    """Atomic write: tmp file + os.replace (a crash mid-write can never
    truncate the artifact — Luna r1 #11)."""
    import os

    path = (pathlib.Path(root) if root is not None else QUEUE_ROOT) / f"{q['cluster']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(q, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)
