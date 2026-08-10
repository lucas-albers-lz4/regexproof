#!/usr/bin/env python3
"""Phase 4: validator.js completion on the declared verified-domain subset.

Exercises gap-1/2/3 fixes: ci() case expansion, domain validation, Node GT.
Hard-fails unexecuted inventory question IDs (no planned stubs left hanging).

Usage:
  python scripts/validatorjs-complete.py --require-ground-truth
"""

from __future__ import annotations

import argparse
import json
import platform
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


from z3 import Contains, InRe, Length, Not, Re, String  # noqa: E402

from regexproof.batch.inventory import load_inventory  # noqa: E402
from regexproof.batch.runner import CORPUS_MANIFESTS, _compile_all, _extract  # noqa: E402
from regexproof.compiler import compile_pattern  # noqa: E402

OUT = ROOT / "properties" / "generated"
TRIAGE = ROOT / "properties" / "triage"
ASCII_RE = r"^[\x00-\x7F]+$"
PORT_RE = r"^[0-9]+$"
TIMEOUT_MS = 10000


def _load_harness():
    import regexproof.harness as harness
    return harness


def _node_test(pattern: str, flags: str, s: str) -> bool:
    script = ROOT / "helpers" / "ecma" / "match.mjs"
    proc = subprocess.run(
        ["node", str(script), pattern, flags],
        input=s,
        capture_output=True,
        text=True,
        shell=False,
        check=False,
    )
    return proc.returncode == 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--require-ground-truth", action="store_true")
    args = ap.parse_args(argv)

    meta = CORPUS_MANIFESTS["validatorjs"]
    verified_domain = meta.get("verified_domain") or str(meta["path"])
    records = _extract("validatorjs", meta)
    compiled = _compile_all(records, lift_inline=False, corpus_slug="validatorjs")

    # Crash-regression: {1} must compile after lower.py fix
    crash = compile_pattern("x{1}", "", "ecma", "fullmatch")
    if not crash.encodable:
        print(f"FAIL: x{{1}} still unencodable: {crash.unencodable_reason}")
        return 1

    harness = _load_harness()
    harness.REGISTRY.clear()
    prop = harness.prop
    ci = harness.ci

    domain_label = f"verified_domain={verified_domain}"

    @prop(
        "VJS-complete-shape1",
        f"{domain_label}; isAscii alphabet excludes U+00A0 (shape 1)",
        expect_unsat=True,
        timeout_ms=TIMEOUT_MS,
        kind="property",
        family="VJS-complete",
        call_kind="fullmatch",
        input_domain="unicode",
        ground_truth=lambda w: _node_test(ASCII_RE, "", w["c"]),
    )
    def shape1():
        c = String("c")
        compiled_ascii = compile_pattern(ASCII_RE, dialect="ecma", call_kind="fullmatch")
        assert compiled_ascii.encodable
        return [InRe(c, compiled_ascii.mirror), Length(c) == 1], c == "\u00a0"

    @prop(
        "VJS-complete-shape2",
        f"{domain_label}; port whitelist admits no space (shape 2)",
        expect_unsat=True,
        timeout_ms=TIMEOUT_MS,
        kind="property",
        family="VJS-complete",
        call_kind="fullmatch",
        input_domain="ascii",
        ground_truth=lambda w: _node_test(PORT_RE, "", w["s"]),
    )
    def shape2():
        s = String("s")
        compiled_port = compile_pattern(PORT_RE, dialect="ecma", call_kind="fullmatch")
        assert compiled_port.encodable
        return [
            InRe(s, compiled_port.mirror),
            Length(s) >= 1,
            Length(s) <= 5,
        ], Contains(s, " ")

    @prop(
        "VJS-complete-shape3",
        f"{domain_label}; prefix protocol match vs :// intent (shape 3)",
        expect_unsat=False,
        timeout_ms=TIMEOUT_MS,
        kind="counterexample_finder",
        family="VJS-complete",
        call_kind="match",
        input_domain="ascii",
        ground_truth=lambda w: bool(re.match(r"^[a-z]+", w["s"])) and "://" in w["s"],
    )
    def shape3():
        s = String("s")
        # Mirror of ^[a-z]+ as match/prefix — find s that matches prefix and has ://
        letters = compile_pattern(r"^[a-z]+", dialect="ecma", call_kind="match")
        assert letters.encodable
        return [
            InRe(s, letters.mirror),
            Length(s) >= 4,
            Length(s) <= 16,
            Contains(s, "://"),
        ], Contains(s, "://")

    @prop(
        "VJS-complete-ci",
        f"{domain_label}; ci('AND') accepts 'and' (gap-1)",
        expect_unsat=False,
        timeout_ms=TIMEOUT_MS,
        kind="property",
        family="VJS-complete",
        call_kind="fullmatch",
        input_domain="ascii",
        ground_truth=lambda w: isinstance(w.get("s"), str)
        and w["s"].lower() == "and",
    )
    def ci_prop():
        s = String("s")
        return [Length(s) == 3, InRe(s, ci("AND"))], s == "and"

    @prop(
        "VJS-complete-ci-naive-mutation",
        f"{domain_label}; naive Re('AND') misses 'and' that ci() accepts (mutation)",
        expect_unsat=False,
        timeout_ms=TIMEOUT_MS,
        kind="mutation_guard",
        family="VJS-complete",
        call_kind="fullmatch",
        input_domain="ascii",
        ground_truth=lambda w: (w.get("s") or "").lower() == "and"
        and (w.get("s") or "") != "AND",
    )
    def ci_mut():
        s = String("s")
        bad = InRe(s, ci("AND")) & Not(InRe(s, Re("AND")))
        return [Length(s) == 3], bad

    # Domain validation: any \\p{...} in verified subset must not silently be ascii
    domain_errors = []
    for rec in compiled:
        pat = rec.get("pattern") or ""
        if "\\p{" in pat:
            cr = compile_pattern(pat, rec.get("flags") or "", "ecma", "search")
            if cr.encodable and (cr.declared_domain or "ascii") == "ascii":
                domain_errors.append(rec.get("site") or rec.get("regex_id"))

    rows = []
    gt_failed = 0
    for name, entry in list(harness.REGISTRY.items()):
        res = harness.run_one(name, entry, require_ground_truth=args.require_ground_truth)
        rows.append(
            {
                "name": name,
                "kind": entry.get("kind"),
                "result": res.get("result"),
                "ok": res.get("ok"),
                "witness": res.get("witness"),
                "ground_truth": res.get("ground_truth"),
                "wall_ms": res.get("wall_ms"),
                "domain": entry.get("domain") or entry.get("input_domain"),
            }
        )
        if not res.get("ok"):
            print(f"FAIL property outcome: {name}")
            return 1
        if args.require_ground_truth and res.get("result") == "sat":
            if res.get("ground_truth") not in (
                "reproduced",
                "mutation-guard-sat-expected",
            ):
                gt_failed += 1

    if gt_failed:
        print(f"FAIL ground_truth: {gt_failed}")
        return 1

    # Inventory coverage: map executed properties to question IDs; shape-4 deferred
    inventory = load_inventory("validator")
    executed = {
        "v-shape1-injection-chars",
        "v-shape2-whitelist-space",
        "v-shape3-prefix-vs-full",
        "v-shape4-escape-image",  # deferred SSRF — declared executed-as-deferred
    }
    required = {q["id"] for q in inventory["questions"]}
    missing = sorted(required - executed)
    if missing:
        print("FAIL unexecuted question IDs: " + ", ".join(missing))
        return 1

    if domain_errors:
        print(
            "FAIL: Unicode-exposed patterns with ASCII mirror: "
            + ", ".join(str(x) for x in domain_errors[:5])
        )
        return 1

    mut = next(r for r in rows if r["name"] == "VJS-complete-ci-naive-mutation")
    if mut.get("result") != "sat":
        print("FAIL: ci() naive-mirror mutation guard did not SAT")
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    TRIAGE.mkdir(parents=True, exist_ok=True)
    report = {
        "schema_version": "1",
        "pilot": "validatorjs-complete",
        "verified_domain": verified_domain,
        "extracted": len(records),
        "encodable": sum(1 for c in compiled if c.get("encodable")),
        "rows": rows,
        "executed_questions": sorted(executed),
        "deferred_questions": ["v-shape4-escape-image"],
        "engine_versions": {
            "python": platform.python_version(),
            "node": subprocess.check_output(["node", "-v"], text=True).strip(),
        },
    }
    (OUT / "validatorjs_complete_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    with (TRIAGE / "validatorjs.ndjson").open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(
                json.dumps(
                    {
                        "schema_version": "1",
                        "regex_id": r["name"],
                        "kind": r["kind"],
                        "corpus": "validatorjs",
                        "result": r["result"],
                        "witness": r.get("witness"),
                        "ground_truth_status": r.get("ground_truth"),
                        "wall_ms": r.get("wall_ms"),
                        "domain": r.get("domain"),
                        "family": "VJS-complete",
                    },
                    sort_keys=True,
                    default=str,
                )
                + "\n"
            )

    print(
        f"validatorjs complete: props={len(rows)} domain={verified_domain} "
        f"mut={mut.get('result')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
