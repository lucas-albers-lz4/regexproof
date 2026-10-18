"""Exact-pin replays for Aidevops webhook receiver contracts."""

from __future__ import annotations

import hashlib
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from regexproof.groundtruth.aidevops_cited_file_replay import _source_bytes, source_root

PIN = "8666b6c6c52472b5535aa295f2df593918152cb1"
REPOSITORY = "https://github.com/marcusquinn/aidevops"
RECEIVER_FILE = ".agents/scripts/pulse-merge-webhook-receiver.sh"
RECEIVER_SHA256 = "6d882dac90c3f9deb1a0007c9a4216d70f365a4a34ffacd145eb04cc8ae3a325"
_SUPPORT = {
    ".agents/scripts/pulse-merge-webhook-server.py": "9d421c8d07d15c28ca541b4acc8d32dd4c96f402abf7d4a76e229972edf92862",
    ".agents/configs/webhook-receiver.conf": "67facfca1f93dc0d8e06f2f7b391596f971fb6011fce3c5322fcafcbcb8917c3",
    ".agents/reference/auto-merge.md": "a46aafe164dccdfd4cc949fd5a0108d2f82f3854f91107fce991d52dd0ca0794",
    ".agents/scripts/tests/test-pulse-merge-webhook-invalidation.py": "766e742f356c9290e7143d62f72eb88ac3eb5a0c4e33de11652e8e74dd2e2058",
}


def _function(source: str, name: str) -> str:
    matches = list(re.finditer(rf"(?ms)^{re.escape(name)}\(\) \{{.*?^\}}$", source))
    if len(matches) != 1:
        raise RuntimeError(f"pinned Bash function {name} is missing or ambiguous")
    return matches[0].group(0)


def _source(mutation: str | None = None) -> str:
    root = source_root()
    for path, digest in _SUPPORT.items():
        _source_bytes(root, path, digest)
    raw = _source_bytes(root, RECEIVER_FILE, RECEIVER_SHA256)
    source = raw.decode("utf-8")
    if hashlib.sha256(raw).hexdigest() != RECEIVER_SHA256:
        raise RuntimeError("Aidevops webhook receiver digest mismatch")
    if mutation is None:
        return source
    mutations = {
        "secret_env": (
            "_resolve_secret",
            '[[ "$env_var_name" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]',
            '[[ "$env_var_name" =~ ^[A-Za-z0-9_][A-Za-z0-9_]*$ ]]',
        ),
        "slug_owner": (
            "_webhook_valid_slug",
            '[[ "$owner" =~ ^[A-Za-z0-9][A-Za-z0-9_.-]*$ ]]',
            '[[ "$owner" =~ ^[A-Za-z0-9_.-]+$ ]]',
        ),
        "sha_length": (
            "_webhook_invalidate_checks",
            '[[ "$sha" =~ ^[A-Fa-f0-9]{40}$ ]]',
            '[[ "$sha" =~ ^[A-Fa-f0-9]{1,40}$ ]]',
        ),
        "pr_number": (
            "_dispatch_webhook_action_line",
            '[[ ! "$pr_number" =~ ^[0-9]+$ || "$pr_number" -le 0 ]]',
            '[[ ! "$pr_number" =~ ^.*$ || "$pr_number" -le 0 ]]',
        ),
    }
    if mutation not in mutations:
        raise ValueError(f"unknown mutation {mutation}")
    name, old, new = mutations[mutation]
    function = _function(source, name)
    if function.count(old) != 1:
        raise RuntimeError(f"pinned mutation target for {name} is ambiguous")
    return source.replace(function, function.replace(old, new, 1), 1)


def _run(
    names: tuple[str, ...],
    body: str,
    args: tuple[str, ...] = (),
    *,
    mutation: str | None = None,
    extra_env: dict[str, str] | None = None,
) -> dict[str, Any]:
    source = _source(mutation)
    script = "set +e\n" + "\n\n".join(_function(source, n) for n in names) + "\n\n" + body
    with tempfile.TemporaryDirectory(prefix="aidevops-webhook-replay-") as temp_name:
        temp = Path(temp_name)
        home = temp / "home"
        empty_bin = temp / "bin"
        home.mkdir()
        empty_bin.mkdir()
        env = {"HOME": str(home), "PATH": str(empty_bin), "LC_ALL": "C"}
        env.update(extra_env or {})
        completed = subprocess.run(
            ["/bin/bash", "-s", "--", *args],
            input=script,
            text=True,
            capture_output=True,
            env=env,
            timeout=15,
            check=False,
            shell=False,
        )
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "source_pin": PIN,
        "repository": REPOSITORY,
        "source_file": RECEIVER_FILE,
        "source_sha256": RECEIVER_SHA256,
        "mutation": mutation,
    }


