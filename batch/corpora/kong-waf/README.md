# kong-waf — Smith re-NO-GO

Triage-trial [#304](https://github.com/lucas-albers-lz4/regexproof/issues/304)
superseded after Smith triage at pin `bb1bb34e63be9b11b26114882fcdc69e1cee5906`.

| Bucket | Sites | Decision |
|---|---:|---|
| CRS fork pcre rules (27 conf files) | 300 | vendored CRS class |

**Superseding no-go** (coraza/hihttps precedent): full OWASP CRS file
layout (REQUEST-901..RESPONSE-9xx). The CRS WAF-rule family is already
covered — coraza-coreruleset superseded at admission, hihttps same shape.
No novel surface.

Gate: `properties/generated/kong-waf_gate_decision.json` (triage-trial).
Smith: `properties/generated/kong-waf_smith_decision.json` (no-go).
