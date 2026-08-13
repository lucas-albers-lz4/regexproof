# modsec — Smith re-NO-GO

Triage-trial [#322](https://github.com/lucas-albers-lz4/regexproof/issues/322)
superseded after Smith triage at pin `500c111dbfffec4ee11c629b102f4ac04d09ac3a`.

| Bucket | Sites | Decision |
|---|---:|---|
| CRS fork pcre rules (5,982 SecRule lines) | 318 | vendored CRS class |

**Superseding no-go** (coraza/hihttps precedent): full OWASP CRS fork
(modsecurity_crs_* naming, SEC642 course). Vendored WAF family already
covered (coraza-coreruleset + hihttps superseded). No novel surface.

Gate: `properties/generated/modsec_gate_decision.json` (triage-trial).
Smith: `properties/generated/modsec_smith_decision.json` (no-go).
