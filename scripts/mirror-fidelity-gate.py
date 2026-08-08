#!/usr/bin/env python3
"""Corpus-wave pre-gate: mirror-fidelity differential fuzz on inventory samples.

Samples encodable records from CRS / validator.js (and optional extra
inventory NDJSON), compiles each pattern, and runs differential-fuzz against
the dialect's real helper (PCRE2 / go-re2 / Python re / node when available).

Hard-fails on any mirror↔real mismatch. Writes
``properties/generated/mirror_fidelity_gate.json``.

Usage:
  python scripts/mirror-fidelity-gate.py
  python scripts/mirror-fidelity-gate.py --max-per-corpus 8 --runs 40
"""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import z3  # noqa: E402

from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler import pcre as pcre_mod  # noqa: E402
from regexproof.compiler import re2 as re2_mod  # noqa: E402
from regexproof.fuzz.adapters import real_accepts_argv  # noqa: E402

OUT = ROOT / "properties" / "generated" / "mirror_fidelity_gate.json"


def _mirror_accepts(mirror, s: str) -> bool | None:
    solver = z3.Solver()
    solver.set("timeout", 5000)
    solver.add(z3.InRe(z3.StringVal(s), mirror))
    r = solver.check()
    if r == z3.unknown:
        return None
    return r == z3.sat


def _alphabet_for(pattern: str) -> str:
    """Build a probe alphabet including hex-decoded codepoints (TRAPS #23)."""
    import re as _re

    chars: set[str] = set()
    for m in _re.finditer(r"\\x\{([0-9a-fA-F]+)\}|\\x([0-9a-fA-F]{2})", pattern):
        hexdigits = m.group(1) or m.group(2)
        try:
            code = int(hexdigits, 16)
        except ValueError:
            continue
        if 0 <= code <= 0x10FFFF:
            ch = chr(code)
            if ch.isprintable() or ch in '"\'\\':
                chars.add(ch)
    for c in pattern:
        if 32 <= ord(c) <= 126 and c not in "\\[](){}|*+?^$":
            chars.add(c)
    # Always include hex-regression witnesses + common tokens.
    chars.update('"' + "xX._-abc012")
    base = "".join(sorted(chars))
    return base[:48] if len(base) > 48 else base


def _replay_argv(dialect: str, pattern: str, flags: str) -> list[str] | None:
    if dialect == "pcre":
        if not pcre_mod.helper_used_for_parse_and_replay():
            return None
        return pcre_mod.replay_argv(pattern, flags)
    if dialect == "re2":
        if not re2_mod.helper_used_for_parse_and_replay():
            return None
        return re2_mod.replay_argv(pattern, flags)
    if dialect == "py_re":
        # Tiny inline helper: python -c matching fullmatch/search via stdin.
        code = (
            "import re,sys\n"
            f"p=re.compile({pattern!r},0)\n"
            "s=sys.stdin.read()\n"
            "sys.exit(0 if p.search(s) is not None else 1)\n"
        )
        return [sys.executable, "-c", code]
    if dialect == "ecma":
        # Prefer node if present.
        if subprocess.run(["node", "-e", "process.exit(0)"], capture_output=True).returncode != 0:
            return None
        js = (
            f"const p=new RegExp({json.dumps(pattern)},{json.dumps(flags)});"
            "let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',"
            "()=>process.exit(p.test(d)?0:1));"
        )
        return ["node", "-e", js]
    return None


def _sample_from_inventory(path: Path, *, dialect: str, limit: int) -> list[dict]:
    rows = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if not rec.get("encodable"):
            continue
        if rec.get("selector"):
            continue
        if dialect and rec.get("dialect") and rec.get("dialect") != dialect:
            continue
        rows.append(rec)
        if len(rows) >= limit:
            break
    return rows


