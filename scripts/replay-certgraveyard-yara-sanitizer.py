#!/usr/bin/env python3
"""Replay the pinned CertGraveyard sanitizer contract on adversarial inputs.

This loads the real function definitions from generator.py's AST, without
installing the candidate repository's dependencies. It checks the declared
output alphabet and generated-name path-component behavior; it is differential
fuzz evidence, not a solver proof.
"""

from __future__ import annotations

import argparse
import ast
import copy
import itertools
import json
import random
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath
from types import SimpleNamespace
from typing import Any

EXPECTED_PIN = "d965ff32860bef8010f7eb1e7df7b9ea1762d2d4"
TARGET_FUNCTIONS = {"sanitize_name", "generate_rule_filename", "generate_rule_name"}
COMPONENT = re.compile(r"[A-Za-z0-9_]+\Z", re.ASCII)
FILENAME = re.compile(
    r"rule_MAL_Compromised_Cert_[A-Za-z0-9_]+_[A-Za-z0-9_]+_[A-Za-z0-9_]+\.yara\Z",
    re.ASCII,
)
DEFAULTS = ("Unknown_Malware", "Unknown_Issuer", "Unknown_Serial")


def _git_pin(repo: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result.stdout.strip()


def _assert_tracked_files_match_head(repo: Path) -> None:
    result = subprocess.run(
        ["git", "-C", str(repo), "diff", "--quiet", "HEAD", "--"],
        capture_output=True,
        timeout=30,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit("candidate checkout has tracked changes from its pinned HEAD")


def _load_functions(
    source_text: str, filename: str, *, weakened: bool = False
) -> dict[str, Any]:
    tree = ast.parse(source_text, filename=filename)
    nodes = [
        copy.deepcopy(node)
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name in TARGET_FUNCTIONS
    ]
    present = {node.name for node in nodes}
    if present != TARGET_FUNCTIONS:
        raise SystemExit(f"expected {sorted(TARGET_FUNCTIONS)}, found {sorted(present)}")

    mutation_applied = False

    class WeakenFirstClass(ast.NodeTransformer):
        def visit_Call(self, node: ast.Call) -> ast.AST:
            nonlocal mutation_applied
            self.generic_visit(node)
            is_re_sub = (
                isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "re"
                and node.func.attr == "sub"
            )
            if (
                weakened
                and not mutation_applied
                and is_re_sub
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and node.args[0].value == r"[^a-zA-Z0-9]"
            ):
                node.args[0].value = r"[^a-zA-Z0-9/]"
                mutation_applied = True
            return node

    nodes = [WeakenFirstClass().visit(node) for node in nodes]
    if weakened and not mutation_applied:
        raise SystemExit("could not locate first sanitizer character class to mutate")
    module = ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[]))
    namespace: dict[str, Any] = {"re": re, "CertificateRecord": object}
    exec(compile(module, filename, "exec"), namespace)
    return namespace


def _inputs() -> list[str]:
    alphabet = (
        "a", "Z", "7", "_", "/", "\\", ".", "-", "@", " ", "\n", "\x00",
        "é", "\u0661", "\u200b", "\u202e", "💣",
    )
    values = [""]
    for size in range(1, 4):
        values.extend(
            "".join(chars) for chars in itertools.product(alphabet, repeat=size)
        )
    values.extend(chr(codepoint) for codepoint in range(128))
    values.extend(
        [
            "NaN",
            "..",
            "../etc/passwd",
            "..\\..\\Windows\\system.ini",
            "///\\\\",
            "___",
            " leading and trailing ",
            "a\rb\tc",
            "e\u0301",
            "\u202eexe.txt",
            "name\x00.yara",
        ]
    )
    rng = random.Random(0xC37)
    for _ in range(5000):
        size = rng.randrange(0, 65)
        sample = []
        while len(sample) < size:
            cp = rng.randrange(0x110000)
            if not 0xD800 <= cp <= 0xDFFF:
                sample.append(chr(cp))
        values.append("".join(sample))
    return values


def _check(repo: Path) -> dict[str, Any]:
    repo = repo.expanduser().resolve()
    pin = _git_pin(repo)
    if pin != EXPECTED_PIN:
        raise SystemExit(f"source pin mismatch: expected {EXPECTED_PIN}, found {pin}")
    _assert_tracked_files_match_head(repo)
    source = "src/cert_graveyard_yara/generator.py"
    source_text = (repo / source).read_text(encoding="utf-8")
    functions = _load_functions(source_text, source)
    sanitize_name = functions["sanitize_name"]
    make_filename = functions["generate_rule_filename"]
    make_rule_name = functions["generate_rule_name"]

    inputs = _inputs()
    sanitized_checked = 0
    generated_names_checked = 0
    for value in inputs:
        for index in (0, 1, 73):
            components = [sanitize_name(value, default, index) for default in DEFAULTS]
            if not all(COMPONENT.fullmatch(component) for component in components):
                raise SystemExit(f"unsafe component for value={value!r}: {components!r}")
            sanitized_checked += len(components)

            record = SimpleNamespace(
                malware_name=value,
                cert_issuer_short=value,
                cert_serial=value,
            )
            filename = make_filename(record, index)
            rule_name = make_rule_name(record, index)
            if (
                not FILENAME.fullmatch(filename)
                or PurePosixPath(filename).name != filename
                or PureWindowsPath(filename).name != filename
                or not COMPONENT.fullmatch(rule_name)
            ):
                raise SystemExit(
                    f"unsafe generated name for value={value!r}: "
                    f"filename={filename!r}, rule_name={rule_name!r}"
                )
            generated_names_checked += 2

    mutated = _load_functions(source_text, source, weakened=True)["sanitize_name"]
    mutation_witness = "/"
    mutated_output = mutated(mutation_witness, DEFAULTS[0], 0)
    mutation_guard_passed = not COMPONENT.fullmatch(mutated_output)
    if not mutation_guard_passed:
        raise SystemExit("weakened sanitizer unexpectedly preserved the contract")

    return {
        "schema_version": "1",
        "corpus": "tjnel/certgraveyard_yara",
        "pin": pin,
        "site": "src/cert_graveyard_yara/generator.py:79,81:sanitize_name",
        "result": "pass",
        "input_cases": len(inputs),
        "distinct_input_strings": len(set(inputs)),
        "sanitized_components_checked": sanitized_checked,
        "generated_names_checked": generated_names_checked,
        "mutation_guard": {
            "mutation": "allow '/' through the first sanitizer character class",
            "witness": mutation_witness,
            "mutated_output": mutated_output,
            "result": "pass" if mutation_guard_passed else "fail",
        },
        "limits": [
            "Differential replay of the pinned Python implementation; not an SMT proof.",
            "Checks identifier and filename components only; metadata escaping is out of scope.",
            "No length bound is claimed.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path, help="exact-pin candidate checkout")
    parser.add_argument("--output", type=Path, help="write replay result JSON to this path")
    args = parser.parse_args(argv)
    result = _check(args.repo)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.expanduser().resolve().write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
