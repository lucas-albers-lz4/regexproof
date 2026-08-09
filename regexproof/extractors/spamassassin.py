"""SpamAssassin .cf extractor: body/header/uri/rawbody regex rules (Wave 3 / #113).

Parses:
  body NAME /pat/flags
  header NAME Header =~ /pat/flags
  uri NAME /pat/flags
  rawbody NAME /pat/flags

Also lightly supports ``m{…}`` / ``m#…#`` delimiters. Multi-line rules joined
when a line ends with ``\\``. ``#`` comments and empty lines are skipped.
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

_KIND_RE = re.compile(
    r"^(body|header|uri|rawbody)\s+(\S+)\s+(.+)$",
    re.DOTALL,
)
_FLAGS_RE = re.compile(r"^[imsx]*$")


def _join_continuations(source: str) -> list[tuple[int, str]]:
    """Yield (start_line, joined_text), joining trailing-backslash continuations."""
    out: list[tuple[int, str]] = []
    buf: list[str] = []
    start: int | None = None
    for i, line in enumerate(source.splitlines(), 1):
        raw = line.rstrip("\n")
        # Strip full-line comments / blanks only when not mid-continuation.
        if not buf:
            stripped = raw.strip()
            if not stripped or stripped.startswith("#"):
                continue
            start = i
        if raw.endswith("\\"):
            buf.append(raw[:-1].rstrip())
            continue
        buf.append(raw)
        assert start is not None
        out.append((start, " ".join(buf)))
        buf = []
        start = None
    if buf and start is not None:
        out.append((start, " ".join(buf)))
    return out


def _extract_delimited(rest: str) -> tuple[str, str] | None:
    """Parse ``/pat/flags``, ``m{pat}flags``, or ``m#pat#flags`` from *rest*."""
    s = rest.lstrip()
    if not s:
        return None
    if s.startswith("m") and len(s) >= 2 and s[1] not in ("/",) and not s[1].isalnum():
        # m{…} / m#…# / m!…! etc.
        delim = s[1]
        close = {"{": "}", "(": ")", "[": "]"}.get(delim, delim)
        i = 2
        body: list[str] = []
        while i < len(s):
            ch = s[i]
            if ch == "\\" and i + 1 < len(s):
                body.append(ch)
                body.append(s[i + 1])
                i += 2
                continue
            if ch == close:
                flags = s[i + 1 :].strip()
                # Drop trailing junk (if-unset:, comments).
                flags = flags.split()[0] if flags.split() else ""
                if not _FLAGS_RE.fullmatch(flags):
                    flags = "".join(c for c in flags if c in "imsx")
                return "".join(body), flags
            body.append(ch)
            i += 1
        return None
    # Primary: /…/flags
    if s[0] != "/":
        return None
    i = 1
    body_chars: list[str] = []
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s):
            body_chars.append(ch)
            body_chars.append(s[i + 1])
            i += 2
            continue
        if ch == "/":
            flags = s[i + 1 :].strip()
            flags = flags.split()[0] if flags.split() else ""
            if not _FLAGS_RE.fullmatch(flags):
                flags = "".join(c for c in flags if c in "imsx")
            return "".join(body_chars), flags
        body_chars.append(ch)
        i += 1
    return None


def _pattern_from_rule(kind: str, rest: str) -> tuple[str, str] | None:
    payload = rest.strip()
    if kind == "header":
        # header NAME Header =~ /pat/  or  header NAME exists:Foo
        m = re.search(r"(=~|!~)\s*", payload)
        if not m:
            return None
        return _extract_delimited(payload[m.end() :])
    # body/uri/rawbody: skip eval: forms
    if payload.startswith("eval:"):
        return None
    return _extract_delimited(payload)


def extract_spamassassin(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """Extract perl-dialect regex sites from a SpamAssassin .cf file."""
    records: list[dict[str, Any]] = []
    for line_no, joined in _join_continuations(source):
        m = _KIND_RE.match(joined.strip())
        if not m:
            continue
        kind, name, rest = m.group(1), m.group(2), m.group(3)
        parsed = _pattern_from_rule(kind, rest)
        if parsed is None:
            continue
        pattern, flags = parsed
        if not pattern:
            continue
        flags = "".join(sorted(set(flags)))
        col = 0
        rec = make_record(
            repo=repo,
            pattern=pattern,
            flags=flags,
            dialect="perl",
            call_kind="search",
            file=file,
            line=line_no,
            column=col,
            context_snippet=joined[:500],
        )
        rec["rule_kind"] = kind
        rec["rule_name"] = name
        records.append(rec)
    return records
