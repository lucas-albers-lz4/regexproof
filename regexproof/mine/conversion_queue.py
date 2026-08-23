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
    against the stub schema by the emitter's caller."""
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


def claim(
    cluster: str,
    site: str,
    *,
    corpus_status: str,
    ledger_state: dict[str, Any],
    generation: int,
    root: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Claim a site for review. Refused unless: the corpus is ``gated:go``,
    the site is within the top-15, and the site is currently ``emitted``."""
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
    row["status"] = "claimed"
    row["claimed_at"] = ledger_state.get("now_iso", "")
    row["ledger_state_at_claim"] = ledger_state
    row["wave_generation_at_claim"] = generation
    _write(q, root)
    return row


def contract(
    cluster: str,
    site: str,
    *,
    contract: dict[str, Any],
    root: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Adopt a contract for a claimed site. Contract fields are validated
    by the caller against the contract schema; ``provenance=stub`` rows
    NEVER contract (they must be re-ranked / human-adopted first)."""
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


def skip(
    cluster: str,
    site: str,
    *,
    reason: str,
    note: str = "",
    root: pathlib.Path | None = None,
) -> dict[str, Any]:
    """Skip a site with a reason (skipped_<reason> vocabulary)."""
    reason = str(reason or "").strip()
    status = f"skipped_{reason}" if reason else ""
    if status not in STATUSES:
        raise SystemExit(
            f"conversion_queue: unknown skip reason {reason!r}; allowed: "
            f"{sorted(s for s in STATUSES if s.startswith('skipped_'))}"
        )
    q = load_queue(cluster, root)
    row = _row(q, site)
    row["status"] = status
    row["reasons"].append({"reason": reason, "note": note})
    _write(q, root)
    return row


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
    path = (pathlib.Path(root) if root is not None else QUEUE_ROOT) / f"{q['cluster']}.json"
    path.write_text(json.dumps(q, indent=2, sort_keys=True) + "\n", encoding="utf-8")
