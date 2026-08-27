# marcusquinn/aidevops — conversion wave 1 (cluster N+1)

> Design: [`docs/CLUSTER-CONVERSION.md`](../../docs/CLUSTER-CONVERSION.md).
> Prior cluster close-out:
> [`properties/generated/openwrt_luci_conversion_wave.md`](../../properties/generated/openwrt_luci_conversion_wave.md)
> (LuCI idiom yield flat → **stop LuCI**; next cluster = aidevops posix-shell
> agent hooks).

**Goal:** Admit and convert one **posix-shell** cluster from
`marcusquinn/aidevops` (agent hooks / pre-push guards under `.agents/hooks/`,
not the ECMA plugin tree). Rank 15, write ≤5 human contracts, ground-truth
on **BusyBox** (product engine), emit `aidevops_conversion.ndjson` so
`properties_asked` moves.

**End state:** logged yield + skip deny-list. Not every `.agents/plugins`
mjs file. Not mixed into family `OW-packages` / `OW-luci`. Not
`WAVE_CORPORA`. No public aidevops filing without a human approval file.

## Trust map (Gate 2 input)

aidevops is an AI-devops agent runtime: POSIX shell hooks and guards that
run on git events (pre-push, pre-edit) and shape tool-call / credential /
scope policy. Wave 1 is **posix-shell only** — ECMA under
`.agents/plugins/opencode-aidevops/` is a later dialect decision, not a
silent expand. Trust classes:

| Trust | Typical source | Example |
|---|---|---|
| `untrusted-input` | Agent tool-call args, git remotes, user-supplied paths/filenames, credential-shaped strings in transcripts | filename guard, credential-emission pre-push, task-id collision |
| `config` | Operator-authored hook allowlists / repo policy already accepted by the agent | scope-guard patterns, gh-wrapper allowlists |
| `internal` | Feature detect, test fixtures, i18n, plugin cosmetics | `tests/test-*.sh`, complexity-advisory py internals |

Default: treat hook/guard validators as `config` unless the surrounding
code shows argv / transcript / remote ingest. `internal` never gets a
contract.

**Vocab tokens:** `hooks`, `guard`, `pre-push`, `pre-edit`, `credential`,
`privacy`, `scope`, `secret`, `gh-wrapper`, `task-id`, `filename`,
`complexity`, `repo-verify`, `.agents/hooks`.

**Product engine:** BusyBox ash + BusyBox `grep`/`sed`/`awk` (same pin
golden CI already installs). BusyBox is the product result. GNU is logged
when it can disagree; **agreement is not required**. Absence of BusyBox is
a hard fail. Node `RegExp` is **not** the product engine here (LuCI
cluster already covered that).

**Dialect / extractor:** `posix-shell` via `shell_posix`. Do **not** claim
`new-surface` — posix-shell is already admitted (anax, mycelium, packages,
…). This wave is **conversion**, not compiler novelty. Admission basis:
**large-under-saturated** (scale: 7,031 non-test first-party shell sites
≥ 1000; shell under-saturated), **not** security-boundary
(`security_boundary=unknown`; not a security-tool corpus).

**Family:** `AI-aidevops`. Same `family=` on every property including the
mutation guard.

## Already measured (Gate 0 — 2026-08-13)

From `properties/generated/marcusquinn-aidevops_gate_decision.json`
(plan-time probe; `check_admission_gates` does not read this filename):

| Fact | Value |
|---|---|
| Unit | `marcusquinn/aidevops.git` @ `8666b6c6c52472b5535aa295f2df593918152cb1` |
| Sites | **12,880** total / **11,330** posix-shell / 1,042 ECMA / 508 py_re / 1,817 files |
| Density | `.agents/` 11,881; `.agents/hooks/` 12 files / 50 sites (wave-1 bucket); `tests/` 795 |
| Probe decision | **GO** on `large-under-saturated`. `new-surface=false`. `security-boundary=false`. |
| Batch | **not registered** until P1. Follow-on from the dated probe GO. |

**Gate 0 stop:** if P1 encodable fraction **< 0.30**, stop the cluster
(no PR2 rank/contracts). TIMEOUT is not a pass.

