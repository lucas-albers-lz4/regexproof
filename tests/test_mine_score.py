"""Mine score-v1 allocator + rank CLI (#148)."""

from __future__ import annotations

import importlib.util
import json
import os
from datetime import date
from pathlib import Path

from regexproof.mine.ledger import empty_ledger, save_ledger
from regexproof.mine.score import SCORE_VERSION, candidate_score, rank_candidates
from regexproof.mine.search import SEARCH_QUERIES, SearchRunResult

ROOT = Path(__file__).resolve().parents[1]


def _load_mine_cli():
    spec = importlib.util.spec_from_file_location(
        "mine_cli_score", ROOT / "scripts" / "mine-corpus-candidates.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _load_rank_cli():
    spec = importlib.util.spec_from_file_location(
        "rank_cli", ROOT / "scripts" / "rank-mine-candidates.py"
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_security_high_stars_beats_testdata_low_stars():
    today = date(2026, 8, 9)
    security = {
        "url": "https://github.com/acme/gitleaks",
        "stars": 5000,
        "source_query": SEARCH_QUERIES[0],
        "pushed_date": "2026-07-01",
        "capped": False,
    }
    testdata = {
        "url": "https://github.com/acme/re-testdata",
        "stars": 3,
        "source_query": SEARCH_QUERIES[8],
        "pushed_date": "2020-01-01",
        "capped": True,
    }
    ranked = rank_candidates([testdata, security], today=today)
    assert ranked[0]["url"].endswith("/gitleaks")
    s_sec, _ = candidate_score(security, today=today)
    s_td, _ = candidate_score(testdata, today=today)
    assert s_sec > s_td


def test_boundary_false_ranks_below_unknown():
    today = date(2026, 8, 9)
    tutorial = {
        "url": "https://github.com/acme/awesome-regex-tutorial",
        "stars": 100,
        "source_query": SEARCH_QUERIES[3],
        "pushed_date": "2026-01-01",
    }
    unknown = {
        "url": "https://github.com/acme/octo-widget",
        "stars": 100,
        "source_query": SEARCH_QUERIES[3],
        "pushed_date": "2026-01-01",
    }
    ranked = rank_candidates([tutorial, unknown], today=today)
    assert ranked[0]["url"].endswith("/octo-widget")
    t_score, t_bd = candidate_score(tutorial, today=today)
    u_score, u_bd = candidate_score(unknown, today=today)
    assert t_bd["boundary"] == "deterministic-false"
    assert u_bd["boundary"] == "unknown"
    assert u_score > t_score


def test_assimilate_drains_highest_score_first():
    mod = _load_mine_cli()
    ledger = empty_ledger()
    queue = {
        "schema_version": "1",
        "items": [
            {
                "url": "https://github.com/queued/low-testdata",
                "default_branch": "main",
                "pin": "aaa",
                "pushed_date": "2026-07-01",
                "stars": 2,
                "source_query": SEARCH_QUERIES[8],
            },
            {
                "url": "https://github.com/queued/gitleaks-high",
                "default_branch": "main",
                "pin": "bbb",
                "pushed_date": "2026-08-01",
                "stars": 8000,
                "source_query": SEARCH_QUERIES[0],
            },
        ],
    }
    search = SearchRunResult(candidates=[])
    os.environ["DAILY_MINE_CAP"] = "1"
    try:
        accepted = mod.assimilate(
            search_result=search,
            ledger=ledger,
            queue=queue,
            admitted=set(),
            dry_run=True,
            now_iso="2026-08-09T00:00:00Z",
        )
        assert len(accepted) == 1
        assert accepted[0]["url"].endswith("/gitleaks-high")
        assert any(i["url"].endswith("/low-testdata") for i in queue["items"])
    finally:
        os.environ.pop("DAILY_MINE_CAP", None)


def test_rank_cli_prints_top(tmp_path: Path, capsys):
    ledger_path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    ledger["candidates"] = [
        {
            "url": "https://github.com/acme/re-testdata",
            "default_branch": "main",
            "pin": "x",
            "pushed_date": "2020-01-01",
            "stars": 2,
            "source_query": SEARCH_QUERIES[8],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
        {
            "url": "https://github.com/acme/gitleaks",
            "default_branch": "main",
            "pin": "y",
            "pushed_date": "2026-08-01",
            "stars": 9000,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
    ]
    save_ledger(ledger_path, ledger)
    mod = _load_rank_cli()
    rc = mod.main(["--ledger", str(ledger_path), "--limit", "1"])
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 1
    row = json.loads(lines[0])
    assert row["url"].endswith("/gitleaks")
    assert row["score_version"] == SCORE_VERSION
    assert "breakdown" in row


def test_rank_cli_skip_gated(tmp_path: Path, capsys):
    ledger_path = tmp_path / "candidate-ledger.json"
    gen = tmp_path / "generated"
    gen.mkdir()
    ledger = empty_ledger()
    ledger["candidates"] = [
        {
            "url": "https://github.com/acme/already-gated",
            "default_branch": "main",
            "pin": "x",
            "pushed_date": "2026-08-01",
            "stars": 9000,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
        {
            "url": "https://github.com/acme/fresh-mine",
            "default_branch": "main",
            "pin": "y",
            "pushed_date": "2026-08-01",
            "stars": 100,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-10T00:00:00Z",
            "status": "mined",
        },
    ]
    save_ledger(ledger_path, ledger)
    (gen / "already-gated_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "already-gated",
                "candidate_url": "https://github.com/acme/already-gated",
                "decision": "no-go",
            }
        ),
        encoding="utf-8",
    )
    mod = _load_rank_cli()
    rc = mod.main(
        [
            "--ledger",
            str(ledger_path),
            "--generated",
            str(gen),
            "--skip-gated",
            "--limit",
            "10",
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 1
    assert json.loads(lines[0])["url"].endswith("/fresh-mine")
