"""dogfood_shell conversion-wave harness family + ledger join (funnel #615)."""

from __future__ import annotations

import json
import random
import re
import shutil
import string
import subprocess
from pathlib import Path

import jsonschema
import pytest

from regexproof.harness.contract import product_reportable
from regexproof.harness.core import REGISTRY, check_mutation_coverage, run_one
import regexproof.harness.dogfood_shell as df  # noqa: F401 — register family
from regexproof.harness.dogfood_shell import (
    FAMILY,
    SED_SCRIPT,
    normalize_mirror,
)
from regexproof.schemas import load_schema

ROOT = Path(__file__).resolve().parents[1]
PRODUCT_NAMES = (
    "DF-dogfood-shell-normalize-fixpoint",
    "DF-dogfood-shell-normalize-idempotent",
)
GUARD_NAMES = (
    "DF-dogfood-shell-normalize-mutated-colon",
    "DF-dogfood-shell-normalize-mutated-once",
)
FWLIVE_FUNC = (
    "/root/workspace/fwlive/openwrt-feed/luci-app-fwlive"
    "/root/usr/libexec/rpcd/fwlive"
)
# Vendored bytes (CI has no dogfood checkouts). The drift assert below keeps
# the fixture pinned to the live file wherever the checkout exists.
FIXTURE = ROOT / "tests" / "fixtures" / "fwlive-normalize_log_prefix.sh"


def test_df_family_in_registry_and_mutation_coverage():
    assert any(e.get("family") == FAMILY for e in REGISTRY.values())
    for name in PRODUCT_NAMES:
        assert name in REGISTRY
        assert REGISTRY[name]["family"] == FAMILY
        assert product_reportable(REGISTRY[name]) is True
    for name in GUARD_NAMES:
        assert REGISTRY[name]["family"] == FAMILY
        assert REGISTRY[name]["kind"] == "mutation_guard"
        assert product_reportable(REGISTRY[name]) is False
    assert check_mutation_coverage() == 0


def test_df_contracts_validate_schema():
    schema = load_schema("property_contract.schema.json")
    for name in PRODUCT_NAMES:
        contract = REGISTRY[name]["contract"]
        jsonschema.validate(instance=contract, schema=schema)
        assert contract["provenance"] == "human"
        assert "normalize_log_prefix" in contract["site"]


def test_df_properties_hold_and_guards_fire():
    for name in PRODUCT_NAMES:
        res = run_one(name, REGISTRY[name])
        assert res["result"] == "unsat", res
        assert res["ok"] is True
    for name in GUARD_NAMES:
        res = run_one(name, REGISTRY[name])
        assert res["result"] == "sat", res
        assert res["ok"] is True
        # Non-vacuous witness: must carry a strip-class char (the empty
        # string proves nothing — SuffixOf("", c) is always False).
        wit = res["witness"]["x"]
        assert wit != "", name


def _sed(engine: str, script: str, stream: str) -> str:
    cmd = [engine, "sed", script] if engine == "busybox" else ["sed", script]
    proc = subprocess.run(
        cmd,
        input=stream.encode("utf-8"),
        capture_output=True,
        timeout=30,
        check=False,
    )
    assert proc.returncode == 0
    out = proc.stdout.decode("utf-8")
    return out[:-1] if out.endswith("\n") else out


def test_df_mirror_agrees_with_sed():
    # GNU sed is always present; the BusyBox half degrades to skip on
    # minimal images without busybox (CI installs it; the CI checker
    # hard-fails there instead).
    engines = ["sed"] + (["busybox"] if shutil.which("busybox") else [])
    if engines == ["sed"]:
        pytest.skip("busybox absent — GNU half only")
    rng = random.Random(615)
    alphabet = string.ascii_letters + string.digits + " \t:.-_/" + "\r\x0c\x0b"
    for engine in engines:
        for _ in range(100):
            s = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 12)))
            assert _sed(engine, SED_SCRIPT, s) == normalize_mirror(s), s


def _extract_shipped_function() -> str:
    text = FIXTURE.read_text(encoding="utf-8")
    m = re.search(r"^normalize_log_prefix\(\) \{\n(?:.*\n)*?^\}", text, re.M)
    assert m is not None, "fixture carries no normalize_log_prefix"
    body = m.group(0)
    assert "s/[[:space:]:]*$//" in body, "fixture script drifted"
    assert SED_SCRIPT in body, "harness SED_SCRIPT drifted from fixture"
    live = Path(FWLIVE_FUNC)
    try:
        live_present = live.is_file()
    except OSError:
        # CI runners have an unreadable /root (EACCES, not ENOENT) —
        # absence of the checkout is absence, never a failure.
        live_present = False
    if live_present:
        # The checkout exists (local dev): the fixture must equal the live
        # bytes, or the pin is stale — refresh the fixture, do not weaken
        # this assert.
        live_text = live.read_text(encoding="utf-8")
        lm = re.search(r"^normalize_log_prefix\(\) \{\n(?:.*\n)*?^\}", live_text, re.M)
        assert lm is not None, "live normalize_log_prefix not found"
        assert lm.group(0) == body, (
            "fixture drifted from live fwlive HEAD — refresh "
            "tests/fixtures/fwlive-normalize_log_prefix.sh"
        )
    return body


def test_df_shipped_function_replays_under_dash():
    # Ground-truth: the EXACT shipped bytes (extracted, never retyped)
    # evaluated under dash — idempotency on the #250 drift input.
    if not shutil.which("dash"):
        pytest.skip("dash absent")
    func = _extract_shipped_function()
    script = (
        func
        + '\nnormalize_log_prefix "$1"; echo\n'
        + 'normalize_log_prefix "$(normalize_log_prefix "$1")"; echo\n'
    )
    proc = subprocess.run(
        ["dash", "-c", script, "dash", "zz::"],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    once, twice = proc.stdout.splitlines()
    assert once == "zz"
    assert twice == once, "shipped function is not idempotent"


def test_df_guard_witness_replays_as_real_regression():
    # The mutation-guard witness must be a REAL bug witness for weakened
    # code: weakened sed leaves the colon standing.
    res = run_one(GUARD_NAMES[0], REGISTRY[GUARD_NAMES[0]])
    wit = res["witness"]["x"]
    assert _sed("sed", "s/[[:space:]]*$//", wit).endswith(":")
    assert _sed("sed", SED_SCRIPT, wit) == normalize_mirror(wit)


def test_proof_job_runs_busybox_dogfood_shell_checker():
    yml = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "ci-check-busybox-dogfood-shell.py" in yml
    assert "BusyBox dogfood_shell normalize replay" in yml
    proof = yml.split("name: Z3 proof harness", 1)[1].split("golden:", 1)[0]
    assert "--require-contract" in proof
    assert "--require-ground-truth" in proof


def test_committed_conversion_ndjson_matches_registry():
    path = ROOT / "properties" / "generated" / "dogfood_shell_conversion.ndjson"
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert len(rows) == len(PRODUCT_NAMES)
    assert {r["name"] for r in rows} == set(PRODUCT_NAMES)
    for row in rows:
        assert row["family"] == FAMILY
        assert row["corpus"] == "dogfood_shell"
        assert row["product_reportable"] is True
        assert row["idiom_bucket"] == "normalize-fixpoint"
        assert row["wave_id"] == "dogfood_shell_w1"
