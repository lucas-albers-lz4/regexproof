"""P2a tests: shell extractor + make_record extra_fields + schema enum."""

from __future__ import annotations

import json

import jsonschema
import pytest

from regexproof.compiler.base import Unencodable
from regexproof.compiler.posix_shell import normalize_shell
from regexproof.extractors import shell_posix as sp
from regexproof.extractors.record import make_record
from regexproof.schemas import extractor_schema

REPO = "t"
FILE = "x.sh"


def extract(src: str) -> list[dict]:
    return sp.extract_shell_posix(src, repo=REPO, file=FILE, dialect="posix-shell")


def patterns(src: str) -> list[str]:
    return [r["pattern"] for r in extract(src)]


# --- 4-way semantic fixture at the EXTRACTOR level --------------------------

def test_four_way_syntax_selector():
    src = (
        "grep 'a+b' f\n"          # BRE bare + = literal
        "grep 'a\\+b' f\n"      # BRE backslash-meta + = one-or-more
        "grep -E 'a+b' f\n"       # ERE one-or-more
        "grep -E 'a\\+b' f\n"   # ERE backslash-meta = literal a+b
    )
    recs = extract(src)
    assert [r["pattern"] for r in recs] == ["a+b", "a\\+b", "a+b", "a\\+b"]
    sf = [r["shell_flags"] for r in recs]
    assert sf[0] == {"syntax": "bre", "grep_mode": "basic"}
    assert sf[1] == {"syntax": "bre", "grep_mode": "basic"}
    assert sf[2] == {"syntax": "ere", "grep_mode": "extended"}
    assert sf[3] == {"syntax": "ere", "grep_mode": "extended"}


def test_sed_bre_syntax():
    recs = extract("sed 's/ab/cd/' f")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "ab"
    assert recs[0]["call_kind"] == "substitution"
    assert recs[0]["shell_flags"] == {"syntax": "bre", "grep_mode": "basic"}


def test_sed_address_is_search():
    """sed /re/ address forms are searches, not substitutions."""
    recs = extract("sed '/listen_https/d' f")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "listen_https"
    assert recs[0]["call_kind"] == "search"


# --- bash/ksh [[ =~ ]] ------------------------------------------------------

def test_bash_ere_unquoted_only():
    assert patterns("[[ $x =~ ^[0-9]+$ ]]") == ["^[0-9]+$"]
    assert patterns('[[ $x =~ "^[0-9]+$" ]]') == []  # quoted = literal match
    assert patterns('[[ "$v" =~ ^[0-9]+$ ]]') == ["^[0-9]+$"]  # quoted LHS ok
    assert patterns('[[ $x =~ foo"bar" ]]') == []  # partial-quoted rejected
    assert patterns("[[ $x =~ ^[Yy]$ ]]") == ["^[Yy]$"]


def test_bash_ksh_provenance():
    rec = extract("[[ $x =~ ^[0-9]+$ ]]")[0]
    assert rec["shell_flags"] == {"syntax": "bash_ksh", "grep_mode": None}
    assert rec["dialect"] == "posix-shell"


# --- literal rejection + flags ----------------------------------------------

def test_fgrep_and_F_literal():
    assert patterns("fgrep 'a.b' f") == []
    assert patterns("grep -F 'a.b' f") == []
    assert patterns("grep 'a.b' f") == ["a.b"]


def test_grep_i_maps_to_flags():
    recs = extract("grep -i 'foo' f")
    assert recs[0]["flags"] == "i"
    assert extract("grep 'foo' f")[0]["flags"] == ""
    # separate flag runs still match (VERBOSE-space regression: no re.VERBOSE)
    assert [r["pattern"] for r in extract("grep -i -q 'foo' f")] == ["foo"]


def test_sed_i_is_not_caseless():
    recs = extract("sed -i 's/ab/cd/' f")  # -i = in-place, NOT caseless
    assert recs[0]["flags"] == ""
    assert recs[0]["shell_flags"]["syntax"] == "bre"


# --- sed forms --------------------------------------------------------------

def test_sed_forms():
    assert patterns("sed 's/foo/bar/' f") == ["foo"]
    assert patterns("sed 's#foo#bar#' f") == ["foo"]
    assert patterns("sed '/listen_https/d' f") == ["listen_https"]
    assert patterns("sed -n '1,20p' f") == []  # numeric address, not a regex


