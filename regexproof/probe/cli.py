"""Wave 11 (#580): one entry for the two probe CLIs.

``python -m regexproof.probe --single …`` wraps
``scripts/probe-corpus-admission.py``.
``python -m regexproof.probe --batch …`` wraps ``scripts/batch-probe.py``.
The legacy scripts still work; they print a pointer when stderr is a TTY.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[2]


def _load_script(filename: str) -> ModuleType:
    path = ROOT / "scripts" / filename
    spec = importlib.util.spec_from_file_location(f"_rp_probe_{filename}", path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"probe: cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    ap = argparse.ArgumentParser(
        prog="python -m regexproof.probe",
        description=__doc__,
    )
    ap.add_argument(
        "--single",
        action="store_true",
        help="Pre-wave single-repo probe (probe-corpus-admission.py)",
    )
    ap.add_argument(
        "--batch",
        action="store_true",
        help="Wave-2/5 leased batch probe (batch-probe.py)",
    )
    if not argv or argv[0] in {"-h", "--help"}:
        ap.print_help()
        return 0
    mode = None
    rest: list[str] = []
    for i, tok in enumerate(argv):
        if tok == "--single" and mode is None:
            mode = "single"
            rest = argv[i + 1 :]
            break
        if tok == "--batch" and mode is None:
            mode = "batch"
            rest = argv[i + 1 :]
            break
    if mode is None:
        ap.error("one of --single / --batch is required")
    script = (
        "probe-corpus-admission.py" if mode == "single" else "batch-probe.py"
    )
    try:
        rc = _load_script(script).main(rest)
    except SystemExit as exc:
        code = exc.code
        if code is None:
            return 0
        return int(code) if isinstance(code, int) else 1
    return int(rc)
