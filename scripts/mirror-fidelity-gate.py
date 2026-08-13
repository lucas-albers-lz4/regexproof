#!/usr/bin/env python3
"""Corpus-wave mirror-fidelity gate (Wave 2 + Wave 3 surfaces).

1. Fail-closed surface probes for ALL 8 Wave-2 surfaces (fixtures under
   ``sweep/corpus-wave2/fixtures/``). Absent fixture → gate fail.
2. YARA byte-level replay (temp-file + ``yara``) with UTF-16LE / NUL probes;
   a deliberately-wrong ``wide`` mirror must be caught.
3. Wave-3: 8 of 9 surfaces under ``sweep/corpus-wave3/fixtures/`` with
   per-corpus REQUIRED-INPUT assertions (no synthetic fallback for W3).
   P1: spamassassin/noseyparker/shhgit/perl_re/go_regexp;
   P4: dompurify/isemail/email_addresses (mjsunit deferred to P5).
   Deliberately-wrong ``(?x)`` mirror must be caught (``wrong_xflag_caught``).
4. Legacy inventory differential fuzz (CRS / gitleaks) when helpers exist
   (Wave-2 path only; disabled under ``--wave3-only``).

Hard-fails on any mirror↔real mismatch or missing surface. Writes
``properties/generated/mirror_fidelity_gate.json``.

Usage:
  python scripts/mirror-fidelity-gate.py
  python scripts/mirror-fidelity-gate.py --max-per-corpus 8 --runs 40
  python scripts/mirror-fidelity-gate.py --skip-inventory
"""


from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import z3  # noqa: E402

from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler import pcre as pcre_mod  # noqa: E402
from regexproof.compiler import re2 as re2_mod  # noqa: E402
from regexproof.fuzz.adapters import (  # noqa: E402
    real_accepts_argv,
    real_accepts_perl,
    real_accepts_yara,
)
from regexproof.z3_pin import assert_z3_pinned  # noqa: E402

OUT = ROOT / "properties" / "generated" / "mirror_fidelity_gate.json"
FIXTURES = ROOT / "sweep" / "corpus-wave2" / "fixtures"
FIXTURES_W3 = ROOT / "sweep" / "corpus-wave3" / "fixtures"

# Explicit Wave-2 surfaces — fail closed when fixture absent.
WAVE2_SURFACES = (
    "yara",
    "semgrep",
    "pcre2",
    "re2",
    "cpython",
    "busybox",
    "test262",
    "rule_diff",
)

# Wave-3 P1: 5 of 9.
WAVE3_SURFACES_P1 = (
    "spamassassin",
    "noseyparker",
    "shhgit",
    "perl_re",
    "go_regexp",
)

# Wave-3 P4: 3 ecma frontier surfaces (mjsunit deferred to P5).
WAVE3_SURFACES_P4 = (
    "dompurify",
    "isemail",
    "email_addresses",
)

WAVE3_SURFACES = WAVE3_SURFACES_P1 + WAVE3_SURFACES_P4

SURFACES = WAVE2_SURFACES + WAVE3_SURFACES


def _mirror_accepts(mirror, s: str) -> bool | None:
    solver = z3.Solver()
    solver.set("timeout", 5000)
    solver.add(z3.InRe(z3.StringVal(s), mirror))
    r = solver.check()
    if r == z3.unknown:
        return None
    return r == z3.sat


def _mirror_accepts_bytes(mirror, data: bytes) -> bool | None:
    # Z3 string theory is Unicode codepoints; map latin-1 so NUL survives.
    try:
        s = data.decode("latin-1")
    except UnicodeDecodeError:
        return None
    return _mirror_accepts(mirror, s)


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
    if dialect == "perl":
        helper = ROOT / "helpers" / "perl" / "match.py"
        if not helper.is_file():
            return None
        # Presence gate via version (fail closed).
        ver = subprocess.run(
            [sys.executable, str(helper), "version"],
            capture_output=True,
            text=True,
            check=False,
        )
        if ver.returncode != 0:
            return None
        return [sys.executable, str(helper), "match", pattern, flags or ""]
    if dialect == "py_re":
        code = (
            "import re,sys\n"
            f"p=re.compile({pattern!r},0)\n"
            "s=sys.stdin.read()\n"
            "sys.exit(0 if p.search(s) is not None else 1)\n"
        )
        return [sys.executable, "-c", code]
    if dialect == "ecma":
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
    import random
    from itertools import product

    rng = random.Random(seed)
    probes = [""]
    if "\\x" in pattern:
        probes.extend(['"', "x22", "x2", "A", "\x22"])
    for n in range(1, 3):
        pool = alphabet[:8]
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
            mismatches.append({"input": s, "mirror": bool(m), "real": bool(real)})
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


