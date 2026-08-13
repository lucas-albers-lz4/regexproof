"""Pattern-final ``(?:...|$)`` lowering (wave #81 / P2 #87).

Accept condition (strict):
  - pattern ends with a non-capturing alternation whose final branch is ``$``
  - that alternation is the last pattern element
  - prefix X is anchor-free at top level (no ``^`` / ``$``); ``\\b`` allowed
  - no other anchors inside the final alternation's non-``$`` branches

Encoding (A1B language as a regex mirror; length bound is declared domain):

  core   ≈ Star(any)·X·R·(Star(any) for search)
  suffix ≈ Star(any)·X          # regex form of SuffixOf + InRe(q, X)
  mirror = Union(core, suffix)

Bare X/R sub-mirrors use ``call_kind='fullmatch'`` (search wrappers in
sub-expression position are unsound — #86). ``\\b INNER`` suffix uses
``wb_leading_suffix_mirror`` (stock WordBounded+``$`` false-SAT).

Property sat-find should prefer case-split Or branches and may declare
``Length(q) ≤ A1B_SUFFIX_BOUND`` (default 128) on the suffix witness.
"""

from __future__ import annotations

from typing import Any

from z3 import Concat, Re, Star, Union

from regexproof.compiler.base import (
    CompileResult,
    Unencodable,
    any_char,
    composite_meta,
    opt,
    wrap_kind_for_call,
)
from regexproof.compiler.lower import ranges_excluding

A1B_SUFFIX_BOUND = 128

_WORD_CODES = frozenset(
    list(range(ord("a"), ord("z") + 1))
    + list(range(ord("A"), ord("Z") + 1))
    + list(range(ord("0"), ord("9") + 1))
    + [ord("_")]
)


def _unescaped_at(s: str, i: int) -> bool:
    n = 0
    j = i - 1
    while j >= 0 and s[j] == "\\":
        n += 1
        j -= 1
    return n % 2 == 0


def final_noncap_open(pattern: str) -> int | None:
    """Index of ``(?:`` opening the group closed by final ``|$)``."""
    if not pattern.endswith("|$)") :
        return None
    depth = 0
    i = len(pattern) - 1
    while i >= 0:
        ch = pattern[i]
        if ch in "()" and _unescaped_at(pattern, i):
            if ch == ")":
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    if pattern.startswith("(?:", i):
                        return i
                    return None
        i -= 1
    return None


def split_trailing_dollar(pattern: str) -> dict[str, str] | None:
    """Split pattern-final ``(?:R|$)`` into x_bare / r_alt / xr strings."""
    open_idx = final_noncap_open(pattern)
    if open_idx is None:
        return None
    # Inside (?: … |$) — slice drops "(?:" and the trailing "|$)".
    r_alt = pattern[open_idx + 3 : -3]
    x_bare = pattern[:open_idx]
    if r_alt:
        xr = f"{x_bare}(?:{r_alt})"
    else:
        xr = x_bare if x_bare else "(?:)"
    return {
        "x_bare": x_bare,
        "r_alt": r_alt,
        "xr": xr,
        "empty_x": not x_bare,
    }


def _x_has_top_level_anchor(x_bare: str) -> bool:
    """Reject X with top-level ``^`` / ``$`` (``\\b`` is ok)."""
    if not x_bare:
        return False
    if x_bare.startswith("^") and _unescaped_at(x_bare, 0):
        return True
    # Scan for unescaped $ outside classes / groups — conservative: any
    # unescaped $ in X (final alt already stripped).
    in_class = False
    i = 0
    while i < len(x_bare):
        ch = x_bare[i]
        if ch == "\\" and i + 1 < len(x_bare):
            i += 2
            continue
        if ch == "[":
            in_class = True
        elif ch == "]" and in_class:
            in_class = False
        elif ch == "$" and not in_class:
            return True
        i += 1
    return False


def wb_leading_suffix_mirror(inner_mirror):
    """``(^|\\W) INNER $`` — no trailing Star(any)."""
    nw = ranges_excluding(set(_WORD_CODES))
    any_c = any_char()
    return Union(inner_mirror, Concat(Star(any_c), nw, inner_mirror))


