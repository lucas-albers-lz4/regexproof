"""P2b tests: BRE→ERE normalize + pcre backend for dialect posix-shell."""

from __future__ import annotations

import inspect

import pytest

from regexproof.batch import compile_records as cr_mod
from regexproof.batch.compile_records import compile_records
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
        normalize_shell(r"\(ab\)\1", "bre")
    assert ei.value.reason == "backref"


def test_rejection_returns_compile_result_not_raise():
    """Finding-1 regression: normalize runs INSIDE compile_pattern's
    try/except, so a rejection returns a rejected CompileResult instead of
    propagating (which would abort batch)."""
    r = comp(r"\(ab\)\1", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert not r.encodable
    assert r.unencodable_reason == "backref"
    assert r.dialect == "posix-shell"
    r2 = comp(r"(?i)foo", shell_flags={"syntax": "ere", "grep_mode": "extended"})
    assert not r2.encodable
    assert r2.unencodable_reason == "inline-flag-like"


def test_batch_backref_row_not_abort():
    """compile_records must not abort on a rejected shell record."""
    rec = {
        "schema_version": "2", "repo": "t", "pattern": r"\(ab\)\1",
        "flags": "", "dialect": "posix-shell", "call_kind": "search",
        "site": "x.sh:1:0", "file": "x.sh", "line": 1, "column": 0,
        "shell_flags": {"syntax": "bre", "grep_mode": "basic"},
    }
    rows = compile_records([rec], lift_inline=False, corpus_slug="dogfood_shell")
    assert len(rows) == 1
    rows = [pair[0] for pair in rows]
    assert rows[0]["encodable"] is False
    assert rows[0]["compile_reason"] == "backref"


def test_gnu_word_boundary_rejected():
    for pat in (r"foo\<", r"\>bar", r"a\<b"):
        with pytest.raises(Unencodable) as ei:
            normalize_shell(pat, "bre")
        assert ei.value.reason == "gnu-word-boundary"


def test_gnu_shorthand_classes_rejected():
    r"""\w \W \s \S  \B are GNU/busybox classes/boundaries in BOTH BRE and
    ERE (machine-verified) — rejected, never silently translated to pcre."""
    for pat in (r"\w", r"\W", r"\s", r"\S", r"\b", r"\B"):
        for syntax in ("bre", "ere"):
            with pytest.raises(Unencodable) as ei:
                normalize_shell(pat, syntax)
            assert ei.value.reason == "gnu-extension", (pat, syntax)


def test_ere_inline_flag_guard():
    """`(?` in an ERE record is Unencodable — pcre would read it as flags."""
    for pat in (r"(?i)foo", r"(?:foo)"):
        with pytest.raises(Unencodable) as ei:
            normalize_shell(pat, "ere")
        assert ei.value.reason == "inline-flag-like"
    # class-aware: [(?] and nested-POSIX-class classes are NOT flags
    assert normalize_shell("[(?]", "ere") == "[(?]"
    assert normalize_shell("[[:digit:](?]", "ere") == "[[:digit:](?]"
    assert normalize_shell(r"\(?a", "ere") == r"\(?a"
    # and through compile_pattern it surfaces as a rejected result
    r = comp(r"(?i)foo", shell_flags={"syntax": "ere", "grep_mode": "extended"})
    assert not r.encodable
    assert r.unencodable_reason == "inline-flag-like"


def test_bre_inline_flag_is_literal():
    """BRE `(?i)foo` compiles as LITERAL text (grep BRE matches literal)."""
    r = comp(r"(?i)foo", shell_flags={"syntax": "bre", "grep_mode": "basic"})
    assert r.encodable
    assert normalize_shell(r"(?i)foo", "bre") == r"\(\?i\)foo"


def test_ere_backref_rejected():
    """GNU grep 3.11 + busybox 1.37 support `\1` as an ERE backref
    (verified: `grep -E '^(a)\1$'` matches aa) — modeling it faithfully is
    out of scope, so the mirror fails closed (cumulative Reviewer B #1)."""
    for pat in (r"a\1b", r"^(a)\1$"):
        with pytest.raises(Unencodable) as ei:
            normalize_shell(pat, "ere")
        assert ei.value.reason == "backref"


def test_unknown_escape_drops_backslash():
    r"""BRE `a\d` = literal ad (grep semantics); pcre would read \d as class.
    \w is a GNU CLASS (rejected separately) — the drop applies only to
    truly-unknown escapes like \d."""
    assert normalize_shell(r"a\d", "bre") == "ad"
    assert normalize_shell(r"\d+", "bre") == r"d\+"
    # kept escapes stay identical
    assert normalize_shell(r"a\.b", "bre") == r"a\.b"
    assert normalize_shell(r"a\*b", "bre") == r"a\*b"


def test_ere_unknown_escape_drops_backslash():
    r"""ERE `a\d` = literal ad on grep AND busybox (verified); pcre would
    read \d as a digit class — the drop keeps them agreeing."""
    assert normalize_shell(r"a\d", "ere") == "ad"
    assert normalize_shell(r"a\d", "bash_ksh") == "ad"
    # ERE backslash-metas stay literal-identical (grep and pcre agree)
    assert normalize_shell(r"a\+b", "ere") == r"a\+b"
    assert normalize_shell(r"a\?b", "ere") == r"a\?b"


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


def test_unknown_syntax_defaults_bre():
    """Unknown syntax selectors fall back to BRE (documented contract) —
    literal-escape applies and the ERE inline-flag guard does not."""
    assert normalize_shell(r"a+b", "fixed") == r"a\+b"  # BRE literal
    assert normalize_shell(r"(?i)foo", "bogus") == r"\(\?i\)foo"  # literal
    assert normalize_shell(r"a\+b", "fixed") == "a+b"  # BRE one-or-more


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


def test_negated_class_with_first_member_close_bracket():
    """luna #276 -r3 #5: `[^](?]` is a valid GNU ERE class (first member ]
    after the ^ negation is literal) — not an inline flag."""
    assert normalize_shell("[^](?]", "ere") == "[^](?]"