# --- awk forms --------------------------------------------------------------

def test_awk_forms():
    assert patterns("awk '/re/' f") == ["re"]
    assert patterns("awk -F'[, ]' '{print $1}' f") == ["[, ]"]  # glued
    assert patterns("awk -F '[, ]' '{print $1}' f") == ["[, ]"]  # spaced
    assert patterns("awk '{print $1}' f") == []  # program text, not a regex


# --- filters ----------------------------------------------------------------

def test_empty_and_short_patterns_dropped():
    assert patterns("grep '' f") == []
    assert patterns("grep 'a' f") == []  # length-2 filter


def test_var_grep_kept():
    assert patterns("grep '$var' f") == ["$var"]


# --- context guards (precision) --------------------------------------------

def test_context_guards():
    assert patterns("# grep 'foo' f") == []
    assert patterns('echo "use grep \'foo\' here"') == []
    assert patterns("my-grep 'foo' f") == []
    assert patterns("echo ok;# grep 'foo' f") == []
    assert patterns('echo "a\\""; grep \'foo\' f') == ["foo"]
    assert patterns("echo 'x\\'; grep 'foo' f") == ["foo"]  # POSIX single-quote


# --- record contract --------------------------------------------------------

def test_column_is_line_relative():
    recs = extract("grep 'foo' f\ngrep 'bar' f")
    assert [r["column"] for r in recs] == [0, 0]  # both at line start
    recs = extract("x=1; grep 'foo' f")
    assert recs[0]["column"] == 5  # "x=1; " is 5 chars
    assert recs[0]["site"] == f"{FILE}:1:5"


def test_call_kind_search_and_substitution():
    assert extract("grep 'xy' f")[0]["call_kind"] == "search"
    assert extract("sed 's/xy/z/' f")[0]["call_kind"] == "substitution"


def test_make_record_extra_fields_merge():
    rec = make_record(
        repo=REPO, pattern="x", flags="", dialect="posix-shell",
        call_kind="search", file=FILE, line=1, column=0,
        extra_fields={"shell_flags": {"syntax": "bre", "grep_mode": "basic"},
                      "rule_name": "r1"},
    )
    assert rec["shell_flags"] == {"syntax": "bre", "grep_mode": "basic"}
    assert rec["rule_name"] == "r1"


def test_make_record_fixed_fields_win():
    rec = make_record(
        repo=REPO, pattern="real", flags="i", dialect="posix-shell",
        call_kind="search", file=FILE, line=1, column=0,
        extra_fields={"pattern": "spoof", "dialect": "yara",
                      "regex_id": "0" * 32},
    )
    assert rec["pattern"] == "real"          # override dropped
    assert rec["dialect"] == "posix-shell"   # override dropped
    assert rec["regex_id"] != "0" * 32       # computed from real fields
    assert rec["flags"] == "i"


def test_schema_valid_with_posix_shell():
    recs = extract("grep -i 'foo' f\n[[ $x =~ ^[0-9]+$ ]]\nsed 's/ab/cd/' f")
    assert len(recs) == 3
    for r in recs:
        jsonschema.validate(instance=r, schema=extractor_schema())
    # and the schema rejects a dialect OUTSIDE the enum (enum is enforced)
    bad = dict(recs[0])
    bad["dialect"] = "bogus"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad, schema=extractor_schema())


def test_ndjson_round_trip_line_records():
    """The AC3 validator path: per-line json.loads + validate."""
    recs = extract("grep 'a+b' f\ngrep -E 'a+b' f")
    lines = [json.dumps(r) for r in recs]
    for line in lines:
        jsonschema.validate(instance=json.loads(line), schema=extractor_schema())


# --- P3 reconcile finding: command substitution is SHELL CODE ----------------

def test_substitution_double_quoted_grep_extracted():
    """`"$(grep 'pat')"` is a real grep — the guard must not treat the
    double-quoted $( ) body as a string literal (golang-build.sh class)."""
    recs = extract("files=\"$(printf '%s\\n' \"$x\" | grep '\\.\\(c\\|go\\)$')\"")
    assert len(recs) == 1
    assert recs[0]["pattern"] == r"\.\(c\|go\)$"


