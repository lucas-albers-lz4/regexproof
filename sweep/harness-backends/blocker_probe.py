#!/usr/bin/env python3
"""Blocker exit-criterion probe (design #213 §7 #2): NETFILTER_KV_GLUE through the
three branches. The load-bearing property: the MIRROR language ≡ the AS-WRITTEN
ECMA language (equivalence theorem, both directions) — if exact, any property
provable on the mirror holds for the as-written pattern.

  Branch A: mirror through stock z3 + cvc5 cross-check → cross-checked tier
  Branch B: from_ecma2020 (as-written, search-wrapped) → escalated-unconfirmed
  Branch C: neither decides → still-unknown

Writes sweep/harness-backends/p1-baseline/blocker-probe.json (the narrative report
blocker-probe.md is authored from the JSON).
"""
import sys, os, re, json, time, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "sweep", "harness-backends"))
import z3
from z3 import String, InRe, Concat, Star, Union, Range, Re, StringVal, Not
import ecma_pilot as ep  # mirror_re, ecma_pattern, PATTERNS, smt_string
from matrix_baseline import run_cvc5

NOODLER = os.environ.get("NOODLER", "/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared")
OUT = os.path.join(ROOT, "sweep", "harness-backends", "p1-baseline")

NAME = "NETFILTER_KV_GLUE"
PAT, FLAGS = next((p, f) for n, p, f in ep.PATTERNS if n == NAME)
MIRROR = ep.mirror_re(NAME, PAT, FLAGS)
ECMA = ep.ecma_pattern(NAME, PAT, FLAGS)  # .*(pattern).* wrapped

def ci_word_smt(w):
    return "(re.++ " + " ".join(
        f'(re.union (str.to_re "{c}") (str.to_re "{c.swapcase()}"))' for c in w) + ")"

def alt_smt(words):
    parts = [ci_word_smt(w) for w in words.split("|")]
    return parts[0] if len(parts) == 1 else "(re.union " + " ".join(parts) + ")"

def mirror_smt_text():
    """The mirror expression as SMT-LIB text, generated directly (z3's printer
    wraps shared subexpressions in multi-binding lets, which inlining would
    complicate). Mirror = .* [^\\s] (KEY) = .*"""
    any_r = '(re.* (re.range "\\u{0}" "\\u{7f}"))'
    ns = '(re.union (re.range "\\u{0}" "\\u{8}") (re.range "\\u{e}" "\\u{1f}") (re.range "!" "\\u{7f}"))'
    key = alt_smt(ep.KVS)
    return f'(re.++ {any_r} {ns} {key} (str.to_re "=") {any_r})'

def noodler_rule_diff(ecma_pat, direction):
    """One direction of the equivalence theorem in Noodler (both languages
    parseable there), RESTRICTED TO THE DECLARED ASCII DOMAIN (D14): s must be
    all-ASCII (the unconstrained theorem fails only on non-ASCII chars — measured
    witness: NUL NUL CODE= TAB U+0080, the trailing U+0080 outside \\x7f).
    Returns (verdict, ms)."""
    mir_expr = mirror_smt_text()
    ascii_dom = '(re.* (re.range "\\u{0}" "\\u{7f}"))'
    if direction == "M2E":
        # exists s in mirror but not in ecma
        body = ("(set-logic QF_SLIA)\n(declare-const s String)\n"
                f"(assert (str.in_re s {ascii_dom}))\n"
                f"(assert (str.in_re s {mir_expr}))\n"
                f"(assert (not (str.in_re s (re.from_ecma2020 '{ecma_pat}'))))\n"
                "(check-sat)\n")
    else:
        body = ("(set-logic QF_SLIA)\n(declare-const s String)\n"
                f"(assert (str.in_re s {ascii_dom}))\n"
                f"(assert (str.in_re s (re.from_ecma2020 '{ecma_pat}')))\n"
                f"(assert (not (str.in_re s {mir_expr})))\n"
                "(check-sat)\n")
    with tempfile.NamedTemporaryFile("w", suffix=".smt2", delete=False) as f:
        f.write(body)
        path = f.name
    try:
        t0 = time.perf_counter()
        p = subprocess.run([NOODLER, path], capture_output=True, text=True, timeout=60)
        dt = (time.perf_counter() - t0) * 1000
        first = p.stdout.strip().splitlines()[0] if p.stdout.strip() else "EMPTY"
        return f"{first}/rc={p.returncode}", round(dt, 1)
    finally:
        os.unlink(path)

