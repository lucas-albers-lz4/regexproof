"""Exact-pin replay for Xibo's OAuth consent CSRF cookie helper."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

PIN = "978def55c8e68cab3a50a7ee4725039da753f0a1"
REPOSITORY = "https://github.com/xibosignage/xibo-cms"
GIT_REPOSITORY = f"{REPOSITORY}.git"
COMPONENT_FILE = (
    "frontend/src/pages/Administration/Applications/Authorize/AuthorizeApplication.tsx"
)
CSRF_FILE = "lib/Middleware/CsrfGuard.php"
ROUTES_FILE = "lib/routes-react.php"
JSON_ENTRY_FILE = "web/json/index.php"
SOURCE_FILES = {
    COMPONENT_FILE: "8377f717735d9efe5c0148e2691c3d36e91395b91ebaaa61045601d073128513",
    CSRF_FILE: "f4ffd5e29e603ff48ce561d56e43953e996a99ae5b018895da9724ad9cfae826",
    ROUTES_FILE: "c1e17860d451299266b03fa5566085325a2b9ab0d049c9fde56426224da77895",
    JSON_ENTRY_FILE: "2647084b98216a14c72e4c0189c6f29f3296ff7a7745475ebdc4a8d54ca4cedf",
}
_SOURCE_ENV = "XIBO_CSRF_REPLAY_SOURCE"
_DEFAULT_ROOT = (
    Path(tempfile.gettempdir())
    / "regexproof-pinned-sources"
    / f"xibo-cms-{PIN}"
)

_NODE_RUNNER = r"""
const vm = require('node:vm');
let body = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => body += chunk);
process.stdin.on('end', () => {
  const request = JSON.parse(body);
  const context = { document: { cookie: '' } };
  vm.runInNewContext(request.helper, context, { timeout: 1000 });
  const outputs = [];
  for (const cookie of request.cookies) {
    context.document.cookie = cookie;
    outputs.push(context.getCsrfTokenFromCookie());
  }
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


def _safe_source(root: Path, relpath: str) -> bytes:
    rel = Path(relpath)
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        raise RuntimeError(f"unsafe pinned source path: {relpath}")
    cursor = root
    for part in rel.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise RuntimeError(f"pinned source path traverses a symlink: {relpath}")
    source = cursor.resolve()
    source.relative_to(root)
    committed = _git(root, "show", f"{PIN}:{relpath}", binary=True)
    if not isinstance(committed, bytes) or not source.is_file():
        raise RuntimeError(f"pinned source is missing: {relpath}")
    if source.read_bytes() != committed:
        raise RuntimeError(f"working-tree source differs from {PIN}:{relpath}")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != SOURCE_FILES[relpath]:
        raise RuntimeError(f"{relpath} sha256 is {digest}, expected {SOURCE_FILES[relpath]}")
    return committed


def _verify_checkout(root: Path) -> dict[str, bytes]:
    if root.is_symlink() or not root.is_dir():
        raise RuntimeError(f"Xibo checkout is missing or a symlink: {root}")
    revision = _git(root, "rev-parse", "HEAD")
    if revision != PIN:
        raise RuntimeError(f"Xibo source is {revision}, expected exact pin {PIN}")
    if _git(root, "status", "--porcelain", "--untracked-files=all"):
        raise RuntimeError("Xibo source must be a clean pinned checkout")
    sources = {path: _safe_source(root, path) for path in SOURCE_FILES}

    component = sources[COMPONENT_FILE]
    required_component = (
        b"function getCsrfTokenFromCookie(): string {",
        b"document.cookie.match(/(?:^|;\\s*)XSRF-TOKEN=([^;]*)/)",
        b'<input type="hidden" name="csrfToken" value={getCsrfTokenFromCookie()} />',
        b"action={withPublicPath('json/application/authorize')}",
    )
    if any(component.count(fragment) != 1 for fragment in required_component):
        raise RuntimeError("OAuth consent helper/form source shape changed")
    guard = sources[CSRF_FILE]
    required_guard = (
        b"$key = 'csrfToken'",
        b"if ($param == $this->key)",
        b"$userToken = $value;",
        b"if (!hash_equals((string)$token, (string)$userToken))",
        b"$token = bin2hex(random_bytes(20));",
        b"'XSRF-TOKEN',",
        b"'httponly' => false,",
    )
    if any(fragment not in guard for fragment in required_guard):
        raise RuntimeError("CSRF middleware no longer issues/verifies the consent token as reviewed")
    routes = sources[ROUTES_FILE]
    if b"$app->post('/application/authorize'" not in routes:
        raise RuntimeError("pinned route file no longer registers OAuth consent POST")
    entry = sources[JSON_ENTRY_FILE]
    if (
        b"new \\Xibo\\Middleware\\CsrfGuard($app)" not in entry
        or b"require PROJECT_ROOT . '/lib/routes-react.php'" not in entry
    ):
        raise RuntimeError("JSON entrypoint no longer applies CsrfGuard to the route table")
    return sources


def source_root() -> Path:
    """Return a clean checkout at the exact frozen Xibo 20-r2 pin."""
    root = (
        Path(os.environ[_SOURCE_ENV]).expanduser().resolve()
        if os.environ.get(_SOURCE_ENV)
        else _DEFAULT_ROOT
    )
    if root.exists():
        _verify_checkout(root)
        return root
    root.parent.mkdir(parents=True, exist_ok=True)
    root.mkdir()
    try:
        _git(root, "init", "--quiet")
        _git(root, "remote", "add", "origin", GIT_REPOSITORY)
        _git(root, "fetch", "--quiet", "--depth=1", "origin", PIN)
        _git(root, "checkout", "--quiet", "--detach", "FETCH_HEAD")
        _verify_checkout(root)
    except (OSError, subprocess.SubprocessError, RuntimeError):
        shutil.rmtree(root, ignore_errors=True)
        raise
    return root


def _helper_from_source(component: bytes, *, spill_to_neighbor: bool = False) -> str:
    start_marker = b"function getCsrfTokenFromCookie(): string {"
    start = component.find(start_marker)
    end = component.find(b"\n}\n", start)
    if start < 0 or end <= start:
        raise RuntimeError("cannot isolate the exact pinned CSRF cookie helper")
    helper = component[start : end + 2]
    if helper.count(b"(?:^|;\\s*)XSRF-TOKEN=([^;]*)") != 1:
        raise RuntimeError("pinned helper no longer has one expected capture pattern")
    helper = helper.replace(b"(): string {", b"() {", 1)
    if spill_to_neighbor:
        helper = helper.replace(b"([^;]*)", b"(.*)", 1)
        if b"([^;]*)" in helper or b"XSRF-TOKEN=(.*)" not in helper:
            raise RuntimeError("could not apply the exact capture-widening mutation")
    return helper.decode("utf-8")


def run_helper(cookies: list[str], *, spill_to_neighbor: bool = False) -> tuple[list[str], str]:
    """Execute the exact pinned TypeScript helper (type annotation stripped) in Node."""
    component = _verify_checkout(source_root())[COMPONENT_FILE]
    helper = _helper_from_source(component, spill_to_neighbor=spill_to_neighbor)
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Node.js is required for Xibo's browser-helper replay")
    result = subprocess.run(
        [node, "--eval", _NODE_RUNNER],
        input=json.dumps({"helper": helper, "cookies": cookies}, ensure_ascii=True),
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
        shell=False,
    )
    if result.returncode:
        raise RuntimeError(f"Node helper replay failed ({result.returncode}): {result.stderr.strip()}")
    try:
        payload: dict[str, Any] = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Node helper replay returned invalid JSON") from exc
    outputs = payload.get("outputs")
    if not isinstance(outputs, list) or len(outputs) != len(cookies) or any(
        not isinstance(item, str) for item in outputs
    ):
        raise RuntimeError("Node helper replay returned an invalid output vector")
    return outputs, str(payload.get("node", "unknown"))


def mutation_reproduces(captured_character: str) -> bool:
    """Ground the widened capture's semicolon witness in the real helper."""
    if captured_character != ";":
        return False
    token = "a1b2c3d4" * 5
    cookie = f"XSRF-TOKEN={token}; session=neighbor"
    baseline, _ = run_helper([cookie])
    weakened, _ = run_helper([cookie], spill_to_neighbor=True)
    return baseline == [token] and weakened == [f"{token}; session=neighbor"]
