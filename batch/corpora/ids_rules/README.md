# ids_rules corpus (Phase 1a)

Suricata/Snort-compatible **Emerging Threats Open** rules (Suricata 7.0.3
bundle). Combined IDS corpus (plan #51 / #53).

## Materialize

```bash
curl -fsSL -o /tmp/emerging.rules.tar.gz \
  https://rules.emergingthreats.net/open/suricata-7.0.3/emerging.rules.tar.gz
mkdir -p /tmp/ids-rules && tar -xzf /tmp/emerging.rules.tar.gz -C /tmp/ids-rules
ln -sfn /tmp/ids-rules/rules batch/corpora/ids_rules/rules
```

Extractor: `ids_rules` (`pcre:"/…/flags"`). Dialect: `pcre`.
Accepted: `*.rules`. Skipped: commented alerts, non-rules files.

```bash
python scripts/measure-corpus-fraction.py --corpus ids_rules --assert-determinism
```
