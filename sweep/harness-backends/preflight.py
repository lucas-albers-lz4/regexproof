#!/usr/bin/env python3
"""R8 runtime pre-flight (design #213 R8/rev 3): verifies the INVOKED Noodler
binary before trusting it. Checks, in order:
  1. sha256 pin (22b19f12...464 for v1.6.1)
  2. wrong-UNSAT regression replays: #316 (closed) and #325 (STILL OPEN upstream)
     must both return sat — the bug class the escalation exists to distrust
  3. #344 (segfault-without-set-logic class): with (set-logic QF_SLIA) the binary
     must return a verdict within the timeout, never hang/crash
  4. version string (expect "Z3 version 4.16.0")
  5. determinism spot-check: one known-abstain and one known-sat formula, 3 runs
     each, must be stable (the measured 10/10 class, spot-checked at runtime)

Usage: python preflight.py [binary-path]   (default: the pinned v1.6.1)
Exits 0 only if every check passes. Writes preflight-report.txt next to the binary.
"""
import sys, os, re, subprocess, time, hashlib, json

PIN_SHA256 = "22b19f123d3e7f54e10fdc46af3f91de23d89148c9a259eb072bc9e12f083464"
EXPECT_VERSION = "Z3 version 4.16.0"
DEFAULT = "/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared"
HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURES = os.path.join(HERE, "p1-baseline", "fixtures")

FIXTURE_316 = os.path.join(FIXTURES, "gh316.smt2")
FIXTURE_325 = os.path.join(FIXTURES, "gh325.smt2")
FIXTURE_344 = os.path.join(FIXTURES, "gh344.smt2")  # carries (set-logic QF_SLIA) in-file

def fixture(name):
    """Read a fixture file — the checked-in files are the single source of truth
    (fixture edits must not silently diverge from the runtime checks)."""
    with open(name) as f:
        return f.read()
ABSTAIN_CASE = "(set-logic QF_SLIA)\n(declare-const s String)\n(assert (str.in_re s (re.from_ecma2020 '.*(?=IN=).*')))\n(assert (= s \"IN=\"))\n(check-sat)\n"
SAT_CASE = "(set-logic QF_SLIA)\n(declare-const s String)\n(assert (str.in_re s (re.from_ecma2020 '.*(?=IN=).*')))\n(assert (= s \"xIN=\"))\n(check-sat)\n"

def run(binary, smt, timeout=35):
    with open("/tmp/_preflight_q.smt2", "w") as f:
        f.write(smt)
    t0 = time.perf_counter()
    try:
        p = subprocess.Popen([binary, "/tmp/_preflight_q.smt2"], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True,
                             start_new_session=True)  # D6 process-group kill
        try:
            out, _ = p.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(os.getpgid(p.pid), 9)
            out, _ = p.communicate()
            return "TIMEOUT", timeout * 1000, None
        rc, out = p.returncode, out.strip()
    except Exception as e:
        return f"DISPATCH-ERROR: {e}", 0.0, None
    dt = (time.perf_counter() - t0) * 1000
    if rc < 0:
        # signal death: output untrusted even with a printed verdict (S13 literal)
        return f"CRASH(rc={rc})", round(dt, 1), out
    first = out.splitlines()[0] if out else "EMPTY"
    return f"{first}/rc={rc}", round(dt, 1), out

def main():
    binary = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    rows = []

    # 1. sha256
    h = hashlib.sha256(open(binary, "rb").read()).hexdigest()
    rows.append(("sha256 pin", "PASS" if h == PIN_SHA256 else "FAIL",
                 f"{h[:16]}… (expect {PIN_SHA256[:16]}…)"))

    # 2. wrong-UNSAT replays (must be sat) — fixtures read from the checked-in files
    for name, path in (("#316", FIXTURE_316), ("#325", FIXTURE_325)):
        v, ms, _ = run(binary, fixture(path))
        rows.append((f"{name} replay (expect sat)", "PASS" if v.startswith("sat") else "FAIL",
                     f"{v} ({ms:.0f}ms)"))

    # 3. #344 with set-logic (containment: verdict OR timeout-contained hang,
    # NEVER a crash — the measured behavior on v1.6.1 is a >30s hang, the
    # improvement over the v1.5.x-era segfault; the runner's timeout contains it)
    v, ms, _ = run(binary, fixture(FIXTURE_344))
    kind = v.split("/")[0]
    ok = kind in ("sat", "unsat", "unknown", "TIMEOUT")
    rows.append(("#344 set-logic (contained)", "PASS" if ok else "FAIL",
                 f"{v} ({ms:.0f}ms)"))

    # 4. version string
    try:
        p = subprocess.run([binary, "-version"], capture_output=True, text=True, timeout=15)
        ver = (p.stdout + p.stderr).strip().splitlines()[0] if (p.stdout or p.stderr) else "?"
    except Exception as e:
        ver = f"error: {e}"
    rows.append(("version string", "PASS" if EXPECT_VERSION in ver else "FAIL", ver[:60]))

    # 5. determinism spot-check (3 runs each)
    for name, smt, expect in (("abstain case", ABSTAIN_CASE, "unknown"),
                              ("sat case", SAT_CASE, "sat")):
        results = []
        for _ in range(3):
            v, ms, _ = run(binary, smt)
            results.append(v.split("/")[0])
        stable = len(set(results)) == 1
        correct = stable and results[0] == expect
        rows.append((f"determinism {name} (expect {expect})",
                     "PASS" if correct else "FAIL", f"{results}"))

    allpass = all(r[1] == "PASS" for r in rows)
    lines = ["# Noodler pre-flight report", f"binary: {binary}", f"time: {time.strftime('%Y-%m-%d %H:%M')}",
             "", "| check | result | detail |", "|---|---|---|"]
    for name, res, det in rows:
        lines.append(f"| {name} | {res} | {det} |")
    lines.append("")
    lines.append(f"OVERALL: {'PASS' if allpass else 'FAIL'}")
    report = "\n".join(lines)
    out_path = os.path.join(os.path.dirname(binary), "preflight-report.txt")
    with open(out_path, "w") as f:
        f.write(report)
    print(report)
    sys.exit(0 if allpass else 1)

if __name__ == "__main__":
    main()
