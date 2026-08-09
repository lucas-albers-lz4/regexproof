"""Extract patterns from CPython ``Lib/test/re_tests.py`` table + ``test_re.py`` AST.

Combines two extraction passes:
1. Table pass: ``(r'pattern', ...)`` rows from ``re_tests.py``-style tuple tables
2. AST pass: ``re.compile/match/search/fullmatch/sub/split`` calls from
   ``test_re.py``-style test files (reuses ``python_ast.extract_python``)

Bucketed parse issues: a=parsed, b=skipped, c=parse-error.
"""

from __future__ import annotations

import ast
import re
from typing import Any

from regexproof.extractors.record import make_record

_ROW = re.compile(
    r"^\s*\(\s*(?P<prefix>[rRuUbBfF]*)(?P<q>['\"])(?P<pat>(?:\\.|(?!\2).)*)(?P=q)\s*,",
    re.MULTILINE,
)


class ParseStats:
    __slots__ = ("parsed", "skipped", "errors")

    def __init__(self) -> None:
        self.parsed = 0
        self.skipped = 0
        self.errors = 0

    def as_dict(self) -> dict[str, int]:
        return {"a_parsed": self.parsed, "b_skipped": self.skipped, "c_errors": self.errors}


def extract_cpython_re_tests(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "py_re",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    stats = ParseStats()

    for m in _ROW.finditer(source):
        raw = m.group("pat")
        prefix = m.group("prefix") or ""
        lit = prefix + m.group("q") + raw + m.group("q")
        try:
            pattern = ast.literal_eval(lit)
        except Exception:  # noqa: BLE001
            pattern = raw
            stats.errors += 1
        if not isinstance(pattern, str) or not pattern:
            stats.skipped += 1
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
        stats.parsed += 1

    for rec in out:
        rec["_parse_stats"] = stats.as_dict()
    return out


def extract_cpython_test_re(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """AST pass over ``test_re.py`` — extracts re.compile/match/search/etc."""
    from regexproof.extractors.python_ast import extract_python

    try:
        records = extract_python(source, repo=repo, file=file)
    except SyntaxError:
        return []
    stats = ParseStats()
    stats.parsed = len([r for r in records if not r.get("unencodable_reason")])
    stats.skipped = len([r for r in records if r.get("unencodable_reason")])
    for rec in records:
        rec["_parse_stats"] = stats.as_dict()
    return records


def extract_cpython_combined(
    sources: dict[str, str],
    *,
    repo: str,
    base_path: str = "",
) -> list[dict[str, Any]]:
    """Combined extraction: re_tests.py table + test_re.py AST.

    ``sources`` maps filename → content (e.g. ``{"re_tests.py": "...", "test_re.py": "..."}``).
    """
    out: list[dict[str, Any]] = []
    for filename, content in sorted(sources.items()):
        fpath = f"{base_path}/{filename}" if base_path else filename
        if "re_tests" in filename:
            out.extend(extract_cpython_re_tests(
                content, repo=repo, file=fpath, dialect="py_re",
            ))
        elif "test_re" in filename:
            out.extend(extract_cpython_test_re(
                content, repo=repo, file=fpath,
            ))
    return out
