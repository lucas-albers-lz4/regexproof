#!/usr/bin/env python3
"""P1 baseline matrix (design #213 §8 P1 / R1): full property registry through
stock z3 5.0.0 and the pinned Noodler v1.6.1 CLI, with timing, witnesses, and
cvc5 surface. D6-correct invocation: (set-logic QF_SLIA) first, (check-sat)
appended, model=true positional, process timeout.

Writes sweep/harness-backends/p1-baseline/matrix.json + MATRIX.md.
Noodler binary path via NOODLER env (default /tmp/noodler/...); the sha256 pin is
documented in PIN.md. Origin/main must be checked out; properties load from
regexproof.harness.properties.
"""
import sys, time, subprocess, os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import z3
from z3 import String, StringVal, Contains, InRe, Length, Concat, Star, Union, Range, Re
from regexproof.harness.properties import REGISTRY

NOODLER = os.environ.get("NOODLER", "/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared")
OUT = os.path.join(ROOT, "sweep", "harness-backends", "p1-baseline")
os.makedirs(OUT, exist_ok=True)

def build_extra(which):
    """The two documented seq-timeout forms (fact 17), not in the registry."""
    if which == "P2-len64":
        a = String("a")
        ACTOR_CLS = Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("."), Re("_"), Re("@"), Re("-"))
        wl_re = Concat(ACTOR_CLS, Star(ACTOR_CLS))
        return [InRe(a, wl_re), Length(a) >= 1, Length(a) <= 64], Contains(a, StringVal(" ")), 30000, "P2 whitelist len<=64 (seq timeout class)"
    if which == "P4-monolithic":
        v = String("v")
        ESCAPE_SAFE = Union(Range("\x20", "\x21"), Range("\x23", "\x5b"), Range("\x5d", "\x7e"))
        ESCAPE_ESC = Union(Re("\\\\"), Re('\\"'), Re("\\t"), Re("\\r"), Re("\\n"))
        ESCAPE_TOKENS = Union(ESCAPE_SAFE, ESCAPE_ESC)
        return [InRe(v, Star(ESCAPE_TOKENS)), Length(v) >= 1], Contains(v, StringVal("\t")), 30000, "P4 monolithic image (seq timeout class)"
    raise KeyError(which)

def smt_dump(constraints, goal):
    s = z3.Solver()
    s.add(constraints)
    s.add(goal)
    return "(set-logic QF_SLIA)\n" + s.sexpr() + "\n(check-sat)\n"

def witness_stock(s, r):
    if r != z3.sat:
        return None
    m = s.model()
    w = {}
    for d in m.decls():
        v = m[d]
        try:
            if v.sort() == z3.StringVal("").sort():
                w[d.name()] = v.as_string()
        except Exception:
            pass
    return w

def scan_smt_string(text, i):
    """SMT-LIB string scanner: quote-doubling, literal backslash, Z3 \\xHH/\\u{}/short escapes."""
    out = []
    i += 1
    while i < len(text):
        c = text[i]
        if c == '"':
            if i + 1 < len(text) and text[i + 1] == '"':
                out.append('"'); i += 2; continue
            return "".join(out), i + 1
        if c == "\\" and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt == "x":
                out.append(chr(int(text[i+2:i+4], 16))); i += 4; continue
            if nxt == "u":
                j = text.index("}", i + 2)
                out.append(chr(int(text[i+3:j], 16))); i = j + 1; continue
            if nxt in "ntr":
                out.append({"n": "\n", "t": "\t", "r": "\r"}[nxt]); i += 2; continue
            out.append("\\"); i += 1; continue
        out.append(c); i += 1
    return "".join(out), i

def parse_noodler_model(out):
    """Noodler CLI prints models WITHOUT a (model ...) wrapper — the define-fun
    list starts directly after the verdict. Scan each string value directly."""
    w = {}
    for dm in re.finditer(r"\(define-fun\s+(\S+)\s*\(\)\s*String\s*\"", out):
        val, _ = scan_smt_string(out, dm.end() - 1)
        w[dm.group(1)] = val
    return w or None

def run_stock(constraints, goal, timeout_ms):
    s = z3.Solver()
    s.set(timeout=timeout_ms)
    s.add(constraints)
    s.add(goal)
    t0 = time.perf_counter()
    r = s.check()
    dt = (time.perf_counter() - t0) * 1000
    return str(r), dt, witness_stock(s, r)

def run_noodler(smt, timeout_ms):
    fn = os.path.join(OUT, "_q.smt2")
    with open(fn, "w") as f:
        f.write(smt + "(get-model)\n")
    t0 = time.perf_counter()
    try:
        p = subprocess.run([NOODLER, "model=true", fn], capture_output=True,
                           text=True, timeout=timeout_ms / 1000 + 5)
        rc, out = p.returncode, p.stdout.strip()
    except subprocess.TimeoutExpired:
        return "TIMEOUT", timeout_ms, None, None
    dt = (time.perf_counter() - t0) * 1000
    lines = [ln for ln in out.splitlines() if ln.strip() in ("sat", "unsat", "unknown")]
    verdict = lines[0] if lines else ("?" if out else "NO-VERDICT")
    wit = parse_noodler_model(out) if verdict == "sat" else None
    return verdict, dt, wit, rc

