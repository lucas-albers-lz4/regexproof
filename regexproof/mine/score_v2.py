"""Pure-Python score-v2 fitter and feature encoder.

The module deliberately has no numerical or machine-learning dependencies.
The JSON weight file is an input artifact; scoring never writes a score back
to a candidate or to disk.
"""

from __future__ import annotations

import json
import math
import random
from datetime import date
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping, Sequence

from regexproof.admission.boundary import BoundarySignals, classify_boundary
from regexproof.mine.exclusions import normalize_repo_url

# Feature helpers live in features.py so v1/v2 do not import each other's
# private score helpers. score.py still lazy-imports this module for v2.
from regexproof.mine.features import (
    _query_family,
    _recency_points,
    _repo_slug,
    _stars_points,
)

SCHEMA_VERSION = "1"
DEFAULT_SEED = 432
DEFAULT_FIT_DATE = date(2026, 8, 13)
POSITIVE_MAPPINGS = {
    "go-only": frozenset({"go"}),
    "go-or-triage-trial": frozenset({"go", "triage-trial"}),
}

V1_FEATURE_NAMES = (
    "boundary_true",
    "boundary_false",
    "family_security",
    "family_rules",
    "family_validators",
    "family_testdata",
    "family_other",
    "stars_points",
    "recency_points",
    "capped",
)

_LANGUAGE_FEATURES = (
    "python",
    "javascript",
    "typescript",
    "go",
    "rust",
    "java",
    "c_cpp",
    "csharp",
    "php",
    "ruby",
    "shell",
    "other",
)

V2_FEATURE_NAMES = V1_FEATURE_NAMES + (
    "enrich_fork",
    "enrich_fork_missing",
    "enrich_archived",
    "enrich_archived_missing",
    "enrich_size_log",
    "enrich_size_missing",
    "enrich_language_missing",
    *(f"enrich_language_{name}" for name in _LANGUAGE_FEATURES),
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
    "probe_regex_sites_log",
    "probe_boundary_true",
    "probe_boundary_false",
    "probe_dialect_count_log",
    "probe_bucket_count_log",
)

_FAMILIES = ("security", "rules", "validators", "testdata", "other")
_TREE_CONFIG_SUFFIXES = frozenset({".cfg", ".conf", ".hcl", ".ini", ".json", ".toml", ".yaml", ".yml"})
_TREE_JS_SUFFIXES = frozenset({".js", ".jsx", ".mjs", ".ts", ".tsx"})
_TREE_PYTHON_SUFFIXES = frozenset({".py"})
_TREE_SHELL_SUFFIXES = frozenset({".bash", ".ksh", ".sh", ".zsh"})
_TREE_YARA_SUFFIXES = frozenset({".yar", ".yara"})


def feature_names(feature_set: str = "v2") -> tuple[str, ...]:
    """Return the frozen feature names for the requested model variant."""
    if feature_set == "v1":
        return V1_FEATURE_NAMES
    if feature_set == "v2":
        return V2_FEATURE_NAMES
    raise ValueError(f"unknown score-v2 feature set: {feature_set!r}")


def _as_date(value: date | str | None) -> date:
    if value is None:
        return DEFAULT_FIT_DATE
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value)[:10])


def _boundary_for_candidate(candidate: Mapping[str, Any]) -> str:
    slug = _repo_slug(str(candidate.get("url") or ""))
    repo_name = slug.split("/")[-1] if slug else ""
    return classify_boundary(BoundarySignals(repo_name=repo_name))


def _probe(candidate: Mapping[str, Any]) -> Mapping[str, Any]:
    value = candidate.get("probe")
    if isinstance(value, Mapping):
        return value
    value = candidate.get("_probe")
    return value if isinstance(value, Mapping) else {}


