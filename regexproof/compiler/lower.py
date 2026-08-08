"""Lower simple_parse AST → Z3 with dialect-specific char semantics."""

from __future__ import annotations

from typing import Callable

from z3 import Concat, Range, Re, Star, Union

from regexproof.compiler.base import (
    Unencodable,
    any_char,
    python_trailing_dollar,
    repeat_z3,
)
from regexproof.compiler import simple_parse as sp

_DIGIT_CODES = frozenset(range(ord("0"), ord("9") + 1))
_SPACE_CODES = frozenset(ord(c) for c in " \t\n\r\f\v")


def space_codes_from_chars(chars: str) -> frozenset[int]:
    """Dialect space alphabet as codepoints (for complement / negated class)."""
    return frozenset(ord(c) for c in chars)


_WORD_CODES = frozenset(
    list(range(ord("a"), ord("z") + 1))
    + list(range(ord("A"), ord("Z") + 1))
    + list(range(ord("0"), ord("9") + 1))
    + [ord("_")]
)
_BMP_HI = 0xFFFF


def lower(
    node,
    *,
    fold: Callable[[str], set[str]] | None,
    dot_terminators: frozenset[str],
    digit: Callable[[], object],
    space: Callable[[], object],
    word: Callable[[], object],
    trailing_dollar_nl: bool,
    call_kind: str,
    case_fold: Callable[[str], set[str]] | None = None,
    allow_ascii_word_boundary: bool = False,
    space_codes: frozenset[int] | None = None,
):
    """Lower AST to Z3.

    ``fold`` is the active case-fold (None unless ignorecase). ``case_fold`` is
    the dialect fold closure used for scoped ``(?i:…)`` (Folded nodes) when
    the outer pattern is case-sensitive.

    ``allow_ascii_word_boundary``: encode edge ``\\b`` (WordBounded) using an
    ASCII ``\\w``/``\\W`` split faithful for RE2/PCRE/ECMA and Python
    ``re.ASCII``. Leave False for Unicode-default Python ``\\b`` (TRAPS #17).
    """
    meta = {
        "leading_caret": False,
        "trailing_dollar": False,
        "has_internal_anchor": False,
        "word_boundary_wrap": False,
    }
    scodes = space_codes if space_codes is not None else _SPACE_CODES
    body = _lower_node(
        node,
        fold=fold,
        case_fold=case_fold or fold,
        dot_terminators=dot_terminators,
        digit=digit,
        space=space,
        word=word,
        meta=meta,
        at_start=True,
        at_end=True,
        allow_ascii_word_boundary=allow_ascii_word_boundary,
        space_codes=scodes,
    )
    if meta["has_internal_anchor"]:
        raise Unencodable("internal-anchor")
    if meta["trailing_dollar"] and trailing_dollar_nl:
        body = python_trailing_dollar(body)
    if meta.get("word_boundary_wrap"):
        # WordBounded lowering already applied search-shaped edge constraints.
        return body, meta
    return _wrap(body, call_kind, meta), meta


def _wrap(body, call_kind, meta):
    any_c = any_char()
    leading = meta["leading_caret"]
    trailing = meta["trailing_dollar"]
    if call_kind == "fullmatch":
        return body
    if call_kind == "match":
        return body if trailing else Concat(body, Star(any_c))
    parts = []
    if not leading:
        parts.append(Star(any_c))
    parts.append(body)
    if not trailing:
        parts.append(Star(any_c))
    return parts[0] if len(parts) == 1 else Concat(*parts)


