# whohk corpus

Pinned wgpsec/whohk yara pack for Smith GO admit
[#306](https://github.com/lucas-albers-lz4/regexproof/issues/306)
under umbrella [#305](https://github.com/lucas-albers-lz4/regexproof/issues/305).

Linux incident-response tool. 22 yara files measured **1,318/2,138 =
0.6165 encodable** (complete, deterministic) with 18 findings.

## Materialize

```bash
PIN=1143af45b06c2e49c9f13efb149cd20067e8ea38
git clone --filter=blob:none https://github.com/wgpsec/whohk.git /tmp/whohk
git -C /tmp/whohk fetch --depth 1 origin "$PIN"
git -C /tmp/whohk checkout "$PIN"
ln -sfn /tmp/whohk batch/corpora/whohk/rules
test "$(git -C /tmp/whohk rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/whohk_gate_decision.json` (`go`).
Smith: `properties/generated/whohk_smith_decision.json` (`go`).
IR tool, not a vendor security product → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus whohk --assert-determinism
python -m regexproof.batch --corpus whohk
```
