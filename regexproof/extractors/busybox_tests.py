"""Extract regex patterns from busybox ``*.tests`` scripts (full format).

Uses linear scanners (no nested-quantifier regexes) to stay ReDoS-safe.
Handles testing() wrappers and direct grep/sed invocations.
"""

from __future__ import annotations

from typing import Any

from regexproof.extractors.record import make_record


class ParseStats:
    __slots__ = ("errors", "parsed", "skipped")

    def __init__(self) -> None:
        self.parsed = 0
        self.skipped = 0
        self.errors = 0

    def as_dict(self) -> dict[str, int]:
        return {"a_parsed": self.parsed, "b_skipped": self.skipped, "c_errors": self.errors}


def _read_dq(s: str, i: int) -> tuple[str | None, int]:
    """Read a double-quoted string starting at s[i]=='\"'. Linear scan."""
    if i >= len(s) or s[i] != '"':
        return None, i
    i += 1
    out: list[str] = []
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            out.append(s[i + 1])
            i += 2
            continue
        if c == '"':
            return "".join(out), i + 1
        out.append(c)
        i += 1
    return None, i


def _read_sq(s: str, i: int) -> tuple[str | None, int]:
    if i >= len(s) or s[i] != "'":
        return None, i
    i += 1
    out: list[str] = []
    while i < len(s):
        c = s[i]
        if c == "'":
            return "".join(out), i + 1
        out.append(c)
        i += 1
    return None, i


def _skip_ws(s: str, i: int) -> int:
    while i < len(s) and s[i].isspace():
        i += 1
    return i


def _find_quoted_after(s: str, start: int, needle: str) -> list[str]:
    """Find needle then next single- or double-quoted string (linear)."""
    found: list[str] = []
    i = 0
    while True:
        j = s.find(needle, i)
        if j < 0:
            break
        k = _skip_ws(s, j + len(needle))
        if k < len(s) and s[k] in "'\"":
            reader = _read_sq if s[k] == "'" else _read_dq
            val, nxt = reader(s, k)
            if val is not None and val:
                found.append(val)
            i = nxt
        else:
            i = j + len(needle)
    return found


def _sed_sub_pattern(s: str) -> list[str]:
    """Extract sed s/// search halves with delimiter awareness (linear)."""
    out: list[str] = []
    i = 0
    while True:
        j = s.find("sed", i)
        if j < 0:
            break
        k = _skip_ws(s, j + 3)
        # skip flags like -n -r
        while k < len(s) and s[k] == "-":
            while k < len(s) and not s[k].isspace() and s[k] not in "'\"":
                k += 1
            k = _skip_ws(s, k)
        if k >= len(s) or s[k] not in "'\"":
            i = j + 3
            continue
        quote = s[k]
        body, nxt = (_read_sq if quote == "'" else _read_dq)(s, k)
        if body is None or not body.startswith("s") or len(body) < 3:
            i = nxt
            continue
        delim = body[1]
        # body is s<delim><pat><delim>...
        rest = body[2:]
        pat_chars: list[str] = []
        m = 0
        while m < len(rest):
            if rest[m] == "\\" and m + 1 < len(rest):
                pat_chars.append(rest[m : m + 2])
                m += 2
                continue
            if rest[m] == delim:
                break
            pat_chars.append(rest[m])
            m += 1
        pat = "".join(pat_chars)
        if pat:
            out.append(pat)
        i = nxt
    return out


def _extract_patterns_from_cmd(cmd: str) -> list[tuple[str, str]]:
    results: list[tuple[str, str]] = []
    seen: set[str] = set()

    def add(pats: list[str], tool: str) -> None:
        for pat in pats:
            if pat and pat not in seen:
                seen.add(pat)
                results.append((pat, tool))

    add(_find_quoted_after(cmd, 0, "grep -E"), "grep-E")
    add(_find_quoted_after(cmd, 0, "grep "), "grep")
    add(_sed_sub_pattern(cmd), "sed-sub")
    # sed/awk address: /pat/
    for needle, tool in (("sed ", "sed-addr"), ("awk ", "awk")):
        i = 0
        while True:
            j = cmd.find(needle, i)
            if j < 0:
                break
            k = cmd.find("/", j + len(needle))
            if k < 0:
                break
            m = k + 1
            chars: list[str] = []
            while m < len(cmd):
                if cmd[m] == "\\" and m + 1 < len(cmd):
                    chars.append(cmd[m : m + 2])
                    m += 2
                    continue
                if cmd[m] == "/":
                    break
                chars.append(cmd[m])
                m += 1
            pat = "".join(chars)
            if pat:
                add([pat], tool)
            i = m + 1
    add(_find_quoted_after(cmd, 0, " : "), "expr")
    return results


def _iter_testing_calls(source: str) -> list[tuple[int, str, str]]:
    """Yield (line_no, cmd, snippet) for testing \"...\" pentuples — linear."""
    out: list[tuple[int, str, str]] = []
    i = 0
    while True:
        j = source.find("testing", i)
        if j < 0:
            break
        k = _skip_ws(source, j + 7)
        fields: list[str] = []
        ok = True
        for _ in range(5):
            k = _skip_ws(source, k)
            if k >= len(source) or source[k] != '"':
                ok = False
                break
            val, k = _read_dq(source, k)
            if val is None:
                ok = False
                break
            fields.append(val)
        if ok and len(fields) == 5:
            line_no = source.count("\n", 0, j) + 1
            snippet = source[j:k][:500]
            out.append((line_no, fields[1], snippet))
            i = k
        else:
            i = j + 7
    return out


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

    for line_no, cmd, snippet in _iter_testing_calls(source):
        pairs = _extract_patterns_from_cmd(cmd)
        if not pairs:
            stats.skipped += 1
            continue
        for pat, _tool in pairs:
            rec = make_record(
                repo=repo,
                pattern=pat,
                flags="",
                dialect=dialect,
                call_kind="search",
                file=file,
                line=line_no,
                column=0,
                context_snippet=snippet,
            )
            if rec["regex_id"] not in seen_ids:
                seen_ids.add(rec["regex_id"])
                out.append(rec)
                stats.parsed += 1

    # Direct grep -E / sed on non-testing lines
    for line_no, line in enumerate(source.splitlines(), 1):
        if "testing" in line:
            continue
        for pat, _tool in _extract_patterns_from_cmd(line):
            rec = make_record(
                repo=repo,
                pattern=pat,
                flags="",
                dialect=dialect,
                call_kind="search",
                file=file,
                line=line_no,
                column=0,
                context_snippet=line[:500],
            )
            if rec["regex_id"] not in seen_ids:
                seen_ids.add(rec["regex_id"])
                out.append(rec)
                stats.parsed += 1

    for rec in out:
        rec["_parse_stats"] = stats.as_dict()
    return out
