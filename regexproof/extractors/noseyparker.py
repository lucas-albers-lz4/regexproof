"""Nosey Parker builtin YAML rule extractor (Wave 3 / #114).

Parses ``pattern:`` keys (quoted or ``|`` block scalars) from Nosey Parker
rule files. Applies ``strip_verbose_x`` at extraction time; lifted flags are
merged into the record (``x`` dropped — residual ``x`` must not remain).

Dialect ``re2`` is a declared approximation of the rust ``regex`` crate used
by Nosey Parker (see ``sweep/corpus-wave3/noseyparker-dialect.md``).
``call_kind`` is ``search`` (secret scanners match substrings in content).
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.compiler.xflag_strip import strip_verbose_x
from regexproof.extractors.record import make_record

_RULE_START = re.compile(r"^(\s*)-\s+name:\s*(.+?)\s*$")
_FIELD = re.compile(r"^(\s*)(id|pattern|categories)\s*:\s*(.*)$")


def extract_noseyparker(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "re2",
) -> list[dict[str, Any]]:
    """Extract regex sites from a Nosey Parker builtin rules YAML file."""
    lines = source.splitlines()
    out: list[dict[str, Any]] = []
    i = 0
    cur_name: str | None = None
    cur_id: str | None = None
    cur_categories: str = ""
    rule_indent = 0

    while i < len(lines):
        line = lines[i]
        m_start = _RULE_START.match(line)
        if m_start:
            cur_name = _unquote_scalar(m_start.group(2).strip()) or m_start.group(2).strip()
            cur_id = None
            cur_categories = ""
            rule_indent = len(m_start.group(1))
            i += 1
            continue

        m = _FIELD.match(line)
        if not m:
            i += 1
            continue
        indent = len(m.group(1))
        if indent <= rule_indent and not line.lstrip().startswith("-"):
            # Sibling of the rule list (or top-level key) — do not attribute
            # to the previous rule's metadata.
            i += 1
            continue
        key = m.group(2)
        rest = m.group(3).rstrip()
        line_no = i + 1

        if key == "id":
            cur_id = _unquote_scalar(rest.strip()) or rest.strip()
            i += 1
            continue
        if key == "categories":
            cur_categories = rest.strip()
            if rest.strip() in ("", "|", ">", "|-", ">-"):
                cats, i, _ = _read_block(lines, i + 1, indent)
                cur_categories = (cats or "").replace("\n", ",")
            else:
                i += 1
            continue
        if key != "pattern":
            i += 1
            continue

        pat, i, reason = _parse_value(lines, i, rest, indent)
        if not pat and reason:
            continue
        if not pat:
            continue
        stripped, lifted = strip_verbose_x(pat)
        # Drop residual x; keep other lifted flags (i/m/s). ``s`` is rejected
        # fail-closed later in compile_re2 (s-flag).
        flag_set = set(lifted) - {"x"}
        flags = "".join(sorted(flag_set))
        snippet_parts = []
        if cur_id:
            snippet_parts.append(f"id={cur_id}")
        if cur_name:
            snippet_parts.append(f"name={cur_name}")
        if cur_categories:
            snippet_parts.append(f"categories={cur_categories}")
        snippet = "; ".join(snippet_parts) or line.strip()
        rec = make_record(
            repo=repo,
            pattern=stripped,
            flags=flags,
            dialect=dialect,
            call_kind="search",
            file=file,
            line=line_no,
            column=0,
            context_snippet=snippet[:500],
            unencodable_reason=reason,
        )
        if cur_id:
            rec["rule_id"] = cur_id
        if cur_name:
            rec["rule_name"] = cur_name
        out.append(rec)
    return out


def _parse_value(
    lines: list[str], idx: int, rest: str, key_indent: int
) -> tuple[str | None, int, str | None]:
    rest = rest.strip()
    if rest in ("|", ">", "|-", ">-", "|+", ">+"):
        return _read_block(lines, idx + 1, key_indent)
    if rest.startswith('"') or rest.startswith("'"):
        pat = _unquote_scalar(rest)
        if pat is None:
            return None, idx + 1, "parse-error"
        return pat, idx + 1, None
    if rest == "":
        return None, idx + 1, "parse-error"
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


def _unquote_scalar(s: str) -> str | None:
    s = s.strip()
    if len(s) < 2:
        return s if s else None
    q = s[0]
    if q not in "\"'":
        return s
    # Trailing comment after quoted scalar: 'pat' # note
    end = s.rfind(q, 1)
    if end <= 0:
        return None
    inner = s[1:end]
    if q == "'":
        return inner.replace("''", "'")
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
