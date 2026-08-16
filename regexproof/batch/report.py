"""Scanner NDJSON + markdown reporting with witness redaction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from regexproof.io_atomic import atomic_write_lines, atomic_write_text

# Per-finding metadata keys aligned with docs/REPORTING.md / Phase-3 pilot rows.
_FINDING_META_KEYS = (
    "regex_id",
    "schema_version",
    "kind",
    "corpus",
    "dialect",
    "call_kind",
    "shape",
    "result",
    "family",
    "domain",
    "wall_ms",
    "ground_truth_status",
    "engine_versions",
    "disclosure",
    "site",
)


def _redact_value(value: object, *, min_len: int = 8) -> object:
    """Redact a dict/list value, recursing into nested containers."""
    if isinstance(value, dict):
        return {k: _redact_value(v, min_len=min_len) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_redact_value(v, min_len=min_len) for v in value]
    if isinstance(value, str) and value.startswith("<redacted"):
        return value
    if isinstance(value, str) and len(value) >= min_len:
        return f"<redacted len={len(value)}>"
    return value


def redact_witness(witness: object, *, min_len: int = 8) -> object:
    """Idempotent redaction for secret-scanner-safe committed artifacts.

    Nested lists/dicts are walked so container-typed witness fields cannot
    leak secrets (fix-wave #71). Top-level non-dict witnesses remain fully
    opaque (`<redacted>`), matching the prior contract.
    CRS reports pass ``min_len=1`` so short SAT strings are not committed (#473).
    """
    if witness is None:
        return None
    if isinstance(witness, dict):
        return {k: _redact_value(v, min_len=min_len) for k, v in witness.items()}
    if isinstance(witness, str) and witness.startswith("<redacted"):
        return witness
    return "<redacted>"


def write_ndjson(path: Path, records: list[dict[str, Any]]) -> None:
    lines: list[str] = []
    for rec in sorted(
        records,
        key=lambda r: (
            r.get("regex_id") or "",
            r.get("question_id") or (r.get("detail") or {}).get("question_id") or "",
            r.get("bad_char") or (r.get("detail") or {}).get("bad_char") or "",
            r.get("kind") or "",
        ),
    ):
        payload = dict(rec)
        if payload.get("synthesized"):
            # Solver timing is deliberately not part of the reproducibility
            # artifact (cache/parallel workstreams may change it).
            payload["wall_ms"] = 0
        if "witness" in payload:
            payload["witness"] = redact_witness(payload.get("witness"))
        lines.append(json.dumps(payload, sort_keys=True))
    atomic_write_lines(path, lines)


def _yaml_scalar(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, dict):
        # Compact JSON for nested maps (engine_versions).
        return json.dumps(value, sort_keys=True)
    text = str(value)
    # Quote anything ambiguous for YAML 1.1 (N/A, YES, NO, ON, OFF, …).
    ambiguous = {
        "",
        "n/a",
        "yes",
        "no",
        "y",
        "n",
        "true",
        "false",
        "on",
        "off",
        "null",
        "~",
    }
    if (
        text.lower() in ambiguous
        or any(c in text for c in (":", "#", "\n", '"', "'", "[", "]", "{", "}"))
        or text[:1] in "-?&*!|>%@`"
    ):
        return json.dumps(text)
    return text


def write_markdown(path: Path, *, corpus: str, findings: list[dict[str, Any]]) -> None:
    """Write ``*_batch.md`` with report front matter + per-finding contracted fields.

    Does not write Phase-3 shape-5 paths such as ``gitleaks.md``.
    """
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
    for f in sorted(
        findings,
        key=lambda r: (
            r.get("regex_id") or "",
            r.get("kind") or "",
            (r.get("detail") or {}).get("keyword") or "",
            (r.get("detail") or {}).get("question_id") or "",
        ),
    ):
        detail = f.get("detail") or {}
        # Prefer finding-level call_kind; fall back to detail.
        if f.get("call_kind") is None and detail.get("call_kind") is not None:
            f = {**f, "call_kind": detail.get("call_kind")}
        if f.get("dialect") is None and detail.get("dialect") is not None:
            f = {**f, "dialect": detail.get("dialect")}
        if f.get("family") is None and detail.get("family") is not None:
            f = {**f, "family": detail.get("family")}
        if f.get("domain") is None and (
            f.get("input_domain") is not None or detail.get("domain") is not None
        ):
            f = {
                **f,
                "domain": f.get("input_domain") or detail.get("domain"),
            }

        suffix = detail.get("keyword") or detail.get("question_id") or f.get("call_kind") or ""
        heading = f"## {f.get('kind')}:{f.get('regex_id')}"
        if suffix:
            heading = f"{heading}:{suffix}"
        lines.extend([heading, "", "```yaml"])
        for key in _FINDING_META_KEYS:
            if key not in f and key != "schema_version":
                continue
            val = f.get(key)
            if key == "schema_version":
                # Always emit the string constant required by scanner schemas.
                lines.append(f'schema_version: "1"')
                continue
            if val is None and key not in ("ground_truth_status", "disclosure", "shape"):
                continue
            lines.append(f"{key}: {_yaml_scalar(val)}")
        lines.extend(
            [
                "```",
                "",
                "### Pattern",
                "",
                f"`{f.get('pattern', '')}`",
                "",
                "### Context",
                "",
                f"```json\n{json.dumps(detail, sort_keys=True)}\n```",
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
    atomic_write_text(path, "\n".join(lines))
