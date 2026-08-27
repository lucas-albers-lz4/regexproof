# mycelium0/mycelium — conversion wave 1

> Design: [`docs/CLUSTER-CONVERSION.md`](../../docs/CLUSTER-CONVERSION.md).
> Prior cluster close-out:
> [`properties/generated/aidevops_conversion_wave.md`](../../properties/generated/aidevops_conversion_wave.md)
> (posix-shell hooks done; ECMA plugins deferred). Next cluster = mycelium
> control-plane fail-closed guards.

**Goal:** Convert one **posix-shell** cluster from `mycelium0/mycelium`
(AmneziaWG / REALITY node control plane under `control/`, not
`tests/conformance`). Rank 15, write ≤5 human contracts, ground-truth on
**BusyBox** (product engine), emit `mycelium_conversion.ndjson` so
`properties_asked` moves.

**End state:** logged yield + skip deny-list. Not every `scripts/`
bootstrap file. Not mixed into family `OW-packages` / `OW-luci` /
`AI-aidevops`. Not `WAVE_CORPORA`. No public mycelium filing without a
human approval file.

Gate+Smith GO and batch already landed (fraction **0.8105**). Manifest
`CORPUS_MANIFESTS["mycelium"]` exists — do **not** re-batch or copy gate.

## Trust map (Gate 2 input)

mycelium is a mesh-networking node control plane: POSIX shell libraries
under `control/` that render AmneziaWG configs, harden sshd/ufw, pick a
REALITY donor, rotate transports, and self-test liveness. Wave 1 is
**posix-shell `control/` only** — `tests/conformance` is Gate 1 drop;
`scripts/` bootstrap is a later path-slice. Trust classes:

| Trust | Typical source | Example |
|---|---|---|
| `untrusted-input` | Donor TLS handshake bytes, operator-forced donor host, client NAME at `--awg-issue` | ALPN h2 line, awg-issue NAME glob |
| `config` | Live `awg0.conf`, effective `sshd -T`, operator params / identity state | dialect-line count, AllowedIPs last octet, authorized_keys prefix |
| `internal` | Feature detect, version pin skip, test fixtures, i18n | `tests/conformance/**`, `sing-box version` parse, empty-line counters |

Default: treat control-plane fail-closed validators as `config` unless the
surrounding code shows argv / handshake / remote ingest. `internal` never
gets a contract.

**Vocab tokens:** `control/`, `awg`, `failsafe`, `failclosed`, `rotate`,
`render`, `selftest`, `gated`.

**Product engine:** BusyBox ash + BusyBox `grep`/`sed`/`awk` (same pin
golden CI already installs). BusyBox is the product result. GNU is **not**
consulted. Absence of BusyBox is a hard fail. Dispatch by tool (`grep -E`
for search sites; `sed -E` for substitution captures as at the call site —
not sed-for-bash-`=~`). Node `RegExp` / Go `regexp` are **not** the product
engine here.

**Dialect / extractor:** `posix-shell` via `shell_posix`. Do **not** claim
`new-surface` — posix-shell is already admitted. This wave is
**conversion**, not compiler novelty. Admission basis:
**large-under-saturated** (1,029 posix-shell sites; fraction 0.8105).

**Family:** `MY-mycelium`. Same `family=` on every property including the
mutation guard.

**Exclude:** `tests/`, `tests/conformance`, fixtures. Gate 1 still drops
those before ranking even if a clone materialize allowlist is broader.

## Already measured (Gate 0 — admit done)

From `properties/generated/mycelium_gate_decision.json` +
`mycelium_smith_decision.json` + `mycelium_encodable_fraction.json`:

| Fact | Value |
|---|---|
| Unit | `mycelium0/mycelium` @ `4b53dc7629ca3bc88bf5467db481ad2af7130711` |
| Sites | **1,040** probe / **1,029** posix-shell / 11 re2 |
| Density | `control/` 97 sites (wave-1 bucket); `tests/conformance` dominates the rest |
| Probe + Smith | **GO**. `new-surface=false`. Batch fraction **0.8105** (834/1029). |
| Manifest | `CORPUS_MANIFESTS["mycelium"]` already registered — **do not re-batch**. |

posix-shell is already admitted. A **fresh** gate must **not** claim
`new-surface` is still met.

## Non-goals

- NO re-asking aidevops / OpenWrt / LuCI idioms (hostname / JSON `[^"]*` /
  digit-semicolon / brief t-ID).
- NO mixing Go `internal/diag` redact or re2 into family `MY-mycelium`.
- NO `WAVE_CORPORA` membership.
- NO taint engine; NO synthesized shape-1/2 product rows.
- NO public upstream filing without approval.
- NO `tests/conformance/**` in wave 1.

## Artifact contract

| Artifact | Role |
|---|---|
| `sweep/mycelium-conversion/plan.md` | this file |
| `mycelium_gate_decision.json` | Gate 0 (already committed) |
| `batch/corpora/mycelium/` + `CORPUS_MANIFESTS` | manifest corpus, not WAVE |
| `mycelium_{encodable_fraction,batch_summary}.json` + `.ndjson` | Gate 1 filter (already committed) |
| `mycelium_rank.json` | top 15 (`control/` path filter) |
| harness family `MY-mycelium` | contracts + ≥1 mutation guard; BusyBox GT |
| `mycelium_conversion.ndjson` | ledger join |
| `mycelium_conversion_wave.md` | close-out |

## Phases (this PR = P2–P4)

P1 (gate + manifest + batch) is **already on main**. This wave is rank /
contracts / BusyBox GT / ledger join / close-out.

### P2 — Rank 15 / write ≤5

- Vocab above; drop tests/vendor. Current bucket:
  **control-plane fail-closed guards** (`control/`).
- Mix: 2–3 shape 1 (new alphabet only), 1–2 shape 3, 0–1 shape 4 if an
  escaper is in the bucket. A shape-3-less wave is allowed when remaining
  captures are Concat-identity — record that in the close-out; do not
  invent a tautological shape 3.
- Family `MY-mycelium`; `provenance=human`; mutation guard required.
- Shape-3: only if a capture can actually disagree with the source field.
  AllowedIPs last-octet `Concat(octet, "/", mask)` is Concat-identity
  (octet is digits; no slash) — skip, do not file.

### P3 — BusyBox GT + ledger join

- SAT: replay on BusyBox (`grep`/`sed`/`awk` as the site uses).
- Expected-UNSAT shape-3: differential fuzz (BusyBox vs mirror).
- Do not clone P3 GNU∩BusyBox. Empty capture is **not** truncation.
- Generate `mycelium_conversion.ndjson`; ledger `properties_asked`
  delta in **[1, 5]**.

### P4 — Close-out

- Asked / skip / next idiom or stop-cluster / next cluster named explicitly.
- Pattern-class SAT (alphabet cannot contain the witness char) →
  `wont_file`, not `private_first`.

## Risks

- **`tests/conformance` inflation** — Gate 1 drops `tests/` before ranking;
  materialize may need `--allowlist-file` because the probe file list
  starts with `tests/`.
- **IPv4 last-octet vs charset deny-list** — last-octet `([0-9]+)/` is
  Concat-identity, not a charset re-ask and not a sound shape 3. Skip it.
- **Disclosure** — third-party mycelium bugs are not auto-`private_first`;
  no public issue without approval.
