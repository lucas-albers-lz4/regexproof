"""Semgrep-specific YAML extractor — only true regex sites.

Extracts:
  - ``pattern-regex:`` (quoted, bare, or block scalar ``|`` / ``>``)
  - ``metavariable-regex:`` map values (quoted / bare / block)

Ignores semgrep code-pattern language under ``pattern:`` / ``patterns:``
metavariable templates (``$X``, ``...``). Nested ``pattern-either`` /
``pattern-inside`` / ``patterns`` lists are walked by scanning every line
for the regex keys above (structure-agnostic, deterministic).
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

_REGEX_KEY = re.compile(
    r"^(?P<indent>\s*)(?:-\s*)?(?P<key>pattern-regex|metavariable-regex)\s*:\s*"
    r"(?P<rest>.*)$"
)
_META_ENTRY = re.compile(
    r"^(?P<indent>\s*)(?P<name>\$?[A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?P<rest>.*)$"
)


def extract_semgrep_yaml(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "py_re",
) -> list[dict[str, Any]]:
    """Extract regex sites from a semgrep rule YAML file."""
    lines = source.splitlines()
    out: list[dict[str, Any]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _REGEX_KEY.match(line)
        if not m:
            i += 1
            continue
        key = m.group("key")
        rest = m.group("rest").rstrip()
        line_no = i + 1
        indent = len(m.group("indent"))

        if key == "metavariable-regex" and (rest == "" or rest == "|" or rest == ">"):
            # Mapping form:
            # metavariable-regex:
            #   $VAR: "regex"
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip() or nxt.strip().startswith("#"):
                    i += 1
                    continue
                leading = len(nxt) - len(nxt.lstrip(" "))
                if leading <= indent and nxt.lstrip().startswith("-"):
                    break
                if leading <= indent and not nxt.lstrip().startswith("-"):
                    # dedent to sibling key
                    if not nxt.lstrip().startswith("$") and ":" in nxt.lstrip():
                        break
                em = _META_ENTRY.match(nxt)
                if not em or leading <= indent:
                    break
                name = em.group("name")
                erest = em.group("rest").rstrip()
                pat, consumed, reason = _parse_value(lines, i, erest, leading)
                i = consumed
                if not pat:
                    # Empty / unreadable metavariable body — skip (not a regex site).
                    continue
                out.append(
                    _rec(
                        repo=repo,
                        file=file,
                        line=line_no,
                        pattern=pat,
                        dialect=dialect,
                        snippet=f"metavariable-regex:{name}",
                        reason=reason,
                    )
                )
            continue

        pat, consumed, reason = _parse_value(lines, i, rest, indent)
        i = consumed
        if not pat:
            continue
        out.append(
            _rec(
                repo=repo,
                file=file,
                line=line_no,
                pattern=pat,
                dialect=dialect,
                snippet=line.strip()[:500],
                reason=reason,
            )
        )
    return out


def _parse_value(
    lines: list[str], idx: int, rest: str, key_indent: int
) -> tuple[str | None, int, str | None]:
    """Return (pattern, next_index, unencodable_reason)."""
    rest = rest.strip()
    if rest in ("|", ">", "|-", ">-", "|+", ">+"):
        return _read_block(lines, idx + 1, key_indent)
    if rest.startswith('"') or rest.startswith("'"):
        pat = _unquote(rest)
        if pat is None:
            return None, idx + 1, "parse-error"
        return pat, idx + 1, None
    if rest == "":
        return None, idx + 1, "parse-error"
    # bare scalar
    return rest, idx + 1, None


def _read_block(
    lines: list[str], start: int, key_indent: int
) -> tuple[str | None, int, str | None]:
    raw: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            raw.append(line)
            i += 1
            continue
        leading = len(line) - len(line.lstrip(" "))
        if leading <= key_indent:
            break
        raw.append(line)
        i += 1
    nonempty = [ln for ln in raw if ln.strip()]
    if not nonempty:
        return None, i, "parse-error"
    base = min(len(ln) - len(ln.lstrip(" ")) for ln in nonempty)
    body = [(ln[base:] if ln.strip() else "") for ln in raw]
    while body and body[-1] == "":
        body.pop()
    pat = "\n".join(body)
    if not pat:
        return None, i, "parse-error"
    return pat, i, None


def _unquote(s: str) -> str | None:
    s = s.strip()
    if len(s) < 2:
        return None
    q = s[0]
    if q not in "\"'":
        return s
    if not s.endswith(q):
        return None
    inner = s[1:-1]
    if q == "'":
        return inner
    out: list[str] = []
    i = 0
    while i < len(inner):
        if inner[i] == "\\" and i + 1 < len(inner):
            nxt = inner[i + 1]
            escapes = {"n": "\n", "t": "\t", "r": "\r", "\\": "\\", '"': '"'}
            out.append(escapes.get(nxt, nxt))
            i += 2
            continue
        out.append(inner[i])
        i += 1
    return "".join(out)


def _rec(
    *,
    repo: str,
    file: str,
    line: int,
    pattern: str,
    dialect: str,
    snippet: str,
    reason: str | None,
) -> dict[str, Any]:
    kwargs: dict[str, Any] = dict(
        repo=repo,
        pattern=pattern,
        flags="",
        dialect=dialect,
        call_kind="search",
        file=file,
        line=line,
        column=0,
        context_snippet=snippet[:500],
    )
    if reason:
        kwargs["unencodable_reason"] = reason
        kwargs["pattern"] = pattern or ""
    return make_record(**kwargs)
