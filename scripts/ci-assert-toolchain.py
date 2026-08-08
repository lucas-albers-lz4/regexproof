#!/usr/bin/env python3
"""Assert CI job toolchains match ci/toolchain.toml (fail on drift)."""

from __future__ import annotations

import argparse
import json
import platform
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_toml(path: Path) -> dict:
    import tomllib

    return tomllib.loads(path.read_text(encoding="utf-8"))


def _python_mm() -> str:
    v = sys.version_info
    return f"{v.major}.{v.minor}"


def _node_major() -> int | None:
    try:
        out = subprocess.check_output(["node", "-v"], text=True, shell=False).strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    m = re.match(r"v?(\d+)", out)
    return int(m.group(1)) if m else None


def _go_version() -> str | None:
    try:
        out = subprocess.check_output(["go", "version"], text=True, shell=False).strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    m = re.search(r"go(\d+\.\d+(?:\.\d+)?)", out)
    return m.group(1) if m else None


def _z3_version() -> str:
    import z3

    return z3.get_version_string()


def _npm_dep(pkg: str) -> str | None:
    lock = ROOT / "helpers" / "redos" / "package.json"
    data = json.loads(lock.read_text(encoding="utf-8"))
    return (data.get("dependencies") or {}).get(pkg)


def _pip_pin(name: str) -> str | None:
    text = (ROOT / "requirements-redos.txt").read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith(name.lower() + "=="):
            return line.split("==", 1)[1].strip()
    return None


def assert_job(job: str, cfg: dict) -> list[str]:
    errors: list[str] = []
    py = cfg["python"]
    mm = _python_mm()

    if job == "proof":
        if mm != py["proof"]:
            errors.append(f"python {mm} != proof pin {py['proof']}")
        z3v = _z3_version()
        if not z3v.startswith(cfg["z3"]["version_prefix"]):
            errors.append(f"z3 {z3v} does not start with {cfg['z3']['version_prefix']}")
    elif job == "golden":
        if mm not in py["minors"]:
            errors.append(f"python {mm} not in golden minors {py['minors']}")
        node_m = _node_major()
        if node_m is None:
            errors.append("node not available")
        elif node_m != int(cfg["node"]["major"]):
            errors.append(f"node major {node_m} != pin {cfg['node']['major']}")
        go_v = _go_version()
        want = cfg["go"]["version"]
        if go_v is None:
            errors.append("go not available")
        elif not go_v.startswith(want):
            errors.append(f"go {go_v} does not start with {want}")
        z3v = _z3_version()
        if not z3v.startswith(cfg["z3"]["version_prefix"]):
            errors.append(f"z3 {z3v} does not start with {cfg['z3']['version_prefix']}")
        pcre = cfg["pcre2"]
        if pcre.get("status") != "n/a":
            errors.append("pcre2 status must be n/a until CI installs it")
        else:
            print(f"pcre2: n/a ({pcre.get('reason')})")
    elif job == "redos":
        if mm != py["redos"]:
            errors.append(f"python {mm} != redos pin {py['redos']}")
        node_m = _node_major()
        if node_m is None or node_m != int(cfg["node"]["major"]):
            errors.append(f"node major {node_m} != pin {cfg['node']['major']}")
        redos = cfg["redos"]
        for pkg, key in (("recheck", "recheck"), ("safe-regex2", "safe_regex2")):
            got = _npm_dep(pkg)
            want = redos[key]
            if got != want:
                errors.append(f"npm {pkg}={got!r} != pin {want!r}")
        rp = _pip_pin("regexploit")
        if rp != redos["regexploit"]:
            errors.append(f"regexploit pin {rp!r} != {redos['regexploit']!r}")
    else:
        errors.append(f"unknown job {job!r}")

    # Cross-check python matrix file for golden/proof minors source of truth
    matrix = _load_toml(ROOT / "ci" / "python-matrix.toml")
    if sorted(matrix.get("minors") or []) != sorted(py["minors"]):
        errors.append(
            f"ci/toolchain.toml python.minors {py['minors']} != "
            f"ci/python-matrix.toml {matrix.get('minors')}"
        )
    return errors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--job", required=True, choices=("proof", "golden", "redos"))
    ap.add_argument(
        "--config",
        type=Path,
        default=ROOT / "ci" / "toolchain.toml",
    )
    args = ap.parse_args(argv)
    cfg = _load_toml(args.config)
    errs = assert_job(args.job, cfg)
    if errs:
        for e in errs:
            print(f"FAIL toolchain drift: {e}", file=sys.stderr)
        return 1
    print(
        f"toolchain ok job={args.job} python={_python_mm()} "
        f"platform={platform.platform()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
