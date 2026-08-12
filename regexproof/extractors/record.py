"""Build versioned extractor JSONL records."""

from __future__ import annotations

from typing import Any

from regexproof.regex_id import DEFAULT_DOMAIN, make_regex_id
from regexproof.schemas import EXTRACTOR_SCHEMA_VERSION


def make_record(
    *,
    repo: str,
    pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    file: str,
    line: int,
    column: int,
    domain: str = DEFAULT_DOMAIN,
    context_snippet: str = "",
    unencodable_reason: str | None = None,
    extra_fields: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a versioned extractor record.

    ``extra_fields`` is the field-extensibility contract: a typed dict merged
    into the record BEFORE the fixed fields are set — fixed fields win, so an
    ``extra_fields`` attempt to override ``pattern``/``dialect``/``regex_id``
    (or any fixed field) is silently ignored.  Deliberately NOT bare
    ``**kwargs``: a typo'd kwarg from any of the 30+ callers would silently
    corrupt records.
    """
    site = f"{file}:{line}:{column}"
    rec: dict[str, Any] = dict(extra_fields or {})
    rec.update({
        "schema_version": EXTRACTOR_SCHEMA_VERSION,
        "regex_id": make_regex_id(repo, pattern, flags, dialect, call_kind, site, domain=domain),
        "repo": repo,
        "pattern": pattern,
        "flags": flags,
        "dialect": dialect,
        "call_kind": call_kind,
        "site": site,
        "file": file,
        "line": line,
        "column": column,
        "domain": domain,
        "context_snippet": context_snippet[:500],
    })
    if unencodable_reason:
        rec["unencodable_reason"] = unencodable_reason
    return rec
