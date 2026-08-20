"""P2 queue / exclusions / search / CLI tests (B2–B5)."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest

from regexproof.mine.exclusions import is_excluded, load_admitted_urls, normalize_repo_url
from regexproof.mine.ledger import empty_ledger
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
    assert enqueue(q, {"url": "https://github.com/a/a", "pushed_date": "2026-08-01"}) == "enqueued"
    assert enqueue(q, {"url": "https://github.com/b/b", "pushed_date": "2026-08-02"}) == "enqueued"
    save_queue(qpath, q)
    loaded = load_queue(qpath)
    drained = drain(loaded, 1)
    assert drained[0]["url"].endswith("/a/a")
    assert len(loaded["items"]) == 1

    stale = {
        "schema_version": "1",
        "items": [
            {"url": "https://github.com/old/old", "pushed_date": "2020-01-01", "queued_at": "2020-01-02"},
            {
                "url": "https://github.com/new/new",
                "pushed_date": "2020-01-01",  # old push, but freshly queued
                "queued_at": "2026-08-01",
            },
            {"url": "https://github.com/nodate/x"},  # no dates → stale
        ],
    }
    n = evict_stale(stale, ttl_days=90, today=date(2026, 8, 9))
    assert n == 2
    assert len(stale["items"]) == 1
    assert stale["items"][0]["url"].endswith("/new/new")

    full = {"schema_version": "1", "items": [{"url": f"https://github.com/x/{i}"} for i in range(100)]}
    assert enqueue(full, {"url": "https://github.com/x/overflow"}) == "full"

    # Duplicate URL (scheme variant) refreshes metadata in place
    q2 = {
        "schema_version": "1",
        "items": [
            {
                "url": "https://github.com/a/a",
                "pin": "old",
                "stars": 1,
                "queued_at": "2026-08-01",
            }
        ],
    }
    assert (
        enqueue(
            q2,
            {
                "url": "http://github.com/a/a.git",
                "pin": "newsha",
                "stars": 9,
            },
        )
        == "duplicate"
    )
    assert len(q2["items"]) == 1
    assert q2["items"][0]["pin"] == "newsha"
    assert q2["items"][0]["stars"] == 9
    assert q2["items"][0]["queued_at"] == "2026-08-01"


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


def test_exclusions_owner_schemeless_host_prefix():
    """Schemeless github.com/owner/... must not parse the host as the owner."""
    assert (
        is_excluded("github.com/lucas-albers-lz4/regexproof")
        == "excluded-owner:lucas-albers-lz4"
    )
    assert (
        is_excluded("www.github.com/lucas-albers-lz4/regexproof")
        == "excluded-owner:lucas-albers-lz4"
    )
    assert is_excluded("github.com/other/ok") is None
    assert is_excluded("www.github.com/other/ok") is None


def test_search_401_fail_fast():
    session = FakeSession([FakeResp(401, text="bad creds")])
    with pytest.raises(AuthError):
        search_code(session, "filename:x", sleep_fn=lambda _s: None)


def test_search_429_retries_then_raises():
    session = FakeSession([FakeResp(429, text="slow")] * 5)
    with pytest.raises(RateLimitError):
        search_code(session, "filename:x", retry_cap=3, sleep_fn=lambda _s: None)


def test_enrich_repo_429_retries_then_raises():
    from regexproof.mine.search import enrich_repo

    session = FakeSession([FakeResp(429, text="slow")] * 5)
    with pytest.raises(RateLimitError):
        enrich_repo(session, "acme/tool", retry_cap=3, sleep_fn=lambda _s: None)


def test_enrich_repo_429_then_success():
    from regexproof.mine.search import enrich_repo

    session = FakeSession(
        [
            FakeResp(429, text="slow"),
            FakeResp(
                200,
                {
                    "default_branch": "main",
                    "stargazers_count": 9,
                    "html_url": "https://github.com/acme/tool",
                },
            ),
        ]
    )
    meta = enrich_repo(session, "acme/tool", retry_cap=3, sleep_fn=lambda _s: None)
    assert meta["stargazers_count"] == 9


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


def test_assimilate_calendar_day_cap_and_no_capped_on_overflow():
    import importlib.util
    import os

    spec = importlib.util.spec_from_file_location(
        "mine_cli2", ROOT / "scripts" / "mine-corpus-candidates.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    ledger = empty_ledger()
    ledger["candidates"].append(
        {
            "url": "https://github.com/earlier/one",
            "default_branch": "main",
            "pin": "x",
            "pushed_date": "2026-08-01",
            "stars": 1,
            "source_query": "q",
            "first_seen": "2026-08-09T01:00:00Z",
            "status": "mined",
        }
    )
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
        ],
        capped=True,
    )
    os.environ["DAILY_MINE_CAP"] = "1"
    try:
        accepted = mod.assimilate(
            search_result=search,
            ledger=ledger,
            queue=queue,
            admitted=set(),
            dry_run=True,
            now_iso="2026-08-09T12:00:00Z",
        )
        assert accepted == []
        assert any(i["url"].endswith("/fresh/second") for i in queue["items"])
        assert any(i["url"].endswith("/queued/first") for i in queue["items"])
    finally:
        os.environ.pop("DAILY_MINE_CAP", None)

    os.environ["DAILY_MINE_CAP"] = "1"
    try:
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
        accepted2 = mod.assimilate(
            search_result=SearchRunResult(candidates=[], capped=True),
            ledger=ledger2,
            queue=queue2,
            admitted=set(),
            dry_run=True,
            now_iso="2026-08-09T12:00:00Z",
        )
        assert len(accepted2) == 1
        assert "capped" not in accepted2[0]
    finally:
        os.environ.pop("DAILY_MINE_CAP", None)


def test_normalize_url_scheme_and_git_suffix():
    a = normalize_repo_url("http://github.com/Acme/Tool.git")
    b = normalize_repo_url("https://github.com/acme/tool")
    assert a == b == "https://github.com/acme/tool"


def test_normalize_url_schemeless_host_and_slug():
    want = "https://github.com/acme/tool"
    assert normalize_repo_url("github.com/acme/tool") == want
    assert normalize_repo_url("github.com/Acme/Tool.git") == want
    assert normalize_repo_url("www.github.com/acme/tool") == want
    assert normalize_repo_url("acme/tool") == want
    assert normalize_repo_url("git@github.com:Acme/Tool.git") == want
    # Host-suffix bypass: github.com.evil.com is not github.com.
    assert (
        normalize_repo_url("https://github.com.evil.com/acme/tool")
        == "https://github.com.evil.com/acme/tool"
    )


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


def test_mine_cli_prints_run_summary(tmp_path: Path, monkeypatch, capsys):
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "mine_cli_summary", ROOT / "scripts" / "mine-corpus-candidates.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    ledger = tmp_path / "candidate-ledger.json"
    queue = tmp_path / "mine-queue.json"
    ledger.write_text('{"schema_version":"1","candidates":[]}\n', encoding="utf-8")
    queue.write_text('{"schema_version":"1","items":[]}\n', encoding="utf-8")

    monkeypatch.setattr(
        mod,
        "run_search",
        lambda _session: SearchRunResult(candidates=[], capped=True, errors=[]),
    )
    monkeypatch.setattr(mod, "_http_session", lambda: object())
    rc = mod.main(
        [
            "--dry-run",
            "--ledger",
            str(ledger),
            "--queue",
            str(queue),
            "--generated",
            str(tmp_path),
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    summary = json.loads(lines[-1])
    assert summary["kind"] == "mine_run_summary"
    assert summary["capped"] is True
    assert summary["dry_run"] is True
    assert summary["accepted"] == 0
    assert summary["allocator"] == "score-v1"


def test_search_queries_nonempty_unique():
    """Guard against empty/duplicate query strings in search.py."""
    from regexproof.mine.search import SEARCH_QUERIES
    assert len(SEARCH_QUERIES) >= 15
    assert len(set(SEARCH_QUERIES)) == len(SEARCH_QUERIES)
    assert all(q.strip() for q in SEARCH_QUERIES)


def test_enqueue_replacement_requires_outscore():
    """Newcomer with LOWER score must NOT replace; equal score returns full."""
    q = {
        "schema_version": "1",
        "capacity_source": "regexproof.mine.queue.DEFAULT_QUEUE_CAP",
        "items": [
            {
                "url": "https://github.com/existing/high",
                "stars": 5000,
                "source_query": "filename:gitleaks.toml",
                "pushed_date": "2026-08-01",
                "queued_at": "2026-08-01",
            }
        ],
    }
    # Lower-scored newcomer
    low = {
        "url": "https://github.com/newcomer/low",
        "stars": 1,
        "source_query": "path:testdata",
        "pushed_date": "2020-01-01",
    }
    repl = [10]
    status = enqueue(q, low, cap=1, replacements_left=repl)
    assert status == "full"
    assert len(q["items"]) == 1
    assert q["items"][0]["url"].endswith("/existing/high")
    assert repl[0] == 10  # not decremented

    # Equal score → also full (must outscore, not merely tie)
    eq = {
        "url": "https://github.com/newcomer/equal",
        "stars": 5000,
        "source_query": "filename:gitleaks.toml",
        "pushed_date": "2026-08-01",
    }
    status2 = enqueue(q, eq, cap=1, replacements_left=repl)
    assert status2 == "full"
    assert len(q["items"]) == 1


def test_enqueue_max_10_replacements_enforced():
    """After 10 replacements, further newcomers return full."""
    items = [
        {
            "url": f"https://github.com/pool/lo{i}",
            "stars": i,
            "source_query": "path:testdata",
            "pushed_date": "2026-01-01",
            "queued_at": "2026-01-01",
        }
        for i in range(1, 101)
    ]
    q = {
        "schema_version": "1",
        "capacity_source": "regexproof.mine.queue.DEFAULT_QUEUE_CAP",
        "items": items,
    }

    repl = [10]
    for i in range(10):
        newcomer = {
            "url": f"https://github.com/new/hi{i}",
            "stars": 9999,
            "source_query": "filename:gitleaks.toml",
            "pushed_date": "2026-08-13",
        }
        status = enqueue(q, newcomer, cap=100, replacements_left=repl)
        assert status == "replaced"
    assert repl[0] == 0

    # 11th newcomer → full (budget exhausted)
    overflow = {
        "url": "https://github.com/new/overflow",
        "stars": 9999,
        "source_query": "filename:gitleaks.toml",
        "pushed_date": "2026-08-13",
    }
    status = enqueue(q, overflow, cap=100, replacements_left=repl)
    assert status == "full"


def test_run_search_three_page_budget():
    """A query with >3 pages of results only fetches 3 pages; the budget counts QUERIES (P7 fold — luna re-gate 4), so one query == queries_run 1 regardless of pages."""
    # Each page returns items to keep paginating; 4th page should never be hit
    page_items = {
        "total_count": 10,
        "items": [
            {
                "repository": {
                    "full_name": f"acme/tool{i}",
                    "stargazers_count": 5,
                    "html_url": f"https://github.com/acme/tool{i}",
                }
            }
            for i in range(3)
        ],
    }
    # 3 pages of search results + enrich + pin for each unique repo
    responses = []
    for _page in range(3):
        responses.append(FakeResp(200, page_items))
        for i in range(3):
            responses.append(FakeResp(200, {
                "default_branch": "main",
                "stargazers_count": 5,
                "pushed_at": "2026-08-01T00:00:00Z",
                "html_url": f"https://github.com/acme/tool{i}",
            }))
            responses.append(FakeResp(200, {"sha": f"sha{i}"}))

    session = FakeSession(responses)
    result = run_search(
        session,
        queries=["filename:gitleaks.toml"],
        query_budget=100,
        max_pages=3,
        sleep_fn=lambda _s: None,
    )
    # Only 3 search_code calls (pages 1-3), no 4th
    search_calls = [c for c in session.calls if "search/code" in c]
    assert len(search_calls) == 3
    assert result.queries_run == 1  # budget counts queries, not pages


def test_run_search_ratelimit_aborts_both_loops():
    """RateLimitError aborts the whole search run, not just the inner page loop."""
    # First query: page 1 succeeds, page 2 hits rate limit (5x 429 exhausts retry_cap)
    # Second query should NOT be attempted
    page1_items = {
        "total_count": 5,
        "items": [
            {
                "repository": {
                    "full_name": "acme/tool1",
                    "stargazers_count": 5,
                    "html_url": "https://github.com/acme/tool1",
                }
            }
        ],
    }
    session = FakeSession(
        [
            FakeResp(200, page1_items),                    # query1 page1
            FakeResp(200, {                                # enrich
                "default_branch": "main",
                "stargazers_count": 5,
                "pushed_at": "2026-08-01T00:00:00Z",
                "html_url": "https://github.com/acme/tool1",
            }),
            FakeResp(200, {"sha": "aaa"}),                 # pin
            FakeResp(429, text="rate limited"),             # query1 page2 attempt 1
            FakeResp(429, text="rate limited"),             # attempt 2
            FakeResp(429, text="rate limited"),             # attempt 3
            FakeResp(429, text="rate limited"),             # attempt 4
            FakeResp(429, text="rate limited"),             # attempt 5 → raises RateLimitError
            FakeResp(200, page1_items),                    # query2 — should NOT be reached
        ]
    )
    result = run_search(
        session,
        queries=["q1", "q2"],
        query_budget=100,
        sleep_fn=lambda _s: None,
    )
    assert result.capped is True
    assert result.queries_run == 1  # only page1 of q1 completed
    # search q1/p1, enrich, pin, then 5x 429 for q1/p2 = 8 calls total
    assert len(session.calls) == 8


def test_queue_schema_has_capacity_source():
    """Queue schema includes capacity_source field."""
    from regexproof.mine.queue import QUEUE_CAPACITY_SOURCE, empty_queue

    q = empty_queue()
    assert "capacity_source" in q
    assert q["capacity_source"] == QUEUE_CAPACITY_SOURCE


def test_run_search_fork_below_50_stars_dropped():
    """D4 (P7 fold): fork:true repos below 50 stars are dropped as a
    post-filter on the enrich object (code search cannot filter stars)."""
    page1_items = {
        "items": [
            {
                "repository": {
                    "full_name": "acme/forked-lib",
                    "stargazers_count": 20,
                }
            },
            {
                "repository": {
                    "full_name": "acme/original-lib",
                    "stargazers_count": 300,
                }
            },
            {
                "repository": {
                    "full_name": "acme/big-fork",
                    "stargazers_count": 120,
                }
            },
        ]
    }
    session = FakeSession(
        responses=[
            FakeResp(200, page1_items),
            # forked-lib enrich (fork, 20 stars) -> dropped before pin
            FakeResp(200, {"fork": True, "stargazers_count": 20, "default_branch": "main"}),
            # original-lib enrich + pin
            FakeResp(200, {"fork": False, "stargazers_count": 300, "default_branch": "main"}),
            FakeResp(200, {"sha": "bbb"}),
            # big-fork enrich (fork, 120 stars >= 50) + pin
            FakeResp(200, {"fork": True, "stargazers_count": 120, "default_branch": "main"}),
            FakeResp(200, {"sha": "ccc"}),
        ]
    )
    result = run_search(session, queries=["q1"], sleep_fn=lambda _s: None)
    urls = [c["url"] for c in result.candidates]
    assert len(urls) == 2
    assert any("original-lib" in u for u in urls)
    assert any("big-fork" in u for u in urls)
    assert not any("forked-lib" in u for u in urls)


def test_query_budget_counts_queries_not_pages():
    """P7 fold (luna re-gate 4): budget=2 with 3 queries stops after 2
    QUERIES even though each query has multiple pages (the old per-page
    counting stopped after 2 pages, silently skipping a full query)."""
    page_items = {
        "items": [
            {"repository": {"full_name": "acme/tool0", "stargazers_count": 5,
                            "html_url": "https://github.com/acme/tool0"}}
        ]
    }
    empty_items = {"items": []}
    responses = []
    for q in range(3):
        responses.append(FakeResp(200, page_items))           # search p1
        responses.append(FakeResp(200, {"default_branch": "main",
                                        "stargazers_count": 5,
                                        "pushed_at": "2026-08-01T00:00:00Z",
                                        "html_url": "https://github.com/acme/tool0"}))
        responses.append(FakeResp(200, {"sha": "s0"}))
        responses.append(FakeResp(200, empty_items))          # search p2 -> stop
    session = FakeSession(responses)
    result = run_search(session, queries=["q1", "q2", "q3"], query_budget=2,
                        max_pages=3, sleep_fn=lambda _s: None)
    assert result.queries_run == 2  # two QUERIES consumed, budget hit
    assert result.capped is True
    search_calls = [c for c in session.calls if "search/code" in c]
    assert len(search_calls) == 4  # q1 p1+p2, q2 p1+p2 — q3 never searched


def test_enrich_rate_limit_aborts_page_loop_without_extra_search():
    """P7 (luna re-gate 7): an enrich-repo rate limit must abort the run
    WITHOUT requesting the next search page. The item-loop break falls
    through to `if rate_limited: break` inside the page loop (search.py:304),
    so only ONE search_code call may ever fire."""
    page_items = {
        "items": [
            {"repository": {"full_name": "acme/tool0", "stargazers_count": 5,
                            "html_url": "https://github.com/acme/tool0"}},
            {"repository": {"full_name": "acme/tool1", "stargazers_count": 5,
                            "html_url": "https://github.com/acme/tool1"}},
        ]
    }
    session = FakeSession(
        responses=[
            FakeResp(200, page_items),          # q1 p1 search
            # enrich: 5x 429 exhausts the retry cap -> RateLimitError
            FakeResp(429, {}),
            FakeResp(429, {}),
            FakeResp(429, {}),
            FakeResp(429, {}),
            FakeResp(429, {}),
        ]
    )
    result = run_search(session, queries=["q1"], query_budget=10,
                        max_pages=3, sleep_fn=lambda _s: None)
    assert result.capped is True
    assert any("enrich rate-limited" in e for e in result.errors), result.errors
    search_calls = [c for c in session.calls if "search/code" in c]
    assert len(search_calls) == 1  # no page-2 search after the rate limit
