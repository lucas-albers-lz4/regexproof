"""Possessive/atomic strip must not mutate char-class contents."""

from __future__ import annotations

from regexproof.compiler.pcre_strip import strip_atomic_and_possessive


def test_class_star_plus_preserved():
    assert strip_atomic_and_possessive("[*+]") == "[*+]"
    assert strip_atomic_and_possessive(r"[a*+b]") == r"[a*+b]"


def test_possessive_outside_class_stripped():
    assert strip_atomic_and_possessive("a++") == "a+"
    assert strip_atomic_and_possessive("a*+") == "a*"
    assert strip_atomic_and_possessive("a?+") == "a?"
    assert strip_atomic_and_possessive("a{2,3}+") == "a{2,3}"


def test_atomic_group_rewritten():
    assert strip_atomic_and_possessive("(?>ab)c") == "(?:ab)c"


def test_escaped_bracket_not_class():
    # \[ does not open a class; possessive after still strips.
    assert strip_atomic_and_possessive(r"\[a++") == r"\[a+"
