"""Perl dialect compiler goldens (Wave 3 / #113)."""

from __future__ import annotations

from regexproof.compiler import compile_pattern
from regexproof.compiler.perl import compile_perl
from regexproof.compiler.perl_strip import strip_k_reset, strip_perl_transparent


def test_plain_encodable():
    r = compile_perl(r"viagra", call_kind="search")
    assert r.encodable, r.unencodable_reason
    assert r.dialect == "perl"


def test_inline_i_flag():
    r = compile_perl(r"offer", flags="i", call_kind="search")
    assert r.encodable, r.unencodable_reason


def test_posix_alpha_rewritten():
    r = compile_perl(r"[[:alpha:]]+", call_kind="search")
    assert r.encodable, r.unencodable_reason


def test_k_reset_stripped_encodable():
    assert strip_k_reset(r"foo\Kbar") == r"foobar"
    assert strip_k_reset(r"[\K]") == r"[\K]"  # inside class untouched
    assert strip_perl_transparent(r"a++\Kb") == r"a+b"
    r = compile_perl(r"foo\Kbar", call_kind="search")
    assert r.encodable, r.unencodable_reason


def test_reject_code_embed():
    r = compile_perl(r"(?{1})", call_kind="search")
    assert not r.encodable
    assert r.unencodable_reason == "code-embed"


def test_reject_g_brace():
    r = compile_perl(r"\g{1}", call_kind="search")
    assert not r.encodable
    assert r.unencodable_reason == "backref"


def test_dispatch_via_compile_pattern():
    r = compile_pattern(r"abc", "", "perl", "search")
    assert r.encodable, r.unencodable_reason
    assert r.dialect == "perl"


def test_trailing_alt_dollar_via_dispatch():
    r = compile_pattern(r"(?:spam|$)", "", "perl", "search")
    assert r.encodable, r.unencodable_reason
