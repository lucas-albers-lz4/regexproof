"""Scanner NDJSON + markdown reporting with witness redaction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def redact_witness(witness: object) -> object:
    """Idempotent redaction for secret-scanner-safe committed artifacts."""
    if witness is None:
        return None
    if isinstance(witness, dict):
        out = {}
        for k, v in witness.items():
            if isinstance(v, str) and v.startswith("<redacted"):
                out[k] = v
            elif isinstance(v, str) and len(v) >= 8:
                out[k] = f"<redacted len={len(v)}>"
            else:
                out[k] = v
        return out
    if isinstance(witness, str) and witness.startswith("<redacted"):
        return witness
    return "<redacted>"


def write_ndjson(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for rec in sorted(records, key=lambda r: (r.get("regex_id") or "", r.get("kind") or "")):
            payload = dict(rec)
            if "witness" in payload:
                payload["witness"] = redact_witness(payload.get("witness"))
            fh.write(json.dumps(payload, sort_keys=True) + "\n")


def write_markdown(path: Path, *, corpus: str, findings: list[dict[str, Any]]) -> None:
    lines = [
        "---",
        'schema_version: "1"',
        f"corpus: {corpus}",
        f"findings: {len(findings)}",
        "---",
        "",
        f"# {corpus} batch findings",
        "",
    ]
    for f in sorted(findings, key=lambda r: r.get("regex_id") or ""):
        lines.extend(
            [
                f"## {f.get('kind')}:{f.get('regex_id')}",
                "",
                f"- result: `{f.get('result')}`",
                f"- site: `{f.get('site')}`",
                f"- ground_truth_status: `{f.get('ground_truth_status')}`",
                f"- disclosure: `{f.get('disclosure')}`",
                "",
                "### Pattern",
                "",
                f"`{f.get('pattern', '')}`",
                "",
                "### Context",
                "",
                f"```json\n{json.dumps(f.get('detail') or {}, sort_keys=True)}\n```",
                "",
                "### Witness",
                "",
                f"```json\n{json.dumps(redact_witness(f.get('witness')), sort_keys=True)}\n```",
                "",
                "### Ground-truth",
                "",
                f"{f.get('ground_truth_status')}",
                "",
            ]
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
