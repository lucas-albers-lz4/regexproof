"""PCRE2 ``testdata/testinput*`` full-format pattern extractor.

Handles the pcre2test input format:
- Multiple delimiters (any non-alphanumeric ASCII character)
- Multi-line continuations (pattern spans lines until closing delimiter)
- Modifier lists after closing delimiter (comma-separated or flag chars)
- ``#`` command lines (``#pattern``, ``#subject``, ``#perltest``, etc.)
- Bucketed parse issues: a=parsed, b=skipped/command, c=parse-error
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

_PCRE2_FLAGS = frozenset("imsx")
_PCRE2_MODIFIERS = frozenset({
    "caseless", "multiline", "dotall", "extended", "anchored",
    "dollar_endonly", "ungreedy", "dupnames", "utf", "ucp",
    "no_auto_capture", "no_auto_possess", "no_start_optimize",
    "alt_bsux", "allow_empty_class", "auto_callout",
    "firstline", "match_unset_backref", "never_backslash_c",
    "never_ucp", "never_utf", "no_dotstar_anchor",
})
_COMMAND_RE = re.compile(r"^#\s*\w")
_DELIMITERS = set(
    c for c in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    if not c.isalnum()
)


def _closing_delim(opening: str) -> str:
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    return pairs.get(opening, opening)


def _parse_modifiers(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    if "," in text:
        parts = [p.strip().lower() for p in text.split(",")]
        flags = []
        for p in parts:
            if p in ("caseless", "i"):
                flags.append("i")
            elif p in ("multiline", "m"):
                flags.append("m")
            elif p in ("dotall", "s"):
                flags.append("s")
            elif p in ("extended", "x"):
                flags.append("x")
        return "".join(sorted(set(flags)))
    flags = []
    for c in text.lower():
        if c in _PCRE2_FLAGS:
            flags.append(c)
        elif c.isalpha():
            continue
        else:
            break
    return "".join(sorted(set(flags)))


class ParseStats:
    __slots__ = ("errors", "parsed", "skipped")

    def __init__(self) -> None:
        self.parsed = 0
        self.skipped = 0
        self.errors = 0

    def as_dict(self) -> dict[str, int]:
        return {"a_parsed": self.parsed, "b_skipped": self.skipped, "c_errors": self.errors}


def extract_pcre2_testdata(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "pcre",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    lines = source.splitlines()
    stats = ParseStats()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("#"):
            if len(stripped) > 1 and stripped[1] == " ":
                stats.skipped += 1
                i += 1
                continue
            has_closing_hash = "#" in stripped[1:]
            if not has_closing_hash:
                if _COMMAND_RE.match(stripped):
                    stats.skipped += 1
                i += 1
                continue

        first_char = stripped[0]
        if first_char.isalnum() or first_char.isspace():
            i += 1
            continue

        if first_char not in _DELIMITERS:
            i += 1
            continue

        opening = first_char
        closing = _closing_delim(opening)
        line_no = i + 1

        body_start = stripped.find(opening) + 1
        body_chars: list[str] = []
        rest = stripped[body_start:]
        found_close = False

        j = 0
        while j < len(rest):
            if rest[j] == "\\" and j + 1 < len(rest):
                body_chars.append(rest[j])
                body_chars.append(rest[j + 1])
                j += 2
                continue
            if rest[j] == closing:
                found_close = True
                modifier_text = rest[j + 1:]
                break
            body_chars.append(rest[j])
            j += 1

        if not found_close:
            i += 1
            while i < len(lines) and not found_close:
                cont = lines[i]
                body_chars.append("\n")
                k = 0
                while k < len(cont):
                    if cont[k] == "\\" and k + 1 < len(cont):
                        body_chars.append(cont[k])
                        body_chars.append(cont[k + 1])
                        k += 2
                        continue
                    if cont[k] == closing:
                        found_close = True
                        modifier_text = cont[k + 1:]
                        break
                    body_chars.append(cont[k])
                    k += 1
                i += 1

        if not found_close:
            stats.errors += 1
            i += 1
            continue

        pattern = "".join(body_chars)
        if not pattern:
            stats.skipped += 1
            i = max(i + 1, line_no + 1)
            continue

        try:
            flags = _parse_modifiers(modifier_text)
        except Exception:
            flags = ""
            stats.errors += 1

        context = lines[line_no - 1][:500] if line_no <= len(lines) else ""
        out.append(
            make_record(
                repo=repo,
                pattern=pattern,
                flags=flags,
                dialect=dialect,
                call_kind="search",
                file=file,
                line=line_no,
                column=0,
                context_snippet=context,
            )
        )
        stats.parsed += 1

        i = max(i + 1, line_no + 1)

    for rec in out:
        rec["_parse_stats"] = stats.as_dict()
    return out
