"""Caret-in-X pattern-final ``^X(?:R|$)`` lowering (issue #103).

Separate from A1B ([`trailing_alt_dollar`](trailing_alt_dollar.py)): A1B
rejects leading ``^`` in X by design. This shape encodes only:

  - pattern-final non-capturing ``(?:…|$)``
  - X is a single leading ``^`` plus an anchor-free remainder X'

Encoding (search / exec / substitution) — **not** A1B mid-string suffix:

  R-branch ≈ strings with prefix X'R   →  Concat(X'R, Star(any))
  $-branch ≈ strings equal to X'       →  fullmatch(X')
  mirror   = Union(R-branch, $-branch)

Sub-mirrors of X'/R use ``call_kind='fullmatch'`` (#86).
"""

from __future__ import annotations

from typing import Any

from z3 import Concat, Re, Star, Union

from regexproof.compiler.base import (
    CompileResult,
    Unencodable,
    any_char,
    composite_meta,
    wrap_kind_for_call,
)
from regexproof.compiler.trailing_alt_dollar import (
    _unescaped_at,
    _x_has_top_level_anchor,
    split_trailing_dollar,
)

CARET_IN_X_DOMAIN = "ascii;caret_in_x"


def is_caret_in_x_candidate(pattern: str) -> bool:
    """True when pattern looks like ``^X(?:R|$)`` with X' anchor-free."""
    split = split_trailing_dollar(pattern)
    if split is None:
        return False
    x_bare = split["x_bare"]
    if not x_bare.startswith("^") or not _unescaped_at(x_bare, 0):
        return False
    x_inner = x_bare[1:]
    # Remainder must not introduce further top-level ^ / $.
    if _x_has_top_level_anchor(x_inner):
        return False
    return True


def try_compile_caret_in_x(
    pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    *,
    max_length: int = 256,
    compile_bare,
) -> CompileResult | None:
    """Return caret-in-X CompileResult, or None if outside the class."""
    if len(pattern) > max_length:
        return None
    if not is_caret_in_x_candidate(pattern):
        return None

    split = split_trailing_dollar(pattern)
    assert split is not None
    x_inner = split["x_bare"][1:]
    domain = CARET_IN_X_DOMAIN

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
        if not x_inner:
            # ^(?:R|$) — empty X'
            if split["r_alt"]:
                r_cr = compile_bare(split["r_alt"], flags, dialect, "fullmatch")
                if not r_cr.encodable:
                    return _fail(r_cr.unencodable_reason or "per-alternative-anchor")
                r_body = r_cr.mirror
            else:
                r_body = Re("")
            empty = Re("")
            any_c = any_char()
            star = Star(any_c)
            if call_kind in ("search", "exec", "substitution", "match"):
                mirror: Any = Union(Concat(r_body, star), empty)
            elif call_kind == "fullmatch":
                mirror = Union(r_body, empty)
            else:
                return None
            # C1 fold (luna re-gate): a \b-containing R subcompile stays
            # word-boundary-wrapped — propagate, never hardcode False.
            # A boundary-wrapped child makes the composite search-shaped
            # (matches lower.py's convention), so wrap_kind normalizes.
            wb = bool(r_cr.word_boundary_wrap) if split["r_alt"] else False
            meta = composite_meta(
                leading_caret=True,
                # C1 fold (luna re-gate 3): trailing_dollar is source-derived
                # (lower.py sets it from the $ node) — the fast-path shape
                # `^(?:X|$)` has the trailing $ alternative by construction.
                trailing_dollar=True,
                word_boundary_wrap=wb,
                wrap_kind="search" if wb else wrap_kind_for_call(call_kind),
                mirror_exact=bool(r_cr.mirror_exact) if split["r_alt"] else True,
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

        x_cr = compile_bare(x_inner, flags, dialect, "fullmatch")
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
        if call_kind in ("search", "exec", "substitution", "match"):
            # Leading ^ ⇒ no leading Star(any); R-branch allows trailing junk.
            core = Concat(xr_body, star)
            suffix = x_cr.mirror  # exact X'
            mirror = Union(core, suffix)
        elif call_kind == "fullmatch":
            mirror = Union(xr_body, x_cr.mirror)
        else:
            return None

        # C1 (issue #426): synthesize the metadata contract this fast path
        # bypasses ``lower()``'s ``_meta`` dict — leading ^ is structural, the
        # union is never the bare body, and any ``\b`` sub-mirror stays
        # word-boundary-wrapped (no second wrap applied).
        wb = any(m.get("word_boundary_wrap") for m in sub_metas)
        meta = composite_meta(
            leading_caret=True,
            # C1 fold (luna re-gate 3): source-derived — the `^(?:X|$)` shape
            # carries the trailing $ alternative.
            trailing_dollar=True,
            word_boundary_wrap=wb,
            wrap_kind="search" if wb else wrap_kind_for_call(call_kind),
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
