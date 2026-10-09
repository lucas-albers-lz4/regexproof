"""Mine score-v1 allocator + rank CLI (#148)."""

from __future__ import annotations

import importlib.util
import json
import os
from datetime import date
from pathlib import Path

from regexproof.mine.ledger import empty_ledger, save_ledger
from regexproof.mine.score import (
    SCORE_VERSION,
    SCORE_V2_WEIGHTS_PATH,
    _QUERY_FAMILY,
    _query_family,
    candidate_score,
    rank_candidates,
)
from regexproof.mine.score_v2 import auc, grouped_split, load_weights, sanity_check_v1_boundary
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
    # Default behavior: skip gated rows (no --skip-gated flag needed)
    rc = mod.main(
        [
            "--ledger",
            str(ledger_path),
            "--generated",
            str(gen),
            "--limit",
            "10",
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 1
    assert json.loads(lines[0])["url"].endswith("/fresh-mine")


def test_rank_cli_no_skip_gated(tmp_path: Path, capsys):
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
            "--no-skip-gated",
            "--limit",
            "10",
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 2


def test_rank_cli_skips_gated_status_rows(tmp_path: Path, capsys):
    ledger_path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    ledger["candidates"] = [
        {
            "url": "https://github.com/acme/gated-go",
            "default_branch": "main",
            "pin": "x",
            "pushed_date": "2026-08-01",
            "stars": 9000,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "gated:go",
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
    mod = _load_rank_cli()
    # Use --status "" to include ALL statuses — this proves skip-gated
    # actually filters gated:* rows, not the status filter.
    rc = mod.main(
        [
            "--ledger",
            str(ledger_path),
            "--status",
            "",
            "--limit",
            "10",
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 1
    assert json.loads(lines[0])["url"].endswith("/fresh-mine")


def test_every_search_query_has_family():
    """Fail-closed: any SEARCH_QUERIES addition must carry a family mapping."""
    assert set(SEARCH_QUERIES) <= set(_QUERY_FAMILY)
    for q in SEARCH_QUERIES:
        assert q in _QUERY_FAMILY, f"query missing family entry: {q}"
        assert _query_family(q) == _QUERY_FAMILY[q]


def test_new_query_families_are_classified():
    """The 2026-08-13 expanded queries resolve to the right families."""
    families = {q: f for q, f in zip(SEARCH_QUERIES, [_QUERY_FAMILY[q] for q in SEARCH_QUERIES])}
    # security expansion
    assert families[SEARCH_QUERIES[10]] == "security"  # .gitleaks.toml
    assert families[SEARCH_QUERIES[11]] == "security"  # .trufflehog
    assert families[SEARCH_QUERIES[12]] == "security"  # secretlintrc
    assert families[SEARCH_QUERIES[14]] == "security"  # secrets.yml/yaml
    # rules expansion (semgrep.yml + yara conventions)
    assert families[SEARCH_QUERIES[13]] == "rules"     # semgrep.yml/yaml
    assert families[SEARCH_QUERIES[15]] == "rules"     # index.yar
    assert families[SEARCH_QUERIES[16]] == "rules"     # path:signatures extension:yar
    assert families[SEARCH_QUERIES[17]] == "rules"     # rules.yar path:rules
    # validators expansion
    assert families[SEARCH_QUERIES[18]] == "validators"
    # testdata expansion (go)
    assert families[SEARCH_QUERIES[19]] == "testdata"
    # fuzzy fallback agrees with exact map
    for q in SEARCH_QUERIES:
        assert _query_family(q) == _QUERY_FAMILY[q]


def test_fuzzy_fallback_classifies_drifted_queries():
    """Strings NOT in the exact map must still classify via the fuzzy fallback."""
    drifted = [
        ("filename:gitleaks.toml", "security"),            # dropped the OR branch
        ("path:config filename:trufflehog.yml", "security"),
        ("filename:secretlintrc", "security"),             # dropped extension
        ("filename:secrets.yml", "security"),              # dropped path:config
        ("filename:index.yar", "rules"),                   # yara index convention
        ("filename:rules.yar", "rules"),
        ("filename:regexp_test.go", "testdata"),
        ("filename:regex_test.go", "testdata"),
        ("filename:validator.py", "validators"),
    ]
    for q, expected in drifted:
        assert _query_family(q) == expected, f"drifted {q!r} -> {_query_family(q)}, want {expected}"


def test_score_v2_auc_is_pure_python_and_tie_aware():
    assert auc([0.9, 0.1, 0.5, 0.5], [1, 0, 1, 0]) == 0.875


def test_score_v2_grouped_split_keeps_duplicate_urls_together():
    rows = [
        {"url": "https://github.com/acme/same", "label": "go"},
        {"url": "https://github.com/acme/same/", "label": "no-go"},
        *[
            {"url": f"https://github.com/acme/repo-{index}", "label": "no-go"}
            for index in range(8)
        ],
    ]
    folds = grouped_split(rows, seed=432)
    locations = {
        id(row): fold
        for fold, rows_in_fold in enumerate(folds)
        for row in rows_in_fold
    }
    assert locations[id(rows[0])] == locations[id(rows[1])]


def test_score_v2_sanity_harness_reproduces_v1_boundary_order():
    result = sanity_check_v1_boundary()
    assert result["passed"] is True
    assert result["verdicts"] == [
        "deterministic-true",
        "unknown",
        "deterministic-false",
    ]


def test_rank_cli_score_v2_tags_allocator(tmp_path: Path, capsys):
    ledger_path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    ledger["candidates"] = [
        {
            "url": "https://github.com/acme/v2-candidate",
            "default_branch": "main",
            "pin": "x",
            "pushed_date": "2026-08-01",
            "stars": 100,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
            "fork": False,
            "size": 10,
            "language": "Python",
            "archived": False,
        }
    ]
    save_ledger(ledger_path, ledger)
    mod = _load_rank_cli()
    assert mod.main([
        "--ledger", str(ledger_path),
        "--allocator", "score-v2",
        "--limit", "1",
    ]) == 0
    row = json.loads(capsys.readouterr().out)
    assert row["allocator"] == "score-v2"
    assert row["score_version"] == "v2"
    probe = (row.get("features") or {}).get("tree_probe") or {}
    assert probe.get("reason") != "missing-probed-pin"


def test_score_v2_weights_name_label_reproduction():
    art = load_weights(SCORE_V2_WEIGHTS_PATH)
    assert art["default_allocator"] == "score-v1"
    assert art["holdout_positive_count"] == 16
    assert "label_reproduction_auc" in art
    assert art["label_reproduction_auc"] == art["holdout_auc"]


def test_score_v2_tree_lookup_is_pin_aware():
    base = {
        "url": "https://github.com/acme/pin-sensitive",
        "stars": 100,
        "source_query": SEARCH_QUERIES[0],
        "pushed_date": "2026-08-01",
        "fork": False,
        "size": 10,
        "language": "Python",
        "archived": False,
    }
    old_pin = {**base, "pin_probed": "OLD"}
    new_pin = {**base, "pin_probed": "NEW"}
    features = {
        (base["url"], "OLD"): {
            "complete": True,
            "security_boundary": "deterministic-false",
            "path_count": 1,
            "regex_file_type_counts": {},
            "truncated": False,
        },
        (base["url"], "NEW"): {
            "complete": True,
            "security_boundary": "deterministic-true",
            "path_count": 1,
            "regex_file_type_counts": {},
            "truncated": False,
        },
    }
    ranked = rank_candidates(
        [old_pin, new_pin],
        allocator="score-v2",
        tree_features=features,
    )
    assert ranked[0]["pin_probed"] == "NEW"


def test_rank_cli_exclude_family_rules(tmp_path: Path, capsys):
    """--exclude-family rules drops YARA/rules source_query after score."""
    ledger_path = tmp_path / "candidate-ledger.json"
    ledger = empty_ledger()
    ledger["candidates"] = [
        {
            "url": "https://github.com/acme/yara-pack",
            "default_branch": "main",
            "pin": "a",
            "pushed_date": "2026-08-01",
            "stars": 9000,
            "source_query": SEARCH_QUERIES[6],  # path:rules extension:yar
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
        {
            "url": "https://github.com/acme/gitleaks",
            "default_branch": "main",
            "pin": "b",
            "pushed_date": "2026-08-01",
            "stars": 100,
            "source_query": SEARCH_QUERIES[0],  # security
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
    ]
    save_ledger(ledger_path, ledger)
    mod = _load_rank_cli()
    rc = mod.main(
        [
            "--ledger",
            str(ledger_path),
            "--exclude-family",
            "rules",
            "--limit",
            "10",
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 1
    assert json.loads(lines[0])["url"].endswith("/gitleaks")
    assert _query_family(SEARCH_QUERIES[6]) == "rules"


def test_rank_cli_decision_go_fail_closed(tmp_path: Path, capsys):
    """--no-skip-gated --decision go keeps GO only; missing decision drops."""
    ledger_path = tmp_path / "candidate-ledger.json"
    gen = tmp_path / "generated"
    gen.mkdir()
    ledger = empty_ledger()
    ledger["candidates"] = [
        {
            "url": "https://github.com/acme/go-corpus",
            "default_branch": "main",
            "pin": "g",
            "pushed_date": "2026-08-01",
            "stars": 50,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
        {
            "url": "https://github.com/acme/nogo-corpus",
            "default_branch": "main",
            "pin": "n",
            "pushed_date": "2026-08-01",
            "stars": 9000,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
        {
            "url": "https://github.com/acme/ungated-mine",
            "default_branch": "main",
            "pin": "u",
            "pushed_date": "2026-08-01",
            "stars": 8000,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
    ]
    save_ledger(ledger_path, ledger)
    (gen / "go-corpus_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "go-corpus",
                "candidate_url": "https://github.com/acme/go-corpus",
                "decision": "go",
            }
        ),
        encoding="utf-8",
    )
    (gen / "nogo-corpus_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "nogo-corpus",
                "candidate_url": "https://github.com/acme/nogo-corpus",
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
            "--no-skip-gated",
            "--decision",
            "go",
            "--limit",
            "10",
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 1
    assert json.loads(lines[0])["url"].endswith("/go-corpus")


def test_rank_cli_decision_requires_no_skip_gated(tmp_path: Path, capsys):
    ledger_path = tmp_path / "candidate-ledger.json"
    save_ledger(ledger_path, empty_ledger())
    mod = _load_rank_cli()
    rc = mod.main(
        ["--ledger", str(ledger_path), "--decision", "go", "--limit", "1"]
    )
    assert rc == 2
    err = capsys.readouterr().err
    assert "--decision requires --no-skip-gated" in err


def test_rank_cli_decision_rejects_bare_triage(tmp_path: Path):
    """Schema enum is triage-trial, not triage — argparse must refuse."""
    import pytest

    ledger_path = tmp_path / "candidate-ledger.json"
    save_ledger(ledger_path, empty_ledger())
    mod = _load_rank_cli()
    with pytest.raises(SystemExit) as exc:
        mod.main(
            [
                "--ledger",
                str(ledger_path),
                "--no-skip-gated",
                "--decision",
                "triage",
            ]
        )
    assert exc.value.code == 2


def test_rank_cli_skips_non_object_gate_json(tmp_path: Path, capsys):
    """Malformed/non-object gate JSON must not crash; fail-closed skip."""
    ledger_path = tmp_path / "candidate-ledger.json"
    gen = tmp_path / "generated"
    gen.mkdir()
    ledger = empty_ledger()
    ledger["candidates"] = [
        {
            "url": "https://github.com/acme/go-corpus",
            "default_branch": "main",
            "pin": "g",
            "pushed_date": "2026-08-01",
            "stars": 50,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
    ]
    save_ledger(ledger_path, ledger)
    (gen / "broken_gate_decision.json").write_text("[]\n", encoding="utf-8")
    (gen / "go-corpus_gate_decision.json").write_text(
        json.dumps(
            {
                "schema_version": "1",
                "corpus": "go-corpus",
                "candidate_url": "https://github.com/acme/go-corpus",
                "decision": "go",
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
            "--no-skip-gated",
            "--decision",
            "go",
            "--limit",
            "10",
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 1
    assert json.loads(lines[0])["url"].endswith("/go-corpus")


def test_rank_cli_default_skip_gated_tolerates_non_object_gate(
    tmp_path: Path, capsys
):
    """Default skip-gated path uses load_admitted_urls — must not crash on []."""
    ledger_path = tmp_path / "candidate-ledger.json"
    gen = tmp_path / "generated"
    gen.mkdir()
    ledger = empty_ledger()
    ledger["candidates"] = [
        {
            "url": "https://github.com/acme/fresh-mine",
            "default_branch": "main",
            "pin": "f",
            "pushed_date": "2026-08-01",
            "stars": 100,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-10T00:00:00Z",
            "status": "mined",
        },
        {
            "url": "https://github.com/acme/already-gated",
            "default_branch": "main",
            "pin": "a",
            "pushed_date": "2026-08-01",
            "stars": 9000,
            "source_query": SEARCH_QUERIES[0],
            "first_seen": "2026-08-09T00:00:00Z",
            "status": "mined",
        },
    ]
    save_ledger(ledger_path, ledger)
    (gen / "broken_gate_decision.json").write_text("[]\n", encoding="utf-8")
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
            "--limit",
            "10",
        ]
    )
    assert rc == 0
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert len(lines) == 1
    assert json.loads(lines[0])["url"].endswith("/fresh-mine")
