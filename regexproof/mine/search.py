"""GitHub Code Search client for corpus mining (P2 B4)."""

from __future__ import annotations

import os
import random
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Protocol

# Curated query families — shard with repeated filename:/path: (no repo qualifiers).
SEARCH_QUERIES: list[str] = [
    # security tools
    "filename:gitleaks.toml OR filename:gitleaks.yml",
    "filename:.secrets.baseline OR filename:detect-secrets",
    "path:config filename:trufflehog OR filename:trufflehog.yml",
    # validators
    "filename:validator.js path:src OR filename:validators.py",
    "re.compile email OR re.compile url path:validators",
    # rule sets
    "filename:rules.yml path:.semgrep OR path:semgrep",
    "path:rules extension:yar OR extension:yara",
    "SecRule filename:REQUEST path:rules",
    # testdata
    "filename:re_tests OR filename:test_re.py path:Lib/test",
    "path:testdata filename:regex OR filename:regexp",
]

DEFAULT_QUERY_BUDGET = 30
DEFAULT_RETRY_CAP = 5
SEARCH_CAP_THRESHOLD = 950
MIN_STARS = 2


class HttpResponse(Protocol):
    status_code: int
    headers: dict[str, str]

    def json(self) -> Any: ...

    @property
    def text(self) -> str: ...


class HttpSession(Protocol):
    def get(self, url: str, *, headers: dict[str, str], params: dict[str, Any] | None = None, timeout: float = 30) -> HttpResponse: ...


@dataclass
class SearchRunResult:
    candidates: list[dict[str, Any]] = field(default_factory=list)
    capped: bool = False
    queries_run: int = 0
    errors: list[str] = field(default_factory=list)


class AuthError(RuntimeError):
    """GitHub returned 401 — fail fast, no backoff."""


class RateLimitError(RuntimeError):
    """GitHub returned 429 after retries exhausted."""


def github_headers(token: str | None = None) -> dict[str, str]:
    headers = {"Accept": "application/vnd.github+json"}
    tok = token if token is not None else os.environ.get("GITHUB_TOKEN")
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    return headers


def _sleep_backoff(attempt: int, *, sleep_fn: Callable[[float], None] = time.sleep) -> None:
    # ~2s → ~60s with jitter
    base = min(60.0, 2.0 * (2**attempt))
    sleep_fn(base + random.uniform(0, 0.5))


