"""Exact-pin replay of Aidevops' pre-read secret-extension guard."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

PIN = "8666b6c6c52472b5535aa295f2df593918152cb1"
REPOSITORY = "https://github.com/marcusquinn/aidevops.git"
SOURCE_FILE = ".agents/plugins/opencode-aidevops/quality-hooks-secret-read.mjs"
SOURCE_SHA256 = "668f7dc002b263d58def6003194fd83dfa91b82b2fdcb9a10b1427f1cb942cf0"
_SOURCE_ENV = "AIDEVOPS_SECRET_READ_REPLAY_SOURCE"
_DEFAULT_ROOT = (
    Path(tempfile.gettempdir())
    / "regexproof-pinned-sources"
    / f"aidevops-{PIN}"
)

CALLER_SHA256 = {
    ".agents/plugins/opencode-aidevops/quality-hooks.mjs":
        "3da80b121d778f474e4f7e25983e6041877731cf415fae90e61ed8c64677747d",
    ".agents/plugins/opencode-aidevops/source-access-approval.mjs":
        "c7bfa82af900399621f2d1c107470a9fe65b39d2814f5191da9f04f78d32860d",
}

SOURCE_PATTERN = r"\.(pem|key|p12|pfx|kdbx|age|asc|gpg)$"
SOURCE_BASENAME_PATTERN = (
    r"^(id_(rsa|dsa|ecdsa|ed25519)|\.env(\..*)?|credentials(\.sh|\.json|\.ya?ml)?|"
    r"service-account(\.json)?|kubeconfig|config\.json|op-vault-export.*|"
    r".*password.*|.*passwd.*|.*secret.*)$"
)
READ_TOOLS = ("Read", "Glob", "NotebookRead")
_DECLARATION = (
    b"const SECRET_EXTENSION_RE = /\\.(pem|key|p12|pfx|kdbx|age|asc|gpg)$/i;"
)
_MUTATED_DECLARATION = (
    b"const SECRET_EXTENSION_RE = /\\.(key|p12|pfx|kdbx|age|asc|gpg)$/i;"
)
_BASENAME_DECLARATION = (
    b"const SECRET_BASENAME_RE = /^(id_(rsa|dsa|ecdsa|ed25519)|\\.env(\\..*)?|"
    b"credentials(\\.sh|\\.json|\\.ya?ml)?|service-account(\\.json)?|kubeconfig|"
    b"config\\.json|op-vault-export.*|.*password.*|.*passwd.*|.*secret.*)$/i;"
)
_MUTATED_BASENAME_DECLARATION = (
    b"const SECRET_BASENAME_RE = /^(id_(rsa|dsa|ecdsa|ed25519)|\\.env(\\..*)?|"
    b"credentials(\\.sh|\\.json|\\.ya?ml)?|service-account(\\.json)?|kubeconfig|"
    b"config\\.json|op-vault-export.*|.*password.*|.*passwd.*)$/i;"
)

_NODE_RUNNER = r"""
import { pathToFileURL } from "node:url";
const request = JSON.parse(await new Promise((resolve, reject) => {
  let input = "";
  process.stdin.setEncoding("utf8");
  process.stdin.on("data", chunk => input += chunk);
  process.stdin.on("end", () => resolve(input));
  process.stdin.on("error", reject);
}));
const module = await import(pathToFileURL(request.modulePath).href);
const results = request.cases.map(({ path, tool = "Read" }) => {
  const reason = module.secretReadBlockReason(path);
  let blocked = false;
  let message = "";
  try {
    module.checkSecretReadGate(tool, { filePath: path }, () => {});
  } catch (error) {
    blocked = true;
    message = String(error?.message || error);
  }
  return { reason, blocked, message };
});
process.stdout.write(JSON.stringify({ node: process.version, results }));
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


def _safe_source_file(root: Path, relative: str, expected_sha256: str) -> bytes:
    path = root / relative
    cursor = root
    for part in Path(relative).parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise RuntimeError(f"Aidevops source path traverses a symlink: {relative}")
    if not path.is_file():
        raise RuntimeError(f"Aidevops pinned source is missing: {relative}")
    committed = _git(root, "show", f"{PIN}:{relative}", binary=True)
    if not isinstance(committed, bytes) or path.read_bytes() != committed:
        raise RuntimeError(f"Aidevops worktree bytes differ from pin: {relative}")
    digest = hashlib.sha256(committed).hexdigest()
    if digest != expected_sha256:
        raise RuntimeError(f"Aidevops source digest differs at {relative}: {digest}")
    return committed


