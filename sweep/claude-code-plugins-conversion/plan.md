# melodic-software/claude-code-plugins — conversion wave 1

> Design: [`docs/CLUSTER-CONVERSION.md`](../../docs/CLUSTER-CONVERSION.md).
> Prior cluster close-out:
> [`properties/generated/mycelium_conversion_wave.md`](../../properties/generated/mycelium_conversion_wave.md)
> (posix-shell `control/` done; `scripts/` bootstrap deferred). Next cluster =
> claude-code-plugins posix-shell plugin/hooks/guards.

**Goal:** Convert one **posix-shell** cluster from
`melodic-software/claude-code-plugins` (Claude Code plugin marketplace
hooks/guards under `plugins/guardrails/hooks/`, not ECMA skills/MCP). Rank 15,
write ≤5 human contracts, ground-truth on **BusyBox** (product engine), emit
`claude-code-plugins_conversion.ndjson` so `properties_asked` moves.

**End state:** logged yield + skip deny-list. Not every `plugins/*/hooks/hook-utils.sh`
copy. Not mixed into family `OW-packages` / `OW-luci` / `AI-aidevops` /
`MY-mycelium`. Not `WAVE_CORPORA`. No public claude-code-plugins filing without
a human approval file.

Gate+Smith GO and batch already landed (fraction **0.8132**). Manifest
`CORPUS_MANIFESTS["claude-code-plugins"]` exists — do **not** re-batch or copy
gate.

## Trust map (Gate 2 input)

claude-code-plugins is a Claude Code plugin marketplace: POSIX shell hooks
that gate agent tool calls (dangerous git, hook-bypass writes, CLI-flag
hallucinations, skill-reference resolve). Wave 1 is **posix-shell
`plugins/guardrails/hooks/` only** — `*.test.sh` is Gate 1 drop; ECMA under
skills/MCP is a later dialect decision. Trust classes:

| Trust | Typical source | Example |
|---|---|---|
| `untrusted-input` | Agent Write/Edit payloads, Bash/PowerShell tool-call argv | CLI long-flag extract, `/plugin:skill` ref, `git clean -e` bundle |
| `config` | Operator plugin options already accepted at enable time | scratch-root list, skip-bins, allow-list form tokens |
| `internal` | Feature detect, timeout parse, env-wrapper peel, test fixtures | `hook-utils.sh` `read -t` micros, `*.test.sh` |

Default: treat hook/guard validators as `config` unless the surrounding code
shows argv / written-file ingest. `internal` never gets a contract.

**Vocab tokens:** `hooks`, `guard`, `guardrails`, `secret`, `block`, `bypass`,
`convention`, `permission`, `flag`, `dangerous`, `no-verify`, `git`.

**Product engine:** BusyBox ash + BusyBox `grep`/`sed`/`awk` (same pin
golden CI already installs). BusyBox is the product result. GNU is **not**
consulted. Absence of BusyBox is a hard fail. Dispatch by tool (`grep -E`
for bash `=~` search sites; `sed -E` for substitution captures as at the
call site). Node `RegExp` is **not** the product engine here.

**Dialect / extractor:** `posix-shell` via `shell_posix`. Do **not** claim
`new-surface` — posix-shell is already admitted. This wave is
**conversion**, not compiler novelty. Admission basis:
**large-under-saturated** (1,344 posix-shell sites; fraction 0.8132).

**Family:** `AI-claude-plugins`. Same `family=` on every property including
the mutation guard.

**Exclude:** `tests/`, `*.test.sh`, fixtures, ECMA (`*.mjs` / `*.js`). Gate 1
still drops those before ranking.

**Deny-list (prior close-outs):** no hostname / JSON `[^"]*` / digit-semicolon
/ brief t-ID / ssh-key / awg-dialect / ALPN re-asks.

## Already measured (Gate 0 — admit done)

From `properties/generated/claude-code-plugins_gate_decision.json` +
`claude-code-plugins_smith_decision.json` +
`claude-code-plugins_encodable_fraction.json`:

