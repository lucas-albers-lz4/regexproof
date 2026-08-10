# evmos — Smith re-NO-GO

Triage-trial [#182](https://github.com/lucas-albers-lz4/regexproof/issues/182)
superseded after Smith file-map review at pin
`0402a01c9036b40a7f47dc2fc5fb4cfae019f5f1`.

| Bucket | Sites | Notes |
|---|---:|---|
| `client/docs/swagger-ui/*.js` | 361 | Vendored swagger-ui |
| `scripts/changelog_checker` / license / compile | 38 | Tooling scripts |
| tests / suite | 10 | Not product boundary |

No product security-boundary regex surface worth batch measure.
Gate: `properties/generated/evmos_gate_decision.json` → **no-go**.
