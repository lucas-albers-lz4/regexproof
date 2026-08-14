#!/usr/bin/env python3
"""Clone a gated corpus to a unique /tmp path and symlink batch/corpora/<slug>/rules.

Usage:
  python scripts/materialize-corpus.py --gate properties/generated/openmed_gate_decision.json
  python scripts/materialize-corpus.py --corpus openmed --allow-inflation
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.admission.clone import CloneError, partial_clone  # noqa: E402
from regexproof.batch.manifests import CORPUS_MANIFESTS  # noqa: E402
from regexproof.batch.smith_support import (  # noqa: E402
    clone_dest,
    inflation_hits,
    load_json,
)


def _from_gate(path: Path) -> tuple[str, str, str, dict]:
    gate = load_json(path)
    corpus = str(gate.get("corpus") or "")
    url = str(gate.get("candidate_url") or "")
    pin = str(gate.get("corpus_pin") or "")
    if not corpus or not url:
        raise SystemExit(f"error: {path} missing corpus or candidate_url")
    return corpus, url, pin, gate


def _from_manifest(name: str) -> tuple[str, str, str, dict]:
    meta = CORPUS_MANIFESTS.get(name)
    if meta is None:
        raise SystemExit(f"error: corpus {name!r} not in CORPUS_MANIFESTS")
    repo = str(meta.get("repo") or "")
    pin = str(meta.get("corpus_pin") or meta.get("commit") or "")
    if not repo:
        raise SystemExit(f"error: manifest {name!r} has no repo")
    url = repo if repo.startswith("https://") else f"https://github.com/{repo}"
    return name, url, pin, {}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gate", type=Path, help="admission gate JSON")
    ap.add_argument("--corpus", help="CORPUS_MANIFESTS key")
    ap.add_argument(
        "--allow-inflation",
        action="store_true",
        help="clone even if probe files look like locale/vendor/testdata",
    )
    ap.add_argument("--link-name", default="rules", help="symlink name under batch/corpora/<slug>/")
    args = ap.parse_args(argv)
    if bool(args.gate) == bool(args.corpus):
        print("error: provide exactly one of --gate or --corpus", file=sys.stderr)
        return 2
    if args.gate:
        corpus, url, pin, gate = _from_gate(args.gate)
        probe = gate.get("probe") if isinstance(gate.get("probe"), dict) else {}
        per_file = probe.get("regex_sites_per_file") if isinstance(probe, dict) else None
        if isinstance(per_file, dict) and not args.allow_inflation:
            hits = inflation_hits(per_file)
            if hits:
                print(
                    "error: probe paths look like locale/vendor/testdata inflation "
                    f"({hits[0]}). Paste a files allowlist; rerun with "
                    "--allow-inflation only after that (tarcoin lesson).",
                    file=sys.stderr,
                )
                return 2
    else:
        corpus, url, pin, _gate = _from_manifest(args.corpus)

    dest = clone_dest(url, corpus)
    try:
        result = partial_clone(url, dest=dest, pin=pin or None)
    except CloneError as exc:
        print(f"error: clone failed: {exc}", file=sys.stderr)
        return 1
    link_dir = ROOT / "batch" / "corpora" / corpus
    link_dir.mkdir(parents=True, exist_ok=True)
    link = link_dir / args.link_name
    if link.is_symlink() or link.exists():
        link.unlink()
    link.symlink_to(dest)
    print(f"materialized {corpus} pin={result.pin} dest={dest} link={link}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
