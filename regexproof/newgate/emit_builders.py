"""Generation-time helpers that *emit* source into scaffolded gate.py.

Generated gates must remain self-contained: do not import these at runtime
from gate.py. Callers interpolate the returned source snippets into templates.
"""

from __future__ import annotations

# Bodies kept byte-stable with historical scaffold output (Grok G3 / Luna L5).
EMITTED_FLAG_BITS = """_FLAG_BITS = {
    "i": re.IGNORECASE,
    "m": re.MULTILINE,
    "s": re.DOTALL,
    "x": re.VERBOSE,
    "a": re.ASCII,
    "u": re.UNICODE,
}"""

EMITTED_BUILD_ALPHABET = '''def _build_alphabet():
    """Collapse contiguous code points into Range (Union of 39 Re() is slow)."""
    if not ALPHABET_CHARS:
        raise SystemExit("newgate gate: empty ALPHABET_CHARS")
    codes = sorted({ord(ch) for ch in ALPHABET_CHARS})
    parts = []
    start = prev = codes[0]
    for code in codes[1:]:
        if code == prev + 1:
            prev = code
            continue
        parts.append(
            Range(chr(start), chr(prev)) if start != prev else Re(chr(start))
        )
        start = prev = code
    parts.append(Range(chr(start), chr(prev)) if start != prev else Re(chr(start)))
    if len(parts) == 1:
        return parts[0]
    return Union(*parts)'''
