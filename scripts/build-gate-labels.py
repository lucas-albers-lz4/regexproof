#!/usr/bin/env python3
"""Build the deterministic gate-label artifact used by the P8 fit.

The default invocation is read-only with respect to GitHub: it joins the
committed ledger and decision files and writes the artifact.  ``--backfill``
enables optional GitHub enrichment/tree calls for rows whose materialized
fields are absent; all such calls are budgeted and failures degrade to an
incomplete feature rather than an inferred negative.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.admission.serialize import dumps_pinned
from regexproof.io_atomic import atomic_write_text
from regexproof.mine.exclusions import normalize_repo_url
from regexproof.mine.ledger import ENRICH_FIELDS, load_ledger, save_ledger
from regexproof.mine.search import AuthError, RateLimitError, enrich_repo, github_headers
from regexproof.mine.tree import (
    DEFAULT_TREE_PROBE_BUDGET,
    TreeCache,
    materialize_tree_features,
)

DECISION_GLOB = "*_gate_decision.json"
ARTIFACT_SCHEMA_VERSION = "1"


def _read_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def _repo_slug(url: str) -> str:
    return normalize_repo_url(url).removeprefix("https://github.com/")


def _int_map(value: Any) -> dict[str, int]:
    if not isinstance(value, dict):
        return {}
    return {str(key): int(number) for key, number in sorted(value.items())}


def _ledger_view(candidate: dict[str, Any]) -> dict[str, Any]:
    """Return the stable ledger feature subset plus materialized enrich data."""
    out: dict[str, Any] = {
        "stars": int(candidate.get("stars") or 0),
        "pushed_date": str(candidate.get("pushed_date") or ""),
        "source_query": str(candidate.get("source_query") or ""),
        "capped": bool(candidate.get("capped")),
    }
    for field in ENRICH_FIELDS:
        out[field] = candidate.get(field)
    return out


def _row(
    candidate: dict[str, Any],
    decision: dict[str, Any],
    *,
    tree_feature: dict[str, Any] | None = None,
) -> dict[str, Any]:
    decision_probe = decision.get("probe")
    probe = decision_probe if isinstance(decision_probe, dict) else {}
    decision_url = str(decision.get("candidate_url") or candidate.get("url") or "")
    return {
        "url": str(candidate.get("url") or decision_url),
        "label": str(decision.get("decision") or ""),
        "decision_date": str(decision.get("decision_date") or ""),
        "probe": {
            "regex_sites": int(probe.get("regex_sites") or 0),
            "dialect_counts": _int_map(probe.get("dialect")),
            "security_boundary": str(probe.get("security_boundary") or "unknown"),
            "predicted_buckets": _int_map(probe.get("predicted_buckets")),
            "tree_probe": tree_feature,
        },
        "ledger": _ledger_view(candidate),
    }


def _decision_paths(directory: Path) -> list[Path]:
    return sorted(directory.glob(DECISION_GLOB), key=lambda path: path.name)


def _linked_records(
    ledger: dict[str, Any], decision_paths: list[Path]
) -> list[tuple[dict[str, Any], dict[str, Any], dict[str, Any]]]:
    by_url: dict[str, dict[str, Any]] = {}
    for candidate in ledger.get("candidates", []):
        if isinstance(candidate, dict) and candidate.get("url"):
            by_url.setdefault(normalize_repo_url(str(candidate["url"])), candidate)

    records: list[tuple[dict[str, Any], dict[str, Any], dict[str, Any]]] = []
    seen_urls: set[str] = set()
    for path in decision_paths:
        decision = _read_json(path)
        if decision is None:
            continue
        url = decision.get("candidate_url")
        label = decision.get("decision")
        if not url or label not in {"go", "triage-trial", "no-go"}:
            continue
        nurl = normalize_repo_url(str(url))
        if nurl in seen_urls:
            # Owner-prefix and manifest-slug copies of the same decision
            # must not double-weight the P8 fit (one row per URL).
            continue
        candidate = by_url.get(nurl)
        if candidate is None:
            continue
        seen_urls.add(nurl)
        records.append((candidate, decision, {"path": path.name}))
    return records


def _backfill_enrich(
    records: list[tuple[dict[str, Any], dict[str, Any], dict[str, Any]]],
    *,
    session: Any,
    budget: int,
    headers: dict[str, str] | None,
) -> None:
    remaining = max(0, int(budget))
    for candidate, _decision, _meta in records:
        if remaining <= 0:
            return
        if all(candidate.get(field) is not None for field in ENRICH_FIELDS):
            continue
        try:
            meta = enrich_repo(
                session,
                _repo_slug(str(candidate.get("url") or "")),
                headers=headers,
            )
        except (AuthError, RateLimitError, OSError, ValueError):
            meta = {}
        remaining -= 1
        for field in ENRICH_FIELDS:
            if field in meta:
                candidate[field] = meta[field]


def build_gate_labels(
    *,
    ledger_path: Path | str,
    generated_dir: Path | str,
    output_path: Path | str,
    session: Any | None = None,
    backfill: bool = False,
    enrich_budget: int = 0,
    tree_probe_budget: int = DEFAULT_TREE_PROBE_BUDGET,
    tree_cache_path: Path | str | None = None,
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Join inputs and atomically write the P6 artifact, returning its object."""
    if tree_cache_path is None:
        tree_cache_path = ROOT / "properties" / "generated" / "mine-tree-features.json"
    ledger_file = Path(ledger_path)
    generated = Path(generated_dir)
    output = Path(output_path)
    ledger = load_ledger(ledger_file)
    decision_paths = _decision_paths(generated)
    records = _linked_records(ledger, decision_paths)

    if backfill and session is not None and enrich_budget > 0:
        _backfill_enrich(
            records,
            session=session,
            budget=enrich_budget,
            headers=headers,
        )
        # Persist the materialized enrich fields back into the ledger file —
        # the artifact's ledger view joins the FILE, so an in-memory-only
        # backfill would be lost on the next run (P6 luna gate 1 fold).
        save_ledger(ledger_file, ledger)

    tree_features: dict[str, dict[str, Any]] = {}
    cache = TreeCache(tree_cache_path) if tree_cache_path is not None else None
    if cache is not None:
        # Always join the tracked tree-features file (offline regeneration);
        # --backfill extends it with fresh probes. Offline, the budget is 0:
        # cached rows carry features, uncached rows degrade to
        # budget-exhausted incomplete (never a silent negative).
        probe_candidates = []
        for candidate, decision, _meta in records:
            probe = decision.get("probe") if isinstance(decision.get("probe"), dict) else {}
            # A decision's corpus/probe pin is a decision-time probed pin.  Do
            # not substitute the ledger's mined pin when E3 data is absent.
            probed_pin = str(
                probe.get("pin_probed")
                or decision.get("corpus_pin")
                or probe.get("pin")
                or ""
            )
            probe_candidates.append({"url": candidate.get("url"), "pin_probed": probed_pin})
        tree_features, _calls = materialize_tree_features(
            session if backfill else None,
            probe_candidates,
            budget=tree_probe_budget if backfill else 0,
            cache=cache,
            headers=headers,
        )

    rows = [
        _row(
            candidate,
            decision,
            tree_feature=_tree_feature_for(tree_features, candidate, decision),
        )
        for candidate, decision, _meta in records
    ]
    rows.sort(key=lambda row: (
        str(row.get("url") or ""),
        str(row.get("decision_date") or ""),
        str(row.get("label") or ""),
    ))
    artifact = {
        "schema_version": ARTIFACT_SCHEMA_VERSION,
        "provenance": {
            "schema_version": ARTIFACT_SCHEMA_VERSION,
            "input_file_count": len(decision_paths),
            "gate_decision_count": len(decision_paths),
            "linked_row_count": len(rows),
            "inputs_hash": _inputs_hash(decision_paths, ledger_file, Path(tree_cache_path)),
        },
        "rows": rows,
    }
    atomic_write_text(output, dumps_pinned(artifact))
    return artifact