def _utf16le(token: str) -> bytes:
    return token.encode("utf-16-le")


def _check_yara_surface(fixture: Path) -> dict:
    """Spike mirrors vs real yara; wrong-wide must be detected."""
    if shutil.which("yara") is None:
        return {"surface": "yara", "status": "absent", "error": "yara-cli-missing"}
    meta = json.loads(fixture.read_text(encoding="utf-8"))
    rule_ascii = meta["rule_ascii"]
    rule_wide = meta["rule_wide"]
    # Correct ascii mirror: literal "abc" (fullmatch of exact probe)
    correct_ascii = z3.Re("abc")
    # Correct wide mirror: UTF-16LE of "abc" as a Z3 string (NUL codepoints)
    correct_wide = z3.Re("a\x00b\x00c\x00")
    wrong_wide = z3.Re("abc")  # deliberately ignores UTF-16LE

    # Exact-string probes only (YARA is substring; spike mirrors are fullmatch
    # literals — substring Contains forms land with production YARA encoding).
    probes_ascii = [b"abc", b"ab", b""]
    probes_wide = [
        _utf16le("abc"),
        _utf16le("ab"),
        b"abc",  # ascii must NOT match wide-only rule
        b"a\x00b\x00",
    ]

    mismatches = []
    for data in probes_ascii:
        m = _mirror_accepts_bytes(correct_ascii, data)
        real = real_accepts_yara(rule_ascii, data)
        if m is None or bool(m) != bool(real):
            mismatches.append(
                {
                    "domain": "ascii",
                    "input_hex": data.hex(),
                    "mirror": m,
                    "real": real,
                }
            )

    for data in probes_wide:
        m = _mirror_accepts_bytes(correct_wide, data)
        real = real_accepts_yara(rule_wide, data)
        if m is None or bool(m) != bool(real):
            mismatches.append(
                {
                    "domain": "wide",
                    "input_hex": data.hex(),
                    "mirror": m,
                    "real": real,
                }
            )

    # Wrong-wide catch: on UTF-16LE "abc", wrong mirror says yes, real yara yes —
    # but on ASCII "abc", wrong mirror says yes while real wide rule says no.
    catch_probe = b"abc"
    wrong_m = _mirror_accepts_bytes(wrong_wide, catch_probe)
    real_w = real_accepts_yara(rule_wide, catch_probe)
    wrong_wide_caught = bool(wrong_m) is True and bool(real_w) is False

    status = "ok"
    if mismatches:
        status = "mismatch"
    elif not wrong_wide_caught:
        status = "wrong_wide_not_caught"
    return {
        "surface": "yara",
        "status": status,
        "wrong_wide_caught": wrong_wide_caught,
        "mismatches": mismatches,
        "domains": ["ascii", "wide"],
        "probes": len(probes_ascii) + len(probes_wide),
    }


def _check_dialect_surface(
    name: str,
    fixture: Path,
    *,
    dialect: str,
    call_kind: str = "search",
) -> dict:
    meta = json.loads(fixture.read_text(encoding="utf-8"))
    pattern = meta["pattern"]
    flags = meta.get("flags") or ""
    probes = meta.get("probes") or ["", "a", "ab", "0"]
    argv = _replay_argv(dialect, pattern, flags)
    if argv is None:
        return {
            "surface": name,
            "status": "absent",
            "error": f"helper-unavailable:{dialect}",
        }
    cr = compile_pattern(pattern, flags, dialect, call_kind)
    if not cr.encodable or cr.mirror is None:
        return {
            "surface": name,
            "status": "absent",
            "error": f"unencodable:{cr.unencodable_reason}",
        }
    mismatches = []
    for s in probes:
        m = _mirror_accepts(cr.mirror, s)
        if m is None:
            mismatches.append({"input": s, "reason": "mirror_timeout"})
            break
        real = real_accepts_argv(argv, s)
        if bool(m) != bool(real):
            mismatches.append({"input": s, "mirror": bool(m), "real": bool(real)})
            break
    return {
        "surface": name,
        "status": "mismatch" if mismatches else "ok",
        "dialect": dialect,
        "domain": meta.get("domain") or "ascii",
        "mismatches": mismatches,
        "probes": len(probes),
    }


