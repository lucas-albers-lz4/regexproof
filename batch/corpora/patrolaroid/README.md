# patrolaroid corpus

Pinned rpetrich/patrolaroid yara pack for Smith GO admit
[#331](https://github.com/lucas-albers-lz4/regexproof/issues/331)
under umbrella [#328](https://github.com/lucas-albers-lz4/regexproof/issues/328).

AWS malware scanner. 38 yara files measured **1,687/4,491 = 0.3756
encodable** (complete, deterministic) with 22 findings — the lowest yara
fraction in the matrix (scanner detection rules are fullword-boundary-heavy).

## Materialize

```bash
PIN=ed7ad98fa495ca9a7d9e855dd260218ba4e67a9b
git clone --filter=blob:none https://github.com/rpetrich/patrolaroid.git /tmp/patrolaroid
git -C /tmp/patrolaroid fetch --depth 1 origin "$PIN"
git -C /tmp/patrolaroid checkout "$PIN"
ln -sfn /tmp/patrolaroid/rules batch/corpora/patrolaroid/rules
test "$(git -C /tmp/patrolaroid rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/patrolaroid_gate_decision.json` (`go`).
Smith: `properties/generated/patrolaroid_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus patrolaroid --assert-determinism
python -m regexproof.batch --corpus patrolaroid
```

## Notes

- The 0.3756 fraction is the yara-family floor so far (yara_rules 0.656,
  malcontent 0.6993, volatility3-mcp 0.6563, SMAT 0.6269, PEpper 0.6229,
  sec_check 0.6189, whohk 0.6165, Antivirus 0.5799). Detection rules with
  `fullword` boundaries dominate the rejects — consistent with the known
  yara reject profile.
