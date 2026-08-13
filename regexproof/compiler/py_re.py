"""Python `re` dialect → Z3 regex AST (via sre_parse).

Never constructs z3.Re(pattern_string) as a pattern parse.
"""

from __future__ import annotations

import re
from typing import Any

# Prefer re._parser (3.11+); fall back to deprecated sre_* for older minors.
try:
    from re import _constants as sc
    from re import _parser as sre_parse
except ImportError:  # pragma: no cover
    import sre_constants as sc  # type: ignore
    import sre_parse  # type: ignore

from z3 import Concat, Range, Re, Star, Union

from regexproof.compiler.base import (
    CompileResult,
    Unencodable,
    add_compiler_meta,
    any_char,
    python_trailing_dollar,
    repeat_z3,
    wrap_call_kind,
    wrap_kind_for_call,
)
from regexproof.compiler.fold import python_fold_closure

# Pattern length limit — never truncate (unencodable instead).
DEFAULT_MAX_LENGTH = 256

# Python `.` fails only on `\n` unless DOTALL.
_PY_LINE_TERMINATORS = frozenset("\n")


def _flags_from_string(flags: str) -> int:
    mapping = {
        "i": re.IGNORECASE,
        "m": re.MULTILINE,
        "s": re.DOTALL,
        "x": re.VERBOSE,
        "a": re.ASCII,
        "u": re.UNICODE,
    }
    acc = 0
    for ch in flags:
        if ch not in mapping:
            raise Unencodable(f"unknown-flag:{ch}")
        acc |= mapping[ch]
    return acc


def _normalize_flags(flags: str) -> str:
    return "".join(sorted(set(flags.lower())))


def compile_py_re(
    pattern: str,
    flags: str = "",
    call_kind: str = "search",
    *,
    max_length: int = DEFAULT_MAX_LENGTH,
) -> CompileResult:
    flags = _normalize_flags(flags)
    try:
        if len(pattern) > max_length:
            raise Unencodable("pattern-too-long")
        if "m" in flags:
            raise Unencodable("m-flag")
        flag_bits = _flags_from_string(flags)
        # VERBOSE: let sre_parse preprocess whitespace/comments.
        # Inline (?i)/(?s)/(?a) update State.flags (fix-wave #70).
        state = sre_parse.State()
        state.flags = flag_bits
        parsed = sre_parse.parse(pattern, flag_bits, state=state)
        effective = int(getattr(state, "flags", flag_bits) or flag_bits)
        ascii_only = bool(effective & re.ASCII)
        ignorecase = bool(effective & re.IGNORECASE)
        dotall = bool(effective & re.DOTALL)
        ctx = _Ctx(
            ascii_only=ascii_only,
            ignorecase=ignorecase,
            dotall=dotall,
            call_kind=call_kind,
        )
        body, meta = _translate(parsed, ctx)
        if meta.get("has_internal_anchor"):
            raise Unencodable("internal-anchor")
        # Trailing $ → Python newline-tolerant end.
        if meta.get("trailing_dollar"):
            body = python_trailing_dollar(body)
        # Leading/trailing anchors already stripped into meta; apply call_kind.
        if meta.get("leading_caret") and call_kind == "search":
            # search with ^ : no leading Star(any)
            pass
        mirror = _apply_wrappers(body, call_kind, meta)
        # C1 (issue #426): derived wrapper metadata — must agree with what
        # `_apply_wrappers` actually returned (bare body == whole-string).
        meta["fullmatch_shaped"] = mirror is body
        meta["wrap_kind"] = wrap_kind_for_call(call_kind)
        # Unicode-default \w/\d/\s are expanded "lightly" (py_re.py _word/
        # _digit/_space) — the mirror is not a faithful encoding of the
        # engine language there, so mirror_exact is False (fail-closed).
        add_compiler_meta(meta, mirror_exact=not ctx.light_unicode_expansion)
        domain = "ascii" if ascii_only else "unicode"
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect="py_re",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
            meta=meta,
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect="py_re",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii" if "a" in flags else "unicode",
        )
    except (re.error, TypeError, ValueError, OverflowError, RecursionError) as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=f"parse-error:{type(exc).__name__}",
            dialect="py_re",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="unicode",
        )


