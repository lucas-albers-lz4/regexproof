"""CRS encodable-fraction helpers (Fowler Move Function, #454).

JSON payloads must stay byte-identical to the pre-move ``runner.py`` writers.
Do not call ``batch.measure.fraction_report`` (it rounds differently).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from regexproof.batch.manifests import CORPUS_MANIFESTS, ROOT
from regexproof.compiler import compile_pattern
from regexproof.extractors.modsec import count_operators, extract_modsec
from regexproof.io_atomic import atomic_write_lines, atomic_write_text


def measure_coreruleset_sample(
    out_dir: Path, *, as_primary: bool = False
) -> dict[str, Any]:
    """PCRE encodable-fraction gate on pinned CRS sample; go iff >= 0.30.

    Always writes ``coreruleset_sample_encodable_fraction.json``. Only when
    ``as_primary`` (full ``rules/`` absent) may it also write the primary
    ``coreruleset_encodable_fraction.json`` — never overwrite a full-corpus
    primary with the sample report.
    """
    sample = ROOT / "batch" / "corpora" / "coreruleset" / "sample.rules"
    lines = [
        ln.strip()
        for ln in sample.read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    encodable = 0
    for i, pat in enumerate(lines):
        cr = compile_pattern(pat, "", "pcre", "search")
        if cr.encodable:
            encodable += 1
    n = len(lines) or 1
    fraction = encodable / n
    decision = "go" if fraction >= 0.30 else "no-go"
    report = {
        "schema_version": "1",
        "pilot": "coreruleset",
        "dialect": "pcre",
        "sample_size": len(lines),
        "encodable": encodable,
        "fraction": fraction,
        "go_no_go_threshold": 0.3,
        "decision": decision,
        "sample_path": str(sample.relative_to(ROOT)),
        "scope": "sample",
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    atomic_write_text(out_dir / "coreruleset_sample_encodable_fraction.json", payload)
    if as_primary:
        primary = out_dir / "coreruleset_encodable_fraction.json"
        # Never clobber a committed/full-corpus primary when rules/ is absent
        # (CI smoke without materializing CRS).
        keep_full = False
        if primary.is_file():
            try:
                prev = json.loads(primary.read_text(encoding="utf-8"))
                keep_full = prev.get("scope") == "full_corpus"
            except json.JSONDecodeError:
                keep_full = False
        if not keep_full:
            atomic_write_text(primary, payload)
    return report


def measure_coreruleset_full(out_dir: Path) -> dict[str, Any] | None:
    """Full-corpus CRS fraction (modsec extractor + normalize → compile_pcre).

    Returns None when ``batch/corpora/coreruleset/rules`` is not materialized.
    Writes ``coreruleset_encodable_fraction.json`` (primary artifact) and
    ``crs-inventory.ndjson`` for P2/P3 handoff. @rx-only numerator matches the
    Phase-1 GO comment (selectors reported separately).
    """
    from collections import Counter

    import platform as _platform

    import z3

    rules_dir = ROOT / "batch" / "corpora" / "coreruleset" / "rules"
    if not rules_dir.is_dir():
        return None

    records: list[dict[str, Any]] = []
    op_counts: Counter[str] = Counter()
    for fp in sorted(rules_dir.glob("*.conf")):
        src = fp.read_text(encoding="utf-8", errors="replace")
        op_counts.update(count_operators(src))
        rel = str(fp.relative_to(ROOT))
        records.extend(extract_modsec(src, repo="coreruleset/coreruleset", file=rel))

    # Call-time lookup so scripts/measure-p5-guarded.py patching
    # runner._compile_all still reaches CRS full measure (luna #454).
    from regexproof.batch.runner import _compile_all, _discard_streamed_mirrors

    compiled = _compile_all(
        records, lift_inline=True, corpus_slug="coreruleset",
        budget=CORPUS_MANIFESTS.get("coreruleset", {}).get("budget"),
    )
    rows = [pair[0] for pair in compiled]
    _discard_streamed_mirrors(compiled)
    rx_only = [c for c in rows if not c.get("selector")]
    selectors = [c for c in rows if c.get("selector")]
    rx_enc = [c for c in rx_only if c.get("encodable")]
    n = len(rx_only) or 1
    fraction = len(rx_enc) / n
    decision = "go" if fraction >= 0.30 else "no-go"
    reasons = Counter((c.get("compile_reason") or "ok") for c in rx_only)

    out_dir.mkdir(parents=True, exist_ok=True)
    inv_path = out_dir / "crs-inventory.ndjson"
    atomic_write_lines(
        inv_path,
        (
            json.dumps(
                {
                    "regex_id": c.get("regex_id"),
                    "rule_id": c.get("rule_id"),
                    "site": c.get("site"),
                    "pattern": c.get("pattern"),
                    "flags": c.get("flags") or "",
                    "dialect": c.get("dialect"),
                    "call_kind": c.get("call_kind"),
                    "encodable": bool(c.get("encodable")),
                    "compile_reason": c.get("compile_reason"),
                    "negated": c.get("negated"),
                    "selector": bool(c.get("selector")),
                    "corpus": "coreruleset",
                },
                sort_keys=True,
            )
            for c in rows
        ),
    )

    report = {
        "schema_version": "1",
        "pilot": "coreruleset",
        "dialect": "pcre",
        "scope": "full_corpus",
        "corpus_pin": "v4.28.0",
        "sample_size": len(rx_only),
        "encodable": len(rx_enc),
        "fraction": round(fraction, 4),
        "go_no_go_threshold": 0.3,
        "decision": decision,
        "decision_rule": (
            "go iff @rx-only encodable/sample_size >= 0.3 "
            "(normalize_inline_flags → compile_pcre; selectors excluded from fraction)"
        ),
        "reasons": dict(reasons),
        "selectors": {
            "count": len(selectors),
            "encodable": sum(1 for c in selectors if c.get("encodable")),
        },
        "operators": dict(op_counts),
        "extracted_total": len(rows),
        "inventory_path": str(inv_path),
        "engine_versions": {
            "python": _platform.python_version(),
            "z3": z3.get_version_string(),
        },
        "records": [
            {
                "regex_id": c.get("regex_id"),
                "rule_id": c.get("rule_id"),
                "site": c.get("site"),
                "call_kind": c.get("call_kind"),
                "dialect": c.get("dialect"),
                "encodable": bool(c.get("encodable")),
                "reason": c.get("compile_reason"),
                "pattern": (c.get("pattern") or "")[:120],
                "flags": c.get("flags") or "",
                "selector": bool(c.get("selector")),
            }
            for c in rows
        ],
    }
    atomic_write_text(
        out_dir / "coreruleset_encodable_fraction.json",
        json.dumps(report, indent=2, sort_keys=True) + "\n",
    )
    return report


def measure_coreruleset(out_dir: Path) -> dict[str, Any]:
    """Prefer full-corpus fraction when rules/ is present and out_dir is in-repo."""
    try:
        out_dir.resolve().relative_to((ROOT / "properties").resolve())
        in_repo_properties = True
    except ValueError:
        in_repo_properties = False
    if in_repo_properties:
        full = measure_coreruleset_full(out_dir)
        if full is not None:
            # Still emit sample artifact for CI smoke without depending on it for GO.
            measure_coreruleset_sample(out_dir, as_primary=False)
            return full
        # rules/ missing: keep returning a committed full-corpus primary if present.
        primary = out_dir / "coreruleset_encodable_fraction.json"
        if primary.is_file():
            try:
                prev = json.loads(primary.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                prev = {}
            if prev.get("scope") == "full_corpus":
                measure_coreruleset_sample(out_dir, as_primary=False)
                return prev
    return measure_coreruleset_sample(out_dir, as_primary=True)