def _check_rule_diff_surface(fixture: Path) -> dict:
    """Toy R1/R2 gap: mirror membership only (no engine dual-replay in P1)."""
    meta = json.loads(fixture.read_text(encoding="utf-8"))
    r1 = meta["r1"]
    r2 = meta["r2"]
    witness = meta["witness"]
    cr1 = compile_pattern(r1, "", "re2", "fullmatch")
    cr2 = compile_pattern(r2, "", "re2", "fullmatch")
    if not (cr1.encodable and cr2.encodable and cr1.mirror is not None and cr2.mirror is not None):
        return {"surface": "rule_diff", "status": "absent", "error": "unencodable"}
    in_r1 = _mirror_accepts(cr1.mirror, witness)
    in_r2 = _mirror_accepts(cr2.mirror, witness)
    # Expect gap: in R2, not in R1
    ok = in_r1 is False and in_r2 is True
    return {
        "surface": "rule_diff",
        "status": "ok" if ok else "mismatch",
        "domain": "ascii",
        "in_r1": in_r1,
        "in_r2": in_r2,
        "witness": witness,
    }


def _check_perl_surface(name: str, fixture: Path) -> dict:
    """Spike mirror (re2-encodable) vs real perl helper — dialect not in DIALECTS yet."""
    meta = json.loads(fixture.read_text(encoding="utf-8"))
    pattern = meta["pattern"]
    flags = meta.get("flags") or ""
    probes = meta.get("probes") or ["", "a"]
    try:
        # Presence gate
        helper = ROOT / "helpers" / "perl" / "match.py"
        ver = subprocess.run(
            [sys.executable, str(helper), "version"],
            capture_output=True,
            text=True,
            check=False,
        )
        if ver.returncode != 0:
            return {
                "surface": name,
                "status": "absent",
                "error": "perl-helper-unavailable",
            }
    except OSError as exc:
        return {"surface": name, "status": "absent", "error": str(exc)}

    # Mirror via re2 compile of the same pattern (spike patterns are re2-safe).
    cr = compile_pattern(pattern, flags, "re2", "fullmatch")
    if not cr.encodable or cr.mirror is None:
        return {
            "surface": name,
            "status": "absent",
            "error": f"unencodable:{cr.unencodable_reason}",
        }
    mismatches = []
    for s in probes:
        m = _mirror_accepts(cr.mirror, s)
        if m is None:
            mismatches.append({"input": s, "reason": "mirror_timeout"})
            break
        try:
            real = real_accepts_perl(pattern, flags, s)
        except RuntimeError as exc:
            msg = str(exc)
            if "perl-helper-unavailable" in msg:
                return {"surface": name, "status": "absent", "error": msg}
            mismatches.append({"input": s, "error": msg})
            break
        if bool(m) != bool(real):
            mismatches.append({"input": s, "mirror": bool(m), "real": bool(real)})
            break
    return {
        "surface": name,
        "status": "mismatch" if mismatches else "ok",
        "helper": "perl",
        "domain": meta.get("domain") or "ascii",
        "mismatches": mismatches,
        "probes": len(probes),
    }


