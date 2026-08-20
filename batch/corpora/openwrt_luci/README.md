# openwrt_luci corpus

Pinned `openwrt/luci` at `77dad3f31405bc11f8384d742f7ad95314179694` for
the LuCI conversion wave
([`sweep/openwrt-luci-conversion/plan.md`](../../../sweep/openwrt-luci-conversion/plan.md)).

Plan-time probe: **895** ECMA sites / 189 files (GO on `security-boundary`).
Runtime gate: `properties/generated/openwrt_luci_gate_decision.json`.

**Not** in `WAVE_CORPORA` — local batch / conversion only. Prefer this
cluster over Smith drain ([#533](https://github.com/lucas-albers-lz4/regexproof/issues/533)).

## Materialize

```bash
PIN=77dad3f31405bc11f8384d742f7ad95314179694
git clone --filter=blob:none https://github.com/openwrt/luci.git /tmp/openwrt-luci-probe
git -C /tmp/openwrt-luci-probe fetch --filter=blob:none origin "$PIN"
git -C /tmp/openwrt-luci-probe checkout --detach "$PIN"
mkdir -p batch/corpora/openwrt_luci
ln -sfn /tmp/openwrt-luci-probe batch/corpora/openwrt_luci/rules
test "$(git -C /tmp/openwrt-luci-probe rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/openwrt_luci_gate_decision.json` (`go`).
Probe (plan-time only): `properties/generated/openwrt_luci_probe_decision.json`.

Extractor: `js_precise_dir` with
`glob: **/htdocs/**/*.js,**/htdocs/**/*.mjs` (skips `*.min.js`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus openwrt_luci \
  --assert-determinism
python -m regexproof.batch --corpus openwrt_luci
```

Do **not** pass `--with-redos` for conversion wave P1. Leave
`WAVE_CORPORA` unchanged. Commit `_batch_summary.json` only with a
conversion-ledger regen in the same PR.
