#!/usr/bin/env python3
"""Extract java Pattern.compile → pcre approx, classify, fuzz, report.

Usage:
  python scripts/java-html-sanitizer-triage.py --root PATH [-o properties/generated]
  python scripts/java-html-sanitizer-triage.py --fixture
  python scripts/java-html-sanitizer-triage.py --root PATH --corpus hippo \\
      --artifact-stem hippo_java --pin SHA --url URL --files a.java --files b.java
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.admission.java_pin import (
    JAVA_HTML_SANITIZER_PIN,
    JAVA_HTML_SANITIZER_URL,
)
from regexproof.admission.serialize import dumps_pinned
from regexproof.compiler.pcre import compile_pcre
from regexproof.extractors.java_pattern import extract_java_pattern

HELPER = ROOT / "helpers" / "pcre2" / "match.py"
DEFAULT_CORPUS = "java-html-sanitizer"

# Align with admission.walk skips so a full-clone --root does not pull test trees.
_SKIP_DIR_NAMES = frozenset(
    {
        ".git",
        ".hg",
        ".svn",
        "node_modules",
        "vendor",
        "third_party",
        "third-party",
        "__pycache__",
        ".venv",
        "venv",
        "target",
        "build",
        "dist",
        "out",
        "testdata",
        "test-data",
        "fixtures",
    }
)
def _iter_java(root: Path) -> list[Path]:
    out: list[Path] = []
    root = root.resolve()
    for p in sorted(root.rglob("*.java")):
        if not p.is_file():
            continue
        rel_path = p.relative_to(root)
        # Only skip dirs *under* root (ancestors like …/tests/fixtures must not apply).
        if any(part in _SKIP_DIR_NAMES for part in rel_path.parts):
            continue
        # Segment-aware Maven/layout skips (avoid substring false positives like
        # ``src/testing`` matching ``src/test`` or ``src/items`` matching ``src/it``).
        parts = rel_path.parts
        if (
            len(parts) >= 2
            and parts[0] == "src"
            and parts[1] in {"test", "tests", "it", "integration-test"}
        ):
            continue
        # Top-level test/ trees (non-Maven layouts).
        if parts and parts[0] in {"test", "tests"}:
            continue
        out.append(p)
    return out


def extract_tree(
    root: Path,
    *,
    repo: str = DEFAULT_CORPUS,
    files: list[str] | None = None,
) -> list[dict]:
    recs: list[dict] = []
    if files:
        paths = []
        for rel in files:
            fp = (root / rel).resolve()
            if not fp.is_file():
                raise SystemExit(f"HARD ERROR: missing --files entry: {rel}")
            paths.append((fp, rel))
    else:
        paths = [(fp, str(fp.relative_to(root))) for fp in _iter_java(root)]
    for fp, rel in paths:
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        recs.extend(extract_java_pattern(text, repo=repo, file=rel))
    return recs


def classify_encodable(rec: dict) -> dict:
    """Mark unencodable when reject markers fire *or* compile_pcre fails."""
    if rec.get("unencodable_reason"):
        return rec
    result = compile_pcre(
        rec["pattern"],
        rec.get("flags") or "",
        call_kind=rec.get("call_kind") or "search",
    )
    if not result.encodable:
        rec = dict(rec)
        rec["unencodable_reason"] = result.unencodable_reason or "compile-failed"
    return rec


def _pcre2_match(
    pattern: str, flags: str, data: str, *, call_kind: str = "fullmatch"
) -> bool | None:
    """Replay via helpers/pcre2. ``fullmatch`` anchors like Java Matcher.matches()."""
    replay = pattern
    if call_kind in {"fullmatch", "match"}:
        # Helper uses search/pcre2grep; wrap to whole-string membership.
        replay = f"^(?:{pattern})$"
    proc = subprocess.run(
        [sys.executable, str(HELPER), "match", replay, flags],
        input=data,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode == 0:
        return True
    if proc.returncode == 1:
        return False
    return None


def differential_check(rec: dict, *, samples: list[str] | None = None) -> dict:
    """Compare compile_pcre mirror vs helpers/pcre2 on short samples."""
    import z3

    pattern = rec["pattern"]
    flags = rec.get("flags") or ""
    call_kind = rec.get("call_kind") or "fullmatch"
    # Avoid empty-string samples: pcre2 helper line/match semantics disagree with
    # Z3 on optional patterns (e.g. `.?`) for the empty input.
    samples = samples or ["a", "A", "0", " ", "center", "LEFT", "#fff", "noresize", "xy"]
    result = compile_pcre(pattern, flags, call_kind=call_kind)
    if not result.encodable or result.mirror is None:
        return {
            "regex_id": rec["regex_id"],
            "ok": False,
            "reason": result.unencodable_reason or "compile-failed",
            "disagreements": 0,
        }
    disagree = 0
    checked = 0
    for s in samples:
        real = _pcre2_match(pattern, flags, s, call_kind=call_kind)
        if real is None:
            continue
        solver = z3.Solver()
        solver.add(z3.InRe(z3.StringVal(s), result.mirror))
        mirror_hit = solver.check() == z3.sat
        checked += 1
        if mirror_hit != real:
            disagree += 1
    return {
        "regex_id": rec["regex_id"],
        "ok": disagree == 0 and checked > 0,
        "checked": checked,
        "disagreements": disagree,
        "reason": None if disagree == 0 else "mirror-real-disagreement",
    }


def run_triage(
    root: Path,
    out_dir: Path,
    *,
    corpus: str = DEFAULT_CORPUS,
    candidate_url: str = JAVA_HTML_SANITIZER_URL,
    corpus_pin: str = JAVA_HTML_SANITIZER_PIN,
    artifact_stem: str | None = None,
    files: list[str] | None = None,
) -> dict:
    out_dir = out_dir.expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = artifact_stem or corpus
    recs = [
        classify_encodable(r)
        for r in extract_tree(root, repo=corpus, files=files)
    ]
    encodable = [r for r in recs if not r.get("unencodable_reason")]
    rejected = [r for r in recs if r.get("unencodable_reason")]

    fuzz_rows = []
    for rec in encodable:
        try:
            fuzz_rows.append(differential_check(rec))
        except Exception as e:  # pragma: no cover
            fuzz_rows.append(
                {
                    "regex_id": rec["regex_id"],
                    "ok": False,
                    "reason": f"fuzz-error:{type(e).__name__}",
                    "disagreements": 0,
                }
            )

    fuzz_ok = sum(1 for r in fuzz_rows if r.get("ok"))
    fuzz_fail = [r for r in fuzz_rows if not r.get("ok")]
    reasons = Counter(r.get("unencodable_reason") or "ok" for r in recs)

    summary = {
        "schema_version": "1",
        "corpus": corpus,
        "candidate_url": candidate_url,
        "corpus_pin": corpus_pin,
        "approximation": "java→pcre",
        "total_sites": len(recs),
        "encodable": len(encodable),
        "rejected": len(rejected),
        "encodable_fraction": (len(encodable) / len(recs)) if recs else 0.0,
        "reject_reasons": dict(reasons),
        "differential_ok": fuzz_ok,
        "differential_fail": len(fuzz_fail),
        "differential_zero_disagreement_pass": len(fuzz_fail) == 0 and fuzz_ok > 0,
        "pass_criteria": {
            "zero_disagreements_on_encodable_subset": True,
            "bounded_samples": True,
        },
    }
    if files:
        summary["files"] = list(files)

    # Extractor JSONL
    ext_path = out_dir / f"{stem}_extractor.jsonl"
    with ext_path.open("w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n")

    # Triage NDJSON (finding-shaped summary rows)
    ndjson_path = out_dir / f"{stem}_triage.ndjson"
    with ndjson_path.open("w", encoding="utf-8") as f:
        for row in fuzz_rows:
            rec = {
                "schema_version": "1",
                "kind": "triage",
                "corpus": corpus,
                "approximation": "java→pcre",
                **row,
            }
            f.write(json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n")

    frac_path = out_dir / f"{stem}_encodable_fraction.json"
    frac_path.write_text(dumps_pinned(summary), encoding="utf-8")

    md_path = out_dir / f"{stem}_batch.md"
    md = [
        f"# {stem} triage (java→pcre approximation)",
        "",
        f"- corpus: `{corpus}`",
        f"- pin: `{corpus_pin}`",
        f"- url: {candidate_url}",
        f"- sites: {summary['total_sites']} (encodable {summary['encodable']}, "
        f"rejected {summary['rejected']}, fraction {summary['encodable_fraction']:.4f})",
        f"- differential: ok={fuzz_ok} fail={len(fuzz_fail)} "
        f"zero_disagreement_pass={summary['differential_zero_disagreement_pass']}",
        f"- reject_reasons: `{json.dumps(summary['reject_reasons'], sort_keys=True)}`",
        "",
        "See `sweep/corpus-wave4/java-features.md`.",
        "",
    ]
    md_path.write_text("\n".join(md), encoding="utf-8")

    summary["artifacts"] = {
        "extractor": str(ext_path.resolve()),
        "triage_ndjson": str(ndjson_path.resolve()),
        "fraction": str(frac_path.resolve()),
        "batch_md": str(md_path.resolve()),
    }
    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, help="Repo root to walk for .java files")
    ap.add_argument(
        "--fixture",
        action="store_true",
        help="Use tests/fixtures/admission/java_sites",
    )
    ap.add_argument(
        "--corpus",
        default=DEFAULT_CORPUS,
        help=f"Corpus name in artifacts (default {DEFAULT_CORPUS})",
    )
    ap.add_argument(
        "--artifact-stem",
        default=None,
        help="Filename stem for outputs (default: --corpus; use hippo_java for hippo)",
    )
    ap.add_argument("--pin", default=None, help="corpus_pin recorded in summary")
    ap.add_argument("--url", default=None, help="candidate_url recorded in summary")
    ap.add_argument(
        "--files",
        action="append",
        default=None,
        help="Relative .java path under --root (repeatable; skips full walk)",
    )
    ap.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=ROOT / "properties" / "generated",
    )
    args = ap.parse_args(argv)
    if args.fixture:
        root = (ROOT / "tests" / "fixtures" / "admission" / "java_sites").resolve()
        corpus = DEFAULT_CORPUS
        pin = JAVA_HTML_SANITIZER_PIN
        url = JAVA_HTML_SANITIZER_URL
        files = None
        stem = None
    elif args.root:
        root = args.root.expanduser().resolve()
        corpus = args.corpus
        pin = args.pin or (
            JAVA_HTML_SANITIZER_PIN if corpus == DEFAULT_CORPUS else "unknown"
        )
        url = args.url or (
            JAVA_HTML_SANITIZER_URL if corpus == DEFAULT_CORPUS else "unknown"
        )
        files = args.files
        stem = args.artifact_stem
    else:
        ap.error("provide --root or --fixture")
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2
    summary = run_triage(
        root,
        args.output_dir.expanduser().resolve(),
        corpus=corpus,
        candidate_url=url,
        corpus_pin=pin,
        artifact_stem=stem,
        files=files,
    )
    print(dumps_pinned(summary))
    return 0 if summary.get("differential_zero_disagreement_pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
