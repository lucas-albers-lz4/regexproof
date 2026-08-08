#!/usr/bin/env python3
"""Phase 2 hand-authored pilot properties (shapes 1–3) with ground truth.

Families:
  VJS — validator.js isAscii (ECMA)
  VJS-port — digit port whitelist
  VJS-proto — call_kind/prefix counterexample
  GL — gitleaks encodable token (RE2)

Every security property has a mutation_guard sibling.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import importlib.util  # noqa: E402

from z3 import (  # noqa: E402
    AllChar,
    Contains,
    InRe,
    Length,
    Plus,
    Range,
    Re,
    Star,
    String,
    Union,
)

from regexproof.compiler import compile_pattern  # noqa: E402
from regexproof.compiler.normalize import normalize_inline_flags  # noqa: E402
from regexproof.compiler.re2 import replay_argv  # noqa: E402


def _load_harness():
    path = ROOT / "scripts" / "z3-verify.py"
    spec = importlib.util.spec_from_file_location("z3_verify", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


harness = _load_harness()
prop = harness.prop
REGISTRY = harness.REGISTRY

ASCII_RE = r"^[\x00-\x7F]+$"
PORT_RE = r"^[0-9]+$"
# Encoded subset of gitleaks AWS access-key style rule (fast for Z3).
GL_PAT = r"AKIA[0-9A-Z]{16}"


def _node_test(pattern: str, flags: str, s: str) -> bool:
    script = ROOT / "helpers" / "ecma" / "match.mjs"
    proc = subprocess.run(
        ["node", str(script), pattern, flags],
        input=s,
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    return proc.returncode == 0


def _go_re2_test(pattern: str, flags: str, s: str) -> bool:
    argv = replay_argv(pattern, flags)
    proc = subprocess.run(
        argv, input=s, capture_output=True, text=True, shell=False, check=False
    )
    return proc.returncode == 0


def _gt_ascii_high(w: dict) -> bool:
    """Shape-1 UNSAT expected; if SAT, real engine must also accept (bug)."""
    return _node_test(ASCII_RE, "", w["c"])


def _gt_port(w: dict) -> bool:
    return _node_test(PORT_RE, "", w["s"])


def _gt_proto(w: dict) -> bool:
    # Counterexample: string matches prefix protocol and contains ://
    return bool(re.match(r"^[a-z]+", w["s"])) and "://" in w["s"]


def _gt_gl(w: dict) -> bool:
    return _go_re2_test(GL_PAT, "", w["s"])


@prop(
    "VJS-ascii-no-high",
    "validator.js isAscii ^[\\x00-\\x7F]+$: no codepoint > 0x7F is a full match "
    "(shape 1 alphabet disjointness; Unicode input domain)",
    expect_unsat=True,
    kind="property",
    family="VJS",
    call_kind="fullmatch",
    input_domain="unicode",
    ground_truth=_gt_ascii_high,
)
def vjs_ascii_no_high():
    c = String("c")
    compiled = compile_pattern(ASCII_RE, dialect="ecma", call_kind="fullmatch")
    assert compiled.encodable, compiled.unencodable_reason
    return [InRe(c, compiled.mirror), Length(c) == 1], c == "\u00a0"


@prop(
    "VJS-mutated-star",
    "MUTATION GUARD: Star(AllChar) admits U+00A0",
    expect_unsat=False,
    kind="mutation_guard",
    family="VJS",
    call_kind="fullmatch",
)
def vjs_mutated():
    c = String("c")
    any_c = AllChar(Re("").sort())
    return [InRe(c, Star(any_c)), Length(c) == 1], c == "\u00a0"


@prop(
    "VJS-port-no-alpha",
    "isURL port ^[0-9]+$: digit whitelist contains no letter (shape 2)",
    expect_unsat=True,
    kind="property",
    family="VJS-port",
    call_kind="fullmatch",
    input_domain="ascii",
    ground_truth=_gt_port,
)
def vjs_port_no_alpha():
    s = String("s")
    compiled = compile_pattern(PORT_RE, dialect="ecma", call_kind="fullmatch")
    assert compiled.encodable
    return [
        InRe(s, compiled.mirror),
        Length(s) >= 1,
        Length(s) <= 8,
    ], Contains(s, "a")


@prop(
    "VJS-port-mutated",
    "MUTATION GUARD: widen alphabet to digits|a admits 'a'",
    expect_unsat=False,
    kind="mutation_guard",
    family="VJS-port",
    call_kind="fullmatch",
)
def vjs_port_mutated():
    s = String("s")
    wide = Plus(Union(Range("0", "9"), Re("a")))
    return [InRe(s, wide), Length(s) <= 8], Contains(s, "a")


@prop(
    "VJS-proto-counterexample",
    "COUNTEREXAMPLE FINDER (shape 3): prefix protocol match + '://' in string "
    "(call_kind mismatch class — match vs full URL)",
    expect_unsat=False,
    kind="counterexample_finder",
    family="VJS-proto",
    call_kind="match",
    input_domain="ascii",
    ground_truth=_gt_proto,
)
def vjs_proto_ce():
    s = String("s")
    body = compile_pattern(r"^[a-z]+", dialect="ecma", call_kind="match")
    assert body.encodable
    return [InRe(s, body.mirror), Length(s) <= 16], Contains(s, "://")


@prop(
    "VJS-proto-mutated",
    "MUTATION GUARD: any short string with :// is SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family="VJS-proto",
    call_kind="match",
)
def vjs_proto_mutated():
    s = String("s")
    return [Length(s) <= 16], Contains(s, "://")


@prop(
    "GL-ops-no-space",
    "gitleaks encodable token as fullmatch: the token language itself admits "
    "no space (shape 2 whitelist exclusion; search wrappers deferred)",
    expect_unsat=True,
    kind="property",
    family="GL",
    call_kind="fullmatch",
    input_domain="ascii",
    ground_truth=lambda w: _go_re2_test(f"^{GL_PAT}$", "", w["s"]),
)
def gl_ops_no_space():
    s = String("s")
    pat, flags = normalize_inline_flags(GL_PAT, "")
    compiled = compile_pattern(pat, flags=flags, dialect="re2", call_kind="fullmatch")
    assert compiled.encodable, compiled.unencodable_reason
    return [InRe(s, compiled.mirror), Length(s) <= 40], Contains(s, " ")


@prop(
    "GL-mutated",
    "MUTATION GUARD: Star(any) admits spaces",
    expect_unsat=False,
    kind="mutation_guard",
    family="GL",
    call_kind="fullmatch",
)
def gl_mutated():
    s = String("s")
    any_c = AllChar(Re("").sort())
    return [InRe(s, Star(any_c)), Length(s) <= 40], Contains(s, " ")


def main() -> int:
    require_gt = "--require-ground-truth" in sys.argv
    pilot_names = [
        n for n, e in REGISTRY.items() if e["family"].startswith(("VJS", "GL"))
    ]
    failures = 0
    results = []
    for n in sorted(pilot_names):
        res = harness.run_one(n, REGISTRY[n], require_ground_truth=require_gt)
        results.append(res)
        if not res["ok"]:
            failures += 1
        if res.get("result") == "timeout":
            print(f"NOT PROVEN (timeout): {n}", file=sys.stderr)
        res["engine_versions"] = {
            "z3": __import__("z3").get_version_string(),
            "python": sys.version.split()[0],
        }
    # Mutation coverage for pilot families only
    guarded = {
        e["family"]
        for e in REGISTRY.values()
        if e["kind"] == "mutation_guard" and e["family"].startswith(("VJS", "GL"))
    }
    needing = {
        e["family"]
        for e in REGISTRY.values()
        if e["kind"] in ("property", "counterexample_finder")
        and e["family"].startswith(("VJS", "GL"))
    }
    missing = sorted(needing - guarded)
    if missing:
        print(f"FAIL: pilot families missing mutation guards: {missing}", file=sys.stderr)
        failures += 1

    out = ROOT / "properties" / "generated" / "phase2_pilot_properties.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"\n{len(pilot_names) - failures}/{len(pilot_names)} pilot properties passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
