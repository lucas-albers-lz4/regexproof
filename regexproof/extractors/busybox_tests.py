"""Extract quoted regex-like strings from busybox ``*.tests`` scripts."""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

# Common busybox test invocations: testing "name" "cmd" "expect"
# Also grep -E 'pattern' style inside scripts.
_GREP_E = re.compile(r"grep\s+-E\s+(?P<q>['\"])(?P<pat>(?:\\.|(?!\1).)*)(?P=q)")
_SED_E = re.compile(r"sed\s+-n?\s*e\s*(?P<q>['\"])(?P<pat>(?:\\.|(?!\1).)*)(?P=q)")


def extract_busybox_tests(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "pcre",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for rx in (_GREP_E, _SED_E):
        for m in rx.finditer(source):
            pattern = m.group("pat")
            if not pattern or len(pattern) < 2:
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
