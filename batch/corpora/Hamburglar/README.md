# Hamburglar — Smith re-NO-GO

Triage-trial [#283](https://github.com/lucas-albers-lz4/regexproof/issues/283)
superseded after Smith triage at pin
`87cec6a57add4bd487df37e80f04559555c1b01c`.

| Bucket | Sites | Notes |
|---|---:|---|
| `src/hamburglar/detectors/regex_detector.py` DEFAULT_PATTERNS | 22 | Dict-literal secret patterns (AWS keys, GitHub tokens, RSA private keys) — **the gitleaks class**; extractor-blind (not `re.compile` calls) |
| `rules/*.yar` (19 files) | 143 rules / 1,973 lines | String-match malware-signature yara rules — **the yara_rules class** |

Probe counted 8 sites (5 py_re + 3 yara) — the dict-literal patterns and
string-based yara rules are undercounted by the extractors. Regardless of the
true count, the **pattern classes are already covered by four admitted
corpora**: gitleaks (0.819), detect-secrets, noseyparker, shhgit (secret
detection) and yara_rules / ail-yara-rules (yara strings). No novel dialect,
no new construct class, no findings surface beyond the admitted duplicates.
Duplicate class → **no-go**.

Gate: `properties/generated/Hamburglar_gate_decision.json` → **no-go**
(supersedes `triage-trial`).