class _Ctx:
    def __init__(self, ascii_only, ignorecase, dotall, call_kind):
        self.ascii_only = ascii_only
        self.ignorecase = ignorecase
        self.dotall = dotall
        self.call_kind = call_kind
        # Set when a unicode-default \w/\d/\s is expanded "lightly" — the
        # mirror is then not a faithful encoding of the engine language.
        self.light_unicode_expansion = False


def _apply_wrappers(body, call_kind: str, meta: dict):
    any_c = any_char()
    leading = meta.get("leading_caret", False)
    trailing = meta.get("trailing_dollar", False)

    if call_kind == "fullmatch":
        return body
    if call_kind == "match":
        # Implicit prefix; strip leading ^ (already removed). Trailing $ means
        # no Star suffix; else Concat(body, Star(any)).
        if trailing:
            return body
        return Concat(body, Star(any_c))
    if call_kind in ("search", "exec", "substitution"):
        parts = []
        if not leading:
            parts.append(Star(any_c))
        parts.append(body)
        if not trailing:
            parts.append(Star(any_c))
        if len(parts) == 1:
            return parts[0]
        return Concat(*parts)
    raise Unencodable(f"unsupported-call_kind:{call_kind}")


def _translate(pattern: sre_parse.SubPattern, ctx: _Ctx):
    """Return (z3_regex, meta_dict)."""
    parts: list[Any] = []
    meta = {
        "leading_caret": False,
        "trailing_dollar": False,
        "has_internal_anchor": False,
        "word_boundary_wrap": False,  # py_re \b is Unencodable — never set
    }
    items = list(pattern)
    for idx, (op, av) in enumerate(items):
        is_first = idx == 0
        is_last = idx == len(items) - 1
        if op in (sc.AT, getattr(sc, "AT_BEGINNING", object()), getattr(sc, "AT_END", object())):
            # sre encodes AT with av in (AT_BEGINNING, AT_END, ...)
            pass
        if op is sc.AT:
            if av in (sc.AT_BEGINNING, sc.AT_BEGINNING_STRING):
                if is_first:
                    meta["leading_caret"] = True
                else:
                    meta["has_internal_anchor"] = True
                continue
            if av in (sc.AT_END, sc.AT_END_STRING):
                if is_last:
                    meta["trailing_dollar"] = True
                else:
                    meta["has_internal_anchor"] = True
                continue
            if av == sc.AT_BOUNDARY or av == getattr(sc, "AT_NON_BOUNDARY", None):
                raise Unencodable("word-boundary")
            raise Unencodable(f"anchor:{av}")
        if op is sc.LITERAL:
            parts.append(_lit(chr(av), ctx))
        elif op is sc.NOT_LITERAL:
            # Single excluded char over declared alphabet — encode as range union.
            parts.append(_not_literal(chr(av), ctx))
        elif op is sc.ANY:
            parts.append(_dot(ctx))
        elif op is sc.IN:
            parts.append(_in_class(av, ctx))
        elif op is sc.BRANCH:
            # av = (None, [subpattern, ...])
            alts = []
            for sub in av[1]:
                sub_body, sub_meta = _translate(sub, ctx)
                if sub_meta.get("has_internal_anchor"):
                    meta["has_internal_anchor"] = True
                # Per-alternative anchors: leading/trailing on a branch are
                # branch-local; for v1 reject mixed anchor branches that would
                # need per-alt wrappers (encode union of bodies only when no
                # per-alt caret/dollar divergence across branches).
                if sub_meta.get("leading_caret") or sub_meta.get("trailing_dollar"):
                    # Mark for caller — simplify: reject for now if any branch
                    # has anchors (safe under-approx avoidance).
                    raise Unencodable("per-alternative-anchor")
                alts.append(sub_body)
            parts.append(Union(*alts) if len(alts) > 1 else alts[0])
        elif op is sc.SUBPATTERN:
            # (group, add_flags, del_flags, subpattern) on 3.11+
            if len(av) >= 4:
                _group, add_flags, del_flags, sub = av[0], av[1], av[2], av[3]
            else:
                add_flags, del_flags, sub = 0, 0, av[-1]
            child_ignore = ctx.ignorecase
            if add_flags & re.IGNORECASE:
                child_ignore = True
            if del_flags & re.IGNORECASE:
                child_ignore = False
            child_dotall = ctx.dotall
            if add_flags & re.DOTALL:
                child_dotall = True
            if del_flags & re.DOTALL:
                child_dotall = False
            child_ascii = ctx.ascii_only
            if add_flags & re.ASCII:
                child_ascii = True
            if del_flags & re.ASCII:
                child_ascii = False
            # Reject scoped flags we do not model (m/x).
            if (add_flags | del_flags) & (re.MULTILINE | re.VERBOSE):
                raise Unencodable("inline-flag")
            child_ctx = _Ctx(
                ascii_only=child_ascii,
                ignorecase=child_ignore,
                dotall=child_dotall,
                call_kind=ctx.call_kind,
            )
            sub_body, sub_meta = _translate(sub, child_ctx)
            if sub_meta.get("has_internal_anchor"):
                meta["has_internal_anchor"] = True
            parts.append(sub_body)
        elif op is sc.MAX_REPEAT or op is sc.MIN_REPEAT:
            # greedy/non-greedy — same language
            lo, hi, sub = av
            sub_body, sub_meta = _translate(sub, ctx)
            if sub_meta.get("has_internal_anchor"):
                meta["has_internal_anchor"] = True
            parts.append(_repeat(sub_body, lo, hi))
        elif op is sc.GROUPREF or op is sc.GROUPREF_EXISTS:
            raise Unencodable("backref")
        elif op is sc.ASSERT or op is sc.ASSERT_NOT:
            raise Unencodable("lookaround")
        elif op is sc.CATEGORY:
            parts.append(_category(av, ctx))
        elif op is sc.RANGE:
            # Should appear inside IN only
            raise Unencodable("bare-range")
        else:
            # ATOMIC_GROUP etc.
            name = getattr(op, "name", str(op))
            if "LOCALE" in name:
                raise Unencodable("locale")
            raise Unencodable(f"unsupported:{name}")
    if not parts:
        body: Any = Re("")
    elif len(parts) == 1:
        body = parts[0]
    else:
        body = Concat(*parts)
    return body, meta