def search_code(
    session: HttpSession,
    query: str,
    *,
    page: int = 1,
    headers: dict[str, str] | None = None,
    retry_cap: int = DEFAULT_RETRY_CAP,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> tuple[dict[str, Any], bool]:
    """Run one code search. Returns (json_body, hit_search_cap).

    401 fail-fast. 429 retries with backoff. Other errors raise RuntimeError.
    """
    hdrs = headers or github_headers()
    url = "https://api.github.com/search/code"
    last_err = ""
    for attempt in range(retry_cap):
        resp = session.get(
            url,
            headers=hdrs,
            params={"q": query, "per_page": 100, "page": page},
            timeout=30,
        )
        if resp.status_code == 401:
            raise AuthError("GitHub search returned 401 — check GITHUB_TOKEN")
        if resp.status_code == 429:
            last_err = resp.text[:200]
            if attempt + 1 >= retry_cap:
                raise RateLimitError(last_err)
            _sleep_backoff(attempt, sleep_fn=sleep_fn)
            continue
        if resp.status_code != 200:
            raise RuntimeError(f"search HTTP {resp.status_code}: {resp.text[:200]}")
        body = resp.json()
        total = int(body.get("total_count") or 0)
        return body, total >= SEARCH_CAP_THRESHOLD
    raise RateLimitError(last_err or "rate limit")


def enrich_repo(
    session: HttpSession,
    full_name: str,
    *,
    headers: dict[str, str] | None = None,
    retry_cap: int = DEFAULT_RETRY_CAP,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> dict[str, Any]:
    hdrs = headers or github_headers()
    last_err = ""
    for attempt in range(retry_cap):
        resp = session.get(
            f"https://api.github.com/repos/{full_name}",
            headers=hdrs,
            timeout=30,
        )
        if resp.status_code == 401:
            raise AuthError("GitHub repos API returned 401")
        if resp.status_code == 429:
            last_err = resp.text[:200]
            if attempt + 1 >= retry_cap:
                raise RateLimitError(last_err or f"enrich rate-limited: {full_name}")
            _sleep_backoff(attempt, sleep_fn=sleep_fn)
            continue
        if resp.status_code != 200:
            return {}
        return resp.json()
    raise RateLimitError(last_err or f"enrich rate-limited: {full_name}")


def resolve_default_pin(
    session: HttpSession,
    full_name: str,
    default_branch: str,
    *,
    headers: dict[str, str] | None = None,
    retry_cap: int = DEFAULT_RETRY_CAP,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> str:
    hdrs = headers or github_headers()
    last_err = ""
    for attempt in range(retry_cap):
        resp = session.get(
            f"https://api.github.com/repos/{full_name}/commits/{default_branch}",
            headers=hdrs,
            timeout=30,
        )
        if resp.status_code == 401:
            raise AuthError("GitHub commits API returned 401")
        if resp.status_code == 429:
            last_err = resp.text[:200]
            if attempt + 1 >= retry_cap:
                raise RateLimitError(last_err or f"pin rate-limited: {full_name}")
            _sleep_backoff(attempt, sleep_fn=sleep_fn)
            continue
        if resp.status_code != 200:
            return ""
        data = resp.json()
        return str(data.get("sha") or "")
    raise RateLimitError(last_err or f"pin rate-limited: {full_name}")


def run_search(
    session: HttpSession,
    *,
    queries: list[str] | None = None,
    query_budget: int = DEFAULT_QUERY_BUDGET,
    min_stars: int = MIN_STARS,
    headers: dict[str, str] | None = None,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> SearchRunResult:
    """Execute curated queries until budget exhaustion; return candidates + capped flag."""
    result = SearchRunResult()
    hdrs = headers or github_headers()
    seen_repos: set[str] = set()
    for query in queries or SEARCH_QUERIES:
        if result.queries_run >= query_budget:
            result.capped = True
            break
        try:
            body, hit_cap = search_code(
                session, query, headers=hdrs, sleep_fn=sleep_fn
            )
        except AuthError:
            raise
        except RateLimitError as e:
            result.errors.append(str(e))
            result.capped = True
            break
        except RuntimeError as e:
            result.errors.append(str(e))
            result.queries_run += 1
            continue

        result.queries_run += 1
        if hit_cap:
            result.capped = True

        for item in body.get("items") or []:
            repo = item.get("repository") or {}
            full_name = repo.get("full_name") or ""
            if not full_name or full_name in seen_repos:
                continue
            seen_repos.add(full_name)
            try:
                meta = enrich_repo(
                    session, full_name, headers=hdrs, sleep_fn=sleep_fn
                )
            except RateLimitError as e:
                result.errors.append(f"enrich rate-limited: {full_name}: {e}")
                result.capped = True
                break
            if not meta:
                result.errors.append(f"enrich failed: {full_name}")
                continue
            stars = int(meta.get("stargazers_count") or repo.get("stargazers_count") or 0)
            if stars < min_stars:
                continue
            default_branch = str(meta.get("default_branch") or "main")
            try:
                pin = resolve_default_pin(
                    session,
                    full_name,
                    default_branch,
                    headers=hdrs,
                    sleep_fn=sleep_fn,
                )
            except RateLimitError as e:
                result.errors.append(f"pin rate-limited: {full_name}: {e}")
                result.capped = True
                break
            if not pin:
                result.errors.append(f"pin resolve failed: {full_name}")
                continue
            pushed = str(meta.get("pushed_at") or "")[:10]
            html = str(meta.get("html_url") or f"https://github.com/{full_name}")
            entry = {
                "url": html,
                "default_branch": default_branch,
                "pin": pin,
                "pushed_date": pushed,
                "stars": stars,
                "source_query": query,
                "capped": hit_cap,
            }
            result.candidates.append(entry)
    return result
