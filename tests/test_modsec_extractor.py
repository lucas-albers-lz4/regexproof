"""ModSecurity extractor accuracy: @rx operators, escaped quotes, selectors."""

from __future__ import annotations

import itertools
import random
import re
from pathlib import Path

import jsonschema

import regexproof.extractors.modsec as modsec
from regexproof.extractors.modsec import count_operators, extract_modsec
from regexproof.schemas import extractor_schema

REPO = "coreruleset/coreruleset"


def _extract(source: str) -> list[dict]:
    recs = extract_modsec(source, repo=REPO, file="rules/test.conf")
    schema = extractor_schema()
    for r in recs:
        jsonschema.validate(r, schema)
    return recs


def test_basic_rx_operator():
    src = 'SecRule REQUEST_URI "@rx /admin" "id:1,phase:2,deny"\n'
    recs = _extract(src)
    assert len(recs) == 1
    assert recs[0]["pattern"] == "/admin"
    assert recs[0]["dialect"] == "pcre"
    assert recs[0]["call_kind"] == "search"
    assert recs[0]["site"] == "rules/test.conf:1:0"
    assert recs[0]["negated"] is False
    assert recs[0]["rule_id"] == "1"


def test_multiline_secrule_captures_rule_id():
    src = (
        'SecRule ARGS "@rx (?i)union\\s+select" \\\n'
        '    "id:942100,\\\n'
        '    phase:2,\\\n'
        '    deny"\n'
    )
    recs = _extract(src)
    assert len(recs) == 1
    assert recs[0]["rule_id"] == "942100"
    assert "union" in recs[0]["pattern"]


def test_negated_rx_operator():
    src = 'SecRule REQUEST_URI "!@rx /admin" "id:2,phase:1,allow"\n'
    recs = _extract(src)
    assert len(recs) == 1
    assert recs[0]["pattern"] == "/admin"
    assert recs[0]["negated"] is True


def test_escaped_quote_inside_pattern_not_truncated():
    """Regression: CRS patterns embed \\" escapes; naive capture truncates."""
    src = r'SecRule ARGS "@rx <script[^>]*>[\s\x0b&\)\"\']*" "id:3,phase:2,deny"' + "\n"
    recs = _extract(src)
    assert len(recs) == 1
    assert recs[0]["pattern"] == r"<script[^>]*>[\s\x0b&\)\"\']*"


def test_pattern_with_alternation_and_classes():
    src = r'SecRule ARGS "@rx (?i)union\s+select|[\--9A-Z_a-z]" "id:4"' + "\n"
    recs = _extract(src)
    assert len(recs) == 1
    assert "union" in recs[0]["pattern"]


def test_variable_selector_regex_extracted():
    src = 'SecRule REQUEST_COOKIES "!@within x" "id:5"\n'
    src += 'SecRule ARGS "!REQUEST_COOKIES:/^_pk_ref/" "id:6,phase:1,pass"\n'
    src += 'SecRule ARGS "!REQUEST_COOKIES:/^pbjs-\\w+$/" "id:7"\n'
    recs = _extract(src)
    selectors = [r for r in recs if r.get("selector")]
    assert len(selectors) == 2
    assert selectors[0]["pattern"] == "^_pk_ref"
    assert selectors[0]["negated"] is True
    assert selectors[1]["pattern"] == r"^pbjs-\w+$"


def test_quoted_variable_selector_is_literal_not_regex():
    src = 'SecRule ARGS "!REQUEST_COOKIES:FCCDCF" "id:8"\n'
    recs = _extract(src)
    assert recs == []


def test_non_regex_operator_not_extracted_but_counted():
    src = 'SecRule REQUEST_BODY "@lt 1024" "id:9"\n'
    src += 'SecRule REQUEST_BODY "@ge 1024" "id:10"\n'
    assert _extract(src) == []
    counts = count_operators(src)
    assert counts["@lt"] == 1
    assert counts["@ge"] == 1


def test_comments_and_non_secrule_lines_skipped():
    src = "# a comment\nSecRule ARGS \"@rx x\" \"id:11\"\nSecAction \"id:12,phase:1\"\n"
    recs = _extract(src)
    assert len(recs) == 1
    assert recs[0]["line"] == 2


