"""C1 metadata contract (issue #426): CompileResult.mirror + lowering shape.

The accessors mirror ``lower()``'s ``_meta`` keys on every successful compile
path — including the ``caret_in_x`` / ``trailing_alt_dollar`` fast paths that
bypass ``_meta`` — and ``compile_records`` streams ``(row, mirror, meta)``
triples with lean NDJSON rows (no AST in rows).
"""

from __future__ import annotations

import z3

from regexproof.batch.compile_records import compile_records
from regexproof.batch.runner import _discard_streamed_mirrors
from regexproof.compiler import compile_pattern


def test_anchors_surface_in_meta_fullmatch():
    cr = compile_pattern("^abc$", "", "py_re", "fullmatch")
    assert cr.encodable
    assert cr.leading_caret is True
    assert cr.trailing_dollar is True
    assert cr.has_internal_anchor is False
    assert cr.word_boundary_wrap is False
    # bare lowered body == whole-string language
    assert cr.fullmatch_shaped is True
    assert cr.wrap_kind == "fullmatch"


def test_search_wraps_so_not_fullmatch_shaped():
    cr = compile_pattern("abc", "", "py_re", "search")
    assert cr.encodable
    assert cr.leading_caret is False
    assert cr.trailing_dollar is False
    assert cr.fullmatch_shaped is False
    assert cr.wrap_kind == "search"


def test_leading_caret_search():
    cr = compile_pattern("^abc", "", "py_re", "search")
    assert cr.encodable
    assert cr.leading_caret is True
    assert cr.trailing_dollar is False
    assert cr.wrap_kind == "search"


def test_trailing_dollar_match():
    cr = compile_pattern("abc$", "", "py_re", "match")
    assert cr.encodable
    assert cr.trailing_dollar is True
    assert cr.wrap_kind == "match"


def test_absent_metadata_is_none_not_false():
    cr = compile_pattern(r"\bword\b", "", "py_re", "search")
    assert not cr.encodable
    assert cr.meta is None
    # fail-closed: absent metadata reads None, never a confident False
    assert cr.leading_caret is None
    assert cr.trailing_dollar is None
    assert cr.fullmatch_shaped is None
    assert cr.wrap_kind is None
    assert cr.word_boundary_wrap is None
    assert cr.alphabet_certified is None
    assert cr.mirror_exact is None


def test_word_boundary_wrap_flagged_re2():
    cr = compile_pattern(r"\bword\b", "", "re2", "search")
    assert cr.encodable
    assert cr.word_boundary_wrap is True
    assert cr.fullmatch_shaped is False
    assert cr.wrap_kind == "search"
    assert cr.mirror_exact is True


def test_word_boundary_absent_for_plain_pattern():
    cr = compile_pattern("foo", "", "re2", "search")
    assert cr.encodable
    assert cr.word_boundary_wrap is False
    assert cr.wrap_kind == "search"


def test_mirror_exact_ascii_domain_templates():
    for dialect in ("re2", "ecma", "pcre", "perl"):
        cr = compile_pattern(r"\w+", "", dialect, "search")
        assert cr.encodable, (dialect, cr.unencodable_reason)
        assert cr.declared_domain == "ascii"
        assert cr.mirror_exact is True, dialect


def test_py_re_ascii_flag_mirror_exact():
    cr = compile_pattern(r"\w+", "a", "py_re", "search")
    assert cr.encodable
    assert cr.declared_domain == "ascii"
    assert cr.mirror_exact is True


def test_py_re_unicode_default_shorthands_not_exact():
    # Unicode-default \w/\d/\s are "expanded lightly" — the mirror is not a
    # faithful encoding, so mirror_exact must be False (fail-closed for P3).
    for pat in (r"\w+", r"\d+", r"\s+", r"\w"):
        cr = compile_pattern(pat, "", "py_re", "search")
        assert cr.encodable, (pat, cr.unencodable_reason)
        assert cr.declared_domain == "unicode"
        assert cr.mirror_exact is False, pat


def test_py_re_ascii_classes_still_exact():
    cr = compile_pattern(r"[A-Z0-9]{20}", "", "py_re", "fullmatch")
    assert cr.encodable
    assert cr.mirror_exact is True