def _tree_feature(candidate: Mapping[str, Any], supplied: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if supplied is not None:
        return supplied
    value = candidate.get("tree_probe")
    if isinstance(value, Mapping):
        return value
    value = candidate.get("_tree_probe")
    return value if isinstance(value, Mapping) else {}


def _language_key(value: Any) -> str:
    language = str(value or "").strip().lower()
    if not language:
        return "other"
    if language in {"python", "python 3"}:
        return "python"
    if language in {"javascript", "node", "node.js"}:
        return "javascript"
    if language in {"typescript"}:
        return "typescript"
    if language in {"go", "golang"}:
        return "go"
    if language in {"rust"}:
        return "rust"
    if language in {"java", "kotlin", "scala"}:
        return "java"
    if language in {"c", "c++", "objective-c", "objective-c++"}:
        return "c_cpp"
    if language in {"c#", "csharp"}:
        return "csharp"
    if language in {"php"}:
        return "php"
    if language in {"ruby"}:
        return "ruby"
    if language in {"shell", "shellscript", "powershell"}:
        return "shell"
    return "other"


def _scaled_log(value: Any, divisor: float = 10.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        number = 0.0
    return math.log1p(max(0.0, number)) / divisor


def _base_features(candidate: Mapping[str, Any], *, today: date) -> dict[str, float]:
    boundary = _boundary_for_candidate(candidate)
    family = _query_family(str(candidate.get("source_query") or ""))
    out = {name: 0.0 for name in V1_FEATURE_NAMES}
    out["boundary_true"] = float(boundary == "deterministic-true")
    out["boundary_false"] = float(boundary == "deterministic-false")
    out[f"family_{family if family in _FAMILIES else 'other'}"] = 1.0
    # Keep the v1 point definitions, but put continuous fields on a compact
    # scale for the fixed-step fitter. The categorical boundary signal is not
    # scaled, preserving its decision-boundary semantics.
    out["stars_points"] = _stars_points(int(candidate.get("stars") or 0)) / 25.0
    out["recency_points"] = _recency_points(str(candidate.get("pushed_date") or ""), today=today) / 15.0
    out["capped"] = float(bool(candidate.get("capped")))
    return out


def candidate_features(
    candidate: Mapping[str, Any],
    *,
    feature_set: str = "v2",
    today: date | str | None = None,
    tree_feature: Mapping[str, Any] | None = None,
) -> dict[str, float]:
    """Encode one ledger/rank candidate using the frozen v1 or v2 schema."""
    today_date = _as_date(today)
    out = _base_features(candidate, today=today_date)
    if feature_set == "v1":
        return {name: out[name] for name in V1_FEATURE_NAMES}
    if feature_set != "v2":
        raise ValueError(f"unknown score-v2 feature set: {feature_set!r}")

    for name in V2_FEATURE_NAMES:
        out.setdefault(name, 0.0)

    fork = candidate.get("fork")
    out["enrich_fork"] = float(fork is True)
    out["enrich_fork_missing"] = float(fork is None)
    archived = candidate.get("archived")
    out["enrich_archived"] = float(archived is True)
    out["enrich_archived_missing"] = float(archived is None)
    size = candidate.get("size")
    out["enrich_size_log"] = _scaled_log(size)
    out["enrich_size_missing"] = float(size is None)
    language = candidate.get("language")
    out["enrich_language_missing"] = float(language is None)
    out[f"enrich_language_{_language_key(language)}"] = 1.0

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
        out["tree_python"] = _scaled_log(sum(int(counts.get(suffix) or 0) for suffix in _TREE_PYTHON_SUFFIXES))
        out["tree_javascript"] = _scaled_log(sum(int(counts.get(suffix) or 0) for suffix in _TREE_JS_SUFFIXES))
        out["tree_config"] = _scaled_log(sum(int(counts.get(suffix) or 0) for suffix in _TREE_CONFIG_SUFFIXES))
        out["tree_yara"] = _scaled_log(sum(int(counts.get(suffix) or 0) for suffix in _TREE_YARA_SUFFIXES))
        out["tree_shell"] = _scaled_log(sum(int(counts.get(suffix) or 0) for suffix in _TREE_SHELL_SUFFIXES))

    probe = _probe(candidate)
    out["probe_regex_sites_log"] = _scaled_log(probe.get("regex_sites"))
    out["probe_boundary_true"] = float(str(probe.get("security_boundary") or "unknown") == "deterministic-true")
    out["probe_boundary_false"] = float(str(probe.get("security_boundary") or "unknown") == "deterministic-false")
    dialects = probe.get("dialect_counts")
    dialects = dialects if isinstance(dialects, Mapping) else {}
    out["probe_dialect_count_log"] = _scaled_log(sum(int(value or 0) for value in dialects.values()))
    buckets = probe.get("predicted_buckets")
    buckets = buckets if isinstance(buckets, Mapping) else {}
    out["probe_bucket_count_log"] = _scaled_log(sum(int(value or 0) for value in buckets.values()))
    return {name: out[name] for name in V2_FEATURE_NAMES}


def row_candidate(row: Mapping[str, Any]) -> dict[str, Any]:
    """Convert one gate-label row to the candidate shape used by the scorer."""
    ledger = row.get("ledger")
    candidate: dict[str, Any] = dict(ledger) if isinstance(ledger, Mapping) else {}
    candidate["url"] = str(row.get("url") or candidate.get("url") or "")
    probe = row.get("probe")
    if isinstance(probe, Mapping):
        candidate["probe"] = dict(probe)
        tree = probe.get("tree_probe")
        if isinstance(tree, Mapping):
            candidate["tree_probe"] = dict(tree)
    return candidate


def _sigmoid(value: float) -> float:
    if value >= 0:
        e = math.exp(-min(value, 700.0))
        return 1.0 / (1.0 + e)
    e = math.exp(max(value, -700.0))
    return e / (1.0 + e)


def fit_logistic(
    rows: Sequence[Mapping[str, Any]],
    labels: Sequence[int],
    *,
    feature_set: str = "v2",
    today: date | str | None = None,
    iterations: int = 3000,
    learning_rate: float = 0.08,
    l2: float = 0.03,
    boundary_prior_strength: float = 0.02,
) -> dict[str, Any]:
    """Fit a deterministic balanced logistic model with fixed-step descent."""
    if len(rows) != len(labels) or not rows:
        raise ValueError("rows and labels must be non-empty and have equal length")
    names = feature_names(feature_set)
    vectors = [candidate_features(row_candidate(row), feature_set=feature_set, today=today) for row in rows]
    matrix = [[vector[name] for name in names] for vector in vectors]
    positives = sum(1 for label in labels if label)
    negatives = len(labels) - positives
    if not positives or not negatives:
        raise ValueError("both classes are required for fitting")
    class_weights = {1: len(labels) / (2.0 * positives), 0: len(labels) / (2.0 * negatives)}
    weights = [
        0.5 if name == "boundary_true" else -0.5 if name == "boundary_false" else 0.0
        for name in names
    ]
    intercept = 0.0
    count = float(len(labels))
    for step in range(max(1, int(iterations))):
        rate = learning_rate / (1.0 + 0.001 * step)
        grad_intercept = 0.0
        gradients = [l2 * weight for weight in weights]
        for vector, label in zip(matrix, labels):
            logit = intercept + sum(weight * value for weight, value in zip(weights, vector))
            error = (_sigmoid(logit) - float(label)) * class_weights[int(bool(label))]
            grad_intercept += error
            for index, value in enumerate(vector):
                gradients[index] += error * value
        # The v1 boundary classifier has an explicit, reviewed ordering. A
        # small centered prior retains that ordering for categories absent
        # from a particular training fold (the current corpus has no
        # repo-name-only deterministic-false rows) without copying v1's
        # literal +50/-40 score weights.
        for index, name in enumerate(names):
            if name == "boundary_true":
                gradients[index] += boundary_prior_strength * count * (weights[index] - 0.5)
            elif name == "boundary_false":
                gradients[index] += boundary_prior_strength * count * (weights[index] + 0.5)
        scale = 1.0 / count
        intercept -= rate * grad_intercept * scale
        for index, gradient in enumerate(gradients):
            weights[index] -= rate * gradient * scale
    return {
        "feature_set": feature_set,
        "feature_names": list(names),
        "intercept": intercept,
        "weights": {name: weight for name, weight in zip(names, weights)},
        "fitter": {
            "method": "balanced-logistic-gradient-descent",
            "iterations": int(iterations),
            "learning_rate": learning_rate,
            "learning_rate_decay": 0.001,
            "l2": l2,
            "boundary_prior_strength": boundary_prior_strength,
        },
    }


def linear_score(
    candidate: Mapping[str, Any],
    model: Mapping[str, Any],
    *,
    today: date | str | None = None,
    tree_feature: Mapping[str, Any] | None = None,
) -> float:
    feature_set = str(model.get("feature_set") or "v2")
    names = tuple(str(name) for name in model.get("feature_names") or feature_names(feature_set))
    values = candidate_features(candidate, feature_set=feature_set, today=today, tree_feature=tree_feature)
    weights = model.get("weights")
    weights = weights if isinstance(weights, Mapping) else {}
    return float(model.get("intercept") or 0.0) + sum(
        float(weights.get(name) or 0.0) * values.get(name, 0.0) for name in names
    )


def predict_scores(
    rows: Sequence[Mapping[str, Any]],
    model: Mapping[str, Any],
    *,
    today: date | str | None = None,
) -> list[float]:
    return [linear_score(row_candidate(row), model, today=today) for row in rows]


def auc(scores: Sequence[float], labels: Sequence[int]) -> float:
    """Return tie-aware ROC AUC using only Python sorting and arithmetic."""
    if len(scores) != len(labels):
        raise ValueError("scores and labels must have equal length")
    positive_count = sum(1 for label in labels if label)
    negative_count = len(labels) - positive_count
    if not positive_count or not negative_count:
        return float("nan")
    ordered = sorted(zip(scores, labels), key=lambda pair: pair[0])
    positive_rank_sum = 0.0
    index = 0
    while index < len(ordered):
        end = index + 1
        while end < len(ordered) and ordered[end][0] == ordered[index][0]:
            end += 1
        average_rank = (index + 1 + end) / 2.0
        positive_rank_sum += average_rank * sum(1 for _score, label in ordered[index:end] if label)
        index = end
    return (positive_rank_sum - positive_count * (positive_count + 1) / 2.0) / (positive_count * negative_count)


def mean_gap(scores: Sequence[float], labels: Sequence[int]) -> float:
    positive = [score for score, label in zip(scores, labels) if label]
    negative = [score for score, label in zip(scores, labels) if not label]
    if not positive or not negative:
        return float("nan")
    return sum(positive) / len(positive) - sum(negative) / len(negative)


def grouped_split(
    rows: Sequence[Mapping[str, Any]],
    *,
    seed: int = DEFAULT_SEED,
    train_fraction: float = 0.6,
    dev_fraction: float = 0.2,
) -> tuple[list[Mapping[str, Any]], list[Mapping[str, Any]], list[Mapping[str, Any]]]:
    """Split rows by normalized URL, so duplicate decisions cannot straddle folds."""
    groups: dict[str, list[Mapping[str, Any]]] = {}
    for row in rows:
        groups.setdefault(normalize_repo_url(str(row.get("url") or "")), []).append(row)
    keys = sorted(groups)
    random.Random(seed).shuffle(keys)
    train_count = max(1, min(len(keys) - 2, round(len(keys) * train_fraction)))
    dev_count = max(1, min(len(keys) - train_count - 1, round(len(keys) * dev_fraction)))
    train_keys = set(keys[:train_count])
    dev_keys = set(keys[train_count:train_count + dev_count])
    train = [row for row in rows if normalize_repo_url(str(row.get("url") or "")) in train_keys]
    dev = [row for row in rows if normalize_repo_url(str(row.get("url") or "")) in dev_keys]
    holdout = [row for row in rows if normalize_repo_url(str(row.get("url") or "")) not in train_keys | dev_keys]
    return train, dev, holdout


def _labels(rows: Sequence[Mapping[str, Any]], positive: frozenset[str]) -> list[int]:
    return [int(str(row.get("label") or "") in positive) for row in rows]


def _bootstrap_auc_interval(
    scores: Sequence[float],
    labels: Sequence[int],
    *,
    seed: int,
    samples: int = 1000,
) -> list[float] | None:
    if not scores or not any(labels) or all(labels):
        return None
    rng = random.Random(seed)
    values: list[float] = []
    indexes = list(range(len(scores)))
    for _ in range(samples):
        selected = [rng.choice(indexes) for _ in indexes]
        sample_scores = [scores[index] for index in selected]
        sample_labels = [labels[index] for index in selected]
        if not any(sample_labels) or all(sample_labels):
            continue
        values.append(auc(sample_scores, sample_labels))
    if not values:
        return None
    values.sort()
    low = values[max(0, int(0.025 * (len(values) - 1)))]
    high = values[min(len(values) - 1, int(0.975 * (len(values) - 1)))]
    return [low, high]


def _baseline_candidate(row: Mapping[str, Any]) -> dict[str, Any]:
    candidate = row_candidate(row)
    candidate.pop("probe", None)
    candidate.pop("tree_probe", None)
    return candidate


def _boundary_sanity_model(model: Mapping[str, Any], *, today: date) -> dict[str, Any]:
    common = {
        "stars": 100,
        "pushed_date": today.isoformat(),
        "source_query": "filename:validator.py path:src",
        "capped": False,
    }
    candidates = [
        {**common, "url": "https://github.com/acme/gitleaks"},
        {**common, "url": "https://github.com/acme/octo-widget"},
        {**common, "url": "https://github.com/acme/awesome-regex-tutorial"},
    ]
    scores = [linear_score(candidate, model, today=today) for candidate in candidates]
    from regexproof.mine.score import candidate_score

    v1_scores = [candidate_score(candidate, today=today)[0] for candidate in candidates]
    v1_order = [
        _boundary_for_candidate(candidate)
        for candidate in candidates
    ]
    passed = scores[0] > scores[1] > scores[2] and v1_scores[0] > v1_scores[1] > v1_scores[2]
    if v1_order != ["deterministic-true", "unknown", "deterministic-false"]:
        raise AssertionError("v1 boundary sanity fixtures no longer cover all verdicts")
    if not passed:
        raise AssertionError(f"fitted v1 boundary order changed: {scores!r}")
    return {
        "passed": True,
        "verdicts": v1_order,
        "scores": scores,
        "v1_scores": v1_scores,
        "v1_weight_order": [50.0, 0.0, -40.0],
    }


def sanity_check_v1_boundary(model: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """Assert that a fitted v1-feature model retains v1 boundary ordering."""
    if model is None:
        model = fit_logistic(
            [
                {"url": "https://github.com/acme/gitleaks", "label": "go"},
                {"url": "https://github.com/acme/octo-widget", "label": "no-go"},
                {"url": "https://github.com/acme/awesome-regex-tutorial", "label": "no-go"},
            ],
            [1, 0, 0],
            feature_set="v1",
        )
    return _boundary_sanity_model(model, today=DEFAULT_FIT_DATE)


def fit_report(
    rows: Sequence[Mapping[str, Any]],
    *,
    seed: int = DEFAULT_SEED,
    fit_date: date | str = DEFAULT_FIT_DATE,
) -> dict[str, Any]:
    """Fit, select the mapping on dev, and evaluate the selected mapping once."""
    if not rows:
        raise ValueError("gate-label artifact has no rows")
    today = _as_date(fit_date)
    train, dev, holdout = grouped_split(rows, seed=seed)
    mapping_results: dict[str, Any] = {}
    fitted_by_mapping: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for name, positive in POSITIVE_MAPPINGS.items():
        train_labels = _labels(train, positive)
        dev_labels = _labels(dev, positive)
        full_model = fit_logistic(train, train_labels, feature_set="v2", today=today)
        v1_model = fit_logistic(train, train_labels, feature_set="v1", today=today)
        dev_scores = predict_scores(dev, full_model, today=today)
        mapping_results[name] = {
            "positive_labels": sorted(positive),
            "train_positive_count": sum(train_labels),
            "dev_positive_count": sum(dev_labels),
            "dev_negative_count": len(dev_labels) - sum(dev_labels),
            "dev_auc": auc(dev_scores, dev_labels),
        }
        fitted_by_mapping[name] = (full_model, v1_model)

    chosen_mapping = max(
        POSITIVE_MAPPINGS,
        key=lambda name: (mapping_results[name]["dev_auc"], name == "go-only"),
    )
    positive = POSITIVE_MAPPINGS[chosen_mapping]
    train_labels = _labels(train, positive)
    holdout_labels = _labels(holdout, positive)
    full_model, v1_model = fitted_by_mapping[chosen_mapping]
    full_holdout_scores = predict_scores(holdout, full_model, today=today)
    v1_holdout_scores = predict_scores(holdout, v1_model, today=today)

    # This is the only holdout evaluation for the selected positive mapping;
    # both scores use the same rows and labels for the attribution ablation.
    holdout_auc = auc(full_holdout_scores, holdout_labels)
    ablation_auc = auc(v1_holdout_scores, holdout_labels)
    baseline_scores = []
    from regexproof.mine.score import candidate_score

    for row in holdout:
        score, _breakdown = candidate_score(_baseline_candidate(row), today=today)
        baseline_scores.append(score)
    baseline_auc = auc(baseline_scores, holdout_labels)
    full_gap = mean_gap(full_holdout_scores, holdout_labels)
    ablation_gap = mean_gap(v1_holdout_scores, holdout_labels)
    baseline_gap = mean_gap(baseline_scores, holdout_labels)
    sanity = _boundary_sanity_model(v1_model, today=today)
    interval = _bootstrap_auc_interval(full_holdout_scores, holdout_labels, seed=seed + 1)
    gate = {
        "label_reproduction_auc_ge_0_70": bool(holdout_auc >= 0.70),
        "holdout_auc_ge_0_70": bool(holdout_auc >= 0.70),  # alias
        "ablation_beats_v1_features": bool(holdout_auc > ablation_auc),
        "mean_gap_beats_v1_baseline_informational": bool(full_gap > baseline_gap),
        "default_allocator_flip_allowed": bool(holdout_auc >= 0.70 and holdout_auc > ablation_auc),
    }
    artifact = {
        "schema_version": SCHEMA_VERSION,
        "allocator": "score-v2",
        "feature_set": "v2",
        "feature_names": list(full_model["feature_names"]),
        "intercept": full_model["intercept"],
        "weights": full_model["weights"],
        "n": len(rows),
        "date": today.isoformat(),
        "label_reproduction_auc": holdout_auc,
        "holdout_auc": holdout_auc,  # deprecated alias; not external validation
        "holdout_positive_count": sum(holdout_labels),
        "holdout_negative_count": len(holdout_labels) - sum(holdout_labels),
        "holdout_auc_bootstrap_95": interval,
        "training": {
            "n": len(rows),
            "train_n": len(train),
            "dev_n": len(dev),
            "holdout_n": len(holdout),
            "seed": seed,
            "grouped_by": "normalized_url",
            "fit_date": today.isoformat(),
            "positive_mapping": chosen_mapping,
            "mapping_decision": mapping_results,
            "fitter": full_model["fitter"],
            "feature_set_frozen": True,
            "holdout_evaluated_once": True,
        },
        "evaluation": {
            "label_set": "gate-labels.json",
            "positive_mapping": chosen_mapping,
            "label_reproduction_auc": holdout_auc,
            "holdout_auc": holdout_auc,  # deprecated alias
            "v1_feature_ablation_auc": ablation_auc,
            "recomputed_v1_baseline_auc": baseline_auc,
            "score_v2_mean_gap": full_gap,
            "v1_feature_ablation_mean_gap": ablation_gap,
            "recomputed_v1_baseline_mean_gap": baseline_gap,
            "same_holdout_label_set": True,
            "same_positive_class_definition": True,
            "sanity": sanity,
            "gate": gate,
        },
        # Do not flip the production default automatically when the artifact
        # is regenerated; the allocator flag is the explicit rollout control.
        "default_allocator": "score-v1",
    }
    return artifact


@lru_cache(maxsize=4)
def load_weights(path: Path | str) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("allocator") != "score-v2":
        raise ValueError("invalid score-v2 weight artifact")
    names = value.get("feature_names")
    weights = value.get("weights")
    if value.get("feature_set") != "v2" or not isinstance(names, list) or not isinstance(weights, Mapping):
        raise ValueError("score-v2 weight artifact has an invalid feature schema")
    if tuple(str(name) for name in names) != V2_FEATURE_NAMES:
        raise ValueError("score-v2 weight artifact feature set does not match the frozen encoder")
    return value


def format_report(artifact: Mapping[str, Any]) -> dict[str, Any]:
    """Return the stable, concise machine-readable fit report."""
    training = artifact.get("training") if isinstance(artifact.get("training"), Mapping) else {}
    evaluation = artifact.get("evaluation") if isinstance(artifact.get("evaluation"), Mapping) else {}
    return {
        "kind": "score_v2_fit",
        "allocator": "score-v2",
        "n": artifact.get("n"),
        "date": artifact.get("date"),
        "positive_mapping": training.get("positive_mapping"),
        "mapping_decision": training.get("mapping_decision"),
        "label_reproduction_auc": artifact.get("label_reproduction_auc", artifact.get("holdout_auc")),
        "holdout_auc": artifact.get("label_reproduction_auc", artifact.get("holdout_auc")),
        "holdout_positive_count": artifact.get("holdout_positive_count"),
        "holdout_auc_bootstrap_95": artifact.get("holdout_auc_bootstrap_95"),
        "v1_feature_ablation_auc": evaluation.get("v1_feature_ablation_auc"),
        "recomputed_v1_baseline_mean_gap": evaluation.get("recomputed_v1_baseline_mean_gap"),
        "score_v2_mean_gap": evaluation.get("score_v2_mean_gap"),
        "gate": evaluation.get("gate"),
        "sanity": evaluation.get("sanity"),
    }
