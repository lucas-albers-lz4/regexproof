"""RE2 upstream testdata extractor (AT&T testregex-style format).

Handles:
- Tab-delimited rows: ``type\\tpattern\\tstring\\texpected``
- Type field: E=extended, B=basic, L=literal (and combinations)
- ``#`` comment lines, ``:`` directive lines
- Bucketed parse issues: a=parsed, b=skipped, c=parse-error
"""

from __future__ import annotations

from typing import Any

from regexproof.extractors.record import make_record

_TYPE_TO_CALL_KIND = {
    "E": "search",
    "B": "search",
    "L": "search",
}


class ParseStats:
    __slots__ = ("errors", "parsed", "skipped")

    def __init__(self) -> None:
        self.parsed = 0
        self.skipped = 0
        self.errors = 0

    def as_dict(self) -> dict[str, int]:
        return {"a_parsed": self.parsed, "b_skipped": self.skipped, "c_errors": self.errors}


def extract_re2_testdata(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "re2",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    stats = ParseStats()

    for line_no, line in enumerate(source.splitlines(), 1):
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.startswith("#"):
            stats.skipped += 1
            continue

        if stripped.startswith(":"):
            stats.skipped += 1
            continue

        parts = line.split("\t")
        if len(parts) < 2:
            stats.skipped += 1
            continue

        type_field = parts[0].strip()
        pattern = parts[1]

        if not type_field or not any(c in type_field.upper() for c in "EBL"):
            stats.skipped += 1
            continue

        if not pattern:
            stats.skipped += 1
            continue

        primary_type = "E"
        for c in type_field.upper():
            if c in _TYPE_TO_CALL_KIND:
                primary_type = c
                break

        call_kind = _TYPE_TO_CALL_KIND.get(primary_type, "search")

        unencodable = None
        if primary_type == "L":
            unencodable = None
        if primary_type == "B":
            pass

        try:
            out.append(
                make_record(
                    repo=repo,
                    pattern=pattern,
                    flags="",
                    dialect=dialect,
                    call_kind=call_kind,
                    file=file,
                    line=line_no,
                    column=0,
                    context_snippet=line[:500],
                    unencodable_reason=unencodable,
                )
            )
            stats.parsed += 1
        except Exception:
            stats.errors += 1

    for rec in out:
        rec["_parse_stats"] = stats.as_dict()
    return out
