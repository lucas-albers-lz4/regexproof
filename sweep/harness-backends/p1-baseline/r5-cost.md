# R5 effort calibration — pre-committed vs measured (design #213 rev 7)

Measured 2026-08-11. The pre-committed thresholds were published IN THE DESIGN
(rev 7, luna-final fold — anti-backfit: the ranges existed before measurement).
The download and per-property-overhead values are live-measured on the pinned
v1.6.1 (sha256 22b19f12…464); the CI row combines MEASURED stock job times with a
PROJECTED escalated-set cost (labeled as such — the real CI increase is measured
in the P4 job).

| Threshold | Pre-committed (rev 7) | Measured | Headroom | Verdict + mapped action |
|---|---|---|---|---|
| Cold-download cost | ≤ 2 min (40.1 MB asset) | **0.83 s** (40.1 MB @ 48.6 MB/s from the GitHub release CDN; sha256 verified on the downloaded bytes) | ~144× | PASS — action not triggered; CI downloads the pinned asset with per-run sha256 verify (P6 design unchanged) |
| Per-property cost | ≤ 2 s | **overhead ≈16 ms** (deep-research per-invocation timing) and **total per-property cost 11.8–69.4 ms** (matrix rows: subprocess spawn + parse + solve — the solve dominates the range) | ~29× (total) to ~125× (overhead) | PASS — batch-reuse not triggered; per-query isolation stays the default (D2) |
| CI wall-clock increase | ≤ 15% of stock | stock proof-harness job **2m50s–3m14s** across the merged PRs' CI runs (Golden suites 3.12/3.13: 4m27s–4m41s). 15% budget ≈ **26–29 s** on the proof-harness job. Projected escalated-set cost: N × ≤70 ms (measured per-property ceiling) with N = the decomposition_exhausted + ECMA subset (corpus sweep stays manual per design P4) → bounded ≈ seconds | within budget (projected) | PASS — the P4 CI job measures the real escalated-set wall-clock and re-verifies against this threshold; exceed → reduce the escalated set (design's mapped action) |

## Measurement evidence
- **Download timing**: `curl -sL -o /dev/null -w %{time_total}` on
  `https://github.com/VeriFIT/z3-noodler/releases/download/v1.6.1/z3-noodler-ubuntu-24.04-x86_64-shared`
  → 0.8256 s, 48,586,021 B/s, 40,111,648 bytes.
- **Download integrity (separate file-based run)**: `curl -sL -o /tmp/ndl_cold.bin
  <same URL>` then `sha256sum /tmp/ndl_cold.bin` → `22b19f12…464` (matches the
  pin; temp file deleted after verification).
- **Per-property overhead**: deep-research per-invocation timing (~16 ms for
  spawn + parse on a trivial query — distinct from solve time).
- **Total per-property cost**: the parity matrix (p1-baseline/matrix.json) rows —
  every Noodler row 11.8–69.4 ms total (subprocess spawn + parse + solve; the
  solve dominates the range).
- **CI stock times**: observed on the merged PRs #222–#226 runs (GitHub Actions
  job durations for Z3 proof harness + Golden suites on main-equivalent trees).
- **Projected escalated-set cost**: per-property total ceiling (≤70 ms measured)
  × subset size — the real measurement lands in the P4 CI job per the threshold's
  re-verification clause.

## Anti-backfit statement
Thresholds were fixed in the design (rev 7) before any of these measurements
existed. The download leg passes with ~144× headroom and the per-property leg with
~29×–125× (total/overhead); the CI leg is projected within budget and is
re-verified with real wall-clock numbers in the P4 CI job. No threshold required a
bump. The bump procedure (design R5) remains: exceed → mapped action + maintainer
approval.
