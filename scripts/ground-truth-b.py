"""Ground-truth for the \\b Unicode-divergence differential-fuzz demo.

Mirrors gateway/run.py:150 exactly: r"\\bsk-[A-Za-z0-9][A-Za-z0-9_\\-]{12,}\\b"
Python \\b is Unicode-aware: 中 is \\w, so 中sk-<token> has NO boundary and
is NOT redacted. An ASCII mirror (no \\b) treats it as a match -> mismatch.
"""

import re
import sys

PAT = re.compile(r"\bsk-[A-Za-z0-9][A-Za-z0-9_\-]{12,}\b")
sys.exit(0 if PAT.search(sys.stdin.read()) else 1)