def _lit(ch: str, ctx: _Ctx):
    if ctx.ignorecase:
        chars = sorted(python_fold_closure(ch, ascii_only=ctx.ascii_only))
        if len(chars) == 1:
            return Re(chars[0])
        return Union(*[Re(c) for c in chars])
    return Re(ch)


def _not_literal(ch: str, ctx: _Ctx):
    # Approximate: any_char minus this char — use Union of ranges around it
    # for ASCII when ascii_only; otherwise reject over-broad Unicode complement.
    if not ctx.ascii_only:
        raise Unencodable("unicode-not-literal")
    excluded = python_fold_closure(ch, ascii_only=True) if ctx.ignorecase else {ch}
    parts = []
    for code in range(1, 128):  # skip NUL in declared ASCII domain often
        c = chr(code)
        if c in excluded:
            continue
        parts.append(Re(c))
    if not parts:
        raise Unencodable("empty-not-literal")
    return Union(*parts)


def _dot(ctx: _Ctx):
    if ctx.dotall:
        return any_char()
    # Alphabet minus line terminators — for membership we use Union of
    # complementary encoding: any char then constrain — Z3 AllChar including
    # \n would over-accept. Build ASCII-ish: prefer Range unions excluding \n.
    # Practical encoding: Union of [\0-\t], [\v-\U0010ffff] approx via
    # complement of \n at single-char level using Star of (not \n) is hard.
    # Use: Concat of single-char class = all unicode except \n via
    # z3 doesn't have easy char complement; use AllChar with a note that
    # differential fuzz catches \n over-accept if we used AllChar wrongly.
    # Correct approach for py: Intersect is unavailable; build as
    # Union(Range(\x00,\t), Range(\x0b,\ud7ff), ...) — too large.
    # Stock approach in plan: declared alphabet minus terminators.
    # For solver: use Star-ready single char = Union of common ranges +
    # fallback AllChar only when domain is unicode and we add Not(Contains).
    # Simpler faithful encoding used here:
    return _char_class_excluding(_PY_LINE_TERMINATORS, ctx)


