"""P2 queue / exclusions / search / CLI tests (B2–B5)."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from types import SimpleNamespace

import pytest

from regexproof.mine.exclusions import is_excluded, load_admitted_urls, normalize_repo_url
from regexproof.mine.ledger import empty_ledger, load_ledger, save_ledger
from regexproof.mine.queue import (
    daily_mine_cap,
    drain,
    enqueue,
    evict_stale,
    load_queue,
    save_queue,
)
from regexproof.mine.search import (
    AuthError,
    RateLimitError,
    SearchRunResult,
    run_search,
    search_code,
)

ROOT = Path(__file__).resolve().parents[1]


class FakeResp:
    def __init__(self, status_code: int, payload: dict | None = None, text: str = ""):
        self.status_code = status_code
        self._payload = payload or {}
        self.text = text or json.dumps(self._payload)
        self.headers: dict[str, str] = {}

    def json(self):
        return self._payload


class FakeSession:
    def __init__(self, responses: list[FakeResp]):
        self._responses = list(responses)
        self.calls: list[str] = []

    def get(self, url: str, *, headers=None, params=None, timeout: float = 30):
        self.calls.append(url)
        if not self._responses:
            return FakeResp(500, text="empty")
        return self._responses.pop(0)


def test_queue_fifo_cap_and_ttl(tmp_path: Path):
    qpath = tmp_path / "mine-queue.json"
    q = {"schema_version": "1", "items": []}
    assert enqueue(q, {"url": "https://github.com/a/a", "pushed_date": "2026-08-01"})
    assert enqueue(q, {"url": "https://github.com/b/b", "pushed_date": "2026-08-02"})
    save_queue(qpath, q)
    loaded = load_queue(qpath)
    drained = drain(loaded, 1)
    assert drained[0]["url"].endswith("/a/a")
    assert len(loaded["items"]) == 1

    stale = {
        "schema_version": "1",
        "items": [
            {"url": "https://github.com/old/old", "pushed_date": "2020-01-01"},
            {"url": "https://github.com/new/new", "pushed_date": "2026-08-01"},
        ],
    }
    n = evict_stale(stale, ttl_days=90, today=date(2026, 8, 9))
    assert n == 1
    assert len(stale["items"]) == 1

    full = {"schema_version": "1", "items": [{"url": f"https://github.com/x/{i}"} for i in range(100)]}
    assert enqueue(full, {"url": "https://github.com/x/overflow"}) is False


def test_daily_mine_cap_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("DAILY_MINE_CAP", "3")
    assert daily_mine_cap() == 3


def test_exclusions_owner_ledger_admitted(tmp_path: Path):
    admitted = {normalize_repo_url("https://github.com/gitleaks/gitleaks")}
    ledger = empty_ledger()
    ledger["candidates"].append(
        {
            "url": "https://github.com/example/seen",
            "default_branch": "main",
            "pin": "x",
            "pushed_date": "2026-01-01",
            "stars": 1,
            "source_query": "q",
            "first_seen": "t",
            "status": "mined",
        }
    )
    assert is_excluded(
        "https://github.com/lucas-albers-lz4/regexproof",
        ledger=ledger,
        admitted=admitted,
    )
    assert is_excluded(
        "https://github.com/gitleaks/gitleaks", ledger=ledger, admitted=admitted
    )
    assert is_excluded(
        "https://github.com/example/seen", ledger=ledger, admitted=admitted
    )
    assert (
        is_excluded("https://github.com/other/ok", ledger=ledger, admitted=admitted)
        is None
    )

    # Real admitted set from repo
    real = load_admitted_urls(ROOT / "properties" / "generated")
    assert any("gitleaks" in u for u in real)


def test_search_401_fail_fast():
    session = FakeSession([FakeResp(401, text="bad creds")])
    with pytest.raises(AuthError):
        search_code(session, "filename:x", sleep_fn=lambda _s: None)


def test_search_429_retries_then_raises():
    session = FakeSession([FakeResp(429, text="slow")] * 5)
    with pytest.raises(RateLimitError):
        search_code(session, "filename:x", retry_cap=3, sleep_fn=lambda _s: None)


def test_run_search_budget_exhaustion_sets_capped():
    # One successful search then stop via budget=1
    items = {
        "total_count": 10,
        "items": [
            {
                "repository": {
                    "full_name": "acme/tool",
                    "stargazers_count": 5,
                    "html_url": "https://github.com/acme/tool",
                }
            }
        ],
    }
    session = FakeSession(
        [
            FakeResp(200, items),
            FakeResp(
                200,
                {
                    "default_branch": "main",
                    "stargazers_count": 5,
                    "pushed_at": "2026-08-01T00:00:00Z",
                    "html_url": "https://github.com/acme/tool",
                },
            ),
            FakeResp(200, {"sha": "deadbeef"}),
        ]
    )
    result = run_search(
        session,
        queries=["filename:gitleaks.toml"],
        query_budget=1,
        sleep_fn=lambda _s: None,
    )
    assert result.queries_run == 1
    assert len(result.candidates) == 1
    assert result.candidates[0]["pin"] == "deadbeef"


def test_assimilate_overflow_before_new_and_dry_run_determinism(tmp_path: Path):
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "mine_cli", ROOT / "scripts" / "mine-corpus-candidates.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    ledger = empty_ledger()
    queue = {
        "schema_version": "1",
        "items": [
            {
                "url": "https://github.com/queued/first",
                "default_branch": "main",
                "pin": "aaa",
                "pushed_date": "2026-08-01",
                "stars": 3,
                "source_query": "q0",
            }
        ],
    }
    search = SearchRunResult(
        candidates=[
            {
                "url": "https://github.com/fresh/second",
                "default_branch": "main",
                "pin": "bbb",
                "pushed_date": "2026-08-02",
                "stars": 4,
                "source_query": "q1",
            }
        ]
    )
    # Cap 1 so queued wins and fresh goes to overflow
    import os

    os.environ["DAILY_MINE_CAP"] = "1"
    try:
        a1 = mod.assimilate(
            search_result=search,
            ledger=ledger,
            queue=queue,
            admitted=set(),
            dry_run=True,
            now_iso="2026-08-09T00:00:00Z",
        )
        assert len(a1) == 1
        assert a1[0]["url"].endswith("/queued/first")
        # fresh enqueued
        assert any(i["url"].endswith("/fresh/second") for i in queue["items"])

        # determinism: same inputs → same accepted urls
        ledger2 = empty_ledger()
        queue2 = {
            "schema_version": "1",
            "items": [
                {
                    "url": "https://github.com/queued/first",
                    "default_branch": "main",
                    "pin": "aaa",
                    "pushed_date": "2026-08-01",
                    "stars": 3,
                    "source_query": "q0",
                }
            ],
        }
        search2 = SearchRunResult(candidates=list(search.candidates))
        a2 = mod.assimilate(
            search_result=search2,
            ledger=ledger2,
            queue=queue2,
            admitted=set(),
            dry_run=True,
            now_iso="2026-08-09T00:00:00Z",
        )
        assert [c["url"] for c in a1] == [c["url"] for c in a2]
    finally:
        os.environ.pop("DAILY_MINE_CAP", None)


def test_normalize_url_scheme_and_git_suffix():
    a = normalize_repo_url("http://github.com/Acme/Tool.git")
    b = normalize_repo_url("https://github.com/acme/tool")
    assert a == b == "https://github.com/acme/tool"


def test_run_search_dedupes_across_queries():
    items = {
        "total_count": 1,
        "items": [
            {
                "repository": {
                    "full_name": "acme/tool",
                    "stargazers_count": 5,
                    "html_url": "https://github.com/acme/tool",
                }
            }
        ],
    }
    meta = {
        "default_branch": "main",
        "stargazers_count": 5,
        "pushed_at": "2026-08-01T00:00:00Z",
        "html_url": "https://github.com/acme/tool",
    }
    session = FakeSession(
        [
            FakeResp(200, items),
            FakeResp(200, meta),
            FakeResp(200, {"sha": "aaa"}),
            FakeResp(200, items),  # same repo, second query — should skip enrich
        ]
    )
    result = run_search(
        session,
        queries=["filename:a", "filename:b"],
        query_budget=2,
        sleep_fn=lambda _s: None,
    )
    assert result.queries_run == 2
    assert len(result.candidates) == 1
    # Only one enrich + one pin for the first hit
    assert sum(1 for u in session.calls if "/repos/acme/tool" in u and "/commits/" not in u) == 1


def test_search_cap_threshold_flagged():
    body = {"total_count": 960, "items": []}
    session = FakeSession([FakeResp(200, body)])
    _data, hit = search_code(session, "q", sleep_fn=lambda _s: None)
    assert hit is True
