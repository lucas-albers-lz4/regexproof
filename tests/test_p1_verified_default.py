"""P1 (#425) verified-by-default gates — --require-domain gate-fires fixtures.

Covers the A acceptance:
- proof job (harness CLI): a fixture property with no ``input_domain`` makes
  ``--require-domain`` fail (and the flag is the only thing that flips it).
- ``pilot-properties.py`` (golden job): the same fixture fails its
  ``--require-domain`` invocation before any solve runs.
- ``rule-diff-pilot.py``: accepts the flag; the check is INERT for
  ``rule_diff`` kinds (``check_domain_coverage`` covers ``property`` +
  ``counterexample_finder`` only).
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

from z3 import Contains, InRe, Range, Star, String, StringVal

from regexproof.harness import core
from regexproof.harness.cli import main

ROOT = Path(__file__).resolve().parents[1]

FIXTURE_FAMILY = "p1-fixture"


def _fixture_prop(name: str = "p1-fixture-undeclared-domain") -> dict:
    """A property-kind entry with input_domain=None (the legacy default).

    Never satisfiable (no 'x' in [a-z]*), so only the domain gate can fail it.
    """
    def _fn():
        u = String("u")
        return [InRe(u, Star(Range("a", "z")))], Contains(u, StringVal("x"))

    return {
        "fn": _fn,
        "domain": "t",
        "expect_unsat": True,
        "timeout_ms": 30000,
        "ground_truth": None,
        "kind": "property",
        "family": FIXTURE_FAMILY,
        "input_domain": None,
        "call_kind": None,
        "backend": "seq",
    }


def _register_fixture(monkeypatch=None):
    name = "p1-fixture-undeclared-domain"
    core.REGISTRY[name] = _fixture_prop(name)
    # The fixture family needs a mutation guard so check_mutation_coverage
    # stays silent during the run (same pattern as tests/test_ci_contracts.py).
    core.REGISTRY["p1-fixture-mut"] = {
        **_fixture_prop("p1-fixture-mut"),
        "kind": "mutation_guard",
        "expect_unsat": False,
    }
    return name


def _unregister_fixture(name):
    core.REGISTRY.pop(name, None)
    core.REGISTRY.pop("p1-fixture-mut", None)


def test_require_domain_fails_on_undeclared_fixture():
    """Gate fires: the proof job invocation --require-domain exits 1 when a
    property declares no input_domain; without the flag it still passes."""
    name = _register_fixture()
    try:
        assert main(["--require-domain", name]) == 1
        assert main([name]) == 0  # legacy default unchanged without the flag
    finally:
        _unregister_fixture(name)


def test_require_domain_coverage_full_registry():
    """Precondition for landing the flag: every property/counterexample_finder
    in the canonical registry declares input_domain (the 5 P1 additions:
    P2-actor-whitelist, P3-sed-capture-truncation, P4-escape-image-tab/
    newline/del)."""
    assert core.check_domain_coverage(require=True) == 0


def test_domain_coverage_only_inspects_property_kinds():
    """The rule-diff-pilot inert claim: rule_diff and mutation_guard entries
    with no input_domain are not inspected by check_domain_coverage."""
    names = []
    for kind, expect in (("rule_diff", False), ("mutation_guard", False)):
        e = _fixture_prop(f"p1-fixture-{kind}")
        e["kind"] = kind
        e["expect_unsat"] = expect
        core.REGISTRY[f"p1-fixture-{kind}"] = e
        names.append(f"p1-fixture-{kind}")
    try:
        assert core.check_domain_coverage(require=True) == 0
    finally:
        for n in names:
            core.REGISTRY.pop(n, None)


def _load_pilot_properties():
    path = ROOT / "scripts" / "pilot-properties.py"
    spec = importlib.util.spec_from_file_location("pilot_properties_under_test", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_pilot_properties_require_domain_gate_fires():
    """Golden job: pilot-properties.py --require-domain fails fast when a
    registered property has no input_domain (before any solver work)."""
    mod = _load_pilot_properties()
    name = _register_fixture()
    try:
        assert mod.main(["--require-domain"]) == 1
        assert mod.main([]) == 0  # legacy default unchanged without the flag
    finally:
        _unregister_fixture(name)


def test_rule_diff_pilot_accepts_flag_and_is_inert():
    """rule-diff-pilot.py parses --require-domain and documents it as inert
    (its registry holds rule_diff gaps + mutation guards only)."""
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "rule-diff-pilot.py"), "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "--require-domain" in proc.stdout
    assert "INERT" in proc.stdout
    src = (ROOT / "scripts" / "rule-diff-pilot.py").read_text(encoding="utf-8")
    assert "check_domain_coverage(require=args.require_domain)" in src
    assert "INERT" in src
    assert "property" in src and "counterexample_finder" in src
