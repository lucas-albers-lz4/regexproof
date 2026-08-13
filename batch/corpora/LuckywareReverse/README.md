# LuckywareReverse — Smith re-NO-GO

Triage-trial [#327](https://github.com/lucas-albers-lz4/regexproof/issues/327)
superseded after Smith triage at pin `350ed405971a723d54bce08080e5a7491c930b01`.

| Bucket | Sites | Decision |
|---|---:|---|
| Probe surface | 51 | below proof floor |

**Superseding no-go** (coraza/Hamburglar precedent): 51 yara sites - below any proof floor. Rootkit-removal yara rules are a subset of the yara class already admitted (malcontent/volatility3-mcp have rootkit families).

Gate: `properties/generated/LuckywareReverse_gate_decision.json` (no-go).
Smith: `properties/generated/LuckywareReverse_smith_decision.json` (no-go).