def test_substitution_unquoted_and_nested():
    recs = extract("x=$(grep -i 'foo' f)")
    assert [r["pattern"] for r in recs] == ["foo"]
    assert recs[0]["shell_flags"]["syntax"] == "bre"
    assert recs[0]["flags"] == "i"
    recs = extract('y="$(echo "$(grep \'bar\' f)")"')
    assert [r["pattern"] for r in recs] == ["bar"]


def test_backtick_substitution_extracted():
    recs = extract('z=`grep "baz" f`')
    assert [r["pattern"] for r in recs] == ["baz"]


def test_substitution_comment_still_suppresses():
    recs = extract('x="$(grep "real" f # comment)"')
    assert [r["pattern"] for r in recs] == ["real"]


def test_string_literal_still_suppressed():
    """The pre-fix behavior stays: `echo "use grep 'x'"` is a string, not a
    site (and the string is not re-opened as substitution)."""
    assert extract('echo "use grep \'x\'"') == []
    # a $( inside single quotes is literal
    assert extract("echo '$(grep \"nope\" f)'") == []


# --- cumulative zen-MCR fold (wave #264 close-out review) --------------------

def test_sed_E_is_extended_syntax():
    """Cumulative finding #1: sed -E/-r switches to ERE — the mirror must
    match the executing engine (GNU sed 4.x + busybox both support -E)."""
    recs = extract("sed -E 's/[0-9]+//' f")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "[0-9]+"
    assert recs[0]["shell_flags"]["syntax"] == "ere"


def test_grep_P_skipped():
    """Cumulative finding #2: grep -P is PCRE-in-shell — the documented
    false negative must actually skip (was recorded as BRE, contradicting
    the docstring)."""
    assert extract("grep -P '[0-9]+' f") == []


def test_ere_class_with_question_paren_not_rejected():
    """Cumulative finding #3: [(?] is a valid ERE char class — the inline-
    flag guard must be class-aware (grep -E '[(?]' matches '(' and '?')."""
    assert normalize_shell("[(?]", "ere") == "[(?]"
    with pytest.raises(Unencodable):
        normalize_shell("(?i)foo", "ere")


def test_sed_escaped_delimiter_search():
    r"""Cumulative finding #4: s/a\/b/c/ must yield the full search regex
    a\/b (the old lazy scan truncated at the escaped delimiter)."""
    recs = extract(r"sed 's/a\/b/c/' f")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "a\\/b"
    assert recs[0]["call_kind"] == "substitution"
    recs = extract("sed 's/\\/usr\\/local/\\/opt/g' f")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "\\/usr\\/local"


def test_sed_unterminated_rejected():
    """luna #276 -r6 #2: sed 's' and sed 's/foo/bar' (missing replacement
    delimiter) are rejected by GNU sed AND busybox — not sites, no crash."""
    assert extract("sed 's' f") == []
    assert extract("sed 's/foo' f") == []
    assert extract("sed 's/foo/bar' f") == []


def test_grep_trailing_flags():
    """luna #276 -r7 #1: flags AFTER the -e pattern still apply —
    grep -e 'a.b' -F is fixed-string (literal, not a regex site) and
    grep -e '(?i)foo' -P is skipped PCRE."""
    assert extract("grep -e 'a.b' -F f") == []
    assert extract("grep -e '(?i)foo' -P f") == []
    # -E trailing still selects ERE
    recs = extract("grep -e 'a.b' -E f")
    assert len(recs) == 1
    assert recs[0]["shell_flags"]["syntax"] == "ere"


def test_mixed_heredoc_openers_sequential():
    """luna #276 -r7 #2: `cat <<A <<'B'` — A is unquoted (LIVE: its
    $(grep) executes) and B is quoted (blanked); B's body starts AFTER
    A's terminator."""
    src = ("cat <<A <<'B'\n"
           "x=\"$(grep 'xy' f)\"\n"
           "A\n"
           "grep 'zzz'\n"
           "B\n")
    recs = extract(src)
    assert [r["pattern"] for r in recs] == ["xy"]


