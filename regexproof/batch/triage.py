"""Triage NDJSON writer — unencodable / timeout / ambiguous → one record each."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from regexproof.io_atomic import atomic_write_lines

TRIAGE_SCHEMA_VERSION = "1"


def triage_records_from_compiled(compiled: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for rec in compiled:
        reason = rec.get("compile_reason") or rec.get("unencodable_reason")
        if rec.get("encodable") and not reason and rec.get("result") != "timeout":
            continue
        # Timeout may be signaled via result= and/or compile_reason= (runner
        # sets both when a compile times out — fix-wave #71).
        if reason == "timeout" or rec.get("result") == "timeout":
            kind = "timeout"
        elif reason:
            kind = "unencodable"
        else:
            kind = "ambiguous"
        row = {
            "schema_version": TRIAGE_SCHEMA_VERSION,
            "regex_id": rec["regex_id"],
            "reason_kind": kind,
            "unencodable_reason": reason,
            "dialect": rec.get("dialect") or "",
            "call_kind": rec.get("call_kind") or "",
            "site": rec.get("site") or "",
            "pattern": rec.get("pattern") or "",
        }
        # Surface ModSecurity negation so triage never looks like a normal rule.
        if rec.get("negated") is not None:
            row["negated"] = bool(rec.get("negated"))
        if rec.get("selector") is not None:
            row["selector"] = bool(rec.get("selector"))
        out.append(row)
    out.sort(key=lambda r: r["regex_id"])
    return out


def write_triage_ndjson(path: Path, records: list[dict[str, Any]]) -> None:
    atomic_write_lines(path, (json.dumps(rec, sort_keys=True) for rec in records))
