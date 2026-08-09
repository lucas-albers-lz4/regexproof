"""P4 B2: java→pcre extractor + fixture triage (#133)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import jsonschema

from regexproof.admission.java_pin import JAVA_HTML_SANITIZER_PIN
from regexproof.admission.serialize import dumps_pinned
from regexproof.extractors.java_pattern import (
    APPROXIMATION,
    extract_java_pattern,
    java_reject_reason,
)
from regexproof.schemas import gate_decision_schema

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "admission" / "java_sites"
GENERATED = ROOT / "properties" / "generated"
TRIAGE = ROOT / "scripts" / "java-html-sanitizer-triage.py"


def test_java_reject_unicode_quote_and_parse_error():
    assert java_reject_reason(r"\p{L}+") == "unicode-property"
    assert java_reject_reason(r"\Qfoo\E") == "quote"
    assert java_reject_reason("(ab") == "parse-error"
    assert java_reject_reason("abc+") is None


def test_extract_java_pattern_marks_approximation():
    src = 'Pattern.compile("(?i)center|left|right");\n'
    recs = extract_java_pattern(src, repo="fixture", file="X.java")
    assert len(recs) == 1
    rec = recs[0]
    assert rec["dialect"] == "pcre"
    assert rec["source_dialect"] == "java"
    assert rec["approximation"] == APPROXIMATION
    assert rec["flags"] == "i"
    assert rec["pattern"] == "center|left|right"
    assert not rec.get("unencodable_reason")


def test_fixture_triage_zero_disagreement(tmp_path: Path):
    out = tmp_path / "out"
    proc = subprocess.run(
        [sys.executable, str(TRIAGE.resolve()), "--fixture", "-o", str(out.resolve())],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout
    summary = json.loads(proc.stdout)
    assert summary["total_sites"] == 22
    assert summary["encodable"] == 22
    assert summary["differential_zero_disagreement_pass"] is True
    assert summary["approximation"] == APPROXIMATION
    frac = json.loads((out / "java-html-sanitizer_encodable_fraction.json").read_text())
    assert frac["differential_ok"] == 22
    assert (out / "java-html-sanitizer_triage.ndjson").is_file()
    assert (out / "java-html-sanitizer_batch.md").is_file()


def test_committed_gate_decision_supersedes_trial():
    path = GENERATED / "java-html-sanitizer_gate_decision.json"
    decision = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=decision, schema=gate_decision_schema())
    assert decision["decision"] == "go"
    assert decision["decision_basis"] == "escape_hatch"
    assert decision["escape_hatch_applied"] is True
    assert decision["corpus_pin"] == JAVA_HTML_SANITIZER_PIN
    assert decision["fraction_decision"] == "go"
    # Byte-stable key order for dumps_pinned contract
    assert path.read_text(encoding="utf-8") == dumps_pinned(decision)


def test_committed_fraction_artifact():
    frac = json.loads(
        (GENERATED / "java-html-sanitizer_encodable_fraction.json").read_text(
            encoding="utf-8"
        )
    )
    assert frac["corpus_pin"] == JAVA_HTML_SANITIZER_PIN
    assert frac["encodable_fraction"] >= 0.30
    assert frac["differential_zero_disagreement_pass"] is True
    assert frac["approximation"] == APPROXIMATION


def test_fixture_still_reports_java_22():
    from regexproof.admission.walk import walk_repo

    walked = walk_repo(FIXTURE, repo_name="java-html-sanitizer")
    assert walked["dialect"] == {"java": 22}
    assert walked["regex_sites"] == 22