def main():
    results = {"pattern": NAME, "ecma_wrapped": ECMA}
    print(f"--- {NAME} exit-criterion probe ---")

    # Branch B: from_ecma2020 decides the as-written language (nonemptiness + boundary)
    r = ep.noodler_ecma(ECMA, ["xIN=", "eth0IN=", "\tIN=", "a=bSRC="])
    results["branch_B_membership"] = {k: str(v) for k, v in r.items()}
    print("Branch B (from_ecma2020):", {k: str(v) for k, v in r.items()})

    # Equivalence theorem: both directions in Noodler
    m2e, m2e_ms = noodler_rule_diff(ECMA, "M2E")
    e2m, e2m_ms = noodler_rule_diff(ECMA, "E2M")
    results["theorem_M2E"] = m2e; results["theorem_M2E_ms"] = m2e_ms
    results["theorem_E2M"] = e2m; results["theorem_E2M_ms"] = e2m_ms
    print(f"Equivalence theorem: mirror→ecma diff: {m2e} ({m2e_ms}ms) | ecma→mirror diff: {e2m} ({e2m_ms}ms)")
    theorem = (m2e.startswith("unsat") and e2m.startswith("unsat"))
    results["equivalence_theorem"] = "HOLDS" if theorem else f"REFUTED ({m2e}, {e2m})"
    print("Theorem:", results["equivalence_theorem"])

    # Branch A: stock z3 + cvc5 decide the mirror language (nonemptiness + boundary)
    # nonemptiness: exists s in L_mirror
    s = String("s")
    sol = z3.Solver()
    sol.add(InRe(s, MIRROR))
    t0 = time.perf_counter(); ra = sol.check(); dt_a = (time.perf_counter() - t0) * 1000
    results["branch_A_stock_nonempty"] = str(ra)
    print(f"Branch A stock (nonemptiness): {ra} ({dt_a:.1f}ms)")
    # cvc5 cross-check on the same formula
    nonempty_smt = ("(set-logic QF_SLIA)\n(declare-const s String)\n"
                    f"(assert (str.in_re s {mirror_smt_text()}))\n(check-sat)\n")
    r_cvc, dt_cvc, note = run_cvc5(nonempty_smt, 30000)
    results["branch_A_cvc5_nonempty"] = r_cvc
    print(f"Branch A cvc5 (nonemptiness): {r_cvc} ({dt_cvc}ms) {note or ''}")

    # Branch A boundary decisions (stock + cvc5 on the mirror, 13-string set)
    bset = ["xIN=", "xIN=y", "x IN=", "\tIN=", "=IN=", "x\nIN=", "SPT=", "eth0IN=",
            "xSPT=", "a=bIN=", "IN=", " xIN=", "x\x00IN="]
    st = {}
    cvc = {}
    for st_ in bset:
        sol = z3.Solver()
        sol.add(InRe(s, MIRROR))
        sol.add(s == StringVal(st_))
        st[st_] = str(sol.check())
        bsm = ("(set-logic QF_SLIA)\n(declare-const s String)\n"
               f"(assert (str.in_re s {mirror_smt_text()}))\n"
               f"(assert (= s {ep.smt_string(st_)}))\n(check-sat)\n")
        r_c, _, _ = run_cvc5(bsm, 30000)
        cvc[st_] = r_c
    results["branch_A_boundary_stock"] = st
    results["branch_A_boundary_cvc5"] = cvc
    agree = all(st[k] == cvc[k] for k in bset if cvc[k] in ("sat", "unsat"))
    results["branch_A_boundary_agreement"] = agree
    print("Branch A stock (boundary):", st)
    print("Branch A cvc5  (boundary):", cvc)
    print("Boundary agreement:", agree)

    with open(os.path.join(OUT, "blocker-probe.json"), "w") as f:
        json.dump(results, f, indent=1, default=str)
    print(f"wrote {OUT}/blocker-probe.json")

if __name__ == "__main__":
    main()
