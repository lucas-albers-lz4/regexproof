"""Budgeted GitHub repository-tree probes for mine ranking and labels.

The tree endpoint is deliberately kept separate from score-v1.  It produces
materialized features for the ranker and the label artifact; a later allocator
can choose weights without changing the API/cache contract.
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from regexproof.admission.boundary import BoundarySignals, classify_boundary
from regexproof.mine.root_dir import root_names_from_paths
from regexproof.io_atomic import atomic_write_text
from regexproof.mine.exclusions import github_repo_slug, normalize_repo_url
from regexproof.mine.search import (
    AuthError,
    HttpSession,
    RateLimitError,
    github_headers,
)

# Match the mine's query budget: rank-time probing is bounded by default, and
# callers can pass zero to explicitly select the v1 degradation path.
DEFAULT_TREE_PROBE_BUDGET = 30

# Secondary-rate 429 retries for the tree API (P6 luna gate 2).
_RATE_RETRY_ATTEMPTS = 3


def _sleep_backoff(attempt: int) -> None:
    """Exponential backoff with jitter, mirroring search.py's policy."""
    import random
    import time

    time.sleep(min(60, 2 ** attempt) + random.uniform(0, 1))
DEFAULT_TREE_CACHE_PATH = (
    Path(__file__).resolve().parents[2] / ".cache" / "regexproof" / "mine-tree.json"
)

# These are the file types currently covered by the admission extractors or
# commonly used for regex rule/configuration files.  The output is a count of
# files, not regex sites: the tree endpoint contains paths only.
REGEX_FILE_SUFFIXES = frozenset(
    {
        ".bash",
        ".c",
        ".cc",
        ".cfg",
        ".conf",
        ".cpp",
        ".cs",
        ".h",
        ".hpp",
        ".hcl",
        ".ini",
        ".java",
        ".js",
        ".json",
        ".jsx",
        ".ksh",
        ".mjs",
        ".nim",
        ".php",
        ".pl",
        ".pm",
        ".py",
        ".rb",
        ".rs",
        ".sh",
        ".toml",
        ".ts",
        ".tsx",
        ".yaml",
        ".yml",
        ".yar",
        ".yara",
        ".zsh",
    }
)


@dataclass(frozen=True)
class TreeProbeResult:
    """A summarized tree response suitable for persistence in an artifact."""

    complete: bool
    truncated: bool
    security_boundary: str
    regex_file_type_counts: dict[str, int]
    path_count: int
    probed_pin: str
    root_dir_names: tuple[str, ...] = ()
    reason: str | None = None

    def as_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {
            "complete": self.complete,
            "truncated": self.truncated,
            "security_boundary": self.security_boundary,
            "regex_file_type_counts": dict(self.regex_file_type_counts),
            "path_count": self.path_count,
            "probed_pin": self.probed_pin,
        }
        if self.root_dir_names:
            out["root_dir_names"] = list(self.root_dir_names)
        if self.reason:
            out["reason"] = self.reason
        return out


class TreeCache:
    """Small JSON cache keyed by the tuple ``(slug, probed_pin)``."""

    def __init__(self, path: Path | str | None = None):
        self.path = Path(path) if path else DEFAULT_TREE_CACHE_PATH
        self._entries: dict[str, dict[str, dict[str, Any]]] = {}
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
        if not isinstance(entries, dict):
            return
        self._entries = {
            str(slug): {
                str(pin): body
                for pin, body in pins.items()
                if isinstance(body, dict)
            }
            for slug, pins in entries.items()
            if isinstance(pins, dict)
        }

    def get(self, slug: str, probed_pin: str) -> dict[str, Any] | None:
        body = self._entries.get(slug, {}).get(probed_pin)
        return dict(body) if isinstance(body, dict) else None

    def put(self, slug: str, probed_pin: str, body: dict[str, Any]) -> None:
        self._entries.setdefault(slug, {})[probed_pin] = dict(body)
        self._dirty = True

    def save(self) -> None:
        if not self._dirty:
            return
        data = {"schema_version": "1", "entries": self._entries}
        text = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        atomic_write_text(self.path, text)
        self._dirty = False


def _repo_slug(url_or_slug: str) -> str:
    """Return github.com ``owner/repo``, or ``""`` for foreign hosts.

    Always parse through ``github_repo_slug`` / ``normalize_repo_url`` (no
    ``startswith("github.com/")`` substring checks). Tree probes must not
    send non-github URLs to ``api.github.com/repos/{slug}``.
    """
    return github_repo_slug(str(url_or_slug or ""))


def _repo_name(slug: str) -> str:
    return slug.rsplit("/", 1)[-1]


def _tree_paths(body: dict[str, Any]) -> list[tuple[str, str]]:
    tree = body.get("tree")
    if not isinstance(tree, list):
        return []
    out: list[tuple[str, str]] = []
    for item in tree:
        if not isinstance(item, dict):
            continue
        path = item.get("path")
        if not isinstance(path, str) or not path:
            continue
        out.append((path, str(item.get("type") or "")))
    return out