def test_caret_in_x_synthesizes_contract():
    cr = compile_pattern("^0+(?:&|$)", "", "pcre", "search")
    assert cr.encodable
    assert cr.leading_caret is True
    # Source-derived (C1 fold, luna re-gate 3): the `^(?:X|$)` shape carries
    # the trailing $ alternative by construction.
    assert cr.trailing_dollar is True
    assert cr.has_internal_anchor is False
    assert cr.word_boundary_wrap is False
    # Union composite — never the bare body.
    assert cr.fullmatch_shaped is False
    assert cr.wrap_kind == "search"


def test_caret_in_x_fullmatch_trailing_dollar():
    cr = compile_pattern("^ab(?:cd|$)", "", "pcre", "fullmatch")
    assert cr.encodable
    assert cr.leading_caret is True
    assert cr.trailing_dollar is True
    assert cr.wrap_kind == "fullmatch"
    assert cr.fullmatch_shaped is False


def test_caret_in_x_empty_x_branch():
    cr = compile_pattern("^(?:;|$)", "", "pcre", "search")
    assert cr.encodable
    assert cr.leading_caret is True
    # Source-derived (C1 fold, luna re-gate 3): the `^(?:X|$)` shape carries
    # the trailing $ alternative.
    assert cr.trailing_dollar is True


def test_trailing_alt_dollar_synthesizes_contract():
    cr = compile_pattern("foo(?:bar|$)", "", "re2", "search")
    assert cr.encodable
    assert cr.leading_caret is False
    # Source-derived (C1 fold, luna re-gate 3): the `(?:X|$)` shape carries
    # the trailing $ alternative.
    assert cr.trailing_dollar is True
    assert cr.has_internal_anchor is False
    assert cr.fullmatch_shaped is False
    assert cr.wrap_kind == "search"


def test_trailing_alt_dollar_wb_wrap():
    cr = compile_pattern(r"\b(TOK[A-Z0-9]{8})(?:[\x60'\"\s;]|$)", "", "re2", "search")
    assert cr.encodable, cr.unencodable_reason
    assert cr.word_boundary_wrap is True
    assert cr.wrap_kind == "search"


def _valid(rec):
    return {
        "regex_id": "meta-test-0001",
        "pattern": rec["pattern"],
        "flags": rec.get("flags") or "",
        "dialect": rec["dialect"],
        "call_kind": rec["call_kind"],
        "site": "meta.test:1:0",
        "repo": "meta-test",
    }


def test_compile_records_streams_pairs_with_lean_rows():
    rec = _valid({"pattern": "^abc$", "dialect": "re2", "call_kind": "fullmatch"})
    stream = compile_records([rec], lift_inline=False, corpus_slug="meta-test")
    assert len(stream) == 1
    row, mirror, meta = stream[0]
    assert row["encodable"] is True
    # NDJSON rows stay lean — no AST/metadata serialized into the row.
    assert "mirror" not in row
    assert "meta" not in row
    assert isinstance(mirror, z3.ReRef)
    assert meta["leading_caret"] is True
    assert meta["trailing_dollar"] is True
    assert meta["mirror_exact"] is True


def test_compile_records_failed_row_pairs_none():
    rec = _valid({"pattern": r"\bword\b", "dialect": "py_re", "call_kind": "search"})
    stream = compile_records([rec], lift_inline=False, corpus_slug="meta-test")
    row, mirror, meta = stream[0]
    assert row["encodable"] is False
    assert mirror is None
    assert meta is None


def test_discard_streamed_mirrors_runs():
    rec = _valid({"pattern": "^abc$", "dialect": "re2", "call_kind": "fullmatch"})
    stream = compile_records([rec], lift_inline=False, corpus_slug="meta-test")
    assert len(stream) >= 1
    _discard_streamed_mirrors(stream)
    # C1 fold (luna re-gate 4): the discard must actually release the
    # triples — a no-op discard fails this assertion.
    assert stream == []


