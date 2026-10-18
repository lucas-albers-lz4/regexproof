"""Exact-pin AutoAR JavaScript escaper replay and source mutation helper."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

PIN = "01cd447ad3b1acfed7e0680596c2c74458a4cf06"
REPOSITORY = "https://github.com/h0tak88r/AutoAR.git"
SOURCE_FILE = "internal/api/ui/pages/html-escape.js"
SOURCE_SHA256 = "8b3dd2cc810e7e5c0a88095ca04257a0755f0d22d2fa7d05f2e3479c1f70a900"
_SOURCE_ENV = "AUTOAR_REPLAY_SOURCE"
_DEFAULT_ROOT = (
    Path(tempfile.gettempdir())
    / "regexproof-pinned-sources"
    / f"AutoAR-{PIN}"
)

_REPLACEMENT_SOURCES = (
    b".replace(/&/g, '&amp;')",
    b".replace(/</g, '&lt;')",
    b".replace(/>/g, '&gt;')",
    b'.replace(/\"/g, \'&quot;\')',
    b".replace(/'/g, '&#39;')",
)

_NODE_RUNNER = r"""
const vm = require('node:vm');
let body = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => body += chunk);
process.stdin.on('end', () => {
  const request = JSON.parse(body);
  const context = { window: {} };
  vm.runInNewContext(request.source, context, { timeout: 1000 });
  const outputs = request.values.map(value => context.window.HtmlEscapePage.esc(value));
  process.stdout.write(JSON.stringify({ node: process.version, outputs }));
});
"""


def _git(root: Path, *args: str, binary: bool = False) -> str | bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=not binary,
        timeout=30,
        shell=False,
    )
    return result.stdout if binary else result.stdout.strip()


def _verify_checkout(root: Path) -> None:
    if root.is_symlink() or not root.is_dir():
        raise RuntimeError(f"AutoAR checkout is missing or a symlink: {root}")
    revision = _git(root, "rev-parse", "HEAD")
    if revision != PIN:
        raise RuntimeError(f"AutoAR source is {revision}, expected exact pin {PIN}")
    if _git(root, "status", "--porcelain", "--untracked-files=all"):
        raise RuntimeError("AutoAR source must be a clean pinned checkout")
    source = root / SOURCE_FILE
    if source.is_symlink() or not source.is_file():
        raise RuntimeError(f"pinned AutoAR source is missing or a symlink: {source}")
    committed = _git(root, "show", f"{PIN}:{SOURCE_FILE}", binary=True)
    if not isinstance(committed, bytes) or source.read_bytes() != committed:
        raise RuntimeError("AutoAR escaper bytes differ from the pinned commit")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_SHA256:
        raise RuntimeError(f"AutoAR escaper digest is {digest}, expected {SOURCE_SHA256}")
    start = committed.find(b"function esc(s) {")
    end = committed.find(b"function escAttr(s) {")
    if start < 0 or end <= start:
        raise RuntimeError("AutoAR source no longer has the expected esc function boundary")
    esc_body = committed[start:end]
    cursor = -1
    for replacement in _REPLACEMENT_SOURCES:
        if esc_body.count(replacement) != 1:
            raise RuntimeError(f"AutoAR source no longer has one {replacement!r} site")
        offset = esc_body.index(replacement)
        if offset <= cursor:
            raise RuntimeError("AutoAR escaper replacement order changed")
        cursor = offset


def source_root() -> Path:
    """Return a clean checkout at the frozen 20-r2 AutoAR pin."""
    root = Path(os.environ[_SOURCE_ENV]).expanduser().resolve() if os.environ.get(_SOURCE_ENV) else _DEFAULT_ROOT
    if root.exists():
        _verify_checkout(root)
        return root

    root.parent.mkdir(parents=True, exist_ok=True)
    root.mkdir()
    try:
        _git(root, "init", "--quiet")
        _git(root, "remote", "add", "origin", REPOSITORY)
        _git(root, "fetch", "--quiet", "--depth=1", "origin", PIN)
        _git(root, "checkout", "--quiet", "--detach", "FETCH_HEAD")
        _verify_checkout(root)
    except (OSError, subprocess.SubprocessError, RuntimeError):
        shutil.rmtree(root, ignore_errors=True)
        raise
    return root


def _mutated_source(source: bytes) -> bytes:
    needle = b".replace(/</g, '&lt;')"
    start = source.find(b"function esc(s) {")
    end = source.find(b"function escAttr(s) {")
    if start < 0 or end <= start:
        raise RuntimeError("cannot locate the pinned esc function for mutation")
    esc_body = source[start:end]
    if esc_body.count(needle) != 1:
        raise RuntimeError("cannot uniquely locate the pinned esc less-than replacement")
    mutated_body = esc_body.replace(needle, b".replace(/</g, '<')", 1)
    return source[:start] + mutated_body + source[end:]


def run_esc(values: list[str], *, leak_less_than: bool = False) -> tuple[list[str], str]:
    """Run the real pinned helper in Node's VM with an optional source mutation."""
    source = (source_root() / SOURCE_FILE).read_bytes()
    if leak_less_than:
        source = _mutated_source(source)
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Node.js is required to replay AutoAR's browser helper")
    result = subprocess.run(
        [node, "--eval", _NODE_RUNNER],
        input=json.dumps({"source": source.decode("utf-8"), "values": values}, ensure_ascii=True),
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
        shell=False,
    )
    if result.returncode:
        raise RuntimeError(f"Node helper replay failed ({result.returncode}): {result.stderr.strip()}")
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Node helper replay returned invalid JSON") from exc
    outputs = payload.get("outputs")
    if not isinstance(outputs, list) or len(outputs) != len(values) or any(not isinstance(item, str) for item in outputs):
        raise RuntimeError("Node helper replay returned an invalid output vector")
    return outputs, payload.get("node", "unknown")


def mutation_reproduces(value: str) -> bool:
    if value != "<":
        return False
    outputs, _ = run_esc([value], leak_less_than=True)
    return outputs == ["<"] and "<" in outputs[0]
