"""Keep selected corpus README Smith summaries aligned with decisions."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_readme_smith_decisions_match_artifacts():
    expected = [
        ("inhale", "306/372 = 0.8226 encodable"),
        ("llm-honeypot-intelligence", "68/68 = 1.0000 encodable"),
        ("devguard", "9/9 = 1.0000 encodable"),
        ("Doberman-Core", "40/69 = 0.5797 encodable"),
    ]
    for corpus, fraction in expected:
        artifact_path = ROOT / "properties" / "generated" / f"{corpus}_smith_decision.json"
        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        readme = " ".join(
            (ROOT / "batch" / "corpora" / corpus / "README.md")
            .read_text(encoding="utf-8")
            .split()
        )

        assert artifact["corpus"] == corpus
        assert artifact["smith_decision"] == "go"
        assert artifact["supersedes"] == "triage-trial"
        assert (
            f"Smith: `properties/generated/{corpus}_smith_decision.json` "
            f"(`go`; supersedes `triage-trial`; {fraction})."
        ) in readme
        assert "for Smith triage-trial keep" not in readme