def test_heredoc_body_not_extracted():
    """Cumulative finding #7: QUOTED heredoc bodies are DATA, not shell
    code — cat <<'EOF' prints them literally; a grep inside is not a site."""
    assert extract("cat <<'EOF'\ngrep 'never-executed'\nEOF\n") == []
    # real code after the heredoc still extracts
    recs = extract("cat <<'EOF'\ndata\ngrep 'body'\nEOF\ngrep 'real' f\n")
    assert [r["pattern"] for r in recs] == ["real"]


def test_heredoc_unquoted_body_is_live():
    """luna #276 -r6 #1: an UNQUOTED delimiter (<<EOF) EXPANDS command
    substitutions during heredoc processing — $(grep 'xy') in the body is a
    REAL executed site (verified: bash runs the substitution). Pattern is
    2+ chars (the P1-frozen min-length-2 filter drops single-char args)."""
    recs = extract("cat <<EOF\nprintf '%s\\n' \"$(grep 'xy' f)\"\nEOF\n")
    assert [r["pattern"] for r in recs] == ["xy"]


def test_heredoc_double_quoted_delimiter_and_exact_terminator():
    """luna #276 -r2: `<<\"EOF\"` is a valid opener, and the terminator must
    be EXACTLY the delimiter — ` EOF ` (padded) does NOT terminate."""
    assert extract('cat <<"EOF"\ngrep \'x\'\nEOF\n') == []
    # padded terminator: the body extends (grep stays suppressed)
    assert extract("cat <<'EOF'\ngrep 'x'\n EOF \nEOF\n") == []


def test_heredoc_tab_terminator_with_dash_form():
    assert extract("cat <<-EOF\n\tgrep 'x'\n\tEOF\n") == []


def test_case_in_substitution_documented():
    """Cumulative finding #6 is a DOCUMENTED limitation: case-pattern `)`
    inside $(...) pops the substitution frame early (a full case parser is
    out of scope for the labeled heuristic)."""
    # the case body after `a)` is mis-tracked as string context — the
    # docstring carries the limitation; assert the current (documented)
    # behavior rather than an over-promise.
    assert "case" in (sp._in_comment_or_string.__doc__ or "")


def test_arithmetic_expansion_does_not_pop_substitution_frame():
    """Cumulative Reviewer B #4: $((1+2)) arithmetic is NOT a substitution —
    its `))` must not pop the enclosing $() frame (the grep after it is a
    real site; quoted pattern per the extractor's documented contract)."""
    src = 'x="$(echo $((1+2)); printf real | grep \'real\')"'
    recs = extract(src)
    assert [r["pattern"] for r in recs] == ["real"]
    # standalone arithmetic inside a double-quoted string stays literal
    assert extract('echo "$((1+2))"') == []


def test_multiple_heredocs_per_line_sequential():
    """luna #276 -r3 #4: `cat <<A <<B` — QUOTED bodies are SEQUENTIAL; the
    second body's grep must not leak (bash -n accepts the script)."""
    src = "cat <<'A' <<'B'\nbody-a\ngrep 'leak-a'\nA\nbody-b\ngrep 'leak-b'\nB\n"
    assert extract(src) == []


def test_nested_arithmetic_parens():
    """luna #276 -r3 #6: $((1+(2*3))) — the inner `))` must not close the
    arithmetic frame early; the grep after still extracts."""
    src = 'x=$((1+(2*3))); printf real | grep \'real\''
    recs = extract(src)
    assert [r["pattern"] for r in recs] == ["real"]


def test_subshell_inside_substitution():
    """luna #276 -r6 #4: a balanced subshell `( ... )` inside $() must not
    pop the substitution frame (verified: bash runs it)."""
    src = 'x="$( (echo a); grep \'real\' f)"'
    recs = extract(src)
    assert [r["pattern"] for r in recs] == ["real"]


def test_heredoc_escaped_and_dotted_delimiters():
    """luna #276 -r6 #3: `<<\\EOF` behaves like a QUOTED heredoc (no
    expansion — verified) and `<<'END.SQL'` is a valid dotted delimiter."""
    assert extract("cat <<\\EOF\ngrep 'x'\nEOF\n") == []
    assert extract("cat <<'END.SQL'\ngrep 'x'\nEND.SQL\n") == []