def _inputs_hash(
    decision_paths: list[Path],
    ledger_file: Path | None = None,
    tree_features_file: Path | None = None,
) -> str:
    """Content hash over the sorted decision files — stable provenance.

    D5 lesson (#437): the committing git HEAD drifts on every commit and
    breaks any regen-and-diff check; a content-derived key is stable
    across clones/commits unless the inputs themselves change.
    """
    h = hashlib.sha256()
    if ledger_file is not None and ledger_file.exists():
        h.update(b"ledger:")
        h.update(ledger_file.name.encode("utf-8"))
        h.update(ledger_file.read_bytes())
    if tree_features_file is not None and tree_features_file.exists():
        h.update(b"tree-features:")
        h.update(tree_features_file.name.encode("utf-8"))
        h.update(tree_features_file.read_bytes())
    for p in sorted(decision_paths):
        h.update(b"decision:")
        h.update(p.name.encode("utf-8"))
        h.update(p.read_bytes())
    return h.hexdigest()




def _tree_feature_for(
    tree_features: dict[tuple[str, str], dict[str, Any]],
    candidate: dict[str, Any],
    decision: dict[str, Any],
) -> dict[str, Any] | None:
    """Pin-aware tree-feature lookup.

    P6 (luna gate 1): tree features are cached per (slug, probed_pin); the
    row lookup must use the row's OWN probed pin — a URL with duplicate
    decisions at different pins must not inherit a sibling's probe result.
    """
    url = str(candidate.get("url") or "")
    probe = decision.get("probe") if isinstance(decision.get("probe"), dict) else {}
    probed_pin = str(
        probe.get("pin_probed")
        or decision.get("corpus_pin")
        or probe.get("pin")
        or ""
    )
    return tree_features.get((normalize_repo_url(url), probed_pin)) if url else None


