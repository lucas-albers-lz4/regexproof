"""P6 label materialization and budgeted tree-probe coverage."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from regexproof.mine.ledger import empty_ledger
from regexproof.mine.search import SearchRunResult
from regexproof.mine.tree import TreeCache, _repo_slug, materialize_tree_features

ROOT = Path(__file__).resolve().parents[1]


class _Response:
    def __init__(self, status_code: int, payload: dict):
        self.status_code = status_code
        self._payload = payload
        self.text = json.dumps(payload)

    def json(self):
        return self._payload


class _Session:
    def __init__(self, responses: list[_Response]):
        self.responses = list(responses)
        self.urls: list[str] = []

    def get(self, url, *, headers=None, params=None, timeout=30):
        self.urls.append(url)
        return self.responses.pop(0)


def _load_labels_script():
    spec = importlib.util.spec_from_file_location(
        "build_gate_labels", ROOT / "scripts" / "build-gate-labels.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_tree_probe_uses_probed_pin_and_budget(tmp_path: Path):
    session = _Session(
        [
            _Response(
                200,
                {
                    "truncated": False,
                    "tree": [
                        {"path": "src/sanitizer.py", "type": "blob"},
                        {"path": "README.md", "type": "blob"},
                    ],
                },
            )
        ]
    )
    cache = TreeCache(tmp_path / "tree.json")
    features, calls = materialize_tree_features(
        session,
        [
            {
                "url": "https://github.com/acme/tool",
                "pin": "MINED",
                "pin_probed": "PROBED",
            },
            {
                "url": "https://github.com/acme/other",
                "pin": "MINED2",
                "pin_probed": "PROBED2",
            },
        ],
        budget=1,
        cache=cache,
    )
    assert calls == 1
    assert session.urls == [
        "https://api.github.com/repos/acme/tool/git/trees/PROBED"
    ]
    first = features[("https://github.com/acme/tool", "PROBED")]
    assert first["complete"] is True
    assert first["security_boundary"] == "deterministic-true"
    assert first["regex_file_type_counts"] == {".py": 1}
    assert features[("https://github.com/acme/other", "PROBED2")]["reason"] == "budget-exhausted"

    cache.save()
    second_session = _Session([])
    cached, cached_calls = materialize_tree_features(
        second_session,
        [{"url": "https://github.com/acme/tool", "pin_probed": "PROBED"}],
        budget=0,
        cache=TreeCache(tmp_path / "tree.json"),
    )
    assert cached_calls == 0
    assert second_session.urls == []
    assert cached[("https://github.com/acme/tool", "PROBED")]["complete"] is True


def test_repo_slug_normalizes_url_variants():
    assert _repo_slug("https://github.com/Acme/Tool.git") == "acme/tool"
    assert _repo_slug("http://github.com/acme/tool") == "acme/tool"
    assert _repo_slug("github.com/Acme/Tool") == "acme/tool"
    assert _repo_slug("www.github.com/acme/tool") == "acme/tool"
    assert _repo_slug("acme/tool") == "acme/tool"
    assert _repo_slug("git@github.com:acme/tool.git") == "acme/tool"
    assert _repo_slug("") == ""
    # Incomplete substring must not treat github.com.evil.com as github.com.
    assert _repo_slug("https://github.com.evil.com/acme/tool") != "acme/tool"
    assert _repo_slug("git@gitlab.com:owner/repo") != "owner/repo"
    assert _repo_slug("git@github.com.evil.com:owner/repo") != "owner/repo"


def test_tree_probe_slug_from_http_and_host_prefix(tmp_path: Path):
    session = _Session(
        [
            _Response(
                200,
                {
                    "truncated": False,
                    "tree": [{"path": "src/sanitizer.py", "type": "blob"}],
                },
            ),
            _Response(
                200,
                {
                    "truncated": False,
                    "tree": [{"path": "src/sanitizer.py", "type": "blob"}],
                },
            ),
        ]
    )
    cache = TreeCache(tmp_path / "tree.json")
    features, calls = materialize_tree_features(
        session,
        [
            {"url": "http://github.com/Acme/Tool.git", "pin_probed": "HEAD"},
            {"url": "github.com/acme/other", "pin_probed": "PIN"},
        ],
        budget=2,
        cache=cache,
    )
    assert calls == 2
    assert session.urls == [
        "https://api.github.com/repos/acme/tool/git/trees/HEAD",
        "https://api.github.com/repos/acme/other/git/trees/PIN",
    ]
    assert features[("https://github.com/acme/tool", "HEAD")]["complete"] is True
    assert features[("https://github.com/acme/other", "PIN")]["complete"] is True


def test_truncated_tree_contributes_no_signal(tmp_path: Path):
    session = _Session([_Response(200, {"truncated": True, "tree": []})])
    features, _calls = materialize_tree_features(
        session,
        [{"url": "https://github.com/acme/gitleaks", "pin_probed": "HEAD"}],
        budget=1,
        cache=TreeCache(tmp_path / "tree.json"),
    )
    feature = features[("https://github.com/acme/gitleaks", "HEAD")]
    assert feature["complete"] is False
    assert feature["truncated"] is True
    assert feature["security_boundary"] == "unknown"
    assert feature["regex_file_type_counts"] == {}


def test_gate_labels_join_is_deterministic_and_dedupes_duplicate_urls(tmp_path: Path):
    script = _load_labels_script()
    generated = tmp_path / "generated"
    generated.mkdir()
    ledger_path = tmp_path / "ledger.json"
    ledger_path.write_text(
        json.dumps(
            {
                "schema_version": "1",
                "candidates": [
                    {
                        "url": "https://github.com/acme/tool",
                        "stars": 3,
                        "pushed_date": "2026-01-01",
                        "source_query": "q",
                        "capped": False,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    decision = {
        "candidate_url": "https://github.com/acme/tool",
        "decision": "go",
        "decision_date": "2026-08-13",
        "probe": {
            "regex_sites": 2,
            "dialect": {"py_re": 2},
            "predicted_buckets": {"inline-flag": 1},
            "security_boundary": "unknown",
        },
    }
    for name in ("a_gate_decision.json", "b_gate_decision.json"):
        (generated / name).write_text(json.dumps(decision), encoding="utf-8")
    out = tmp_path / "labels.json"
    first = script.build_gate_labels(
        ledger_path=ledger_path,
        generated_dir=generated,
        output_path=out,
    )
    first_bytes = out.read_bytes()
    second = script.build_gate_labels(
        ledger_path=ledger_path,
        generated_dir=generated,
        output_path=out,
    )
    assert first == second
    assert out.read_bytes() == first_bytes
    assert len(first["rows"]) == 1
    assert first["provenance"]["input_file_count"] == 2
    ledger_path.write_text(
        ledger_path.read_text(encoding="utf-8").replace('"stars": 3', '"stars": 4'),
        encoding="utf-8",
    )
    after_ledger = script.build_gate_labels(
        ledger_path=ledger_path,
        generated_dir=generated,
        output_path=out,
    )
    assert after_ledger["provenance"]["inputs_hash"] != first["provenance"]["inputs_hash"]


def test_list_gate_decision_paths_falls_back_to_glob_outside_repo(tmp_path: Path):
    from regexproof.mine.gate_files import git_ls_decision_paths, list_gate_decision_paths

    generated = tmp_path / "generated"
    generated.mkdir()
    (generated / "acme_gate_decision.json").write_text("{}", encoding="utf-8")
    assert git_ls_decision_paths(generated) is None
    paths = list_gate_decision_paths(generated)
    assert [p.name for p in paths] == ["acme_gate_decision.json"]
    script = _load_labels_script()
    generated = ROOT / "properties" / "generated"
    tracked = script._git_ls_decision_paths(generated)
    assert tracked is not None
    assert tracked == script._decision_paths(generated)
    assert any(path.name.endswith("_gate_decision.json") for path in tracked)
    tmp_only = generated.parent.parent / "no-such-generated-for-labels-test"
    assert script._git_ls_decision_paths(tmp_only) is None


def test_read_repo_bytes_keeps_git_spelling_without_resolve(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    from regexproof.mine import gate_files as gf

    root = tmp_path / "repo"
    generated = root / "properties" / "generated"
    generated.mkdir(parents=True)
    (generated / "validator_gate_decision.json").write_bytes(b"disk-folded")
    calls: list[list[str]] = []

    def fake_run(cmd, **kwargs):
        calls.append(list(cmd))

        class Proc:
            returncode = 0
            stdout = b'{"corpus":"Validator"}'

        return Proc()

    monkeypatch.setattr(gf.subprocess, "run", fake_run)
    data = gf.read_repo_bytes(
        generated / "Validator_gate_decision.json", repo_root=root
    )
    assert data == b'{"corpus":"Validator"}'
    spec = "HEAD:properties/generated/Validator_gate_decision.json"
    assert any(spec in cmd for cmd in calls)


def test_assimilate_persists_enrichment_fields():
    mine_spec = importlib.util.spec_from_file_location(
        "mine_corpus_candidates", ROOT / "scripts" / "mine-corpus-candidates.py"
    )
    assert mine_spec is not None and mine_spec.loader is not None
    mine = importlib.util.module_from_spec(mine_spec)
    mine_spec.loader.exec_module(mine)
    ledger = empty_ledger()
    queue = {"schema_version": "1", "items": []}
    accepted = mine.assimilate(
        search_result=SearchRunResult(
            candidates=[
                {
                    "url": "https://github.com/acme/tool",
                    "pin": "MINED",
                    "pin_probed": "PROBED",
                    "stars": 4,
                    "source_query": "q",
                    "fork": True,
                    "size": 12,
                    "language": "Python",
                    "archived": False,
                }
            ]
        ),
        ledger=ledger,
        queue=queue,
        admitted=set(),
        dry_run=True,
        now_iso="2026-08-13T00:00:00Z",
    )
    assert len(accepted) == 1
    assert accepted[0]["fork"] is True
    assert accepted[0]["size"] == 12
    assert accepted[0]["language"] == "Python"
    assert accepted[0]["archived"] is False
    assert accepted[0]["pin_probed"] == "PROBED"
