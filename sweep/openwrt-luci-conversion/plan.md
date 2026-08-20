# OpenWrt LuCI — conversion wave 1 (cluster N+1)

> Design: [`docs/CLUSTER-CONVERSION.md`](../../docs/CLUSTER-CONVERSION.md).
> Prior cluster close-out:
> [`properties/generated/openwrt_packages_conversion_wave3.md`](../../properties/generated/openwrt_packages_conversion_wave3.md)
> (packages idiom yield flat → **stop packages**; next cluster = LuCI).

**Goal:** Admit and convert one **ECMA/JS** cluster from `openwrt/luci`
(LuCI core + in-tree `luci-app-*` under `applications/`, not the ash
`openwrt/packages` family). Rank 15, write ≤5 human contracts, ground-truth
on **Node `RegExp`** (`helpers/ecma/match.mjs`), emit
`openwrt_luci_conversion.ndjson` so `properties_asked` moves.

**End state:** logged yield + skip deny-list. Not every `htdocs` file. Not
mixed into family `OW-packages`. Not `WAVE_CORPORA`. No public OpenWrt
filing without a human approval file.

## Trust map (Gate 2 input)

LuCI is the OpenWrt web UI. Client JS under `htdocs/luci-static/resources/`
runs in the browser (ECMAScript `RegExp`). Server-side ucode/Lua is out of
this wave unless a site is clearly JS. Trust classes:

| Trust | Typical source | Example |
|---|---|---|
| `untrusted-input` | WAN / unauthenticated HTTP fields, log lines, form values before UCI write | firewall log classifier tokens, hostname fields in status views |
| `config` | Operator UCI options already accepted by LuCI forms | validated option → RPC / uci.set |
| `internal` | i18n keys, build paths, theme class names, feature detect | `/^luci-/` package-name cosmetics |

Default: treat form-bound validators as `config` unless the surrounding code
shows a WAN or log-ingest path. `internal` never gets a contract.

**Vocab tokens:** `htdocs`, `luci-static`, `resources/view`, `firewall`,
`network`, `system`, `status`, `uci`, `rpc`, `passwd`, `wireless`, `ddns`,
`banip`, `pbr`, `adblock`.

**Product engine:** Node.js `RegExp` via `helpers/ecma/match.mjs` (same
semantics as browser LuCI). Absence of Node is a hard fail for this family.
BusyBox is **not** the product engine here (packages cluster already covered
that).

**Dialect / extractor:** `ecma` via `js_precise_dir` / `extract_js_precise`.
Do **not** claim `new-surface` for ECMA — ECMA is already admitted
(dompurify, isemail, …). This wave is **conversion**, not compiler novelty.
Admission basis: **security-boundary** (web UI validators / classifiers on
UCI and log paths) with findings potential, **or** documented escape hatch
if the probe boundary classifier stays `unknown` — same honesty as packages
(dated probe GO copy for runtime gate; do not refresh as if ECMA were novel).

## Already measured (Gate 0 — 2026-08-20)

From [`probe.md`](probe.md) and
`properties/generated/openwrt_luci_probe_decision.json`:

| Fact | Value |
|---|---|
| Unit | `openwrt/luci.git` @ `77dad3f31405bc11f8384d742f7ad95314179694` |
| Sites | **895** ECMA / 189 files / 52 apps with sites |
| Extract | ~1.5 s; clone 211M (`blob:none`, `max_disk_mb=2000`) |
| Density | `validation.js` 45, qosify 34, network.js 34, firewall app 42, banip 22 |
| Probe decision | **GO** on `security-boundary`. `new-surface=false` (ECMA admitted). `large-under-saturated=false` (895&lt;1000). |
| Batch | **not registered yet** — P2. |

## Non-goals

- NO re-asking packages idioms (hostname / JSON `[^"]*` / query `[^&]*` / …).
- NO mixing BusyBox ash properties into family `OW-luci`.
- NO `WAVE_CORPORA` membership.
- NO taint engine; NO synthesized shape-1/2 product rows.
- NO public upstream filing without approval.
- NO ucode (`.uc`) in wave 1.

## Artifact contract

| Artifact | Role |
|---|---|
| `sweep/openwrt-luci-conversion/plan.md` | this file |
| `properties/generated/openwrt_luci_probe_decision.json` | Gate 0 probe (plan-time) |
| `sweep/openwrt-luci-conversion/probe.md` + NDJSON | probe evidence |
| `openwrt_luci_gate_decision.json` | runtime gate (P1; copy/xref of probe like packages) |
| `batch/corpora/openwrt_luci/` + `CORPUS_MANIFESTS` | manifest corpus, not WAVE |
| `openwrt_luci_{encodable_fraction,batch_summary}.json` + `.ndjson` | Gate 1 filter; ledger regen same PR |
| `openwrt_luci_rank.json` | top 15 |
| harness family `OW-luci` | contracts + ≥1 mutation guard; Node GT |
| `openwrt_luci_conversion.ndjson` | ledger join |
| `openwrt_luci_conversion_wave.md` | close-out |

## Phases (serial)

### P0 — Plan + packages stop record

- This plan lands.
- Packages wave-3 close-out updated: **stop packages cluster**; LuCI started.
- Index links in `AGENTS.md` / README only if needed for discoverability
  (keep diff small).

### P1 — Runtime gate + manifest + batch (scan, not prove)

- Runtime gate file for `check_admission_gates` (probe copy + `related` xref).
- Register `openwrt_luci` in `CORPUS_MANIFESTS` (`extractor: js_precise_dir`,
  `dialect: ecma`, `security_tool: false`, htdocs glob).
- Measure + batch; commit summary **and** conversion-ledger regen same PR.
- Reconcile probe vs batch within 10% aggregate.

### P2 — Rank 15 / write ≤5

- Vocab above; drop tests/vendor/minified.
- Mix: 2–3 shape 1 (new alphabet only), 1–2 shape 3, 0–1 shape 4 if an
  escaper is in the bucket.
- Family `OW-luci`; `provenance=human`; mutation guard required.

### P3 — Node GT + ledger join

- SAT: replay via `helpers/ecma/match.mjs`.
- Expected-UNSAT shape-3: differential fuzz (Node vs mirror).
- Generate `openwrt_luci_conversion.ndjson`; ledger `properties_asked`
  delta in **[1, 5]**.

### P4 — Close-out

- Asked / skip / next idiom or stop-cluster / next cluster (e.g. OpenWrt
  core) named explicitly.

## Suggested PR carving

| PR | Phase |
|---|---|
| A | P0 plan + packages stop note + probe GO (docs) |
| B | P1 gate + `js_precise_dir` glob + manifest + batch + ledger |
| C | P2–P4 contracts, Node GT, close-out |

Non-trivial PRs: **Luna then Bugbot** before merge (workspace Bugbot
rule + this wave’s stronger Luna gate). Trivial docs-only may skip both.

## Risks

- **Repo size** — LuCI >> packages; enforce disk budget after blob
  materialization; prefer `--ext js,mjs` / `htdocs` scope so the walk does
  not pull every blob.
- **Minified vendor JS** — Gate 1 must drop `*.min.js` / large single-line
  files or rank will prefer noise.
- **ECMA already admitted** — do not invent `new-surface`; convert or
  security-boundary evidence only.
- **Ucode vs JS** — many modern LuCI apps are `.uc`; wave 1 is JS-only.
  Ucode is a later dialect decision, not a silent expand.
- **Disclosure** — third-party LuCI bugs are not auto-`private_first`; no
  public issue without approval.
