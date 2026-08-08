"""PCRE2 ``testdata/testinput*`` pattern extractor.

Lines that begin with ``/`` introduce a pattern; the pattern ends at the
next unescaped ``/`` (flags may follow). Modifier/command lines are skipped.
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

_START = re.compile(r"^/(?P<body>.*)$")


def extract_pcre2_testdata(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "pcre",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for i, line in enumerate(source.splitlines(), 1):
        if not line.startswith("/"):
            continue
        # Find closing /
        j = 1
        while j < len(line):
            if line[j] == "\\" and j + 1 < len(line):
                j += 2
                continue
            if line[j] == "/":
                pattern = line[1:j]
                flags = "".join(c for c in line[j + 1 :].lower() if c in "imsx")
                if pattern:
                    out.append(
                        make_record(
                            repo=repo,
                            pattern=pattern,
                            flags=flags,
                            dialect=dialect,
                            call_kind="search",
                            file=file,
                            line=i,
                            column=0,
                            context_snippet=line[:500],
                        )
                    )
                break
            j += 1
    return out
