# hihttps — Smith re-NO-GO

Triage-trial [#262](https://github.com/lucas-albers-lz4/regexproof/issues/262)
superseded after Smith triage at pin
`545a3bf676786f475509434724a25765f27a29f6`.

| Bucket | Sites | Notes |
|---|---:|---|
| `rules/REQUEST-*.conf` SecRule `@rx` | 243 | Modified OWASP CRS 3.x-lineage rules (rule IDs 942011…; comment-stripped diff vs CRS v4.11.0 = 1,078 lines, vs v3.3.5 = 734 lines) — **the coreruleset class** |
| `rules/main.rule` MainRule `rx:` | 1 | Custom SQL-keyword rule (`select|union|update|delete|insert|table|from|ascii|hex|unhex|drop`, id:1000) |
| `rules/*.data` (5 files) | 253 lines | Scanner-list data, not regex |
| `rules/webattack.txt` | 12 lines | Attack-sample strings, not regex |

The only non-CRS regex surface is **one** custom MainRule pattern. The 243
SecRule rows are CRS-derived duplicates of the admitted `coreruleset` families
(SQLi/XSS/PHP/RCE). Modified-CRS fork with ~1 novel pattern → **no-go**
(coraza-coreruleset #245 precedent).

Gate: `properties/generated/hihttps_gate_decision.json` → **no-go**
(supersedes `triage-trial`).
