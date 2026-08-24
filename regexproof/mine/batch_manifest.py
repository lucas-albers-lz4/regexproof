"""Wave 5 (#574): immutable ranked batch manifest at ``batch/manifest.json``.

Snapshot of ``rank-mine-candidates`` JSONL. The digest covers the *items*
payload only (not timestamps) so a rewritten file with the same ranked set
verifies; a mutated URL/pin fails closed.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
from typing import Any
from urllib.parse import urlparse

from regexproof.mine.exclusions import normalize_repo_url

MANIFEST_PATH = pathlib.Path("batch/manifest.json")
SCHEMA_VERSION = "1"


def corpus_from_url(url: str) -> str:
    """Derive a corpus slug from a git URL (never the clone dirname)."""
    s = str(url or "").strip().rstrip("/")
    if s.startswith("git@"):
        path = s.split(":", 1)[-1]
    elif "://" in s:
        path = urlparse(s).path
    else:
        return pathlib.Path(s).name or "unknown"
    parts = [p for p in path.split("/") if p]
    if not parts:
        return "unknown"
    name = parts[-1]
    if name.endswith(".git"):
        name = name[:-4]
    return name or "unknown"


def items_digest(items: list[dict[str, Any]]) -> str:
    body = json.dumps(items, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def _sha40(value: str) -> bool:
    return len(value) == 40 and all(c in "0123456789abcdefABCDEF" for c in value)


def items_from_rank_ndjson(text: str) -> list[dict[str, Any]]:
    """Parse rank-mine-candidates stdout into manifest items. Fail closed
    on a ranked row with an empty pin (E3: prefer ``pin_probed`` when it is
    a 40-char SHA; otherwise the ledger mined ``pin``)."""
    items: list[dict[str, Any]] = []
    for line_no, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(
                f"batch-manifest: rank NDJSON line {line_no} is not JSON ({exc})"
            ) from exc
        if not isinstance(row, dict):
            raise SystemExit(f"batch-manifest: rank NDJSON line {line_no} is not an object")
        url = str(row.get("url") or "").strip()
        probed = str(row.get("pin_probed") or "").strip()
        mined = str(row.get("pin") or "").strip()
        pin = probed if _sha40(probed) else mined
        if not url:
            raise SystemExit(f"batch-manifest: rank NDJSON line {line_no} missing url")
        if not _sha40(pin):
            raise SystemExit(
                f"batch-manifest: rank NDJSON line {line_no} pin must be a 40-char hex SHA "
                f"(got {pin!r}) — refuse empty/mined-fallback"
            )
        items.append(
            {
                "url": normalize_repo_url(url),
                "pin": pin.lower(),
                "corpus": corpus_from_url(url),
                "score": row.get("score"),
                "allocator": row.get("allocator") or row.get("score_version"),
            }
        )
    return items


def write_manifest(
    items: list[dict[str, Any]],
    *,
    allocator: str,
    limit: int,
    path: pathlib.Path | None = None,
    created_at: str = "",
) -> dict[str, Any]:
    import datetime as _dt

    created_at = created_at or _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")
    digest = items_digest(items)
    doc = {
        "schema_version": SCHEMA_VERSION,
        "digest": digest,
        "allocator": allocator,
        "limit": int(limit),
        "created_at": created_at,
        "items": items,
    }
    p = pathlib.Path(path) if path is not None else MANIFEST_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(p)
    return doc


def load_and_verify(path: pathlib.Path | None = None) -> dict[str, Any]:
    """Load ``batch/manifest.json`` and fail closed on digest mismatch."""
    p = pathlib.Path(path) if path is not None else MANIFEST_PATH
    if not p.is_file():
        raise SystemExit(f"batch-manifest: {p} missing — snapshot rank first")
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"batch-manifest: {p} is not JSON ({exc})") from exc
    if not isinstance(doc, dict):
        raise SystemExit(f"batch-manifest: {p} is not an object")
    items = doc.get("items")
    if not isinstance(items, list):
        raise SystemExit(f"batch-manifest: {p} missing items list")
    expected = str(doc.get("digest") or "")
    actual = items_digest(items)
    if expected != actual:
        raise SystemExit(
            f"batch-manifest: digest mismatch (file={expected[:12]}… "
            f"recomputed={actual[:12]}…) — refuse to drain a mutated snapshot"
        )
    return doc
