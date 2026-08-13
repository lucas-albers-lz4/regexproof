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
    assert cr.trailing_dollar is False
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
    assert cr.trailing_dollar is False


def test_trailing_alt_dollar_synthesizes_contract():
    cr = compile_pattern("foo(?:bar|$)", "", "re2", "search")
    assert cr.encodable
    assert cr.leading_caret is False
    assert cr.trailing_dollar is False
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
    _discard_streamed_mirrors(stream)