def _lower_node(
    node,
    *,
    fold,
    case_fold,
    dot_terminators,
    digit,
    space,
    word,
    meta,
    at_start,
    at_end,
    allow_ascii_word_boundary: bool = False,
    space_codes: frozenset[int] = _SPACE_CODES,
):
    if isinstance(node, sp.WordBoundary):
        raise Unencodable("word-boundary")
    if isinstance(node, sp.WordBounded):
        if not allow_ascii_word_boundary:
            raise Unencodable("word-boundary")
        return _lower_word_bounded(
            node,
            fold=fold,
            case_fold=case_fold,
            dot_terminators=dot_terminators,
            digit=digit,
            space=space,
            word=word,
            meta=meta,
            space_codes=space_codes,
        )
    if isinstance(node, sp.Folded):
        active = case_fold if case_fold is not None else fold
        if active is None:
            raise Unencodable("inline-flag")
        return _lower_node(
            node.item,
            fold=active,
            case_fold=case_fold,
            dot_terminators=dot_terminators,
            digit=digit,
            space=space,
            word=word,
            meta=meta,
            at_start=at_start,
            at_end=at_end,
            allow_ascii_word_boundary=allow_ascii_word_boundary,
            space_codes=space_codes,
        )
    if isinstance(node, sp.Lit):
        if node.ch == "":
            return Re("")
        return _lit(node.ch, fold)
    if isinstance(node, sp.Any):
        return _dot(dot_terminators)
    if isinstance(node, sp.Seq):
        items = node.items
        parts = []
        for idx, it in enumerate(items):
            parts.append(
                _lower_node(
                    it,
                    fold=fold,
                    case_fold=case_fold,
                    dot_terminators=dot_terminators,
                    digit=digit,
                    space=space,
                    word=word,
                    meta=meta,
                    at_start=at_start and idx == 0,
                    at_end=at_end and idx == len(items) - 1,
                    allow_ascii_word_boundary=allow_ascii_word_boundary,
                    space_codes=space_codes,
                )
            )
        if not parts:
            return Re("")
        return parts[0] if len(parts) == 1 else Concat(*parts)
    if isinstance(node, sp.Alt):
        # Per-alternative anchors must not hoist onto the whole Union
        # (false-UNSAT under search: ^a|b vs ^(a|b)). Reject like py_re.
        alts = []
        for it in node.items:
            alt_meta = {
                "leading_caret": False,
                "trailing_dollar": False,
                "has_internal_anchor": False,
                "word_boundary_wrap": False,
            }
            lowered = _lower_node(
                it,
                fold=fold,
                case_fold=case_fold,
                dot_terminators=dot_terminators,
                digit=digit,
                space=space,
                word=word,
                meta=alt_meta,
                at_start=at_start,
                at_end=at_end,
                allow_ascii_word_boundary=allow_ascii_word_boundary,
                space_codes=space_codes,
            )
            if alt_meta.get("has_internal_anchor"):
                meta["has_internal_anchor"] = True
            if alt_meta.get("leading_caret") or alt_meta.get("trailing_dollar"):
                raise Unencodable("per-alternative-anchor")
            alts.append(lowered)
        return Union(*alts) if len(alts) > 1 else alts[0]
    if isinstance(node, sp.Repeat):
        inner = _lower_node(
            node.item,
            fold=fold,
            case_fold=case_fold,
            dot_terminators=dot_terminators,
            digit=digit,
            space=space,
            word=word,
            meta=meta,
            at_start=False,
            at_end=False,
            allow_ascii_word_boundary=allow_ascii_word_boundary,
            space_codes=space_codes,
        )
        return _repeat(inner, node.lo, node.hi)
    if isinstance(node, sp.Cls):
        return _class(node, fold, digit, space, word, space_codes=space_codes)
    if isinstance(node, sp.Anchor):
        if node.kind == "start":
            if at_start:
                meta["leading_caret"] = True
                return Re("")
            meta["has_internal_anchor"] = True
            return Re("")
        if node.kind == "end":
            if at_end:
                meta["trailing_dollar"] = True
                return Re("")
            meta["has_internal_anchor"] = True
            return Re("")
    raise Unencodable(f"unsupported-node:{type(node).__name__}")


def _ascii_nonword():
    """RE2/PCRE/ECMA ``\\W``: not ``[A-Za-z0-9_]`` over the BMP."""
    return ranges_excluding(set(_WORD_CODES))


def _lower_word_bounded(
    node: sp.WordBounded,
    *,
    fold,
    case_fold,
    dot_terminators,
    digit,
    space,
    word,
    meta,
    space_codes: frozenset[int] = _SPACE_CODES,
):
    """Encode edge ``\\b`` as (^|\\W)inner(\\W|$) under ASCII ``\\w``.

    Faithful for engines whose ``\\w`` is ASCII (RE2, stock PCRE without UCP,
    ECMA without unicode flag). Emits a search-shaped language and sets
    ``meta['word_boundary_wrap']=True`` so the caller skips a second wrap.
    """
    inner_meta = {
        "leading_caret": False,
        "trailing_dollar": False,
        "has_internal_anchor": False,
        "word_boundary_wrap": False,
    }
    inner = _lower_node(
        node.item,
        fold=fold,
        case_fold=case_fold,
        dot_terminators=dot_terminators,
        digit=digit,
        space=space,
        word=word,
        meta=inner_meta,
        at_start=True,
        at_end=True,
        allow_ascii_word_boundary=False,  # no nested WordBounded
        space_codes=space_codes,
    )
    if inner_meta["has_internal_anchor"]:
        raise Unencodable("internal-anchor")
    any_c = any_char()
    nw = _ascii_nonword()
    # leading \\b: match at start OR after a non-word char.
    # trailing \\b: match at end OR before a non-word char.
    prefix_after_nw = Concat(Star(any_c), nw)
    suffix_at_end = Re("")
    suffix_before_nw = Concat(nw, Star(any_c))

    if node.leading and node.trailing:
        body = Union(
            Concat(inner, suffix_at_end),
            Concat(inner, suffix_before_nw),
            Concat(prefix_after_nw, inner, suffix_at_end),
            Concat(prefix_after_nw, inner, suffix_before_nw),
        )
    elif node.leading:
        body = Union(
            Concat(inner, Star(any_c)),
            Concat(prefix_after_nw, inner, Star(any_c)),
        )
    elif node.trailing:
        body = Union(
            Concat(Star(any_c), inner),
            Concat(Star(any_c), inner, suffix_before_nw),
        )
    else:
        raise Unencodable("word-boundary")
    meta["word_boundary_wrap"] = True
    # Propagate caret/dollar only if inner had them (unusual with \\b wraps).
    meta["leading_caret"] = inner_meta["leading_caret"]
    meta["trailing_dollar"] = inner_meta["trailing_dollar"]
    return body


