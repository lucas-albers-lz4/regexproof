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
        snippet = f"part={cur_part}; name={cur_name}" if cur_part or cur_name else line.strip()
        rec = make_record(
            repo=repo,
            pattern=pat,
            flags="i",
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
    s = s.strip()
    if len(s) < 2:
        return s if s else None
    q = s[0]
    if q not in "\"'":
        return s
    if not s.endswith(q):
        # Allow trailing YAML comment: 'pat' # note
        end = s.rfind(q, 1)
        if end <= 0:
            return None
        return s[1:end]
    return s[1:-1]
