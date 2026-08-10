#!/usr/bin/env python3
"""regexproof harness skeleton — property registry + mutation guards.

Contract (from docs/PLAYBOOK.md and docs/DECOMPOSITION.md):
  - TIMEOUT (solver `unknown`) is a HARD FAILURE — never a pass, never a
    counterexample.
  - Every property declares its DOMAIN: exactly what was proven. A length
    bound means "proven up to this length", not "inputs are this length".
  - Mutation guards (expect_sat=True) weaken the regex and assert the result
    flips UNSAT->SAT. A harness that can't fail proves nothing.
  - Per-property wall time is logged so slice bounds can be tuned empirically.
  - SAT witnesses MUST be ground-truthed against the real implementation
    before being reported (see properties/usrmanage-p1-p6.md for the sed
    ground-truth protocol).

Usage:
  python3 z3-verify.py --list
  python3 z3-verify.py --all
  python3 z3-verify.py P1 P2 P1-mutated
  python3 z3-verify.py --all --require-ground-truth
  python3 z3-verify.py --all --json          # NDJSON (one object per line)
  python3 z3-verify.py --all --json-legacy   # one-release JSON array mode
  python3 z3-verify.py --check-mutation-coverage

Exit code: 0 = all pass; 1 = any FAIL/TIMEOUT/coverage gap;
2 = unknown property names / flag conflict on the CLI; 3 = wrong z3-solver version.

--require-ground-truth: any SAT (counterexample) result MUST have replayed
its witness against the real implementation via the property's ground_truth
callback. A SAT result without a callback (or a witness that fails to
reproduce) is a hard failure — an unverified counterexample is never
reported as a vulnerability.

--json: emit one NDJSON object per property (schema_version, result, witness,
ground-truth, domain, wall_ms, engine_versions, not_proven). Same facts as
the human output — the two reports can never disagree. Partial streams remain
valid if a later property fails. Mutually exclusive with --json-legacy.

--json-legacy: emit a single JSON array of the same records (one-release
compat). Mutually exclusive with --json.
"""

import contextlib
import io
import json
import platform
import re
import subprocess
import sys
import time
from pathlib import Path

# Checkout bootstrap (match scripts/batch-scan.py) — fix-wave #71.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import z3
from z3 import (
    AllChar,
    Concat,
    Contains,
    IndexOf,
    InRe,
    Length,
    Loop,
    Range,
    Re,
    Solver,
    Star,
    String,
    StringVal,
    SubString,
    Union,
    sat,
    unknown,
    unsat,
)

from regexproof.kinds import (
    KINDS_NEEDING_MUTATION_GUARD,
    validate_call_kind,
    validate_kind,
)

