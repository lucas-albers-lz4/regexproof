"""Execution-only property runner shared by harness and newgate CLIs.

Returns results; does **not** decide process exit codes (§10 stays in each
``main()``). ``--json-legacy`` array + ``derive_tier`` stays in harness
``main()`` — this module only streams NDJSON records when ``as_json`` is set.
"""

from __future__ import annotations

import contextlib
import io
import json
import sys
from typing import Any

from regexproof.harness.core import REGISTRY, run_one


def run_named_properties(
    names: list[str],
    *,
    require_gt: bool = False,
    as_json: bool = False,
    quiet: bool = False,
) -> list[dict[str, Any]]:
    """Run named properties; print NDJSON records when ``as_json``.

    ``quiet`` suppresses ``run_one`` human PASS/FAIL lines (needed for
    ``--json-legacy`` so only the REPORT array hits stdout). Returns the
    list of result dicts. Callers own exit policy (0/1/2), human summary
    lines, and ``--json-legacy`` REPORT mode.
    """
    results: list[dict[str, Any]] = []
    if as_json or quiet:
        sink = io.StringIO()
        with contextlib.redirect_stdout(sink):
            for name in names:
                res = run_one(name, REGISTRY[name], require_gt)
                results.append(res)
                if as_json:
                    # Flush each record immediately so partial streams stay valid.
                    print(
                        json.dumps(res, sort_keys=True),
                        file=sys.__stdout__,
                        flush=True,
                    )
    else:
        for name in names:
            res = run_one(name, REGISTRY[name], require_gt)
            results.append(res)
    return results