def test_py_re_nested_scoped_shorthand_not_exact():
    # C1 fold (luna re-gate): a Unicode-default shorthand inside a scoped-flag
    # group or a plain group sets the CHILD context's expansion flag; the root
    # mirror_exact check must see it (propagated upward), or (?i:\w) / (\d)
    # wrongly report mirror_exact=True.
    for pat in (r"(?i:\w)", r"(\d)", r"(\w+)", r"x(\d)+y"):
        cr = compile_pattern(pat, "", "py_re", "search")
        assert cr.encodable, (pat, cr.unencodable_reason)
        assert cr.mirror_exact is False, pat


def test_alphabet_certified_stays_unset_on_success():
    # C1 contract: alphabet_certified is set by P3's certification only —
    # a successful compile must leave it unset (fail-closed default).
    cr = compile_pattern(r"^[A-Z0-9]+$", "", "py_re", "fullmatch")
    assert cr.encodable
    assert cr.alphabet_certified is None


def test_mirror_discard_path_releases_stream():
    # The interim discard path must consume the triple stream without
    # affecting row content (rows stay lean, output byte-identical).
    from regexproof.batch.compile_records import compile_records
    recs = [
        {"repo": "a/b", "file": "f.js", "line": 1, "pattern": r"^[a-z]+$",
         "flags": "", "dialect": "py_re", "call_kind": "fullmatch",
         "site": "pkg/f.js", "id": "x1"},
    ]
    rows = compile_records(recs, lift_inline=False, corpus_slug="validatorjs")
    for row, mirror, meta in rows:
        assert isinstance(row, dict)
        assert "mirror" not in row  # lean rows — no AST in records
        if mirror is not None:
            assert meta is not None
    # C1 fold (luna re-gate 4): the discard clears the list (no-op guard).
    _discard_streamed_mirrors(rows)
    assert rows == []


def test_fast_path_propagates_word_boundary_wrap():
    # C1 fold (luna re-gate 2): caret_in_x / trailing_alt_dollar composites
    # must propagate a \b-containing subcompile's word_boundary_wrap instead
    # of hardcoding False (the child mirror is already search-shaped).
    # caret_in_x: ^(?:\bfoo|$) under search; trailing_alt_dollar empty_x+r_alt:
    # (?:\bfoo|$) under fullmatch (under search the union with the empty
    # alternative is the universal language — no boundary constraint).
    cases = [
        (r"^(?:\bfoo|$)", "search"),
        (r"(?:\bfoo|$)", "fullmatch"),
    ]
    for pat, call_kind in cases:
        cr = compile_pattern(pat, "", "pcre", call_kind)
        assert cr.encodable, (pat, cr.unencodable_reason)
        assert cr.word_boundary_wrap is True, (pat, cr.word_boundary_wrap)
        assert cr.fullmatch_shaped is False, pat


def test_fast_path_plain_alt_no_wrap():
    # No \b in the subcompiles -> word_boundary_wrap stays False.
    cr = compile_pattern(r"^(?:foo|$)", "", "pcre", "search")
    assert cr.encodable
    assert cr.word_boundary_wrap is False


def test_fast_path_wrap_kind_normalizes_to_search_when_wb():
    # C1 fold (luna re-gate 3): a boundary-wrapped child makes the composite
    # search-shaped — wrap_kind must normalize to search, never fullmatch.
    for pat, call_kind in [(r"(?:\bfoo|$)", "fullmatch"), (r"^(?:\bfoo|$)", "search")]:
        cr = compile_pattern(pat, "", "pcre", call_kind)
        assert cr.encodable
        assert cr.word_boundary_wrap is True
        assert cr.wrap_kind == "search", (pat, cr.wrap_kind)


def test_py_re_negated_unicode_shorthand_not_exact():
    # C1 fold (luna re-gate 3): [^\d]/[^\s] unicode mirrors exclude only the
    # approximate subset — mirror_exact must be False.
    for pat in (r"[^\d]", r"[^\s]"):
        cr = compile_pattern(pat, "", "py_re", "search")
        assert cr.encodable, (pat, cr.unencodable_reason)
        assert cr.mirror_exact is False, pat


