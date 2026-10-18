#!/usr/bin/env python3
"""Reproduce the bounded-timeout whole-helper slug inclusion attempt."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from z3 import And, Concat, InRe, IndexOf, Length, Not, Plus, Range, Re, Solver, Star, String, StringVal, SubString, Union, unsat, unknown  # noqa: E402

from regexproof.compiler import compile_pattern  # noqa: E402

PIN = "8666b6c6c52472b5535aa295f2df593918152cb1"
REPOSITORY = "marcusquinn/aidevops"
PATTERN = r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$"
OWNER_PATTERN = r"^[A-Za-z0-9][A-Za-z0-9_.-]*$"


def _mirror(pattern: str):
    compiled = compile_pattern(
        pattern,
        dialect="posix-shell",
        call_kind="search",
        max_length=256,
        domain="ascii",
        shell_flags={"syntax": "bash_ksh"},
    )
    if not compiled.encodable:
        raise RuntimeError(f"source Bash pattern is not encodable: {compiled.unencodable_reason}")
    return compiled.mirror


def main() -> int:
    slug = String("slug")
    slash = IndexOf(slug, StringVal("/"), 0)
    owner = SubString(slug, 0, slash)
    name = SubString(slug, slash + 1, Length(slug) - slash - 1)
    allowed = Union(Range("A", "Z"), Range("a", "z"), Range("0", "9"), Re("_"), Re("."), Re("-"))
    safe_owner = Concat(
        Union(Range("A", "Z"), Range("a", "z"), Range("0", "9")),
        Star(allowed),
    )
    safe_slug = Concat(safe_owner, Re("/"), Plus(allowed))
    accepted = And(
        InRe(slug, _mirror(PATTERN)),
        InRe(owner, _mirror(OWNER_PATTERN)),
        name != StringVal("."),
        name != StringVal(".."),
    )

    solver = Solver()
    solver.set(timeout=30000)
    solver.add(accepted, Not(InRe(slug, safe_slug)))
    started = time.perf_counter()
    result = solver.check()
    wall_ms = round((time.perf_counter() - started) * 1000, 1)
    payload = {
        "schema_version": "1",
        "question_id": "AE-aidevops-webhook-repository-action-token",
        "site": f"{REPOSITORY}@{PIN}:.agents/scripts/pulse-merge-webhook-receiver.sh:197:1",
        "source_pattern": PATTERN,
        "declared_contract_file": "contract-repository-slug.json",
        "dialect": "posix-shell",
        "shell_syntax": "bash_ksh",
        "input_domain": "ascii; exact pinned local action token; NUL excluded by the line protocol",
        "result": "timeout" if result == unknown else "unsat" if result == unsat else "sat",
        "not_proven": result == unknown,
        "wall_ms": wall_ms,
        "timeout_ms": 30000,
        "reason_unknown": solver.reason_unknown() if result == unknown else None,
        "claim": "A source-matched Bash slug accepted by the complete helper fits one safe owner/repository token, excluding . and .. repository names.",
        "limitation": "TIMEOUT is not a proof; this attempt is excluded from useful-proof counts.",
    }
    rendered = json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
    Path(__file__).with_name("slug-inclusion-attempt.json").write_text(
        rendered, encoding="utf-8"
    )
    print(rendered, end="")
    return 0 if result == unsat else 1


if __name__ == "__main__":
    raise SystemExit(main())