def _http_session() -> Any:
    try:
        import requests
    except ImportError as exc:  # pragma: no cover
        raise SystemExit("requests is required for backfill") from exc
    return requests.Session()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--ledger",
        type=Path,
        default=ROOT / "properties" / "generated" / "candidate-ledger.json",
    )
    ap.add_argument(
        "--generated",
        type=Path,
        default=ROOT / "properties" / "generated",
    )
    ap.add_argument(
        "--output",
        type=Path,
        default=ROOT / "properties" / "generated" / "gate-labels.json",
    )
    ap.add_argument(
        "--backfill",
        action="store_true",
        help="Fetch missing enrich/tree features using the explicit budgets.",
    )
    ap.add_argument(
        "--enrich-budget",
        type=int,
        default=0,
        help="Max repository enrich calls during backfill (default: 0).",
    )
    ap.add_argument(
        "--tree-probe-budget",
        type=int,
        default=DEFAULT_TREE_PROBE_BUDGET,
        help=(
            "Max uncached tree API calls during backfill "
            f"(default: {DEFAULT_TREE_PROBE_BUDGET})."
        ),
    )
    ap.add_argument(
        "--tree-cache",
        type=Path,
        default=ROOT / "properties" / "generated" / "mine-tree-features.json",
        help="Tree features file; defaults to the tracked "
        "properties/generated/mine-tree-features.json.",
    )
    args = ap.parse_args(argv)

    session = _http_session() if args.backfill else None
    build_gate_labels(
        ledger_path=args.ledger.expanduser().resolve(),
        generated_dir=args.generated.expanduser().resolve(),
        output_path=args.output.expanduser().resolve(),
        session=session,
        backfill=args.backfill,
        enrich_budget=args.enrich_budget,
        tree_probe_budget=args.tree_probe_budget,
        tree_cache_path=args.tree_cache,
        headers=github_headers(),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
