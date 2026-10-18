"""Exact-pin replay for Real-Router's navigation parameter validator."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any

PIN = "55aa7ef43a9c129beba90823cd8a4db10bb01211"
REPOSITORY = "https://github.com/greydragon888/real-router"
REPO_ID = "greydragon888/real-router"
NAVIGATION_FILE = "packages/validation-plugin/src/validators/navigation.ts"
PLUGIN_FILE = "packages/validation-plugin/src/validationPlugin.ts"
TEST_FILE = "packages/validation-plugin/tests/functional/navigation.validation.test.ts"
CHANGELOG_FILE = "packages/validation-plugin/CHANGELOG.md"
SOURCE_SHA256 = "619bbc25796534163c82de8f01dab1ab3fc38cd844a7a0742301dab0534173c6"
PINNED_FILES = {
    NAVIGATION_FILE: SOURCE_SHA256,
    "packages/validation-plugin/src/type-guards/guards/params.ts":
        "4d3f2cee1ed7547667f0a42aff758c300dbe74669c6c9218e576e2b120b51c47",
    "packages/validation-plugin/src/type-guards/guards/navigation.ts":
        "1da164545d069bfec2b56b4f701f80985dc97c7bd3aa2d80aec25bb95926be89",
    "packages/validation-plugin/src/type-guards/guards/primitives.ts":
        "2c20b34bd5a28bed084b22aeca85c79923f17860d33202fd00c4baaf1703bac8",
    "packages/validation-plugin/src/type-guards/utilities/type-description.ts":
        "65c651fce462e31b68c5acfaef8d9e647b977f567b64b4429643515515bbf102",
    PLUGIN_FILE:
        "903f06ac7e3a55a85512b25d30acd41b122dd919b9f7478a11b33740c0fbbc2a",
    TEST_FILE:
        "63763865c3a73ab2cb2a23636d07ae2bfec091ea2d1612d3e015b26dc17f01f6",
    CHANGELOG_FILE:
        "318ae54e5918a681c644c00c42e347ce4c9d08e9bbc56a5d4536abd349fff1f9",
}
DEFAULT_SOURCE_ROOT = Path(
    "/tmp/regexproof-pinned-sources/real-router-55aa7ef43a9c129beba90823cd8a4db10bb01211"
)

_NODE_REPLAY = r'''import fs from "node:fs";
import { validateNavigateParams } from "./src/validators/navigation.mts";

const input = JSON.parse(fs.readFileSync(0, "utf8"));
const outcomes = [];
for (const value of input.values) {
  try {
    validateNavigateParams({ value }, "navigate");
    outcomes.push("accepted");
  } catch (error) {
    outcomes.push(error?.name || "Error");
  }
}
process.stdout.write(JSON.stringify({ version: process.version, outcomes }));
'''


def source_root() -> Path:
    return Path(os.environ.get("REAL_ROUTER_REPLAY_SOURCE", DEFAULT_SOURCE_ROOT)).resolve()


def _run(argv: list[str], *, cwd: Path | None = None, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        argv,
        cwd=cwd,
        input=input_text,
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
        shell=False,
    )


def _pinned_source(root: Path, relative: str, expected_sha256: str) -> bytes:
    path = root / relative
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"pinned Real-Router source is missing or a symlink: {path}")
    source = path.read_bytes()
    shown = _run(["git", "-C", str(root), "show", f"{PIN}:{relative}"])
    if shown.returncode != 0 or shown.stdout.encode("utf-8") != source:
        raise RuntimeError(f"working source differs from {PIN}:{relative}")
    digest = hashlib.sha256(source).hexdigest()
    if digest != expected_sha256:
        raise RuntimeError(
            f"Real-Router {relative} digest is {digest}, expected {expected_sha256}"
        )
    return source


def verify_source(root: Path | None = None) -> dict[str, Any]:
    root = (root or source_root()).resolve()
    head = _run(["git", "-C", str(root), "rev-parse", "HEAD"])
    if head.returncode != 0 or head.stdout.strip() != PIN:
        raise RuntimeError(f"Real-Router checkout is not at expected pin {PIN}")
    status = _run(["git", "-C", str(root), "status", "--porcelain=v1", "--untracked-files=all"])
    if status.returncode != 0 or status.stdout.strip():
        raise RuntimeError("Real-Router source checkout is not clean")
    bindings = {
        relative: hashlib.sha256(_pinned_source(root, relative, digest)).hexdigest()
        for relative, digest in PINNED_FILES.items()
    }
    navigation = (root / NAVIGATION_FILE).read_text(encoding="utf-8")
    declaration = r"const CONTROL_CHARS_RE = /[\u0000-\u001F\u007F]/;"
    if navigation.count(declaration) != 1:
        raise RuntimeError("pinned CONTROL_CHARS_RE declaration changed or is ambiguous")
    if navigation.count("if (valueType === \"string\" && CONTROL_CHARS_RE.test(value as string))") != 1:
        raise RuntimeError("pinned parameter validation no longer searches each string value")
    if navigation.count("export function validateNavigateParams(") != 1:
        raise RuntimeError("pinned validateNavigateParams export changed")
    lines = navigation.splitlines()
    if len(lines) < 69 or lines[68][25] != "/":
        raise RuntimeError("frozen inventory column-25 selector no longer points at the regex")
    plugin = (root / PLUGIN_FILE).read_text(encoding="utf-8")
    if plugin.count("validateParams: validateNavigateParams") != 1:
        raise RuntimeError("pinned opt-in plugin wiring changed")
    return {"pin": PIN, "source_files": bindings}


def _adapt_params_type_parameter_property(source: str) -> str:
    """Translate one TS-only parameter property to its equivalent JS field write."""
    old = "class SubtreeExit {\n  constructor(readonly container: object) {}\n}"
    new = (
        "class SubtreeExit {\n"
        "  constructor(container) {\n"
        "    this.container = container;\n"
        "  }\n"
        "}"
    )
    if source.count(old) != 1:
        raise RuntimeError("pinned params helper parameter-property adapter no longer applies uniquely")
    return source.replace(old, new, 1)


def _write_exact_modules(root: Path, source_root_path: Path, *, weakened: bool) -> None:
    runtime_files = (
        NAVIGATION_FILE,
        "packages/validation-plugin/src/type-guards/guards/params.ts",
        "packages/validation-plugin/src/type-guards/guards/navigation.ts",
        "packages/validation-plugin/src/type-guards/guards/primitives.ts",
        "packages/validation-plugin/src/type-guards/utilities/type-description.ts",
    )
    files = {
        relative: (source_root_path / relative).read_text(encoding="utf-8")
        for relative in runtime_files
    }
    navigation = files[NAVIGATION_FILE]
    import_from = 'from "../type-guards";'
    import_to = 'from "../type-guards/index.mts";'
    if navigation.count(import_from) != 1:
        raise RuntimeError("cannot uniquely adapt navigation type-guard import")
    navigation = navigation.replace(import_from, import_to, 1)
    declaration = r"const CONTROL_CHARS_RE = /[\u0000-\u001F\u007F]/;"
    if weakened:
        replacement = r"const CONTROL_CHARS_RE = /[\u0000-\u001F]/;"
        if navigation.count(declaration) != 1:
            raise RuntimeError("cannot uniquely source-mutate CONTROL_CHARS_RE")
        navigation = navigation.replace(declaration, replacement, 1)

    params_path = "packages/validation-plugin/src/type-guards/guards/params.ts"
    params = _adapt_params_type_parameter_property(files[params_path])
    base = root / "src"
    (base / "validators").mkdir(parents=True, exist_ok=True)
    (base / "type-guards" / "guards").mkdir(parents=True, exist_ok=True)
    (base / "type-guards" / "utilities").mkdir(parents=True, exist_ok=True)
    (base / "validators" / "navigation.mts").write_text(navigation, encoding="utf-8")
    module_paths = {
        params_path: base / "type-guards" / "guards" / "params.mts",
        "packages/validation-plugin/src/type-guards/guards/navigation.ts":
            base / "type-guards" / "guards" / "navigation.mts",
        "packages/validation-plugin/src/type-guards/guards/primitives.ts":
            base / "type-guards" / "guards" / "primitives.mts",
        "packages/validation-plugin/src/type-guards/utilities/type-description.ts":
            base / "type-guards" / "utilities" / "type-description.mts",
    }
    for relative, destination in module_paths.items():
        body = params if relative == params_path else files[relative]
        destination.write_text(body, encoding="utf-8")
    (base / "type-guards" / "index.mts").write_text(
        'export { getTypeDescription } from "./utilities/type-description.mts";\n'
        'export { isNavigationOptions } from "./guards/navigation.mts";\n'
        'export { isParams } from "./guards/params.mts";\n'
        'export { isString } from "./guards/primitives.mts";\n',
        encoding="utf-8",
    )
    (root / "replay.mts").write_text(_NODE_REPLAY, encoding="utf-8")


def run_helper_values(
    values: list[str], *, weakened: bool = False, root: Path | None = None
) -> dict[str, Any]:
    """Run the pinned validator with only TS import/type syntax adapted."""
    source = (root or source_root()).resolve()
    verify_source(source)
    with tempfile.TemporaryDirectory(prefix="regexproof-real-router-navigation-") as temp:
        temp_root = Path(temp)
        _write_exact_modules(temp_root, source, weakened=weakened)
        proc = _run(
            ["node", "--experimental-strip-types", str(temp_root / "replay.mts")],
            cwd=temp_root,
            input_text=json.dumps({"values": values}, ensure_ascii=True),
        )
    if proc.returncode != 0:
        raise RuntimeError(
            "Node exact-source navigation validator replay failed: "
            f"{proc.stderr.strip() or proc.stdout.strip()}"
        )
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Node exact-source navigation replay returned invalid JSON") from exc
    if result.get("version") is None or len(result.get("outcomes", [])) != len(values):
        raise RuntimeError("Node exact-source navigation replay returned incomplete evidence")
    return result


def del_removal_mutation_reproduces(witness: dict[str, str]) -> bool:
    if witness.get("navigation_control_char") != "\x7f":
        return False
    original = run_helper_values(["\x7f"])
    weakened = run_helper_values(["\x7f"], weakened=True)
    return (
        original["outcomes"] == ["TypeError"]
        and weakened["outcomes"] == ["accepted"]
    )


__all__ = [
    "CHANGELOG_FILE",
    "DEFAULT_SOURCE_ROOT",
    "NAVIGATION_FILE",
    "PIN",
    "PINNED_FILES",
    "PLUGIN_FILE",
    "REPO_ID",
    "REPOSITORY",
    "SOURCE_SHA256",
    "TEST_FILE",
    "del_removal_mutation_reproduces",
    "run_helper_values",
    "source_root",
    "verify_source",
]
