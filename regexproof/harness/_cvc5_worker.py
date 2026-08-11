#!/usr/bin/env python3
"""cvc5 per-query worker (D2 process isolation). Usage:
    python _cvc5_worker.py <smt-file> <timeout-ms>
Prints one line: "V <sat|unsat|unknown> <ms>" or "E <parse-error-text>".

The shared SMT text carries a trailing (check-sat): parse declarations only,
then run exactly ONE explicit checkSat (duplicated checks measured as a
Phase-1 review finding).
"""
import sys


def main():
    fn, timeout_ms = sys.argv[1], int(sys.argv[2])
    smt = open(fn).read()
    try:
        import cvc5
    except ImportError:
        print("E cvc5 not importable (need the cvc5 wheel; cross-check leg "
              "records absent)")
        return
    # The shared text carries a trailing (check-sat). Parse declarations only,
    # then run exactly ONE explicit checkSat.
    smt = smt.replace("\n(check-sat)\n", "\n")
    try:
        solver = cvc5.Solver()
        solver.setOption("tlimit-per", str(timeout_ms))
        solver.setOption("produce-models", "true")
        sm = cvc5.SymbolManager(solver)
        parser = cvc5.InputParser(solver, sm)
        parser.setStringInput(cvc5.InputLanguage.SMT_LIB_2_6, smt, "q.smt2")
        while not parser.done():
            cmd = parser.nextCommand()
            if cmd.isNull():
                break
            cmd.invoke(solver, sm)
        import time

        t0 = time.perf_counter()
        r = solver.checkSat()
        dt = round((time.perf_counter() - t0) * 1000, 1)
        print(f"V {str(r)} {dt}")
    except Exception as e:
        print(f"E {str(e)[:100]}")


if __name__ == "__main__":
    main()
