"""Phase 7 docs contracts: verified findings, taxonomy, NDJSON ≡ AGENTS."""

from __future__ import annotations

import json
import re
from pathlib import Path

from regexproof.kinds import CALL_KINDS, DIALECTS, PROPERTY_KINDS
from regexproof.schemas import scanner_finding_schema

ROOT = Path(__file__).resolve().parents[1]


def _findings() -> list[dict]:
    path = ROOT / "docs" / "verified-findings.jsonl"
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


def test_verified_findings_covered_in_docs_entry():
    for rec in _findings():
        rel = rec["docs_entry"]
        path = ROOT / rel
        assert path.is_file(), rec["id"]
        text = path.read_text(encoding="utf-8")
        assert rec["id"] in text, f"{rec['id']} missing from {rel}"
        assert f"verified-finding: {rec['id']}" in text or rec["id"] in text


def test_verified_findings_unique_ids():
    ids = [r["id"] for r in _findings()]
    assert ids
    assert len(ids) == len(set(ids))
    for i in ids:
        assert re.fullmatch(r"VF-\d{3}", i), i


def test_agents_ndjson_contract_matches_cli_markers():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    # Markers required by Phase 7 AC (semantic equivalence with z3-verify help).
    for needle in (
        "--json-legacy",
        "schema_version",
        "not_proven",
        "Mutually exclusive",
        "Partial streams remain valid",
        "engine_versions",
    ):
        assert needle in agents, needle
    help_doc = (ROOT / "scripts" / "z3-verify.py").read_text(encoding="utf-8")
    assert "--json-legacy" in help_doc
    assert "schema_version" in help_doc
    assert "not_proven" in help_doc
    assert "Mutually exclusive with --json-legacy" in help_doc or (
        "Mutually exclusive with `--json-legacy`" in help_doc
    )


def test_taxonomy_in_docs_matches_kinds():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    semantics = (ROOT / "docs" / "SEMANTICS.md").read_text(encoding="utf-8")
    for kind in PROPERTY_KINDS:
        # bug_demo / rule_diff etc. must appear somewhere in AGENTS kind list or examples
        assert kind in agents or kind in semantics, kind
    for ck in CALL_KINDS:
        assert f"`{ck}`" in semantics or ck in semantics, ck
    for d in DIALECTS:
        assert f"`{d}`" in semantics or d in semantics, d
    scanner_kinds = set(scanner_finding_schema()["properties"]["kind"]["enum"])
    for sk in scanner_kinds:
        assert sk in agents or sk in (ROOT / "docs" / "REPORTING.md").read_text(), sk


def test_security_and_reporting_linked():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "SECURITY.md" in agents
    assert "REPORTING.md" in agents
    assert (ROOT / "SECURITY.md").is_file()
    assert (ROOT / "docs" / "REPORTING.md").is_file()
    assert (ROOT / "docs" / "examples" / "shape5-rule_diff.md").is_file()
    disclose = (ROOT / "regexproof" / "batch" / "disclose.py").read_text(encoding="utf-8")
    assert "SECURITY.md" in disclose
