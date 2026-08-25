"""Wave 9 (#578): offline pre-probe skip-class surrogate.

Fit a small logistic model on the Phase 0 **train** half only. Features are
pre-probe (ledger + materialized tree). Walked ``regex_sites`` is the label
source, never a feature. Live drain stays score-v1; this module does not
roll out score-v2.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from regexproof.mine.root_dir import root_dir_deprioritized
from regexproof.mine.score_v2 import (
    V1_FEATURE_NAMES,
    _base_features,
    _scaled_log,
    _sigmoid,
    _tree_feature,
    auc,
)
from regexproof.mine.score_v2 import (
    _TREE_CONFIG_SUFFIXES,
    _TREE_JS_SUFFIXES,
    _TREE_PYTHON_SUFFIXES,
    _TREE_SHELL_SUFFIXES,
    _TREE_YARA_SUFFIXES,
)

# Predict the ≤50-site NO-GO class (the ~65% skip class from #578).
SKIP_SITE_CAP = 50
PREDECLARED_THRESHOLD = 0.5
DEFAULT_FIT_DATE = "2026-08-22"

# Slug-name tokens stand in for missing GitHub topics (ledger has none).
_SLUG_TOKENS = (
    "test",
    "tests",
    "tutorial",
    "example",
    "examples",
    "awesome",
    "demo",
    "sample",
    "playground",
    "kata",
)

SURROGATE_FEATURE_NAMES: tuple[str, ...] = (
    *V1_FEATURE_NAMES,
    "tree_complete",
    "tree_incomplete",
    "tree_boundary_true",
    "tree_boundary_false",
    "tree_path_log",
    "tree_regex_files_log",
    "tree_python",
    "tree_javascript",
    "tree_config",
    "tree_yara",
    "tree_shell",
    "tree_root_deprioritized",
    *(f"slug_{tok}" for tok in _SLUG_TOKENS),
)


def skip_class_label(status: str, regex_sites: int | None) -> int:
    """Unknown/malformed site counts are not the skip class."""
    if type(regex_sites) is not int:
        return 0
    return int(str(status) == "no-go" and regex_sites <= SKIP_SITE_CAP)


def encode_features(
    candidate: Mapping[str, Any],
    *,
    tree_feature: Mapping[str, Any] | None = None,
    today: str | None = None,
) -> dict[str, float]:
    """Pre-probe vector: v1 metadata + tree + slug tokens. No walk features."""
    out = {name: 0.0 for name in SURROGATE_FEATURE_NAMES}
    base = _base_features(dict(candidate), today=_as_date(today))
    for name in V1_FEATURE_NAMES:
        out[name] = float(base.get(name) or 0.0)

    tree = _tree_feature(candidate, tree_feature)
    complete = tree.get("complete") is True and tree.get("truncated") is not True
    out["tree_complete"] = float(complete)
    out["tree_incomplete"] = float(not complete)
    tree_boundary = str(tree.get("security_boundary") or "unknown")
    out["tree_boundary_true"] = float(tree_boundary == "deterministic-true")
    out["tree_boundary_false"] = float(tree_boundary == "deterministic-false")
    if complete:
        out["tree_path_log"] = _scaled_log(tree.get("path_count"))
        counts = tree.get("regex_file_type_counts")
        counts = counts if isinstance(counts, Mapping) else {}
        total_files = sum(max(0, int(value or 0)) for value in counts.values())
        out["tree_regex_files_log"] = _scaled_log(total_files)
        out["tree_python"] = _scaled_log(
            sum(int(counts.get(suffix) or 0) for suffix in _TREE_PYTHON_SUFFIXES)
        )
        out["tree_javascript"] = _scaled_log(
            sum(int(counts.get(suffix) or 0) for suffix in _TREE_JS_SUFFIXES)
        )
        out["tree_config"] = _scaled_log(
            sum(int(counts.get(suffix) or 0) for suffix in _TREE_CONFIG_SUFFIXES)
        )
        out["tree_yara"] = _scaled_log(
            sum(int(counts.get(suffix) or 0) for suffix in _TREE_YARA_SUFFIXES)
        )
        out["tree_shell"] = _scaled_log(
            sum(int(counts.get(suffix) or 0) for suffix in _TREE_SHELL_SUFFIXES)
        )
        out["tree_root_deprioritized"] = float(
            root_dir_deprioritized(tree.get("root_dir_names") or ())
        )

    slug = str(candidate.get("url") or "").lower()
    name = slug.rsplit("/", 1)[-1]
    for tok in _SLUG_TOKENS:
        out[f"slug_{tok}"] = float(tok in name)
    return out


def _as_date(value: str | None):
    from datetime import date

    if not value:
        return date.fromisoformat(DEFAULT_FIT_DATE)
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value)[:10])


def fit_surrogate(
    rows: Sequence[Mapping[str, Any]],
    labels: Sequence[int],
    *,
    today: str | None = None,
    iterations: int = 800,
    learning_rate: float = 0.08,
    l2: float = 0.03,
) -> dict[str, Any]:
    if len(rows) != len(labels) or not rows:
        raise ValueError("rows and labels must be non-empty and have equal length")
    names = SURROGATE_FEATURE_NAMES
    matrix = [
        [encode_features(row, tree_feature=row.get("tree_feature"), today=today)[n] for n in names]
        for row in rows
    ]
    positives = sum(1 for label in labels if label)
    negatives = len(labels) - positives
    if not positives or not negatives:
        raise ValueError("both classes are required for fitting")
    class_weights = {
        1: len(labels) / (2.0 * positives),
        0: len(labels) / (2.0 * negatives),
    }
    weights = [0.0] * len(names)
    intercept = 0.0
    count = float(len(labels))
    for step in range(max(1, int(iterations))):
        rate = learning_rate / (1.0 + 0.001 * step)
        grad_intercept = 0.0
        gradients = [l2 * w for w in weights]
        for vector, label in zip(matrix, labels):
            logit = intercept + sum(w * v for w, v in zip(weights, vector))
            error = (_sigmoid(logit) - float(label)) * class_weights[int(bool(label))]
            grad_intercept += error
            for index, value in enumerate(vector):
                gradients[index] += error * value
        scale = 1.0 / count
        intercept -= rate * grad_intercept * scale
        for index, gradient in enumerate(gradients):
            weights[index] -= rate * gradient * scale
    return {
        "feature_names": list(names),
        "intercept": intercept,
        "weights": {name: w for name, w in zip(names, weights)},
        "fitter": {
            "method": "balanced-logistic-gradient-descent",
            "iterations": int(iterations),
            "learning_rate": learning_rate,
            "l2": l2,
        },
    }


def predict_proba(row: Mapping[str, Any], model: Mapping[str, Any], *, today: str | None = None) -> float:
    names = model["feature_names"]
    weights = model["weights"]
    feats = encode_features(row, tree_feature=row.get("tree_feature"), today=today)
    logit = float(model["intercept"]) + sum(
        float(weights.get(name) or 0.0) * float(feats.get(name) or 0.0) for name in names
    )
    return _sigmoid(logit)


def evaluate_skip_rate(
    rows: Sequence[Mapping[str, Any]],
    labels: Sequence[int],
    model: Mapping[str, Any],
    *,
    threshold: float = PREDECLARED_THRESHOLD,
    today: str | None = None,
) -> dict[str, Any]:
    scores = [predict_proba(row, model, today=today) for row in rows]
    predicted = [int(s >= threshold) for s in scores]
    skip_n = sum(labels)
    flagged = sum(1 for y, p in zip(labels, predicted) if y and p)
    skip_rate = (flagged / skip_n) if skip_n else 0.0
    fp = sum(1 for y, p in zip(labels, predicted) if (not y) and p)
    tn_fp = sum(1 for y in labels if not y)
    return {
        "threshold": threshold,
        "test_n": len(labels),
        "skip_class_n": skip_n,
        "skip_class_flagged": flagged,
        "skip_rate": round(skip_rate, 6),
        "false_positive_n": fp,
        "non_skip_n": tn_fp,
        "auc": round(auc(scores, list(labels)), 6),
        "hard_reject": False,
        "note": (
            "skip_rate is recall of the ≤50-site NO-GO class at the "
            "predeclared threshold. Soft ranking only — never a hard reject."
        ),
    }
