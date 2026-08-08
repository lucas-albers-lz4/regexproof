"""Golden-suite case registry with coverage-matrix counters."""

from __future__ import annotations

from dataclasses import dataclass

import z3

from regexproof.compiler import compile_pattern


@dataclass
class GoldenCase:
    dialect: str
    pattern: str
    flags: str
    call_kind: str
    accept: list[str]
    reject: list[str]
    category: str = "positive"  # positive | reject | trap
    expect_unencodable: str | None = None
    trap: str | None = None


CASES: list[GoldenCase] = []


def _add(dialect, pattern, flags, call_kind, accept, reject, **kw):
    CASES.append(
        GoldenCase(dialect, pattern, flags, call_kind, accept, reject, **kw)
    )


# --- py_re positives (≥10) ---
for pat, acc, rej in [
    (r"^[a-z]+$", ["abc"], ["ab1", "Abc"]),
    (r"^[0-9]{2,4}$", ["12", "1234"], ["1", "12345"]),
    (r"foo|bar", ["foo", "bar", "xfoo"], ["baz"]),
    (r"a+", ["a", "aaa"], ["", "b"]),
    (r"^a?$", ["", "a"], ["aa"]),
    (r"(ab)+", ["ab", "abab"], ["a", "b"]),
    (r"^\w+$", ["abc_1"], ["a-b"]),
    (r"^\d+$", ["09", "123"], ["a9"]),
    (r"^a\.b$", ["a.b"], ["ab", "aXb"]),
    (r"^foo", ["foo", "foobar"], ["xfoo"]),
    (r"bar$", ["bar", "xbar"], ["barx"]),
    (r"(?i)^[a-z]+$", ["Abc", "ABC"], ["A1"]),
]:
    ck = "fullmatch" if pat.startswith("^") and pat.endswith("$") else (
        "match" if pat.startswith("^") and not pat.endswith("$") else (
            "search" if not pat.startswith("^") and pat.endswith("$") else "search"
        )
    )
    if pat.startswith("^") and pat.endswith("$"):
        ck = "fullmatch"
    elif pat.startswith("^"):
        ck = "match"
    elif pat.endswith("$"):
        ck = "search"
    else:
        ck = "search"
    _add("py_re", pat, "i" if "(?i)" in pat else "", ck, acc, rej)

# ASCII digit under re.ASCII
_add("py_re", r"^\d+$", "a", "fullmatch", ["09"], ["\u0660"], category="positive")

# --- ecma positives (≥10) ---
for pat, flags, ck, acc, rej in [
    (r"^[a-z]+$", "", "fullmatch", ["abc"], ["ab1"]),
    (r"^[0-9]+$", "", "fullmatch", ["12"], ["1a"]),
    (r"foo|bar", "", "search", ["foo"], ["baz"]),
    (r"a+", "", "search", ["aaa"], [""]),
    (r"a?", "", "search", ["", "a"], []),
    (r"(ab)+", "", "search", ["abab"], ["a"]),
    (r"^\w+$", "", "fullmatch", ["ab_1"], ["a-b"]),
    (r"^\d+$", "", "fullmatch", ["09"], ["a"]),
    (r"^a\.b$", "", "fullmatch", ["a.b"], ["ab"]),
    (r"foo", "i", "search", ["FOO", "Foo"], ["bar"]),
    (r"^https?://", "", "match", ["http://x", "https://x"], ["ftp://x"]),
    (r"end$", "", "search", ["end", "the end"], ["endx"]),
]:
    _add("ecma", pat, flags, ck, acc, rej)

# --- re2 positives (≥10) ---
for pat, flags, ck, acc, rej in [
    (r"^[a-z]+$", "", "fullmatch", ["abc"], ["Abc"]),
    (r"^[0-9]+$", "", "fullmatch", ["42"], ["4a"]),
    (r"foo|bar", "", "search", ["bar"], ["baz"]),
    (r"a+", "", "search", ["aa"], [""]),
    (r"(ab)+", "", "search", ["ab"], ["ba"]),
    (r"^\w+$", "", "fullmatch", ["a_1"], ["a-b"]),
    (r"^\d+$", "", "fullmatch", ["7"], ["x"]),
    (r"^a\.b$", "", "fullmatch", ["a.b"], ["aab"]),
    (r"(?i)^[a-z]+$", "i", "fullmatch", ["AbC"], ["A1"]),
    (r"tok$", "", "search", ["tok", "xtok"], ["tokx"]),
    (r"^tok", "", "match", ["tok", "tokx"], ["xtok"]),
    (r"a{2,3}", "", "search", ["aa", "aaa"], ["a"]),
]:
    # strip (?i) from pattern if flags carry i
    p = pat.replace("(?i)", "")
    _add("re2", p, flags, ck, acc, rej)

# ASCII-domain edge \\b (RE2/PCRE/ECMA); py_re Unicode-default stays reject.
for dialect in ("re2", "ecma", "pcre"):
    _add(
        dialect,
        r"\bword\b",
        "",
        "search",
        ["word", " word ", "word!", "!word"],
        ["awordb", "xwordy", "wordword"],
        category="positive",
    )

