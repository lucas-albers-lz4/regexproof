#!/usr/bin/env python3
"""P1 spike (#86): pattern-final ``(?:...|$)`` encoding wall-clock + soundness.

Evidence-only — does not change the compiler accept path. Builds hand mirrors
for ``search(X(?:R|$))`` via string-split of pattern-final ``|$)``:

  E1 (preferred): ``InRe(s, search(X·R)) ∨ InRe(s, search(X$))``
                  (empty X under search/exec → universal language for the
                  ``$`` branch, since empty-at-EOS matches every string)
  E2 (bounded):   ``InRe(s, Star·(X·R)) ∨ InRe(s, Star·X)`` with ``len(s)≤N``

Tractability gate (AC-P1): membership + sat-find on the *tractability cohort*
(toys, ids_rules, shape-reduced gitleaks) must decide in <5s. Full secret-
detector kw/``\\b`` patterns are also measured; unconstrained sat-find often
times out on those shapes even for XR alone (large ``{n}`` / ``{0,50}``) —
that hardness is recorded but is not an encoding failure when membership is
instant and soundness is clean (same stance as word-boundary spike).

Usage:
  .venv/bin/python scripts/spike-trailing-alt-dollar.py
  .venv/bin/python scripts/spike-trailing-alt-dollar.py --out properties/generated/trailing_alt_dollar_spike.json

Exit 0 on completed matrix (GO / GO-BOUNDED / NO-GO recorded in JSON).
Exit 3 on wrong z3-solver version.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import z3  # noqa: E402
from z3 import And, BoolVal, Concat, InRe, Length, Or, Solver, String  # noqa: E402

from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler.base import CompileResult, any_char  # noqa: E402
from regexproof.compiler.lower import ranges_excluding  # noqa: E402
from regexproof.compiler.re2 import replay_argv  # noqa: E402
from regexproof.fuzz.adapters import real_accepts_argv  # noqa: E402

_WORD_CODES = frozenset(
    list(range(ord("a"), ord("z") + 1))
    + list(range(ord("A"), ord("Z") + 1))
    + list(range(ord("0"), ord("9") + 1))
    + [ord("_")]
)

if not z3.get_version_string().startswith("5.0"):
    print(
        f"FATAL: z3-solver {z3.get_version_string()} — spike validated on 5.0.x only.",
        file=sys.stderr,
    )
    sys.exit(3)

TIMEOUT_MS = 5000
GO_WALL_MS = 5000
E2_LEN_BOUND = 256
OUT_DEFAULT = ROOT / "properties" / "generated" / "trailing_alt_dollar_spike.json"
GITLEAKS_FROZEN = ROOT / "properties" / "generated" / "gitleaks-frozen-ids.ndjson"

TOYS = [
    {"id": "toy-a-dollar", "pattern": "(?:a|$)", "bucket": "toy"},
    {"id": "toy-foo-bar", "pattern": "foo(?:bar|$)", "bucket": "toy"},
    {"id": "toy-x-ab", "pattern": "x(?:a|b|$)", "bucket": "toy"},
    {
        "id": "toy-mid-control",
        "pattern": "a(?:$|b)c",
        "bucket": "control-reject",
        "expect_split": False,
    },
    {
        "id": "toy-caret-branch",
        "pattern": "(?:^|a)",
        "bucket": "control-reject",
        "expect_split": False,
    },
]

# Shape-reduced gitleaks-like (encoding tractability without {0,50}? / {93}).
REDUCED = [
    {
        "id": "reduced-adafruit",
        "pattern": r"(?:adafruit)=([a-z0-9_-]{32})(?:[\x60'\"\s;]|$)",
        "bucket": "reduced",
        "dialect": "re2",
    },
    {
        "id": "reduced-delim",
        "pattern": r"secret([a-z0-9]{16})(?:[\x60'\"\s;]|\\[nr]|$)",
        "bucket": "reduced",
        "dialect": "re2",
    },
    {
        "id": "reduced-b-short",
        "pattern": r"\b(TOK[A-Z0-9]{8})(?:[\x60'\"\s;]|$)",
        "bucket": "reduced",
        "dialect": "re2",
    },
]

IDS_SAMPLES = [
    {"id": "ids-0-amp", "pattern": "^0+(?:&|$)", "bucket": "ids_rules", "dialect": "pcre"},
    {
        "id": "ids-hta",
        "pattern": r"\.hta(?:[?&]|$)",
        "bucket": "ids_rules",
        "dialect": "pcre",
        "flags": "i",
    },
    {
        "id": "ids-hex64",
        "pattern": "^[a-f0-9]{64}(?:&|$)",
        "bucket": "ids_rules",
        "dialect": "pcre",
    },
]

TRACTABILITY_BUCKETS = frozenset({"toy", "ids_rules", "reduced"})
CORPUS_BUCKETS = frozenset({"gitleaks-kw", "gitleaks-b", "gitleaks-other"})


def split_trailing_dollar(pattern: str) -> dict[str, str] | None:
    """Split pattern-final ``(?:...|$)`` into XR / X$ / X bare strings."""
    if not pattern.endswith("|$)") :
        return None
    open_idx = pattern.rfind("(?:")
    if open_idx < 0:
        return None
    xr = pattern[:-3] + ")"
    x_bare = pattern[:open_idx]
    x_dollar = x_bare + "$" if x_bare else ""  # empty X → special-cased in E1
    return {"xr": xr, "x_dollar": x_dollar, "x_bare": x_bare, "empty_x": not x_bare}


def _load_gitleaks_paa() -> list[dict]:
    rows: list[dict] = []
    for line in GITLEAKS_FROZEN.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        pattern = rec["pattern"]
        cr = compile_pattern(pattern, dialect="re2", call_kind="search")
        if cr.unencodable_reason != "per-alternative-anchor":
            continue
        rows.append(
            {
                "id": rec["regex_id"],
                "pattern": pattern,
                "bucket": _gitleaks_bucket(pattern),
                "dialect": "re2",
            }
        )
    return rows


def _gitleaks_bucket(pattern: str) -> str:
    if pattern.startswith("[\\w.-]"):
        return "gitleaks-kw"
    if pattern.startswith("\\b"):
        return "gitleaks-b"
    return "gitleaks-other"


def stratify_samples(paa: list[dict], *, n_kw: int = 5, n_b: int = 3) -> list[dict]:
    kw = [r for r in paa if r["bucket"] == "gitleaks-kw"]
    b = [r for r in paa if r["bucket"] == "gitleaks-b"]
    other = [r for r in paa if r["bucket"] == "gitleaks-other"]
    return kw[:n_kw] + b[:n_b] + other[:1]


def _compile(pattern: str, *, dialect: str, call_kind: str, flags: str = ""):
    return compile_pattern(pattern, flags=flags, dialect=dialect, call_kind=call_kind)


def wb_leading_suffix_mirror(x_bare: str, *, dialect: str, flags: str):
    """Faithful ``\\b INNER $``: INNER at EOS with a leading ASCII word boundary.

    The stock compiler over-approximates ``\\b INNER $`` because ``$`` lands
    *inside* ``WordBounded`` and the leading-only wrap still appends
    ``Star(any)`` (false-SAT). Spike uses this correct end-anchored form.
    """
    assert x_bare.startswith("\\b")
    inner_pat = x_bare[2:]
    if inner_pat.endswith("\\b"):
        inner_pat = inner_pat[:-2]
    cr = _compile(inner_pat, dialect=dialect, call_kind="fullmatch", flags=flags)
    if not cr.encodable:
        return None, cr.unencodable_reason
    inner = cr.mirror
    nw = ranges_excluding(set(_WORD_CODES))
    any_c = any_char()
    # (^|\\W) INNER $  — no trailing Star.
    mirror = z3.Union(inner, Concat(z3.Star(any_c), nw, inner))
    return mirror, None


def build_e1(xr_mirror, x_dollar_mirror, s, *, empty_x: bool, call_kind: str):
    """E1 predicate. Empty X + search/exec → ``$`` matches every string."""
    if empty_x and call_kind in ("search", "exec", "substitution"):
        return Or(InRe(s, xr_mirror), BoolVal(True))
    if empty_x:
        # match/fullmatch: ``$`` ≡ ε → whole string empty OR match body
        return Or(InRe(s, xr_mirror), InRe(s, z3.Re("")))
    return Or(InRe(s, xr_mirror), InRe(s, x_dollar_mirror))


def build_e2(xr_body, x_body, s, *, len_bound: int, empty_x: bool):
    star = z3.Star(any_char())
    if empty_x:
        right = InRe(s, z3.Re(""))  # under-approx; E2 is secondary
    else:
        right = InRe(s, Concat(star, x_body))
    return And(Length(s) <= len_bound, Or(InRe(s, Concat(star, xr_body)), right))


def solve_constraint(constraint, s, *, timeout_ms: int) -> dict:
    solver = Solver()
    solver.set("timeout", timeout_ms)
    solver.add(constraint)
    t0 = time.perf_counter()
    result = solver.check()
    wall_ms = round((time.perf_counter() - t0) * 1000.0, 2)
    out: dict = {"result": str(result), "wall_ms": wall_ms, "witness": None}
    if result == z3.sat:
        model = solver.model()
        for decl in model.decls():
            if decl.name() == s.decl().name():
                val = model[decl]
                try:
                    out["witness"] = val.as_string()
                except Exception:  # noqa: BLE001
                    out["witness"] = str(val)
                break
    return out


def membership(constraint_fn, text: str, *, timeout_ms: int = 10000) -> dict:
    s = String("s")
    solver = Solver()
    solver.set("timeout", timeout_ms)
    solver.add(constraint_fn(s))
    solver.add(s == z3.StringVal(text))
    t0 = time.perf_counter()
    result = solver.check()
    wall_ms = round((time.perf_counter() - t0) * 1000.0, 2)
    if result == z3.unknown:
        return {"result": "unknown", "wall_ms": wall_ms, "accepts": None}
    return {"result": str(result), "wall_ms": wall_ms, "accepts": result == z3.sat}


def py_re_accepts(pattern: str, text: str, *, flags: str, call_kind: str) -> bool:
    fl = 0
    if "i" in flags:
        fl |= re.IGNORECASE
    if "m" in flags:
        fl |= re.MULTILINE
    if "s" in flags:
        fl |= re.DOTALL
    cre = re.compile(pattern, fl)
    if call_kind == "fullmatch":
        return cre.fullmatch(text) is not None
    if call_kind == "match":
        return cre.match(text) is not None
    return cre.search(text) is not None


def re2_accepts(pattern: str, text: str, *, flags: str) -> bool | None:
    try:
        argv = replay_argv(pattern, flags)
    except Exception:  # noqa: BLE001
        return None
    try:
        return real_accepts_argv(argv, text, timeout=5.0)
    except Exception:  # noqa: BLE001
        return None


def _accept_candidates(pattern: str, split: dict, witness: str | None) -> list[str]:
    """Build short accept/reject probes for soundness."""
    out: list[str] = []
    if witness:
        out.append(witness)
    if split.get("empty_x"):
        out.extend(["", "a", "foo", "xyz"])
    elif pattern == "foo(?:bar|$)":
        out.extend(["foo", "foobar", "xfoo", "foobarz", "bar"])
    elif pattern == "x(?:a|b|$)":
        out.extend(["x", "xa", "xb", "zxa", "ab"])
    elif pattern.startswith("^0+"):
        out.extend(["0", "000", "0&", "x0", "1"])
    elif ".hta" in pattern:
        out.extend([".hta", "x.hta?", "HTA", "nope"])
    elif pattern.startswith("^[a-f0-9]{64}"):
        hx = "a" * 64
        out.extend([hx, hx + "&", "b" * 63, "g" * 64])
    elif "adafruit" in pattern and "[a-z0-9_-]{32}" in pattern:
        tok = "a" * 32
        out.extend(
            [
                f"adafruit={tok};",
                f"adafruit={tok}",
                f"xadafruit={tok};",
                "adafruit=short;",
                "zzz_nomatch_zzz",
            ]
        )
    elif pattern.startswith("\\b(TOK"):
        out.extend(["TOKABCDEF12", "TOKABCDEF12;", "xTOKABCDEF12", "TOKSHORT", ""])
    elif "secret(" in pattern:
        tok = "b" * 16
        out.extend([f"secret{tok};", f"secret{tok}", "secret", "zzz"])
    else:
        out.extend(["", "a", "zzz_nomatch_zzz"])
        # Reject-only probes for heavy corpus shapes (accept built when cheap).
        m = re.search(r"\(\?:([a-z0-9_-]{3,32})\)", pattern, re.I)
        if m:
            out.append(m.group(1))
    # Dedup preserve order
    seen: set[str] = set()
    uniq = []
    for t in out:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq


def soundness_check(
    pattern: str,
    *,
    dialect: str,
    flags: str,
    call_kind: str,
    e1_fn,
    split: dict,
    witness: str | None,
) -> dict:
    mismatches: list[dict] = []
    membership_walls: list[float] = []
    checked = 0
    for text in _accept_candidates(pattern, split, witness):
        mem = membership(e1_fn, text)
        membership_walls.append(mem["wall_ms"])
        if mem["accepts"] is None:
            mismatches.append({"s": text, "error": "mirror-timeout", "wall_ms": mem["wall_ms"]})
            continue
        m_acc = mem["accepts"]
        py_acc = py_re_accepts(pattern, text, flags=flags, call_kind=call_kind)
        real = re2_accepts(pattern, text, flags=flags) if dialect == "re2" else py_acc
        engine = "re2" if dialect == "re2" else "py_re"
        checked += 1
        if real is not None and m_acc != real:
            mismatches.append(
                {
                    "s": text,
                    "mirror": m_acc,
                    "engine": engine,
                    "real": real,
                    "py_re": py_acc,
                    "wall_ms": mem["wall_ms"],
                }
            )
        elif dialect != "py_re" and m_acc != py_acc:
            # Informational when primary engine agrees (ASCII vs Unicode, etc.).
            mismatches.append(
                {
                    "s": text,
                    "mirror": m_acc,
                    "engine": "py_re",
                    "real": py_acc,
                    "note": "informational",
                    "wall_ms": mem["wall_ms"],
                }
            )
    hard = [m for m in mismatches if m.get("note") != "informational"]
    return {
        "checked": checked,
        "mismatches": hard,
        "max_membership_ms": max(membership_walls) if membership_walls else 0,
        "membership_walls_ms": membership_walls,
    }


def run_sample(sample: dict, *, encodings: list[str], timeout_ms: int) -> list[dict]:
    pattern = sample["pattern"]
    dialect = sample.get("dialect", "re2")
    flags = sample.get("flags", "")
    call_kind = sample.get("call_kind", "search")
    expect_split = sample.get("expect_split", True)
    split = split_trailing_dollar(pattern)
    rows: list[dict] = []
    base = {
        "id": sample["id"],
        "pattern": pattern,
        "bucket": sample.get("bucket"),
        "dialect": dialect,
        "flags": flags,
        "call_kind": call_kind,
        "split": split,
    }

    if split is None:
        cr = _compile(pattern, dialect=dialect, call_kind=call_kind, flags=flags)
        rows.append(
            {
                **base,
                "encoding": None,
                "encodable_today": cr.encodable,
                "compile_reason": cr.unencodable_reason,
                "result": "no-split",
                "wall_ms": 0,
                "ok_expect_no_split": not expect_split,
            }
        )
        return rows

    xr_cr = _compile(split["xr"], dialect=dialect, call_kind=call_kind, flags=flags)
    xd_note = None
    if split["empty_x"]:
        xd_cr = CompileResult(
            mirror=z3.Re(""),
            unencodable_reason=None,
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern="",
            declared_domain="ascii",
        )
    elif split["x_bare"].startswith("\\b"):
        # Correct \\b INNER $ (stock compile over-approx — see wb_leading_suffix_mirror).
        wb_m, wb_reason = wb_leading_suffix_mirror(
            split["x_bare"], dialect=dialect, flags=flags
        )
        if wb_m is None:
            xd_cr = CompileResult(
                mirror=None,
                unencodable_reason=wb_reason,
                dialect=dialect,
                call_kind=call_kind,
                flags=flags,
                pattern=split["x_dollar"],
                declared_domain="ascii",
            )
        else:
            xd_cr = CompileResult(
                mirror=wb_m,
                unencodable_reason=None,
                dialect=dialect,
                call_kind=call_kind,
                flags=flags,
                pattern=split["x_dollar"],
                declared_domain="ascii",
            )
            xd_note = "wb_leading_suffix_mirror"
    else:
        xd_cr = _compile(split["x_dollar"], dialect=dialect, call_kind=call_kind, flags=flags)

    if not xr_cr.encodable or (not split["empty_x"] and not xd_cr.encodable):
        rows.append(
            {
                **base,
                "encoding": "E1",
                "result": "split-unencodable",
                "wall_ms": 0,
                "xr_reason": xr_cr.unencodable_reason,
                "x_dollar_reason": xd_cr.unencodable_reason,
            }
        )
        return rows

    def e1_fn(s, xr_m=xr_cr.mirror, xd_m=xd_cr.mirror, empty=split["empty_x"], ck=call_kind):
        return build_e1(xr_m, xd_m, s, empty_x=empty, call_kind=ck)

    bucket = sample.get("bucket")
    # Full gitleaks paa shapes (large {n} / {0,50}) can ignore Solver timeout on
    # sat-find; measure membership+soundness only for CORPUS_BUCKETS.
    run_sat_find = bucket not in CORPUS_BUCKETS

    if "E1" in encodings:
        if run_sat_find:
            # Case-split sat-find: Or(xr, xd) can TIMEOUT in z3 even when each
            # branch alone decides quickly (seen on \\b reduced shapes).
            s_xr = String("s")
            xr_sat = solve_constraint(
                InRe(s_xr, xr_cr.mirror), s_xr, timeout_ms=timeout_ms
            )
            if split["empty_x"] and call_kind in ("search", "exec", "substitution"):
                xd_sat = {
                    "result": "sat",
                    "wall_ms": 0,
                    "witness": "",
                    "note": "empty-x-universal",
                }
            else:
                s_xd = String("s")
                xd_sat = solve_constraint(
                    InRe(s_xd, xd_cr.mirror), s_xd, timeout_ms=timeout_ms
                )
            if xr_sat["result"] == "sat" or xd_sat["result"] == "sat":
                combined = "sat"
                wit = xr_sat.get("witness") or xd_sat.get("witness")
            elif xr_sat["result"] == "unsat" and xd_sat["result"] == "unsat":
                combined = "unsat"
                wit = None
            else:
                combined = "unknown"
                wit = None
            sat_row = {
                "result": combined,
                "wall_ms": round(
                    (xr_sat.get("wall_ms") or 0) + (xd_sat.get("wall_ms") or 0), 2
                ),
                "witness": wit,
                "xr_sat_find": xr_sat,
                "xd_sat_find": xd_sat,
                "note": "case-split-sat-find",
            }
        else:
            sat_row = {
                "result": "skipped-corpus-sat-find",
                "wall_ms": 0,
                "witness": None,
            }
        sound = soundness_check(
            pattern,
            dialect=dialect,
            flags=flags,
            call_kind=call_kind,
            e1_fn=e1_fn,
            split=split,
            witness=sat_row.get("witness"),
        )
        rows.append(
            {
                **base,
                "encoding": "E1",
                "sat_find": sat_row,
                "result": sat_row["result"],
                "wall_ms": sat_row["wall_ms"],
                "witness": sat_row.get("witness"),
                "soundness": sound,
                "max_membership_ms": sound.get("max_membership_ms"),
                "x_dollar_encoding": xd_note or "compile_x$",
            }
        )

    if "E2" in encodings and run_sat_find:
        xr_fm = _compile(split["xr"], dialect=dialect, call_kind="fullmatch", flags=flags)
        if split["empty_x"]:
            x_body = z3.Re("")
            xb_ok = True
            xb_reason = None
        else:
            xb_cr = _compile(
                split["x_bare"], dialect=dialect, call_kind="fullmatch", flags=flags
            )
            x_body = xb_cr.mirror
            xb_ok = xb_cr.encodable
            xb_reason = xb_cr.unencodable_reason
        if not xr_fm.encodable or not xb_ok:
            rows.append(
                {
                    **base,
                    "encoding": "E2",
                    "result": "split-unencodable",
                    "wall_ms": 0,
                    "len_bound": E2_LEN_BOUND,
                    "xr_fm_reason": xr_fm.unencodable_reason,
                    "x_bare_reason": xb_reason,
                }
            )
        else:
            s = String("s")
            sat_row = solve_constraint(
                build_e2(
                    xr_fm.mirror,
                    x_body,
                    s,
                    len_bound=E2_LEN_BOUND,
                    empty_x=split["empty_x"],
                ),
                s,
                timeout_ms=timeout_ms,
            )
            rows.append(
                {
                    **base,
                    "encoding": "E2",
                    "sat_find": sat_row,
                    "result": sat_row["result"],
                    "wall_ms": sat_row["wall_ms"],
                    "witness": sat_row.get("witness"),
                    "len_bound": E2_LEN_BOUND,
                }
            )

    return rows


def call_kind_matrix(
    toy_pattern: str = "foo(?:bar|$)", *, timeout_ms: int
) -> list[dict]:
    out = []
    split = split_trailing_dollar(toy_pattern)
    assert split is not None
    for call_kind in ("search", "exec", "match", "fullmatch"):
        for dialect in ("re2", "py_re"):
            xr = _compile(split["xr"], dialect=dialect, call_kind=call_kind)
            xd = _compile(split["x_dollar"], dialect=dialect, call_kind=call_kind)
            if not xr.encodable or not xd.encodable:
                out.append(
                    {
                        "call_kind": call_kind,
                        "dialect": dialect,
                        "result": "split-unencodable",
                        "xr_reason": xr.unencodable_reason,
                        "x_dollar_reason": xd.unencodable_reason,
                    }
                )
                continue

            def e1_fn(s, xr_m=xr.mirror, xd_m=xd.mirror, ck=call_kind):
                return build_e1(xr_m, xd_m, s, empty_x=False, call_kind=ck)

            s = String("s")
            row = solve_constraint(e1_fn(s), s, timeout_ms=timeout_ms)
            wit = row.get("witness") or "foobar"
            mem = membership(e1_fn, wit)
            py_acc = py_re_accepts(toy_pattern, wit, flags="", call_kind=call_kind)
            out.append(
                {
                    "call_kind": call_kind,
                    "dialect": dialect,
                    "result": row["result"],
                    "wall_ms": row["wall_ms"],
                    "witness": row.get("witness"),
                    "mirror_on_witness": mem.get("accepts"),
                    "py_re_on_witness": py_acc,
                }
            )
    return out


def _e1_rows(results: list[dict], buckets: frozenset[str]) -> list[dict]:
    return [
        r
        for r in results
        if r.get("encoding") == "E1" and r.get("bucket") in buckets
    ]


def decide(results: list[dict]) -> tuple[str, str, str | None, str | None]:
    """Return (decision, note, encoding_chosen, domain)."""
    tract = _e1_rows(results, TRACTABILITY_BUCKETS)
    corpus = _e1_rows(results, CORPUS_BUCKETS)

    def membership_ok(r: dict) -> bool:
        sound = r.get("soundness") or {}
        if sound.get("mismatches"):
            return False
        if (sound.get("max_membership_ms") or 0) >= GO_WALL_MS:
            return False
        return r.get("result") != "split-unencodable"

    def sat_ok(r: dict) -> bool:
        return r.get("result") in ("sat", "unsat") and r.get("wall_ms", 99999) < GO_WALL_MS

    if not tract:
        return "NO-GO", "No tractability-cohort E1 rows.", None, None

    mem_clean = all(membership_ok(r) for r in tract + corpus)
    sat_tract = all(sat_ok(r) for r in tract)
    corpus_split_ok = all(
        r.get("result") != "split-unencodable" and membership_ok(r) for r in corpus
    )

    if mem_clean and sat_tract and corpus_split_ok:
        note = (
            "E1 Or(search(X·R), search(X$)) is sound (membership vs re2/py_re). "
            f"Case-split sat-find <{GO_WALL_MS}ms on the tractability cohort "
            "(toys, ids_rules, shape-reduced); monolithic Or(xr,xd) can TIMEOUT "
            "even when each branch is fine — P2 property queries should case-split. "
            f"Full gitleaks paa samples (n={len(corpus)}): split-encodable + "
            "instant membership; corpus sat-find skipped (large {{n}}/{{0,50}}). "
            "\\b…$ suffix uses wb_leading_suffix_mirror (stock WordBounded+$ "
            "over-approx). P2 lowers the pattern-final class for encodability "
            "recovery. call_kind: search/exec use E1; match/fullmatch wraps differ. "
            "Controls without pattern-final |$) stay rejected."
        )
        domain = (
            "case-split sat-find for Or branches; "
            "full kw/\\b corpus sat-find deferred"
        )
        return "GO", note, "E1", domain

    # E2 fallback on tractability cohort
    e2_tract = [
        r
        for r in results
        if r.get("encoding") == "E2" and r.get("bucket") in TRACTABILITY_BUCKETS
    ]
    if e2_tract and all(sat_ok(r) for r in e2_tract) and mem_clean:
        note = (
            f"E1 sat-find missed the <{GO_WALL_MS}ms gate on the tractability cohort; "
            f"E2 with len(s)<={E2_LEN_BOUND} meets it. Soundness membership clean."
        )
        return "GO-BOUNDED", note, "E2", f"len(s)<={E2_LEN_BOUND}"

    reasons = []
    if not mem_clean:
        reasons.append("soundness/membership failures")
    if not sat_tract:
        reasons.append("sat-find TIMEOUT/fail on tractability cohort")
    return (
        "NO-GO",
        "AC-P1 not met: " + "; ".join(reasons) + ". Reopen encoding on #81.",
        None,
        None,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=OUT_DEFAULT)
    ap.add_argument("--timeout-ms", type=int, default=TIMEOUT_MS)
    args = ap.parse_args()
    timeout_ms = args.timeout_ms

    t0 = time.perf_counter()
    paa = _load_gitleaks_paa()
    samples = TOYS + REDUCED + stratify_samples(paa) + IDS_SAMPLES

    results: list[dict] = []
    for i, sample in enumerate(samples, 1):
        print(
            f"[{i}/{len(samples)}] {sample['id'][:40]} ({sample.get('bucket')})",
            flush=True,
        )
        results.extend(
            run_sample(sample, encodings=["E1", "E2"], timeout_ms=timeout_ms)
        )

    ck = call_kind_matrix(timeout_ms=timeout_ms)
    decision, note, encoding_chosen, domain = decide(results)
    wall_s = round(time.perf_counter() - t0, 3)

    artifact = {
        "schema_version": "1",
        "wave": "trailing-alt-dollar",
        "decision": decision,
        "decision_note": note,
        "encoding_chosen": encoding_chosen,
        "domain": domain,
        "z3": z3.get_version_string(),
        "timeout_ms": timeout_ms,
        "go_wall_ms": GO_WALL_MS,
        "e2_len_bound": E2_LEN_BOUND,
        "issues": {
            "canonical": 81,
            "umbrella": 82,
            "spike": 86,
            "implement": 87,
            "validate": 83,
            "corpus": 84,
            "docs": 85,
        },
        "paa_gitleaks_count": len(paa),
        "sample_count": len(samples),
        "call_kind_matrix": ck,
        "results": results,
        "wall_s": wall_s,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"decision={decision} encoding={encoding_chosen} domain={domain}")
    print(f"wrote {args.out} ({len(results)} rows, {wall_s}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
