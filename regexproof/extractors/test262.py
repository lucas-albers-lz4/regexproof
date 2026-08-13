"""test262 RegExp built-ins extractor (tc39/test262).

Walks ``test/built-ins/RegExp/**/*.js`` and reuses the JS scaffold
(:func:`extract_js`). Reports file counts for expected-vs-actual gating.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from regexproof.extractors.js_babel import extract_js

# Upstream built-ins/RegExp file count at the Wave-2 pin (sparse clone).
EXPECTED_REGEXP_FILES = 1879
# Keep in sync with regexproof.batch.manifests.MAX_FILE_BYTES (#175/#365).
_DEFAULT_MAX_FILE_BYTES = 2_000_000


def extract_test262_tree(
    root: Path,
    *,
    repo: str = "tc39/test262",
    file_prefix: str = "test/built-ins/RegExp",
    expected_files: int | None = EXPECTED_REGEXP_FILES,
    max_file_bytes: int = _DEFAULT_MAX_FILE_BYTES,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Extract regex sites from a RegExp test tree.

    Returns ``(records, stats)`` where stats includes ``files_seen``,
    ``expected_files``, and ``files_ok`` (bool).
    """
    root = Path(root)
    if not root.exists():
        raise FileNotFoundError(f"test262 RegExp root missing: {root}")
    files = sorted(p for p in root.rglob("*.js") if p.is_file())
    out: list[dict[str, Any]] = []
    skipped_oversized = 0
    for fp in files:
        try:
            rel = f"{file_prefix}/{fp.relative_to(root).as_posix()}"
        except ValueError:
            rel = str(fp)
        if fp.stat().st_size > max_file_bytes:
            skipped_oversized += 1
            continue
        src = fp.read_text(encoding="utf-8", errors="replace")
        out.extend(extract_js(src, repo=repo, file=rel))
    stats = {
        "files_seen": len(files),
        "expected_files": expected_files,
        "files_ok": expected_files is None or len(files) == expected_files,
        "records": len(out),
        "skipped_oversized": skipped_oversized,
    }
    return out, stats


def extract_test262(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """Single-file adapter for glob extractors."""
    return extract_js(source, repo=repo, file=file)