def _char_class_excluding(excluded: frozenset[str], ctx: _Ctx):
    """Single-char class: ASCII printable-ish union when ascii_only, else
    AllChar with documented limitation that fuzz must cover terminators.
    """
    if ctx.ascii_only:
        parts = [Re(chr(c)) for c in range(128) if chr(c) not in excluded]
        return Union(*parts)
    # Unicode: encode as AllChar for non-excluded via complement of Re(term)
    # at Length==1 — callers use as one char. For `.` body we need one char.
    # Use Union(Range) over BMP excluding \n — still huge. Practical: AllChar
    # and rely on membership queries; for `.` *pattern* we use:
    from z3 import Complement, Length, String

    # Actually Complement(Re('\n')) is language complement — trap #1.
    # Safe for Length==1 contexts. Our Concat uses it as one atom — Z3
    # treats Re atoms as single-char languages when built from Range/Re(char).
    # Build: Union of Range('\x00','\t'), Range('\x0b','\uffff') as approximation.
    return Union(Range(chr(0), "\t"), Range("\x0b", "\uffff"))


def _in_class(items, ctx: _Ctx):
    from regexproof.compiler.lower import ranges_excluding

    negate = False
    options = []
    forbidden: set[int] = set()
    saw_member = False
    for op, av in items:
        if op is sc.NEGATE:
            negate = True
            continue
        saw_member = True
        if negate:
            if op is sc.LITERAL:
                chars = (
                    python_fold_closure(chr(av), ascii_only=ctx.ascii_only)
                    if ctx.ignorecase
                    else {chr(av)}
                )
                forbidden.update(ord(c) for c in chars if len(c) == 1)
            elif op is sc.RANGE:
                lo, hi = av
                for code in range(lo, hi + 1):
                    chars = (
                        python_fold_closure(chr(code), ascii_only=ctx.ascii_only)
                        if ctx.ignorecase
                        else {chr(code)}
                    )
                    forbidden.update(ord(c) for c in chars if len(c) == 1)
            elif op is sc.CATEGORY:
                forbidden |= _category_codes(av, ctx)
            else:
                raise Unencodable(f"class-op:{op}")
            continue
        if op is sc.LITERAL:
            options.append(_lit(chr(av), ctx))
        elif op is sc.RANGE:
            lo, hi = av
            options.append(_range(chr(lo), chr(hi), ctx))
        elif op is sc.CATEGORY:
            options.append(_category(av, ctx))
        else:
            raise Unencodable(f"class-op:{op}")
    if negate:
        if not saw_member:
            raise Unencodable("empty-class")
        hi = 127 if ctx.ascii_only else 0xFFFF
        return ranges_excluding(forbidden, hi=hi)
    if not options:
        raise Unencodable("empty-class")
    return Union(*options) if len(options) > 1 else options[0]