def _verify_checkout(root: Path) -> None:
    if root.is_symlink() or not root.is_dir():
        raise RuntimeError(f"Aidevops replay checkout is missing or a symlink: {root}")
    if _git(root, "rev-parse", "HEAD") != PIN:
        raise RuntimeError(f"Aidevops replay source is not at exact pin {PIN}")
    if _git(root, "remote", "get-url", "origin").removesuffix(".git") != REPOSITORY.removesuffix(".git"):
        raise RuntimeError("Aidevops replay origin differs from the frozen repository")
    if _git(root, "status", "--porcelain", "--untracked-files=all"):
        raise RuntimeError("Aidevops replay checkout must be clean")
    source = _safe_source_file(root, SOURCE_FILE, SOURCE_SHA256)
    if source.count(_DECLARATION) != 1:
        raise RuntimeError("Aidevops secret-extension declaration changed at the pinned source")
    for relative, digest in CALLER_SHA256.items():
        caller = _safe_source_file(root, relative, digest)
        if relative.endswith("quality-hooks.mjs") and not (
            b"checkSecretReadWithApproval({" in caller
            and b"checkSecretReadGate," in caller
        ):
            raise RuntimeError("pinned quality-hook caller no longer wires the secret-read gate")
        if relative.endswith("source-access-approval.mjs") and not (
            b"secretReadBlockReason(filePath)" in caller
            and b"checkSecretReadGate(tool, args, log);" in caller
        ):
            raise RuntimeError("pinned pre-read path no longer falls back to the secret-read gate")


def source_root() -> Path:
    """Return a clean checkout at the exact Aidevops source pin."""
    configured = os.environ.get(_SOURCE_ENV)
    root = Path(configured).expanduser().resolve() if configured else _DEFAULT_ROOT
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


def _mutated_extension_source(source: bytes) -> bytes:
    if source.count(_DECLARATION) != 1:
        raise RuntimeError("cannot uniquely locate the pinned extension expression")
    return source.replace(_DECLARATION, _MUTATED_DECLARATION, 1)


def _mutated_basename_source(source: bytes) -> bytes:
    if source.count(_BASENAME_DECLARATION) != 1:
        raise RuntimeError("cannot uniquely locate the pinned basename expression")
    return source.replace(_BASENAME_DECLARATION, _MUTATED_BASENAME_DECLARATION, 1)


def run_secret_read(
    paths: list[str],
    *,
    tools: list[str] | None = None,
    omit_pem_extension: bool = False,
    omit_secret_basename: bool = False,
) -> tuple[list[dict[str, str | bool]], str]:
    """Run the actual pinned guard, optionally with one source mutation."""
    root = source_root()
    source_path = root / SOURCE_FILE
    temporary = None
    module_path = source_path
    if omit_pem_extension or omit_secret_basename:
        source = source_path.read_bytes()
        if omit_pem_extension:
            source = _mutated_extension_source(source)
        if omit_secret_basename:
            source = _mutated_basename_source(source)
        temporary = tempfile.TemporaryDirectory(prefix="aidevops-secret-read-mutation-")
        module_path = Path(temporary.name) / "quality-hooks-secret-read.mjs"
        module_path.write_bytes(source)
    cases = [
        {"path": path, "tool": tools[index] if tools else "Read"}
        for index, path in enumerate(paths)
    ]
    node = shutil.which("node")
    if not node:
        if temporary:
            temporary.cleanup()
        raise RuntimeError("Node.js is required to replay Aidevops' pre-read guard")
    try:
        result = subprocess.run(
            [node, "--input-type=module", "--eval", _NODE_RUNNER],
            input=json.dumps({"modulePath": str(module_path), "cases": cases}, ensure_ascii=True),
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
            shell=False,
        )
        if result.returncode:
            raise RuntimeError(
                f"Aidevops Node replay failed ({result.returncode}): {result.stderr.strip()}"
            )
        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("Aidevops Node replay returned invalid JSON") from exc
        results = payload.get("results")
        if not isinstance(results, list) or len(results) != len(paths):
            raise RuntimeError("Aidevops Node replay returned an invalid result vector")
        return results, str(payload.get("node", "unknown"))
    finally:
        if temporary:
            temporary.cleanup()


def mutation_reproduces(basename: str) -> bool:
    if basename != "proof.pem":
        return False
    results, _ = run_secret_read(
        [f"/tmp/{basename}"], omit_pem_extension=True
    )
    return len(results) == 1 and not results[0]["blocked"] and not results[0]["reason"]


def mutation_reproduces_secret_basename(basename: str) -> bool:
    """Replay the real helper after removing its secret-substring alternative."""
    if basename != "secret":
        return False
    results, _ = run_secret_read(
        [f"/tmp/{basename}"] * len(READ_TOOLS),
        tools=list(READ_TOOLS),
        omit_secret_basename=True,
    )
    return len(results) == len(READ_TOOLS) and all(
        not result["blocked"] and not result["reason"] for result in results
    )
