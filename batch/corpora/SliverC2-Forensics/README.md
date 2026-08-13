# SliverC2-Forensics — Smith re-NO-GO

Triage-trial [#334](https://github.com/lucas-albers-lz4/regexproof/issues/334)
superseded after Smith triage at pin `33391a8c016f0e902950e8c2d9867b7e8d0e9b2a`.

| Bucket | Sites | Decision |
|---|---:|---|
| Probe surface | 6 | below proof floor |

**Superseding no-go** (coraza/Hamburglar precedent): 6 yara/py sites - below any proof floor. C2-detection yara rules are a subset of the yara class already admitted (malcontent/volatility3-mcp have C2 families).

Gate: `properties/generated/SliverC2-Forensics_gate_decision.json` (no-go).
Smith: `properties/generated/SliverC2-Forensics_smith_decision.json` (no-go).
