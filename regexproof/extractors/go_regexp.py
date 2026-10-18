"""Extract literal patterns passed to Go's ``regexp`` APIs.

This covers package-level ``MustCompile`` / ``Compile`` calls and the static
pattern argument to ``Match``, ``MatchString``, and ``MatchReader``. Skips
non-``.go`` files. Dynamic pattern expressions remain outside this extractor
and need the separate classification described in ``docs/DYNAMIC.md``.
Raw string literals (backticks) are preferred when present.
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

# regexp.MustCompile("...") or .Compile(`...`) — single-line common case.
_MUST = re.compile(
    r'regexp\.(?:MustCompile|Compile)\(\s*(?P<q>"|`)(?P<body>(?:\\.|(?!\1).)*)(?P=q)\s*\)',
    re.DOTALL,
)
_ONE_SHOT = re.compile(
    r'regexp\.(?:Match|MatchString|MatchReader)\(\s*'
    r'(?P<q>"|`)(?P<body>(?:\\.|(?!\1).)*)(?P=q)\s*,',
    re.DOTALL,
)


def extract_go_regexp(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "re2",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    matches = sorted(
        [*_MUST.finditer(source), *_ONE_SHOT.finditer(source)],
        key=lambda match: match.start(),
    )
    for m in matches:
        # Skip matches that sit on a // comment line (common for WIP patterns).
        line_start = source.rfind("\n", 0, m.start()) + 1
        line_prefix = source[line_start : m.start()]
        if "//" in line_prefix:
            continue
        raw = m.group("body")
        q = m.group("q")
        if q == '"':
            try:
                pattern = bytes(raw, "utf-8").decode("unicode_escape")
            except UnicodeDecodeError:
                pattern = raw
        else:
            pattern = raw
        if not pattern:
            continue
        line_no = source.count("\n", 0, m.start()) + 1
        out.append(
            make_record(
                repo=repo,
                pattern=pattern,
                flags="",
                dialect=dialect,
                call_kind="search",
                file=file,
                line=line_no,
                column=0,
                context_snippet=m.group(0)[:500],
            )
        )
    return out
