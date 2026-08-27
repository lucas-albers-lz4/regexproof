"""Wave P0 (#555): intervals.py determinism + escape-gate decision function.

The single interval library must be seeded-deterministic and the escape-gate
decision function must match the predeclared protocol (#550/#551 shared gate:
one-sided z-test vs the FIXED Phase 0 baseline, fires when p < 0.05)."""

from __future__ import annotations

import statistics
from typing import Sequence

import pytest

from regexproof.stats.intervals import (
    DEFAULT_SEED,
    bootstrap_ci,
    bootstrap_stratified,
    clopper_pearson,
    two_proportion_test,
    wilson_ci,
)

BASELINE = 121 / 864  # committed Phase 0 escape baseline ≈ 14.0% (deduped; +20 NO-GO 2026-08-27)


def test_wilson_ci_escape_baseline():
    lo, hi = wilson_ci(121, 864)
    # Design pins ~[11.8%, 16.5%] for the 121/864 baseline.
    assert lo == pytest.approx(0.1185, abs=0.001)
    assert hi == pytest.approx(0.1648, abs=0.001)


def test_wilson_ci_edges():
    assert wilson_ci(0, 10)[0] == 0.0
    assert wilson_ci(10, 10)[1] == 1.0
    with pytest.raises(ValueError):
        wilson_ci(11, 10)


def test_clopper_pearson_exact_edges():
    assert clopper_pearson(0, 10)[0] == 0.0
    assert clopper_pearson(10, 10)[1] == 1.0
    lo, hi = clopper_pearson(5, 100)
    assert 0.0 < lo < 0.05 < hi < 0.2


def test_bootstrap_ci_is_seed_deterministic():
    data = [1.0] * 127 + [0.0] * 726
    a = bootstrap_ci(data, statistics.mean, seed=42, n_boot=2000)
    b = bootstrap_ci(data, statistics.mean, seed=42, n_boot=2000)
    assert a == b
    c = bootstrap_ci(data, statistics.mean, seed=43, n_boot=2000)
    assert a != c  # different seed → different resample (statistically certain)


def test_bootstrap_bca_interval_is_ordered():
    """BCa must return an ascending (lo, hi) interval. Regression test for the
    sign bug where _z(abs) collapsed z0 and inverted the endpoints."""
    data = [1.0] * 127 + [0.0] * 726
    lo, hi = bootstrap_ci(
        data, statistics.mean, seed=42, n_boot=2000, method="bca"
    )
    assert lo <= hi
    # The interval must be a plausible CI around the observed mean (0.1489).
    assert 0.10 < lo < 0.1489 < hi < 0.20


def test_bootstrap_stratified_preserves_strata():
    strata: dict[str, Sequence[float]] = {
        "go": [1.0] * 10,
        "triage": [1.0] * 5,
        "no": [0.0] * 50,
    }
    lo, hi = bootstrap_stratified(strata, statistics.mean, seed=7, n_boot=500)
    # All resamples keep the 15/65 positive mix → mean is constant.
    assert lo == pytest.approx(15 / 65)
    assert hi == pytest.approx(15 / 65)


def test_escape_fires_below_baseline():
    # 5/100 ≈ 5% vs 14.9% baseline → p ≈ 0.003 < 0.05 → FIRES (blocks scale).
    t = two_proportion_test(k_window=5, n_window=100, baseline=BASELINE)
    assert t["fires"] is True
    assert t["p_value"] < 0.05


def test_escape_does_not_fire_at_or_above_baseline():
    # 15/100 ≈ 15% ≈ baseline → does not fire.
    t = two_proportion_test(k_window=15, n_window=100, baseline=BASELINE)
    assert t["fires"] is False
    # 50/100 well above baseline → does not fire.
    t2 = two_proportion_test(k_window=50, n_window=100, baseline=BASELINE)
    assert t2["fires"] is False


def test_escape_continuity_correction_boundary():
    """CodeRabbit #583: the correction is decision-relevant at the gate's
    own committed baseline — k=3/n=50 vs BASELINE (121/864): uncorrected
    p≈0.0514 (<0.05 borderline) vs corrected p≈0.0768 (does NOT fire)."""
    t = two_proportion_test(k_window=3, n_window=50, baseline=BASELINE)
    assert t["fires"] is False
    assert t["p_value"] == pytest.approx(0.076755, abs=1e-6)  # corrected oracle
    # Sanity: without the correction the same input is borderline (0.051446).
    se = (0.06 - BASELINE) / ((BASELINE * (1.0 - BASELINE) / 50) ** 0.5)
    from regexproof.stats.intervals import _normal_cdf

    assert _normal_cdf(se) == pytest.approx(0.051446, abs=1e-6)


def test_escape_respects_n_floor_and_predeclared_shape():
    # The gate needs n >= 50 or two consecutive windows — at n=10 the test is
    # UNDERpowered (0/10 vs baseline: z = -1.32, p ≈ 0.09, does not fire),
    # which is exactly why the design sets the n-floor. At n=50 the same
    # observed rate fires. The function computes the decision; callers enforce
    # the floor (documented in the shared gate).
    t_small = two_proportion_test(k_window=0, n_window=10, baseline=BASELINE)
    assert t_small["fires"] is False  # underpowered at n < floor
    t_floor = two_proportion_test(k_window=0, n_window=50, baseline=BASELINE)
    assert t_floor["fires"] is True  # n = floor → fires
    assert t_floor["n_window"] == 50


def test_default_seed_is_fixed():
    # Phase 0 freeze date; changing it silently would break reproducibility
    # of every artifact that omits an explicit seed.
    assert DEFAULT_SEED == 20260822
