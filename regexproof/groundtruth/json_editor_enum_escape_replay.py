"""Exact-pin Node replay helpers for json-editor's enum HTML escaping."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path

PIN = "b31ddabecf4ed3209d37a2f5b29956120cd8f9ce"
REPOSITORY = "https://github.com/json-editor/json-editor"
REPO_ID = "json-editor/json-editor"
SOURCE_FILE = "src/editors/enum.js"
SOURCE_SHA256 = "315aae54dbaf602bb25c08c064187805a3ac279a61aae8cd6d4d49eec0c44b14"
DEFAULT_SOURCE_ROOT = Path("/tmp/regexproof-pinned-sources") / f"json-editor-{PIN}"


def source_root(root: Path | None = None) -> Path:
    if root is not None:
        return root.resolve()
    configured = os.environ.get("REGEXPROOF_JSON_EDITOR_CHECKOUT")
    return Path(configured).resolve() if configured else DEFAULT_SOURCE_ROOT


def verify_source(root: Path | None = None) -> Path:
    checkout = source_root(root)
    if not checkout.is_dir() or checkout.is_symlink():
        raise RuntimeError(f"exact pinned checkout is unavailable: {checkout}")
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=checkout, check=True,
        capture_output=True, text=True, timeout=10,
    ).stdout.strip()
    if head != PIN:
        raise RuntimeError(f"source pin mismatch: expected {PIN}, found {head}")
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=checkout, check=True,
        capture_output=True, text=True, timeout=10,
    ).stdout
    if status:
        raise RuntimeError("exact pinned checkout is not clean")
    path = checkout / SOURCE_FILE
    if path.is_symlink() or not path.is_file():
        raise RuntimeError("pinned EnumEditor source is missing or a symlink")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"source file hash mismatch: {digest}")
    text = path.read_text(encoding="utf-8")
    required = (
        "this.html_values[i] = this.getHTML(this.enum[i])",
        "this.display_area.innerHTML = this.html_values[this.selected]",
        ".replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')",
    )
    if not all(item in text for item in required):
        raise RuntimeError("EnumEditor source no longer has the reviewed caller/sink chain")
    return checkout


def run_differential_gate(root: Path | None = None, timeout_seconds: int = 300) -> dict:
    checkout = verify_source(root)
    module_url = (checkout / SOURCE_FILE).resolve().as_uri()
    extra_cases = [
        "",
        "<img src=x onerror=alert(1)>",
        "&lt;script&gt;",
        "&&<>",
        "a\x00<&>\n😀",
        "quotes \" and apostrophe '",
    ]
    random_pool = list('abcdefghijklmnopqrstuvwxyz0123456789&<>\\"\'\t\n') + [
        "é", "中", "😀", "\x00"
    ]
    code = f"""
import {{ EnumEditor }} from {json.dumps(module_url)};
const editor = Object.create(EnumEditor.prototype);
const replacements = new Map([['&', '&amp;'], ['<', '&lt;'], ['>', '&gt;']]);
const reference = value => Array.from(value, ch => replacements.get(ch) ?? ch).join('');
let cases = 0;
let mismatches = 0;
let firstMismatch = null;
const check = value => {{
  cases++;
  const actual = editor.getHTML(value);
  const expected = reference(value);
  if (actual !== expected || actual.includes('<') || actual.includes('>')) {{
    mismatches++;
    if (firstMismatch === null) firstMismatch = {{ value, actual, expected }};
  }}
}};
for (let cp = 0; cp <= 0x10ffff; cp++) {{
  if (cp >= 0xd800 && cp <= 0xdfff) continue;
  check(String.fromCodePoint(cp));
}}
const alphabet = ['&', '<', '>', 'a', '\\u0000', '\\n', 'é', '中', '😀'];
const enumerate = (prefix, remaining) => {{
  if (remaining === 0) {{ check(prefix); return; }}
  for (const ch of alphabet) enumerate(prefix + ch, remaining - 1);
}};
for (let length = 1; length <= 3; length++) enumerate('', length);
for (const value of {json.dumps(extra_cases, ensure_ascii=True)}) check(value);
let seed = 0x4a45454e;
const random = () => {{ seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0; return seed; }};
const pool = {json.dumps(random_pool, ensure_ascii=True)};
for (let n = 0; n < 4096; n++) {{
  const length = random() % 256;
  let value = '';
  for (let i = 0; i < length; i++) value += pool[random() % pool.length];
  check(value);
}}
process.stdout.write(JSON.stringify({{ cases, mismatches, firstMismatch }}));
"""
    result = subprocess.run(
        ["node", "--input-type=module", "-e", code],
        cwd=checkout,
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Node differential gate returned invalid JSON: {exc}") from exc
    if report.get("mismatches") != 0 or report.get("cases", 0) < 1_100_000:
        raise RuntimeError(f"Node differential gate failed: {report}")
    report["node_version"] = subprocess.run(
        ["node", "--version"], check=True, capture_output=True, text=True, timeout=10
    ).stdout.strip()
    report["source_pin"] = PIN
    report["source_file_sha256"] = SOURCE_SHA256
    verify_source(checkout)
    return report


def mutation_reproduces(value: str = "<", root: Path | None = None) -> bool:
    checkout = verify_source(root)
    source = checkout / SOURCE_FILE
    original = source.read_text(encoding="utf-8")
    old = ".replace(/</g, '&lt;')"
    new = ".replace(/</g, '<')"
    if original.count(old) != 1:
        raise RuntimeError("expected one reviewed less-than replacement")
    mutated = original.replace(old, new, 1)
    module_url: str | None = None
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".mjs",
            prefix=".regexproof-enum-mutated-", dir=source.parent, delete=False,
        ) as stream:
            stream.write(mutated)
            temp_path = Path(stream.name)
        module_url = temp_path.resolve().as_uri() + "?mutation=less-than"
        code = f"""
import {{ EnumEditor }} from {json.dumps(module_url)};
const editor = Object.create(EnumEditor.prototype);
const value = {json.dumps(value, ensure_ascii=False)};
process.stdout.write(editor.getHTML(value));
"""
        result = subprocess.run(
            ["node", "--input-type=module", "-e", code],
            cwd=checkout,
            check=True,
            capture_output=True,
            text=True,
            timeout=20,
        )
        return value == "<" and result.stdout == "<"
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
        verify_source(checkout)


__all__ = [
    "DEFAULT_SOURCE_ROOT", "PIN", "REPOSITORY", "REPO_ID", "SOURCE_FILE",
    "SOURCE_SHA256", "mutation_reproduces", "run_differential_gate",
    "source_root", "verify_source",
]
