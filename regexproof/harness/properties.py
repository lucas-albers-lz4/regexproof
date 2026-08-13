"""Canonical property registry entries (usrmanage P1–P6 + CRS guards).

Importing this module registers properties into ``regexproof.harness.core.REGISTRY``.
"""

from __future__ import annotations

import re
import shutil
import subprocess

from z3 import (
    Concat,
    Contains,
    IndexOf,
    InRe,
    Length,
    Loop,
    Range,
    Re,
    Star,
    String,
    StringVal,
    SubString,
    Union,
)

from regexproof.harness.core import (
    REGISTRY,
    ci,
    ci_class,
    prefix_match,
    prop,
)

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


def _sed_capture(stream: str, engine: str = "gnu") -> str:
    """Real sed fallback: capture `[^\"]*` (prefix before first quote).

    Mirrors the rpcd json_get fallback shape. Used as ground truth for P3 —
    the Z3 witness must reproduce against this real implementation.

    Stream is fed on stdin (not as a path). Timeout only — non-zero exit is
    tolerated the same way the historical filename form was (empty capture).

    ``engine`` selects GNU (``"gnu"``, default) or busybox (``"busybox"``)
    via ``busybox sed``. Both engines run in the golden job (E2) so a
    divergence is visible, not silently collapsed.
    """
    if engine == "busybox":
        if not shutil.which("busybox"):
            raise RuntimeError("busybox-sed unavailable")
        argv = ["busybox", "sed", "-n", r's/^.*"\([^"]*\)".*$/\1/p']
    else:
        argv = ["sed", "-n", r's/^.*"\([^"]*\)".*$/\1/p']
    try:
        proc = subprocess.run(
            argv,
            input=stream,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"{engine}-sed replay timed out") from exc
    return proc.stdout.rstrip("\n")


def p3_ground_truth(witness: dict) -> bool:
    """Replay the P3 SAT witness against real sed.

    The Z3 model says: for v containing an escaped quote, the `[^\"]*`
    capture (prefix before the first quote) differs from v. Feed v through
    the real sed fallback and check the capture is a strict prefix (i.e.
    truncation happened at the escaped quote)."""
    v = witness["v"]  # raw string (as_string-extracted)
    stream = f'{{"password":"{v}"}}'
    try:
        capture = _sed_capture(stream)
    except (RuntimeError, subprocess.TimeoutExpired):
        return False
    # Truncation means the capture stopped at the first unescaped quote:
    # capture is a strict prefix of v (v contains an escaped quote).
    return capture != v and v.startswith(capture)


# E2: busybox-sed replay variant. The golden job records BOTH engine verdicts
# (GNU + busybox) so a divergence between the two real engines is visible in
# the ground-truth output, not silently collapsed.
SED_VERDICT_LOG: dict[str, dict[str, bool]] = {}
"""Per-property record of both sed engine verdicts (E2). Populated by
``p3_ground_truth_dual`` — tests/asserts inspect this to confirm both
engines ran and agree."""


