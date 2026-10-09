# wordpress_modsecurity_ruleset corpus

Pinned `Rev3rseSecurity/wordpress-modsecurity-ruleset` at `6bdd250e3b121f79c9b06ea48231cdada8e9dac9` for Smith after admission `wordpress_modsecurity_ruleset_gate_decision.json`.

## Materialize

```bash
python scripts/materialize-corpus.py --gate properties/generated/wordpress_modsecurity_ruleset_gate_decision.json --allowlist-file batch/corpora/wordpress_modsecurity_ruleset/files.txt
```

Gate: `properties/generated/wordpress_modsecurity_ruleset_gate_decision.json`.

The scaffold's generic PCRE guess is `rule_file`; this corpus uses the
registered `modsec` extractor because its inputs are `SecRule` directives.
The explicit root-level allowlist excludes `99-TEST.conf` and `test/` files.
The admission probe counted 23 sites including two test sites; Smith measures
the five production configuration files only.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus wordpress_modsecurity_ruleset --assert-determinism
python -m regexproof.batch --corpus wordpress_modsecurity_ruleset --no-planned --jobs 1
```

Do not add `WAVE_CORPORA` until a local `complete_run`. The triage-trial gate
does not itself adopt a product contract or imply a Smith GO. The 1.0
encodable fraction is an automated compile result; a human Smith decision and
human contract adoption remain separate steps. Do not author a Smith decision
from the fraction alone.
