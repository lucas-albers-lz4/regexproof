"""Rule-file extractor scaffold (gitleaks/trufflehog-style TOML/YAML)."""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

try:
    import tomllib
except ModuleNotFoundError:  # py<3.11
    import tomli as tomllib  # type: ignore


_YAML_REGEX = re.compile(
    r"^\s*(?:regex|pattern)\s*:\s*[\"']?(?P<pat>.+?)[\"']?\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def extract_rule_file(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "re2",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    if file.endswith(".toml") or source.lstrip().startswith("[[") or "regex =" in source:
        return _extract_toml(source, repo=repo, file=file, dialect=dialect)
    for m in _YAML_REGEX.finditer(source):
        line_no = source.count("\n", 0, m.start()) + 1
        out.append(
            make_record(
                repo=repo,
                pattern=m.group("pat"),
                flags="",
                dialect=dialect,
                call_kind="search",
                file=file,
                line=line_no,
                column=0,
                context_snippet=m.group(0).strip()[:500],
            )
        )
    return out


def _extract_toml(source: str, *, repo: str, file: str, dialect: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    try:
        data = tomllib.loads(source)
    except Exception:  # noqa: BLE001
        # Fallback line scan — never treat concatenation as a literal pattern.
        for i, line in enumerate(source.splitlines(), 1):
            if not re.search(r"regex\s*=", line):
                continue
            rhs = line.split("=", 1)[1]
            # Dynamic / concatenated RHS (e.g. "compos" + "ite") → composite.
            if "+" in rhs or not re.search(
                r'^\s*(?:\'\'\'[\s\S]*\'\'\'|"""[\s\S]*"""|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')\s*$',
                rhs.strip(),
            ):
                out.append(
                    make_record(
                        repo=repo,
                        pattern="",
                        flags="",
                        dialect=dialect,
                        call_kind="search",
                        file=file,
                        line=i,
                        column=0,
                        context_snippet=line.strip()[:500],
                        unencodable_reason="composite-pattern",
                    )
                )
                continue
            m = re.search(r'regex\s*=\s*"(?P<p>(?:\\.|[^"\\])*)"', line)
            if not m:
                out.append(
                    make_record(
                        repo=repo,
                        pattern="",
                        flags="",
                        dialect=dialect,
                        call_kind="search",
                        file=file,
                        line=i,
                        column=0,
                        context_snippet=line.strip()[:500],
                        unencodable_reason="composite-pattern",
                    )
                )
                continue
            out.append(
                make_record(
                    repo=repo,
                    pattern=bytes(m.group("p"), "utf-8").decode("unicode_escape"),
                    flags="",
                    dialect=dialect,
                    call_kind="search",
                    file=file,
                    line=i,
                    column=0,
                    context_snippet=line.strip()[:500],
                )
            )
        return out

    rules = data.get("rules") or data.get("Rules") or []
    if isinstance(data, dict):
        # gitleaks: [[rules]]
        pass
    for idx, rule in enumerate(rules):
        if not isinstance(rule, dict):
            continue
        pattern = rule.get("regex") or rule.get("pattern")
        if not pattern:
            continue
        # Approximate line via search
        line_no = 1
        for i, line in enumerate(source.splitlines(), 1):
            if pattern[:20] in line or "regex" in line:
                line_no = i
                break
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
                context_snippet=str(rule.get("id", f"rule-{idx}"))[:500],
            )
        )
    return out
