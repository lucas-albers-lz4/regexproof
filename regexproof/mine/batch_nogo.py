"""Wave 5 (#574): fold deterministic auto-NO-GO into a successful batch walk.

Does not replace ``bulk-review-staged.py`` (operator-initiated no-go stays
there). Sub-scale / duplicate-fork walks file a gate decision here; everyone
else stays ``needs_human`` with the staged draft.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from regexproof.admission.author import AuthorError, author_auto, default_output_path
from regexproof.admission.auto_nogo import AutoNoGoError
from regexproof.mine import audit

# Walk completed (inventory ran). ``ok`` is retained for pre-Wave-5 rows.
WALK_COMPLETED = frozenset({"ok", "auto_nogo", "needs_human"})


def fold_auto_nogo(
    draft: dict[str, Any],
    *,
    generated_dir: Path,
    ledger_path: Path,
    repo_root: Path,
) -> tuple[str, Path | None, str]:
    """Return ``(outcome, decision_path_or_None, note)``.

    ``auto_nogo`` writes a schema-valid no-go via ``author_auto`` (same
    path as ``author-gate-decision.py --auto`` / bulk-review ``--no-go``).
    ``needs_human`` leaves authoring to the operator.
    """
    url = str(draft.get("candidate_url") or "")
    corpus = str(draft.get("corpus") or "corpus")
    try:
        decision = author_auto(draft, generated_dir=generated_dir)
    except AutoNoGoError as exc:
        try:
            audit.mark_needs_human_review(ledger_path, url, reason=str(exc))
        except (ValueError, OSError):
            pass  # draft is the durable hand-off; ledger is best-effort here
        return "needs_human", None, str(exc)
    except AuthorError as exc:
        return "error", None, f"author_auto refused: {exc}"

    out_path = default_output_path(corpus, repo_root=repo_root)
    # Tests inject generated_dir that may not be repo properties/generated;
    # still write under that dir when it is the intended destination.
    if generated_dir.resolve() != (repo_root / "properties" / "generated").resolve():
        safe = out_path.name
        out_path = generated_dir / safe
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pending = out_path.with_name(out_path.name + ".pending")
    if pending.exists():
        pending.unlink(missing_ok=True)
    pending.write_text(
        json.dumps(decision, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    def _rollback() -> None:
        try:
            pending.unlink(missing_ok=True)
        except OSError:
            pass

    try:
        audit.mark_auto_filed(ledger_path, url)
    except Exception as exc:
        _rollback()
        return "error", None, f"auto-filing refused: {exc}"
    try:
        os.replace(pending, out_path)
    except OSError as exc:
        return "error", None, f"artifact install failed: {exc}"
    return "auto_nogo", out_path, "below-scale or duplicate-fork"
