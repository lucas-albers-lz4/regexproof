#!/usr/bin/env python3
"""Clone a gated corpus to a unique /tmp path and symlink batch/corpora/<slug>/rules.

Usage:
  python scripts/materialize-corpus.py --gate properties/generated/openmed_gate_decision.json
  python scripts/materialize-corpus.py --corpus openmed
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
    safe_corpus_slug,
)

CORPORA_ROOT = (ROOT / "batch" / "corpora").resolve()


def _from_gate(path: Path) -> tuple[str, str, str, dict]:
    gate = load_json(path)
    corpus = str(gate.get("corpus") or "")
    url = str(gate.get("candidate_url") or "")
    pin = str(gate.get("corpus_pin") or "")
    if not corpus or not url:
        raise SystemExit(f"error: {path} missing corpus or candidate_url")
    return safe_corpus_slug(corpus), url, pin, gate


def _from_manifest(name: str) -> tuple[str, str, str, dict]:
    slug = safe_corpus_slug(name)
    meta = CORPUS_MANIFESTS.get(slug)
    if meta is None:
        raise SystemExit(f"error: corpus {slug!r} not in CORPUS_MANIFESTS")
    repo = str(meta.get("repo") or "")
    pin = str(meta.get("corpus_pin") or meta.get("commit") or "")
    if not repo:
        raise SystemExit(f"error: manifest {slug!r} has no repo")
    url = repo if repo.startswith("https://") else f"https://github.com/{repo}"
    return slug, url, pin, {}


def _require_allowlist_if_inflated(gate: dict, allowlist_file: Path | None) -> int:
    probe = gate.get("probe") if isinstance(gate.get("probe"), dict) else {}
    per_file = probe.get("regex_sites_per_file") if isinstance(probe, dict) else None
    if not isinstance(per_file, dict):
        return 0
    hits = inflation_hits(per_file)
    if not hits:
        return 0
    if allowlist_file is None or not allowlist_file.is_file():
        print(
            "error: probe paths look like locale/vendor/testdata inflation "
            f"({hits[0]}). Pass --allowlist-file with a non-empty files list "
            "(tarcoin lesson).",
            file=sys.stderr,
        )
        return 2
    lines = [
        ln.strip()
        for ln in allowlist_file.read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    if not lines:
        print("error: --allowlist-file is empty", file=sys.stderr)
        return 2
    for line in lines:
        norm = line.replace("\\", "/")
        if norm.startswith("/") or ".." in Path(norm).parts:
            print(f"error: allowlist path not a relative file: {line!r}", file=sys.stderr)
            return 2
    print(
        "allowlist accepted for clone; paste these paths into CORPUS_MANIFESTS "
        f"files= for {gate.get('corpus')} (not auto-applied).",
        file=sys.stderr,
    )
    return 0


def _corpus_link_dir(corpus: str) -> Path:
    link_dir = (CORPORA_ROOT / corpus).resolve()
    if link_dir != CORPORA_ROOT and CORPORA_ROOT not in link_dir.parents:
        raise SystemExit(f"error: link dir escapes batch/corpora: {link_dir}")
    return link_dir


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gate", type=Path, help="admission gate JSON")
    ap.add_argument("--corpus", help="CORPUS_MANIFESTS key")
    ap.add_argument(
        "--allowlist-file",
        type=Path,
        help="non-empty files allowlist required when probe looks inflated",
    )
    ap.add_argument("--link-name", default="rules", help="symlink name under batch/corpora/<slug>/")
    args = ap.parse_args(argv)
    if bool(args.gate) == bool(args.corpus):
        print("error: provide exactly one of --gate or --corpus", file=sys.stderr)
        return 2
    if args.gate:
        corpus, url, pin, gate = _from_gate(args.gate)
        inflated = _require_allowlist_if_inflated(gate, args.allowlist_file)
        if inflated:
            return inflated
    else:
        corpus, url, pin, _gate = _from_manifest(args.corpus)
        gate_path = ROOT / "properties" / "generated" / f"{corpus}_gate_decision.json"
        if gate_path.is_file():
            inflated = _require_allowlist_if_inflated(load_json(gate_path), args.allowlist_file)
            if inflated:
                return inflated

    dest = clone_dest(url, corpus)
    try:
        result = partial_clone(url, dest=dest, pin=pin or None)
    except CloneError as exc:
        print(f"error: clone failed: {exc}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if "/" in args.link_name or "\\" in args.link_name or args.link_name in {".", ".."}:
        print("error: --link-name must be a single path segment", file=sys.stderr)
        return 2
    link_dir = _corpus_link_dir(corpus)
    link_dir.mkdir(parents=True, exist_ok=True)
    link = link_dir / args.link_name
    if link.is_symlink():
        link.unlink()
    elif link.is_dir():
        print(
            f"error: {link} is a directory, not a symlink; refuse to rmtree",
            file=sys.stderr,
        )
        return 2
    elif link.exists():
        link.unlink()
    link.symlink_to(dest)
    print(f"materialized {corpus} pin={result.pin} dest={dest} link={link}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
