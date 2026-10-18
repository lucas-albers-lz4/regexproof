"""Tests for source-bound P2 cohort inventory generation."""

from __future__ import annotations

import hashlib
import subprocess

from regexproof.mine.cohort_manifest import build_manifest
from regexproof.mine.p2_source_inventory import build_source_inventory


def _manifest(repo_id: str, pin: str):
    return build_manifest(
        {
            "candidates": [
                {
                    "repo_id": repo_id,
                    "url": f"https://github.com/{repo_id}",
                    "pin": pin,
                    "dialect_family": "py_re",
                    "boundary_family": "validator",
                    "score": 1,
                    "sites": 1,
                    "fork": False,
                    "duplicate_of": None,
                    "partial": False,
                }
            ]
        },
        "p2-test-cohort",
        1,
    )


def _git(path, *args):
    subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True)


def _pinned_repo(tmp_path, *, external_symlink=False):
    root = tmp_path / "repo"
    root.mkdir()
    _git(root, "init", "--quiet")
    _git(root, "config", "user.email", "regexproof@example.invalid")
    _git(root, "config", "user.name", "regexproof test")
    _git(root, "remote", "add", "origin", "https://github.com/example/repo")
    source = root / "validator.py"
    source.write_text("import re\nPATTERN = re.compile(r'^[^;]+$')\n", encoding="utf-8")
    if external_symlink:
        outside = tmp_path / "outside.py"
        outside.write_text("import re\nre.search('outside', value)\n", encoding="utf-8")
        (root / "external.py").symlink_to(outside)
    _git(root, "add", "validator.py", *( ["external.py"] if external_symlink else []))
    _git(root, "commit", "--quiet", "-m", "fixture")
    pin = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    return root, pin


def test_inventory_binds_site_to_manifest_tree_and_source_bytes(tmp_path):
    root, pin = _pinned_repo(tmp_path)
    manifest = _manifest("example/repo", pin)

    artifact, sites = build_source_inventory(
        manifest,
        {"example/repo": root},
        cohort_manifest_sha256="a" * 64,
    )

    assert artifact["summary"]["complete_repositories"] == 1
    assert artifact["summary"]["source_sites"] == 1
    assert artifact["summary"]["attempted_questions"] == 0
    assert artifact["repositories"][0]["commit_tree_oid"] == sites[0]["commit_tree_oid"]
    assert sites[0]["source_file"] == "validator.py"
    assert sites[0]["source_file_sha256"] == hashlib.sha256(
        (root / "validator.py").read_bytes()
    ).hexdigest()
    assert sites[0]["git_blob_oid"]
    assert sites[0]["review_status"] == "unreviewed"
    assert sites[0]["contract_status"] == "none"
    assert sites[0]["solver_outcome"] is None


def test_inventory_keeps_missing_checkout_in_original_cohort():
    manifest = _manifest("example/repo", "a" * 40)

    artifact, sites = build_source_inventory(
        manifest, {}, cohort_manifest_sha256="b" * 64
    )

    assert artifact["summary"]["cohort_repositories"] == 1
    assert artifact["summary"]["complete_repositories"] == 0
    assert artifact["repositories"][0]["status"] == "missing_checkout"
    assert sites == []


def test_inventory_refuses_external_source_symlink(tmp_path):
    root, pin = _pinned_repo(tmp_path, external_symlink=True)
    manifest = _manifest("example/repo", pin)

    artifact, sites = build_source_inventory(
        manifest,
        {"example/repo": root},
        cohort_manifest_sha256="c" * 64,
    )

    assert artifact["repositories"][0]["status"] == "failed"
    assert "resolves outside" in artifact["repositories"][0]["error"]
    assert sites == []


def test_inventory_records_pinned_gitlinks_as_incomplete_without_guessing(tmp_path):
    root, _ = _pinned_repo(tmp_path)
    child = tmp_path / "child"
    child.mkdir()
    _git(child, "init", "--quiet")
    _git(child, "config", "user.email", "regexproof@example.invalid")
    _git(child, "config", "user.name", "regexproof test")
    (child / "nested.py").write_text(
        "import re\nre.search(r'child', value)\n", encoding="utf-8"
    )
    _git(child, "add", "nested.py")
    _git(child, "commit", "--quiet", "-m", "child fixture")
    gitlink_oid = subprocess.check_output(
        ["git", "-C", str(child), "rev-parse", "HEAD"], text=True
    ).strip()
    subprocess.run(
        [
            "git", "-c", "protocol.file.allow=always", "-C", str(root),
            "submodule", "add", str(child), "deps/fake",
        ],
        check=True,
        capture_output=True,
    )
    _git(root, "add", ".gitmodules", "deps/fake")
    _git(root, "commit", "--quiet", "-m", "add initialized gitlink")
    pin = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    manifest = _manifest("example/repo", pin)

    artifact, sites = build_source_inventory(
        manifest,
        {"example/repo": root},
        cohort_manifest_sha256="d" * 64,
    )

    repo = artifact["repositories"][0]
    assert repo["status"] == "incomplete_submodules", repo.get("error")
    assert repo["submodules_excluded"] == [
        {"path": "deps/fake", "commit_oid": gitlink_oid}
    ]
    assert repo["site_count"] == 1
    assert len(sites) == 1
