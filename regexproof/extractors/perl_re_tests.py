"""Extract patterns from Perl core ``t/re`` testdata (Wave-3 P5 / #116).

Two passes:
1. Table pass: tab-delimited ``re_tests`` rows (``pat\\tstring\\ty/n/c/...``)
2. ``.t`` pass: ``qr/…/``, ``m/…/``, and ``=~ /…/`` delimited literals

Expected compile-failure rows (``c`` in the outcome field) are recorded with
``unencodable_reason=expected-compile-error`` so they never surface as
unclassified ``parse-error``. Bucketed parse stats: a=parsed, b=skipped,
c=errors.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from regexproof.extractors.record import make_record

# Upstream pin file count: 80 ``*.t`` + ``re_tests``.
EXPECTED_PERL_RE_FILES = 81
# Keep in sync with regexproof.batch.manifests.MAX_FILE_BYTES (#175/#365).
_DEFAULT_MAX_FILE_BYTES = 2_000_000

_CLOSE = {"{": "}", "(": ")", "[": "]", "<": ">"}


class ParseStats:
    __slots__ = ("parsed", "skipped", "errors")

    def __init__(self) -> None:
        self.parsed = 0
        self.skipped = 0
        self.errors = 0

    def as_dict(self) -> dict[str, int]:
        return {
            "a_parsed": self.parsed,
            "b_skipped": self.skipped,
            "c_errors": self.errors,
        }


def _read_delimited(s: str, start: int, open_ch: str) -> tuple[str | None, int, str]:
    """Read a perl-style delimited body starting after the opener.

    Returns ``(body, next_index, flags)`` or ``(None, start, "")`` on failure.
    """
    close = _CLOSE.get(open_ch, open_ch)
    paired = open_ch != close
    i = start
    depth = 1
    body: list[str] = []
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s):
            body.append(ch)
            body.append(s[i + 1])
            i += 2
            continue
        if paired and ch == open_ch:
            depth += 1
            body.append(ch)
            i += 1
            continue
        if ch == close:
            depth -= 1
            if depth == 0:
                i += 1
                flags_chars: list[str] = []
                while i < len(s) and s[i].isalpha():
                    flags_chars.append(s[i])
                    i += 1
                return "".join(body), i, "".join(flags_chars)
            body.append(ch)
            i += 1
            continue
        body.append(ch)
        i += 1
    return None, start, ""


def extract_perl_re_tests_table(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "perl",
) -> list[dict[str, Any]]:
    """Extract from ``t/re/re_tests`` tab-delimited table (after ``__END__``)."""
    stats = ParseStats()
    out: list[dict[str, Any]] = []
    if "__END__" in source:
        source = source.split("__END__", 1)[1]
    for line_no, line in enumerate(source.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            stats.skipped += 1
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            stats.skipped += 1
            continue
        pattern = parts[0]
        outcome = parts[2] if len(parts) >= 3 else ""
        if not pattern:
            stats.skipped += 1
            continue
        # Occasional rows store the pattern as /pat/ (with delimiters).
        if (
            len(pattern) >= 2
            and pattern[0] == "/"
            and pattern.endswith("/")
            and pattern.count("/") >= 2
        ):
            inner = pattern[1:-1]
            if inner:
                pattern = inner
        reason = None
        if "c" in outcome:
            reason = "expected-compile-error"
        try:
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
                    context_snippet=line[:500],
                    unencodable_reason=reason,
                )
            )
            stats.parsed += 1
        except Exception:  # noqa: BLE001
            stats.errors += 1
    for rec in out:
        rec["_parse_stats"] = stats.as_dict()
    return out


def extract_perl_t_file(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "perl",
) -> list[dict[str, Any]]:
    """Extract ``qr…``, ``m…``, and ``=~ /…/`` literals from a ``.t`` file."""
    stats = ParseStats()
    out: list[dict[str, Any]] = []
    i = 0
    n = len(source)
    while i < n:
        # Skip comments / POD lightly: full-line # and =pod…=cut.
        if source.startswith("=pod", i) or source.startswith("=head", i):
            end = source.find("=cut", i)
            if end < 0:
                stats.skipped += 1
                break
            i = end + 4
            continue
        # qr DELIM … DELIM flags
        if source.startswith("qr", i) and i + 2 < n and not (
            source[i + 2].isalnum() or source[i + 2] == "_"
        ):
            j = i + 2
            while j < n and source[j].isspace():
                j += 1
            if j < n and not source[j].isalnum() and source[j] not in "_":
                open_ch = source[j]
                body, nxt, flags = _read_delimited(source, j + 1, open_ch)
                if body is None:
                    stats.errors += 1
                    i = j + 1
                    continue
                reason = None
                if not body:
                    reason = "empty-pattern"
                elif "$" in body and ("{" in body or body.count("$") > 0):
                    # Interpolation inside qr"$pat" / qr/$var/ — mark dynamic.
                    if open_ch in "\"'" or "$" in body:
                        # Single-quoted qr'…' is literal; double / bare may interpolate.
                        if open_ch != "'":
                            # Heuristic: $ followed by ident → composite.
                            for k, ch in enumerate(body):
                                if ch == "$" and k + 1 < len(body) and (
                                    body[k + 1].isalpha() or body[k + 1] == "{"
                                ):
                                    reason = "composite-pattern"
                                    break
                line_no = source.count("\n", 0, i) + 1
                out.append(
                    make_record(
                        repo=repo,
                        pattern=body,
                        flags="".join(c for c in "imsx" if c in flags),
                        dialect=dialect,
                        call_kind="search",
                        file=file,
                        line=line_no,
                        column=0,
                        context_snippet=source[i:nxt][:500],
                        unencodable_reason=reason,
                    )
                )
                stats.parsed += 1
                i = nxt
                continue
        # m DELIM … DELIM (not mm, not method)
        if source.startswith("m", i) and i + 1 < n:
            prev = source[i - 1] if i > 0 else "\n"
            nxtc = source[i + 1]
            if (not prev.isalnum() and prev != "_") and not (
                nxtc.isalnum() or nxtc == "_"
            ):
                j = i + 1
                while j < n and source[j].isspace():
                    j += 1
                if j < n and not source[j].isalnum() and source[j] not in "_":
                    open_ch = source[j]
                    body, nxt, flags = _read_delimited(source, j + 1, open_ch)
                    if body is None:
                        stats.errors += 1
                        i = j + 1
                        continue
                    reason = None
                    if not body:
                        reason = "empty-pattern"
                    elif open_ch != "'" and "$" in body:
                        for k, ch in enumerate(body):
                            if ch == "$" and k + 1 < len(body) and (
                                body[k + 1].isalpha() or body[k + 1] == "{"
                            ):
                                reason = "composite-pattern"
                                break
                    line_no = source.count("\n", 0, i) + 1
                    out.append(
                        make_record(
                            repo=repo,
                            pattern=body,
                            flags="".join(c for c in "imsx" if c in flags),
                            dialect=dialect,
                            call_kind="search",
                            file=file,
                            line=line_no,
                            column=0,
                            context_snippet=source[i:nxt][:500],
                            unencodable_reason=reason,
                        )
                    )
                    stats.parsed += 1
                    i = nxt
                    continue
        # =~ /pat/flags or !~ /pat/flags
        if source.startswith("=~", i) or source.startswith("!~", i):
            j = i + 2
            while j < n and source[j].isspace():
                j += 1
            if j < n and source[j] == "/":
                body, nxt, flags = _read_delimited(source, j + 1, "/")
                if body is None:
                    stats.errors += 1
                    i = j + 1
                    continue
                reason = None
                if not body:
                    reason = "empty-pattern"
                line_no = source.count("\n", 0, i) + 1
                out.append(
                    make_record(
                        repo=repo,
                        pattern=body,
                        flags="".join(c for c in "imsx" if c in flags),
                        dialect=dialect,
                        call_kind="search",
                        file=file,
                        line=line_no,
                        column=0,
                        context_snippet=source[i:nxt][:500],
                        unencodable_reason=reason,
                    )
                )
                stats.parsed += 1
                i = nxt
                continue
        i += 1
    for rec in out:
        rec["_parse_stats"] = stats.as_dict()
    return out


def extract_perl_re_file(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "perl",
) -> list[dict[str, Any]]:
    """Dispatch a single file under ``t/re``."""
    name = Path(file).name
    if name == "re_tests":
        return extract_perl_re_tests_table(
            source, repo=repo, file=file, dialect=dialect
        )
    if name.endswith(".t"):
        return extract_perl_t_file(source, repo=repo, file=file, dialect=dialect)
    return []


def extract_perl_re_tree(
    root: Path,
    *,
    repo: str = "Perl/perl5",
    file_prefix: str = "t/re",
    expected_files: int | None = EXPECTED_PERL_RE_FILES,
    dialect: str = "perl",
    max_file_bytes: int = _DEFAULT_MAX_FILE_BYTES,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Walk ``t/re`` extracting ``*.t`` + ``re_tests``; gate on expected count."""
    root = Path(root)
    if not root.exists():
        raise FileNotFoundError(f"perl t/re root missing: {root}")
    files = sorted(
        [p for p in root.glob("*.t") if p.is_file()]
        + ([root / "re_tests"] if (root / "re_tests").is_file() else [])
    )
    # Deduplicate while preserving sort order.
    seen: set[Path] = set()
    ordered: list[Path] = []
    for fp in files:
        if fp in seen:
            continue
        seen.add(fp)
        ordered.append(fp)
    out: list[dict[str, Any]] = []
    per_file: dict[str, int] = {}
    skipped_oversized = 0
    for fp in ordered:
        rel = f"{file_prefix}/{fp.name}"
        if fp.stat().st_size > max_file_bytes:
            skipped_oversized += 1
            continue
        src = fp.read_text(encoding="utf-8", errors="replace")
        recs = extract_perl_re_file(src, repo=repo, file=rel, dialect=dialect)
        per_file[rel] = len(recs)
        out.extend(recs)
    stats = {
        "files_seen": len(ordered),
        "expected_files": expected_files,
        "files_ok": expected_files is None or len(ordered) == expected_files,
        "records": len(out),
        "per_file_records": per_file,
        "files": [f"{file_prefix}/{fp.name}" for fp in ordered],
        "skipped_oversized": skipped_oversized,
    }
    return out, stats