def run_cvc5(smt, timeout_ms):
    """cvc5 1.3.4 via subprocess worker (D2 per-query isolation — the in-process
    C++ lib segfaulted on re.loop text during the first baseline run, killing the
    whole process; the worker contains the crash). SKIP when cvc5 is unavailable."""
    worker = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cvc5_worker.py")
    fn = os.path.join(OUT, "_cvc5_q.smt2")
    with open(fn, "w") as f:
        f.write(smt)
    t0 = time.perf_counter()
    try:
        p = subprocess.run([sys.executable, worker, fn, str(timeout_ms)],
                           capture_output=True, text=True, timeout=timeout_ms / 1000 + 10)
        dt = (time.perf_counter() - t0) * 1000
        line = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else "?"
        if line.startswith("V "):
            verdict, ms = line[2:].split()
            return verdict, float(ms), None
        if line.startswith("E "):
            return "PARSE-ERROR", 0.0, line[2:][:80]
        return "?", 0.0, line[:80]
    except subprocess.TimeoutExpired:
        return "TIMEOUT", timeout_ms, None
    except Exception as e:
        return "DISPATCH-ERROR", 0.0, str(e)[:80]

def reloop_form():
    """S11: P2-actor-whitelist escalation form via (re.loop wl 17 64). Hand-written
    SMT text (z3py has no ReLoop in 5.0.0)."""
    return """(set-logic QF_SLIA)
(declare-const a String)
(define-fun wl () RegLan (re.union (re.range "a" "z") (re.range "A" "Z") (re.range "0" "9") (str.to_re ".") (str.to_re "_") (str.to_re "@") (str.to_re "-")))
(assert (str.in_re a (re.loop wl 17 64)))
(assert (str.contains a " "))
(check-sat)
"""

def main():
    names = sorted(REGISTRY.keys()) + ["P2-len64", "P4-monolithic"]
    rows = []
    for name in names:
        if name in REGISTRY:
            e = REGISTRY[name]
            constraints, goal = e["fn"]()
            timeout_ms = e.get("timeout_ms", 30000)
            note = e.get("domain", "")[:50]
        else:
            constraints, goal, timeout_ms, note = build_extra(name)
        smt = smt_dump(constraints, goal)
        r_stock, dt_stock, w_stock = run_stock(constraints, goal, timeout_ms)
        r_ndl, dt_ndl, w_ndl, rc_ndl = run_noodler(smt, timeout_ms)
        r_cvc, dt_cvc, cvc_note = run_cvc5(smt, timeout_ms)
        wmatch = "n/a"
        if r_stock == "sat" and r_ndl == "sat" and w_stock is not None and w_ndl is not None:
            wmatch = "MATCH" if w_stock == w_ndl else f"DIFF"
        rows.append({"property": name, "note": note, "stock": r_stock, "stock_ms": round(dt_stock, 1),
                     "noodler": r_ndl, "noodler_ms": round(dt_ndl, 1), "noodler_rc": rc_ndl,
                     "cvc5": r_cvc, "cvc5_ms": round(dt_cvc, 1), "cvc5_note": cvc_note,
                     "witness_match": wmatch,
                     "stock_witness": w_stock, "noodler_witness": w_ndl})
        print(f"{name:28s} {r_stock:8s} {dt_stock:8.1f} {r_ndl:8s} {dt_ndl:7.1f} {r_cvc:12s} {wmatch}")
    # S11 re.loop escalation form
    smt_rl = reloop_form()
    r_ndl, dt_ndl, w_ndl, rc = run_noodler(smt_rl, 30000)
    r_cvc, dt_cvc, cvc_note = run_cvc5(smt_rl, 30000)
    rows.append({"property": "P2-len64-reloop-17-64 (S11)", "note": "re.loop escalation form",
                 "stock": "n/a (z3py no ReLoop)", "stock_ms": 0, "noodler": r_ndl,
                 "noodler_ms": round(dt_ndl, 1), "noodler_rc": rc, "cvc5": r_cvc,
                 "cvc5_ms": round(dt_cvc, 1), "cvc5_note": cvc_note, "witness_match": "n/a",
                 "stock_witness": None, "noodler_witness": w_ndl})
    print(f"{'P2-len64-reloop-17-64':28s} {'n/a':8s} {0.0:8.1f} {r_ndl:8s} {dt_ndl:7.1f} {r_cvc:12s} {cvc_note}")
    with open(os.path.join(OUT, "matrix.json"), "w") as f:
        json.dump(rows, f, indent=1, default=str)
    with open(os.path.join(OUT, "MATRIX.md"), "w") as f:
        f.write("# P1 baseline matrix (2026-08-11)\n\n")
        f.write("| property | stock | ms | noodler | ms | cvc5 | witness |\n|---|---|---|---|---|---|---|\n")
        for r in rows:
            f.write(f"| {r['property']} | {r['stock']} | {r['stock_ms']} | {r['noodler']} | {r['noodler_ms']} | {r['cvc5']} | {r['witness_match']} |\n")
    print(f"wrote {OUT}/matrix.json + MATRIX.md ({len(rows)} rows)")

if __name__ == "__main__":
    main()
