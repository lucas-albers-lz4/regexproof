"""Counterexample finder for AutoAR's pinned script-src loopback fetch path."""

from __future__ import annotations

import json
import atexit
from pathlib import Path

from z3 import And, InRe, Length, Not, String, StringVal

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.autoar_jsendpoints_scope_replay import (
    origins_differ,
    run_collector,
    start_scope_fixture,
)
from regexproof.harness.core import prop

PIN = "01cd447ad3b1acfed7e0680596c2c74458a4cf06"
FAMILY = "AA-autoar-jsendpoints"
SITE = (
    f"h0tak88r/AutoAR@{PIN}:"
    "internal/scanner/jsendpoints/jsendpoints.go:22:scriptSrcRe"
)
QUESTION_ID = "AA-autoar-jsendpoint-loopback-script-src-fetch"
PATTERN = r'''<script[^>]+src\s*=\s*["']([^"'>\s]+)["']'''
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-autoar-jsendpoint-scope-escape-20r2"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))
_COMPILED = compile_pattern(
    PATTERN,
    flags="i",
    dialect="re2",
    call_kind="search",
    max_length=1024,
    domain="ascii",
)
if _COMPILED.mirror is None:
    raise RuntimeError(
        "AutoAR scriptSrcRe is not encodable: "
        f"{_COMPILED.unencodable_reason}"
    )
SCRIPT_SRC_SEARCH = _COMPILED.mirror

_ACTIVE_FIXTURE = None


def _fixture():
    global _ACTIVE_FIXTURE
    if _ACTIVE_FIXTURE is None:
        _ACTIVE_FIXTURE = start_scope_fixture()
    return _ACTIVE_FIXTURE


def _scope_violation_replays(witness: dict) -> bool:
    global _ACTIVE_FIXTURE
    fixture = _ACTIVE_FIXTURE
    if fixture is None:
        return False
    try:
        expected = {
            "document_html": fixture.external_html,
            "target_url": fixture.target_url,
            "target_origin": f"http://127.0.0.1:{fixture.target.server_port}",
            "script_url": fixture.canary_script_url,
            "script_origin": fixture.canary_origin,
        }
        if any(witness.get(name) != value for name, value in expected.items()):
            return False
        if not origins_differ(fixture.target_url, fixture.canary_script_url):
            return False
        response = run_collector(
            [{"hosts": [fixture.target_url], "threads": 1}]
        )
        result = response["results"][0]
        counts = fixture.counts_snapshot()
        return (
            counts.get("target /") == 1
            and counts.get("canary /bundle.js") == 1
            and any(
                endpoint.get("Path") == "/api/v1/users"
                and endpoint.get("Source") == fixture.canary_script_url
                for endpoint in result["endpoints"]
            )
        )
    except (OSError, RuntimeError, ValueError):
        return False
    finally:
        fixture.close()
        _ACTIVE_FIXTURE = None


@prop(
    QUESTION_ID,
    "COUNTEREXAMPLE FINDER: pinned scriptSrcRe accepts an absolute loopback "
    ".js URL from live-host HTML and the exact Go collector fetches it",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=PATTERN,
    pattern_flags="i",
    ground_truth=_scope_violation_replays,
    contract=CONTRACT,
)
def autoar_jsendpoint_loopback_script_src_fetch():
    fixture = _fixture()
    document_html = String("document_html")
    target_url = String("target_url")
    target_origin = String("target_origin")
    script_url = String("script_url")
    script_origin = String("script_origin")
    constraints = [
        document_html
        == StringVal(fixture.external_html),
        target_url == StringVal(fixture.target_url),
        target_origin
        == StringVal(f"http://127.0.0.1:{fixture.target.server_port}"),
        script_url == StringVal(fixture.canary_script_url),
        script_origin == StringVal(fixture.canary_origin),
        Length(document_html) <= 1024,
    ]
    bad = And(
        InRe(document_html, SCRIPT_SRC_SEARCH),
        target_origin != script_origin,
    )
    return constraints, bad


def cleanup_fixture() -> None:
    global _ACTIVE_FIXTURE
    if _ACTIVE_FIXTURE is not None:
        _ACTIVE_FIXTURE.close()
        _ACTIVE_FIXTURE = None


atexit.register(cleanup_fixture)


__all__ = ["CONTRACT", "FAMILY", "PIN", "QUESTION_ID", "SITE"]
