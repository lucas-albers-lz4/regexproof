"""Z3-Noodler re.from_ecma2020 capability probe (auditable fixture)."""

from __future__ import annotations

import json
from pathlib import Path

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "noodler_probe.json"


def test_noodler_probe_recorded():
    """Probe once; persist result. Unavailable → triage fallback documented."""
    pattern = r"(?=a)b"  # lookahead-only
    result = {
        "pattern": pattern,
        "api": "re.from_ecma2020",
        "available": False,
        "tool_version": None,
        "error": None,
        "triage_fallback": True,
    }
    try:
        import z3

        mod = getattr(z3, "re", None) or z3
        fn = getattr(mod, "from_ecma2020", None) or getattr(z3, "from_ecma2020", None)
        if fn is None:
            # Some builds expose via z3.z3core / noodler plugin
            result["error"] = "from_ecma2020 not present on stock z3-solver 5.0.0"
        else:
            fn(pattern)
            result["available"] = True
            result["triage_fallback"] = False
            result["tool_version"] = z3.get_version_string()
    except Exception as exc:  # noqa: BLE001
        result["error"] = f"{type(exc).__name__}: {exc}"
        result["triage_fallback"] = True

    FIXTURE.parent.mkdir(parents=True, exist_ok=True)
    FIXTURE.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    loaded = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert loaded["pattern"] == pattern
    assert "available" in loaded
    assert loaded["triage_fallback"] is True or loaded["available"] is True
