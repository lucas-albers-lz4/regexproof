"""Join Z3-side records and ReDoS findings by regex_id — never conflate."""

from __future__ import annotations

from typing import Any


def join_findings(
    z3_records: list[dict[str, Any]],
    redos_records: list[dict[str, Any]],
) -> dict[str, Any]:
    """Return a report with separate sections keyed by regex_id.

    Deliberately omits any combined/merged verdict field so a ReDoS
    `vulnerable` and a Z3 `unsat` on the same id cannot be collapsed.
    """
    z3_by_id: dict[str, list[dict[str, Any]]] = {}
    for rec in z3_records:
        rid = rec.get("regex_id")
        if not rid:
            continue
        z3_by_id.setdefault(rid, []).append(rec)

    redos_by_id: dict[str, list[dict[str, Any]]] = {}
    for rec in redos_records:
        rid = rec.get("regex_id")
        if not rid:
            continue
        redos_by_id.setdefault(rid, []).append(rec)

    all_ids = sorted(set(z3_by_id) | set(redos_by_id))
    return {
        "schema_version": "1",
        "z3_findings": {rid: z3_by_id.get(rid, []) for rid in all_ids},
        "redos_findings": {rid: redos_by_id.get(rid, []) for rid in all_ids},
        "regex_ids": all_ids,
        # Explicit non-field: no "verdict" / "combined" key by design.
    }
