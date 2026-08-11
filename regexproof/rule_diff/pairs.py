"""Pair discovery: independent-spec R1 × encodable R2 with parity checks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from regexproof.compiler import compile_pattern
from regexproof.compiler.normalize import normalize_inline_flags
from regexproof.extractors.rule_file import extract_rule_file
from regexproof.regex_id import make_regex_id
from regexproof.rule_diff.specs import load_canonical_specs

ADMITTED_SCHEMA_VERSION = "1"
MIN_ADMITTED_PAIRS = 20
DEFAULT_MAX_LEN = 96


def discover_pairs(
    *,
    toml_path: Path,
    specs_path: Path,
    repo: str = "gitleaks/gitleaks",
    file: str | None = None,
    max_len: int = DEFAULT_MAX_LEN,
) -> dict[str, Any]:
    """Join canonical specs to encodable gitleaks rules; emit admit/drop lists."""
    file = file or str(toml_path)
    source = toml_path.read_text(encoding="utf-8")
    records = extract_rule_file(source, repo=repo, file=file, dialect="re2")
    by_rule_id: dict[str, dict[str, Any]] = {}
    for rec in records:
        rid = rec.get("context_snippet") or ""
        if rid:
            by_rule_id[rid] = rec

    specs = load_canonical_specs(specs_path)
    admitted: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []

    for spec in specs:
        rule_id = spec["maps_to_rule_id"]
        r2_rec = by_rule_id.get(rule_id)
        if r2_rec is None:
            dropped.append(
                _drop(
                    spec,
                    None,
                    reason="rule-id-not-found",
                )
            )
            continue
        if r2_rec.get("unencodable_reason"):
            dropped.append(
                _drop(spec, r2_rec, reason=f"extract:{r2_rec['unencodable_reason']}")
            )
            continue

        r1_pat, r1_flags = normalize_inline_flags(spec["pattern"], spec.get("flags") or "")
        r2_pat, r2_flags = normalize_inline_flags(
            r2_rec["pattern"], r2_rec.get("flags") or ""
        )
        r1_ck = spec.get("call_kind") or "search"
        r2_ck = r2_rec.get("call_kind") or "search"
        r1_dialect = spec.get("dialect") or "re2"
        r2_dialect = r2_rec.get("dialect") or "re2"

        if r1_ck != r2_ck:
            dropped.append(_drop(spec, r2_rec, reason="call_kind-mismatch"))
            continue
        if (r1_flags or "") != (r2_flags or ""):
            dropped.append(_drop(spec, r2_rec, reason="flags-mismatch"))
            continue

        r1_c = compile_pattern(r1_pat, r1_flags, r1_dialect, r1_ck, max_length=max_len)
        r2_c = compile_pattern(r2_pat, r2_flags, r2_dialect, r2_ck, max_length=max_len)
        if not r1_c.encodable:
            dropped.append(
                _drop(spec, r2_rec, reason=f"r1-unencodable:{r1_c.unencodable_reason}")
            )
            continue
        if not r2_c.encodable:
            dropped.append(
                _drop(spec, r2_rec, reason=f"r2-unencodable:{r2_c.unencodable_reason}")
            )
            continue
        # Character-set equality via declared_domain (ascii/unicode).
        if r1_c.declared_domain != r2_c.declared_domain:
            dropped.append(_drop(spec, r2_rec, reason="alphabet-mismatch"))
            continue

        # Skip pairs whose R2 cannot match within the length bound (e.g. {250,}).
        if _min_literal_span(r2_pat) > max_len:
            dropped.append(_drop(spec, r2_rec, reason="length-bound-exceeded"))
            continue

        site_r1 = f"canonical_specs:{spec['id']}:0:0"
        regex_id_r1 = make_regex_id(
            repo="independent-spec",
            pattern=r1_pat,
            flags=r1_flags,
            dialect=r1_dialect,
            call_kind=r1_ck,
            site=site_r1,
        )
        pair = {
            "schema_version": ADMITTED_SCHEMA_VERSION,
            "pair_id": f"{spec['id']}__{rule_id}",
            "direction": "r2_minus_r1",
            "regex_id_r1": regex_id_r1,
            "regex_id_r2": r2_rec["regex_id"],
            "r1": {
                "pattern": r1_pat,
                "flags": r1_flags,
                "dialect": r1_dialect,
                "call_kind": r1_ck,
                "site": site_r1,
                "spec_id": spec["id"],
            },
            "r2": {
                "pattern": r2_pat,
                "flags": r2_flags,
                "dialect": r2_dialect,
                "call_kind": r2_ck,
                "site": r2_rec["site"],
                "rule_id": rule_id,
            },
            "provenance": spec["provenance"],
            "call_kind": r1_ck,
            "declared_domain": r1_c.declared_domain,
            "max_len": max_len,
            "family": f"RD-{spec['id']}",
        }
        admitted.append(pair)

    admitted.sort(key=lambda p: p["pair_id"])
    dropped.sort(key=lambda p: (p.get("spec_id") or "", p.get("reason") or ""))
    return {
        "schema_version": ADMITTED_SCHEMA_VERSION,
        "admitted_pairs": admitted,
        "dropped_pairs": dropped,
        "admitted_count": len(admitted),
        "dropped_count": len(dropped),
        "min_admitted_pairs": MIN_ADMITTED_PAIRS,
        "max_len": max_len,
        "floor_ok": len(admitted) >= MIN_ADMITTED_PAIRS,
    }


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    from regexproof.io_atomic import atomic_write_lines

    atomic_write_lines(
        path, (json.dumps(rec, sort_keys=True) for rec in records)
    )


def _drop(
    spec: dict[str, Any],
    r2_rec: dict[str, Any] | None,
    *,
    reason: str,
) -> dict[str, Any]:
    return {
        "schema_version": ADMITTED_SCHEMA_VERSION,
        "spec_id": spec.get("id"),
        "maps_to_rule_id": spec.get("maps_to_rule_id"),
        "reason": reason,
        "r2_site": (r2_rec or {}).get("site"),
        "r2_regex_id": (r2_rec or {}).get("regex_id"),
    }


def _min_literal_span(pattern: str) -> int:
    """Lower bound on match length from `{n}` / `{n,}` and fixed literals."""
    import re

    # Drop non-capturing markers; treat | as zero-width (conservative over-count ok
    # for floors used with slack in the pilot).
    p = re.sub(r"\(\?:", "(", pattern)
    p = re.sub(r"\\.", "x", p)
    floor = 0
    out: list[str] = []
    i = 0
    while i < len(p):
        if p[i] == "[":
            j = i + 1
            if j < len(p) and p[j] == "^":
                j += 1
            while j < len(p) and p[j] != "]":
                j += 1
            i = min(j + 1, len(p))
            m = re.match(r"\{(\d+)(?:,\d*)?\}", p[i:])
            if m:
                floor += int(m.group(1))
                i += m.end()
            elif i < len(p) and p[i] == "+":
                floor += 1
                i += 1
            elif i < len(p) and p[i] in "*?":
                i += 1
            else:
                floor += 1
            continue
        if p[i] in "()|":
            i += 1
            continue
        if p[i] in "*+?":
            i += 1
            continue
        if p[i] == "{":
            m = re.match(r"\{(\d+)(?:,\d*)?\}", p[i:])
            if m:
                if out:
                    out.pop()
                    floor += int(m.group(1))
                else:
                    floor += int(m.group(1))
                i += m.end()
                continue
            i += 1
            continue
        if p[i] in ".^$":
            floor += 1
            i += 1
            continue
        out.append(p[i])
        i += 1
    return floor + len(out)
