# exchange-api — Smith re-NO-GO

GO admit [#308](https://github.com/lucas-albers-lz4/regexproof/issues/308)
superseded after Smith triage at pin
`dfaabdccf3eda5e0bee4d7b95e90c3f52001b70e`.

| Bucket | Sites | Decision |
|---|---:|---|
| vendored swagger-ui bundles (5 files) | 1,305 | vendored third-party class |
| first-party shell (4 files) | 4 | below proof floor |

**Superseding no-go** (typenix/tarcoin precedent): the scale-based GO was
met on vendored swagger-ui bundle numbers. Real first-party surface is 4
shell sites. No novel encodable surface.

Gate: `properties/generated/exchange-api_gate_decision.json` (go).
Smith: `properties/generated/exchange-api_smith_decision.json` (no-go).
