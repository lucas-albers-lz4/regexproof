"""Ground-truth helpers for the pinned LLM honeypot shell sites."""

from __future__ import annotations

import os
import re
import shlex
import subprocess
import tempfile
from pathlib import Path
from typing import Any

PIN = "65624396e263074bb8cb2e049f9a9ec6215ea5c1"
REPO_URL = "https://github.com/Leviticus-Triage/llm-honeypot-intelligence"
SYNC_FILE = "scripts/sync-to-github.sh"
TOR_FILE = "spiderfoot-toolbox/tor-gateway/rotate-tor.sh"
SYNC_SHA256 = "b7cbcd83598d83848516d282de897706da5828df1f1ab6ebcb3f4d87bd203122"
TOR_SHA256 = "0670c3cfcb76b47b0b91a000918afaa9ceea077d6c7b77c4f4a66f1c38522334"
PRIVATE_IP_PATTERN = r"192\.168\.[0-9]+\.[0-9]+"
TOR_PATTERN = "250 OK"


def source_root() -> Path:
    configured = os.environ.get("REGEXPROOF_LHI_SOURCE_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path("/tmp/regexproof-pinned-sources") / f"llm-honeypot-intelligence-{PIN}"


def sed_transform(value: str, pattern: str = PRIVATE_IP_PATTERN) -> str:
    """Run the real sed ERE substitution used by sanitize_dir on one text row."""
    try:
        completed = subprocess.run(
            ["sed", "-E", f"s/{pattern}/[REDACTED]/g"],
            input=value.encode("ascii"),
            capture_output=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError, UnicodeEncodeError):
        return ""
    if completed.returncode != 0:
        return ""
    try:
        return completed.stdout.decode("ascii")
    except UnicodeDecodeError:
        return ""


def grep_matches(value: str, pattern: str = TOR_PATTERN) -> bool:
    """Run the real grep ERE-style line search used by send_newnym."""
    try:
        completed = subprocess.run(
            ["grep", "-q", pattern],
            input=value.encode("ascii"),
            capture_output=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError, UnicodeEncodeError):
        return False
    return completed.returncode == 0


def _git(checkout: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(checkout), *args],
        capture_output=True,
        text=True,
        timeout=10,
        check=True,
    )
    return completed.stdout.strip()


def _pinned_source(checkout: Path, relative: str, expected_sha256: str) -> str:
    import hashlib

    if _git(checkout, "rev-parse", "HEAD") != PIN:
        raise ValueError("LLM honeypot checkout is not at the frozen 20-r2 pin")
    current = checkout / relative
    if current.is_symlink():
        raise ValueError(f"pinned source must not be a symlink: {relative}")
    committed = subprocess.run(
        ["git", "-C", str(checkout), "show", f"{PIN}:{relative}"],
        capture_output=True,
        timeout=10,
        check=True,
    ).stdout
    if current.read_bytes() != committed:
        raise ValueError(f"working source differs from pinned Git blob: {relative}")
    if expected_sha256 and hashlib.sha256(committed).hexdigest() != expected_sha256:
        raise ValueError(f"pinned source hash mismatch: {relative}")
    return committed.decode("utf-8")


def _function_definition(source: str, name: str) -> str:
    lines = source.splitlines()
    start = next(
        (index for index, line in enumerate(lines) if line.strip() == f"{name}() {{"),
        None,
    )
    if start is None:
        raise ValueError(f"pinned source has no {name}() function")
    end = next(
        (index for index in range(start + 1, len(lines)) if lines[index] == "}"),
        None,
    )
    if end is None:
        raise ValueError(f"pinned {name}() function has no closing brace")
    return "\n".join(lines[start : end + 1])


def _shell_pattern(source: str) -> str:
    match = re.search(r"^PRIVATE_IP_PATTERN='([^']*)'$", source, flags=re.MULTILINE)
    if match is None:
        raise ValueError("pinned sync source has no literal PRIVATE_IP_PATTERN")
    return match.group(1)