def test_yara_wide_search_shape_and_nocase_fail_closed():
    # C1 fold (luna re-gate 3): wide literals under search are substring
    # matches (search-shaped mirror); wide nocase is not modeled -> fail closed.
    cr = compile_pattern("abc", "", "yara", "search", domain="wide")
    assert cr.encodable
    assert cr.wrap_kind == "search"
    assert cr.fullmatch_shaped is False
    assert cr.mirror_exact is True
    cr2 = compile_pattern("abc", "", "yara", "fullmatch", domain="wide")
    assert cr2.fullmatch_shaped is True
    cr3 = compile_pattern("abc", "i", "yara", "search", domain="wide")
    assert cr3.mirror_exact is False


def test_alternation_propagates_word_boundary_wrap():
    # C1 fold (luna re-gate 3): \bfoo|\bbar — a \b-wrapped alternative makes
    # the whole mirror search-shaped; fullmatch_shaped must be False.
    cr = compile_pattern(r"\bfoo|\bbar", "", "pcre", "fullmatch")
    assert cr.encodable, cr.unencodable_reason
    assert cr.word_boundary_wrap is True
    assert cr.fullmatch_shaped is False


def test_py_re_unicode_dot_and_negated_class_not_exact():
    # C1 fold (luna re-gate 3): unicode `.` and negated classes are BMP-bounded
    # approximations — mirror_exact must be False.
    for pat in (r"a.b", r"[^a]", r"^[^x]+$"):
        cr = compile_pattern(pat, "", "py_re", "search")
        if not cr.encodable:
            continue  # some negated forms are rejected outright — fine
        assert cr.mirror_exact is False, pat


def test_fast_path_trailing_dollar_source_derived():
    # C1 fold (luna re-gate 3): trailing_dollar comes from the source $ alt,
    # not the call_kind wrap.
    for pat, call_kind in [(r"^(?:abc|$)", "search"), (r"(?:abc|$)", "fullmatch")]:
        cr = compile_pattern(pat, "", "pcre", call_kind)
        assert cr.encodable
        assert cr.trailing_dollar is True, (pat, cr.trailing_dollar)
    # yara wide literal has no $ in source -> False even under fullmatch
    cr = compile_pattern("abc", "", "yara", "fullmatch", domain="wide")
    assert cr.trailing_dollar is False


def test_mixed_alternation_keeps_normal_wrap():
    # C1 fold (luna re-gate 4): \bfoo|bar is MIXED — the plain bar branch
    # needs the search padding. wb must NOT propagate (only the all-wrapped
    # case skips the outer wrap); fullmatch keeps the whole-string shape.
    cr = compile_pattern(r"\bfoo|bar", "", "pcre", "search")
    assert cr.encodable, cr.unencodable_reason
    assert cr.word_boundary_wrap is False
    assert cr.fullmatch_shaped is False  # padded search mirror
    cr2 = compile_pattern(r"\bfoo|\bbar", "", "pcre", "search")
    assert cr2.word_boundary_wrap is True
    assert cr2.fullmatch_shaped is False


def test_yara_wide_match_is_prefix_anchored():
    # C1 fold (luna re-gate 5): a yara wide literal under call_kind=match is
    # prefix-anchored (literal + anything), not the search shape.
    cr = compile_pattern("abc", "", "yara", "match", domain="wide")
    assert cr.encodable
    assert cr.wrap_kind == "match"
    assert cr.fullmatch_shaped is False
    # search shape stays search
    cr2 = compile_pattern("abc", "", "yara", "search", domain="wide")
    assert cr2.wrap_kind == "search"


def test_scoped_ascii_group_mirror_is_faithful():
    # C1 (luna re-gate 5 refuted): (?a:...) applies the ASCII scoping to the
    # child lowering (py_re.py:261-266) — the engine is equally ASCII-limited
    # under the scoped flag, so mirror_exact=True is faithful. Refuted with
    # the probe: (?a:.) / (?a:[^x]) / (?a:\w+) / x(?a:.)y all encodable with
    # the ASCII-limited mirror and mirror_exact=True.
    for pat in (r"(?a:.)", r"(?a:[^x])", r"(?a:\w+)", r"x(?a:.)y"):
        cr = compile_pattern(pat, "", "py_re", "search")
        assert cr.encodable, pat
        assert cr.mirror_exact is True, pat
