# OpenWrt packages — conversion wave 1

> **For Hermes:** execution via standard-development with per-PR luna gates.
> Design: [`docs/CLUSTER-CONVERSION.md`](../../docs/CLUSTER-CONVERSION.md).
> This plan is the first application of that SOP, not a new admission
> theory.

**Goal:** Run one conversion wave on the already-probed `openwrt/packages`
feed: register it as a **manifest** corpus (not `WAVE_CORPORA`), rank 15
boundary candidates, write **5** human contracts (2–3 shape 1, 1–2 shape 3),
ground-truth on BusyBox, and land `openwrt_packages_conversion.ndjson` so
the conversion ledger’s `properties_asked` moves.

**End state:** a logged yield (including 5 UNSAT / 0 SAT) plus skip reasons
the next cluster can reuse. Not 713 proofs. Not luci/routing/telephony/video
or the core tree. Not a public OpenWrt issue unless a human approval file
says so.

**Tech stack:** existing `shell_posix` extractor + batch (`extract_corpus`
walks `**/*` + `_is_shell_script`). Today the filter returns false as soon
as `fp.suffix` is not `.sh`/`.bash`/`.init` (unless `init.d/` is in the
path). Dogfood `--dir` shebang-sniffs **regardless of suffix**. P1 closes
that gap (below). Do **not** copy anax’s manifest `glob: **/*.sh`. Harness
registry + a **new** BusyBox checker (not `ci-check-busybox-sed.py`).
Ledger glob + `product_reportable` count rule in
`scripts/conversion-ledger.py`.

## Trust map (Gate 2 input)

OpenWrt packages ship init scripts, UCI helpers, and hotplug hooks that run
as root on the device under **BusyBox ash** + BusyBox `grep`/`sed`/`awk`
(not GNU). Trust classes for this wave:

| Trust | Typical source | Example |
|---|---|---|
| `config` | UCI / LuCI option → init script | pbr policy names, mwan3 iface, ddns service URLs |
| `untrusted-input` | WAN-facing response, user-supplied hostname/IP that is not only operator UCI | ddns IP taken from a lookup before private-range filter |
| `internal` | kernel/`ip` output, feature detect | `grep -q POINTOPOINT`, `awk '/via/'` |

Default: treat UCI-fed tokens as `config` unless the surrounding code shows
a WAN or unauthenticated path. `internal` never gets a contract.

**Vocab tokens:** `init.d`, `uci`, `nft`, `iptables`, `firewall`, `passwd`,
`ddns`, `mwan`, `banip`, `adblock`, `pbr`, `hotplug`.

**Device engine:** BusyBox 1.37.x class (pin whatever golden CI already
installs). BusyBox is the product result. GNU is logged when it can
disagree; **agreement is not required**. Absence of BusyBox is a hard fail.

## Already measured (do not re-derive)

From [`sweep/corpus-wave5/openwrt-feed-probe.md`](../corpus-wave5/openwrt-feed-probe.md)
and `properties/generated/openwrt_packages_probe_decision.json`:

| Fact | Value |
|---|---|
| Unit | `openwrt/packages.git` @ `e99adbc49f7a11d0377c8135fe706c7757b9e68c` (feed, not 8k repos) |
| Sites | **713** / 202 files / 140 packages |
| Extract | 0.73 s; clone 94 MB depth 1 |
| Density | `net/pbr` 127, `ddns-scripts` 90, `https-dns-proxy` 46, `mwan3` 27 |
| Probe decision | **GO** on `new-surface` (posix-shell unadmitted at capture). `security_boundary=unknown`. **Plan-time only** — `check_admission_gates` does not read `*_probe_decision.json`. |
| Batch | **not registered**. Follow-on from wave 5. |

posix-shell is now admitted (anax, mycelium, claude-code-plugins, …). A
**fresh** gate must **not** claim `new-surface` is still met. This wave is
conversion, not compiler novelty.

Comparable posix-shell compile: ~170–230 ms/site → **~2–3 min** for 713
sites; budgets `max_wall_s=900`, `redos_wall_s=180` (anax). Expected
encodable ~80%.

## Non-goals

