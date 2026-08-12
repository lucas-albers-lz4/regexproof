"""Wave-3 Phase 6 (#117): TRAPS §34–§38 + fraction grep-clean vs sweep docs."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "properties" / "generated"
SWEEP3 = ROOT / "sweep" / "corpus-wave3"
TRAPS = ROOT / "docs" / "TRAPS.md"

# Live fraction citations that must match *_encodable_fraction.json.
WAVE3_FRACTIONS = {
    "spamassassin": 0.7479,
    "noseyparker": 0.7354,
    "shhgit": 0.9263,
    "dompurify": 0.5625,
    "isemail": 0.8000,
    "email_addresses": 0.5000,
    "perl_tre": 0.3541,
    "go_regexp_tests": 0.7524,
    "v8_mjsunit": 0.5346,
}


def test_traps_wave3_sections_present():
    text = TRAPS.read_text(encoding="utf-8")
    for n, needle in [
        (34, "Perl dialect frontier"),
        (35, "whitespace/comment strip"),
        (36, "Secret-detector pack"),
        (37, "ECMA sanitizer"),
        (38, "Testdata full-suite"),
    ]:
        assert f"## {n}." in text, f"missing TRAPS §{n}"
        assert needle in text
        assert "Minimal repro" in text.split(f"## {n}.", 1)[1].split("## ", 1)[0]


def test_matrix_includes_wave3_corpora():
    matrix = json.loads((GENERATED / "cross_corpus_matrix.json").read_text(encoding="utf-8"))
    assert matrix.get("wave") == "corpus-wave3"
    by_name = {r["corpus"]: r for r in matrix["corpora"]}
    for name, frac in WAVE3_FRACTIONS.items():
        assert name in by_name, name
        assert by_name[name]["fraction"] == frac
        assert by_name[name]["decision"] == "go"


def test_sweep_docs_match_fraction_artifacts():
    """Grep-clean: sweep decision docs must cite live fraction values."""
    docs = list(SWEEP3.glob("*.md"))
    assert docs
    blob = "\n".join(p.read_text(encoding="utf-8") for p in docs)
    for name, frac in WAVE3_FRACTIONS.items():
        art = json.loads(
            (GENERATED / f"{name}_encodable_fraction.json").read_text(encoding="utf-8")
        )
        assert art["fraction"] == frac, name
        token = f"{frac:.4f}"
        assert token in blob, (
            f"{name}: fraction {token} not cited in sweep/corpus-wave3/*.md"
        )


def test_no_live_semgrep_02741_in_wave3_sweep():
    """Stale semgrep no-go must not appear as an unsuperseded live claim."""
    for path in SWEEP3.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "0.2741" not in text and "0.2842" not in text:
            continue
        # Allowed only when explicitly marked historical / superseded.
        assert re.search(r"supersed|historical|was |pre-P3|Wave-2", text, re.I), path.name


def test_supersession_map_exists():
    text = (SWEEP3 / "supersession.md").read_text(encoding="utf-8")
    for name in WAVE3_FRACTIONS:
        assert name in text or name.replace("_", " ") in text


def test_wave3_artifact_repro_covers_fractions():
    repro = (GENERATED / "wave3_artifact_repro.sha256").read_text(encoding="utf-8")
    for name in WAVE3_FRACTIONS:
        assert f"{name}_encodable_fraction.json" in repro
        assert f"{name}-inventory.ndjson" in repro
