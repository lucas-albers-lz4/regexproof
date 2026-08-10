"""Checkout bootstrap: put repo root on sys.path (#201).

Scripts that are not installed as a package can::

    import _bootstrap  # noqa: F401

before importing ``regexproof``.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
