"""Security-tool disclosure gate + human-gated PR dry-run.

Policy: SECURITY.md (private-disclosure-first for security-tool corpora).
Field contracts: docs/REPORTING.md.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

SECURITY_TOOL_CORPORA = frozenset(
    {
        "gitleaks",
        "detect-secrets",
        "trufflehog",
        "coreruleset",
        "ids_rules",
        "semgrep_rules",
        "yara_rules",
        "spamassassin",
        "noseyparker",
        "shhgit",
        "dompurify",
        "everclaw-community-branches",
        "tracecat",
        "magic-js",
        "lonkero",
    }
)


def tag_disclosure(findings: list[dict[str, Any]], *, corpus: str) -> list[dict[str, Any]]:
    out = []
    for f in findings:
        rec = dict(f)
        if corpus in SECURITY_TOOL_CORPORA and rec.get("kind") in (
            "rule_diff",
            "property",
            "usage_mismatch",
            "intent_mismatch",
        ):
            rec["disclosure"] = "private_first"
        out.append(rec)
    return out


def write_pr_dry_run(
    path: Path,
    *,
    findings: list[dict[str, Any]],
    approval_path: Path | None = None,
) -> dict[str, Any]:
    """Write dry-run PR artifact. Never publishes without approval file."""
    approved = bool(approval_path and approval_path.is_file())
    private = [f for f in findings if f.get("disclosure") == "private_first"]
    artifact = {
        "schema_version": "1",
        "action": "dry_run",
        "would_open_public_upstream_issue": False,
        "approved": approved,
        "finding_count": len(findings),
        "private_first_count": len(private),
        "publish": False,
    }
    if approved:
        # Even with approval, this helper only records intent — no network publish.
        artifact["publish_intent"] = "human_approved_recorded"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return artifact


def assert_no_auto_publication(artifact: dict[str, Any]) -> None:
    if artifact.get("would_open_public_upstream_issue"):
        raise AssertionError("security-tool findings must not auto-open public upstream issues")
    if artifact.get("publish") and not artifact.get("approved"):
        raise AssertionError("publish without human approval")