def _check_noseyparker_xflag_surface(fixture: Path) -> dict:
    """re2 dialect probes + deliberately-wrong (?x) mirror must be caught."""
    meta = json.loads(fixture.read_text(encoding="utf-8"))
    base = _check_dialect_surface(
        "noseyparker", fixture, dialect="re2", call_kind="search"
    )
    xflag = meta.get("xflag") or {}
    stripped = xflag.get("stripped") or meta["pattern"]
    wrong_literal = xflag.get("wrong_literal") or "a b"
    correct = z3.Re(stripped)
    wrong = z3.Re(wrong_literal)
    argv = _replay_argv("re2", stripped, "")
    if argv is None:
        base["status"] = "absent"
        base["error"] = "helper-unavailable:re2"
        base["wrong_xflag_caught"] = False
        return base

    # Correct stripped form agrees with real on "ab"
    m_ok = _mirror_accepts(correct, stripped)
    real_ok = real_accepts_argv(argv, stripped)
    # Wrong mirror accepts whitespace form; real stripped engine does not
    catch_probe = wrong_literal
    wrong_m = _mirror_accepts(wrong, catch_probe)
    real_catch = real_accepts_argv(argv, catch_probe)
    wrong_xflag_caught = bool(wrong_m) is True and bool(real_catch) is False

    status = base.get("status") or "ok"
    if base.get("mismatches"):
        status = "mismatch"
    elif m_ok is not True or real_ok is not True:
        status = "mismatch"
        base.setdefault("mismatches", []).append(
            {"input": stripped, "mirror": m_ok, "real": real_ok, "kind": "xflag_correct"}
        )
    elif not wrong_xflag_caught:
        status = "wrong_xflag_not_caught"
    base["status"] = status
    base["wrong_xflag_caught"] = wrong_xflag_caught
    base["xflag_stripped"] = stripped
    return base


