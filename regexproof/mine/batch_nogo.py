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


class IncompleteFoldError(RuntimeError):
    """Ledger or artifact install failed — do not complete the batch row."""


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
        except ValueError as ledger_exc:
            # Missing ledger row is deterministic — complete so drain
            # does not re-clone forever.
            return "error", None, f"needs_human ledger join failed: {ledger_exc}"
        except OSError as ledger_exc:
            raise IncompleteFoldError(
                f"needs_human ledger join failed: {ledger_exc}"
            ) from ledger_exc
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
    pending.write_text(
        json.dumps(decision, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    # Always rewrite pending from this inventory. Keep the file on
    # OSError so a transient install can retry; never install a stale journal.
    try:
        audit.mark_auto_filed(ledger_path, url)
    except ValueError as exc:
        # re_evaluate=true is human routing, not a transient install failure.
        # Completing as needs_human prevents an infinite re-clone loop.
        if "re_evaluate" in str(exc):
            try:
                pending.unlink(missing_ok=True)
            except OSError:
                pass
            return "needs_human", None, str(exc)
        try:
            pending.unlink(missing_ok=True)
        except OSError:
            pass
        return "error", None, f"auto-filing refused: {exc}"
    except OSError as exc:
        raise IncompleteFoldError(f"auto-filing refused: {exc}") from exc
    try:
        os.replace(pending, out_path)
    except OSError as exc:
        raise IncompleteFoldError(f"artifact install failed: {exc}") from exc
    return "auto_nogo", out_path, "below-scale or duplicate-fork"
