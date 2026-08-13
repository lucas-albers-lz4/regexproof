# typenix — Smith re-NO-GO

GO admit [#320](https://github.com/lucas-albers-lz4/regexproof/issues/320)
superseded after Smith triage at pin
`13550ee05461121a74a6467aefc479a62026cdfc`.

| Bucket | Sites | Decision |
|---|---:|---|
| testdata/ TS baselines (12,423 js files) | 5,126 | v8/test262 class (admitted) |
| first-party (internal/_packages/root) | 81 | below proof floor |

**Superseding no-go** (tarcoin precedent): the scale-based GO was met on
testdata-inflated numbers. Real first-party surface is 19–80 sites; the
testdata is TypeScript-compiler baselines, same class as the admitted
typescript-go/v8/test262 corpora.

Gate: `properties/generated/typenix_gate_decision.json` (go).
Smith: `properties/generated/typenix_smith_decision.json` (no-go).
