"""JS/TS extractor scaffold — regex literal + new RegExp via regex-based scan.

Full Babel traverse lands with Node deps; this scaffold uses a deterministic
regex scan that fixtures validate, and marks non-literal RegExp as composite.
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

_LITERAL = re.compile(r"/(?P<pat>(?:\\.|[^/\\])+)/(?P<flags>[dgimsuvy]*)")
_NEW_REGEXP = re.compile(
    r"new\s+RegExp\s*\(\s*(?P<arg>[^)]+)\s*\)",
    re.MULTILINE,
)
_CALL = re.compile(
    r"(?P<head>(?:[A-Za-z_$][\w$]*|\([^)]*\)))\s*\.\s*(?P<meth>test|exec|match|replace)\s*\("
)


def extract_js(source: str, *, repo: str, file: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for m in _LITERAL.finditer(source):
        flags = m.group("flags")
        reason = None
        call_kind = "search"
        if any(f in flags for f in "gy"):
            reason = "stateful"
        elif "u" in flags or "v" in flags:
            reason = f"{ 'u' if 'u' in flags else 'v' }-flag"
        # Heuristic consuming call on same line
        line_start = source.rfind("\n", 0, m.start()) + 1
        line_end = source.find("\n", m.end())
        if line_end < 0:
            line_end = len(source)
        line = source[line_start:line_end]
        if ".exec(" in line:
            call_kind = "exec"
        elif ".test(" in line:
            call_kind = "search"
        elif ".replace(" in line:
            call_kind = "substitution"
        line_no = source.count("\n", 0, m.start()) + 1
        col = m.start() - line_start
        out.append(
            make_record(
                repo=repo,
                pattern=m.group("pat"),
                flags="".join(c for c in "dgimsuvy" if c in flags),
                dialect="ecma",
                call_kind=call_kind,
                file=file,
                line=line_no,
                column=col,
                context_snippet=line.strip()[:500],
                unencodable_reason=reason,
            )
        )
    for m in _NEW_REGEXP.finditer(source):
        arg = m.group("arg").strip()
        line_no = source.count("\n", 0, m.start()) + 1
        col = m.start() - (source.rfind("\n", 0, m.start()) + 1)
        if (arg.startswith("'") and arg.endswith("'")) or (
            arg.startswith('"') and arg.endswith('"')
        ) or (arg.startswith("`") and arg.endswith("`") and "${" not in arg):
            pattern = arg[1:-1]
            reason = None
        else:
            pattern = ""
            reason = "composite-pattern"
        out.append(
            make_record(
                repo=repo,
                pattern=pattern,
                flags="",
                dialect="ecma",
                call_kind="search",
                file=file,
                line=line_no,
                column=col,
                context_snippet=m.group(0)[:500],
                unencodable_reason=reason,
            )
        )
    return out
