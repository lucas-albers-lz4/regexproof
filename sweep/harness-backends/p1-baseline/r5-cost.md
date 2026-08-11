# R5 effort calibration — pre-committed vs measured (design #213 rev 7)

Measured 2026-08-11. The pre-committed thresholds were published IN THE DESIGN
(rev 7, luna-final fold — anti-backfit: the ranges existed before measurement).
Every value here is live-measured on the pinned v1.6.1 (sha256 22b19f12…464).

| Threshold | Pre-committed (rev 7) | Measured | Headroom | Verdict + mapped action |
|---|---|---|---|---|
| Cold-download cost | ≤ 2 min (40.1 MB asset) | **0.83 s** (40.1 MB @ 48.6 MB/s from the GitHub release CDN; sha256 verified on the downloaded bytes) | ~144× | PASS — action not triggered; CI downloads the pinned asset with per-run sha256 verify (P6 design unchanged) |
| Per-property process overhead | ≤ 2 s | **≈16 ms** (deep-research measurement; matrix runs 11.8–69.4 ms/property incl. solve) | ~125× | PASS — batch-reuse not triggered; per-query isolation stays the default (D2) |
| CI wall-clock increase | ≤ 15% of stock | stock proof-harness job **2m50s–3m14s** across the merged PRs' CI runs (Golden suites 3.12/3.13: 4m27s–4m41s). 15% budget ≈ **26–29 s** on the proof-harness job. Projected escalated-set cost: N × ≤70 ms (measured per-property ceiling) with N = the decomposition_exhausted + ECMA subset (corpus sweep stays manual per design P4) → bounded ≈ seconds | within budget (projected) | PASS — the P4 CI job measures the real escalated-set wall-clock and re-verifies against this threshold; exceed → reduce the escalated set (design's mapped action) |

## Measurement evidence
- **Download**: `curl -sL -o /dev/null -w %{time_total}` on
  `https://github.com/VeriFIT/z3-noodler/releases/download/v1.6.1/z3-noodler-ubuntu-24.04-x86_64-shared`
  → 0.8256 s, 48,586,021 B/s, 40,111,648 bytes, sha256 `22b19f12…464` (matches the pin).
- **Per-property overhead**: deep-research invocation timing; corroborated by the
  parity matrix (p1-baseline/matrix.json): every Noodler row 11.8–69.4 ms total
  (subprocess spawn + parse + solve).
- **CI stock times**: observed on the merged PRs #222–#226 runs (GitHub Actions
  job durations for Z3 proof harness + Golden suites on main-equivalent trees).
- **Projected escalated-set cost**: per-property ceiling × subset size — the real
  measurement lands in the P4 CI job per the threshold's re-verification clause.

## Anti-backfit statement
Thresholds were fixed in the design (rev 7) before any of these measurements
existed. All three pass with ≥125× headroom; none required a bump. The bump
procedure (design R5) remains: exceed → mapped action + maintainer approval.
