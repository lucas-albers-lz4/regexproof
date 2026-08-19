"""Per-pattern differential-fuzz job schema (Phase 1 integration contract)."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class FuzzJob:
    """One fuzz job: mirror expression vs argv engine adapter."""

    pattern: str
    flags: str
    dialect: str
    call_kind: str
    declared_domain: str
    mirror_expr: str
    engine_argv: tuple[str, ...]
    alphabet: str
    schema_version: str = "1"
    mutations: str = ""
    exhaust_max_len: int = 3
    runs: int = 100
    seed: int = 42

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["engine_argv"] = list(self.engine_argv)
        return d


# Trap-seeded alphabets per dialect (TRAPS + distinguishing cases).
# Exhaustive over a full Unicode alphabet is infeasible; these pins make
# the net real for known divergence classes.
PINNED_ALPHABETS: dict[str, str] = {
    "py_re": "ab01._-\r\n" + "\u0660\u00a0\u0130\u0131",
    "ecma": "ab01._-\r\n" + "\u00a0\u2028\u2029\u00df",
    "re2": "ab01._-\r\n" + "\u0130\u0131",
    "pcre": "ab01._-\r\n" + "\u0660\u00a0",
}


def pinned_alphabet(dialect: str) -> str:
    try:
        return PINNED_ALPHABETS[dialect]
    except KeyError as exc:
        raise ValueError(f"no pinned alphabet for dialect {dialect!r}") from exc
