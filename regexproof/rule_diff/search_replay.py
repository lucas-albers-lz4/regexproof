"""Search/pad matrix for shape-5 SAT witnesses (VF-007).

The solver stays fullmatch. A SAT witness is a reportable search gap only
when some prefix/suffix pad still matches R2 and misses R1 in the real
engine.
"""

from __future__ import annotations

import re
from typing import Any

PADS = ("", "a", " ", "\n", "0", "x")

_FLAG_MAP = {
    "i": re.IGNORECASE,
    "m": re.MULTILINE,
    "s": re.DOTALL,
    "x": re.VERBOSE,
}


def _flags_int(flags: str) -> int:
    out = 0
    for ch in flags or "":
        bit = _FLAG_MAP.get(ch)
        if bit:
            out |= bit
    return out


def real_search(pattern: str, flags: str, text: str) -> bool:
    """Python ``re.search`` pad filter (VF-007).

    This is a necessary SAT filter on the regular fragment, not
    dialect-faithful PCRE2/RE2 replay. Filing still needs the real engines.
    """
    try:
        return re.search(pattern, text, _flags_int(flags)) is not None
    except re.error:
        return False


def search_pad_confirms_gap(
    r1_pattern: str,
    r2_pattern: str,
    witness: str,
    *,
    r1_flags: str = "",
    r2_flags: str = "",
) -> bool:
    """True if some pad makes R2 match and R1 miss under search semantics."""
    if not isinstance(witness, str):
        return False
    for pre in PADS:
        for suf in PADS:
            s = pre + witness + suf
            if real_search(r2_pattern, r2_flags, s) and not real_search(
                r1_pattern, r1_flags, s
            ):
                return True
    return False


def gate_sat_witness(pair: dict[str, Any], witness: str) -> bool:
    """SAT gate used by batch shape-5: search/pad must confirm the gap."""
    r1 = pair.get("r1") or {}
    r2 = pair.get("r2") or {}
    return search_pad_confirms_gap(
        str(r1.get("pattern") or ""),
        str(r2.get("pattern") or ""),
        witness,
        r1_flags=str(r1.get("flags") or ""),
        r2_flags=str(r2.get("flags") or ""),
    )