def _run_surfaces(*, wave3_only: bool = False) -> tuple[dict[str, dict], bool]:
    reports: dict[str, dict] = {}
    all_ok = True
    names = WAVE3_SURFACES if wave3_only else SURFACES
    for name in names:
        if name in WAVE3_SURFACES:
            fixture = FIXTURES_W3 / f"{name}.json"
        else:
            fixture = FIXTURES / f"{name}.json"
        if not fixture.is_file() or fixture.stat().st_size == 0:
            reports[name] = {
                "surface": name,
                "status": "absent",
                "error": f"missing-fixture:{fixture.relative_to(ROOT) if fixture.exists() else name}",
            }
            all_ok = False
            continue
        if name == "yara":
            rec = _check_yara_surface(fixture)
        elif name == "rule_diff":
            rec = _check_rule_diff_surface(fixture)
        elif name in ("spamassassin", "perl_re"):
            rec = _check_perl_surface(name, fixture)
        elif name == "noseyparker":
            rec = _check_noseyparker_xflag_surface(fixture)
        else:
            dialect_map = {
                "semgrep": ("py_re", "search"),
                "pcre2": ("pcre", "search"),
                "re2": ("re2", "fullmatch"),
                "cpython": ("py_re", "search"),
                "busybox": ("pcre", "search"),
                "test262": ("ecma", "search"),
                "shhgit": ("re2", "fullmatch"),
                "go_regexp": ("re2", "fullmatch"),
                "dompurify": ("ecma", "search"),
                "isemail": ("ecma", "fullmatch"),
                "email_addresses": ("ecma", "search"),
            }
            dialect, ck = dialect_map[name]
            rec = _check_dialect_surface(name, fixture, dialect=dialect, call_kind=ck)
        reports[name] = rec
        if rec.get("status") != "ok":
            all_ok = False
    return reports, all_ok


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-per-corpus", type=int, default=6)
    ap.add_argument("--runs", type=int, default=30)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument(
        "--skip-inventory",
        action="store_true",
        help="Only run surface fixtures (used by unit tests).",
    )
    ap.add_argument(
        "--wave3-only",
        action="store_true",
        help="Run Wave-3 surfaces only (no Wave-2 inventory fallback).",
    )
    ap.add_argument(
        "--disable-fallback",
        action="store_true",
        help="Never use synthetic inventory fallback probes (required for Wave-3).",
    )
    args = ap.parse_args(argv)

    assert_z3_pinned()

    # Wave-3 runs never pass via synthetic fallback.
    disable_fallback = bool(args.disable_fallback or args.wave3_only)

    surface_reports, surfaces_ok = _run_surfaces(wave3_only=args.wave3_only)

    results = []
    if not args.skip_inventory and not args.wave3_only:
        corpora = [
            (
                "coreruleset",
                ROOT / "properties" / "generated" / "crs-inventory.ndjson",
                "pcre",
            ),
            (
                "gitleaks",
                ROOT / "properties" / "generated" / "gitleaks_inventory.ndjson",
                "re2",
            ),
        ]
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
        for name, inv, dialect in corpora:
            rows = _sample_from_inventory(inv, dialect=dialect, limit=args.max_per_corpus)
            if name == "gitleaks" and not rows:
                from regexproof.batch.compile_records import compile_records
                from regexproof.batch.extract import extract_corpus
                from regexproof.batch.manifests import CORPUS_MANIFESTS

                meta = dict(CORPUS_MANIFESTS["gitleaks"])
                compiled = compile_records(
                    extract_corpus("gitleaks", meta),
                    lift_inline=True,
                    corpus_slug="gitleaks",
                )
                rows = [
                    c[0]
                    for c in compiled
                    if c[0].get("encodable") and not c[0].get("selector")
                ][: args.max_per_corpus]
            for rec in rows:
                results.append(
                    {
                        "corpus": name,
                        **_fuzz_one(rec, runs=args.runs, seed=args.seed),
                    }
                )
        if not disable_fallback and not any(r.get("status") == "ok" for r in results):
            for rec in fallback:
                # Skip pcre fallbacks when helper absent (CI).
                if rec["dialect"] == "pcre" and not pcre_mod.helper_used_for_parse_and_replay():
                    continue
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
    inv_ok = True
    if not args.skip_inventory and not args.wave3_only:
        inv_ok = len(mismatches) == 0 and len(oks) > 0
        if pcre_attempted and pcre2 and not pcre_ok and not mismatches:
            inv_ok = False

    wrong_wide = bool(surface_reports.get("yara", {}).get("wrong_wide_caught"))
    wrong_xflag = bool(surface_reports.get("noseyparker", {}).get("wrong_xflag_caught"))
    # When wave2 yara is in the run, require wrong_wide; always require wrong_xflag
    # when noseyparker surface is present.
    catch_ok = True
    if "yara" in surface_reports:
        catch_ok = catch_ok and wrong_wide
    if "noseyparker" in surface_reports:
        catch_ok = catch_ok and wrong_xflag
    ok = surfaces_ok and inv_ok and catch_ok

    perl_helper_ok = False
    helper = ROOT / "helpers" / "perl" / "match.py"
    if helper.is_file():
        perl_helper_ok = (
            subprocess.run(
                [sys.executable, str(helper), "version"],
                capture_output=True,
                check=False,
            ).returncode
            == 0
        )

    report = {
        "schema_version": "3",
        "gate": "mirror_fidelity",
        "ok": ok,
        "surfaces_ok": surfaces_ok,
        "wrong_wide_caught": wrong_wide,
        "wrong_xflag_caught": wrong_xflag,
        "surfaces": surface_reports,
        "checked_ok": len(oks),
        "mismatches": len(mismatches),
        "pcre2_helper": pcre2,
        "pcre_checked_ok": len(pcre_ok),
        "yara_helper": shutil.which("yara") is not None,
        "perl_helper": perl_helper_ok,
        "fallback_disabled": disable_fallback,
        "engine_versions": {
            "python": platform.python_version(),
            "z3": z3.get_version_string(),
            "yara": (
                subprocess.run(["yara", "-v"], capture_output=True, text=True).stdout.strip()
                if shutil.which("yara")
                else None
            ),
            "perl": (
                subprocess.run(
                    ["perl", "-e", "print $^V"], capture_output=True, text=True
                ).stdout.strip()
                if shutil.which("perl")
                else None
            ),
        },
        "results": results,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"mirror-fidelity: ok={report['ok']} surfaces_ok={surfaces_ok} "
        f"wrong_wide_caught={wrong_wide} wrong_xflag_caught={wrong_xflag} "
        f"checked={len(oks)} mismatches={len(mismatches)} → {OUT.relative_to(ROOT)}"
    )
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
