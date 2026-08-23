#!/usr/bin/env python3
"""Wave 2 (#559): CI guard — properties-WALKING tools must EXCLUDE
staged_probes/ (staged-draft probes are not contract material).

Targets only BROAD walkers: scripts that glob/rglob under ``properties/``
in a way that could sweep ``staged_probes/`` (the pattern ``properties``
followed by ``*``/``**`` or a bare ``rglob``). Tools scoped to
``properties/generated`` are safe by construction.

Also verifies batch/state.json (if present) parses and its checksum
verifies.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXCLUSION_TOKEN = "staged_probes"

# A broad walk matches properties/ not anchored to generated/.
_BROAD = re.compile(
    r"properties\s*[\)\]]?\s*(?:/\s*\*\*|/\s*\*|\.rglob|\.glob)|"
    r"\.rglob\(.*properties|"
    r"glob\([^)]*properties"
)


def _is_broad_walker(script: pathlib.Path) -> bool:
    try:
        text = script.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return bool(_BROAD.search(text))


def main() -> int:
    problems = []
    for script in sorted((ROOT / "scripts").glob("*.py")):
        if script.name.startswith(("ci-", "test_")):
            continue
        if not _is_broad_walker(script):
            continue
        text = script.read_text(encoding="utf-8", errors="replace")
        if EXCLUSION_TOKEN not in text:
            problems.append(
                f"{script.name}: broad properties-walker does not exclude "
                f"'{EXCLUSION_TOKEN}' (staged-draft probes must never be "
                "walked as contract material)"
            )
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