def secret_name_accepts(name: str, *, mutation: str | None = None) -> bool:
    result = _run(
        ("_resolve_secret",),
        'WEBHOOK_SECRET_ENV="$1"\nif _resolve_secret >/dev/null 2>&1; then printf yes; else printf no; fi\n',
        (name,),
        mutation=mutation,
    )
    return result["returncode"] == 0 and result["stdout"] == "yes"


def secret_resolution_and_clear() -> dict[str, Any]:
    return _run(
        ("_resolve_secret", "_clear_webhook_secret_env"),
        'WEBHOOK_SECRET_ENV=AIDEVOPS_WEBHOOK_SECRET\n'
        'if [[ "$(_resolve_secret)" != fixture-secret ]]; then exit 10; fi\n'
        '_clear_webhook_secret_env || exit 11\n'
        '[[ -z "${AIDEVOPS_WEBHOOK_SECRET+x}" ]] || exit 12\n'
        "printf ok",
        extra_env={"AIDEVOPS_WEBHOOK_SECRET": "fixture-secret"},
    )


def slug_accepts(slug: str, *, mutation: str | None = None) -> bool:
    result = _run(
        ("_webhook_valid_slug",),
        'if _webhook_valid_slug "$1"; then printf yes; else printf no; fi\n',
        (slug,),
        mutation=mutation,
    )
    return result["returncode"] == 0 and result["stdout"] == "yes"


def sha_reaches_invalidator(slug: str, sha: str, *, mutation: str | None = None) -> bool:
    result = _run(
        ("_webhook_valid_slug", "_webhook_invalidate_checks"),
        'calls=0\n'
        'gh_pr_check_status_cache_invalidate() { calls=$((calls + 1)); return 0; }\n'
        '_whlog() { :; }\n'
        '_webhook_invalidate_checks "$1" "$2" >/dev/null 2>&1\n'
        'printf "%s" "$calls"\n',
        (slug, sha),
        mutation=mutation,
    )
    return result["returncode"] == 0 and result["stdout"] == "1"


def dispatches(record: str, *, mutation: str | None = None) -> str | None:
    with tempfile.TemporaryDirectory(prefix="aidevops-webhook-dispatch-") as temp_name:
        calls = Path(temp_name) / "calls.txt"
        result = _run(
            ("_webhook_valid_slug", "_webhook_wait_for_dispatch_slot", "_dispatch_webhook_action_line"),
            'process_pr() { printf "%s|%s\\n" "$1" "$2" >>"$CALLS"; return 0; }\n'
            '_whlog() { :; }\n'
            '_webhook_wait_for_dispatch_slot() { :; }\n'
            '_WEBHOOK_INVALIDATION_FAILED=0\n'
            '_dispatch_webhook_action_line "$1"\n'
            'wait\n'
            'if [[ -s "$CALLS" ]]; then IFS= read -r called <"$CALLS"; printf "%s" "$called"; else printf NONE; fi\n',
            (record,),
            mutation=mutation,
            extra_env={"CALLS": str(calls)},
        )
    if result["returncode"] != 0:
        raise RuntimeError(f"pinned action dispatcher exited unexpectedly: {result}")
    return None if result["stdout"] == "NONE" else result["stdout"]


def secret_env_mutation_reproduces(witness: dict[str, str]) -> bool:
    name = witness.get("name", "")
    if name != "8SECRET":
        return False
    original = secret_name_accepts(name)
    mutated = _run(
        ("_resolve_secret",),
        'WEBHOOK_SECRET_ENV="$1"\n_resolve_secret >/dev/null\nprintf returned\n',
        (name,),
        mutation="secret_env",
    )
    return (
        not original
        and mutated["returncode"] == 0
        and "invalid variable name" in mutated["stderr"]
        and mutated["stdout"] == "returned"
    )


def slug_mutation_reproduces(witness: dict[str, str]) -> bool:
    slug = witness.get("slug", "")
    return slug == ".owner/repo" and not slug_accepts(slug) and slug_accepts(
        slug, mutation="slug_owner"
    )


def sha_mutation_reproduces(witness: dict[str, str]) -> bool:
    sha = witness.get("sha", "")
    return sha == "a" and not sha_reaches_invalidator("owner/repo", sha) and sha_reaches_invalidator(
        "owner/repo", sha, mutation="sha_length"
    )


def pr_number_mutation_reproduces(witness: dict[str, str]) -> bool:
    number = witness.get("number", "")
    record = f"PROCESS_PR owner/repo {number}"
    return number == "2#1" and dispatches(record) is None and dispatches(
        record, mutation="pr_number"
    ) == f"owner/repo|{number}"


__all__ = [
    "PIN", "RECEIVER_FILE", "RECEIVER_SHA256", "REPOSITORY",
    "dispatches", "pr_number_mutation_reproduces", "secret_env_mutation_reproduces",
    "secret_name_accepts", "secret_resolution_and_clear", "sha_mutation_reproduces",
    "sha_reaches_invalidator", "slug_accepts", "slug_mutation_reproduces",
]
