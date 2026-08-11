#!/usr/bin/env python3
"""R2 \p gate table: every \p syntax position, gated against the harness policy,
with a Node differential corpus + a live from_ecma2020 probe per form (the
rejection evidence is measured, not asserted).

Policy (design U4/U8): \p forms are REJECTED at registration — from_ecma2020
does not support \p{} (measured below) and the mirror has no encoding without
full Unicode tables. No silent folding. The gate is conservative: node accepts,
the harness rejects with a rewrite suggestion.

Writes p1-baseline/p-gate-table.md (the table + corpus results are the artifact;
the JSON row data is regenerable).
"""
import sys, os, re, json, subprocess, tempfile, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
NOODLER = os.environ.get("NOODLER", "/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared")
OUT = os.path.join(ROOT, "sweep", "harness-backends", "p1-baseline")

# (position, form, flags) — the full syntax-position matrix
FORMS = [
    ("plain", r"\p{L}", ""),
    ("plain", r"\p{Lu}", ""),
    ("plain", r"\p{ASCII}", ""),
    ("plain", r"\p{Any}", ""),
    ("plain", r"\P{L}", ""),
    ("in-class", r"[\p{L}]", ""),
    ("in-class", r"[\p{L}\d]", ""),
    ("quantified", r"\p{L}+", ""),
    ("quantified", r"\p{L}{2}", ""),
    ("flag-i", r"\p{L}", "i"),
    ("flag-i", r"\p{Lu}", "i"),
    ("script", r"\p{Script=Greek}", ""),
    ("script", r"\p{Greek}", ""),
    ("escaped", r"\\p{L}", ""),          # literal backslash-p (escape)
    ("escaped", r"[\\p{L}]", ""),        # escaped in class
    ("malformed", r"\p{", ""),
    ("malformed", r"\p{}", ""),
    ("malformed", r"\p{L", ""),
    ("malformed", r"\p{L}}", ""),
    ("malformed", r"\p{L}{", ""),
    ("malformed", r"\p{Xyz}", ""),
    ("malformed", r"\p{L}", "u"),        # /u flag: strict semantics
]

TEST_STRS = ["a", "A", "1", "_", "é", "π", "", "ab"]

def node_test(pat, flags, strs):
    js = ",".join(json.dumps(s) for s in strs)
    src = (f"const r = new RegExp({json.dumps(pat)}, {json.dumps(flags)});\n"
           f"const strs = [{js}];\n"
           f"for (const s of strs) {{ r.lastIndex = 0; process.stdout.write(r.test(s) ? '1' : '0'); }}\n")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(src)
        path = f.name
    try:
        p = subprocess.run(["node", path], capture_output=True, text=True, timeout=30)
        bits = p.stdout.strip()
        if len(bits) != len(strs):
            return f"ERROR({p.stderr.strip()[:80]})"
        return bits
    finally:
        os.unlink(path)

