#!/usr/bin/env python3
"""Run the checked-in Phase 6 property subset (z3-verify + one rule_diff family)."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_toml(path: Path) -> dict:
    import tomllib

    return tomllib.loads(path.read_text(encoding="utf-8"))


def _subset_property_names(families: list[str]) -> list[str]:
    from regexproof.harness import REGISTRY

    names = []
    for name in sorted(REGISTRY):
        fam = REGISTRY[name]["family"]
        if fam in families:
            names.append(name)
    return names


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--config",
        type=Path,
        default=ROOT / "ci" / "property-subset.toml",
    )
    args = ap.parse_args(argv)
    cfg = _load_toml(args.config)
    families = list(cfg["families"])
    names = _subset_property_names(families)
    if not names:
        print("FAIL: property subset resolved to empty name list", file=sys.stderr)
        return 1
    print(f"subset families={families} properties={len(names)}")
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "z3-verify.py"),
        "--require-ground-truth",
        *names,
    ]
    r1 = subprocess.run(cmd, cwd=ROOT, shell=False, check=False)
    if r1.returncode != 0:
        return r1.returncode

    family = cfg["rule_diff_family"]
    r2 = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "rule-diff-pilot.py"),
            "--require-ground-truth",
            "--family",
            family,
        ],
        cwd=ROOT,
        shell=False,
        check=False,
    )
    return r2.returncode


if __name__ == "__main__":
    raise SystemExit(main())