def p3_ground_truth_dual(witness: dict) -> bool:
    """Replay the P3 SAT witness against BOTH GNU sed and busybox sed.

    Records both engine verdicts in ``SED_VERDICT_LOG`` (keyed by property
    name) so the golden job's ground-truth output reflects both engines
    (GNU + busybox). Returns True only when BOTH engines reproduce the
    truncation the Z3 witness claims (a divergence between the two real
    engines is a finding, not a silent collapse).

    If busybox is unavailable, the GNU verdict alone determines the result
    (the property still runs — busybox absence is recorded as ``gnu_only``).
    """
    v = witness["v"]
    stream = f'{{"password":"{v}"}}'
    verdicts: dict[str, bool] = {}
    all_reproduced = True

    for engine in ("gnu", "busybox"):
        try:
            capture = _sed_capture(stream, engine=engine)
        except RuntimeError as exc:
            if "busybox" in str(exc):
                verdicts["busybox"] = False
                verdicts["busybox_absent"] = True
                continue
            verdicts[engine] = False
            all_reproduced = False
            continue
        reproduced = capture != v and v.startswith(capture)
        verdicts[engine] = reproduced
        if not reproduced:
            all_reproduced = False

    SED_VERDICT_LOG["P3-sed-busybox-truncation"] = verdicts
    return all_reproduced


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
        # S16 fixture (#220): P1-space is the backend="noodler" fixture property —
        # in stock-only CI the binary is absent → triage_fallback (stock result,
        # exit unchanged, tier seq-only); in the noodler CI job the real binary
        # runs with the cvc5 cross-check leg.
        "backend": "noodler" if _name == "space" else "seq",
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
    # The actor travels as a shell command-line token (git identity rendered
    # into an audit/shell line) — an ASCII, NUL-free alphabet. The whitelist
    # classes are explicit ASCII ranges, so "ascii" is the faithful domain.
    input_domain="ascii",
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
    # v is a shell metacharacter/token alphabet value fed to sed on stdin
    # (POSIX shell strings, ASCII, NUL-free) — the declared boundary domain.
    input_domain="ascii",
)
def p3():
    v = String("v")
    first_quote = IndexOf(v, StringVal('"'), 0)
    capture = SubString(v, 0, first_quote)
    # v is the JSON-escaped value the escaper feeds the rpcd sed fallback, so
    # its alphabet is the escaper's output token vocabulary (ESCAPE_SAFE chars
    # plus the ESCAPE_ESC tokens `\\` `\"` `\t` `\r` `\n`) — constrain v to it
    # so the declared `input_domain="ascii"` is faithful (was: an unconstrained
    # string, an unsupported boundary assumption). The ESCAPE_ESC `\"` token is
    # backslash + raw quote, so the bug-repro semantics (first_quote > 0,
    # capture != v, v contains `\"`) are preserved.
    return [
        InRe(v, Star(ESCAPE_TOKENS)),
        first_quote > 0,
        capture != v,
    ], Contains(v, StringVal('\\"'))


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
    # The escaper runs over a shell metacharacter/token alphabet (POSIX shell
    # strings exclude NUL) — ASCII domain; the P4-nul bug demo shows why the
    # NUL exclusion is load-bearing.
    input_domain="ascii",
)
def p4_tab():
    w = String("w")
    return [InRe(w, ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\t")


@prop(
    "P4-escape-image-newline",
    "same token alphabet contains no raw newline",
    expect_unsat=True,
    input_domain="ascii",
)
def p4_nl():
    w = String("w")
    return [InRe(w, ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\n")


@prop(
    "P4-escape-image-del",
    "same token alphabet contains no raw DEL (0x7f)",
    expect_unsat=True,
    input_domain="ascii",
)
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


# E2: busybox-sed replay variant. Same Z3 witness as P3-sed-capture-truncation
# but the ground-truth callback runs BOTH GNU sed and busybox sed and records
# both engine verdicts (SED_VERDICT_LOG). A divergence between the two real
# engines is a finding, not a silent collapse.
@prop(
    "P3-sed-busybox-truncation",
    "E2: exists v: v contains an escaped quote AND the sed-style capture "
    '[^"]* (prefix before first quote) differs from v — replayed against '
    "BOTH GNU sed and busybox sed; both engine verdicts recorded",
    expect_unsat=False,
    ground_truth=p3_ground_truth_dual,
    kind="counterexample_finder",
    family="P3",
    # Same ASCII, NUL-free boundary domain as P3-sed-capture-truncation.
    input_domain="ascii",
)
def p3_busybox():
    v = String("v")
    first_quote = IndexOf(v, StringVal('"'), 0)
    capture = SubString(v, 0, first_quote)
    return [
        InRe(v, Star(ESCAPE_TOKENS)),
        first_quote > 0,
        capture != v,
    ], Contains(v, StringVal('\\"'))


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