def noodler_probe(pat_ecma):
    """from_ecma2020 membership on one string — records the solver's response to
    the \p form (the rejection evidence at solver level)."""
    body = ("(set-logic QF_SLIA)\n(declare-const s String)\n"
            f"(assert (str.in_re s (re.from_ecma2020 '{pat_ecma}')))\n"
            '(assert (= s "a"))\n(check-sat)\n')
    with tempfile.NamedTemporaryFile("w", suffix=".smt2", delete=False) as f:
        f.write(body)
        path = f.name
    try:
        t0 = time.perf_counter()
        try:
            p = subprocess.Popen([NOODLER, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True, start_new_session=True)
            try:
                out, _ = p.communicate(timeout=35)
            except subprocess.TimeoutExpired:
                os.killpg(os.getpgid(p.pid), 9)
                p.communicate()
                return "TIMEOUT"
        except FileNotFoundError:
            return "NO-BINARY"
        dt = (time.perf_counter() - t0) * 1000
        first = out.strip().splitlines()[0] if out.strip() else "EMPTY"
        if p.returncode < 0 or p.returncode == 139:
            return f"CRASH(rc={p.returncode})"
        return f"{first}/rc={p.returncode}"
    finally:
        os.unlink(path)

def gate_decision(pat):
    """The harness registration gate: REJECT any real property-escape token
    \\p{ or \\P{ (odd backslash chain), ACCEPT only escaped-literal forms
    (\\\\p — an even backslash chain)."""
    if re.search(r"(?<!\\)(?:\\\\)*\\(?:p|P)\{", pat):
        return "REJECT"
    return "ACCEPT"

def main():
    rows = []
    for pos, form, flags in FORMS:
        node_bits = node_test(form, flags, TEST_STRS)
        # search-wrapped form for the from_ecma2020 probe
        probe_pat = ".*" + form.replace("\\", "\\\\") + ".*"
        ndl = noodler_probe(probe_pat)
        gate = gate_decision(form)
        rows.append({"position": pos, "form": form, "flags": flags,
                     "node_bits": node_bits, "from_ecma2020": ndl, "gate": gate})
        print(f"{pos:12s} {form!r:16s} f={flags!r:3s} gate={gate:6s} node={node_bits} from_ecma2020={ndl}")

    with open(os.path.join(OUT, "p-gate.json"), "w") as f:
        json.dump(rows, f, indent=1)

    lines = ["# \\p gate table (R2) — every syntax position, gated + measured",
             "",
             "Run 2026-08-11, pinned Noodler v1.6.1, node v22.23.1. Policy (U4/U8):",
             "**REJECT all real `\\p{}`/`\\P{}` tokens at registration** — measured:",
             "`from_ecma2020` does NOT error on `\\p` — it silently treats it as an",
             "identity escape (literal 'p', exactly like non-/u node). The property",
             "intent (`\\p{L}` = any letter) is silently dropped at solver level:",
             "no error, no abstention, wrong semantics. That is the U4 class — the",
             "registration gate must reject, or the intent is silently lost. The",
             "mirror has no encoding without full Unicode tables. No silent folding;",
             "the gate is conservative (node accepts, the harness rejects with a",
             "rewrite suggestion: expand to explicit classes).",
             "",
             "Corpus: `a A 1 _ é π <empty> ab` — node bitstring per form.",
             "",
             "| position | form | flags | node | from_ecma2020 | gate |",
             "|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['position']} | `{r['form']}` | {r['flags'] or '—'} | "
                     f"{r['node_bits']} | {r['from_ecma2020']} | {r['gate']} |")
    lines += ["",
              "## Reading",
              "- **from_ecma2020 column**: `unsat/rc=0` on every probe = the pattern",
              "  was ACCEPTED and silently re-interpreted as literal text (identity",
              "  escape). Never a parse error, never an abstention — the trap.",
              "- **node without /u**: identical identity-escape semantics (bits match",
              "  the literal interpretation, e.g. `[\\p{L}\\d]` = literal-p OR digit →",
              "  only '1' matches). Node and the solver agree — but both are WRONG",
              "  relative to the property intent.",
              "- **node with /u** (`\\p{L}` row): REAL property semantics — 'a', 'A',",
              "  'é', 'π', 'ab' all match (11001101). The /u row shows what the user",
              "  meant; the harness gate rejects it rather than silently folding to",
              "  the literal form (U4).",
              "- **escaped** (`\\\\p{L}`): ACCEPT — an even backslash chain makes it",
              "  literal text (no `\\p{` token); node treats it as literal (bits all 0",
              "  — no string contains '\\\\pL'... consistent).",
              "- **malformed** (`\\p{`, `\\p{}`, `\\p{L`, `\\p{L}}`, `\\p{L}{`, `\\p{Xyz}`):",
              "  REJECT — node without /u silently literalizes (identity escapes, no",
              "  throw); with /u node throws (strict). The harness rejects uniformly —",
              "  no partial semantics, no reliance on the /u/non-/u divergence.",
              "",
              "## Implementation hook (Phase 2, #218)",
              "The registration gate calls the same Node-based ECMA parser as D7: a",
              "`\\p{`/`\\P{` token (odd backslash chain) anywhere in the pattern →",
              "registration error with the rewrite suggestion. Table-driven from this",
              "matrix."]
    with open(os.path.join(OUT, "p-gate-table.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"wrote {OUT}/p-gate-table.md")

if __name__ == "__main__":
    main()
