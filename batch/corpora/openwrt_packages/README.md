# openwrt_packages corpus

Pinned `openwrt/packages` feed at
`e99adbc49f7a11d0377c8135fe706c7757b9e68c` for the OpenWrt conversion wave
([`sweep/openwrt-conversion/plan.md`](../../../sweep/openwrt-conversion/plan.md)).

Plan-time probe: 713 posix-shell sites / 202 files / 140 packages.
Runtime gate: `properties/generated/openwrt_packages_gate_decision.json`
(dated copy of the 2026-08-12 GO probe decision).

**Not** in `WAVE_CORPORA` — local batch / conversion only.

## Materialize

```bash
python scripts/materialize-corpus.py --gate \
  properties/generated/openwrt_packages_gate_decision.json
# or:
PIN=e99adbc49f7a11d0377c8135fe706c7757b9e68c
git clone --filter=blob:none https://github.com/openwrt/packages.git /tmp/openwrt-packages
git -C /tmp/openwrt-packages fetch --depth 1 origin "$PIN"
git -C /tmp/openwrt-packages checkout "$PIN"
ln -sfn /tmp/openwrt-packages batch/corpora/openwrt_packages/rules
test "$(git -C /tmp/openwrt-packages rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/openwrt_packages_gate_decision.json` (`go`).
Probe (plan-time only): `properties/generated/openwrt_packages_probe_decision.json`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus openwrt_packages \
  --assert-determinism
python -m regexproof.batch --corpus openwrt_packages
```

Do **not** pass `--with-redos` for conversion wave P1. Leave
`WAVE_CORPORA` unchanged.
