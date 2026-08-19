#!/usr/bin/env python3
"""Argv-only Python ReDoS detector CLI (regexploit).

#20 designates vuln-regex-detector, which is not pip-installable (multi-runtime
service). Phase 4 pins regexploit==1.0.0 as the isolated Python detector and
records tool=regexploit in findings. Optional REGEXPROOF_VRD_HOME may point at
a local vuln-regex-detector checkout for future wiring.

Usage:
  python vuln_regex_detector_cli.py <pattern> [flags]
Prints one JSON object on stdout.
"""

from __future__ import annotations

import json
import sys


def emit(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj) + "\n")


def main() -> int:
    if len(sys.argv) < 2:
        emit(
            {
                "tool": "regexploit",
                "tool_version": _version(),
                "result": "error",
                "error_message": "usage: vuln_regex_detector_cli.py <pattern> [flags]",
            }
        )
        return 0
    pattern = sys.argv[1]
    # flags reserved for future VRD; regexploit uses flavour=python
    try:
        from regexploit.ast.sre import SreOpParser
        from regexploit.redos import find

        parsed = SreOpParser().parse_sre(pattern)
        redos = list(find(parsed))
        if redos:
            worst = max(redos, key=lambda r: r.starriness)
            emit(
                {
                    "tool": "regexploit",
                    "tool_version": _version(),
                    "result": "vulnerable",
                    "severity": f"starriness={worst.starriness}",
                    "confidence": "medium",
                    "detail": {
                        "starriness": worst.starriness,
                    },
                    "error_message": None,
                }
            )
        else:
            emit(
                {
                    "tool": "regexploit",
                    "tool_version": _version(),
                    "result": "safe",
                    "severity": None,
                    "confidence": "medium",
                    "error_message": None,
                }
            )
    except Exception as exc:
        emit(
            {
                "tool": "regexploit",
                "tool_version": _version(),
                "result": "error",
                "severity": None,
                "confidence": None,
                "error_message": f"{type(exc).__name__}: {exc}",
            }
        )
    return 0


def _version() -> str:
    try:
        from importlib.metadata import version

        return version("regexploit")
    except Exception:
        return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
