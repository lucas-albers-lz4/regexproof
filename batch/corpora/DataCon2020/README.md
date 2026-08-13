# DataCon2020 — Smith re-NO-GO (measured)

GO admit [#333](https://github.com/lucas-albers-lz4/regexproof/issues/333)
resolved after Smith measurement at pin
`b22446263c872a651a1cba781c1f3d892c552af8`.

| Bucket | Sites | Fraction |
|---|---:|---|
| yara (4 files: rule20/black_rules/crypto/packer) | 1,285 | 90 encodable = **0.0700** |

**Measured no-go** (fraction gate): the competition winner's detection
rules are written for YARA-engine consumption (obfuscation-heavy
conditions, fullword boundaries, engine-specific constructs) — the
compile path rejects ~93%. Lowest fraction in the matrix. Honest
measurement over superseding.

Gate: `properties/generated/DataCon2020_gate_decision.json` (go).
Smith: `properties/generated/DataCon2020_smith_decision.json` (no-go).
