"""Lower simple_parse AST → Z3 with dialect-specific char semantics."""

from __future__ import annotations

from typing import Callable

from z3 import Concat, Plus, Range, Re, Star, Union

from regexproof.compiler.base import Unencodable, any_char, opt, python_trailing_dollar
from regexproof.compiler import simple_parse as sp

_DIGIT_CODES = frozenset(range(ord("0"), ord("9") + 1))
_SPACE_CODES = frozenset(ord(c) for c in " \t\n\r\f\v")
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
):
    """Lower AST to Z3.

    ``fold`` is the active case-fold (None unless ignorecase). ``case_fold`` is
    the dialect fold closure used for scoped ``(?i:…)`` (Folded nodes) when
    the outer pattern is case-sensitive.
    """
    meta = {"leading_caret": False, "trailing_dollar": False, "has_internal_anchor": False}
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
    )
    if meta["has_internal_anchor"]:
        raise Unencodable("internal-anchor")
    if meta["trailing_dollar"] and trailing_dollar_nl:
        body = python_trailing_dollar(body)
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
    node, *, fold, case_fold, dot_terminators, digit, space, word, meta, at_start, at_end
):
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
                )
            )
        if not parts:
            return Re("")
        return parts[0] if len(parts) == 1 else Concat(*parts)
    if isinstance(node, sp.Alt):
        alts = [
            _lower_node(
                it,
                fold=fold,
                case_fold=case_fold,
                dot_terminators=dot_terminators,
                digit=digit,
                space=space,
                word=word,
                meta=meta,
                at_start=at_start,
                at_end=at_end,
            )
            for it in node.items
        ]
        return Union(*alts)
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
        )
        return _repeat(inner, node.lo, node.hi)
    if isinstance(node, sp.Cls):
        return _class(node, fold, digit, space, word)
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


def _member_codes(item: str, fold) -> set[int]:
    if item == "\\d":
        return set(_DIGIT_CODES)
    if item == "\\D":
        return set(range(_BMP_HI + 1)) - set(_DIGIT_CODES)
    if item == "\\s":
        return set(_SPACE_CODES)
    if item == "\\S":
        return set(range(_BMP_HI + 1)) - set(_SPACE_CODES)
    if item == "\\w":
        return set(_WORD_CODES)
    if item == "\\W":
        return set(range(_BMP_HI + 1)) - set(_WORD_CODES)
    chars = fold(item) if fold is not None else {item}
    return {ord(c) for c in chars if len(c) == 1}


def _class(node: sp.Cls, fold, digit, space, word):
    if node.negate:
        forbidden: set[int] = set()
        for item in node.chars:
            forbidden |= _member_codes(item, fold)
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
    from z3 import Loop

    if lo == 0 and hi == 1:
        return opt(body)
    if lo == 0 and hi is None:
        return Star(body)
    if lo == 1 and hi is None:
        return Plus(body)
    if hi is None:
        return Concat(*([body] * lo), Star(body)) if lo else Star(body)
    if lo == hi:
        if lo <= 0:
            return Re("")
        if lo == 1:
            # Z3 Concat requires ≥2 args; `{1}` / `{1,1}` is identity.
            return body
        return Concat(*([body] * lo))
    return Loop(body, lo, hi)
