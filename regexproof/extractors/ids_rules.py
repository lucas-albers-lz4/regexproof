"""IDS rule-file extractor (Suricata / Snort / Emerging Threats).

Extracts ``pcre:"/pattern/flags"`` (and ``pcre:'…'``) directives from
``.rules`` files. Skipped file types: non-``.rules`` sources. Commented-out
alerts (leading ``#``) are skipped.
"""

from __future__ import annotations

import re
from typing import Any

from regexproof.extractors.record import make_record

# pcre:"/body/flags";  or pcre:"body";  Suricata also allows pcre:"/body/ismx"
_PCRE_DQ = re.compile(
    r'\bpcre\s*:\s*"(?P<body>(?:\\.|[^"\\])*)"',
    re.IGNORECASE,
)
_PCRE_SQ = re.compile(
    r"\bpcre\s*:\s*'(?P<body>(?:\\.|[^'\\])*)'",
    re.IGNORECASE,
)
_SID = re.compile(r"\bsid\s*:\s*(?P<sid>\d+)\s*;", re.IGNORECASE)


def extract_ids_rules(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "pcre",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for i, line in enumerate(source.splitlines(), 1):
        stripped = line.lstrip()
        if not stripped or stripped.startswith("#"):
            continue
        for rx in (_PCRE_DQ, _PCRE_SQ):
            for m in rx.finditer(line):
                pattern, flags = _split_pcre_body(m.group("body"))
                if not pattern:
                    continue
                sid_m = _SID.search(line)
                ctx = f"sid:{sid_m.group('sid')}" if sid_m else stripped[:200]
                out.append(
                    make_record(
                        repo=repo,
                        pattern=pattern,
                        flags=flags,
                        dialect=dialect,
                        call_kind="search",
                        file=file,
                        line=i,
                        column=m.start(),
                        context_snippet=ctx[:500],
                    )
                )
    return out


def _split_pcre_body(body: str) -> tuple[str, str]:
    """Split Suricata ``/pattern/flags`` or bare pattern into (pattern, flags)."""
    body = body.strip()
    if len(body) >= 2 and body[0] == "/":
        # Find closing / — flags follow.
        i = 1
        while i < len(body):
            if body[i] == "\\" and i + 1 < len(body):
                i += 2
                continue
            if body[i] == "/":
                pattern = body[1:i]
                flags = body[i + 1 :]
                # Suricata flag letters → our normalize alphabet subset.
                flags = "".join(c for c in flags.lower() if c in "imsx")
                return pattern, flags
            i += 1
    return body, ""
