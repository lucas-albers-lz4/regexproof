"""DOMPurify + isemail + email-addresses extractors / Wave-3 P4 (#115)."""

from __future__ import annotations

from pathlib import Path

import jsonschema
import pytest
import z3

from regexproof.batch.disclose import SECURITY_TOOL_CORPORA
from regexproof.batch.runner import CORPUS_MANIFESTS, WAVE_CORPORA
from regexproof.compiler import compile_pattern
from regexproof.extractors.dompurify import extract_dompurify
from regexproof.extractors.email_addresses import extract_email_addresses
from regexproof.extractors.isemail import extract_isemail
from regexproof.extractors.js_babel import extract_js_precise
from regexproof.schemas import extractor_schema

ROOT = Path(__file__).resolve().parents[1]
DP_SAMPLE = ROOT / "batch" / "corpora" / "dompurify" / "sample"
IS_SAMPLE = ROOT / "batch" / "corpora" / "isemail" / "sample"
EA_SAMPLE = ROOT / "batch" / "corpora" / "email_addresses" / "sample"


def _validate(recs):
    schema = extractor_schema()
    for r in recs:
        jsonschema.validate(r, schema)


def test_dompurify_sample_seal_names():
    src = (DP_SAMPLE / "regexp.ts").read_text(encoding="utf-8")
    recs = extract_dompurify(src, repo="cure53/DOMPurify", file="sample/regexp.ts")
    assert len(recs) == 3
    by_name = {r.get("rule_name"): r for r in recs}
    assert "IS_ALLOWED_URI" in by_name
    assert "IS_SCRIPT_OR_DATA" in by_name
    script = by_name["IS_SCRIPT_OR_DATA"]
    assert script["dialect"] == "ecma"
    assert script["pattern"] == r"^(?:\w+script|data):"
    assert "i" in script["flags"]
    assert script.get("sanitizer_check") == "IS_SCRIPT_OR_DATA"
    _validate(recs)


def test_precise_skips_new_regexp_in_comments():
    src = (
        "// new RegExp('phantom')\n"
        "/* new RegExp(\"also\") */\n"
        "const r = new RegExp('live');\n"
    )
    recs = extract_js_precise(src, repo="t", file="x.js")
    assert len(recs) == 1
    assert recs[0]["pattern"] == "live"


def test_seal_name_not_attached_to_distant_regex():
    """A non-seal regex after a seal binding must not inherit the seal name."""
    src = (
        "export const IS_SCRIPT_OR_DATA = seal(/^(?:\\w+script|data):/i);\n"
        "const later = /https:/i;\n"
    )
    recs = extract_dompurify(src, repo="cure53/DOMPurify", file="x.ts")
    assert len(recs) == 2
    by_pat = {r["pattern"]: r for r in recs}
    assert by_pat[r"^(?:\w+script|data):"].get("rule_name") == "IS_SCRIPT_OR_DATA"
    assert by_pat["https:"].get("rule_name") is None
    assert by_pat["https:"].get("sanitizer_check") is None


def test_seal_name_ignores_bindings_inside_strings():
    """A seal( mention inside a string must not steal the real export name."""
    src = (
        'const note = "export const FAKE = seal(/xx/)";\n'
        "export const IS_SCRIPT_OR_DATA = seal(/^(?:\\w+script|data):/i);\n"
    )
    recs = extract_dompurify(src, repo="cure53/DOMPurify", file="x.ts")
    assert len(recs) == 1
    assert recs[0].get("rule_name") == "IS_SCRIPT_OR_DATA"
    assert recs[0].get("sanitizer_check") == "IS_SCRIPT_OR_DATA"


def test_dompurify_deterministic():
    src = (DP_SAMPLE / "regexp.ts").read_text(encoding="utf-8")
    a = extract_dompurify(src, repo="cure53/DOMPurify", file="sample/regexp.ts")
    b = extract_dompurify(src, repo="cure53/DOMPurify", file="sample/regexp.ts")
    assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]


def test_isemail_sample_ipv6():
    src = (IS_SAMPLE / "parser_snippet.js").read_text(encoding="utf-8")
    recs = extract_isemail(src, repo="hapijs/isemail", file="sample/parser_snippet.js")
    assert len(recs) == 3
    ipv6 = next(r for r in recs if r.get("rule_name") == "ipV6")
    assert ipv6["pattern"] == r"^[a-fA-F\d]{0,4}$"
    assert ipv6["dialect"] == "ecma"
    _validate(recs)


def test_isemail_deterministic():
    src = (IS_SAMPLE / "parser_snippet.js").read_text(encoding="utf-8")
    a = extract_isemail(src, repo="hapijs/isemail", file="sample/parser_snippet.js")
    b = extract_isemail(src, repo="hapijs/isemail", file="sample/parser_snippet.js")
    assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]


