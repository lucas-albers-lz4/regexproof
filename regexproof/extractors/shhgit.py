"""shhgit ``config.yaml`` signature extractor (Wave 3 / #114).

Extracts ``regex:`` entries from the signatures list.

``call_kind`` is always ``search``: upstream ``PatternSignature.Match`` uses
Go ``Regexp.Match`` / ``MatchString``, which are substring membership (not
``re.fullmatch``). Anchors in individual patterns (``^…$``) remain load-bearing.

Flags are always ``i``: upstream ``core/signatures.go`` gates pattern
signatures with ``syntax.Parse(..., syntax.FoldCase)`` (Wave-3 P1 fold).
Dialect ``re2`` (go ``regexp``).
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.compiler.normalize import normalize_inline_flags
from regexproof.extractors.record import make_record

_SIG_NAME = re.compile(r"^(\s*)-\s+part:\s*(.+?)\s*$")
_FIELD = re.compile(r"^(\s*)(name|match|regex)\s*:\s*(.*)$")


def extract_shhgit(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "re2",
) -> list[dict[str, Any]]:
    """Extract regex signature sites from shhgit ``config.yaml``."""
    lines = source.splitlines()
    out: list[dict[str, Any]] = []
    i = 0
    cur_part: str | None = None
    cur_name: str | None = None
    # Only emit regex: keys (match: is literal SimpleSignature).
    while i < len(lines):
        line = lines[i]
        m_part = _SIG_NAME.match(line)
        if m_part:
            cur_part = _unquote(m_part.group(2).strip()) or m_part.group(2).strip()
            cur_name = None
            i += 1
            continue
        m = _FIELD.match(line)
        if not m:
            i += 1
            continue
        key = m.group(2)
        rest = m.group(3).rstrip()
        line_no = i + 1
        if key == "name":
            cur_name = _unquote(rest.strip()) or rest.strip()
            i += 1
            continue
        if key == "match":
            # Literal signature — not a regex site.
            i += 1
            continue
        if key != "regex":
            i += 1
            continue
        pat = _unquote(rest.strip())
        if pat is None:
            pat = rest.strip()
        if not pat:
            i += 1
            continue
        # Strip surrounding quotes already handled; bare scalars OK.
        if (pat.startswith("'") and pat.endswith("'")) or (
            pat.startswith('"') and pat.endswith('"')
        ):
            pat = _unquote(pat) or pat
        # FoldCase → always i; also lift leading (?i)/(?is)/… so regex_id
        # matches the post-lift_inline pattern written to inventory.
        pat, flags = normalize_inline_flags(pat, "i")
        snippet = f"part={cur_part}; name={cur_name}" if cur_part or cur_name else line.strip()
        rec = make_record(
            repo=repo,
            pattern=pat,
            flags=flags,
            dialect=dialect,
            call_kind="search",
            file=file,
            line=line_no,
            column=0,
            context_snippet=snippet[:500],
        )
        if cur_name:
            rec["rule_name"] = cur_name
        if cur_part:
            rec["rule_part"] = cur_part
        out.append(rec)
        i += 1
    return out


def _unquote(s: str) -> str | None:
    """Decode a YAML single- or double-quoted scalar (yaml.Unmarshal rules)."""
    s = s.strip()
    # Allow trailing YAML comment after the closing quote.
    if not s:
        return None
    q = s[0]
    if q not in "\"'":
        # Bare / already-unquoted.
        return s.split(" #", 1)[0].rstrip() if " #" in s else s
    end = _closing_quote_index(s, q)
    if end < 0:
        return None
    inner = s[1:end]
    if q == "'":
        # Single-quoted: only '' → '
        return inner.replace("''", "'")
    # Double-quoted: YAML escape decode.
    return _yaml_double_unescape(inner)


def _closing_quote_index(s: str, q: str) -> int:
    """Index of closing quote matching *q*, respecting escapes / '' pairs."""
    i = 1
    n = len(s)
    while i < n:
        ch = s[i]
        if q == "'" and ch == "'":
            if i + 1 < n and s[i + 1] == "'":
                i += 2
                continue
            return i
        if q == '"':
            if ch == "\\" and i + 1 < n:
                i += 2
                continue
            if ch == '"':
                return i
        i += 1
    return -1


def _yaml_double_unescape(inner: str) -> str:
    out: list[str] = []
    i = 0
    n = len(inner)
    escapes = {
        "n": "\n",
        "t": "\t",
        "r": "\r",
        "\\": "\\",
        '"': '"',
        "/": "/",
        "0": "\0",
        "a": "\a",
        "b": "\b",
        "e": "\x1b",
        "f": "\f",
        "v": "\v",
        "N": "\u0085",
        "_": "\u00a0",
        "L": "\u2028",
        "P": "\u2029",
    }
    while i < n:
        if inner[i] != "\\" or i + 1 >= n:
            out.append(inner[i])
            i += 1
            continue
        nxt = inner[i + 1]
        if nxt in escapes:
            out.append(escapes[nxt])
            i += 2
            continue
        if nxt == "x" and i + 3 < n:
            try:
                out.append(chr(int(inner[i + 2 : i + 4], 16)))
                i += 4
                continue
            except ValueError:
                pass
        if nxt == "u" and i + 5 < n:
            try:
                out.append(chr(int(inner[i + 2 : i + 6], 16)))
                i += 6
                continue
            except ValueError:
                pass
        # Unknown escape: keep the escaped char (YAML drops the backslash).
        out.append(nxt)
        i += 2
    return "".join(out)
