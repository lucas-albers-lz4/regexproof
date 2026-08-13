"""E2 (luna gate 1): enforce the busybox-sed dual-engine replay.

The golden job installs busybox and runs the property suite (which populates
``SED_VERDICT_LOG`` via ``p3_ground_truth_dual``). This script asserts the
record shows BOTH engines ran and agreed — a busybox absence or a GNU/busybox
divergence is a hard failure, never a silent GNU-only collapse.

Run after the phase-2 pilots step in the golden job.
"""

from __future__ import annotations

import sys

from regexproof.harness.properties import SED_VERDICT_LOG, p3_ground_truth_dual


def main() -> int:
    # Force a replay with a witness that exercises the truncation path
    # (a value with an embedded trailing quote: the sed capture truncates
    # at the first unescaped quote — capture is a strict prefix of v).
    ok = p3_ground_truth_dual({"v": 'x"'})
    log = SED_VERDICT_LOG.get("P3-sed-busybox-truncation") or {}
    print("busybox-sed dual replay:", log)
    if log.get("busybox_absent") is True:
        print("error: busybox-sed absent — the golden job must install busybox", file=sys.stderr)
        return 2
    if log.get("gnu") is not True or log.get("busybox") is not True:
        print("error: GNU/busybox sed verdicts disagree:", log, file=sys.stderr)
        return 2
    if not ok:
        print("error: dual replay failed to reproduce the truncation", file=sys.stderr)
        return 2
    print("busybox-sed dual replay: both engines agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