| Fact | Value |
|---|---|
| Unit | `melodic-software/claude-code-plugins` @ `f44d0df5e7bf023b88cccc37301402ba7f9dcdb1` |
| Sites | **1,786** probe / **1,344** posix-shell / 359 ECMA / 83 py_re |
| Density | `plugins/guardrails/hooks/` is the wave-1 bucket; `hook-utils.sh` copies dominate other `plugins/*/hooks/` |
| Probe + Smith | **GO**. `new-surface=false`. Batch fraction **0.8132** (1093/1344). |
| Manifest | `CORPUS_MANIFESTS["claude-code-plugins"]` already registered — **do not re-batch**. |

posix-shell is already admitted. A **fresh** gate must **not** claim
`new-surface` is still met.

## Non-goals

- NO re-asking aidevops / mycelium / OpenWrt / LuCI idioms (hostname / JSON
  `[^"]*` / digit-semicolon / brief t-ID / ssh-key / awg-dialect / ALPN).
- NO mixing ECMA skills/MCP into family `AI-claude-plugins`.
- NO `WAVE_CORPORA` membership.
- NO taint engine; NO synthesized shape-1/2 product rows.
- NO public upstream filing without approval.
- NO `*.test.sh` / `hook-utils.sh` timeout internals in wave 1.

## Artifact contract

| Artifact | Role |
|---|---|
| `sweep/claude-code-plugins-conversion/plan.md` | this file |
| `claude-code-plugins_gate_decision.json` | Gate 0 (already committed) |
| `batch/corpora/claude-code-plugins/` + `CORPUS_MANIFESTS` | manifest corpus, not WAVE |
| `claude-code-plugins_{encodable_fraction,batch_summary}.json` + `.ndjson` | Gate 1 filter (already committed) |
| `claude-code-plugins_rank.json` | top 15 (`plugins/guardrails/hooks/` path filter) |
| harness family `AI-claude-plugins` | contracts + ≥1 mutation guard; BusyBox GT |
| `claude-code-plugins_conversion.ndjson` | ledger join |
| `claude-code-plugins_conversion_wave.md` | close-out |

## Phases (this PR = P2–P4)

P1 (gate + manifest + batch) is **already on main**. This wave is rank /
contracts / BusyBox GT / ledger join / close-out.

### P2 — Rank 15 / write ≤5

- Vocab above; drop tests/vendor. Current bucket:
  **plugin/hooks/guards** (`plugins/guardrails/hooks/`).
- Mix: 2–3 shape 1 (new alphabet only), 0–2 shape 3. A shape-3-less wave is
  allowed when remaining captures are Concat-identity — record that in the
  close-out; do not invent a tautological shape 3.
- Family `AI-claude-plugins`; `provenance=human`; mutation guard required.
- Shape-3: only if a capture can actually disagree with the source field.

### P3 — BusyBox GT + ledger join

- SAT: replay on BusyBox (`grep`/`sed`/`awk` as the site uses).
- Expected-UNSAT shape-3: differential fuzz (BusyBox vs mirror).
- Do not clone P3 GNU∩BusyBox. Empty capture is **not** truncation.
- Generate `claude-code-plugins_conversion.ndjson`; ledger `properties_asked`
  delta in **[1, 5]**.

### P4 — Close-out

- Asked / skip / next idiom or stop-cluster / next cluster named explicitly.
- Pattern-class SAT (alphabet cannot contain the witness char) →
  `wont_file`, not `private_first`.

## Risks

- **`hook-utils.sh` copies** — the same 10 sites repeat across
  `plugins/*/hooks/`. Path-filter `plugins/guardrails/hooks/` plus Gate 1
  test-filename drops; skip timeout/env-wrapper internals as `internal`.
- **Vacuous shape-3** — skill-ref `sed` group-1 vs space trailer is
  Concat-identity when the ref class cannot contain space. Prefer solid
  shape-1.
- **Disclosure** — third-party claude-code-plugins bugs are not
  auto-`private_first`; no public issue without approval.
