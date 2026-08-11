"""Z3 harness core: registry, prop, run_one, coverage checks.

Moved from scripts/z3-verify.py (#192). CLI remains at scripts/z3-verify.py.
"""

from __future__ import annotations

import platform
import re
import sys
import time

import z3
from z3 import (
    AllChar,
    Concat,
    Re,
    Solver,
    Star,
    StringVal,
    Union,
    sat,
    unknown,
    unsat,
)

from regexproof.kinds import (
    KINDS_NEEDING_MUTATION_GUARD,
    PropertyKind,
    SolveResult,
    validate_call_kind,
    validate_kind,
)

# ---------------------------------------------------------------------------
# Solver version pin — the Re()/regex API changed across 4.x/5.x. Refuse to
# run on an unpinned version instead of silently producing unknown/timeouts.
# ---------------------------------------------------------------------------
from regexproof.z3_pin import assert_z3_pinned

Z3_VERSION = assert_z3_pinned()


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
    backend="seq",
    decomposition_trace=None,
    search_wrapped=False,
    pattern=None,
    pattern_flags="",
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
    `backend`: "seq" (default, stock z3) or "noodler" (opt-in escalation via
    the Noodler CLI runner — Phase 2 PR B). The runner is invoked only for
    backend="noodler" properties; the binary must be present and pinned.
    `decomposition_trace`: falsifiable tried-forms record (design U2) —
    list of decomposition forms already attempted (e.g. ["alphabet",
    "fullmatch-bounds", "per-alternative"]). Escalation to noodler is only
    valid when the trace is non-empty and `decomposition_exhausted` semantics
    hold. None = never decomposed.
    `search_wrapped`: True when the property's pattern is used with search
    semantics (the mirror is the `.*pat.*` wrapped form, design D7). The
    registration gate (gates.validate_pattern) verifies the wrap shape.
    `pattern` / `pattern_flags`: the SOURCE pattern text + flags, declared
    when the property participates in the registration gates (\p gate +
    D7 structural checks). None = no source pattern declared (gate skipped).
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
            "backend": backend,
            "decomposition_trace": decomposition_trace,
            "search_wrapped": search_wrapped,
            "pattern": pattern,
            "pattern_flags": pattern_flags,
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
        "backend": entry.get("backend", "seq"),  # "seq" | "noodler" (additive, Phase 2)
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
        result["result"] = SolveResult.TIMEOUT.value
        result["not_proven"] = True
        result["ok"] = False
        print(
            f"[TIMEOUT] {name}: unknown ({entry['timeout_ms']}ms) — "
            "HARD FAILURE (not proven)"
        )
        return result
    result["result"] = SolveResult.UNSAT.value if r == unsat else SolveResult.SAT.value
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
        if entry["kind"] == PropertyKind.MUTATION_GUARD.value:
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
# Registration validation (Phase 2 PR A — the \p gate + D7 structural gate)
# ---------------------------------------------------------------------------
def validate_registry(registry=None):
    """Run the registration gates over every property that declares a source
    pattern (gates.validate_pattern: \p gate + D7 anchored/wrap checks via the
    Node/regexpp parser). Returns (failures: list[str], checked: int). Call
    BEFORE running properties; the CLI does this by default."""
    from regexproof.harness.gates import RegistrationError, validate_pattern

    registry = REGISTRY if registry is None else registry
    failures, checked = [], 0
    for name, entry in sorted(registry.items()):
        pat = entry.get("pattern")
        if not pat:
            continue
        checked += 1
        try:
            validate_pattern(
                pat,
                entry.get("pattern_flags") or "",
                anchored=(not entry.get("search_wrapped"))
                and entry.get("kind") in ("property", "counterexample_finder"),
                search_wrapped=bool(entry.get("search_wrapped")),
            )
        except RegistrationError as e:
            failures.append(f"{name}: {e}")
    return failures, checked


# ---------------------------------------------------------------------------
# Coverage checks
# ---------------------------------------------------------------------------
def check_mutation_coverage():
    """Structural invariant: every family with a security property,
    counterexample finder, or rule_diff must also have at least one
    mutation guard.

    A property with no mutation guard can go vacuous (e.g. via the
    Complement() trap) without any test noticing. Warn loudly so the gap
    is visible; the warning is the guard's guard."""
    guarded = {
        e["family"] for e in REGISTRY.values() if e["kind"] == PropertyKind.MUTATION_GUARD.value
    }
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