def test_inline_crs_style_corpus():
    """A realistic multi-rule CRS-style corpus extracts end to end."""
    src = (
        '# CRS rule\n'
        'SecRule REQUEST_URI "@rx ^(?:connect (?:(?:[0-9]{1,3}\\.){3}[0-9]{1,3}|[a-z]+:[0-9]+)|options \\*)" "id:920100,phase:1,deny"\n'
        'SecRule ARGS "@rx (?i)union\\s+select" "id:942100,phase:2,deny"\n'
        'SecRule REQUEST_HEADERS "!@rx (?i)charset.*?charset" "id:920120,phase:1,pass"\n'
        'SecRule REQUEST_BODY "@lt 1024" "id:920180,phase:1,pass"\n'
        'SecRule ARGS "!REQUEST_COOKIES:/^_pk_ref/" "id:920280,phase:1,pass"\n'
    )
    recs = _extract(src)
    assert len(recs) == 4  # 3 @rx + 1 selector regex; @lt is not regex
    rx = [r for r in recs if not r.get("selector")]
    assert len(rx) == 3
    assert rx[0]["pattern"].startswith("^(?:connect ")
    assert rx[1]["pattern"] == "(?i)union\\s+select"
    assert rx[2]["negated"] is True
    assert rx[2]["pattern"] == "(?i)charset.*?charset"
    assert next(r for r in recs if r.get("selector"))["pattern"] == "^_pk_ref"


def test_selector_escaped_slash_body_extracted():
    """Selectors whose body escapes the delimiter keep extracting post-rewrite."""
    src = 'SecRule ARGS "!REQUEST_COOKIES:/a\\/b/" "id:20"\n'
    recs = _extract(src)
    selectors = [r for r in recs if r.get("selector")]
    assert len(selectors) == 1
    assert selectors[0]["pattern"] == r"a\/b"


def test_selector_trailing_backslash_parity():
    """Parity: the pre-rewrite pattern admitted a lone backslash before the
    closing delimiter (body "a\\" from /a\\/); the rewrite preserves that
    language exactly via the trailing \\? — no silent extraction change."""
    src = 'SecRule ARGS "!X:/a\\/" "id:21"\n'
    recs = _extract(src)
    selectors = [r for r in recs if r.get("selector")]
    assert len(selectors) == 1
    assert selectors[0]["pattern"] == "a\\"


# Pre-rewrite _RX_SELECTOR (py/redos alert #7). The linear-time rewrite must
# match this language exactly — see issue #141 for the differential evidence.
# The vulnerable pattern lives in a fixture, not inline: an inline literal is
# itself flagged by py/redos, and in-source codeql[...] suppression comments
# are not honored by this repo's code scanning (alert #5 precedent). It runs
# only on this file's short deterministic battery, never on untrusted input.
_PRE_REWRITE_SELECTOR = re.compile(
    (
        Path(__file__).resolve().parent
        / "fixtures"
        / "modsec"
        / "pre-rewrite-selector-regex.txt"
    )
    .read_text(encoding="utf-8")
    .strip()
)


def _sig(rx: re.Pattern[str], s: str) -> list[tuple[tuple[int, int], str]]:
    return [(m.span(), m.group(1)) for m in rx.finditer(s)]


def test_selector_regex_language_parity_with_pre_rewrite():
    """Equivalence gate: new _RX_SELECTOR ≡ pre-rewrite pattern (corpus + fuzz)."""
    corpus = [
        'SecRule ARGS "!REQUEST_COOKIES:/^_pk_ref/" "id:6,phase:1,pass"\n',
        'SecRule ARGS "!REQUEST_COOKIES:/^pbjs-\\w+$/" "id:7"\n',
        'SecRule ARGS "!REQUEST_COOKIES:FCCDCF" "id:8"\n',
        'SecRule ARGS "!X:/a\\/b/i" "id:22"\n',
        'SecRule ARGS "!X:"quoted"" "id:23"\n',
    ]
    rng = random.Random(42)
    alpha = ["a", "b", "\\", "/", '"', "!", "X", ":", "i", "_", "^", "$", " ", "0"]
    fuzz = ["".join(rng.choice(alpha) for _ in range(rng.randint(0, 14))) for _ in range(3000)]
    for k in range(5):  # exhaustive short selector bodies over the dangerous chars
        for tup in itertools.product(["a", "\\", "/"], repeat=k):
            body = "".join(tup)
            fuzz.append("!X:/" + body + "/")
            fuzz.append("!X:/" + body)
    for s in corpus + fuzz:
        assert _sig(modsec._RX_SELECTOR, s) == _sig(_PRE_REWRITE_SELECTOR, s), s