def test_email_addresses_sample_ws():
    src = (EA_SAMPLE / "ws.js").read_text(encoding="utf-8")
    recs = extract_email_addresses(
        src, repo="jackbearheart/email-addresses", file="sample/ws.js"
    )
    assert len(recs) == 4
    assert all(r["dialect"] == "ecma" for r in recs)
    # Minified twin must be skipped by path convention.
    assert extract_email_addresses(
        src, repo="jackbearheart/email-addresses", file="lib/email-addresses.min.js"
    ) == []
    _validate(recs)


def test_email_addresses_deterministic():
    src = (EA_SAMPLE / "ws.js").read_text(encoding="utf-8")
    a = extract_email_addresses(
        src, repo="jackbearheart/email-addresses", file="sample/ws.js"
    )
    b = extract_email_addresses(
        src, repo="jackbearheart/email-addresses", file="sample/ws.js"
    )
    assert [r["regex_id"] for r in a] == [r["regex_id"] for r in b]


def test_manifest_files_fail_closed_when_missing(tmp_path: Path):
    """Explicit files: lists must not silently under-count a partial tree."""
    from regexproof.batch.runner import _extract_glob

    root = tmp_path / "rules"
    root.mkdir()
    (root / "src").mkdir()
    (root / "src" / "purify.ts").write_text("const x = /a/;\n", encoding="utf-8")
    # regexp.ts intentionally absent
    meta = {
        "repo": "cure53/DOMPurify",
        "files": ["src/purify.ts", "src/regexp.ts"],
    }
    with pytest.raises(FileNotFoundError, match="regexp.ts"):
        _extract_glob(
            root,
            meta,
            glob="**/*.{ts,js}",
            extract_fn=lambda src, rel: extract_dompurify(
                src, repo="cure53/DOMPurify", file=rel
            ),
        )


def test_wave_corpora_and_security_tool():
    assert "dompurify" in WAVE_CORPORA
    assert "isemail" in WAVE_CORPORA
    assert "email_addresses" in WAVE_CORPORA
    assert "dompurify" in SECURITY_TOOL_CORPORA
    assert "isemail" not in SECURITY_TOOL_CORPORA
    assert "email_addresses" not in SECURITY_TOOL_CORPORA
    assert CORPUS_MANIFESTS["dompurify"]["extractor"] == "dompurify"
    assert CORPUS_MANIFESTS["isemail"]["extractor"] == "isemail"
    assert CORPUS_MANIFESTS["email_addresses"]["extractor"] == "email_addresses"
    files = CORPUS_MANIFESTS["dompurify"]["files"]
    assert "src/purify.ts" in files and "src/regexp.ts" in files


def test_golden_is_script_or_data():
    """Sanitizer boundary: IS_SCRIPT_OR_DATA must encode + classify schemes."""
    pat = r"^(?:\w+script|data):"
    r = compile_pattern(pat, "i", "ecma", "search")
    assert r.encodable, r.unencodable_reason
    solver = z3.Solver()
    solver.set("timeout", 5000)
    solver.add(z3.InRe(z3.StringVal("javascript:"), r.mirror))
    assert solver.check() == z3.sat
    solver = z3.Solver()
    solver.set("timeout", 5000)
    solver.add(z3.InRe(z3.StringVal("https:"), r.mirror))
    assert solver.check() == z3.unsat


def test_golden_isemail_ipv6():
    pat = r"^[a-fA-F\d]{0,4}$"
    r = compile_pattern(pat, "", "ecma", "fullmatch")
    assert r.encodable, r.unencodable_reason
    solver = z3.Solver()
    solver.set("timeout", 5000)
    solver.add(z3.InRe(z3.StringVal("ab12"), r.mirror))
    assert solver.check() == z3.sat


def test_golden_email_addresses_ws():
    pat = r"^\s*"
    r = compile_pattern(pat, "", "ecma", "search")
    assert r.encodable, r.unencodable_reason


def test_mutation_guard_is_script_or_data():
    """Weakening IS_SCRIPT_OR_DATA to admit https: must flip the mirror."""
    tight = compile_pattern(r"^(?:\w+script|data):", "i", "ecma", "search")
    weak = compile_pattern(r"^(?:\w+script|data|https):", "i", "ecma", "search")
    assert tight.encodable and weak.encodable
    solver = z3.Solver()
    solver.set("timeout", 5000)
    # Gap: https: in weak \ tight
    s = z3.String("s")
    solver.add(z3.InRe(s, weak.mirror))
    solver.add(z3.Not(z3.InRe(s, tight.mirror)))
    assert solver.check() == z3.sat


@pytest.mark.parametrize(
    "corpus",
    ["dompurify", "isemail", "email_addresses"],
)
def test_manifest_lists_expected_files(corpus):
    meta = CORPUS_MANIFESTS[corpus]
    assert meta["dialect"] == "ecma"
    assert meta.get("files"), corpus
