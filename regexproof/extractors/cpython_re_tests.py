"""Extract patterns from CPython ``Lib/test/re_tests.py`` style tables."""

from __future__ import annotations

import ast
import re
from typing import Any

from regexproof.extractors.record import make_record

# (pattern, match_string, outcome, ...) — take first string in tuple rows.
_ROW = re.compile(
    r"^\s*\(\s*(?P<q>['\"])(?P<pat>(?:\\.|(?!\1).)*)(?P=q)\s*,",
    re.MULTILINE,
)


def extract_cpython_re_tests(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "py_re",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for m in _ROW.finditer(source):
        raw = m.group("pat")
        try:
            pattern = ast.literal_eval(m.group("q") + raw + m.group("q"))
        except Exception:  # noqa: BLE001
            pattern = raw
        if not isinstance(pattern, str) or not pattern:
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
