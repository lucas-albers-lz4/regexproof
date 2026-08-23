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

# A broad walk matches properties/ not anchored to generated/. Includes
# VARIABLE-path rglob/glob — a parameter- or CLI-driven walk root can be
# pointed at properties (Luna r3 #1: dogfood-singleton-analysis walked
# staged_probes). Hardcoded ROOT-based receivers (ROOT / "regexproof" /
# "compiler", corpus dirs, etc.) can never reach properties/ and are not
# flagged.
_BROAD = re.compile(
    r"properties\s*[\)\]]?\s*(?:/\s*\*\*|/\s*\*|\.rglob|\.glob)|"
    r"[A-Za-z_][A-Za-z0-9_]*\s*\.rglob\(|"
    r"[A-Za-z_][A-Za-z0-9_]*\s*\.glob\([^)]*properties|"
    r"glob\([^)]*properties"
)


def _is_broad_walker(script: pathlib.Path) -> bool:
    try:
        text = script.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    # Any variable assigned from ROOT (e.g. src = ROOT / manifest[...]) is
    # ROOT-anchored and can never reach properties/.
    root_assigned = set(re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s*=\s*ROOT\b", text))
    for line in text.splitlines():
        if not _BROAD.search(line):
            continue
        # Receiver is ROOT or a variable assigned from ROOT → safe.
        m = re.search(r"([A-Za-z_][A-Za-z0-9_]*)\s*\.(?:rglob|glob)\(", line)
        if m and (m.group(1) == "ROOT" or m.group(1) in root_assigned):
            continue
        return True
    return False


def main() -> int:
    problems = []
    # Walker-exclusion scan.
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
    # batch/state.json integrity (the docstring promises this check): parse
    # + verify the checksum; corrupt state is a hard failure.
    state = ROOT / "batch" / "state.json"
    if state.is_file():
        try:
            sys.path.insert(0, str(ROOT))
            from regexproof.mine.batch_state import load_state

            load_state(path=state)
        except SystemExit as exc:
            problems.append(f"batch/state.json: {exc}")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
