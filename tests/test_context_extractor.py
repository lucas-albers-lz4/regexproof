"""Review-form validation checks context consistency, not human adoption."""

import json
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
CLI = ROOT / "scripts" / "context-extractor.py"


def _run(*args):
    return subprocess.run([sys.executable, str(CLI), *map(str, args)],
                          capture_output=True, text=True)


def _form(tmp_path, total=200, target=100):
    tree = tmp_path / "checkout"
    tree.mkdir()
    (tree / "app.sh").write_text(
        "\n".join(f"line {i}" for i in range(1, total + 1)), encoding="utf-8"
    )
    path = tmp_path / "form.json"
    result = _run("--corpus", "demo", "--checkout", tree,
                  "--site", f"app.sh:{target}:token", "--review-form", "-o", path)
    assert result.returncode == 0, result.stderr
    form = json.loads(path.read_text(encoding="utf-8"))
    form.update(witness_reachability="reachable", evidence_ref="extracted window",
                input_format_constraint="NUL-free input")
    return path, form


def _validate(path, form):
    path.write_text(json.dumps(form), encoding="utf-8")
    return _run("--validate", path)


@pytest.mark.parametrize("mutation", [
    "count", "oversized", "start", "end", "site", "duplicate", "reordered",
    "missing_text", "nontext", "missing_flag", "wrong_flag", "nonbool_flag",
])
def test_rejects_inconsistent_context(tmp_path, mutation):
    path, form = _form(tmp_path)
    window = form["window"]
    if mutation == "count":
        window["window_lines"] += 1
    elif mutation == "oversized":
        # Keep every other invariant valid, isolating the hard size cap.
        window.update(window_start=25, window_end=175, window_lines=151)
        window["lines"] = [
            {"line": i, "text": f"line {i}", "is_target": i == 100}
            for i in range(25, 176)
        ]
    elif mutation == "start":
        window["window_start"] = True
    elif mutation == "end":
        window["window_end"] += 1
    elif mutation == "site":
        form["site"] = "app.sh:101:token"
    elif mutation == "duplicate":
        window["lines"][0] = window["lines"][1].copy()
    elif mutation == "reordered":
        window["lines"].reverse()
    elif mutation == "missing_text":
        del window["lines"][0]["text"]
    elif mutation == "nontext":
        window["lines"][0]["text"] = None
    elif mutation == "missing_flag":
        del window["lines"][0]["is_target"]
    elif mutation == "wrong_flag":
        window["lines"][0]["is_target"] = True
    elif mutation == "nonbool_flag":
        window["lines"][0]["is_target"] = 0
    result = _validate(path, form)
    assert result.returncode != 0, f"accepted inconsistent {mutation} context"
    assert "error:" in result.stderr
    assert "Traceback" not in result.stderr
    assert not result.stdout  # no derived queue action emitted


@pytest.mark.parametrize("site_path,window_path", [
    ("other.sh", "app.sh"),
    ("app.sh", "other.sh"),
    ("src/app.sh", "app.sh"),
])
def test_rejects_site_window_path_mismatch(tmp_path, site_path, window_path):
    path, form = _form(tmp_path)
    form["site"] = f"{site_path}:100:token"
    form["window"]["path"] = window_path
    result = _validate(path, form)
    assert result.returncode != 0
    assert "site path must match window.path" in result.stderr
    assert "Traceback" not in result.stderr
    assert not result.stdout


@pytest.mark.parametrize("site_path,window_path", [
    ("./app.sh", "app.sh"),
    ("app.sh", "./app.sh"),
    ("./src//./app.sh", "src/app.sh"),
    ("src/app.sh", "./src//./app.sh"),
])
def test_accepts_equivalent_relative_paths(tmp_path, site_path, window_path):
    path, form = _form(tmp_path)
    form["site"] = f"{site_path}:100:token"
    form["window"]["path"] = window_path
    result = _validate(path, form)
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["queue_action"] == "contractable"


@pytest.mark.parametrize("field", ["site", "window", "both"])
@pytest.mark.parametrize("invalid_path", [
    "", ".", "/app.sh", "//app.sh", "../app.sh", "src/../app.sh",
    "app.sh\x00",
])
def test_rejects_unsafe_paths_even_when_identical(tmp_path, field, invalid_path):
    path, form = _form(tmp_path)
    # Check each side independently, as well as identically invalid paths.
    form["site"] = f"{invalid_path}:100:token"
    form["window"]["path"] = invalid_path
    if field == "site":
        form["window"]["path"] = "app.sh"
    elif field == "window":
        form["site"] = "app.sh:100:token"
    result = _validate(path, form)
    assert result.returncode != 0
    assert "error:" in result.stderr
    assert "Traceback" not in result.stderr
    assert not result.stdout


@pytest.mark.parametrize("invalid_path", [None, 42, [], {}])
def test_rejects_nonstring_window_path(tmp_path, invalid_path):
    path, form = _form(tmp_path)
    form["window"]["path"] = invalid_path
    result = _validate(path, form)
    assert result.returncode != 0
    assert "error:" in result.stderr
    assert "Traceback" not in result.stderr
    assert not result.stdout


@pytest.mark.parametrize("total,target", [(200, 100), (200, 1), (200, 200), (3, 2)])
@pytest.mark.parametrize("reachability,action", [
    ("reachable", "contractable"), ("unreachable", "skipped_unreachable"),
    ("unverified", "claimed"),
])
def test_generated_windows_validate_without_changing_queue_semantics(
    tmp_path, total, target, reachability, action
):
    path, form = _form(tmp_path, total, target)
    form["witness_reachability"] = reachability
    result = _validate(path, form)
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["queue_action"] == action


def test_pinned_review_form_binds_window_to_commit_and_source_bytes(tmp_path):
    tree = tmp_path / "pinned"
    tree.mkdir()
    source = tree / "app.sh"
    source.write_text("validate() { echo ok; }\n")
    subprocess.run(["git", "init", "-q"], cwd=tree, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=tree, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=tree, check=True)
    subprocess.run(["git", "add", "app.sh"], cwd=tree, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "fixture"], cwd=tree, check=True)
    pin = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=tree, check=True,
        capture_output=True, text=True,
    ).stdout.strip()
    form_path = tmp_path / "pinned-form.json"
    result = _run(
        "--corpus", "demo", "--checkout", tree,
        "--site", "app.sh:1:validate", "--review-form",
        "--repository-url", "https://github.com/example/demo", "--pin", pin,
        "--input-format-constraint", "one shell function call",
        "-o", form_path,
    )
    assert result.returncode == 0, result.stderr
    form = json.loads(form_path.read_text())
    form.update(witness_reachability="reachable", evidence_ref="caller and sink")
    form_path.write_text(json.dumps(form))
    valid = _run("--validate", form_path, "--checkout", tree)
    assert valid.returncode == 0, valid.stderr
    assert json.loads(valid.stdout)["source_binding"]["pin"] == pin

    form["source_binding"]["sha256"] = "0" * 64
    form_path.write_text(json.dumps(form))
    tampered = _run("--validate", form_path, "--checkout", tree)
    assert tampered.returncode != 0
    assert "source_binding" in tampered.stderr

    source.write_text("validate() { echo changed; }\n")
    changed = _run("--validate", form_path, "--checkout", tree)
    assert changed.returncode != 0
    assert "differ from the pinned commit" in changed.stderr
