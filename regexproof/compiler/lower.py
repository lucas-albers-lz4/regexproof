"""Lower simple_parse AST → Z3 with dialect-specific char semantics."""

from __future__ import annotations

from typing import Callable

from z3 import Concat, Plus, Range, Re, Star, Union

from regexproof.compiler.base import Unencodable, any_char, opt, python_trailing_dollar
from regexproof.compiler import simple_parse as sp


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
):
    meta = {"leading_caret": False, "trailing_dollar": False, "has_internal_anchor": False}
    body = _lower_node(
        node,
        fold=fold,
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


def _lower_node(node, *, fold, dot_terminators, digit, space, word, meta, at_start, at_end):
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


def _dot(terminators: frozenset[str]):
    # BMP approximation excluding terminators (same approach as py_re).
    parts = []
    # Split around each terminator — for common {\n} or {\n,\r,U+2028,U+2029}
    ranges = [(0, 0xFFFF)]
    for t in sorted(terminators):
        code = ord(t)
        new_ranges = []
        for lo, hi in ranges:
            if code < lo or code > hi:
                new_ranges.append((lo, hi))
                continue
            if lo <= code - 1:
                new_ranges.append((lo, code - 1))
            if code + 1 <= hi:
                new_ranges.append((code + 1, hi))
        ranges = new_ranges
    for lo, hi in ranges:
        if lo == hi:
            parts.append(Re(chr(lo)))
        else:
            parts.append(Range(chr(lo), chr(hi)))
    return Union(*parts) if len(parts) > 1 else parts[0]


def _class(node: sp.Cls, fold, digit, space, word):
    if node.negate:
        raise Unencodable("negated-class")
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
