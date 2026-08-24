"""Single interval library for regexproof (#555 Wave P0).

Deterministic, seeded, and dependency-free (stdlib ``math`` / ``statistics`` /
``random`` only — the repo pins exactly one dependency, ``z3-solver``, and
adding scipy/statsmodels for two intervals would break that discipline).

Every function accepts a ``seed`` so Phase 0's frozen protocol is fully
reproducible from ``phase0_freeze.json``. Consumers MUST pass the seed from
the freeze artifact; a default seed is provided for smoke use only.

Intervals provided (each with an ``exact`` stdlib implementation):

- ``wilson_ci``        — score interval for a binomial proportion (used by the
  escape-baseline artifact and the shared-gate one-sided two-proportion test).
- ``clopper_pearson``  — exact binomial interval (precision@K, descriptive
  only per the flip rule).
- ``bootstrap_ci``     — seeded percentile / BCa bootstrap over a statistic
  function (AUC flip-rule difference distribution). Stratified resampling is
  available via ``bootstrap_stratified`` (pass ``strata``).
- ``two_proportion_test`` — one-sided Wilson two-proportion test with a FIXED
  baseline constant (the committed Phase 0 artifact value), the escape gate's
  exact predeclared decision function.

Determinism contract: same inputs + same seed ⇒ byte-identical outputs.
Never call ``random``/``time`` here without a seed.
"""

from __future__ import annotations

import math
import random
import statistics
from typing import Any, Callable, Sequence

__all__ = [
    "DEFAULT_SEED",
    "bootstrap_ci",
    "bootstrap_stratified",
    "clopper_pearson",
    "two_proportion_test",
    "wilson_ci",
]

DEFAULT_SEED = 20260822  # Phase 0 freeze date; overridden by the artifact

# ---------------------------------------------------------------------------
# Binomial intervals
# ---------------------------------------------------------------------------


def _inv_normal(p: float) -> float:
    """SIGNED lower-tail normal quantile Φ⁻¹(p) (stdlib, no scipy).

    Uses the A&S 26.2.23 rational approximation (error < 1e-8). Returns
    negative for p < 0.5, zero at p = 0.5, positive for p > 0.5."""
    # Rational approximation for the inverse normal CDF (Acklam / A&S).
    a = (
        -3.969683028665376e01,
        2.209460984245205e02,
        -2.759285104469687e02,
        1.383577518672690e02,
        -3.066479806614716e01,
        2.506628277459239e00,
    )
    b = (
        -5.447609879822406e01,
        1.615858368580409e02,
        -1.556989798598866e02,
        6.680131188771972e01,
        -1.328068155288572e01,
    )
    c = (
        -7.784894002430293e-03,
        -3.223964580411365e-01,
        -2.400758277161838e00,
        -2.549732539343734e00,
        4.374664141464968e00,
        2.938163982698783e00,
    )
    d = (
        7.784695709041462e-03,
        3.224671290700398e-01,
        2.445134137142996e00,
        3.754408661907416e00,
    )
    plow = 0.02425
    if p < plow:
        q = math.sqrt(-2.0 * math.log(p))
        x = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0
        )
    elif p <= 1.0 - plow:
        q = p - 0.5
        r = q * q
        x = (
            (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5])
            * q
            / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1.0)
        )
    else:
        q = math.sqrt(-2.0 * math.log(1.0 - p))
        x = -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0
        )
    return x


def _z(confidence: float) -> float:
    """Two-sided normal quantile magnitude for ``confidence`` (stdlib)."""
    return abs(_inv_normal((1.0 - confidence) / 2.0))


