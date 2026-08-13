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
from regexproof.io_atomic import atomic_write_text
from regexproof.mine.exclusions import normalize_repo_url
from regexproof.mine.search import (
    AuthError,
    HttpSession,
    RateLimitError,
    github_headers,
)

# Match the mine's query budget: rank-time probing is bounded by default, and
# callers can pass zero to explicitly select the v1 degradation path.
DEFAULT_TREE_PROBE_BUDGET = 30
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
    value = str(url_or_slug or "")
    if "/" in value and value.startswith("https://github.com/"):
        return normalize_repo_url(value).removeprefix("https://github.com/")
    if value.startswith("github.com/"):
        return value.removeprefix("github.com/").strip("/")
    return value.strip("/")


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
            return summarize_tree(cached, slug, probed_pin).as_dict(), False

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
    if response.status_code != 200:
        return _incomplete(probed_pin, f"http-{response.status_code}"), True
    body = response.json()
    if not isinstance(body, dict):
        return _incomplete(probed_pin, "invalid-json"), True
    if cache is not None:
        cache.put(slug, probed_pin, body)
    return summarize_tree(body, slug, probed_pin).as_dict(), True


def materialize_tree_features(
    session: HttpSession | None,
    candidates: list[dict[str, Any]],
    *,
    budget: int = DEFAULT_TREE_PROBE_BUDGET,
    cache: TreeCache | None = None,
    headers: dict[str, str] | None = None,
) -> tuple[dict[str, dict[str, Any]], int]:
    """Probe candidates in deterministic order until the API budget is spent.

    The mined ``pin`` is never used as a fallback.  Rows without the E3
    ``pin_probed`` value are explicitly incomplete rather than accidentally
    probing a stale commit.
    """
    features: dict[str, dict[str, Any]] = {}
    calls = 0
    remaining = max(0, int(budget))
    for candidate in candidates:
        url = str(candidate.get("url") or "")
        key = normalize_repo_url(url) if url else url
        slug = _repo_slug(url)
        probed_pin = str(candidate.get("pin_probed") or "")
        if not probed_pin:
            features[key] = _incomplete("", "missing-probed-pin")
            continue
        cached_body = cache.get(slug, probed_pin) if cache is not None else None
        if cached_body is not None:
            features[key] = summarize_tree(cached_body, slug, probed_pin).as_dict()
            continue
        if session is None or remaining <= 0:
            features[key] = _incomplete(probed_pin, "budget-exhausted")
            continue
        try:
            result, called = probe_tree(
                session, slug, probed_pin, cache=cache, headers=headers
            )
        except (AuthError, RateLimitError, OSError, ValueError) as exc:
            result = _incomplete(probed_pin, type(exc).__name__)
            called = True
        if called:
            calls += 1
            remaining -= 1
        features[key] = result
    if cache is not None:
        cache.save()
    return features, calls
