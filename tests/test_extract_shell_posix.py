"""P2a tests: shell extractor + make_record extra_fields + schema enum."""

from __future__ import annotations

import json

import jsonschema
import pytest

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
        "grep -E 'a+b' f\n"       # ERE one-or-more
        "grep -E 'a\\\\+b' f\n"   # ERE backslash-meta = literal a+b
    )
    recs = extract(src)
    assert [r["pattern"] for r in recs] == ["a+b", "a+b", "a\\\\+b"]
    sf = [r["shell_flags"] for r in recs]
    assert sf[0] == {"syntax": "bre", "grep_mode": "basic"}
    assert sf[1] == {"syntax": "ere", "grep_mode": "extended"}
    assert sf[2] == {"syntax": "ere", "grep_mode": "extended"}


def test_sed_bre_syntax():
    recs = extract("sed 's/ab/cd/' f")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "ab"
    assert recs[0]["call_kind"] == "substitution"
    assert recs[0]["shell_flags"] == {"syntax": "bre", "grep_mode": "basic"}


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
