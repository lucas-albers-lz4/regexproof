"""jackbearheart/email-addresses lib/ regex extractor (Wave 3 / #115).

RFC5322 address parser — overwhelmingly a hand-written recursive-descent
parser; regex literals are whitespace normalizers only.
"""

from __future__ import annotations

from typing import Any

from regexproof.extractors.js_babel import extract_js_precise


def extract_email_addresses(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """Extract ecma regex literals from email-addresses ``lib/*.js``."""
    # Skip minified builds — they duplicate the non-min source and inflate counts.
    if file.endswith(".min.js"):
        return []
    recs = extract_js_precise(source, repo=repo, file=file)
    for rec in recs:
        snippet = rec.get("context_snippet") or ""
        if "replace" in snippet:
            rec["rule_name"] = "whitespace-normalize"
    return recs
