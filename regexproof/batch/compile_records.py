"""Public compile_records API — pattern → encodable rows (#193)."""

from __future__ import annotations

import time
from typing import Any

from regexproof.batch.budgets import (
    BudgetBreached,
    apply_address_space_cap,
    check_budget_mem,
    check_budget_patterns,
)
from regexproof.batch.negation_policy import (
    NEGATED_UNSUPPORTED_REASON,
    should_reject_negated,
)
from regexproof.compiler import compile_pattern
from regexproof.compiler.normalize import normalize_inline_flags

def compile_records(
    records: list[dict[str, Any]],
    *,
    lift_inline: bool,
    corpus_slug: str,
    budget: dict[str, Any] | None = None,
    wall_t0: float | None = None,
) -> list[dict[str, Any]]:
    budget = budget or {}
    check_budget_patterns(records, budget, corpus_slug)
    max_wall = budget.get("max_wall_s")
    max_mem = budget.get("max_mem_mb")
    # wall_t0 may be set before extraction so max_wall_s covers extract+compile.
    t0 = wall_t0 if wall_t0 is not None else time.monotonic()
    if max_mem:
        apply_address_space_cap(budget)
    else:
        from regexproof.batch import budgets as _budgets

        _budgets.LAST_ADDRESS_SPACE_CAP_APPLIED = None
    out = []
    for rec in records:
        pattern = rec["pattern"]
        flags = rec.get("flags") or ""
        if lift_inline:
            pattern, flags = normalize_inline_flags(pattern, flags)
        if rec.get("unencodable_reason"):
            out.append(
                {
                    **rec,
                    "encodable": False,
                    "compile_reason": rec["unencodable_reason"],
                    "corpus": corpus_slug,
                    "corpus_slug": corpus_slug,
                }
            )
            continue
        # ModSecurity !@rx / selectors: never silent-positive (fix-wave #72).
        if rec.get("negated") and should_reject_negated(rec.get("dialect") or ""):
            out.append(
                {
                    **rec,
                    "encodable": False,
                    "compile_reason": NEGATED_UNSUPPORTED_REASON,
                    "unencodable_reason": NEGATED_UNSUPPORTED_REASON,
                    "corpus": corpus_slug,
                    "corpus_slug": corpus_slug,
                }
            )
            continue
        try:
            cr = compile_pattern(
                pattern,
                flags,
                rec["dialect"],
                rec["call_kind"],
                domain=rec.get("domain") or "ascii",
            )
        except MemoryError as exc:
            raise BudgetBreached(
                corpus_slug,
                "max_mem_mb",
                max_mem or 0,
                check_budget_mem(),
            ) from exc
        row = {
            **rec,
            "pattern": pattern,
            "flags": flags,
            "encodable": cr.encodable,
            "compile_reason": cr.unencodable_reason,
            "corpus": corpus_slug,
            "corpus_slug": corpus_slug,
        }
        # Surface compile timeouts for triage kind=timeout (fix-wave #71).
        if cr.unencodable_reason == "timeout":
            row["result"] = "timeout"
        out.append(row)

        if max_wall and (time.monotonic() - t0) > max_wall:
            raise BudgetBreached(corpus_slug, "max_wall_s", max_wall, time.monotonic() - t0)
        if max_mem:
            rss = check_budget_mem()
            if rss > max_mem:
                raise BudgetBreached(corpus_slug, "max_mem_mb", max_mem, rss)

    return out