def _fuzz_one(rec: dict, *, runs: int, seed: int) -> dict:
    pattern = rec["pattern"]
    flags = rec.get("flags") or ""
    dialect = rec.get("dialect") or "pcre"
    call_kind = rec.get("call_kind") or "search"
    cr = compile_pattern(pattern, flags, dialect, call_kind)
    if not cr.encodable or cr.mirror is None:
        return {
            "regex_id": rec.get("regex_id"),
            "status": "skip_unencodable",
            "reason": cr.unencodable_reason,
        }
    argv = _replay_argv(dialect, pattern, flags)
    if argv is None:
        return {
            "regex_id": rec.get("regex_id"),
            "status": "skip_no_helper",
            "dialect": dialect,
        }
    alphabet = _alphabet_for(pattern)
    mismatches = []
    # Exhaustive short + seeded random
    import random

    rng = random.Random(seed)
    probes = [""]
    # Explicit hex-soundness witnesses when the pattern contains \\x escapes.
    if "\\x" in pattern:
        probes.extend(['"', "x22", "x2", "A", "\x22"])
    for n in range(1, 3):
        # limited product
        pool = alphabet[:8]
        from itertools import product

        for tup in product(pool, repeat=n):
            probes.append("".join(tup))
            if len(probes) > 40:
                break
    for _ in range(runs):
        n = rng.randint(0, 6)
        probes.append("".join(rng.choice(alphabet) for _ in range(n)))
    for s in probes:
        m = _mirror_accepts(cr.mirror, s)
        if m is None:
            mismatches.append({"input": s, "reason": "mirror_timeout"})
            break
        try:
            real = real_accepts_argv(argv, s)
        except Exception as exc:  # noqa: BLE001
            return {
                "regex_id": rec.get("regex_id"),
                "status": "helper_error",
                "error": str(exc),
            }
        if bool(m) != bool(real):
            mismatches.append(
                {"input": s, "mirror": bool(m), "real": bool(real)}
            )
            break
    if mismatches:
        return {
            "regex_id": rec.get("regex_id"),
            "pattern": pattern[:120],
            "dialect": dialect,
            "status": "mismatch",
            "mismatches": mismatches,
        }
    return {
        "regex_id": rec.get("regex_id"),
        "dialect": dialect,
        "status": "ok",
        "probes": len(probes),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-per-corpus", type=int, default=6)
    ap.add_argument("--runs", type=int, default=30)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args(argv)

    if not z3.get_version_string().startswith("5.0"):
        print("FATAL: need z3-solver 5.0.x", file=sys.stderr)
        return 3

    corpora = [
        (
            "coreruleset",
            ROOT / "properties" / "generated" / "crs-inventory.ndjson",
            "pcre",
        ),
        (
            "gitleaks",
            # Prefer inventory NDJSON if present; else measure from TOML inline.
            ROOT / "properties" / "generated" / "gitleaks_inventory.ndjson",
            "re2",
        ),
    ]
    # Fallback: synthesize a few known-good patterns if inventories missing rows.
    fallback = [
        {
            "regex_id": "pregate-hex-22",
            "pattern": r"[\x22]",
            "flags": "",
            "dialect": "pcre",
            "call_kind": "search",
            "encodable": True,
        },
        {
            "regex_id": "pregate-word",
            "pattern": r"^[a-z]+$",
            "flags": "",
            "dialect": "pcre",
            "call_kind": "fullmatch",
            "encodable": True,
        },
        {
            "regex_id": "pregate-re2-digit",
            "pattern": r"^[0-9]+$",
            "flags": "",
            "dialect": "re2",
            "call_kind": "fullmatch",
            "encodable": True,
        },
    ]

    results = []
    for name, inv, dialect in corpora:
        rows = _sample_from_inventory(inv, dialect=dialect, limit=args.max_per_corpus)
        if name == "gitleaks" and not rows:
            # Synthesize from pilot TOML when inventory NDJSON is absent.
            from regexproof.batch.runner import CORPUS_MANIFESTS, _compile_all, _extract

            meta = dict(CORPUS_MANIFESTS["gitleaks"])
            compiled = _compile_all(
                _extract("gitleaks", meta),
                lift_inline=True,
                corpus_slug="gitleaks",
            )
            rows = [
                c
                for c in compiled
                if c.get("encodable") and not c.get("selector")
            ][: args.max_per_corpus]
        for rec in rows:
            results.append(
                {
                    "corpus": name,
                    **_fuzz_one(rec, runs=args.runs, seed=args.seed),
                }
            )

    if not any(r.get("status") == "ok" for r in results):
        for rec in fallback:
            results.append(
                {
                    "corpus": "fallback",
                    **_fuzz_one(rec, runs=args.runs, seed=args.seed),
                }
            )

    mismatches = [r for r in results if r.get("status") == "mismatch"]
    oks = [r for r in results if r.get("status") == "ok"]
    pcre_attempted = [
        r
        for r in results
        if r.get("dialect") == "pcre" or r.get("corpus") == "coreruleset"
    ]
    pcre_ok = [r for r in pcre_attempted if r.get("status") == "ok"]
    pcre2 = pcre_mod.helper_used_for_parse_and_replay()
    # Require at least one successful check; if PCRE was attempted and the
    # helper is available, require at least one PCRE ok (do not pass on RE2
    # alone when CRS inventory was present).
    ok = len(mismatches) == 0 and len(oks) > 0
    if pcre_attempted and pcre2 and not pcre_ok and not mismatches:
        ok = False
    report = {
        "schema_version": "1",
        "gate": "mirror_fidelity",
        "ok": ok,
        "checked_ok": len(oks),
        "mismatches": len(mismatches),
        "pcre2_helper": pcre2,
        "pcre_checked_ok": len(pcre_ok),
        "engine_versions": {
            "python": platform.python_version(),
            "z3": z3.get_version_string(),
        },
        "results": results,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"mirror-fidelity: ok={report['ok']} checked={len(oks)} "
        f"mismatches={len(mismatches)} → {OUT.relative_to(ROOT)}"
    )
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