- NO luci / routing / telephony / video / `openwrt/openwrt` core in this wave.
- NO `WAVE_CORPORA` membership (golden batch time). Manifest + local batch only.
- NO taint engine, no `input_source` on every extractor record (#475).
- NO synthesized shape-1/2 product rows; no auto shape-3 (#478/#479).
- NO 713 contracts; no public upstream filing without approval.
- NO re-probe of the feed unless reconcile **fails** (below). Then stop
  and fix; do not convert on a drifted inventory.

## Artifact contract

| Artifact | Produced-by | Consumed-by |
|---|---|---|
| `docs/CLUSTER-CONVERSION.md` | this wave P0 | agents, OpenClaw-class follow-ons |
| `openwrt_packages_gate_decision.json` | P1 author | `check_admission_gates` (runtime) |
| `batch/corpora/openwrt_packages/` + `CORPUS_MANIFESTS` | P1 | batch / measure |
| `openwrt_packages_{encodable_fraction,batch_summary}.json` + `.ndjson` | P1 batch | Gate 1 filter; **not** the product join. Committing the summary **requires** a conversion-ledger regen in the **same PR** (sites_extracted drift). |
| `openwrt_packages_rank.json` | P2 ranker | Gate 2 reading list |
| harness family `OW-packages` (5 properties + ≥1 mutation guard) | P3–P4 | `z3-verify --all` (proof job). Set `family="OW-packages"` on every entry including the guard — do not rely on `name.split("-")[0]` (`OW`). |
| `openwrt_packages_conversion.ndjson` | P4 | **ledger join** (properties_asked) |
| `openwrt_packages_conversion_wave.md` | P5 | stop/expand record |
| `conversion-ledger.{json,md}` | P1 regen (site counts) + P4 regen (asked) | golden `git diff --exit-code` |

The probe decision file stays. Do not overwrite it. The runtime gate is a
**new** `*_gate_decision.json`.

---

## Phase 0 — Land the SOP (docs)

**Objective:** Merge the design + this plan + index links. No corpus code.

**Files:**

- Create: `docs/CLUSTER-CONVERSION.md` (this wave)
- Create: `sweep/openwrt-conversion/plan.md` (this file)
- Modify: `README.md` layout row, `AGENTS.md` related tooling,
  `docs/CONTRACTS.md` pointer, `docs/why.md` conversion paragraph

**ACs:**

1. Design states the 15/5 caps, the 2–3 + 1–2 mix, the four “correct type”
   rules, Gate 0–3, stop/expand, ledger join via a **special-case**
   `*_conversion.ndjson` glob (generated from harness results; dual schema
   validation; not a broader `*.ndjson` scan), and #475 non-goal.
2. This plan names the pin, the 713-site reconcile **and** the
   shebang/suffix gap, BusyBox as product engine (not the P3 helper),
   P1 ledger regen with the batch summary, the runtime gate as a **copy
   of the existing GO probe decision** (not a fresh `triage-trial`), and
   “not WAVE_CORPORA.”
3. Index links exist; `lychee` on the new docs is clean.

---

## Phase 1 — Manifest + batch (scan, not prove)

**Objective:** Make `openwrt_packages` a batch corpus so Gate 1 has a live
inventory. Conversion does not start until site count reconciles.

**Runtime gate authoring (load-bearing — schema, not taste):**

`gate_decision.schema.json` will reject the naive options:

| Tempting value | Why it fails |
|---|---|
| `decision=triage-trial` | Requires `security-boundary.met=true` and `escape_hatch_applied=true`. Probe has `security_boundary=unknown`. Do not lie. |
| `decision_basis=grandfathered` | Requires `related.backfilled=true`; schema text: a **fresh** probe cannot claim grandfathered. This feed is not a pre-gate backfill. |
| `decision=go` with all `met=false` | Requires grandfathered or escape_hatch. Same traps. |

**Do this instead:** copy the existing plan-time probe artifact to
`properties/generated/openwrt_packages_gate_decision.json`. Keep
`decision=go`, `decision_basis=admission_conditions`,
`new-surface.met=true` as the **2026-08-12 admission** (posix-shell was
unadmitted at capture — that is when the condition was evaluated, and
`decision_date` already records it). This wave does **not** re-probe and
does **not** re-claim novelty today.

- Keep `security-boundary.met=false` and `large-under-saturated.met=false`.
- `corpus_pin`: `e99adbc49f7a11d0377c8135fe706c7757b9e68c` (re-pin only if
  the SHA is gone; then record the new SHA and re-count before converting).
- `related` **must** record anti-backfit provenance (do not set
  `backfilled`):
  - `probe_path`: `properties/generated/openwrt_packages_probe_decision.json`
  - `probe_sha256`: digest of the probe file bytes at copy time
  - `snapshot`: `dated-2026-08-12` (or equivalent explicit dated-snapshot
    flag)
  - `conversion_wave`: this plan path
- Byte-identical to the probe except those `related` keys (and any
  `rationale` one-liner). A test asserts the gate matches the probe aside
  from that permitted xref. Do not refresh `decision_date`.
- Rationale one-liner: runtime filename for an already-valid GO probe
  decision so `check_admission_gates` can run batch; conversion is a
  follow-on, not a new admission theory.

**Manifest:**

- `extractor`: `shell_posix`; `dialect`: `posix-shell`.
- `security_tool`: **false** (not `SECURITY_TOOL_CORPORA`).
- Budget: copy anax (`max_patterns=5000`, `max_wall_s=900`,
  `redos_wall_s=180`, `max_mem_mb=2048`, `max_disk_mb=500`).
- Glob: omit or use the registry default. `shell_posix` dispatch ignores
  glob and uses `**/*` + `_is_shell_script`. A `**/*.sh`-only glob in the
  manifest must not be mistaken for coverage of `init.d/pbr`.
- **Not** in `WAVE_CORPORA`.
- Scaffold via `scripts/scaffold-smith-corpus.py` then edit; materialize
  clone at the pin; `ln -sfn` into `batch/corpora/openwrt_packages/rules`.

**Shebang/suffix gap (load-bearing — close it in P1, do not paper over):**

Dogfood `--dir` (`_classify`) shebang-sniffs even when the suffix is
`.defaults`, `.uci`, `.uci-defaults`, `.hotplug`, `.common`, `.functions`,
`.dnsprefetch`, etc. `_is_shell_script` currently `return False` as soon as
`fp.suffix` is anything other than `.sh`/`.bash`/`.init` (unless `init.d/`
is a path segment). The probe’s `regex_sites_per_file` includes that
surface (on the order of **16 files / ~44 sites / ~6.2%** — under the 10%
aggregate stop, so a naive 713-vs-batch check **passes on a drifted pile**,
including `pbr.user.dnsprefetch`).

**Do this:** change `_is_shell_script` to shebang-sniff **regardless of
suffix**, still using the exact `_SHELL_SHEBANGS` allowlist (the #276 zsh
rejection stays). Tests: a `.defaults` file with a listed shebang is
admitted; `#!/usr/bin/zsh` is not; `init.d/` and `.sh` still admitted
without reading. After the fix, aggregate reconcile is vs **713**.

Do **not** “expect 669” unless the extract.py change is explicitly deferred
in the reconcile report with the 16 paths listed — that path is a last
resort because ranking would miss those files.

**Reconcile (both checks; either failure stops P2):**

1. **Aggregate:** `|batch_extracted − 713| / 713 > 0.10` (~72 sites) → stop.
   After the shebang fix this should be near zero.
2. **Per-file:** vs `sweep/corpus-wave5/openwrt-feed-records-fold.ndjson`,
   same 10% per-file tolerance as `scripts/reconcile_probe.py`. A **new**
   file over tolerance that is not in that documented set → stop.

Commit a reconcile report either way. Do not rank on a regressed extractor.

**ACs:**

1. `check_admission_gates` accepts the new gate file; probe file still
   validates (`tests/test_probe_decision_artifacts.py` green).
2. `python scripts/measure-corpus-fraction.py --corpus openwrt_packages
   --assert-determinism` complete_run; fraction recorded.
3. `python -m regexproof.batch --corpus openwrt_packages` complete_run
   (**no** `--with-redos` in P1). Commit `openwrt_packages.ndjson` +
   `_batch_summary.json` **and** regen `conversion-ledger.{json,md}` in
   the **same PR** (golden drift-checks `sites_extracted`). Do not land
   the summary without the regen.
4. Reconcile: **both** aggregate and per-file gates pass (see above), or
   the wave stops with a reconcile report (no P2). Shebang/suffix gap
   closed (or explicitly listed as a deferred 16-path delta — last resort).
5. Not listed in `WAVE_CORPORA`.
6. Gate JSON equals the probe aside from the permitted `related` xref;
   `probe_sha256` matches the committed probe file.
7. `tests/test_probe_decision_artifacts.py` still asserts the **probe**
   path is unchanged; a new assertion: gate file exists and
   `check_admission_gates(["openwrt_packages"])` reads
   `openwrt_packages_gate_decision.json`, not the probe file.

**Expected machine time:** clone + ~3 min compile. P1 does not run ReDoS
(`redos_wall_s` on the manifest is unused unless `--with-redos`).

---

## Phase 2 — Rank 15

**Objective:** Deterministic Gate 1–2 shortlist. No Z3. No reading yet
beyond confirming drop-rule fixtures.

**Files:**

- Create: `scripts/rank-conversion-candidates.py` (cluster-generic: NDJSON
  in, vocab tokens + drop rules, scored JSON out)
- Create: `tests/test_rank_conversion_candidates.py`
- Create: `properties/generated/openwrt_packages_rank.json` (frozen
  shortlist for this pin)

**Drop rules** (must be tested):

- path contains `tests/`, `testdata/`, or `fixtures/` (path segment, not
  substring-in-filename); name matches `*.test.sh` / `test-version.sh` /
  `run_tests.sh`
- pattern is a single `$ident` or obviously interpolated (`$IPv4_REGEX`)
- pattern is a literal with no metacharacters (feature detect)
- `call_kind=substitution` with no capture group and no charset class
  (design Gate 1 — do not let bare `s/foo/bar/` outrank charset/capture)
- unencodable if the ranker is fed inventory rows that carry a compile
  reason (optional join on inventory; if join is missing, do not drop on
  encodable — ranking still works, P3 reading drops them)

**Density-hijack fixture (load-bearing):** tests include a golden NDJSON
with many `net/pbr/tests/...` rows plus fewer real `net/pbr/files/etc/init.d/pbr`
rows. Assert every `tests/` row is dropped **before** scoring, so density
cannot outrank the init script.

**Score** per [`docs/CLUSTER-CONVERSION.md`](../../docs/CLUSTER-CONVERSION.md)
Gate 2 table + this plan’s vocab. Stable tie-break: `site` string.

**Seed attention (not a hard include):** pbr sanitizer
`sed -E 's/[. ~`!@#$%^&*()+=,<>?;:\/\\-]/_/g'`
(`net/pbr/files/etc/init.d/pbr` ~213); ddns private-IP `grep -v -E '(^0|^10\.|…)'`
(`dynamic_dns_functions.sh` ~823); mwan3 `sed -ne "s/.*dev \([^ ]*\).*/\1/p"`
(`mwan3.sh` ~74). If they survive drops they should rank. If they do not
survive, the rank JSON must say why — do not force them in.

**ACs:**

1. Ranker is deterministic; fixture NDJSON golden in tests.
2. Frozen `openwrt_packages_rank.json` has exactly 15 keep rows (or fewer
   if the pile is smaller — then convert that many, still cap 5 contracts).
3. Every dropped seed has a recorded reason.
4. Ranker does not import z3.
5. Density-hijack fixture: all `net/pbr/tests/` rows dropped before score.
6. Substitution-without-capture-or-charset rows are dropped (design Gate 1).

---

## Phase 3 — Read 15, write 5 contracts

**Objective:** Human-adopted contracts. Spike before registry.

**Steps:**

1. Read 50–150 lines around each of the 15. Apply the four “correct type”
   rules. DYNAMIC-classify interpolations.
2. Keep **at most 5**. Mix: 2–3 shape 1, 1–2 shape 3, 0–1 shape 2, zero
   shape 4/5. Do not exceed 5 in wave 1.
3. Spike with `scripts/z3-property-template.py` copies (throwaway under
   `sweep/openwrt-conversion/spikes/`, not shipped as product).
4. Register family `OW-packages` in a **new** module
   `regexproof/harness/openwrt_packages.py` imported from
   `regexproof/harness/__init__.py` (do not grow `properties.py`). Set
   `family="OW-packages"` on **every** entry including the mutation guard
   (`prop()` defaults family to `name.split("-")[0]` → `OW`). Each entry
   has `contract` with `provenance=human`, `kind` property or
   `counterexample_finder`, `input_domain=ascii` / `domain` string,
   BusyBox `ground_truth` callback on SAT kinds.
5. ≥1 mutation guard for the family (`check_mutation_coverage`).

**ACs:**

1. Five contracts validate against `property_contract.schema.json`
   (`site`, `guarantee`, `input_source`, `trust`, `declared_domain`,
   `provenance=human`). An otherwise scanner-valid incomplete contract is
   rejected in tests.
2. Mix matches the table; a shape-3-less wave is allowed only if the 15
   contained no capture sink — record that in the wave close-out, do not
   invent a shape 3.
3. Spike scripts exist and the registry properties match them (same
   guarantee / domain).
4. `product_reportable` is true on all five; false on the mutation guard.
5. `check_mutation_coverage()` passes for family `OW-packages` (≥1
   `mutation_guard`). A test asserts the family is present in `REGISTRY`.
6. `z3-verify.py --all` **unconditionally** includes the OW-packages
   family (imported from `regexproof.harness.__init__`). Golden `Z3 proof
   harness` runs `--all`; no optional skip. Timeouts stay 30 s; shape 1
   should be instant.

---

## Phase 4 — Ground-truth, ledger join

**Objective:** Device fidelity + visible conversion numerator.

**BusyBox (do not clone P3):**

`p3_ground_truth_dual` / `ci-check-busybox-sed.py` are the **wrong**
contract: they require GNU∩BusyBox agreement, treat busybox-absent as a
recorded flag (harness still PASSes if GNU reproduced), and are sed-only.
OW product engine is BusyBox. GNU is logged; disagreement is a delta, not
a GT fail. Absence of BusyBox is a hard fail for OW properties.

- SAT: `--require-ground-truth` callbacks replay on **BusyBox**
  `grep`/`sed`/`awk` as appropriate. Log GNU. Do not require agreement.
- Expected-UNSAT shape-3: **differential fuzz** (BusyBox tool vs mirror),
  not witness replay (`ground_truth` callbacks do not run on UNSAT).
- Add `scripts/ci-check-busybox-openwrt.py`. Fail closed on
  `busybox_absent`. Dispatch by tool; do not call the P3 helper.
- **`.github/workflows/ci.yml` (required file):**
  - **Z3 proof harness:** install busybox (same `apt-get` as golden). OW
    stays on `--all` (Luna). Add `--require-contract` (existing P1–P6
    already qualify). Without busybox in this job, OW GT GNU-only-collapses
    in the required proof check.
  - **Golden:** named step `BusyBox OpenWrt dual replay` runs the new
    script (E2 sibling). Local/dev without busybox must not skip-pass.

**Ledger join:**

- Special-case glob **only** `*_conversion.ndjson`. Count a row as
  `properties_asked` only if `product_reportable` is true,
  `provenance=human`, `synthesized` absent/false. `agent_derived` and
  contract-less product kinds must **not** increment (test that).
- **Generate** the file from harness `run_one` records. Map harness
  `ground_truth` string → scanner `ground_truth_status`. Require scanner
  top-level `domain`. Fail-closed drift test.
- Batch must not write this filename.
- Regen `conversion-ledger.{json,md}` again (properties_asked bump). P1
  already regenerated for `sites_extracted`.
- Tests: (a) `product_reportable` fixture increments asked without a
  batch summary; (b) incomplete / `agent_derived` contract is rejected.

**ACs:**

1. Proof job in `ci.yml` installs busybox, runs
   `z3-verify.py --all --require-ground-truth --require-domain
   --require-contract --fail-on-property-failure`. Tests assert family
   `OW-packages` is in `REGISTRY` and selected by `--all`. SAT
   `counterexample_finder` rows have GT PASS on BusyBox.
2. Ledger `properties_asked` increase is in **[1, 5]** — never pad, never
   exceed 5 in wave 1.
3. Named golden step + proof-job busybox install: busybox absence is a
   hard fail. Both GNU and BusyBox verdicts are **recorded** on SAT; they
   need not agree. Expected-UNSAT shape-3 has a differential-fuzz AC, not
   a witness-replay AC.
4. No `would_open_public_upstream_issue=true`.
5. Conversion NDJSON is generated from harness results; drift test green;
   `product_reportable` is the count gate.

---

## Phase 5 — Close-out

**Objective:** Stop or expand, written down.

Write `properties/generated/openwrt_packages_conversion_wave.md`:

- 15 read, 5 asked, results, skip reasons (the reusable part)
- stop vs +5, with the design’s rule cited
- “next cluster not started”

**ACs:**

1. Close-out exists and names stop or expand.
2. Expand (if any) is a **new** child plan, not silent extra properties in
   this PR.
3. `docs/conversion-upstream.jsonl` gains a row only for filed / wont_file /
   false_positive last-mile events — not for UNSAT-holds.

---

## Suggested PR carving

| PR | Phase | Notes |
|---|---|---|
| A | P0 | docs only; this file + design + indexes |
| B | P1 | gate + shebang-filter fix + manifest + batch artifacts + **ledger regen**; luna + Bugbot |
| C | P2 | ranker + frozen shortlist |
| D | P3–P5 | contracts, BusyBox checker, `ci.yml` proof-job busybox + `--require-contract`, ledger glob/count, close-out — split if D is large |

Non-trivial PRs follow `.cursor/rules/pr-bugbot-before-merge.mdc`: required
verify job **names** present and green, then Bugbot on branch changes,
then merge. Do not wait on human CODEOWNERS for this cycle.

## Risks / traps

- **`new-surface` vs today:** posix-shell is now admitted. The runtime gate
  is a dated copy of the 2026-08-12 probe GO, not a re-claim that shell is
  novel in 2026-08-17. Do not refresh `decision_date` without re-evaluating
  conditions. Do not use `triage-trial` without a true security-boundary.
- **Glob vs filter:** `shell_posix` ignores manifest glob. Suffix-early
  return currently drops `--dir` shebang files (`.defaults`, `.uci`, …).
  P1 closes that or documents the 16-path delta — do not treat 6.2% as a
  pass.
- **Ledger invisibility / smoke:** harness-only rows do not count. P4’s
  glob is necessary; `product_reportable` + `provenance=human` is the
  count gate. Committing `_batch_summary.json` without ledger regen fails
  golden `sites_extracted` drift.
- **BusyBox ≠ P3 helper:** agreement-required GNU∩BusyBox is usrmanage
  P3, not OpenWrt device fidelity. Proof job must install busybox if OW
  is on `--all`.
- **Test scripts in the pile:** pbr/https-dns-proxy carry many sites under
  `tests/` — Gate 1 must drop them or the ranker will prefer density over
  boundary.
- **DYNAMIC `$IPv4_REGEX`:** prove the constant definition if present;
  proving the `grep -E "$IPv4_REGEX"` call site is not a property.
- **Formulation bugs:** read the sink. Do not ask “no `=` in values” when
  the code embeds `key=value` inside a field (usrmanage P5).
- **Disclosure:** third-party OpenWrt bugs are not scanner
  `private_first` by default; still do not file public issues from this
  wave without a human approval file.

## Open questions (resolve in P1 authoring, not by expanding scope)

1. **Closed:** runtime gate is a copy of the 2026-08-12 GO probe decision
   (`admission_conditions` / `new-surface.met=true` at `decision_date`),
   with `related` probe path + sha256 + dated-snapshot (not `backfilled`).
2. **Closed:** OW-packages **is** in `REGISTRY` and in proof-job `--all`.
   Proof job **installs busybox**. Timeouts stay 30 s; shape 1 should be
   instant.
3. Re-pin if `e99adbc` is unreachable: allowed, but forces a re-count
   before P2.

## Review folds

- **Luna (2026-08-17):** blocking — conversion glob is a special-case
  `*_conversion.ndjson` only; dual schema validation + `provenance=human`;
  NDJSON generated from harness results with drift test; OW-packages
  unconditionally in `--all`. Fold-required — probe sha256 / dated-snapshot
  `related`; named BusyBox CI step; `fixtures/` + `net/pbr/tests/` density
  fixture; aggregate **and** per-file reconcile; mutation-coverage AC.
  Keep: no `triage-trial` without security-boundary; no `grandfathered`
  without `backfilled`; never pad with smoke.
- **Grok (2026-08-17):** blocking — P1 batch summary must regen the ledger
  in the same PR; conversion count requires `product_reportable` (kind
  alone counts smoke); BusyBox is the product engine (do not clone P3
  agreement-required sed helper; proof job must install busybox; UNSAT
  shape-3 = differential fuzz); `_is_shell_script` suffix-early-return
  drops ~44 `--dir` sites under the 10% stop — close the shebang gap.
  Non-blocking folded: write-5 is `[1, 5]`; scanner `domain` +
  `ground_truth_status`; substitution drop rule; `--require-contract` on
  the proof job; probe-vs-gate test; `family="OW-packages"`; no ReDoS in
  P1. Keep: dated GO probe copy is schema-valid; not `WAVE_CORPORA`.

