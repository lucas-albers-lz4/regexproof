"""Ground-truth replay adapters (P1, #425): run the REAL engine on a witness.

Owns wrap semantics (fullmatch vs match vs search), the batch-replay framing
contract, and the mapping onto the existing ``ground_truth_status``
vocabulary (``reproduced`` / ``failed`` / ``refused-no-callback`` plus the
``no-adapter`` marker). See ``regexproof/groundtruth/adapters.py``.
"""

from __future__ import annotations

from regexproof.groundtruth.adapters import (
    ReplayResult,
    ReplayVerdict,
    has_adapter,
    replay,
    replay_batch,
    status_for_claim,
)

__all__ = [
    "ReplayResult",
    "ReplayVerdict",
    "has_adapter",
    "replay",
    "replay_batch",
    "status_for_claim",
]
