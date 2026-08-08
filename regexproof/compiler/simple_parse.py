"""Minimal regex AST for encodable-subset dialects (ECMA / RE2 / PCRE).

Handles: literals, `.`, `|`, `()`, `?` `*` `+` `{n,m}`, char classes `[...]`,
shorthands `\\d\\w\\s`, anchors `^$`. Rejects lookarounds, backrefs, `\\b`.
"""

from __future__ import annotations

from dataclasses import dataclass

from regexproof.compiler.base import Unencodable


@dataclass
class Lit:
    ch: str


@dataclass
class Any:
    pass


@dataclass
class Seq:
    items: list


@dataclass
class Alt:
    items: list


@dataclass
class Repeat:
    item: object
    lo: int
    hi: int | None  # None = unbounded


@dataclass
class Cls:
    chars: list[str]  # expanded single chars / ranges already expanded
    negate: bool = False


@dataclass
class Anchor:
    kind: str  # "start" | "end"


@dataclass
class Folded:
    """Scoped case-insensitive subexpression (from `(?i:…)`)."""

    item: object


def _as_seq(node):
    if isinstance(node, Seq):
        return node
    return Seq([node])


def _parse_alt(s: str, i: int, *, allow_scoped_i: bool = True):
    items = []
    node, i = _parse_concat(s, i, allow_scoped_i=allow_scoped_i)
    items.append(node)
    while i < len(s) and s[i] == "|":
        node, i = _parse_concat(s, i + 1, allow_scoped_i=allow_scoped_i)
        items.append(node)
    if len(items) == 1:
        return items[0], i
    return Alt(items), i


def _parse_concat(s: str, i: int, *, allow_scoped_i: bool = True):
    items = []
    while i < len(s) and s[i] not in "|)":
        node, i = _parse_atom(s, i, allow_scoped_i=allow_scoped_i)
        # quantifier
        if i < len(s) and s[i] in "?*+{":
            node, i = _parse_quant(s, i, node)
        items.append(node)
    if not items:
        return Seq([Lit("")]) if False else Seq([]), i
    if len(items) == 1:
        return items[0], i
    return Seq(items), i


def _parse_atom(s: str, i: int, *, allow_scoped_i: bool = True):
    if i >= len(s):
        return Seq([]), i
    ch = s[i]
    if ch == "^":
        return Anchor("start"), i + 1
    if ch == "$":
        return Anchor("end"), i + 1
    if ch == ".":
        return Any(), i + 1
    if ch == "(":
        if i + 2 < len(s) and s[i + 1] == "?":
            # (?...) groups
            if s[i + 2] in ("=", "!", "<"):
                raise Unencodable("lookaround")
            if s[i + 2] == ":":
                inner, j = _parse_alt(s, i + 3, allow_scoped_i=allow_scoped_i)
                if j >= len(s) or s[j] != ")":
                    raise Unencodable("parse-error")
                return inner, j + 1
            # Scoped inline flags: (?i:…), (?ims:…), etc.
            # (?-i:…) and mid-pattern (?i) without ':' stay inline-flag.
            j = i + 2
            scoped = ""
            while j < len(s) and s[j] in "imsx":
                scoped += s[j]
                j += 1
            if scoped and j < len(s) and s[j] == ":":
                if not allow_scoped_i:
                    raise Unencodable("inline-flag")
                # Only ``i`` is modeled; m/s/x scoped still reject honestly.
                if set(scoped) - {"i"}:
                    raise Unencodable("inline-flag")
                inner, k = _parse_alt(s, j + 1, allow_scoped_i=allow_scoped_i)
                if k >= len(s) or s[k] != ")":
                    raise Unencodable("parse-error")
                if "i" in scoped:
                    return Folded(inner), k + 1
                return inner, k + 1
            raise Unencodable("inline-flag")
        inner, j = _parse_alt(s, i + 1, allow_scoped_i=allow_scoped_i)
        if j >= len(s) or s[j] != ")":
            raise Unencodable("parse-error")
        return inner, j + 1
    if ch == "[":
        return _parse_class(s, i)
    if ch == "\\":
        return _parse_escape(s, i)
    if ch in ")*+?{|":
        raise Unencodable("parse-error")
    return Lit(ch), i + 1


def _parse_escape(s: str, i: int):
    if i + 1 >= len(s):
        raise Unencodable("parse-error")
    e = s[i + 1]
    if e in "dws":
        return Cls(chars=[f"\\{e}"], negate=False), i + 2
    if e in "DWS":
        # Represent as negated positive shorthand (\\D ≡ [^\\d] language).
        return Cls(chars=[f"\\{e.lower()}"], negate=True), i + 2
    if e in "bB":
        raise Unencodable("word-boundary")
    if e.isdigit():
        raise Unencodable("backref")
    if e == "n":
        return Lit("\n"), i + 2
    if e == "t":
        return Lit("\t"), i + 2
    if e == "r":
        return Lit("\r"), i + 2
    if e == "x":
        return _parse_hex_escape(s, i)
    if e in r"\\.^$*+?()[]{}|":
        return Lit(e), i + 2
    return Lit(e), i + 2