def run_pinned_sanitizer(
    value: str,
    *,
    checkout: Path | None = None,
    pattern_override: str | None = None,
) -> dict[str, Any]:
    """Run the exact pinned sanitize_dir function on a temporary eligible file."""
    root = (checkout or source_root()).resolve()
    source = _pinned_source(root, SYNC_FILE, SYNC_SHA256)
    source_pattern = _shell_pattern(source)
    pattern = pattern_override if pattern_override is not None else source_pattern
    helper = _function_definition(source, "sanitize_dir")
    script = (
        "set -eu\n"
        f"PRIVATE_IP_PATTERN={shlex.quote(pattern)}\n"
        f"{helper}\n"
        'sanitize_dir "$1"\n'
    )
    with tempfile.TemporaryDirectory(prefix="regexproof-lhi-sanitize-") as temp:
        directory = Path(temp)
        target = directory / "fixture.txt"
        target.write_text(value, encoding="ascii")
        completed = subprocess.run(
            ["bash", "-c", script, "sanitize-gate", str(directory)],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"pinned sanitize_dir failed ({completed.returncode}): "
                f"{completed.stderr.strip()}"
            )
        return {
            "input": value,
            "output": target.read_text(encoding="ascii"),
            "source_pattern": source_pattern,
            "effective_pattern": pattern,
        }


def run_pinned_send_newnym(
    response: str,
    *,
    checkout: Path | None = None,
    pattern_override: str | None = None,
) -> dict[str, Any]:
    """Replay the exact pinned shell function with a local fake nc response."""
    root = (checkout or source_root()).resolve()
    source = _pinned_source(root, TOR_FILE, TOR_SHA256)
    helper = _function_definition(source, "send_newnym")
    if pattern_override is not None:
        original_line = 'grep -q "250 OK"'
        if helper.count(original_line) != 1:
            raise ValueError("pinned send_newnym grep line did not match once")
        helper = helper.replace(original_line, f"grep -q {shlex.quote(pattern_override)}")

    with tempfile.TemporaryDirectory(prefix="regexproof-lhi-tor-") as temp:
        directory = Path(temp)
        bin_dir = directory / "bin"
        bin_dir.mkdir()
        cookie = directory / "control_auth_cookie"
        cookie.write_bytes(b"\xde\xad")
        reply_file = directory / "reply.txt"
        reply_file.write_text(response, encoding="ascii")
        command_capture = directory / "commands.txt"
        fake_nc = bin_dir / "nc"
        fake_nc.write_text(
            "#!/bin/sh\n"
            'cat > "$LHI_COMMAND_CAPTURE"\n'
            'cat "$LHI_REPLY_FILE"\n',
            encoding="ascii",
        )
        fake_nc.chmod(0o755)
        script = (
            f"{helper}\n"
            "if send_newnym; then printf 'success\\n'; "
            "else printf 'failure\\n'; fi\n"
        )
        environment = os.environ.copy()
        environment.update(
            {
                "PATH": f"{bin_dir}{os.pathsep}{environment.get('PATH', '')}",
                "COOKIE_FILE": str(cookie),
                "CONTROL_HOST": "127.0.0.1",
                "CONTROL_PORT": "9051",
                "LHI_REPLY_FILE": str(reply_file),
                "LHI_COMMAND_CAPTURE": str(command_capture),
            }
        )
        completed = subprocess.run(
            ["sh", "-c", script],
            capture_output=True,
            text=True,
            timeout=10,
            env=environment,
            check=False,
        )
        commands = command_capture.read_text(encoding="ascii") if command_capture.exists() else ""
        return {
            "success": completed.stdout.strip() == "success",
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "commands": commands,
            "expected_commands": "AUTHENTICATE dead\nSIGNAL NEWNYM\nQUIT\n",
            "process_returncode": completed.returncode,
            "reply": response,
            "pattern_override": pattern_override,
        }


__all__ = [
    "PIN",
    "PRIVATE_IP_PATTERN",
    "REPO_URL",
    "SYNC_FILE",
    "TOR_FILE",
    "TOR_PATTERN",
    "grep_matches",
    "run_pinned_sanitizer",
    "run_pinned_send_newnym",
    "sed_transform",
    "source_root",
]
