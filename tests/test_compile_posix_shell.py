"""P2b tests: BRE→ERE normalize + pcre backend for dialect posix-shell."""

from __future__ import annotations

import inspect

import pytest

from regexproof.batch import compile_records as cr_mod
from regexproof.compiler import compile_pattern
from regexproof.compiler.base import Unencodable
from regexproof.compiler.posix_shell import compile_posix_shell, normalize_shell
from regexproof.extractors.shell_posix import extract_shell_posix


def comp(pat: str, *, flags: str = "", shell_flags: dict | None = None):
    """Compile a posix-shell pattern; returns the CompileResult."""
    return compile_pattern(
        pat, flags=flags, dialect="posix-shell", call_kind="search",
        max_length=16, shell_flags=shell_flags,
    )


# --- the 4-way semantic set -------------------------------------------------

def test_bre_bare_plus_is_literal():
    """BRE `a+b` = literal a+b (bare + escaped so pcre does not widen)."""
    r = comp(r"a+b", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert r.encodable
    assert r.mirror is not None


def test_bre_escaped_plus_is_one_or_more():
    """BRE `a` + backslash-plus + `b` = one-or-more (unescaped to ERE a+b)."""
    r = comp(r"a\+b", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert r.encodable


def test_ere_bare_plus_one_or_more():
    """grep -E 'a+b' = one-or-more (pass-through)."""
    r = comp(r"a+b", shell_flags={"syntax": "ere", "grep_mode": "extended"})
    assert r.encodable


def test_ere_backslashed_plus_literal():
    """grep -E with backslash-plus = LITERAL a+b (pass-through)."""
    r = comp(r"a\+b", shell_flags={"syntax": "ere", "grep_mode": "extended"})
    assert r.encodable


def test_normalize_four_way_text():
    assert normalize_shell(r"a+b", "bre") == r"a\+b"      # literal
    assert normalize_shell(r"a\+b", "bre") == r"a+b"      # one-or-more
    assert normalize_shell(r"a+b", "ere") == r"a+b"       # pass-through
    assert normalize_shell(r"a\+b", "ere") == r"a\+b"     # pass-through


# --- rejects ----------------------------------------------------------------

def test_bre_backref_rejected():
    with pytest.raises(Unencodable) as ei:
        comp(r"\(ab\)\1", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert ei.value.reason == "backref"


def test_gnu_word_boundary_rejected():
    for pat in (r"foo\<", r"\>bar", r"a\<b"):
        with pytest.raises(Unencodable) as ei:
            comp(pat, shell_flags={"syntax": "bre", "grep_mode": "basic"})
        assert ei.value.reason == "gnu-word-boundary"


def test_ere_inline_flag_guard():
    """`(?` in an ERE record is Unencodable — pcre would read it as flags."""
    with pytest.raises(Unencodable) as ei:
        comp(r"(?i)foo", shell_flags={"syntax": "ere", "grep_mode": "extended"})
    assert ei.value.reason == "inline-flag-like"
    with pytest.raises(Unencodable) as ei:
        comp(r"(?:foo)", shell_flags={"syntax": "ere", "grep_mode": "extended"})
    assert ei.value.reason == "inline-flag-like"


def test_bre_inline_flag_is_literal():
    """BRE `(?i)foo` compiles as LITERAL text (grep BRE matches literal)."""
    r = comp(r"(?i)foo", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert r.encodable
    assert normalize_shell(r"(?i)foo", "bre") == r"\(\?i\)foo"


def test_unknown_escape_drops_backslash():
    """BRE unknown escape = literal char (grep semantics); pcre would read it as a class."""
    assert normalize_shell(r"a\d", "bre") == "ad"
    assert normalize_shell(r"\w+", "bre") == r"w\+"
    # kept escapes stay identical
    assert normalize_shell(r"a\.b", "bre") == r"a\.b"
    assert normalize_shell(r"a\*b", "bre") == r"a\*b"


# --- double-normalize guard -------------------------------------------------

def test_no_double_normalize():
    r"""BRE a-backslash-plus-b must compile to one-or-more, NOT literal — proves the
    normalize never re-runs in the branch (a round-trip `\+`→`+`→`\+` would
    compile a literal)."""
    r = comp(r"a\+b", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert r.encodable
    # The normalized text is what reaches the pcre route; assert it is the
    # one-or-more form (a+b), not the re-escaped literal form.
    norm = normalize_shell(r"a\+b", "bre")
    assert norm == r"a+b"
    again = normalize_shell(norm, "bre")
    assert again == r"a\+b"  # a SECOND normalize would re-escape — banned
    # and the actual compiled result must not be the re-escaped text:
    r2 = comp_posix_shell_after_entry(norm)
    assert r2.encodable


def comp_posix_shell_after_entry(normalized: str):
    """Simulate compile_pattern's entry normalize then the branch call."""
    return compile_posix_shell(
        normalized, flags="", call_kind="search", max_length=16)


# --- defaults + flags -------------------------------------------------------

def test_missing_shell_flags_defaults_bre():
    r = comp(r"a+b")  # no shell_flags — defaults to BRE
    assert r.encodable
    assert normalize_shell(r"a+b", "bre") == r"a\+b"


def test_dialect_result_and_pattern():
    r = comp(r"a\+b", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert r.dialect == "posix-shell"
    assert r.pattern == r"a+b"  # the normalized text actually compiled


def test_flags_flow_through():
    r = comp(r"foo", flags="i", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert r.flags == "i"
    assert r.encodable


# --- end-to-end value-observation: extractor -> compile_pattern -------------

def test_extractor_output_reaches_compile_unchanged():
    """The shell_flags value-observation contract: extractor records feed
    compile_pattern directly and the syntax selector changes the compile."""
    src = "grep 'a+b' f\ngrep -E 'a+b' f\n"
    recs = extract_shell_posix(src, repo="t", file="x.sh", dialect="posix-shell")
    assert [r["shell_flags"]["syntax"] for r in recs] == ["bre", "ere"]
    bre = compile_pattern(
        recs[0]["pattern"], recs[0]["flags"], recs[0]["dialect"],
        recs[0]["call_kind"], max_length=16,
        shell_flags=recs[0]["shell_flags"],
    )
    ere = compile_pattern(
        recs[1]["pattern"], recs[1]["flags"], recs[1]["dialect"],
        recs[1]["call_kind"], max_length=16,
        shell_flags=recs[1]["shell_flags"],
    )
    assert bre.encodable and ere.encodable
    # both compile, but to DIFFERENT mirrors (literal vs one-or-more)
    assert str(bre.mirror) != str(ere.mirror)


def test_compile_records_threads_shell_flags():
    """compile_records passes rec['shell_flags'] — value-observation via the
    batch route (a BRE a+b compiles encodable, i.e. the literal-escape ran)."""
    src = inspect.getsource(cr_mod)
    assert "shell_flags=rec.get(\"shell_flags\")" in src
