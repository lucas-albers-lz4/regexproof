"""Ground-truth replay adapters (P1, #425): run the REAL engine on a witness.

Owns wrap semantics (fullmatch vs match vs search), the batch-replay framing
contract (single-session NUL-delimited stdin, per-witness verdict channel),
selection-time replayability classification, and the mapping onto the existing
``ground_truth_status`` vocabulary (``reproduced`` / ``failed`` /
``refused-no-callback`` plus the ``no-adapter`` marker). See
``regexproof/groundtruth/adapters.py``.
"""

from __future__ import annotations

from regexproof.groundtruth.adapters import (
    RefusedNoCallbackError,
    Replayability,
    ReplayResult,
    ReplayVerdict,
    classify_replayability,
    has_adapter,
    replay,
    replay_batch,
    require_replayable,
    skip_reason,
    status_for_claim,
)

__all__ = [
    "RefusedNoCallbackError",
    "ReplayResult",
    "ReplayVerdict",
    "Replayability",
    "classify_replayability",
    "has_adapter",
    "replay",
    "replay_batch",
    "require_replayable",
    "skip_reason",
    "status_for_claim",
]
