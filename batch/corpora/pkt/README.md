# pkt — Smith re-NO-GO

Triage-trial [#355](https://github.com/lucas-albers-lz4/regexproof/issues/355)
superseded after Smith triage at pin `12928efec3304d51502f9250bf13fd549b6f7d4b`.

| Bucket | Sites | Decision |
|---|---:|---|
| Probe surface | 20 | below proof floor |

**Superseding no-go** (coraza/Hamburglar precedent): 20 yara sites - below any proof floor (P(compiles) knee needs 20-50 repos of real density; 20 sites has no statistical power). Yara class already covered by malcontent/volatility3-mcp/SMAT/PEpper/sec_check/Antivirus/patrolaroid/whohk.

Gate: `properties/generated/pkt_gate_decision.json` (no-go).
Smith: `properties/generated/pkt_smith_decision.json` (no-go).
