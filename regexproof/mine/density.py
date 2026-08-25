"""Wave 9 (#578): optional pre-clone code-search density (soft, never reject).

One coarse ``repo:`` count. Rate-limit / error → ``None`` (unknown), the
same degrade path as ``tree_unavailable``: missing evidence is not a zero.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from regexproof.io_atomic import atomic_write_text
from regexproof.mine.exclusions import github_repo_slug, normalize_repo_url
from regexproof.mine.search import (
    AuthError,
    HttpSession,
    RateLimitError,
    search_code,
)

# Issue #578: re.compile(|re.match(|Pattern(|.yara — one query per repo.
DENSITY_QUERY_BODY = "re.compile( OR re.match( OR Pattern( OR .yara"
DEFAULT_DENSITY_BUDGET = 0
DEFAULT_DENSITY_CACHE_PATH = (
    Path(__file__).resolve().parents[2] / ".cache" / "regexproof" / "mine-density.json"
)


class DensityCache:
    """JSON cache keyed by github ``owner/repo`` slug."""

    def __init__(self, path: Path | str | None = None):
        self.path = Path(path) if path else DEFAULT_DENSITY_CACHE_PATH
        self._entries: dict[str, Any] = {}
        self._dirty = False
        self._load()

    def _load(self) -> None:
        if not self.path.is_file():
            return
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return
        entries = data.get("entries") if isinstance(data, dict) else None
        if isinstance(entries, dict):
            self._entries = dict(entries)

    def get(self, slug: str) -> int | None:
        body = self._entries.get(slug)
        if isinstance(body, dict) and "hits" in body:
            hits = body.get("hits")
            return int(hits) if isinstance(hits, int) else None
        return None

    def has(self, slug: str) -> bool:
        return slug in self._entries

    def put(self, slug: str, hits: int | None, *, reason: str | None = None) -> None:
        entry: dict[str, Any] = {"hits": hits}
        if reason:
            entry["reason"] = reason
        self._entries[slug] = entry
        self._dirty = True

    def save(self) -> None:
        if not self._dirty:
            return
        text = json.dumps(
            {"schema_version": "1", "entries": self._entries},
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
        ) + "\n"
        atomic_write_text(self.path, text)
        self._dirty = False


def density_query(slug: str) -> str:
    return f"repo:{slug} {DENSITY_QUERY_BODY}"


def probe_density(
    session: HttpSession,
    slug: str,
    *,
    cache: DensityCache | None = None,
) -> tuple[int | None, bool]:
    """Return ``(hit_count_or_None, api_call_made)``.

    ``None`` is the degrade path (rate-limit / HTTP error): not a zero.
    """
    slug = github_repo_slug(slug) or slug.strip().lower()
    if not slug or "/" not in slug:
        return None, False
    if cache is not None and cache.has(slug):
        return cache.get(slug), False
    try:
        body, _capped = search_code(session, density_query(slug))
    except RateLimitError:
        if cache is not None:
            cache.put(slug, None, reason="rate-limited")
        return None, True
    except AuthError:
        raise
    except (OSError, RuntimeError, ValueError, TypeError):
        if cache is not None:
            cache.put(slug, None, reason="error")
        return None, True
    hits = int(body.get("total_count") or 0) if isinstance(body, dict) else 0
    if cache is not None:
        cache.put(slug, hits)
    return hits, True


def materialize_density_hits(
    session: HttpSession | None,
    candidates: list[dict[str, Any]],
    *,
    budget: int = DEFAULT_DENSITY_BUDGET,
    cache: DensityCache | None = None,
) -> tuple[dict[str, int | None], int]:
    """Probe up to ``budget`` uncached repos. Missing/degraded → omitted or None.

    Returned map is keyed by ``normalize_repo_url(url)``. A key present with
    ``None`` means probed-but-unknown (do not treat as empty). A missing key
    means not probed.
    """
    hits: dict[str, int | None] = {}
    calls = 0
    remaining = max(0, int(budget))
    for cand in candidates:
        url = str(cand.get("url") or "")
        key = normalize_repo_url(url) if url else url
        slug = github_repo_slug(url)
        if not slug:
            continue
        if cache is not None and cache.has(slug):
            hits[key] = cache.get(slug)
            continue
        if session is None or remaining <= 0:
            continue
        try:
            count, called = probe_density(session, slug, cache=cache)
        except AuthError:
            if cache is not None:
                cache.put(slug, None, reason="auth")
            count, called = None, True
        if called:
            calls += 1
            remaining -= 1
        hits[key] = count
    if cache is not None:
        cache.save()
    return hits, calls
