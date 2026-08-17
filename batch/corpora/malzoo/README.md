# malzoo corpus

Pinned `nheijmans/malzoo` at `de1b93347a9783e3d2ec7b5297306bf66c9fbaa1`
for Smith after admission `malzoo_gate_decision.json`. YARA pack only
(`data/yara_rules`); `tests/` excluded.

## Materialize

Probe flags `tests/smoke_test.sh` as testdata inflation — materialize requires
a non-empty allowlist of the intended YARA pack paths (acknowledgment only;
manifest `glob` still scopes extract).

```bash
cat > /tmp/malzoo-allowlist.txt <<'EOF'
data/yara_rules/APT_NGO_wuaclt_PDF.yara
data/yara_rules/MMC_d.yara
data/yara_rules/XweberInstall.yara
data/yara_rules/apt1.yara
data/yara_rules/dridex.yar
data/yara_rules/embedded.yara
data/yara_rules/filetypes.yara
data/yara_rules/hangover.yara
data/yara_rules/kins.yara
data/yara_rules/leverage.yar
data/yara_rules/rats.yara
data/yara_rules/themask.yara
data/yara_rules/urausy_skypedat.yar
data/yara_rules/vmdetect.yara
EOF
python scripts/materialize-corpus.py --gate properties/generated/malzoo_gate_decision.json \
  --allowlist-file /tmp/malzoo-allowlist.txt
ln -sfn /tmp/nheijmans-malzoo-malzoo/data/yara_rules batch/corpora/malzoo/rules
test "$(git -C /tmp/nheijmans-malzoo-malzoo rev-parse HEAD)" = "de1b93347a9783e3d2ec7b5297306bf66c9fbaa1"
```

Gate: `properties/generated/malzoo_gate_decision.json` (`go`).
Scanner pack — `security_tool=True` (`private_first`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus malzoo --assert-determinism
python -m regexproof.batch --corpus malzoo
python scripts/author-smith-decision.py --gate properties/generated/malzoo_gate_decision.json \
  --fraction properties/generated/malzoo_encodable_fraction.json \
  --decision go --reason '1214/1230 = 0.9870 on data/yara_rules'
```
