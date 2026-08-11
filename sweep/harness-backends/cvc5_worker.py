#!/usr/bin/env python3
"""cvc5 per-query worker (D2 process isolation). Usage:
    python cvc5_worker.py <smt-file> <timeout-ms>
Prints one line: "V <sat|unsat|unknown> <ms>" or "E <parse-error-text>".
A segfault in the cvc5 C++ library kills only this process, never the caller.
"""
import sys, time

def main():
    fn, timeout_ms = sys.argv[1], int(sys.argv[2])
    smt = open(fn).read()
    try:
        import cvc5
    except ImportError:
        print("E cvc5 not importable (need the cvc5 venv on PYTHONPATH; Phase 4 installs it)")
        return
    solver = cvc5.Solver()
    solver.setOption("produce-models", "true")
    solver.setOption("tlimit-per", str(timeout_ms))
    try:
        sm = cvc5.SymbolManager(solver)
        ip = cvc5.InputParser(solver, sm)
        ip.setStringInput(cvc5.InputLanguage.SMT_LIB_2_6, smt, "q.smt2")
        t0 = time.perf_counter()
        while True:
            cmd = ip.nextCommand()
            if cmd.isNull():
                break
            cmd.invoke(solver, sm)
        r = solver.checkSat()
        dt = (time.perf_counter() - t0) * 1000
        print(f"V {str(r).split()[0]} {dt:.1f}")
    except Exception as e:
        print(f"E {type(e).__name__}: {str(e)[:120]}")

if __name__ == "__main__":
    main()
