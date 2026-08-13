"""Minimal regex AST for encodable-subset dialects (ECMA / RE2 / PCRE).

Handles: literals, `.`, `|`, `()`, `?` `*` `+` `{n,m}`, char classes `[...]`,
shorthands `\\d\\w\\s`, anchors `^$`, word boundaries `\\b` (lowered only under
ASCII-domain dialects — see ``lower``). Rejects lookarounds, backrefs, `\\B`.
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


@dataclass
class WordBoundary:
    """Zero-width ASCII word boundary (``\\b``). ``\\B`` is not represented."""

    pass


@dataclass
class WordBounded:
    """Inner pattern with leading/trailing ``\\b`` constraints (post-rewrite)."""

    item: object
    leading: bool = True
    trailing: bool = True


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
                    raise Unencodable("unsupported-syntax")
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
                    raise Unencodable("unsupported-syntax")
                if "i" in scoped:
                    return Folded(inner), k + 1
                return inner, k + 1
            raise Unencodable("inline-flag")
        inner, j = _parse_alt(s, i + 1, allow_scoped_i=allow_scoped_i)
        if j >= len(s) or s[j] != ")":
            raise Unencodable("unclosed-group")
        return inner, j + 1
    if ch == "[":
        return _parse_class(s, i)
    if ch == "\\":
        return _parse_escape(s, i)
    if ch == "{":
        # Lone '{' as atom (e.g. pattern starts with '{?') — literal.
        brace: object = Lit("{")
        j = i + 1
        if j < len(s) and s[j] in "?*+":
            brace, j = _parse_quant(s, j, brace)
        return brace, j
    if ch in ")*+?|":
        raise Unencodable("unsupported-syntax")
    return Lit(ch), i + 1


def _parse_escape(s: str, i: int):
    if i + 1 >= len(s):
        raise Unencodable("unsupported-syntax")
    e = s[i + 1]
    if e in "dws":
        return Cls(chars=[f"\\{e}"], negate=False), i + 2
    if e in "DWS":
        # Represent as negated positive shorthand (\\D ≡ [^\\d] language).
        return Cls(chars=[f"\\{e.lower()}"], negate=True), i + 2
    if e == "B":
        # Negated boundary: rare in corpora; keep honest reject.
        raise Unencodable("word-boundary")
    if e == "b":
        return WordBoundary(), i + 2
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
    if e == "u":
        return _parse_unicode_escape(s, i)
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


def _parse_unicode_escape(s: str, i: int):
    """Parse the fixed-width / braced Unicode escape used by ECMAScript."""
    if i + 2 < len(s) and s[i + 2] == "{":
        j = s.find("}", i + 3)
        if j < 0 or not s[i + 3 : j] or any(
            c not in "0123456789abcdefABCDEF" for c in s[i + 3 : j]
        ):
            raise Unencodable("bad-range")
        code = int(s[i + 3 : j], 16)
        if code > 0x10FFFF:
            raise Unencodable("bad-range")
        return Lit(chr(code)), j + 1
    if i + 5 < len(s) and all(c in "0123456789abcdefABCDEF" for c in s[i + 2 : i + 6]):
        return Lit(chr(int(s[i + 2 : i + 6], 16))), i + 6
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
        raise Unencodable("unclosed-class")
    return Cls(chars=chars, negate=negate), j + 1


def _parse_class_atom(s: str, j: int) -> tuple[str | list[str], int, str]:
    """Parse one class member. Returns (payload, next_index, kind).

    kind ``char`` → payload is a one-char string; ``shorthand`` → list of
    tokens such as ``[\"\\\\d\"]`` or ``[\"\\\\D\"]``.
    """
    if j >= len(s):
        raise Unencodable("unsupported-syntax")
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
        j = i + 1
        if j < len(s) and s[j] == "?":
            j += 1  # lazy optional — same language (fix-wave #69)
        return Repeat(node, 0, 1), j
    if ch == "*":
        j = i + 1
        if j < len(s) and s[j] == "?":
            j += 1  # lazy star — same language (fix-wave #69)
        return Repeat(node, 0, None), j
    if ch == "+":
        j = i + 1
        if j < len(s) and s[j] == "?":
            j += 1  # lazy plus — same language (fix-wave #69)
        return Repeat(node, 1, None), j
    if ch == "{":
        j = i + 1
        num = ""
        while j < len(s) and s[j].isdigit():
            num += s[j]
            j += 1
        if not num:
            # PCRE/RE2: non-quantifier '{' is a literal; following ?/*/+ apply to it.
            brace: object = Lit("{")
            j = i + 1
            if j < len(s) and s[j] in "?*+":
                brace, j = _parse_quant(s, j, brace)
            return Seq([node, brace]), j
        lo = int(num)
        if j < len(s) and s[j] == "}":
            j += 1
            if j < len(s) and s[j] == "?":
                j += 1  # lazy {n} — same language (fix-wave #69)
            return Repeat(node, lo, lo), j
        if j < len(s) and s[j] == ",":
            j += 1
            num2 = ""
            while j < len(s) and s[j].isdigit():
                num2 += s[j]
                j += 1
            if j >= len(s) or s[j] != "}":
                brace = Lit("{")
                k = i + 1
                if k < len(s) and s[k] in "?*+":
                    brace, k = _parse_quant(s, k, brace)
                return Seq([node, brace]), k
            hi = int(num2) if num2 else None
            j += 1
            if j < len(s) and s[j] == "?":
                j += 1  # lazy bound — same language (fix-wave #69)
            return Repeat(node, lo, hi), j
        brace = Lit("{")
        k = i + 1
        if k < len(s) and s[k] in "?*+":
            brace, k = _parse_quant(s, k, brace)
        return Seq([node, brace]), k
    return node, i


def parse_pattern(pattern: str, *, allow_scoped_i: bool = True):
    """Parse encodable-subset pattern.

    ``allow_scoped_i``: PCRE/RE2 may encode ``(?i:…)``; ECMA must keep
    ``False`` (JS has no scoped inline flags — reject as ``inline-flag``).
    """
    node, i = _parse_alt(pattern, 0, allow_scoped_i=allow_scoped_i)
    if i != len(pattern):
        raise Unencodable("unsupported-syntax")
    return rewrite_word_boundaries(node)


def rewrite_word_boundaries(node):
    """Collapse edge ``\\b`` into ``WordBounded``; reject mid-pattern / nested WB."""
    if isinstance(node, WordBoundary):
        # Lone \\b is not a useful encodable pattern.
        raise Unencodable("word-boundary")
    if isinstance(node, WordBounded):
        return WordBounded(
            rewrite_word_boundaries(node.item),
            leading=node.leading,
            trailing=node.trailing,
        )
    if isinstance(node, Folded):
        return Folded(rewrite_word_boundaries(node.item))
    if isinstance(node, Repeat):
        # \\b cannot be quantified meaningfully for our edge rewrite.
        if _contains_word_boundary(node.item):
            raise Unencodable("word-boundary")
        return Repeat(rewrite_word_boundaries(node.item), node.lo, node.hi)
    if isinstance(node, Alt):
        return Alt([rewrite_word_boundaries(it) for it in node.items])
    if isinstance(node, Seq):
        # Recurse into non-WB children first; leave WordBoundary atoms intact.
        items = []
        for it in node.items:
            if isinstance(it, WordBoundary):
                items.append(it)
            else:
                items.append(rewrite_word_boundaries(it))
        flat: list = []
        for it in items:
            if isinstance(it, Seq):
                flat.extend(it.items)
            else:
                flat.append(it)
        wb_idx = [i for i, it in enumerate(flat) if isinstance(it, WordBoundary)]
        if not wb_idx:
            return Seq(flat) if len(flat) != 1 else flat[0]
        leading = 0 in wb_idx
        trailing = (len(flat) - 1) in wb_idx
        # Only edge WBs supported (leading and/or trailing); no mid-pattern \\b.
        allowed = set()
        if leading:
            allowed.add(0)
        if trailing:
            allowed.add(len(flat) - 1)
        if set(wb_idx) - allowed:
            raise Unencodable("word-boundary")
        inner_items = [it for it in flat if not isinstance(it, WordBoundary)]
        if not inner_items:
            raise Unencodable("word-boundary")
        inner = Seq(inner_items) if len(inner_items) != 1 else inner_items[0]
        if _contains_word_bounded(inner) or _contains_word_boundary(inner):
            raise Unencodable("word-boundary")
        return WordBounded(inner, leading=leading, trailing=trailing)
    return node


def _contains_word_boundary(node) -> bool:
    if isinstance(node, WordBoundary):
        return True
    if isinstance(node, WordBounded):
        return True
    if isinstance(node, Folded):
        return _contains_word_boundary(node.item)
    if isinstance(node, Repeat):
        return _contains_word_boundary(node.item)
    if isinstance(node, Alt):
        return any(_contains_word_boundary(it) for it in node.items)
    if isinstance(node, Seq):
        return any(_contains_word_boundary(it) for it in node.items)
    return False


def _contains_word_bounded(node) -> bool:
    if isinstance(node, (WordBounded, WordBoundary)):
        return True
    if isinstance(node, Folded):
        return _contains_word_bounded(node.item)
    if isinstance(node, Repeat):
        return _contains_word_bounded(node.item)
    if isinstance(node, Alt):
        return any(_contains_word_bounded(it) for it in node.items)
    if isinstance(node, Seq):
        return any(_contains_word_bounded(it) for it in node.items)
    return False