def summarize_tree(body: dict[str, Any], slug: str, probed_pin: str) -> TreeProbeResult:
    """Summarize a GitHub tree, refusing to infer negatives from truncation."""
    if bool(body.get("truncated")):
        return TreeProbeResult(
            complete=False,
            truncated=True,
            security_boundary="unknown",
            regex_file_type_counts={},
            path_count=0,
            probed_pin=probed_pin,
            reason="truncated",
        )

    entries = _tree_paths(body)
    paths = [path for path, _kind in entries]
    counts: Counter[str] = Counter()
    for path, kind in entries:
        if kind and kind != "blob":
            continue
        suffix = Path(path).suffix.lower()
        if suffix in REGEX_FILE_SUFFIXES:
            counts[suffix] += 1
    boundary = classify_boundary(
        BoundarySignals(repo_name=_repo_name(slug), paths=tuple(paths))
    )
    return TreeProbeResult(
        complete=True,
        truncated=False,
        security_boundary=boundary,
        regex_file_type_counts=dict(sorted(counts.items())),
        path_count=len(paths),
        probed_pin=probed_pin,
        root_dir_names=tuple(root_names_from_paths(paths)),
    )


def _incomplete(probed_pin: str, reason: str) -> dict[str, Any]:
    return TreeProbeResult(
        complete=False,
        truncated=False,
        security_boundary="unknown",
        regex_file_type_counts={},
        path_count=0,
        probed_pin=probed_pin,
        reason=reason,
    ).as_dict()


def probe_tree(
    session: HttpSession,
    slug: str,
    probed_pin: str,
    *,
    cache: TreeCache | None = None,
    headers: dict[str, str] | None = None,
) -> tuple[dict[str, Any], bool]:
    """Fetch or cache one tree and return ``(features, api_call_made)``.

    A non-200 response is a degraded result.  Authentication and rate-limit
    errors remain typed so callers can apply their normal run policy.
    """
    slug = _repo_slug(slug)
    if not slug or not probed_pin:
        return _incomplete(probed_pin, "missing-slug-or-pin"), False
    if cache is not None:
        cached = cache.get(slug, probed_pin)
        if cached is not None:
            # The cache stores SUMMARIZED features (P6 luna gate 1 fold);
            # re-summarizing a summary would fabricate a zero-path result.
            return cached, False

    response = session.get(
        f"https://api.github.com/repos/{slug}/git/trees/{probed_pin}",
        headers=headers or github_headers(),
        params={"recursive": "1"},
        timeout=30,
    )
    if response.status_code == 401:
        raise AuthError("GitHub tree API returned 401")
    if response.status_code == 429:
        raise RateLimitError(response.text[:200])
    if response.status_code == 403 and "rate limit" in response.text.lower():
        # Primary-rate exhaustion is transient, not a verdict — retryable
        # like a 429 (P6 luna gate 2: fresh regenerations must reproduce
        # the committed features instead of degrading them to http-403).
        raise RateLimitError(response.text[:200])
    if response.status_code != 200:
        return _incomplete(probed_pin, f"http-{response.status_code}"), True
    body = response.json()
    if not isinstance(body, dict):
        return _incomplete(probed_pin, "invalid-json"), True
    if cache is not None:
        # Summarized features, not the raw tree body — the raw recursive
        # trees made the cache hundreds of MB (P6 luna gate 1 fold).
        cache.put(slug, probed_pin, summarize_tree(body, slug, probed_pin).as_dict())
    return summarize_tree(body, slug, probed_pin).as_dict(), True


def materialize_tree_features(
    session: HttpSession | None,
    candidates: list[dict[str, Any]],
    *,
    budget: int = DEFAULT_TREE_PROBE_BUDGET,
    cache: TreeCache | None = None,
    headers: dict[str, str] | None = None,
) -> tuple[dict[tuple[str, str], dict[str, Any]], int]:
    """Probe candidates in deterministic order until the API budget is spent.

    The mined ``pin`` is never used as a fallback.  Rows without the E3
    ``pin_probed`` value are explicitly incomplete rather than accidentally
    probing a stale commit.
    """
    features: dict[tuple[str, str], dict[str, Any]] = {}
    calls = 0
    remaining = max(0, int(budget))
    for candidate in candidates:
        url = str(candidate.get("url") or "")
        probed_pin = str(candidate.get("pin_probed") or "")
        key = (normalize_repo_url(url), probed_pin) if url else (url, probed_pin)
        slug = _repo_slug(url)
        if not slug:
            reason = "missing-slug-or-pin" if not str(url).strip() else "non-github-host"
            features[key] = _incomplete(probed_pin, reason)
            continue
        if not probed_pin:
            features[key] = _incomplete("", "missing-probed-pin")
            continue
        cached_body = cache.get(slug, probed_pin) if cache is not None else None
        if cached_body is not None:
            # P6 (luna gate 1 fold): the cache stores SUMMARIZED features —
            # the raw recursive-tree bodies made the cache hundreds of MB and
            # OOM-killed the materialization.
            features[key] = cached_body
            continue
        if session is None or remaining <= 0:
            features[key] = _incomplete(probed_pin, "budget-exhausted")
            continue
        try:
            result, called = probe_tree(
                session, slug, probed_pin, cache=cache, headers=headers
            )
        except RateLimitError:
            # Secondary-rate pacing: a 429 is transient, not a verdict.
            # Retry with the standard backoff so a fresh regeneration
            # reproduces the committed features instead of degrading them
            # (P6 luna gate 2). The budget is consumed once per candidate.
            result = _incomplete(probed_pin, "rate-limited")
            for attempt in range(_RATE_RETRY_ATTEMPTS):
                _sleep_backoff(attempt)
                try:
                    retried, _called = probe_tree(
                        session, slug, probed_pin, cache=cache, headers=headers
                    )
                except (AuthError, RateLimitError, OSError, ValueError):
                    continue
                result = retried
                break
            called = True
        except (AuthError, OSError, ValueError) as exc:
            result = _incomplete(probed_pin, type(exc).__name__)
            called = True
        if called:
            calls += 1
            remaining -= 1
        features[key] = result
    if cache is not None:
        cache.save()
    return features, calls
