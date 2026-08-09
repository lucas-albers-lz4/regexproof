"""hapijs/isemail lib/ regex extractor (Wave 3 / #115).

RFC5321/5322 email validator — mostly a character-class parser; only a
handful of true JS regex literals survive a comment/string-aware scan.
"""

from __future__ import annotations

from typing import Any

from regexproof.extractors.js_babel import extract_js_precise


def extract_isemail(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """Extract ecma regex literals from an isemail ``lib/*.js`` unit."""
    recs = extract_js_precise(source, repo=repo, file=file)
    for rec in recs:
        snippet = rec.get("context_snippet") or ""
        # Tag IP / ASCII helpers for triage notes.
        pat = rec.get("pattern") or ""
        if "ipV4" in snippet or "25[0-5]" in pat:
            rec["rule_name"] = "ipV4"
        elif "ipV6" in snippet or "a-fA-F" in pat:
            rec["rule_name"] = "ipV6"
        elif "nonASCII" in snippet:
            rec["rule_name"] = "nonASCII"
    return recs