def _parse_hex_escape(s: str, i: int):
    """Parse ``\\xNN`` or ``\\x{HHHH}`` starting at the backslash index."""
    # s[i] == '\\', s[i+1] == 'x'
    if i + 2 < len(s) and s[i + 2] == "{":
        j = i + 3
        digits: list[str] = []
        while j < len(s) and s[j] != "}":
            if s[j] not in "0123456789abcdefABCDEF":
                raise Unencodable("bad-range")
            digits.append(s[j])
            j += 1
        if not digits or j >= len(s):
            raise Unencodable("bad-range")
        code = int("".join(digits), 16)
        if code > 0x10FFFF:
            raise Unencodable("bad-range")
        return Lit(chr(code)), j + 1
    if i + 3 < len(s) and all(c in "0123456789abcdefABCDEF" for c in s[i + 2 : i + 4]):
        return Lit(chr(int(s[i + 2 : i + 4], 16))), i + 4
    raise Unencodable("bad-range")


def _parse_class(s: str, i: int):
    assert s[i] == "["
    j = i + 1
    negate = False
    if j < len(s) and s[j] == "^":
        negate = True
        j += 1
    chars: list[str] = []
    while j < len(s) and s[j] != "]":
        atom, j, kind = _parse_class_atom(s, j)
        # Range: lo-hi where both ends are single characters (incl. \\xNN).
        if (
            kind == "char"
            and j < len(s)
            and s[j] == "-"
            and j + 1 < len(s)
            and s[j + 1] != "]"
        ):
            j += 1  # skip '-'
            hi_atom, j, hi_kind = _parse_class_atom(s, j)
            if hi_kind != "char":
                raise Unencodable("bad-range")
            lo, hi = atom, hi_atom
            if ord(lo) > ord(hi):
                raise Unencodable("bad-range")
            for code in range(ord(lo), ord(hi) + 1):
                chars.append(chr(code))
            continue
        if kind == "char":
            chars.append(atom)
        else:
            chars.extend(atom)  # shorthand tokens
    if j >= len(s) or s[j] != "]":
        raise Unencodable("parse-error")
    return Cls(chars=chars, negate=negate), j + 1


def _parse_class_atom(s: str, j: int) -> tuple[str | list[str], int, str]:
    """Parse one class member. Returns (payload, next_index, kind).

    kind ``char`` → payload is a one-char string; ``shorthand`` → list of
    tokens such as ``[\"\\\\d\"]`` or ``[\"\\\\D\"]``.
    """
    if j >= len(s):
        raise Unencodable("parse-error")
    if s[j] == "\\":
        node, nj = _parse_escape(s, j)
        if isinstance(node, Lit):
            return node.ch, nj, "char"
        if isinstance(node, Cls):
            tokens: list[str] = []
            if node.negate:
                for c in node.chars:
                    if c == "\\d":
                        tokens.append("\\D")
                    elif c == "\\s":
                        tokens.append("\\S")
                    elif c == "\\w":
                        tokens.append("\\W")
                    else:
                        raise Unencodable("class-escape")
            else:
                tokens.extend(node.chars)
            return tokens, nj, "shorthand"
        raise Unencodable("class-escape")
    return s[j], j + 1, "char"


def _parse_quant(s: str, i: int, node):
    ch = s[i]
    if ch == "?":
        return Repeat(node, 0, 1), i + 1
    if ch == "*":
        return Repeat(node, 0, None), i + 1
    if ch == "+":
        return Repeat(node, 1, None), i + 1
    if ch == "{":
        j = i + 1
        num = ""
        while j < len(s) and s[j].isdigit():
            num += s[j]
            j += 1
        if not num:
            raise Unencodable("parse-error")
        lo = int(num)
        if j < len(s) and s[j] == "}":
            return Repeat(node, lo, lo), j + 1
        if j < len(s) and s[j] == ",":
            j += 1
            num2 = ""
            while j < len(s) and s[j].isdigit():
                num2 += s[j]
                j += 1
            if j >= len(s) or s[j] != "}":
                raise Unencodable("parse-error")
            hi = int(num2) if num2 else None
            return Repeat(node, lo, hi), j + 1
        raise Unencodable("parse-error")
    return node, i


def parse_pattern(pattern: str, *, allow_scoped_i: bool = True):
    """Parse encodable-subset pattern.

    ``allow_scoped_i``: PCRE/RE2 may encode ``(?i:…)``; ECMA must keep
    ``False`` (JS has no scoped inline flags — reject as ``inline-flag``).
    """
    node, i = _parse_alt(pattern, 0, allow_scoped_i=allow_scoped_i)
    if i != len(pattern):
        raise Unencodable("parse-error")
    return node
