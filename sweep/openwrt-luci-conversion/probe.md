# OpenWrt LuCI admission probe — Gate 0 evidence

**Captured:** 2026-08-20 · **Pin:** `77dad3f31405bc11f8384d742f7ad95314179694`
(`luci-app-sfp-info: add missing ucode-mod-math dependency`) ·
**Decision:** GO on `security-boundary` (see
`properties/generated/openwrt_luci_probe_decision.json`).

## Clone

| Fact | Value |
|---|---|
| Unit | `openwrt/luci.git` (monorepo: modules / applications / protocols / themes) |
| Clone SHA | `77dad3f31405bc11f8384d742f7ad95314179694` |
| Depth / filter | `blob:none` partial clone via `regexproof.admission.clone.partial_clone` |
| `du -sh` after tree | **211M** (`max_disk_mb=2000`; GitHub size metadata ~550 MB) |
| Default HEAD | same as pin (tip at probe time) |

## Counter

```
python scripts/dogfood-singleton-analysis.py \
  --dir /tmp/openwrt-luci-probe \
  --name openwrt-luci \
  --ext js --ext mjs \
  --ndjson
```

Restricts to `.js` / `.mjs` (LuCI `htdocs` surface). Ucode (`.uc`) is **out
of wave 1**. NDJSON: `probe_records.ndjson` (895 records).

## Counts

| Metric | Value |
|---|---|
| Regex sites | **895** (all `ecma`) |
| Distinct (exact) | 583 |
| Files with sites | 189 |
| Sites under `htdocs/` | 893 |
| Applications with sites | 52 |
| Flags | none 680 · `g` 171 · `i` 42 · `gi` 2 |
| Constructs (probe) | class-escape 274 · inline-group 69 · lookaround 5 |

### Density (top)

| Sites | Path |
|---|---|
| 45 | `modules/luci-base/.../validation.js` |
| 34 | `applications/luci-app-qosify/.../main.js` |
| 34 | `modules/luci-base/.../network.js` |
| 42 | `luci-app-firewall` (app total) |
| 22 | `luci-app-banip` |
| 15 | `luci-app-adblock` |

`validation.js` alone is the conversion seed attention list: hostname,
IPv4/IPv6, MAC, uciname, and related form alphabets.

## Admission honesty

| Condition | Met | Why |
|---|---|---|
| `new-surface` | **no** | ECMA already admitted |
| `security-boundary` | **yes** | Web UI validators / classifiers on UCI and network/firewall forms |
| `large-under-saturated` | **no** | 895 &lt; 1000 |

Conversion cluster, not compiler novelty. Packages ash cluster is stopped
(wave 3 yield flat). Product engine for this cluster is **Node `RegExp`**,
not BusyBox.

## Next

P1 runtime gate + manifest + batch (plan
`sweep/openwrt-luci-conversion/plan.md`). Not `WAVE_CORPORA`.
