"""Extract regex patterns from busybox ``*.tests`` scripts (full format).

Handles:
- ``testing "desc" "command" "expected" "input" "args"`` function calls
- Embedded grep/sed/awk patterns within command strings
- Direct ``grep -E 'pat'`` and ``sed`` invocations outside testing()
- Bucketed parse issues: a=parsed, b=skipped, c=parse-error
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

_GREP_E_SQ = re.compile(r"grep\s+-E\s+'(?P<pat>(?:\\.|[^'])*)'")
_GREP_E_DQ = re.compile(r'grep\s+-E\s+"(?P<pat>(?:\\.|[^"])*)"')
_GREP_SQ = re.compile(r"grep\s+(?:-[iwnc]*\s+)?'(?P<pat>(?:\\.|[^'])*)'")
_GREP_DQ = re.compile(r'grep\s+(?:-[iwnc]*\s+)?"(?P<pat>(?:\\.|[^"])*)"')
_SED_SUB_SQ = re.compile(r"sed\s+(?:-[nreE]*\s+)*'s(?P<d>.)(?P<pat>(?:\\.|[^'])*)'")
_SED_SUB_DQ = re.compile(r'sed\s+(?:-[nreE]*\s+)*"s(?P<d>.)(?P<pat>(?:\\.|[^"])*)"')
_SED_ADDR_SQ = re.compile(r"sed\s+(?:-[nreE]*\s+)*'/(?P<pat>(?:\\.|[^'/])*)/")
_SED_ADDR_DQ = re.compile(r'sed\s+(?:-[nreE]*\s+)*"/(?P<pat>(?:\\.|[^"/])*)/')
_AWK_PAT_SQ = re.compile(r"awk\s+(?:-F\S+\s+)?'/(?P<pat>(?:\\.|[^'/])*)/")
_AWK_PAT_DQ = re.compile(r'awk\s+(?:-F\S+\s+)?"/(?P<pat>(?:\\.|[^"/])*)/')
_EXPR_SQ = re.compile(r"expr\s+\S+\s+:\s+'(?P<pat>(?:\\.|[^'])*)'")
_EXPR_DQ = re.compile(r'expr\s+\S+\s+:\s+"(?P<pat>(?:\\.|[^"])*)"')

_TESTING_CALL = re.compile(
    r'testing\s+"(?P<desc>(?:\\.|[^"])*)"\s+'
    r'"(?P<cmd>(?:\\.|[^"])*)"\s+'
    r'"(?P<expect>(?:\\.|[^"])*)"\s+'
    r'"(?P<input>(?:\\.|[^"])*)"\s+'
    r'"(?P<args>(?:\\.|[^"])*)"',
)


class ParseStats:
    __slots__ = ("parsed", "skipped", "errors")

    def __init__(self) -> None:
        self.parsed = 0
        self.skipped = 0
        self.errors = 0

    def as_dict(self) -> dict[str, int]:
        return {"a_parsed": self.parsed, "b_skipped": self.skipped, "c_errors": self.errors}


_CMD_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (_GREP_E_SQ, "grep-E"), (_GREP_E_DQ, "grep-E"),
    (_SED_SUB_SQ, "sed-sub"), (_SED_SUB_DQ, "sed-sub"),
    (_SED_ADDR_SQ, "sed-addr"), (_SED_ADDR_DQ, "sed-addr"),
    (_AWK_PAT_SQ, "awk"), (_AWK_PAT_DQ, "awk"),
    (_EXPR_SQ, "expr"), (_EXPR_DQ, "expr"),
    (_GREP_SQ, "grep"), (_GREP_DQ, "grep"),
]

_DIRECT_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (_GREP_E_SQ, "grep-E"), (_GREP_E_DQ, "grep-E"),
    (_SED_SUB_SQ, "sed-sub"), (_SED_SUB_DQ, "sed-sub"),
    (_SED_ADDR_SQ, "sed-addr"), (_SED_ADDR_DQ, "sed-addr"),
]


def _extract_patterns_from_cmd(cmd: str) -> list[tuple[str, str]]:
    """Extract (pattern, tool) pairs from a command string."""
    results: list[tuple[str, str]] = []
    seen: set[str] = set()

    for rx, tool in _CMD_PATTERNS:
        for m in rx.finditer(cmd):
            pat = m.group("pat")
            if pat and len(pat) >= 1 and pat not in seen:
                seen.add(pat)
                results.append((pat, tool))

    return results


def extract_busybox_tests(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "pcre",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    stats = ParseStats()
    seen_ids: set[str] = set()

    for m in _TESTING_CALL.finditer(source):
        cmd = m.group("cmd")
        line_no = source.count("\n", 0, m.start()) + 1
        pairs = _extract_patterns_from_cmd(cmd)
        if not pairs:
            stats.skipped += 1
            continue
        for pat, tool in pairs:
            rec = make_record(
                repo=repo,
                pattern=pat,
                flags="",
                dialect=dialect,
                call_kind="search",
                file=file,
                line=line_no,
                column=0,
                context_snippet=m.group(0)[:500],
            )
            if rec["regex_id"] not in seen_ids:
                seen_ids.add(rec["regex_id"])
                out.append(rec)
                stats.parsed += 1

    for rx, tool in _DIRECT_PATTERNS:
        for m in rx.finditer(source):
            overall_start = m.start()
            line_start = source.rfind("\n", 0, overall_start) + 1
            prefix = source[line_start:overall_start]
            if "testing" in prefix:
                continue
            pat = m.group("pat")
            if not pat or len(pat) < 1:
                continue
            line_no = source.count("\n", 0, overall_start) + 1
            rec = make_record(
                repo=repo,
                pattern=pat,
                flags="",
                dialect=dialect,
                call_kind="search",
                file=file,
                line=line_no,
                column=0,
                context_snippet=m.group(0)[:500],
            )
            if rec["regex_id"] not in seen_ids:
                seen_ids.add(rec["regex_id"])
                out.append(rec)
                stats.parsed += 1

    for rec in out:
        rec["_parse_stats"] = stats.as_dict()
    return out
