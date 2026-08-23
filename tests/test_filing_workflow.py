"""Wave B (#556): approval_missing escape enforcement + filing CLI.

The filing workflow must never produce a dead-end: ``approval_missing``
requires an escape (approval_present + ref, or wont_file + reason_code),
and the recording CLI enforces the same rules the coverage checker does."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


check = _load("rp_check_b", "scripts/check-disposition-coverage.py")
record = _load("rp_record_b", "scripts/record-filing-decision.py")


def _curated(**overrides):
    row = {
        "id": "CU-901",
        "corpus": "demo",
        "status": "filed_plan",
        "kind": "property",
        "language_membership": True,
        "site": "net/demo/files/etc/init.d/demo:42:is_host",
        "question_id": "no-semicolon-in-hostname",
        "filed_at": "2026-08-20",
    }
    row.update(overrides)
    return row


def _gen_dir(tmp_path: Path, *rows) -> Path:
    gen = tmp_path / "generated"
    gen.mkdir(exist_ok=True)
    (gen / "demo_conversion.ndjson").write_text(
        "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8"
    )
    return gen


def _gt_row(**overrides):
    row = {
        "schema_version": "1",
        "kind": "property",
        "result": "sat",
        "regex_id": "a" * 32,
        "corpus": "demo",
        "site": "net/demo/files/etc/init.d/demo:42:is_host",
        "question_id": "no-semicolon-in-hostname",
        "ground_truth_status": "reproduced",
        "synthesized": False,
        "wave_id": "demo_w1",
        "idiom_bucket": "validator-charsets",
    }
    row.update(overrides)
    return row


def _write_upstream(path: Path, *rows) -> Path:
    # The coverage check requires exactly one curated disposition mentioning
    # CRS 942220 (the guard asserts one curated row per rule).
    rows = (
        *rows,
        {
            "id": "CU-005",
            "corpus": "coreruleset",
            "status": "false_positive",
            "kind": "version_diff",
            "language_membership": True,
            "rule": "942220",
        },
    )
    path.write_text(
        "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8"
    )
    return path


# --- checker: approval_missing escape enforcement -------------------------


def test_approval_missing_without_escape_fails(tmp_path: Path):
    gen = _gen_dir(tmp_path, _gt_row())
    curated = _write_upstream(
        tmp_path / "upstream.jsonl",
        _curated(status="approval_missing"),
    )
    with pytest.raises(SystemExit, match="approval_escape"):
        check.run(gen, curated)


def test_approval_missing_approval_present_requires_ref(tmp_path: Path):
    gen = _gen_dir(tmp_path, _gt_row())
    curated = _write_upstream(
        tmp_path / "upstream.jsonl",
        _curated(status="approval_missing", approval_escape="approval_present"),
    )
    with pytest.raises(SystemExit, match="approval_ref"):
        check.run(gen, curated)


def test_approval_missing_wont_file_requires_reason(tmp_path: Path):
    gen = _gen_dir(tmp_path, _gt_row())
    curated = _write_upstream(
        tmp_path / "upstream.jsonl",
        _curated(status="approval_missing", approval_escape="wont_file"),
    )
    with pytest.raises(SystemExit, match="reason_code"):
        check.run(gen, curated)


def test_approval_missing_with_valid_escape_passes(tmp_path: Path):
    gen = _gen_dir(tmp_path, _gt_row())
    curated = _write_upstream(
        tmp_path / "upstream.jsonl",
        _curated(
            status="approval_missing",
            approval_escape="approval_present",
            approval_ref=".approvals/CU-901.json",
        ),
    )
    assert check.run(gen, curated) == 0


def test_approval_missing_wont_file_escape_passes(tmp_path: Path):
    gen = _gen_dir(tmp_path, _gt_row())
    curated = _write_upstream(
        tmp_path / "upstream.jsonl",
        _curated(
            status="approval_missing",
            approval_escape="wont_file",
            reason_code="maintainer_declined",
        ),
    )
    assert check.run(gen, curated) == 0


# --- filing CLI ------------------------------------------------------------


def _cli_args(tmp_path: Path, curated_path: Path, *extra: str) -> list[str]:
    return [
        sys.executable,
        str(ROOT / "scripts" / "record-filing-decision.py"),
        "--curated",
        str(curated_path),
        *extra,
    ]


def test_cli_records_filed_with_date(tmp_path: Path):
    curated = _write_upstream(tmp_path / "upstream.jsonl", _curated())
    r = subprocess.run(
        _cli_args(
            tmp_path, curated, "--id", "CU-901", "--status", "filed",
            "--reason", "opened upstream", "--filed-at", "2026-08-23",
        ),
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr
    rows = [json.loads(line) for line in curated.read_text().splitlines() if line.strip()]
    row = rows[0]
    assert row["status"] == "filed"
    assert row["filed_at"] == "2026-08-23"
    # The recorded row must satisfy the checker.
    gen = _gen_dir(tmp_path, _gt_row())
    assert check.run(gen, curated) == 0


def test_cli_approval_missing_requires_escape(tmp_path: Path):
    curated = _write_upstream(tmp_path / "upstream.jsonl", _curated())
    r = subprocess.run(
        _cli_args(tmp_path, curated, "--id", "CU-901",
                  "--status", "approval_missing", "--reason", "blocked"),
        capture_output=True,
        text=True,
    )
    assert r.returncode != 0
    assert "approval-escape" in r.stderr


def test_cli_approval_missing_approval_present(tmp_path: Path):
    curated = _write_upstream(tmp_path / "upstream.jsonl", _curated())
    r = subprocess.run(
        _cli_args(
            tmp_path, curated, "--id", "CU-901", "--status", "approval_missing",
            "--approval-escape", "approval_present",
            "--approval-ref", ".approvals/CU-901.json",
        ),
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr
    rows = [json.loads(line) for line in curated.read_text().splitlines() if line.strip()]
    assert rows[0]["status"] == "approval_missing"
    assert rows[0]["approval_escape"] == "approval_present"
    assert rows[0]["approval_ref"] == ".approvals/CU-901.json"
    gen = _gen_dir(tmp_path, _gt_row())
    assert check.run(gen, curated) == 0


def test_cli_approval_missing_wont_file_escape(tmp_path: Path):
    curated = _write_upstream(tmp_path / "upstream.jsonl", _curated())
    r = subprocess.run(
        _cli_args(
            tmp_path, curated, "--id", "CU-901", "--status", "approval_missing",
            "--approval-escape", "wont_file", "--reason-code", "maintainer_declined",
        ),
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr
    rows = [json.loads(line) for line in curated.read_text().splitlines() if line.strip()]
    assert rows[0]["approval_escape"] == "wont_file"
    assert rows[0]["reason_code"] == "maintainer_declined"
    gen = _gen_dir(tmp_path, _gt_row())
    assert check.run(gen, curated) == 0


def test_cli_rejects_unknown_id(tmp_path: Path):
    curated = _write_upstream(tmp_path / "upstream.jsonl", _curated())
    r = subprocess.run(
        _cli_args(tmp_path, curated, "--id", "CU-999", "--status", "filed",
                  "--reason", "x", "--filed-at", "2026-08-23"),
        capture_output=True,
        text=True,
    )
    assert r.returncode != 0
    assert "no curated row" in r.stderr


def test_cli_filing_status_requires_date(tmp_path: Path):
    curated = _write_upstream(tmp_path / "upstream.jsonl", _curated())
    r = subprocess.run(
        _cli_args(tmp_path, curated, "--id", "CU-901", "--status", "filed",
                  "--reason", "opened"),
        capture_output=True,
        text=True,
    )
    assert r.returncode != 0
    assert "--filed-at" in r.stderr


def test_cli_records_on_phase_a_backfilled_row(tmp_path: Path):
    """CU-011..014 (Phase A backfills) are the first test input: a GT-
    confirmed SAT row can record a filing disposition end-to-end."""
    curated = _write_upstream(
        tmp_path / "upstream.jsonl",
        _curated(
            id="CU-011",
            status="wont_file",
            backfilled=True,
            reason_code="legacy_predates_date_requirement",
            disposition_date="unknown_date",
            site="net/ddns-scripts/files/usr/lib/ddns/update_transip_nl.sh:96:token",
            question_id="OW-packages-transip-token-truncation",
        ),
    )
    r = subprocess.run(
        _cli_args(
            tmp_path, curated, "--id", "CU-011", "--status", "filed",
            "--reason", "upstream opened", "--filed-at", "2026-08-23",
        ),
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stderr
    rows = [json.loads(line) for line in curated.read_text().splitlines() if line.strip()]
    assert rows[0]["status"] == "filed"
    assert rows[0]["filed_at"] == "2026-08-23"
    gen = _gen_dir(
        tmp_path,
        _gt_row(
            site="net/ddns-scripts/files/usr/lib/ddns/update_transip_nl.sh:96:token",
            question_id="OW-packages-transip-token-truncation",
        ),
    )
    assert check.run(gen, curated) == 0
