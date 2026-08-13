# vedetta — Smith re-NO-GO (measured)

Triage-trial [#289](https://github.com/lucas-albers-lz4/regexproof/issues/289)
resolved after Smith measurement at pin
`cec6a1caef7a576c036e6d07eabd482fe0a6b059`.

| Bucket | Sites | Fraction |
|---|---:|---|
| go re2 (14 files) | 103 | 26 encodable = **0.2524** |
| py_re (2 files) | 138 | 46 encodable = 0.3333 (thin, superseded) |

**Measured no-go** (fraction gate): the SIEM's hostname-fingerprinting
regexes are RE2-heavy (anchors/Go constructs) rejected by the compile
path. Below the 0.30 gate. Honest measurement — the corpus is real but
not encodable enough.

Gate: `properties/generated/vedetta_gate_decision.json` (triage-trial).
Smith: `properties/generated/vedetta_smith_decision.json` (no-go).
