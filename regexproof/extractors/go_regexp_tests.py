"""Extract patterns from Go stdlib ``src/regexp/*_test.go`` (Wave-3 P5 / #116).

Distinct from the trufflehog-oriented :func:`extract_go_regexp` (package-prefixed
``regexp.MustCompile`` only). This path covers:

1. ``MustCompile`` / ``Compile`` / POSIX variants (bare or ``regexp.``-prefixed)
2. Struct-literal first string fields (``FindTest``, ``parseTest``, …)
3. Backtick / quoted entries in ``[]string{…}`` compile tables (``goodRe``)

Dialect: ``re2``. Bucketed parse stats attached per file.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from regexproof.extractors.go_regexp import extract_go_regexp
from regexproof.extractors.record import make_record

# Keep in sync with regexproof.batch.manifests.MAX_FILE_BYTES (#175/#365).
_DEFAULT_MAX_FILE_BYTES = 2_000_000

# Upstream pin: 9 ``*_test.go`` files under ``src/regexp`` (incl. syntax/).
EXPECTED_GO_REGEXP_TEST_FILES = 9

_MUST = re.compile(
    r"(?:regexp\.)?(?:MustCompile|Compile|MustCompilePOSIX|CompilePOSIX)\(\s*"
    r"(?P<q>\"|`)(?P<body>(?:\\.|(?!\1).)*)(?P=q)\s*\)",
    re.DOTALL,
)

# Struct literal whose first field is a string: {`pat`, …} or {"pat", …}
_STRUCT_FIRST = re.compile(
    r"^\s*\{(?P<q>`|\"|)(?P<body>(?:\\.|(?!\1).)*)(?P=q)\s*,",
    re.MULTILINE,
)

# Standalone string entry inside a []string / composite literal.
_STRING_ENTRY = re.compile(
    r"^\s*(?P<q>`|\")(?P<body>(?:\\.|(?!\1).)*)(?P=q)\s*,?\s*(?://.*)?$",
    re.MULTILINE,
)


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


def _decode_go_string(raw: str, quote: str) -> str:
    if quote == "`":
        return raw
    try:
        return bytes(raw, "utf-8").decode("unicode_escape")
    except UnicodeDecodeError:
        return raw


# []string tables whose entries are expected parse failures in Go's own suite.
_INVALID_STRING_TABLES = frozenset({
    "invalidRegexps",
    "onlyPOSIX",  # invalid under Perl/RE2-style parse
})


def _preceding_ident(source: str, pos: int) -> str:
    """Return the identifier immediately before ``pos`` (skipping ``=`` / whitespace)."""
    i = pos - 1
    while i >= 0 and source[i].isspace():
        i -= 1
    if i >= 0 and source[i] == "=":
        i -= 1
        while i >= 0 and source[i].isspace():
            i -= 1
    end = i + 1
    while i >= 0 and (source[i].isalnum() or source[i] == "_"):
        i -= 1
    return source[i + 1 : end]


def extract_go_regexp_tests(
    source: str,
    *,
    repo: str,
    file: str,
    dialect: str = "re2",
) -> list[dict[str, Any]]:
    """Extract regex sites from a Go ``*_test.go`` source."""
    stats = ParseStats()
    out: list[dict[str, Any]] = []
    seen_sites: set[tuple[str, int, str]] = set()

    def _add(pattern: str, line_no: int, snippet: str, reason: str | None = None) -> None:
        key = (pattern, line_no, reason or "")
        if key in seen_sites:
            stats.skipped += 1
            return
        seen_sites.add(key)
        if pattern is None:
            stats.errors += 1
            return
        if reason is None:
            # Format-pass bucketing for constructs our re2 path rejects as
            # bare parse-error (Wave-3 P5 unclassified=0 gate).
            if r"\p{" in pattern or r"\P{" in pattern:
                reason = "unicode-prop"
            elif pattern.endswith("\\") and not pattern.endswith("\\\\"):
                reason = "trailing-backslash"
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
                context_snippet=snippet[:500],
                unencodable_reason=reason,
            )
        )
        stats.parsed += 1

    # 1) Compile call sites (bare + prefixed). Skip // comment prefixes.
    for m in _MUST.finditer(source):
        line_start = source.rfind("\n", 0, m.start()) + 1
        if "//" in source[line_start : m.start()]:
            stats.skipped += 1
            continue
        raw = m.group("body")
        pattern = _decode_go_string(raw, m.group("q"))
        line_no = source.count("\n", 0, m.start()) + 1
        reason = "empty-pattern" if pattern == "" else None
        # Extremely large generated patterns (badRe size bomb) — keep but tag.
        if len(pattern) > 10_000:
            reason = "pattern-too-long"
        _add(pattern, line_no, m.group(0), reason)

    # 2) Struct-literal first fields (FindTest / parseTest / stringError…).
    for m in _STRUCT_FIRST.finditer(source):
        line_start = source.rfind("\n", 0, m.start()) + 1
        if "//" in source[line_start : m.start()]:
            stats.skipped += 1
            continue
        # Skip non-string first fields (identifiers, composites, numbers).
        q = m.group("q")
        if not q:
            stats.skipped += 1
            continue
        raw = m.group("body")
        pattern = _decode_go_string(raw, q)
        line_no = source.count("\n", 0, m.start()) + 1
        reason = "empty-pattern" if pattern == "" else None
        if len(pattern) > 10_000:
            reason = "pattern-too-long"
        # Do NOT infer expected-compile-error from second-field text: FindTest
        # match inputs can contain "error"/"invalid"/… (Bugbot). Compile-failure
        # tables are covered via []stringError / named invalid []string blocks.
        _add(pattern, line_no, m.group(0), reason)

    # 3) Entries inside ``[]string{ … }`` / ``[]stringError{ … }`` tables.
    for block in re.finditer(r"\[\](?:stringError|string)\{", source):
        start = block.end()
        table_name = _preceding_ident(source, block.start())
        is_string_error = "stringError" in block.group(0)
        expected_bad = is_string_error or table_name in _INVALID_STRING_TABLES
        depth = 1
        i = start
        while i < len(source) and depth:
            ch = source[i]
            # Skip string/raw-string contents so `}` inside patterns does not
            # truncate the table (Bugbot).
            if ch in "\"`":
                q = ch
                i += 1
                while i < len(source):
                    if source[i] == "\\" and q == '"' and i + 1 < len(source):
                        i += 2
                        continue
                    if source[i] == q:
                        i += 1
                        break
                    i += 1
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            i += 1
        body = source[start : i - 1] if depth == 0 else ""
        if is_string_error:
            # stringError{ re: "…", err: "…" } / {`pat`, "err"} — first string only.
            for m in _STRUCT_FIRST.finditer(body):
                abs_pos = start + m.start()
                line_start = source.rfind("\n", 0, abs_pos) + 1
                if "//" in source[line_start:abs_pos]:
                    stats.skipped += 1
                    continue
                q = m.group("q")
                if not q:
                    stats.skipped += 1
                    continue
                pattern = _decode_go_string(m.group("body"), q)
                line_no = source.count("\n", 0, abs_pos) + 1
                _add(pattern, line_no, m.group(0), "expected-compile-error")
            continue
        for m in _STRING_ENTRY.finditer(body):
            # Offset line numbers relative to block start.
            abs_pos = start + m.start()
            line_start = source.rfind("\n", 0, abs_pos) + 1
            if "//" in source[line_start:abs_pos]:
                stats.skipped += 1
                continue
            pattern = _decode_go_string(m.group("body"), m.group("q"))
            line_no = source.count("\n", 0, abs_pos) + 1
            reason = "empty-pattern" if pattern == "" else None
            if expected_bad:
                reason = "expected-compile-error"
            elif len(pattern) > 10_000:
                reason = "pattern-too-long"
            _add(pattern, line_no, m.group(0), reason)

    # 4) Package-prefixed MustCompile via shared extractor (deduped).
    for rec in extract_go_regexp(source, repo=repo, file=file, dialect=dialect):
        key = (rec["pattern"], rec["line"], rec.get("unencodable_reason") or "")
        if key in seen_sites:
            continue
        seen_sites.add(key)
        out.append(rec)
        stats.parsed += 1

    for rec in out:
        rec["_parse_stats"] = stats.as_dict()
    return out


def extract_go_regexp_tests_tree(
    root: Path,
    *,
    repo: str = "golang/go",
    file_prefix: str = "src/regexp",
    expected_files: int | None = EXPECTED_GO_REGEXP_TEST_FILES,
    dialect: str = "re2",
    max_file_bytes: int = _DEFAULT_MAX_FILE_BYTES,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Walk ``src/regexp/**/*_test.go``; fail-closed when count mismatches."""
    root = Path(root)
    if not root.exists():
        raise FileNotFoundError(f"go regexp root missing: {root}")
    files = sorted(p for p in root.rglob("*_test.go") if p.is_file())
    out: list[dict[str, Any]] = []
    per_file: dict[str, int] = {}
    rels: list[str] = []
    skipped_oversized = 0
    for fp in files:
        try:
            rel = f"{file_prefix}/{fp.relative_to(root).as_posix()}"
        except ValueError:
            rel = str(fp)
        rels.append(rel)
        if fp.stat().st_size > max_file_bytes:
            skipped_oversized += 1
            continue
        src = fp.read_text(encoding="utf-8", errors="replace")
        recs = extract_go_regexp_tests(src, repo=repo, file=rel, dialect=dialect)
        per_file[rel] = len(recs)
        out.extend(recs)
    stats = {
        "files_seen": len(files),
        "expected_files": expected_files,
        "files_ok": expected_files is None or len(files) == expected_files,
        "records": len(out),
        "per_file_records": per_file,
        "files": rels,
        "skipped_oversized": skipped_oversized,
    }
    return out, stats
