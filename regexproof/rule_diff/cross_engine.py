"""Cross-engine rule_diff helpers (Coraza/go-re2 ↔ ModSecurity/pcre).

Same CRS rule text compiled under two dialects. Result classes:

- ``gap`` / ``no-gap`` — both engines encodable; shape-5 SAT/UNSAT
- ``non-comparable-re2`` — go-re2 rejects at parse; pcre encodable
- ``non-comparable-both`` — both reject at parse (counted, not a finding)
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

from regexproof.compiler import compile_pattern
from regexproof.extractors.modsec import extract_modsec

CRS_PIN_PREFIX = "55b09f5"
CRS_EXPECTED_RULE_GLOBS = ("REQUEST-*.conf", "RESPONSE-*.conf")


def preflight_crs(
    rules_dir: Path,
    *,
    pin_prefix: str = CRS_PIN_PREFIX,
    git_root: Path | None = None,
) -> dict[str, Any]:
    """Fail closed unless CRS rules exist at the pinned commit."""
    rules_dir = Path(rules_dir)
    if not rules_dir.is_dir():
        raise SystemExit(f"HARD ERROR: CRS rules root missing: {rules_dir}")
    confs = sorted(rules_dir.glob("*.conf"))
    if not confs:
        raise SystemExit(f"HARD ERROR: no *.conf under {rules_dir}")
    request = list(rules_dir.glob("REQUEST-*.conf"))
    response = list(rules_dir.glob("RESPONSE-*.conf"))
    if len(request) < 5 or len(response) < 1:
        raise SystemExit(
            f"HARD ERROR: CRS rule-file manifest incomplete under {rules_dir} "
            f"(REQUEST={len(request)} RESPONSE={len(response)})"
        )
    root = Path(git_root) if git_root else rules_dir.parent
    if not (root / ".git").exists() and not (root.parent / ".git").exists():
        # Symlink to /tmp/coreruleset-v4.28.0/rules → git root is parent of rules
        cand = rules_dir.resolve().parent
        if (cand / ".git").exists():
            root = cand
    head = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        text=True,
        shell=False,
        timeout=60,  # #543: local git op — bound it
    ).strip()
    if not head.startswith(pin_prefix):
        raise SystemExit(
            f"HARD ERROR: CRS HEAD {head} does not match pin prefix {pin_prefix}"
        )
    return {
        "rules_dir": str(rules_dir),
        "git_root": str(root),
        "head": head,
        "pin_prefix": pin_prefix,
        "n_conf": len(confs),
        "n_request": len(request),
        "n_response": len(response),
    }


def load_crs_rx_records(rules_dir: Path, *, repo: str = "coreruleset/coreruleset") -> list[dict]:
    """Extract @rx records from CRS .conf files (deterministic order)."""
    rules_dir = Path(rules_dir)
    out: list[dict] = []
    for fp in sorted(rules_dir.glob("*.conf")):
        rel = f"rules/{fp.name}"
        src = fp.read_text(encoding="utf-8", errors="replace")
        for rec in extract_modsec(src, repo=repo, file=rel):
            if rec.get("negated"):
                continue
            out.append(rec)
    return out


def classify_cross_engine(
    pattern: str,
    flags: str = "",
    *,
    call_kind: str = "search",
    max_length: int = 256,
) -> dict[str, Any]:
    """Classify one pattern under re2 + pcre compilers."""
    re2 = compile_pattern(pattern, flags, "re2", call_kind, max_length=max_length)
    pcre = compile_pattern(pattern, flags, "pcre", call_kind, max_length=max_length)
    if re2.encodable and pcre.encodable:
        result_class = "comparable"
    elif (not re2.encodable) and pcre.encodable:
        result_class = "non-comparable-re2"
    elif (not re2.encodable) and (not pcre.encodable):
        result_class = "non-comparable-both"
    else:
        # pcre reject, re2 ok — rare; treat as non-comparable-both for table
        result_class = "non-comparable-both"
    return {
        "result_class": result_class,
        "re2_encodable": re2.encodable,
        "pcre_encodable": pcre.encodable,
        "re2_reason": re2.unencodable_reason,
        "pcre_reason": pcre.unencodable_reason,
        "re2": re2,
        "pcre": pcre,
    }


def discover_cross_engine_pairs(
    records: list[dict[str, Any]],
    *,
    max_pairs: int = 40,
    max_classify: int = 400,
    max_len: int = 96,
) -> dict[str, Any]:
    """Classify CRS records and admit comparable pairs for shape-5."""
    class_counts = {
        "comparable": 0,
        "non-comparable-re2": 0,
        "non-comparable-both": 0,
    }
    pairs: list[dict[str, Any]] = []
    seen: set[str] = set()
    classified = 0
    for rec in records:
        if classified >= max_classify:
            break
        pat = rec.get("pattern") or ""
        if not pat or pat in seen:
            continue
        if len(pat) > max_len:
            continue
        seen.add(pat)
        classified += 1
        flags = rec.get("flags") or ""
        info = classify_cross_engine(pat, flags, call_kind="fullmatch")
        class_counts[info["result_class"]] = class_counts.get(info["result_class"], 0) + 1
        if info["result_class"] != "comparable":
            continue
        if len(pairs) >= max_pairs:
            continue
        family = f"crs-cross-engine:{rec.get('rule_id') or rec.get('regex_id') or len(pairs)}"
        pairs.append(
            {
                "family": family,
                "adapter": "crs_cross_engine_coraza_modsec",
                "direction": "re2_to_pcre",
                "direction_label": "Coraza(go-re2) vs ModSecurity(pcre)",
                "call_kind": "search",
                "declared_domain": "ascii",
                "r1": {
                    "pattern": pat,
                    "flags": flags,
                    "dialect": "re2",
                    "engine": "go_re2",
                    "role": "coraza",
                },
                "r2": {
                    "pattern": pat,
                    "flags": flags,
                    "dialect": "pcre",
                    "engine": "pcre2",
                    "role": "modsecurity",
                },
                "file": rec.get("file"),
                "line": rec.get("line"),
                "rule_id": rec.get("rule_id"),
                "regex_id": rec.get("regex_id"),
            }
        )
    return {
        "class_counts": class_counts,
        "classified": classified,
        "admitted_pairs": pairs,
        "unique_patterns": len(seen),
    }
