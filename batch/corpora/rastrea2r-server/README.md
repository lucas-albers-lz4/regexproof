# rastrea2r-server — Smith re-NO-GO

Triage-trial [#354](https://github.com/lucas-albers-lz4/regexproof/issues/354)
superseded after Smith triage at pin
`3e4d26d06d02a32f309afaac1bdf82cada149c2a`.

| Bucket | Sites | Decision |
|---|---:|---|
| vendored docs-coverage jquery bundles | 107 | vendored third-party class |
| rules/example.yara | 12 | single example rule |
| first-party app code | 2 | below proof floor |

**Superseding no-go** (exchange-api/typenix precedent): probe count inflated
by vendored docs-coverage bundles. Real first-party surface is 2–4 sites.

Gate: `properties/generated/rastrea2r-server_gate_decision.json` (triage-trial).
Smith: `properties/generated/rastrea2r-server_smith_decision.json` (no-go).
