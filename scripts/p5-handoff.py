#!/usr/bin/env python3
"""Phase 5 handoff pilot (P5/P7, #221 — U9-amended: mirror-route only).

1. **D14 fuzz suite**: real-JS-engine membership vs translated MIRROR over the
   pilot's probe corpus + the documented ASCII-domain boundary set (NBSP /
   U+2028 / é — the measured \\s gap marks the domain edge). Regression
   evidence only (finite probe sets cannot prove unbounded equivalence —
   design D14). Divergences INSIDE the declared ASCII domain are triage
   records; boundary probes are EXPECTED divergences, recorded as the
   documented domain edge.

2. **fwlive handoff (P7)**: the six fwlive patterns' MIRROR properties through
   the harness path (2 per pattern: one accept + one reject, each
   ground-truthed by Node). The p5-pilot.md contract: every result carries
   the property id, route, raw evidence, derived tier, and the destination
   mapping into the fwlive #120 pipeline.

3. **U9 reopen trigger evaluated**: the six-pattern inventory is unchanged —
   no new pattern → no reopen; recorded in the pilot.

Run: python scripts/p5-handoff.py   (needs node; NOODLER optional)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from z3 import InRe, String, StringVal, Solver, sat

sys.path.insert(0, str(Path(__file__).resolve().parents[0] / ".." /
                        "sweep" / "harness-backends"))

from ecma_pilot import PATTERNS, mirror_re, node_verdicts, probe_corpus

from regexproof.harness import core
from regexproof.harness.tiers import derive_tier

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "sweep" / "harness-backends"
PILOT_PATH = OUT / "p5-pilot.md"

# The documented ASCII-domain boundary probes (the measured \s gap: NBSP and
# U+2028 are \s in JS but NOT in the ASCII mirror classes). Composed with the
# pattern words so the gap is actually exercised.
BOUNDARY_PROBES = ["\xa0", "a\xa0b", "\u2028", "x\u2028", "é", "aéb",
                   " kernel\xa0", "SYN\xa0ACK", "eth0\xa0IN=",
                   "kernel\u2028", "SYN\u2028ACK", "dnsmasq\xa0",
                   "ACCEPT\xa0DENY"]


def mirror_membership(name, s):
    """Does the mirror accept s (search semantics)? Full-match membership."""
    u = String("u")
    sol = Solver()
    sol.add(InRe(u, mirror_re(name, None, None)))
    sol.add(u == StringVal(s))
    return sol.check() == sat


def d14_fuzz():
    """D14: real JS vs mirror membership over the corpus + boundary set.
    Returns (rows, divergences_in_domain, boundary_divergences)."""
    corpus = probe_corpus()
    rows = []
    in_domain = []
    boundary = []
    for name, pat, flags in PATTERNS:
        all_strs = corpus + BOUNDARY_PROBES
        verdicts = node_verdicts(pat, flags, all_strs)  # dict {s: bool}
        for s in all_strs:
            real = verdicts[s]
            mir = mirror_membership(name, s)
            if real != mir:
                if s in BOUNDARY_PROBES:
                    boundary.append((name, s, real, mir))
                else:
                    in_domain.append((name, s, real, mir))
        rows.append({"pattern": name, "corpus": len(corpus),
                     "probes": len(all_strs),
                     "in_domain_divergences": sum(
                         1 for (n, s, r, m) in in_domain if n == name),
                     "boundary_divergences": sum(
                         1 for (n, s, r, m) in boundary if n == name)})
    return rows, in_domain, boundary


# The fwlive handoff properties: per pattern, one ACCEPT + one REJECT case,
# each ground-truthed by the real engine (the #120 destination noted).
FW = [
    ("fwlive-NON_FIREWALL_PREFIX-accept", "NON_FIREWALL_PREFIX", "dnsmasq",
     True, "classify step 1: prefix gate (accept)"),
    ("fwlive-NON_FIREWALL_PREFIX-reject", "NON_FIREWALL_PREFIX", "xdnsmasq",
     False, "classify step 1: prefix gate (reject)"),
    ("fwlive-FIREWALL_HINT-accept", "FIREWALL_HINT", " kernel ", True,
     "classify step 2: hint gate (accept)"),
    ("fwlive-FIREWALL_HINT-reject", "FIREWALL_HINT", "xkernel", False,
     "classify step 2: hint gate (reject)"),
    ("fwlive-ACTION_RE-accept", "ACTION_RE", " ACCEPT ", True,
     "classify step 3: action gate (accept)"),
    ("fwlive-ACTION_RE-reject", "ACTION_RE", "xACCEPT", False,
     "classify step 3: action gate (reject)"),
    ("fwlive-DENY_ACTION-accept", "DENY_ACTION", " DROP ", True,
     "classify step 4: deny gate (accept)"),
    ("fwlive-DENY_ACTION-reject", "DENY_ACTION", "dropping", False,
     "classify step 4: deny gate (reject)"),
    ("fwlive-TCP_FLAG_TAIL-accept", "TCP_FLAG_TAIL", "SYN ACK FIN", True,
     "classify step 5: tcp-flag tail (accept)"),
    ("fwlive-TCP_FLAG_TAIL-reject", "TCP_FLAG_TAIL", "xSYNxACK", False,
     "classify step 5: tcp-flag tail (reject)"),
    ("fwlive-NETFILTER_KV_GLUE-accept", "NETFILTER_KV_GLUE", "eth0IN=", True,
     "classify step 6: kv glue (accept)"),
    ("fwlive-NETFILTER_KV_GLUE-reject", "NETFILTER_KV_GLUE", "eth0 IN=", False,
     "classify step 6: kv glue (reject)"),
]


def run_handoff():
    """Run the 12 mirror properties through the harness path. EVERY probe is
    ground-truthed by the real engine first (luna r1 on #236: ok=True must
    not just confirm Z3 agrees with a hardcoded expectation)."""
    records = []
    for pid, pat_name, probe, expect_accept, dest in FW:
        pat = next(p[1] for p in PATTERNS if p[0] == pat_name)
        flags = next(p[2] for p in PATTERNS if p[0] == pat_name)
        real = node_verdicts(pat, flags, [probe])[probe]
        if real != expect_accept:
            raise AssertionError(
                f"{pid}: real engine disagrees with the expectation — "
                f"probe {probe!r} real={real} expect_accept={expect_accept}")

        def _fn(pat_name=pat_name, probe=probe):
            u = String("u")
            return [InRe(u, mirror_re(pat_name, None, None))], \
                u == StringVal(probe)
        entry = {
            "fn": _fn, "domain": "ascii (fwlive log lines)", "expect_unsat":
            not expect_accept, "timeout_ms": 30000, "ground_truth": None,
            "kind": "property", "family": "fwlive", "input_domain": "ascii",
            "call_kind": None, "backend": "seq",
        }
        result = core.run_one(pid, entry)
        records.append({
            "property_id": pid,
            "pattern": pat_name,
            "probe": json.dumps(probe),
            "expect_accept": expect_accept,
            "real_engine_verdict": real,  # ground truth (node_verdicts)
            "route": "mirror",
            "raw_evidence": {
                "result": result["result"],
                "wall_ms": result["wall_ms"],
                "state": result.get("state"),
                "ok": result["ok"],
            },
            "derived_tier": derive_tier(result),
            "destination": dest,
            "destination_issue": "#120",
        })
    return records


def evaluate_reopen() -> bool:
    """The U9 reopen trigger (luna r1 on #236 — no hardcoding): a pattern in
    the current set that is NOT in the committed Phase-1 inventory (a NEW
    pattern) AND lacks a standard-encoding mirror reopens U9. The inventory is
    the committed ecma-pilot.json."""
    inventory = json.loads(
        (HERE / "sweep" / "harness-backends" / "p1-baseline" /
         "ecma-pilot.json").read_text()
    )
    known = {p["pattern"] for p in inventory}
    for name, _, _ in PATTERNS:
        if name not in known:
            try:
                mirror_re(name, None, None)
            except KeyError:
                return True  # new pattern WITHOUT a mirror → reopen
    return False


def render(rows, in_domain, boundary, handoff, reopen):
    lines = [
        "# Phase 5 handoff pilot (P5/P7, #221 — mirror-route, U9-amended)",
        "",
        "## D14 differential fuzz (real JS vs mirror, regression evidence)",
        "",
        "| pattern | corpus | probes | in-domain divergences | boundary divergences |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(f"| {r['pattern']} | {r['corpus']} | {r['probes']} | "
                     f"{r['in_domain_divergences']} | "
                     f"{r['boundary_divergences']} |")
    lines += [
        "",
        f"- total in-domain divergences: {len(in_domain)} "
        "(each would be a triage record; zero is the pass criterion)",
        f"- boundary divergences: {len(boundary)} — the documented ASCII-domain "
        "edge (NBSP/U+2028 \\s gap, measured Phase 1)",
        "",
        "## fwlive handoff (P7) — mirror properties through the harness",
        "",
        "| property | pattern | probe | expect | route | result | tier | destination |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for h in handoff:
        lines.append(
            f"| {h['property_id']} | {h['pattern']} | {h['probe']} | "
            f"{'accept' if h['expect_accept'] else 'reject'} | {h['route']} | "
            f"{h['raw_evidence']['result']} (ok={h['raw_evidence']['ok']}) | "
            f"{h['derived_tier']} | {h['destination']} → {h['destination_issue']} |"
        )
    lines += [
        "",
        "Every probe above is ground-truthed by the real JS engine "
        "(real_engine_verdict == expect — the run FAILS on disagreement).",
        "",
        "## U9 reopen trigger evaluation",
        "",
        f"- fwlive pattern inventory: {len(PATTERNS)} patterns compared against "
        "the committed Phase-1 inventory (ecma-pilot.json); no new pattern "
        "lacking a standard-encoding mirror",
        f"- reopen trigger: {'HIT — U9 reopened on #213' if reopen else 'NOT hit — the DROP decision stands'}",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    rows, in_domain, boundary = d14_fuzz()
    handoff = run_handoff()
    reopen = evaluate_reopen()  # inventory comparison — never hardcoded
    report = render(rows, in_domain, boundary, handoff, reopen)
    PILOT_PATH.write_text(report)
    print(report)
    print(f"\nwrote {PILOT_PATH}")
    # D14 pass criterion: zero in-domain divergences
    if in_domain:
        print(f"FAIL: {len(in_domain)} in-domain divergences need triage "
              "records", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