posix-shell is already admitted. A **fresh** gate must **not** claim
`new-surface` is still met. This wave is conversion, not compiler novelty.

## Non-goals

- NO re-asking OpenWrt / LuCI idioms (hostname / JSON `[^"]*` / query `[^&]*` / …).
- NO mixing ECMA plugin properties into family `AI-aidevops` in wave 1.
- NO `WAVE_CORPORA` membership.
- NO taint engine; NO synthesized shape-1/2 product rows.
- NO public upstream filing without approval.
- NO `.agents/plugins/**/*.mjs` in wave 1.

## Artifact contract

| Artifact | Role |
|---|---|
| `sweep/aidevops-conversion/plan.md` | this file |
| `properties/generated/marcusquinn-aidevops_gate_decision.json` | Gate 0 probe (plan-time) |
| `aidevops_gate_decision.json` | runtime gate (P1; copy/xref of probe) |
| `batch/corpora/aidevops/` + `CORPUS_MANIFESTS` | manifest corpus, not WAVE |
| `aidevops_{encodable_fraction,batch_summary}.json` + `.ndjson` | Gate 1 filter; ledger regen same PR |
| `aidevops_rank.json` | top 15 |
| harness family `AI-aidevops` | contracts + ≥1 mutation guard; BusyBox GT |
| `aidevops_conversion.ndjson` | ledger join |
| `aidevops_conversion_wave.md` | close-out |

## Phases (serial)

### P0 — Plan + LuCI stop record

- This plan lands.
- LuCI wave-1 close-out already records **stop LuCI cluster**; aidevops
  started.
- Index links in `AGENTS.md` / README only if needed for discoverability
  (keep diff small).

### P1 — Runtime gate + manifest + batch (scan, not prove)

- Runtime gate file for `check_admission_gates` (probe copy + `related` xref).
- Register `aidevops` in `CORPUS_MANIFESTS` (`extractor: shell_posix`,
  `dialect: posix-shell`, `security_tool: false`, `BUDGET_HEAVY_50K`).
- Measure + batch; commit summary **and** conversion-ledger regen same PR.
- Reconcile probe posix-shell count vs batch extracted within 10% aggregate.
- **Stop** if encodable fraction < 0.30.

### P2 — Rank 15 / write ≤5

- Vocab above; drop tests/vendor. Current bucket:
  **posix-shell agent hooks/guards** (`.agents/hooks/`).
- Mix: 2–3 shape 1 (new alphabet only), 1–2 shape 3, 0–1 shape 4 if an
  escaper is in the bucket.
- Family `AI-aidevops`; `provenance=human`; mutation guard required.

### P3 — BusyBox GT + ledger join

- SAT: replay on BusyBox (`grep`/`sed`/`awk` as the site uses).
- Expected-UNSAT shape-3: differential fuzz (BusyBox vs mirror).
- Do not clone P3 GNU∩BusyBox. Empty capture is **not** truncation.
- Generate `aidevops_conversion.ndjson`; ledger `properties_asked`
  delta in **[1, 5]**.

### P4 — Close-out

- Asked / skip / next idiom or stop-cluster / next cluster named explicitly.
- Pattern-class SAT (alphabet cannot contain the witness char) →
  `wont_file`, not `private_first`.

## Suggested PR carving

| PR | Phase |
|---|---|
| 1 | P1 gate + `shell_posix` manifest + batch + ledger |
| 2 | P2–P4 contracts, BusyBox GT, close-out (only if fraction ≥ 0.30) |

Non-trivial PRs: **Luna then Bugbot** before merge (workspace Bugbot
rule). Trivial docs-only may skip both.

## Risks

- **Scale** — 11k posix-shell sites; `BUDGET_HEAVY_50K` (`max_patterns=50000`,
  `max_wall_s=1200`). Probe counted mixed dialects (12,880); P1 batch is
  posix-shell only — reconcile vs `probe.dialect.posix-shell` (11,330).
- **ECMA already admitted** — do not invent `new-surface`; do not mix
  plugin JS into this family.
- **`tests/` inflation** — materialize `--allowlist-file` ACK; Gate 1
  still drops `tests/` before ranking.
- **Disclosure** — third-party aidevops bugs are not auto-`private_first`;
  no public issue without approval.