def _lit(ch: str, fold):
    if fold is None:
        return Re(ch)
    chars = sorted(fold(ch))
    return Re(chars[0]) if len(chars) == 1 else Union(*[Re(c) for c in chars])


def ranges_excluding(forbidden: set[int], *, hi: int = _BMP_HI):
    """Union of BMP (or ASCII) ranges excluding ``forbidden`` codepoints.

    Encodes char-class complement without ``Star(Complement(...))`` (TRAPS #1).
    When the forbidden set is large (e.g. ``[^\\D]``), build the small
    allowed set instead of punching tens of thousands of holes.
    """
    n = hi + 1
    forbid = {c for c in forbidden if 0 <= c <= hi}
    if len(forbid) >= n:
        raise Unencodable("empty-class")
    if len(forbid) > n // 2:
        return _codes_to_union([c for c in range(n) if c not in forbid])
    ranges: list[tuple[int, int]] = [(0, hi)]
    for code in sorted(forbid):
        new_ranges: list[tuple[int, int]] = []
        for lo, rhi in ranges:
            if code < lo or code > rhi:
                new_ranges.append((lo, rhi))
                continue
            if lo <= code - 1:
                new_ranges.append((lo, code - 1))
            if code + 1 <= rhi:
                new_ranges.append((code + 1, rhi))
        ranges = new_ranges
    return _range_pairs_to_union(ranges)


def _codes_to_union(codes: list[int]):
    if not codes:
        raise Unencodable("empty-class")
    codes = sorted(codes)
    pairs: list[tuple[int, int]] = []
    start = prev = codes[0]
    for c in codes[1:]:
        if c == prev + 1:
            prev = c
            continue
        pairs.append((start, prev))
        start = prev = c
    pairs.append((start, prev))
    return _range_pairs_to_union(pairs)


def _range_pairs_to_union(ranges: list[tuple[int, int]]):
    parts = []
    for lo, rhi in ranges:
        if lo == rhi:
            parts.append(Re(chr(lo)))
        else:
            parts.append(Range(chr(lo), chr(rhi)))
    if not parts:
        raise Unencodable("empty-class")
    return Union(*parts) if len(parts) > 1 else parts[0]


def _dot(terminators: frozenset[str]):
    return ranges_excluding({ord(t) for t in terminators})


def _member_codes(
    item: str, fold, *, space_codes: frozenset[int] = _SPACE_CODES
) -> set[int]:
    if item == "\\d":
        return set(_DIGIT_CODES)
    if item == "\\D":
        return set(range(_BMP_HI + 1)) - set(_DIGIT_CODES)
    if item == "\\s":
        return set(space_codes)
    if item == "\\S":
        return set(range(_BMP_HI + 1)) - set(space_codes)
    if item == "\\w":
        return set(_WORD_CODES)
    if item == "\\W":
        return set(range(_BMP_HI + 1)) - set(_WORD_CODES)
    chars = fold(item) if fold is not None else {item}
    return {ord(c) for c in chars if len(c) == 1}


def _class(node: sp.Cls, fold, digit, space, word, *, space_codes=_SPACE_CODES):
    if node.negate:
        forbidden: set[int] = set()
        for item in node.chars:
            forbidden |= _member_codes(item, fold, space_codes=space_codes)
        if not node.chars:
            raise Unencodable("empty-class")
        return ranges_excluding(forbidden)
    parts = []
    for item in node.chars:
        if item == "\\d":
            parts.append(digit())
        elif item == "\\D":
            raise Unencodable("negated-shorthand")
        elif item == "\\s":
            parts.append(space())
        elif item == "\\S":
            raise Unencodable("negated-shorthand")
        elif item == "\\w":
            parts.append(word())
        elif item == "\\W":
            raise Unencodable("negated-shorthand")
        else:
            parts.append(_lit(item, fold))
    if not parts:
        raise Unencodable("empty-class")
    return Union(*parts) if len(parts) > 1 else parts[0]


def _repeat(body, lo, hi):
    """Dialect wrapper — behavior owned by ``repeat_z3`` (fix-wave #73)."""
    return repeat_z3(body, lo, hi)
