"""YARA rule extractor: parse .yar/.yara for regex strings + modifiers.

Lowering (from sweep/corpus-wave2/yara-modifiers.md):
  - nocase → flag "i" (case-insensitive)
  - ascii / (default) → domain="ascii", single-byte mirror
  - wide → domain="wide", UTF-16LE NUL-interleaved mirror
  - ascii wide → emit TWO records (one per domain variant)
  - fullword → alnum token bounds (NOT \\b); encoded as flag "W"
  - unknown modifiers → reject (unencodable_reason="unsupported-modifier")
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

_RULE_RE = re.compile(
    r"rule\s+(\w+)\s*(?::\s*[\w\s]+)?\s*\{", re.MULTILINE
)

_STRINGS_BLOCK_RE = re.compile(
    r"strings\s*:(.*?)(?=condition\s*:|(?:rule\s+\w)|\Z)",
    re.DOTALL,
)

_STRING_DEF_RE = re.compile(
    r"""
    (?P<var>\$\w+)\s*=\s*
    (?:
      /(?P<regex>(?:[^/\\]|\\.)*)/ (?P<regex_mods>[ism]*)
    |
      "(?P<text>(?:[^"\\]|\\.)*)"
    )
    \s*(?P<modifiers>[^\n$]*)
    """,
    re.VERBOSE,
)

KNOWN_MODIFIERS = frozenset({
    "ascii", "wide", "nocase", "fullword",
    "private", "xor", "base64", "base64wide",
})

UNSUPPORTED_MODIFIERS = frozenset({
    "xor", "base64", "base64wide",
})


def _parse_modifiers(mod_str: str) -> set[str]:
    cleaned = re.sub(r"/\*.*?\*/", "", mod_str, flags=re.DOTALL)
    cleaned = re.sub(r"/\*.*$", "", cleaned)  # unclosed block comment
    cleaned = re.sub(r"\*/", "", cleaned)
    cleaned = re.sub(r"//.*$", "", cleaned)
    tokens = cleaned.strip().split()
    # Keep only identifier-shaped modifier tokens (drop comment debris).
    return {t for t in tokens if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", t)}


def _domains_from_modifiers(mods: set[str]) -> list[str]:
    has_ascii = "ascii" in mods
    has_wide = "wide" in mods
    if has_ascii and has_wide:
        return ["ascii", "wide"]
    if has_wide and not has_ascii:
        return ["wide"]
    return ["ascii"]


def extract_yara(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """Extract regex sites from YARA rule source text.

    Returns one record per (pattern, domain) variant. Emits per-variant
    records when both ascii+wide are specified.
    """
    records: list[dict[str, Any]] = []
    lines = source.split("\n")

    for rule_m in _RULE_RE.finditer(source):
        rule_start = rule_m.start()
        rule_body_start = rule_m.end()

        brace_depth = 1
        pos = rule_body_start
        while pos < len(source) and brace_depth > 0:
            if source[pos] == "{":
                brace_depth += 1
            elif source[pos] == "}":
                brace_depth -= 1
            pos += 1
        rule_body = source[rule_body_start:pos - 1]

        strings_m = _STRINGS_BLOCK_RE.search(rule_body)
        if not strings_m:
            continue

        strings_block = strings_m.group(1)
        strings_offset = rule_body_start + strings_m.start(1)

        for def_m in _STRING_DEF_RE.finditer(strings_block):
            is_regex = def_m.group("regex") is not None
            if is_regex:
                pattern = def_m.group("regex")
                regex_inline_mods = def_m.group("regex_mods") or ""
            else:
                raw_text = def_m.group("text")
                if not raw_text:
                    continue
                pattern = re.escape(raw_text)
                regex_inline_mods = ""

            mod_str = def_m.group("modifiers") or ""
            mods = _parse_modifiers(mod_str)

            unknown = mods - KNOWN_MODIFIERS - {""}
            unsupported = mods & UNSUPPORTED_MODIFIERS

            abs_offset = strings_offset + def_m.start()
            line_no = source[:abs_offset].count("\n") + 1
            col = abs_offset - source.rfind("\n", 0, abs_offset) - 1

            flags = regex_inline_mods
            if "nocase" in mods:
                flags = flags + "i" if "i" not in flags else flags

            fullword = "fullword" in mods
            if fullword:
                flags = flags + "W" if "W" not in flags else flags

            unencodable: str | None = None
            if unknown or unsupported:
                bad = sorted(unknown | unsupported)
                unencodable = f"unsupported-modifier:{','.join(bad)}"

            domains = _domains_from_modifiers(mods)
            snippet = _context_snippet(lines, line_no)

            for domain in domains:
                records.append(
                    make_record(
                        repo=repo,
                        pattern=pattern,
                        flags=flags,
                        dialect="yara",
                        call_kind="search",
                        file=file,
                        line=line_no,
                        column=col,
                        domain=domain,
                        context_snippet=snippet,
                        unencodable_reason=unencodable,
                    )
                )

    return records


def _context_snippet(lines: list[str], line_no: int) -> str:
    start = max(0, line_no - 2)
    end = min(len(lines), line_no + 1)
    return "\n".join(lines[start:end])
