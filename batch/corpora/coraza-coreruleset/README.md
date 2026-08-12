# coraza-coreruleset — Smith re-NO-GO

Triage-trial [#245](https://github.com/lucas-albers-lz4/regexproof/issues/245)
superseded after Smith measurement at pin
`a664dd18b4b0468215126c6f524e91b2a0deec26`.

| Bucket | Sites | Notes |
|---|---:|---|
| `rules/@owasp_crs/*.conf` | 343 | Unmodified OWASP CRS **v4.25.0** embedded verbatim (rule lines byte-identical to upstream tag; only comments stripped) |
| `rules/@coraza.conf-recommended` | 3 | Coraza WAF config Content-Type regexes — config, not a rule corpus |
| `rules/@crs-setup.conf.example` | 0 | `@rx` line is commented out |

Measured `@owasp_crs` at pin: 193/343 = 0.5627 encodable (complete, deterministic)
— but **88.4% of patterns are identical to the already-admitted `coreruleset`
inventory** (260/294), and the residual is version drift of the same rule
families (SQLi/XSS/RCE/JS-URI) against the unpinned admitted corpus. Coraza
packaging adds **no distinct rule-corpus surface worth retaining**: the only
Coraza-specific regexes are 3 Content-Type WAF-config entries in
`@coraza.conf-recommended` (config, not a rule corpus); `@crs-setup.conf.example`'s
`@rx` is commented out. Duplicate → **no-go**.

Gate: `properties/generated/coraza-coreruleset_gate_decision.json` →
**no-go** (supersedes `triage-trial`).
