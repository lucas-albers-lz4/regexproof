"""Mining scanner foundations (mine-and-approve P2)."""

from __future__ import annotations

from regexproof.mine.audit import mark_auto_filed, run_audit_sampler, sample_size
from regexproof.mine.exclusions import is_excluded, load_admitted_urls
from regexproof.mine.ledger import (
    LEDGER_SCHEMA_VERSION,
    load_ledger,
    save_ledger,
)
from regexproof.mine.queue import daily_mine_cap, drain, enqueue, load_queue, save_queue
from regexproof.mine.score import SCORE_VERSION, candidate_score, rank_candidates
from regexproof.mine.search import AuthError, run_search
from regexproof.mine.transition import TransitionError, transition_candidate

__all__ = [
    "AuthError",
    "LEDGER_SCHEMA_VERSION",
    "SCORE_VERSION",
    "TransitionError",
    "candidate_score",
    "daily_mine_cap",
    "drain",
    "enqueue",
    "is_excluded",
    "load_admitted_urls",
    "load_ledger",
    "load_queue",
    "mark_auto_filed",
    "rank_candidates",
    "run_audit_sampler",
    "run_search",
    "sample_size",
    "save_ledger",
    "save_queue",
    "transition_candidate",
]