def wilson_ci(
    k: int,
    n: int,
    confidence: float = 0.95,
) -> tuple[float, float]:
    """Wilson score interval for ``k`` successes in ``n`` trials.

    Returns ``(lower, upper)``. Used by the escape-baseline artifact. The
    escape decision test itself (``two_proportion_test``) compares the window
    rate against the fixed baseline using the null SE — no continuity
    correction."""
    if n <= 0:
        raise ValueError("n must be > 0")
    if not 0 <= k <= n:
        raise ValueError("k must be in [0, n]")
    z = _z(confidence)
    p_hat = k / n
    denom = 1.0 + z * z / n
    centre = (p_hat + z * z / (2.0 * n)) / denom
    half = z * math.sqrt(p_hat * (1.0 - p_hat) / n + z * z / (4.0 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def _beta_continued_fraction(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta I_x(a, b) via continued fraction (stdlib).

    Numerical Recipes betacf port; accurate to ~1e-10 for x in (0,1)."""
    MAX_ITER = 200
    EPS = 3.0e-14
    FPMIN = 1.0e-300

    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAX_ITER + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            break
    return h


def _beta_regularized(a: float, b: float, x: float) -> float:
    """I_x(a, b) — regularized incomplete beta (stdlib)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    ln_gamma = math.lgamma
    bt = math.exp(
        ln_gamma(a + b) - ln_gamma(a) - ln_gamma(b) + a * math.log(x) + b * math.log(1.0 - x)
    )
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _beta_continued_fraction(a, b, x) / a
    return 1.0 - bt * _beta_continued_fraction(b, a, 1.0 - x) / b


def _beta_ppf(p: float, a: float, b: float) -> float:
    """Inverse regularized incomplete beta (stdlib bisection on the CDF)."""
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if _beta_regularized(a, b, mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def clopper_pearson(
    k: int,
    n: int,
    confidence: float = 0.95,
) -> tuple[float, float]:
    """Exact Clopper-Pearson binomial interval (descriptive precision@K)."""
    if n <= 0:
        raise ValueError("n must be > 0")
    if not 0 <= k <= n:
        raise ValueError("k must be in [0, n]")
    alpha = 1.0 - confidence
    if k == 0:
        lower = 0.0
    else:
        lower = _beta_ppf(alpha / 2.0, k, n - k + 1)
    if k == n:
        upper = 1.0
    else:
        upper = _beta_ppf(1.0 - alpha / 2.0, k + 1, n - k)
    return (lower, upper)


# ---------------------------------------------------------------------------
# Bootstrap
# ---------------------------------------------------------------------------


def _resample(rng: random.Random, data: Sequence[Any]) -> list[Any]:
    n = len(data)
    return [data[rng.randrange(n)] for _ in range(n)]


def bootstrap_ci(
    data: Sequence[float],
    stat: Callable[[Sequence[float]], float],
    *,
    seed: int = DEFAULT_SEED,
    n_boot: int = 10000,
    confidence: float = 0.95,
    method: str = "percentile",
) -> tuple[float, float]:
    """Seeded percentile / BCa bootstrap CI for ``stat(data)``.

    ``stat`` must be a pure function of the sample (e.g. ``statistics.mean``).
    Deterministic for a fixed seed. BCa requires the statistic to be
    computable on jackknife leave-one-out samples (used for the AUC
    flip-rule difference distribution)."""
    rng = random.Random(seed)
    observed = stat(data)
    boot = sorted(stat(_resample(rng, data)) for _ in range(n_boot))
    alpha = 1.0 - confidence
    if method == "percentile":
        lo = boot[max(0, math.floor(alpha / 2.0 * n_boot) - 1)]
        hi = boot[min(n_boot - 1, math.ceil((1.0 - alpha / 2.0) * n_boot) - 1)]
        return (lo, hi)
    if method == "bca":
        # Jackknife for the bias-correction z0 and acceleration a.
        n = len(data)
        jack = [stat([v for j, v in enumerate(data) if j != i]) for i in range(n)]
        mean_jack = statistics.fmean(jack)
        num = sum((mean_jack - j) ** 3 for j in jack)
        den = sum((mean_jack - j) ** 2 for j in jack)
        accel = num / (6.0 * den**1.5) if den else 0.0
        frac = sum(1.0 for b in boot if b < observed) / n_boot
        # z0 is the SIGNED bias-correction quantile (negative when the
        # bootstrap median sits below the observed statistic). za is the
        # positive two-sided critical value.
        z0 = _inv_normal(frac) if 0.0 < frac < 1.0 else 0.0
        za = _z(confidence)
        a1 = z0 + (z0 + za) / (1.0 - accel * (z0 + za))
        a2 = z0 + (z0 - za) / (1.0 - accel * (z0 - za))
        p1 = _normal_cdf(a1)
        p2 = _normal_cdf(a2)
        lo = boot[max(0, math.floor(min(p1, p2) * n_boot) - 1)]
        hi = boot[min(n_boot - 1, math.ceil(max(p1, p2) * n_boot) - 1)]
        return (lo, hi)
    raise ValueError(f"unknown method: {method!r}")


def _normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bootstrap_stratified(
    strata: dict[Any, Sequence[float]],
    stat: Callable[[Sequence[float]], float],
    *,
    seed: int = DEFAULT_SEED,
    n_boot: int = 10000,
    confidence: float = 0.95,
) -> tuple[float, float]:
    """Seeded stratified bootstrap: resample WITHIN each stratum, concatenate,
    evaluate ``stat`` on the pooled resample. Preserves the label mix
    (go / triage-trial / no-go) exactly like the Phase 0 stratified split."""
    rng = random.Random(seed)
    keys = list(strata)
    boot = []
    for _ in range(n_boot):
        sample: list[float] = []
        for key in keys:
            sample.extend(_resample(rng, strata[key]))
        boot.append(stat(sample))
    boot.sort()
    alpha = 1.0 - confidence
    lo = boot[max(0, math.floor(alpha / 2.0 * n_boot) - 1)]
    hi = boot[min(n_boot - 1, math.ceil((1.0 - alpha / 2.0) * n_boot) - 1)]
    return (lo, hi)


# ---------------------------------------------------------------------------
# Escape-gate decision function (predeclared, fixed baseline)
# ---------------------------------------------------------------------------


def two_proportion_test(
    k_window: int,
    n_window: int,
    baseline: float,
    *,
    one_sided: str = "smaller",
    significance: float = 0.05,
) -> dict[str, Any]:
    """One-sided Wilson two-proportion test vs a FIXED baseline constant.

    This is the escape gate's exact predeclared decision function (#550/#551
    shared gate): H0 = window rate >= baseline; H1 = window rate < baseline
    (``one_sided='smaller'``). The baseline is the committed Phase 0 artifact
    value (14.9%), treated as a FIXED constant — not a random draw — so the
    test is a one-proportion z-test of the window against the fixed null
    proportion, using the null standard error sqrt(b0*(1-b0)/n) WITH the
    1/(2n) continuity correction applied toward the null. The oracle is
    defined exactly here (stdlib, deterministic): z = (p_hat ± 1/(2n) -
    b0)/se; the named spec implementation is the continuity-corrected
    one-proportion z-test per #550 REV-6 (statsmodels' two-proportion
    wrapper has no ``correction`` parameter — the corrected oracle is this
    function).

    Final-gate #6 (MEDIUM): the correction is DECISION-RELEVANT at the
    boundary — e.g. k=3/n=50 vs baseline 0.149: uncorrected p≈0.0386
    (<0.05, fires) vs corrected p≈0.0584 (does not fire). The gate must
    match the spec.

    Returns ``{p_value, window_rate, baseline, z, fires, n_window}`` where
    ``fires`` means "admission yield too low to justify scale" and BLOCKS
    #550 Phase 2 per the shared gate."""
    if n_window <= 0:
        raise ValueError("n_window must be > 0")
    if not 0 <= k_window <= n_window:
        raise ValueError("k_window must be in [0, n_window]")
    if not 0.0 <= baseline <= 1.0:
        raise ValueError("baseline must be in [0, 1]")
    p_hat = k_window / n_window
    # Null standard error (fixed baseline proportion, not p_hat).
    se = math.sqrt(baseline * (1.0 - baseline) / n_window)
    # Continuity correction 1/(2n), applied toward the null (shrink the
    # deviation by half a trial's worth of probability mass).
    cc = 1.0 / (2.0 * n_window) if n_window > 0 else 0.0
    if one_sided == "smaller":
        z = (p_hat + cc - baseline) / se if se > 0 else 0.0
        p_value = _normal_cdf(z)  # P(Z <= z) under H0
        fires = p_value < significance
    elif one_sided == "greater":
        z = (p_hat - cc - baseline) / se if se > 0 else 0.0
        p_value = 1.0 - _normal_cdf(z)
        fires = p_value < significance
    else:
        raise ValueError(f"unknown one_sided: {one_sided!r}")
    return {
        "p_value": round(p_value, 6),
        "window_rate": round(p_hat, 6),
        "baseline": baseline,
        "z": round(z, 6),
        "fires": bool(fires),
        "n_window": n_window,
    }