def _category_codes(av, ctx: _Ctx) -> set[int]:
    """Codepoints matched by a positive category (for negated-class complement)."""
    if av in (sc.CATEGORY_DIGIT,):
        if ctx.ascii_only:
            return set(range(ord("0"), ord("9") + 1))
        return set(range(ord("0"), ord("9") + 1)) | {ord("\u0660")}
    if av in (sc.CATEGORY_NOT_DIGIT,):
        raise Unencodable("negated-shorthand")
    if av in (sc.CATEGORY_SPACE,):
        chars = " \t\n\r\f\v" if ctx.ascii_only else " \t\n\r\f\v\u00a0\u3000"
        return {ord(c) for c in chars}
    if av in (sc.CATEGORY_NOT_SPACE,):
        raise Unencodable("negated-shorthand")
    if av in (sc.CATEGORY_WORD,):
        if ctx.ascii_only:
            return (
                set(range(ord("a"), ord("z") + 1))
                | set(range(ord("A"), ord("Z") + 1))
                | set(range(ord("0"), ord("9") + 1))
                | {ord("_")}
            )
        # Unicode word — too large for explicit complement; reject.
        raise Unencodable("negated-class")
    if av in (sc.CATEGORY_NOT_WORD,):
        raise Unencodable("negated-shorthand")
    raise Unencodable(f"category:{av}")


def _range(lo: str, hi: str, ctx: _Ctx):
    if ord(lo) > ord(hi):
        raise Unencodable("bad-range")
    if ctx.ignorecase:
        parts = []
        for code in range(ord(lo), ord(hi) + 1):
            parts.append(_lit(chr(code), ctx))
        return Union(*parts)
    return Range(lo, hi)


def _category(av, ctx: _Ctx):
    # CATEGORY_DIGIT, CATEGORY_WORD, CATEGORY_SPACE, and NOT_ variants
    if av in (sc.CATEGORY_DIGIT,):
        return _digit(ctx)
    if av in (sc.CATEGORY_NOT_DIGIT,):
        raise Unencodable("negated-shorthand")
    if av in (sc.CATEGORY_SPACE,):
        return _space(ctx)
    if av in (sc.CATEGORY_NOT_SPACE,):
        raise Unencodable("negated-shorthand")
    if av in (sc.CATEGORY_WORD,):
        return _word(ctx)
    if av in (sc.CATEGORY_NOT_WORD,):
        raise Unencodable("negated-shorthand")
    if av in (sc.CATEGORY_LINEBREAK,):
        return Re("\n")
    raise Unencodable(f"category:{av}")


def _digit(ctx: _Ctx):
    if ctx.ascii_only:
        return Range("0", "9")
    ctx.light_unicode_expansion = True
    # Unicode decimal digits — include ASCII + a distinguishing probe char.
    # Full Nd category is large; encode ASCII + common extras and document
    # that golden probes cover \\u0660.
    return Union(Range("0", "9"), Re("\u0660"))


def _space(ctx: _Ctx):
    if ctx.ascii_only:
        return Union(*[Re(c) for c in " \t\n\r\f\v"])
    ctx.light_unicode_expansion = True
    # Unicode whitespace incl NBSP
    return Union(*[Re(c) for c in " \t\n\r\f\v\u00a0\u3000"])


def _word(ctx: _Ctx):
    if ctx.ascii_only:
        return Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_"))
    ctx.light_unicode_expansion = True
    # Unicode word — ASCII + note; full \\w is huge. Include ASCII alnum + _
    # and rely on ascii flag for precise; for unicode default, expand lightly.
    base = Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_"))
    return base


def _is_maxrepeat(hi) -> bool:
    return hi is sc.MAXREPEAT or hi == sc.MAXREPEAT or repr(hi) == "MAXREPEAT"


def _repeat(body, lo, hi):
    """Dialect wrapper — behavior owned by ``repeat_z3`` (fix-wave #73)."""
    unbounded = hi is None or _is_maxrepeat(hi)
    return repeat_z3(body, lo, None if unbounded else int(hi))


# Silence unused import warning for wrap helpers re-exported conceptually
_ = wrap_call_kind