# ---------------------------------------------------------------------------
# Solver version pin — the Re()/regex API changed across 4.x/5.x. Refuse to
# run on an unpinned version instead of silently producing unknown/timeouts.
# ---------------------------------------------------------------------------
Z3_VERSION = z3.get_version_string()
if not Z3_VERSION.startswith("5.0"):
    print(
        f"FATAL: z3-solver {Z3_VERSION} — this harness is validated against "
        "5.0.x only. Install the pinned version: pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(3)


def z3_str(val) -> str:
    """Extract a raw Python string from a z3 model value.

    z3's as_string() escapes control chars (NUL -> literal '\\u{0}'), which
    would break ground-truth replay of binary witnesses. Decode the escapes
    back to raw bytes."""
    s = val.as_string()
    return re.sub(r"\\u\{([0-9a-fA-F]+)\}", lambda m: chr(int(m.group(1), 16)), s)


# ---------------------------------------------------------------------------
# Property registry
# ---------------------------------------------------------------------------
REGISTRY = {}
SCHEMA_VERSION = "1"


def engine_versions() -> dict:
    """Recorded engines for machine-readable / ground-truth reports."""
    return {
        "python": platform.python_version(),
        "z3": Z3_VERSION,
    }


# ---------------------------------------------------------------------------
# Mirror-construction helpers (dogfooding P0 — verified 2026-08-07)
# ---------------------------------------------------------------------------
def ci(word: str):
    """Case-expanded mirror of a literal word: Union(Re(c.lower()),
    Re(c.upper())) per char. REQUIRED when mirroring a pattern compiled
    with re.I / (?i) — z3's Re("AND") is case-sensitive and silently
    accepts a strict subset of the real (?i)AND language (verified:
    naive mirror rejects 'And'/'aND' while the real regex accepts)."""
    return Concat(*[Union(Re(c.lower()), Re(c.upper())) for c in word])


def ci_class(lo: str, hi: str):
    """Case-expanded char range: every char in [lo..hi] plus its
    uppercase/lowercase counterpart. For r"[a-z]" under re.I."""
    return Union(*[Union(Re(chr(c)), Re(chr(c).upper())) for c in range(ord(lo), ord(hi) + 1)])


def prefix_match(regex):
    """Mirror of re.match(regex, s) / re.sub(regex, ...) with an implicit
    ^ — Z3 InRe is WHOLE-STRING membership, so a prefix matcher must be
    modeled as Concat(regex, <anything>), not as the bare regex.
    Verified divergence: InRe("AND foo", Re("AND")) is unsat while
    re.match(r"AND", "AND foo") matches (hermes-agent gap1 demo 2).
    The suffix is Star(AllChar) — any tail is accepted."""
    any_char = AllChar(Re("").sort())
    return Concat(regex, Star(any_char))


def prop(
    name,
    declared_domain,
    expect_unsat=True,
    timeout_ms=30000,
    ground_truth=None,
    kind="property",
    family=None,
    input_domain=None,
    call_kind=None,
):
    """Decorator: register a property. The wrapped function returns the
    constraint list; the harness adds `bad` and checks satisfiability.

    `kind` distinguishes WHY expect_unsat is False (or why SAT matters):
      - "property": a security invariant that must hold (expect_unsat=True).
      - "counterexample_finder": SAT is the finding (a real bug witness).
      - "mutation_guard": SAT proves the harness is sensitive (weakened
        regex must flip UNSAT->SAT). Its witness is never replayed/reported.
      - "bug_demo": SAT demonstrates a known bug by design (P4-nul).
      - "rule_diff": shape-5 gap query (R2 accepts something R1 misses).
    `family` groups properties that share a mutation guard (e.g. "P1").
    `call_kind`: optional engine usage taxonomy (fullmatch/match/search/exec/
    substitution) — required for auto-generated scanner properties.
    `ground_truth`: optional callable `fn(witness: dict) -> bool` that runs
    the REAL implementation on a SAT witness and reports whether the model's
    behavior reproduces. Required when --require-ground-truth is set and the
    property is satisfiable — UNLESS kind is "mutation_guard" (sensitivity
    probe, not a reportable counterexample).
    `input_domain`: the boundary's alphabet assumption — "ascii" (mirror
    classes like [a-z0-9_] are faithful because the real input is
    ASCII-constrained) or "unicode" (Python \\w\\d\\s\\b are Unicode-aware;
    an ASCII mirror silently diverges). None = unstated (legacy default,
    backward compatible: properties written before this field pass as
    before). --require-domain makes an unstated domain a hard failure.
    """
    assert callable(ground_truth) or ground_truth is None, "ground_truth must be callable"
    if input_domain is not None:
        assert input_domain in ("ascii", "unicode"), (
            f"{name}: input_domain must be 'ascii' | 'unicode' | None, got {input_domain!r}"
        )
    kind = validate_kind(kind)
    call_kind = validate_call_kind(call_kind)

    def deco(fn):
        REGISTRY[name] = {
            "fn": fn,
            "domain": declared_domain,
            "expect_unsat": expect_unsat,
            "timeout_ms": timeout_ms,
            "ground_truth": ground_truth,
            "kind": kind,
            "family": family or name.split("-")[0],
            "input_domain": input_domain,
            "call_kind": call_kind,
        }
        return fn

    return deco


def run_one(name, entry, require_ground_truth=False):
    """Run one property; print human output; return a result dict.

    The dict is also what --json / --json-legacy serializes, so the JSON
    report and the human report always agree on the facts.
    """
    engines = engine_versions()
    result = {
        "schema_version": SCHEMA_VERSION,
        "name": name,
        "kind": entry["kind"],
        "family": entry["family"],
        "call_kind": entry.get("call_kind"),
        "domain": entry["domain"],
        "input_domain": entry["input_domain"],
        "expect_unsat": entry["expect_unsat"],
        "result": None,  # "unsat" | "sat" | "timeout"
        "ok": False,
        "witness": None,
        "ground_truth": None,  # None | "reproduced" | "failed" | "refused-no-callback"
        "wall_ms": None,
        "engine_versions": engines,
        "not_proven": False,  # True iff TIMEOUT — surfaced as "not proven"
    }
    s = Solver()
    s.set("timeout", entry["timeout_ms"])
    constraints, bad = entry["fn"]()
    for c in constraints:
        s.add(c)
    s.add(bad)
    t0 = time.perf_counter()
    r = s.check()
    result["wall_ms"] = round((time.perf_counter() - t0) * 1000, 1)
    if r == unknown:
        result["result"] = "timeout"
        result["not_proven"] = True
        result["ok"] = False
        print(
            f"[TIMEOUT] {name}: unknown ({entry['timeout_ms']}ms) — "
            "HARD FAILURE (not proven)"
        )
        return result
    result["result"] = "unsat" if r == unsat else "sat"
    result["ok"] = (r == unsat) == entry["expect_unsat"]
    tag = "UNSAT (property HOLDS)" if r == unsat else "SAT (counterexample)"
    print(f"[{'PASS' if result['ok'] else 'FAIL'}] {name}: {tag}  [{result['wall_ms']:.1f}ms]")
    print(f"    domain: {entry['domain']}")
    if r == sat:
        m = s.model()
        witness = {}
        for d in m.decls():
            val = m[d]
            # Extract raw string values so ground_truth callbacks see the
            # actual bytes, not z3's repr (e.g. "\u{0}" for NUL).
            try:
                if val.sort() == StringVal("").sort():
                    val = z3_str(val)
            except Exception:
                pass
            witness[d.name()] = val
            print(f"    witness: {d.name()} = {val!r}")
        result["witness"] = witness
        # Note: engine_versions is always populated above; the meaningful
        # --require-ground-truth gate is the callback check below (fix-wave #71).
        gt = entry.get("ground_truth")
        if entry["kind"] == "mutation_guard":
            result["ground_truth"] = "mutation-guard-sat-expected"
            print("    mutation guard: SAT expected (harness-sensitivity probe, not a finding)")
        elif gt is not None:
            reproduced = bool(gt(witness))
            result["ground_truth"] = "reproduced" if reproduced else "failed"
            print(f"    ground-truth: {'REPRODUCED' if reproduced else 'FAILED TO REPRODUCE'}")
            if not reproduced:
                print(
                    "    WARNING: SAT witness did not reproduce against the real "
                    "implementation — do NOT report this as a vulnerability.",
                    file=sys.stderr,
                )
                result["ok"] = False
        elif require_ground_truth:
            result["ground_truth"] = "refused-no-callback"
            print(
                "    ERROR: SAT witness has no ground_truth callback, but "
                "--require-ground-truth is set — refusing to report an "
                "unverified counterexample.",
                file=sys.stderr,
            )
            result["ok"] = False
    return result

# ---------------------------------------------------------------------------
# Properties (mirrors properties/usrmanage-p1-p6.md)
# ---------------------------------------------------------------------------
USERNAME_CLS = Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_"), Re("-"))
USERNAME_RE = Concat(Union(Range("a", "z"), Re("_")), Star(USERNAME_CLS))
DENY_LIST = ["root", "daemon", "ftp", "network", "nobody", "nogroup", "admin", "ubus", "sync"]
INJECTION_CHARS = [
    ("space", " "),
    ("equals", "="),
    ("newline", "\n"),
    ("tab", "\t"),
    ("semicolon", ";"),
    ("pipe", "|"),
    ("dollar", "$"),
    ("backtick", "`"),
    ("ampersand", "&"),
]


def _sed_capture(stream: str) -> str:
    """Real sed fallback: capture `[^\"]*` (prefix before first quote).

    Mirrors the rpcd json_get fallback shape. Used as ground truth for P3 —
    the Z3 witness must reproduce against this real implementation.

    Stream is fed on stdin (not as a path). Timeout only — non-zero exit is
    tolerated the same way the historical filename form was (empty capture).
    """
    try:
        proc = subprocess.run(
            ["sed", "-n", r's/^.*"\([^"]*\)".*$/\1/p'],
            input=stream,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("sed replay timed out") from exc
    return proc.stdout.rstrip("\n")


def p3_ground_truth(witness: dict) -> bool:
    """Replay the P3 SAT witness against real sed.

    The Z3 model says: for v containing an escaped quote, the `[^\"]*`
    capture (prefix before the first quote) differs from v. Feed v through
    the real sed fallback and check the capture is a strict prefix (i.e.
    truncation happened at the escaped quote)."""
    v = witness["v"]  # raw string (as_string-extracted)
    # Build a stream shaped like the rpcd JSON the sed fallback sees.
    stream = f'{{"password":"{v}"}}'
    try:
        capture = _sed_capture(stream)
    except (RuntimeError, subprocess.TimeoutExpired):
        return False
    # Truncation means the capture stopped at the first unescaped quote:
    # capture is a strict prefix of v (v contains an escaped quote).
    return capture != v and v.startswith(capture)


def _p1(ch):
    """P1 builder: username validator + deny-list, 'contains <ch>' as bad."""
    u = String("u")
    constraints = [InRe(u, USERNAME_RE), Length(u) >= 1, Length(u) <= 32]
    constraints += [u != StringVal(d) for d in DENY_LIST]
    return constraints, Contains(u, StringVal(ch))


for _name, _ch in INJECTION_CHARS:
    REGISTRY[f"P1-{_name}"] = {
        "fn": lambda ch=_ch: _p1(ch),
        "expect_unsat": True,
        "timeout_ms": 30000,
        "domain": "usernames matching "
        "^[a-z_][a-z0-9_-]{0,31}$ minus deny-list "
        "(declared domain: len 1..32) contain no "
        f"{_name}",
        "kind": "property",
        "family": "P1",
        "input_domain": "ascii",
        "ground_truth": None,
    }

ACTOR_CLS = Union(
    Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("."), Re("_"), Re("@"), Re("-")
)


@prop(
    "P2-actor-whitelist",
    "actor whitelist [A-Za-z0-9._@-]{1,64} admits no audit-line-breaking "
    "char (proven for len <= 16; slice 17-64 for full coverage)",
    expect_unsat=True,
    family="P2",
)
def p2():
    a = String("a")
    wl_re = Concat(ACTOR_CLS, Star(ACTOR_CLS))
    constraints = [InRe(a, wl_re), Length(a) >= 1, Length(a) <= 16]
    return constraints, Contains(a, StringVal(" "))


@prop(
    "P3-sed-capture-truncation",
    "exists v: v contains an escaped quote AND the sed-style capture "
    '[^"]* (prefix before first quote) differs from v — the rpcd sed '
    "fallback bug repro",
    expect_unsat=False,
    ground_truth=p3_ground_truth,
    kind="counterexample_finder",
    family="P3",
)
def p3():
    v = String("v")
    first_quote = IndexOf(v, StringVal('"'), 0)
    capture = SubString(v, 0, first_quote)
    return [first_quote > 0, capture != v], Contains(v, StringVal('\\"'))


ESCAPE_SAFE = Union(Range("\x20", "\x21"), Range("\x23", "\x5b"), Range("\x5d", "\x7e"))
ESCAPE_ESC = Union(Re("\\\\"), Re('\\"'), Re("\\t"), Re("\\r"), Re("\\n"))
ESCAPE_TOKENS = Union(ESCAPE_SAFE, ESCAPE_ESC)


@prop(
    "P4-escape-image-tab",
    "um_json_escape output token alphabet (safe chars + escape tokens, "
    "input alphabet excludes NUL per POSIX shell domain assumption) "
    "contains no raw tab. NOTE: encoded as single-char membership — "
    "Contains-vs-Star-image TIMES OUT even per-token (measured 30s); "
    "alphabet disjointness is the equivalent instant form (0.4ms).",
    expect_unsat=True,
)
def p4_tab():
    w = String("w")
    return [InRe(w, ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\t")


@prop("P4-escape-image-newline", "same token alphabet contains no raw newline", expect_unsat=True)
def p4_nl():
    w = String("w")
    return [InRe(w, ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\n")


@prop("P4-escape-image-del", "same token alphabet contains no raw DEL (0x7f)", expect_unsat=True)
def p4_del():
    w = String("w")
    return [InRe(w, ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\x7f")


def _escape_mirror(byte: str) -> str:
    """Mirror of the real escaper: o == 0 falls through the `o > 0 && o < 32`
    guard and is printed raw (NUL passthrough). Anything else is escaped or
    safe-printed. Used as ground truth for P4-nul."""
    o = ord(byte)
    if o == 0:
        return byte  # raw NUL — the bug
    if 0 < o < 32:
        return f"\\x{o:02x}"
    return byte


@prop(
    "P4-nul-passthrough-demo",
    "BUG DEMO: a faithful token alphabet that includes the escaper's "
    "raw-NUL else-branch DOES contain NUL — this is why the POSIX "
    "input-domain assumption must be stated explicitly in the real property",
    expect_unsat=False,
    ground_truth=lambda w: _escape_mirror(w["w"][0] if w["w"] else "\x00") == "\x00",
    kind="bug_demo",
    family="P4",
)
def p4_nul():
    w = String("w")
    # o == 0 falls through the `o > 0 && o < 32` guard -> printed raw
    faithful = Union(ESCAPE_TOKENS, Re("\x00"))
    return [InRe(w, faithful), Length(w) == 1], w == StringVal("\x00")


# ---------------------------------------------------------------------------
# Mutation guards — the harness must be able to fail
# ---------------------------------------------------------------------------
WEAKENED_USERNAME_RE = Concat(Union(Range("a", "z"), Re("_")), Star(Union(USERNAME_CLS, Re("*"))))


@prop(
    "P1-mutated-star",
    "MUTATION GUARD: if the username regex is weakened to allow '*', the "
    "'no star' property MUST flip UNSAT->SAT. If this passes as UNSAT, the "
    "mirror is not tracking the real regex.",
    expect_unsat=False,
    kind="mutation_guard",
    family="P1",
)
def p1_mutated():
    u = String("u")
    constraints = [InRe(u, WEAKENED_USERNAME_RE), Length(u) >= 1, Length(u) <= 32]
    return constraints, Contains(u, StringVal("*"))


# P2 guard: weaken the actor whitelist to admit a space. The P2 property
# ("no space in whitelisted actors") MUST flip UNSAT->SAT.
WEAKENED_ACTOR_CLS = Union(ACTOR_CLS, Re(" "))


@prop(
    "P2-mutated-space",
    "MUTATION GUARD: if the actor whitelist is weakened to admit ' ', the "
    "'no space' property MUST flip UNSAT->SAT. If this passes as UNSAT, the "
    "mirror is not tracking the real whitelist.",
    expect_unsat=False,
    kind="mutation_guard",
    family="P2",
)
def p2_mutated():
    a = String("a")
    wl_re = Concat(WEAKENED_ACTOR_CLS, Star(WEAKENED_ACTOR_CLS))
    constraints = [InRe(a, wl_re), Length(a) >= 1, Length(a) <= 16]
    return constraints, Contains(a, StringVal(" "))


# P3 guard: make the capture CORRECT (whole value, no truncation). The
# counterexample (capture != v) MUST disappear -> flip SAT->UNSAT. This
# proves the P3 mirror is sensitive to the truncation it models.
@prop(
    "P3-mutated-correct-capture",
    "MUTATION GUARD: if the sed capture were CORRECT (captures the whole "
    "value, no truncation at the first quote), no counterexample exists — "
    "the property MUST flip SAT->UNSAT. If this stays SAT, the mirror is "
    "not tracking the truncation.",
    expect_unsat=True,
    kind="mutation_guard",
    family="P3",
)
def p3_mutated():
    v = String("v")
    first_quote = IndexOf(v, StringVal('"'), 0)
    correct_capture = SubString(v, 0, Length(v))  # whole value, no truncation
    return [first_quote > 0, correct_capture != v], Contains(v, StringVal('\\"'))


# P4 guard: weaken the escape alphabet to admit a raw tab. The P4 property
# ("no raw tab in escape output") MUST flip UNSAT->SAT.
WEAKENED_ESCAPE_TOKENS = Union(ESCAPE_TOKENS, Re("\t"))


@prop(
    "P4-mutated-tab",
    "MUTATION GUARD: if the escape token alphabet is weakened to admit a "
    "raw tab, the 'no raw tab' property MUST flip UNSAT->SAT. If this "
    "passes as UNSAT, the mirror is not tracking the real escaper.",
    expect_unsat=False,
    kind="mutation_guard",
    family="P4",
)
def p4_mutated():
    w = String("w")
    return [InRe(w, WEAKENED_ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\t")


# ---------------------------------------------------------------------------
# P5 — case-insensitive boundary (dogfooding P0-1/P1-1, hermes-agent gap 1)
# ---------------------------------------------------------------------------
# Real boundary (hermes-agent telegram adapter): a @handle is validated with
#   re.fullmatch(r"[a-z0-9_]{2,29}bot", handle, re.IGNORECASE)
# The whitelist is ASCII + IGNORECASE. Properties:
#   P5-handle-safe: no control/separator char can be in the accepted handle.
#   P5-mutated-lowercase: weaken the mirror to lowercase-only -> the
#     "accepts MyBot" claim flips UNSAT->SAT (case-flag sensitivity).
# Full handle language: [A-Za-z0-9_]{2,29}bot with both cases.
HANDLE_CHAR = Union(ci_class("a", "z"), Range("0", "9"), Re("_"))
HANDLE_LANG = Concat(
    Loop(HANDLE_CHAR, 2, 29),
    ci("bot"),  # case-expanded "bot" — the IGNORECASE part
)


@prop(
    "P5-handle-safe",
    "telegram bot-handle whitelist [a-z0-9_]{2,29}bot (re.IGNORECASE) admits "
    "no control/separator char — case-expanded mirror via ci()/ci_class()",
    expect_unsat=True,
    input_domain="ascii",
    family="P5",
)
def p5_handle_safe():
    h = String("h")
    bad = Union(Range("\x00", "\x1f"), Re("\x7f"), Re(" "), Re(";"), Re("="))
    # Any single char of the handle language that is ALSO bad:
    return [InRe(h, HANDLE_CHAR), Length(h) == 1], InRe(h, bad)


@prop(
    "P5-mutated-lowercase",
    "MUTATION GUARD (case flags): the case-expanded mirror MUST accept "
    "'MyBot' (SAT) — the real IGNORECASE regex does. A lowercase-only "
    "mirror gives UNSAT here (verified: Re('bot') rejects 'MyBot'), which "
    "is exactly the silently-narrower-language trap (hermes-agent gap 1).",
    expect_unsat=False,
    kind="mutation_guard",
    family="P5",
)
def p5_mutated_lowercase():
    # Correct mirror: case-expanded everywhere. Must accept "MyBot".
    h = String("h")
    return [InRe(h, HANDLE_LANG)], h == StringVal("MyBot")


# ---------------------------------------------------------------------------
# CRS cross-engine rule_diff mutation guard (Wave-2 P5 / issue #100)
# ---------------------------------------------------------------------------
# Shape-5 sensitivity probe for the Coraza(go-re2)↔ModSecurity(pcre) family.
# Uses a tiny shared alphabet pattern so --all stays hermetic (no CRS clone).
@prop(
    "crs-cross-engine-widen-R1",
    "MUTATION GUARD (cross-engine family): narrowing R1 to a singleton "
    "impossible prefix must flip the gap query to SAT (harness sensitivity).",
    expect_unsat=False,
    kind="mutation_guard",
    family="crs-cross-engine",
    input_domain="ascii",
    call_kind="search",
)
def crs_cross_engine_widen_r1():
    from regexproof.rule_diff.encode import shape5_constraints

    r2 = Concat(Re("a"), Star(Union(Range("a", "z"), Range("0", "9"))))
    narrow_r1 = Concat(Re("\x01"), Star(Re("\x01")))
    constraints, bad, _s = shape5_constraints(narrow_r1, r2, min_len=1, max_len=16)
    return constraints, bad


@prop(
    "crs-cross-engine-control",
    "MUTATION GUARD (cross-engine family): identical R1/R2 mirrors must be "
    "UNSAT (no self-gap).",
    expect_unsat=True,
    kind="mutation_guard",
    family="crs-cross-engine",
    input_domain="ascii",
    call_kind="search",
)
def crs_cross_engine_control():
    from regexproof.rule_diff.encode import shape5_constraints

    r = Concat(Re("a"), Star(Union(Range("a", "z"), Range("0", "9"))))
    constraints, bad, _s = shape5_constraints(r, r, min_len=1, max_len=16)
    return constraints, bad


# ---------------------------------------------------------------------------
# P6 — prefix-match modeling (dogfooding finding, issue #11)
# ---------------------------------------------------------------------------
# re.match(r"^AND", "AND foo") MATCHES, but InRe("AND foo", Re("AND")) is
# unsat (whole-string membership). The prefix_match() helper models the
# anchor; this property proves the divergence is real and the helper fixes it.
@prop(
    "P6-prefix-match-demo",
    "DEMO: re.match/^ is a prefix match, InRe is whole-string — the bare "
    "mirror MUST FAIL here (UNSAT proves the trap): 'AND foo' is not in "
    "the exact-string language Re('AND'), but re.match(r'AND', 'AND foo') "
    "matches. The helper P6-prefix-match-helper shows the correct form.",
    expect_unsat=True,
    kind="bug_demo",
    family="P6",
)
def p6_prefix_match_demo():
    s = String("s")
    # bare mirror (wrong): "AND foo" is NOT in the Re("AND") language
    return [InRe(s, Re("AND"))], s == StringVal("AND foo")


@prop(
    "P6-prefix-match-helper",
    "prefix_match(Re('AND')) models re.match(r'AND', s) — 'AND foo' IS in "
    "the prefix language (correct mirror, SAT)",
    expect_unsat=False,
    kind="bug_demo",
    family="P6",
    ground_truth=lambda w: bool(re.match(r"AND", w["s"])),
)
def p6_prefix_match_helper():
    s = String("s")
    return [InRe(s, prefix_match(Re("AND")))], s == StringVal("AND foo")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def check_mutation_coverage():
    """Structural invariant: every family with a security property,
    counterexample finder, or rule_diff must also have at least one
    mutation guard.

    A property with no mutation guard can go vacuous (e.g. via the
    Complement() trap) without any test noticing. Warn loudly so the gap
    is visible; the warning is the guard's guard."""
    guarded = {e["family"] for e in REGISTRY.values() if e["kind"] == "mutation_guard"}
    needing = {
        e["family"]
        for e in REGISTRY.values()
        if e["kind"] in KINDS_NEEDING_MUTATION_GUARD
    }
    missing = sorted(needing - guarded)
    if missing:
        print(
            "WARNING: families with properties but NO mutation guard: "
            f"{', '.join(missing)} — a vacuous encoding would pass silently.",
            file=sys.stderr,
        )
        return 1
    return 0


def check_domain_coverage(require=False):
    """input_domain discipline (dogfooding gap-2 finding, issue #11).

    With --require-domain, every security property / counterexample finder
    must declare input_domain ("ascii" | "unicode"). Without it, an ASCII
    mirror of a Unicode-exposed boundary passes silently — the exact false-
    safety class the hermes-agent gap-2 finding demonstrated (an ASCII \\b
    mirror 'proves' redaction while real Python leaks CJK-adjacent tokens).
    Backward compatible: legacy properties with no declaration only fail
    when the flag is passed, matching how --require-ground-truth works.
    """
    if not require:
        return 0
    missing = sorted(
        e["family"] + ":" + n
        for n, e in REGISTRY.items()
        if e["kind"] in ("property", "counterexample_finder") and e["input_domain"] is None
    )
    if missing:
        print(
            "FAIL: --require-domain, but these properties declare no "
            f"input_domain ('ascii' | 'unicode'): {', '.join(missing)}. "
            "An unstated alphabet assumption can silently diverge from "
            "Unicode-aware \\w\\d\\s\\b in the real regex.",
            file=sys.stderr,
        )
        return 1
    return 0


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    require_ground_truth = "--require-ground-truth" in args
    require_domain = "--require-domain" in args
    as_json = "--json" in args
    as_json_legacy = "--json-legacy" in args
    check_cov_only = "--check-mutation-coverage" in args
    if as_json and as_json_legacy:
        print(
            "error: --json and --json-legacy are mutually exclusive",
            file=sys.stderr,
        )
        return 2
    args = [
        a
        for a in args
        if a
        not in (
            "--require-ground-truth",
            "--require-domain",
            "--json",
            "--json-legacy",
            "--check-mutation-coverage",
        )
    ]
    if check_cov_only:
        return check_mutation_coverage()
    if not args or "--all" in args:
        named = [a for a in args if a != "--all"]
        if named:
            print(
                f"WARNING: --all ignores explicitly named properties: {named}",
                file=sys.stderr,
            )
        names = sorted(REGISTRY)
    elif "--list" in args:
        for n in sorted(REGISTRY):
            e = REGISTRY[n]
            print(
                f"{n}  expect_unsat={e['expect_unsat']}  "
                f"timeout={e['timeout_ms']}ms  "
                f"kind={e['kind']}  family={e['family']}  "
                f"call_kind={e.get('call_kind')}  "
                f"input_domain={e['input_domain']}  "
                f"ground_truth={'yes' if e.get('ground_truth') else 'no'}"
            )
            print(f"    domain: {e['domain']}")
        return 0
    else:
        names = [a for a in args if a in REGISTRY]
        missing = [a for a in args if a not in REGISTRY]
        if missing:
            print(f"unknown properties: {missing}", file=sys.stderr)
            return 2

    coverage_fail = check_mutation_coverage()
    domain_fail = check_domain_coverage(require=require_domain)
    failures = 0
    results = []
    if as_json or as_json_legacy:
        sink = io.StringIO()
        with contextlib.redirect_stdout(sink):
            for n in names:
                res = run_one(n, REGISTRY[n], require_ground_truth)
                results.append(res)
                if not res["ok"]:
                    failures += 1
                if as_json:
                    # Flush each record immediately so partial streams stay valid.
                    print(json.dumps(res, sort_keys=True), file=sys.__stdout__)
    else:
        for n in names:
            res = run_one(n, REGISTRY[n], require_ground_truth)
            results.append(res)
            if not res["ok"]:
                failures += 1
    failures += domain_fail
    if as_json_legacy:
        print(json.dumps(results, indent=2, sort_keys=True))
    elif not as_json:
        print(f"\n{len(names) - failures}/{len(names)} passed")
    return 1 if (failures or coverage_fail) else 0


if __name__ == "__main__":
    sys.exit(main())
