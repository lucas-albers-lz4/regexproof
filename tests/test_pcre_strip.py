"""Possessive/atomic/lazy strip must not mutate char-class contents."""

from __future__ import annotations

from regexproof.compiler import compile_pattern
from regexproof.compiler.pcre_strip import (
    strip_atomic_and_possessive,
    strip_language_transparent,
    strip_lazy_quantifiers,
)


def test_class_star_plus_preserved():
    assert strip_atomic_and_possessive("[*+]") == "[*+]"
    assert strip_atomic_and_possessive(r"[a*+b]") == r"[a*+b]"


def test_possessive_outside_class_stripped():
    assert strip_atomic_and_possessive("a++") == "a+"
    assert strip_atomic_and_possessive("a*+") == "a*"
    assert strip_atomic_and_possessive("a?+") == "a?"
    assert strip_atomic_and_possessive("a{2,3}+") == "a{2,3}"


def test_literal_brace_plus_not_stripped_as_possessive():
    """fix-wave #70: `a}+` is literal `}` + one-or-more, not `{n,m}+`."""
    assert strip_atomic_and_possessive("a}+") == "a}+"
    assert strip_lazy_quantifiers("a}?") == "a}?"


def test_atomic_group_rewritten():
    assert strip_atomic_and_possessive("(?>ab)c") == "(?:ab)c"


def test_escaped_bracket_not_class():
    # \[ does not open a class; possessive after still strips.
    assert strip_atomic_and_possessive(r"\[a++") == r"\[a+"


def test_lazy_outside_class_stripped():
    assert strip_lazy_quantifiers("a*?") == "a*"
    assert strip_lazy_quantifiers("a+?") == "a+"
    assert strip_lazy_quantifiers("a??") == "a?"
    assert strip_lazy_quantifiers("a{2,3}?") == "a{2,3}"


def test_lazy_inside_class_preserved():
    assert strip_lazy_quantifiers("[?]") == "[?]"
    assert strip_lazy_quantifiers("[a*?]") == "[a*?]"


def test_language_transparent_combined():
    assert strip_language_transparent("a*+") == "a*"
    assert strip_language_transparent("a*?") == "a*"
    assert strip_language_transparent("(?>a)+?") == "(?:a)+"


def test_lazy_patterns_become_encodable_pcre_and_ecma():
    for dialect in ("pcre", "ecma"):
        lazy = compile_pattern("a*?", "", dialect, "fullmatch")
        eager = compile_pattern("a*", "", dialect, "fullmatch")
        assert lazy.encodable, (dialect, lazy.unencodable_reason)
        assert eager.encodable
        braced = compile_pattern("a{2,3}?", "", dialect, "fullmatch")
        assert braced.encodable, (dialect, braced.unencodable_reason)


def test_hex_escapes_encode_as_literals():
    for dialect in ("pcre", "ecma", "re2"):
        nn = compile_pattern(r"\x41", "", dialect, "fullmatch")
        assert nn.encodable, (dialect, nn.unencodable_reason)
        brace = compile_pattern(r"\x{41}", "", dialect, "fullmatch")
        assert brace.encodable, (dialect, brace.unencodable_reason)
        bad = compile_pattern(r"\xGG", "", dialect, "fullmatch")
        assert not bad.encodable
        assert bad.unencodable_reason in ("bad-range", "unsupported-syntax", "parse-error")
