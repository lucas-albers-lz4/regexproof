"""Build versioned extractor JSONL records."""

from __future__ import annotations

from typing import Any

from regexproof.regex_id import make_regex_id
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
    context_snippet: str = "",
    unencodable_reason: str | None = None,
) -> dict[str, Any]:
    site = f"{file}:{line}:{column}"
    rec: dict[str, Any] = {
        "schema_version": EXTRACTOR_SCHEMA_VERSION,
        "regex_id": make_regex_id(repo, pattern, flags, dialect, call_kind, site),
        "repo": repo,
        "pattern": pattern,
        "flags": flags,
        "dialect": dialect,
        "call_kind": call_kind,
        "site": site,
        "file": file,
        "line": line,
        "column": column,
        "context_snippet": context_snippet[:500],
    }
    if unencodable_reason:
        rec["unencodable_reason"] = unencodable_reason
    return rec
