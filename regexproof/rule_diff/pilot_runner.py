"""Shared shape-5 pilot registration helpers (#194).

Pilots keep their own discovery/main/report assembly; the gap/control/widen/
narrow property triplet is registered here so kind/expect_unsat semantics
cannot diverge across scripts.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from z3 import Concat, Re, Star

from regexproof.compiler import compile_pattern
from regexproof.rule_diff.encode import shape5_constraints
from regexproof.rule_diff.timeout_gate import fail_message, timeout_gate

LengthBoundsFn = Callable[[str], tuple[int, int]]
ReplayFn = Callable[[str, str, str], bool]  # (pattern, flags, s) -> matched


@dataclass(frozen=True)
class Shape5PairConfig:
    """How to compile and ground-truth one admitted pair."""

    dialect_r1: str
    dialect_r2: str
    timeout_ms: int
    length_bounds: LengthBoundsFn
    ground_truth: Callable[[dict[str, Any], dict[str, Any]], bool] | None = None
    # ground_truth(pair, witness) -> bool; None skips GT callback
    domain_fn: Callable[[dict[str, Any], int, int], str] | None = None
    solver_call_kind: str = "fullmatch"
    include_narrow_r2: bool = True
    max_length: int = 256


def load_harness():
    """Importable harness (post-#192)."""
    import regexproof.harness as harness

    return harness


def register_shape5_pair(
    harness,
    pair: dict[str, Any],
    *,
    cfg: Shape5PairConfig,
) -> None:
    """Register gap + control + widen-R1 (+ optional narrow-R2) for one pair."""
    prop = harness.prop
    family = pair["family"]
    r1 = pair["r1"]
    r2 = pair["r2"]
    lo, hi = cfg.length_bounds(r2["pattern"])
    r1_c = compile_pattern(
        r1["pattern"],
        r1["flags"],
        cfg.dialect_r1,
        cfg.solver_call_kind,
        max_length=cfg.max_length,
    )
    r2_c = compile_pattern(
        r2["pattern"],
        r2["flags"],
        cfg.dialect_r2,
        cfg.solver_call_kind,
        max_length=cfg.max_length,
    )
    assert r1_c.encodable and r2_c.encodable, (
        r1_c.unencodable_reason,
        r2_c.unencodable_reason,
    )

    gt = None
    if cfg.ground_truth is not None:
        _gt = cfg.ground_truth

        def gt(w: dict, _pair=pair, _fn=_gt) -> bool:
            return bool(_fn(_pair, w))

    if cfg.domain_fn is not None:
        domain = cfg.domain_fn(pair, lo, hi)
    else:
        domain = (
            f"len(s) in [{lo},{hi}]; dialect_r1={cfg.dialect_r1}; "
            f"dialect_r2={cfg.dialect_r2}; solver_call_kind={cfg.solver_call_kind}"
        )
        if pair.get("call_kind"):
            domain = f"{domain}; site_call_kind={pair['call_kind']}"

    input_domain = pair.get("declared_domain") or "ascii"
    call_kind = pair.get("call_kind") or "search"

    @prop(
        f"{family}-gap",
        domain,
        expect_unsat=True,
        timeout_ms=cfg.timeout_ms,
        ground_truth=gt,
        kind="rule_diff",
        family=family,
        input_domain=input_domain,
        call_kind=call_kind,
    )
    def _gap():
        constraints, bad, _s = shape5_constraints(
            r1_c.mirror, r2_c.mirror, min_len=lo, max_len=hi
        )
        return constraints, bad

    @prop(
        f"{family}-control",
        domain,
        expect_unsat=True,
        timeout_ms=cfg.timeout_ms,
        kind="mutation_guard",
        family=family,
        input_domain=input_domain,
        call_kind=call_kind,
    )
    def _control():
        constraints, bad, _s = shape5_constraints(
            r2_c.mirror, r2_c.mirror, min_len=lo, max_len=hi
        )
        return constraints, bad

    narrow_r1 = Concat(Re("\x01"), Star(Re("\x01")))

    @prop(
        f"{family}-widen-R1",
        domain,
        expect_unsat=False,
        timeout_ms=cfg.timeout_ms,
        kind="mutation_guard",
        family=family,
        input_domain=input_domain,
        call_kind=call_kind,
    )
    def _widen_r1():
        constraints, bad, _s = shape5_constraints(
            narrow_r1, r2_c.mirror, min_len=lo, max_len=hi
        )
        return constraints, bad

    if cfg.include_narrow_r2:

        @prop(
            f"{family}-narrow-R2",
            domain,
            expect_unsat=True,
            timeout_ms=cfg.timeout_ms,
            kind="mutation_guard",
            family=family,
            input_domain=input_domain,
            call_kind=call_kind,
        )
        def _narrow_r2():
            constraints, bad, _s = shape5_constraints(
                r1_c.mirror, r1_c.mirror, min_len=lo, max_len=hi
            )
            return constraints, bad

        _ = _narrow_r2

    _ = (_gap, _control, _widen_r1)


def run_registered(
    harness,
    *,
    family_prefix: str | None = None,
    require_ground_truth: bool = False,
    timeout_allowlist: frozenset[str] | None = None,
) -> tuple[list[dict[str, Any]], bool, int, float, list[str]]:
    """Run registry entries (optionally filtered) and apply timeout_gate."""
    names = sorted(
        n
        for n, e in harness.REGISTRY.items()
        if family_prefix is None or e.get("family") == family_prefix or n.startswith(family_prefix)
    )
    # Prefer filter by family when prefix looks like a family id
    if family_prefix and not any(n.startswith(f"{family_prefix}-") for n in names):
        names = sorted(
            n for n, e in harness.REGISTRY.items() if e.get("family") == family_prefix
        )
    results = []
    for name in names:
        entry = harness.REGISTRY[name]
        if family_prefix and entry.get("family") != family_prefix and not name.startswith(
            f"{family_prefix}-"
        ):
            continue
        res = harness.run_one(name, entry, require_ground_truth=require_ground_truth)
        # rule_diff: both sat and unsat are valid; only timeout fails.
        if entry.get("kind") == "rule_diff" and res.get("result") in ("sat", "unsat"):
            res = dict(res)
            res["ok"] = True
        results.append(res)
    ok, n_timeout, rate, bad = timeout_gate(
        results, allowlist=timeout_allowlist
    )
    return results, ok, n_timeout, rate, bad


__all__ = [
    "Shape5PairConfig",
    "fail_message",
    "load_harness",
    "register_shape5_pair",
    "run_registered",
    "timeout_gate",
]
