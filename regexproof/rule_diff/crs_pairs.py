"""CRS shape-5 pair discovery: version-diff + sibling-family.

CRS adapter (documented): R1 for same-ID adjacent-tag pairs is intentionally
**rule-derived** (the prior release's pattern). That is the security question
("did R2 widen / change acceptance vs R1?"). Do **not** route CRS through
``reject_rule_derived_r1`` — that gate is for independent-spec corpora
(gitleaks). Integrity for CRS is:

- same-ID pairs: R1.rule_id == R2.rule_id, R1 from older tag, R2 from newer
- sibling-family: only with an explicit ``family_contract`` (R1, R2,
  provenance). Default discovery does not admit sibling pairs (#469).

Unchanged same-ID patterns are skipped (vacuous). Direction is always
``r2_minus_r1`` (shape-5: R2 accepts something R1 misses).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from regexproof.compiler import compile_pattern
from regexproof.compiler.normalize import normalize_inline_flags
from regexproof.extractors.modsec import extract_modsec
from regexproof.regex_id import make_regex_id
from regexproof.rule_diff.pairs import DEFAULT_MAX_LEN, _min_literal_span

ADMITTED_SCHEMA_VERSION = "1"
_FAMILY_PREFIX = re.compile(r"^(\d{3})")


def _load_rules(rules_dir: Path, *, tag: str) -> dict[str, dict[str, Any]]:
    """Index @rx records by rule_id (selectors excluded)."""
    by_id: dict[str, dict[str, Any]] = {}
    for fp in sorted(rules_dir.glob("*.conf")):
        recs = extract_modsec(
            fp.read_text(encoding="utf-8", errors="replace"),
            repo="coreruleset/coreruleset",
            file=str(fp),
        )
        for rec in recs:
            if rec.get("selector"):
                continue
            rid = rec.get("rule_id")
            if not rid:
                continue
            if rid in by_id:
                continue
            by_id[rid] = {**rec, "tag": tag}
    return by_id


def _family(rule_id: str) -> str | None:
    m = _FAMILY_PREFIX.match(rule_id)
    return m.group(1) if m else None


def _side(rec: dict[str, Any], *, compile_max_len: int = 256) -> dict[str, Any] | None:
    pat, flags = normalize_inline_flags(rec["pattern"], rec.get("flags") or "")
    cr = compile_pattern(pat, flags, "pcre", "fullmatch", max_length=compile_max_len)
    if not cr.encodable:
        return None
    site = rec.get("site") or f"crs:{rec.get('tag')}:{rec.get('rule_id')}:0:0"
    return {
        "pattern": pat,
        "flags": flags,
        "dialect": "pcre",
        "call_kind": "search",
        "site": site,
        "rule_id": rec.get("rule_id"),
        "tag": rec.get("tag"),
        "regex_id": rec.get("regex_id")
        or make_regex_id(
            repo="coreruleset/coreruleset",
            pattern=pat,
            flags=flags,
            dialect="pcre",
            call_kind="search",
            site=site,
        ),
        "declared_domain": cr.declared_domain or "ascii",
    }


def _make_pair(
    *,
    pair_id: str,
    family: str,
    pair_kind: str,
    r1: dict[str, Any],
    r2: dict[str, Any],
    max_len: int,
    provenance: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": ADMITTED_SCHEMA_VERSION,
        "pair_id": pair_id,
        "direction": "r2_minus_r1",
        "regex_id_r1": r1["regex_id"],
        "regex_id_r2": r2["regex_id"],
        "r1": r1,
        "r2": r2,
        "provenance": provenance,
        "call_kind": "search",
        "declared_domain": r2.get("declared_domain") or "ascii",
        "max_len": max_len,
        "family": family,
        "pair_kind": pair_kind,
        "adapter": provenance.get("adapter"),
        "adapter_note": provenance.get("adapter_note"),
        "direction_label": provenance.get("direction_label"),
    }


def discover_crs_version_pairs(
    *,
    older_rules: Path,
    newer_rules: Path,
    older_tag: str = "v4.27.0",
    newer_tag: str = "v4.28.0",
    max_len: int = DEFAULT_MAX_LEN,
) -> dict[str, Any]:
    """Same-ID pairs across adjacent tags; R1=older, R2=newer."""
    old = _load_rules(older_rules, tag=older_tag)
    new = _load_rules(newer_rules, tag=newer_tag)
    admitted: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []
    for rid in sorted(set(old) & set(new)):
        if old[rid]["pattern"] == new[rid]["pattern"]:
            dropped.append(
                {"rule_id": rid, "reason": "unchanged-id", "pair_kind": "version_diff"}
            )
            continue
        r1 = _side(old[rid])
        r2 = _side(new[rid])
        if r1 is None or r2 is None:
            dropped.append(
                {
                    "rule_id": rid,
                    "reason": "unencodable",
                    "pair_kind": "version_diff",
                }
            )
            continue
        if _min_literal_span(r2["pattern"]) > max_len:
            dropped.append(
                {
                    "rule_id": rid,
                    "reason": "length-bound-exceeded",
                    "pair_kind": "version_diff",
                }
            )
            continue
        admitted.append(
            _make_pair(
                pair_id=f"crs-{rid}-{older_tag}-{newer_tag}",
                family=f"RD-crs-{rid}-version",
                pair_kind="version_diff",
                r1=r1,
                r2=r2,
                max_len=max_len,
                provenance={
                    "adapter": "crs_rule_derived_r1",
                    "adapter_note": (
                        "R1 is the prior-tag CRS rule (intentionally rule-derived); "
                        "reject_rule_derived_r1 does not apply to this adapter"
                    ),
                    "direction_label": f"{older_tag}->{newer_tag}",
                    "older_tag": older_tag,
                    "newer_tag": newer_tag,
                    "rule_id": rid,
                },
            )
        )
    return {
        "schema_version": ADMITTED_SCHEMA_VERSION,
        "pair_kind": "version_diff",
        "older_tag": older_tag,
        "newer_tag": newer_tag,
        "admitted": admitted,
        "dropped": dropped,
        "admitted_count": len(admitted),
        "dropped_count": len(dropped),
    }


def _valid_family_contract(family_contract: object) -> bool:
    if not isinstance(family_contract, dict):
        return False
    return all(str(family_contract.get(key) or "").strip() for key in ("R1", "R2", "provenance"))


def discover_crs_sibling_pairs(
    *,
    rules_dir: Path,
    tag: str = "v4.28.0",
    max_len: int = DEFAULT_MAX_LEN,
    max_pairs_per_family: int = 8,
    family_contract: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Sibling rules within a family (e.g. 942xxx); R1=lower id, R2=higher id.

    Requires an explicit ``family_contract`` (same field as the CRS
    cross-engine report). Without it, nothing is admitted — sibling SAT is
    not a version-diff or engine-parity theorem (#469).
    """
    empty = {
        "schema_version": ADMITTED_SCHEMA_VERSION,
        "pair_kind": "sibling_family",
        "tag": tag,
        "admitted": [],
        "dropped": [],
        "admitted_count": 0,
        "dropped_count": 0,
    }
    if not _valid_family_contract(family_contract):
        empty["dropped"] = [
            {
                "reason": "missing-family-contract",
                "pair_kind": "sibling_family",
            }
        ]
        empty["dropped_count"] = 1
        return empty
    empty["family_contract"] = family_contract
    by_id = _load_rules(rules_dir, tag=tag)
    families: dict[str, list[str]] = {}
    for rid in by_id:
        fam = _family(rid)
        if fam:
            families.setdefault(fam, []).append(rid)

    admitted: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    for fam, ids in sorted(families.items()):
        encodable: list[tuple[str, dict[str, Any]]] = []
        for rid in sorted(ids):
            enc = _side(by_id[rid])
            if enc is None:
                dropped.append(
                    {
                        "rule_id": rid,
                        "reason": "unencodable",
                        "pair_kind": "sibling_family",
                        "family_prefix": fam,
                    }
                )
                continue
            encodable.append((rid, enc))
        count = 0
        for i in range(len(encodable) - 1):
            if count >= max_pairs_per_family:
                break
            rid1, r1 = encodable[i]
            rid2, r2 = encodable[i + 1]
            key = (rid1, rid2)
            if key in seen:
                continue
            seen.add(key)
            if r1["pattern"] == r2["pattern"]:
                dropped.append(
                    {
                        "rule_id": f"{rid1}/{rid2}",
                        "reason": "identical-patterns",
                        "pair_kind": "sibling_family",
                    }
                )
                continue
            if _min_literal_span(r2["pattern"]) > max_len:
                dropped.append(
                    {
                        "rule_id": f"{rid1}/{rid2}",
                        "reason": "length-bound-exceeded",
                        "pair_kind": "sibling_family",
                    }
                )
                continue
            admitted.append(
                _make_pair(
                    pair_id=f"crs-{fam}-{rid1}-{rid2}-sibling",
                    family=f"RD-crs-{fam}-{rid1}-{rid2}-sibling",
                    pair_kind="sibling_family",
                    r1=r1,
                    r2=r2,
                    max_len=max_len,
                    provenance={
                        "adapter": "crs_sibling_family",
                        "adapter_note": (
                            "Both sides are CRS rules from the same tag; "
                            "reject_rule_derived_r1 does not apply"
                        ),
                        "direction_label": f"{rid1}->{rid2}",
                        "tag": tag,
                        "family_prefix": fam,
                    },
                )
            )
            count += 1

    return {
        "schema_version": ADMITTED_SCHEMA_VERSION,
        "pair_kind": "sibling_family",
        "tag": tag,
        "family_contract": family_contract,
        "admitted": admitted,
        "dropped": dropped,
        "admitted_count": len(admitted),
        "dropped_count": len(dropped),
    }


def discover_crs_pairs(
    *,
    older_rules: Path,
    newer_rules: Path,
    older_tag: str = "v4.27.0",
    newer_tag: str = "v4.28.0",
    max_len: int = DEFAULT_MAX_LEN,
) -> dict[str, Any]:
    """Version-diff pairs only. Sibling-family pairing is not a theorem (#469)."""
    ver = discover_crs_version_pairs(
        older_rules=older_rules,
        newer_rules=newer_rules,
        older_tag=older_tag,
        newer_tag=newer_tag,
        max_len=max_len,
    )
    admitted = sorted(ver["admitted"], key=lambda p: p["pair_id"])
    return {
        "schema_version": ADMITTED_SCHEMA_VERSION,
        "older_tag": older_tag,
        "newer_tag": newer_tag,
        "admitted": admitted,
        "dropped": ver["dropped"],
        "admitted_count": len(admitted),
        "dropped_count": len(ver["dropped"]),
        "version_diff_admitted": ver["admitted_count"],
        "sibling_admitted": 0,
    }