# --- pcre positives (≥10) ---
for pat, flags, ck, acc, rej in [
    (r"^[a-z]+$", "", "fullmatch", ["abc"], ["1"]),
    (r"^[0-9]+$", "", "fullmatch", ["9"], ["x"]),
    (r"foo|bar", "", "search", ["foo"], ["qux"]),
    (r"a+", "", "search", ["a"], [""]),
    (r"(ab)+", "", "search", ["ab"], ["b"]),
    (r"^\w+$", "", "fullmatch", ["Z_9"], ["-"]),
    (r"^\d+$", "", "fullmatch", ["0"], ["o"]),
    (r"^a\.b$", "", "fullmatch", ["a.b"], ["ab"]),
    (r"^x{1,2}$", "", "fullmatch", ["x", "xx"], ["xxx"]),
    (r"end$", "", "search", ["end"], ["endx"]),
    (r"^start", "", "match", ["start"], ["xstart"]),
    (r"(?:ab)+", "", "search", ["abab"], ["a"]),
    (r"^[^0-9]+$", "", "fullmatch", ["abc"], ["a1"]),
    (r"pre-(?i:abc)-post", "", "fullmatch", ["pre-ABC-post", "pre-abc-post"], ["pre-abd-post"]),
]:
    _add("pcre", pat, flags, ck, acc, rej)

# --- reject-list (≥5 per category samples) ---
REJECTS = [
    ("py_re", r"(?=a)b", "", "search", "lookaround"),
    ("py_re", r"(?<=a)b", "", "search", "lookaround"),
    ("py_re", r"(a)\1", "", "search", "backref"),
    ("py_re", r"\bword\b", "", "search", "word-boundary"),  # Unicode-default; ASCII gate required
    ("py_re", r"^a$", "m", "search", "m-flag"),
    ("py_re", "a" * 300, "", "search", "pattern-too-long"),
    ("ecma", r"(?=a)b", "", "search", "lookaround"),
    ("ecma", r"(a)\1", "", "search", "backref"),
    ("ecma", r"foo\bbar", "", "search", "word-boundary"),  # mid-pattern \\b unsupported
    ("ecma", r"a", "u", "search", "u-flag"),
    ("ecma", r"a", "v", "search", "v-flag"),
    ("ecma", r"a", "m", "search", "m-flag"),
    ("ecma", r"a", "g", "search", "stateful"),
    ("ecma", r"a", "y", "search", "stateful"),
    ("ecma", r"(?i:a)", "", "search", "inline-flag"),
    ("re2", r"(?=a)b", "", "search", "lookaround"),
    ("re2", r"(a)\1", "", "search", "backref"),
    ("re2", r"foo\bbar", "", "search", "word-boundary"),  # mid-pattern \\b unsupported
    ("re2", r"\Bword\B", "", "search", "word-boundary"),  # \\B stays reject
    ("re2", r"^a$", "m", "search", "m-flag"),
    ("re2", "b" * 300, "", "search", "pattern-too-long"),
    ("re2", r"(?-i:abc)", "", "search", "inline-flag"),
    ("pcre", r"(?=a)b", "", "search", "lookaround"),
    ("pcre", r"(a)\1", "", "search", "backref"),
    ("pcre", r"(?(1)a|b)", "", "search", "conditional"),
    ("pcre", r"a\K b", "", "search", "reset"),
    ("pcre", "c" * 300, "", "search", "pattern-too-long"),
    ("pcre", r"(?ms:abc)", "", "search", "inline-flag"),
]
for dialect, pat, flags, ck, reason in REJECTS:
    _add(
        dialect,
        pat,
        flags,
        ck,
        [],
        [],
        category="reject",
        expect_unencodable=reason,
    )

# --- trap probes (≥3 each for key traps) ---
TRAPS = [
    ("py_re", r".", "", "fullmatch", ["a", "\r"], ["\n"], "dot-terminator"),
    ("py_re", r".", "s", "fullmatch", ["a", "\n"], [], "dotall"),
    ("py_re", r"\d", "", "search", ["5", "\u0660"], ["x"], "unicode-digit"),
    ("ecma", r".", "", "fullmatch", ["a"], ["\n", "\u2028"], "dot-terminator"),
    ("ecma", r"\s", "", "search", [" ", "\u00a0"], ["a"], "js-space"),
    ("ecma", r"^ß$", "i", "fullmatch", ["ß"], ["SS"], "js-fold-ss"),
    ("re2", r"^[a-z]$", "i", "fullmatch", ["A"], ["\u0130"], "re2-fold-i"),
    ("re2", r".", "", "fullmatch", ["a", "\r"], ["\n"], "dot-terminator"),
    ("pcre", r"abc$", "", "fullmatch", ["abc", "abc\n"], ["abc\nx"], "dollar-nl"),
    ("py_re", r"abc$", "", "fullmatch", ["abc", "abc\n"], ["ab"], "dollar-nl"),
    ("py_re", r"\Z", "", "search", [], [], "z-eos"),  # may unencodable or end
]
for row in TRAPS:
    dialect, pat, flags, ck, acc, rej, trap = row
    _add(dialect, pat, flags, ck, acc, rej, category="trap", trap=trap)


def coverage_counts() -> dict[str, dict[str, int]]:
    counts: dict[str, dict[str, int]] = {}
    for c in CASES:
        d = counts.setdefault(c.dialect, {"positive": 0, "reject": 0, "trap": 0})
        d[c.category] = d.get(c.category, 0) + 1
    return counts


def membership(mirror, s: str) -> bool:
    solver = z3.Solver()
    solver.set("timeout", 10000)
    solver.add(z3.InRe(z3.StringVal(s), mirror))
    r = solver.check()
    if r == z3.unknown:
        raise TimeoutError(s)
    return r == z3.sat
