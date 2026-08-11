# Witness divergence triage (P1 baseline, 2026-08-11)

Three SAT rows show differing witnesses between stock z3 and Noodler. All three are
**valid alternative models of the same existential formula** (multi-model
multiplicity — measured and documented in the m2 close, design D16), not anomalies.
Byte-comparison across solvers applies only to uniquely-pinned witnesses.

| Property | Stock witness | Noodler witness | Verdict | Why both are valid |
|---|---|---|---|---|
| P1-mutated-star | `u = "l*"` | `u = "a" + 31 stars` | **No disagreement** | The mutation guard weakens the username regex so `*` is a literal; the language accepts any `a*`-shaped string, including both witnesses. Existential — many models |
| P2-mutated-space | `a = " "` | `a = "a" + 15 spaces` | **No disagreement** | Property is `Contains(a, " ")` over the whitelist; any whitelisted string containing a space is a witness. Both qualify |
| P3-sed-capture-truncation | `v = "\""` (backslash + quote) | `v = "\"" + 3 quotes` | **No disagreement** | Property is `Contains(v, escaped-quote-token)` with the capture-differs goal; any string containing `\"` with a differing prefix qualifies. Both reproduce the sed truncation bug (ground-truth replay passes on both) |

**Non-issue confirmation:** P4-nul-passthrough-demo reports MATCH — the two solvers
print the same NUL character differently (`\u{0}` SMT-LIB form vs `\x00`), and the
baseline decodes both to the raw character before comparing (the earlier DIFF was an
escaping artifact, not a model difference).

No wrong-verdict signal in any row: all three DIFFs re-assert `sat` in stock z3
against the property formula (D16 — the re-validation gate that Phase 2 ships as a
runner feature; the baseline comparison is the pre-runner calibration).

**S11 cvc5 note (run 8, 2026-08-11):** the cvc5 worker on the re.loop text is
NONDETERMINISTIC between runs — PARSE-ERROR ("Symbol 're.loop' not declared") in
runs 6-7, ABSTAIN-SIGSEGV (worker rc -11) in run 8. This is the documented
batch-segfault class (design D2): the cvc5 C++ library crashes on some inputs it
cannot parse. Both outcomes are abstentions; the worker containment is the design
behavior — a crash is recorded, never propagated, never a verdict.
