# OpenWrt feed admission probe — evidence (P3-A, wave #264)

**Captured:** 2026-08-12, BEFORE any P2 merge (shell dialect still unadmitted —
the `new-surface` timing rule). Final-semantics re-measure: 2026-08-12, with
the P1-frozen scanner (PR #259 merge `f48a850`).

## 1. Clone facts

| Fact | Value |
|---|---|
| Feed | `openwrt/packages.git` (feed-level unit — NOT 8,000 individual package repos) |
| Clone SHA | `e99adbc49f7a11d0377c8135fe706c7757b9e68c` |
| Clone commit | `sing-box: bump to 1.13.18 without Naive outbound support` |
| Clone date | 2026-08-12 (branch may be deleted after merge — SHA + message recorded) |
| Clone size | 94 MB (`du -sh`) |
| Depth | 1 |

## 2. Counting tool (named and scaled)

The P1 script `scripts/dogfood-singleton-analysis.py --dir` IS the probe
counter — it inherits the P1-frozen extraction semantics (`=~` unquoted,
fgrep/-F literal, `-i`→flags, sed forms, `*.init` + shebang selection) and
the `MAX_FILE_BYTES`/`--ext` bounds.

- **Pre-P2 capture** (2026-08-12, PR #259 branch @ `93f4333`, pre-guard
  scanner): 739 sites / 1,097 files scanned / 1 oversized skipped, 0.73s.
- **Final-semantics re-measure** (merged main `f48a850`, guard-fixed
  scanner — the P2.5 re-freeze proved the registered extractor reproduces
  these semantics byte-identically): **659 sites / 1,097 files / 1 oversized
  skipped**. The guards removed 80 phantom sites (mygrep/pgrep-prefixed
  commands, comment/string contexts). 659 was the interim authoritative
  count.
- **Post-reconcile count (authoritative): 713 sites / 203 files** — the P3
  reconcile exposed a REAL scanner regression in the context guard:
  `"$(cmd 'pat')"` command substitutions were suppressed as string
  literals (fixed in PR #274). The fix restored 54 real sites
  (659 → 713; 134 → 140 packages). The final reconcile (pre-P2 capture vs
  fixed registered extractor): 13 files over the 10% per-file tolerance
  (6.22%), every one a documented correction (boundary-fix phantoms
  `pgrep "$x"` → `$x`, mygrep-prefixed commands + fold corrections). NOT a
  false removal. Reconcile report:
  `openwrt-reconcile-report.json`.
- **Cumulative-review fold re-measure (final): 713 sites / 202 files /
  140 packages — NET ZERO vs the post-reconcile count.** The close-out
  zen-MCR's precision folds (heredoc bodies are data not code, `grep -P`
  rebranched, escaped sed delimiters, `sed -E` → ERE) were applied and the
  feed re-measured: the OpenWrt heredoc bodies contain NO regex patterns,
  so the corrected count is unchanged at 713 (an interim 688 measurement
  was an offset-drift artifact of the heredoc-blanking implementation —
  fixed by offset-aligned blanking). The final reconcile vs the fold-
  adjusted extractor: 13 files over tolerance (6.22%), all documented
  corrections. The merged draft + `openwrt_packages_probe_decision.json`
  carry the final 713.

Command (both runs, `LC_ALL=C`):
```
python3 scripts/dogfood-singleton-analysis.py --dir <clone> --name openwrt-packages --dry-run
python3 scripts/dogfood-singleton-analysis.py --dir <clone> --name openwrt-packages --ndjson
```
Runtime: 0.73s (4-core/8GB class; budget <5 min) · Disk: 94 MB clone +
walk (<500 MB cap).

## 3. Aggregation (per-package distribution — the <200 scale red flag override)

The gate's <200-site scale signal was designed for repo-level corpora; an
8k-package monorepo breaks its assumptions. Counts are per-package-directory,
reported as a distribution (the gate schema has no per-package field — the
distribution is a probe artifact; schema extension is follow-on if the stream
graduates):

- Packages with sites: **140** · min=**1** · median=**1** · max=**127**
  (net/pbr) · total=**713**
- Top packages: net/pbr 127, net/ddns-scripts 90, net/https-dns-proxy 46,
  net/mwan3 27, multimedia/imagemagick 17.
- Syntax surface: BRE 590 · ERE 118 · bash_ksh 5 (final fold-semantics
  split — sed -E → ERE reclassification moved 20 sites). Flag surface:
  `-i` 39.
- Full per-file export: `openwrt-feed-records-fold.ndjson` (registered
  extractor, post-guard-fix + fold semantics — the merge-probe-draft
  input; tracked in-tree). The pre-P2 frozen capture is tracked as
  `openwrt-feed-records-preP2.ndjson` — the reconcile report's
  `probe_ndjson`/`now_ndjson` fields reference the tracked files (the
  report is reproducible from the tree).

**Scale red flag explicitly OVERRIDDEN** (documented in the artifact's
`rationale`): a feed is not a repo; the scale signal is meaningless at this
granularity. GO requires total sites ≥ 1 AND ≥1 package with novel dialect
surface — both met (init scripts with grep -E/sed/BRE/awk -F patterns,
busybox-ash constructs).

## 4. Probe mechanics (recorded)

`LC_ALL=C`; `grep -a` for binary files; CRLF-tolerant counting (the P1
counter reads with `errors="replace"`); busybox-ash `[[` vs `[` vs `test`
handled by the `=~` unquoted-RHS rule (5 bash_ksh sites); Makefile
`pattern = value` false-positive avoidance — the counter extracts only
grep/sed/awk/`=~` quoted-argument forms, never Makefile assignments.

## 5. Timing / novelty honesty

The pre-P2 capture + final-semantics re-measure both predate the OpenWrt
artifact's authoring. The novelty claim is `new-surface` (posix-shell
dialect unadmitted at capture time — the shell corpus's own admission is
P2c's `dogfood_shell_gate_decision.json`, which lands in the same wave).
The artifact's `decision_basis` = `admission_conditions` with condition id
`new-surface` + this evidence; no escape_hatch (init scripts are config
parsing, a weak leg — not claimed).

## 6. Reconciliation (P3-B, post-P2.5)

After P2 lands, `scripts/reconcile_probe.py` compares the probe per-file
counts (aggregated from `--dir --ndjson`) against the registered-extractor
output, `--tolerance-pct 10`, and the tolerance report is committed HERE.

## 7. Budget partition (documented — no runner change this wave)

The OpenWrt stream is admitted to a SHARED compile budget with the GitHub
stream: a reserved pattern/wall budget for the GitHub stream before any
OpenWrt extraction/compile is admitted. The partition is the decision record
for the follow-on global gate; runner-level enforcement is follow-on.
