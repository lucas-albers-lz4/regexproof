#!/usr/bin/env python3
"""Write a README stub and print a CORPUS_MANIFESTS fragment. Does not edit WAVE.

Usage:
  python scripts/scaffold-smith-corpus.py --gate properties/generated/openmed_gate_decision.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.batch.smith_support import (  # noqa: E402
    guess_extractor,
    load_json,
    owner_slug_from_url,
    safe_corpus_slug,
    wave_checklist,
)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gate", type=Path, required=True)
    ap.add_argument("--force", action="store_true", help="overwrite existing README")
    args = ap.parse_args(argv)
    gate = load_json(args.gate)
    raw_corpus = str(gate.get("corpus") or "")
    url = str(gate.get("candidate_url") or "")
    pin = str(gate.get("corpus_pin") or "")
    if not raw_corpus or not url:
        print("error: gate missing corpus or candidate_url", file=sys.stderr)
        return 2
    try:
        corpus = safe_corpus_slug(raw_corpus)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    owner, repo = owner_slug_from_url(url)
    probe = gate.get("probe") if isinstance(gate.get("probe"), dict) else {}
    dialect = probe.get("dialect") if isinstance(probe.get("dialect"), dict) else {}
    extractor, glob, dialect = guess_extractor(dialect if isinstance(dialect, dict) else {})
    dest_dir = ROOT / "batch" / "corpora" / corpus
    dest_dir = dest_dir.resolve()
    corpora_root = (ROOT / "batch" / "corpora").resolve()
    if corpora_root not in dest_dir.parents:
        print("error: corpus dir escapes batch/corpora", file=sys.stderr)
        return 2
    dest_dir.mkdir(parents=True, exist_ok=True)
    readme = dest_dir / "README.md"
    body = (
        f"# {corpus} corpus\n\n"
        f"Pinned `{owner}/{repo}` at `{pin}` for Smith after admission "
        f"`{corpus}_gate_decision.json`.\n\n"
        "## Materialize\n\n"
        "```bash\n"
        f"python scripts/materialize-corpus.py --gate "
        f"properties/generated/{corpus}_gate_decision.json\n"
        "```\n\n"
        f"Gate: `properties/generated/{corpus}_gate_decision.json`.\n\n"
        "## Measure / batch\n\n"
        "```bash\n"
        f"python scripts/measure-corpus-fraction.py --corpus {corpus} "
        "--assert-determinism\n"
        f"python -m regexproof.batch --corpus {corpus}\n"
        f"python scripts/author-smith-decision.py --gate "
        f"properties/generated/{corpus}_gate_decision.json "
        f"--fraction properties/generated/{corpus}_encodable_fraction.json "
        "--decision go|no-go|triage-continues --reason '...'\n"
        "```\n\n"
        "Leave `files` empty in the manifest until a human pastes an allowlist. "
        "Do not add WAVE_CORPORA until a local complete_run.\n"
    )
    if readme.exists() and not args.force:
        print(f"keep existing {readme}", file=sys.stderr)
    else:
        readme.write_text(body, encoding="utf-8")
        print(f"wrote {readme}", file=sys.stderr)
    stub = {
        corpus: {
            "corpus_type": "rule_corpus",
            "path": f"batch/corpora/{corpus}/rules",
            "files": [],
            "glob": glob,
            "dialect": dialect,
            "extractor": extractor,
            "repo": f"{owner}/{repo}",
            "security_tool": False,
            "lift_inline": False,
            "corpus_pin": pin,
            "commit": pin,
        }
    }
    print(json.dumps(stub, indent=2, sort_keys=True))
    print(wave_checklist(corpus), file=sys.stderr)
    print(
        "files allowlist is empty until a human pastes it; fail closed on inflation dirs.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
