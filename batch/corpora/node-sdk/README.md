# node-sdk — Smith re-NO-GO

Triage-trial [#181](https://github.com/lucas-albers-lz4/regexproof/issues/181)
superseded after Smith file-map review at pin
`594ee0e0c0b042ee9eed21f262be3c4bc5a1919b`.

| Bucket | Sites | Notes |
|---|---:|---|
| `test/unit/*.test.js` | 406 | Generated client fixtures |
| `scripts/typedoc/theme/...` | 114 | Docs theme vendor |
| `scripts/jsdoc/.../prettify` + publish | 85 | Docs tooling |
| `lib/*.ts` + report script | 4 | Only thin first-party |

No product security-boundary regex surface worth batch measure.
Gate: `properties/generated/node-sdk_gate_decision.json` → **no-go**.