def try_compile_trailing_alt_dollar(
    pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    *,
    max_length: int = 256,
    compile_bare,
) -> CompileResult | None:
    """Return A1B CompileResult, or None if the pattern is outside the class.

    ``compile_bare(pattern, flags, dialect, call_kind)`` must compile without
    re-entering this lowering (skip flag in the dispatcher).
    """
    if len(pattern) > max_length:
        return None
    split = split_trailing_dollar(pattern)
    if split is None:
        return None
    if _x_has_top_level_anchor(split["x_bare"]):
        return None

    domain = f"ascii;a1b_suffix_bound={A1B_SUFFIX_BOUND}"

    def _fail(reason: str) -> CompileResult:
        return CompileResult(
            mirror=None,
            unencodable_reason=reason,
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
        )

    try:
        if split["empty_x"]:
            # (?:R|$) under search/exec: empty-at-EOS → universal language.
            if call_kind in ("search", "exec", "substitution"):
                mirror: Any = Star(any_char())
                meta = composite_meta(
                    leading_caret=False,
                    trailing_dollar=False,
                    word_boundary_wrap=False,
                    wrap_kind="search",
                    mirror_exact=True,
                )
                return CompileResult(
                    mirror=mirror,
                    unencodable_reason=None,
                    dialect=dialect,
                    call_kind=call_kind,
                    flags=flags,
                    pattern=pattern,
                    declared_domain=domain,
                    meta=meta,
                )
            # match/fullmatch: R | ε
            if split["r_alt"]:
                r_cr = compile_bare(split["r_alt"], flags, dialect, "fullmatch")
                if not r_cr.encodable:
                    return _fail(r_cr.unencodable_reason or "per-alternative-anchor")
                body = (
                    opt(r_cr.mirror)
                    if call_kind == "fullmatch"
                    else Concat(opt(r_cr.mirror), Star(any_char()))
                )
                mirror_exact = bool(r_cr.mirror_exact)
            else:
                body = Re("")
                mirror_exact = True
            meta = composite_meta(
                leading_caret=False,
                trailing_dollar=(call_kind == "fullmatch"),
                word_boundary_wrap=False,
                wrap_kind=wrap_kind_for_call(call_kind),
                mirror_exact=mirror_exact,
            )
            return CompileResult(
                mirror=body,
                unencodable_reason=None,
                dialect=dialect,
                call_kind=call_kind,
                flags=flags,
                pattern=pattern,
                declared_domain=domain,
                meta=meta,
            )

        x_bare = split["x_bare"]
        is_wb = x_bare.startswith("\\b")

        if is_wb:
            # XR via normal search compile (WordBounded wrap); suffix via WB helper.
            xr_cr = compile_bare(split["xr"], flags, dialect, call_kind)
            if not xr_cr.encodable:
                return _fail(xr_cr.unencodable_reason or "per-alternative-anchor")
            inner_pat = x_bare[2:]
            if inner_pat.endswith("\\b"):
                inner_pat = inner_pat[:-2]
            inner_cr = compile_bare(inner_pat, flags, dialect, "fullmatch")
            if not inner_cr.encodable:
                return _fail(inner_cr.unencodable_reason or "per-alternative-anchor")
            suffix_m = wb_leading_suffix_mirror(inner_cr.mirror)
            # xr_cr.mirror already search-shaped for WordBounded; do not re-wrap.
            mirror = Union(xr_cr.mirror, suffix_m)
            meta = composite_meta(
                leading_caret=False,
                trailing_dollar=False,
                word_boundary_wrap=True,
                wrap_kind="search",
                mirror_exact=bool(xr_cr.mirror_exact)
                and bool(inner_cr.mirror_exact),
            )
            return CompileResult(
                mirror=mirror,
                unencodable_reason=None,
                dialect=dialect,
                call_kind=call_kind,
                flags=flags,
                pattern=pattern,
                declared_domain=domain,
                meta=meta,
            )

        x_cr = compile_bare(x_bare, flags, dialect, "fullmatch")
        if not x_cr.encodable:
            return _fail(x_cr.unencodable_reason or "per-alternative-anchor")
        sub_metas = [x_cr.meta or {}]
        if split["r_alt"]:
            r_cr = compile_bare(split["r_alt"], flags, dialect, "fullmatch")
            if not r_cr.encodable:
                return _fail(r_cr.unencodable_reason or "per-alternative-anchor")
            xr_body = Concat(x_cr.mirror, r_cr.mirror)
            sub_metas.append(r_cr.meta or {})
        else:
            xr_body = x_cr.mirror

        any_c = any_char()
        star = Star(any_c)
        if call_kind in ("search", "exec", "substitution"):
            core = Concat(star, xr_body, star)
            suffix = Concat(star, x_cr.mirror)
            mirror = Union(core, suffix)
        elif call_kind == "match":
            core = Concat(xr_body, star)
            suffix = x_cr.mirror  # whole-string X
            mirror = Union(core, suffix)
        elif call_kind == "fullmatch":
            mirror = Union(xr_body, x_cr.mirror)
        else:
            return None

        # C1 (issue #426): synthesize the metadata contract this fast path
        # bypasses ``lower()``'s ``_meta`` dict — X is anchor-free (no
        # leading_caret) and the union is never the bare body.
        meta = composite_meta(
            leading_caret=False,
            trailing_dollar=(call_kind == "fullmatch"),
            word_boundary_wrap=False,
            wrap_kind=wrap_kind_for_call(call_kind),
            mirror_exact=all(bool(m.get("mirror_exact")) for m in sub_metas),
        )
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
            meta=meta,
        )
    except Unencodable as exc:
        return _fail(exc.reason)
