"""Extract patterns from V8 ``test/mjsunit/regexp*.js`` (Wave-3 P5 / #116).

Uses the precise JS extractor (:func:`extract_js_precise`) so comments/strings
are skipped. Expected file count is gated fail-closed against the pin.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from regexproof.extractors.js_babel import extract_js_precise

# Upstream pin: 91 ``regexp*.js`` files under ``test/mjsunit`` (recursive).
EXPECTED_V8_MJSUNIT_FILES = 91


def extract_v8_mjsunit(
    source: str,
    *,
    repo: str,
    file: str,
) -> list[dict[str, Any]]:
    """Single-file adapter."""
    return extract_js_precise(source, repo=repo, file=file)


def extract_v8_mjsunit_tree(
    root: Path,
    *,
    repo: str = "v8/v8",
    file_prefix: str = "test/mjsunit",
    expected_files: int | None = EXPECTED_V8_MJSUNIT_FILES,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Walk ``regexp*.js`` under mjsunit; gate on expected count."""
    root = Path(root)
    if not root.exists():
        raise FileNotFoundError(f"v8 mjsunit root missing: {root}")
    files = sorted(p for p in root.rglob("regexp*.js") if p.is_file())
    out: list[dict[str, Any]] = []
    per_file: dict[str, int] = {}
    rels: list[str] = []
    for fp in files:
        try:
            rel = f"{file_prefix}/{fp.relative_to(root).as_posix()}"
        except ValueError:
            rel = str(fp)
        rels.append(rel)
        src = fp.read_text(encoding="utf-8", errors="replace")
        recs = extract_v8_mjsunit(src, repo=repo, file=rel)
        per_file[rel] = len(recs)
        out.extend(recs)
    stats = {
        "files_seen": len(files),
        "expected_files": expected_files,
        "files_ok": expected_files is None or len(files) == expected_files,
        "records": len(out),
        "per_file_records": per_file,
        "files": rels,
    }
    return out, stats
