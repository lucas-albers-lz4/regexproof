# Lookbehind rewrite — string-ops encoding for unprovable patterns

Stock Z3's regular-language theory has no lookahead/lookbehind
(`(?=...)`, `(?<=...)`, `(?<!...)`). Most lookarounds are **fixed-width**
(one char: `(?<=\s)`, `(?<![A-Za-z0-9_])`) and can be folded into the
adjacent char class of the mirror. The genuinely unprovable case is a
**variable-width** lookbehind — `(?<=^)` under `re.MULTILINE` (line
start, zero-or-more width depending on the newline position).

This document is the worked rewrite (hermes-agent dogfooding, issue #11,
gap 3 — the one variable-width lookbehind found in a 3000-file corpus).

## The pattern (gateway/platforms/yuanbao.py:4860)

```python
_AT_USER_RE = re.compile(r"(?:(?<=\s)|(?<=^))@(\S+?)(?=\s|$)", re.MULTILINE)
```

Semantics: match `@nickname` (non-space run) when preceded by whitespace
OR start-of-line (MULTILINE: start of ANY line), and followed by
whitespace or end-of-string. The nickname is the capture.

Why unprovable as written: `(?<=^)` with `re.MULTILINE` means "the
position right after a `\n`" — a variable-width context Z3's regex theory
cannot express (no line anchors, no lookbehind).

## The string-ops rewrite

Model the line as a whole and constrain the match position with
`IndexOf` / `SubString` / `CharAt` — no regex needed:

```
s = the full text
i = IndexOf(s, "@", 0)            # first @ position
prefix = SubString(s, 0, i)       # everything before the @

match iff:
  i >= 0                                             # @ exists
  AND SubString(s, i+1, len(s)-(i+1)) matches \S+?    # nickname: non-space run
  AND (i == 0                                       # (?<=^) at very start
       OR CharAt(s, i-1) in WHITESPACE              # (?<=\s)
       OR CharAt(s, i-1) == "\n"                    # (?<=^) after newline
          ... but CharAt(s, i-1) == "\n" is already
          covered by "\n" in WHITESPACE)
  AND (i+1+len(nick) == len(s)                       # (?=$)
       OR CharAt(s, i+1+len(nick)) in WHITESPACE)    # (?=\s)
```

The key insight: `(?<=^)` under MULTILINE collapses into "previous char
is `\n` or the string starts" — both expressible as `CharAt` checks. The
lookbehind never needed regex at all.

## Z3 encoding (sketch)

```python
s = String("s")
nick = String("nick")            # the capture
i = IndexOf(s, "@", 0)           # z3.IndexOf(StringVal s, StringVal "@", 0)

# nickname is a non-space run of length >= 1:
InRe(nick, Concat(Union(Range("!", "~")), Star(Union(Range("!", "~")))))
# (\\S over the printable range; tighten to the real alphabet if known)

constraints = [
    i >= 0,
    s == Concat(SubString(s, 0, i), "@", nick, SubString(s, i+1+Length(nick), 999)),
    # prefix boundary: start OR whitespace/newline before the @
    Or(i == 0, InRe(SubString(s, i-1, 1), WHITESPACE)),
    # suffix boundary: end OR whitespace after the nickname
    Or(i+1+Length(nick) == Length(s),
       InRe(SubString(s, i+1+Length(nick), 1), WHITESPACE)),
]
```

## When the rewrite is needed vs not

| Lookaround | Width | Verdict |
|---|---|---|
| `(?<=\s)` / `(?<!X)` (single char) | fixed | fold into the adjacent class — no rewrite |
| `(?<=^)` / `(?<=$)` WITHOUT MULTILINE | fixed (0) | `i == 0` check |
| `(?<=^)` / `(?<=$)` WITH MULTILINE | variable | **this rewrite** (previous char is `\n` or start) |
| `(?=...)` lookahead | — | see properties/fwlive-classifier.md (the fwlive decomposition route) |

## Checklist

- [ ] Fixed-width lookarounds folded into char classes first (cheap)
- [ ] Variable-width lookbehind rewritten with IndexOf/SubString/CharAt
- [ ] The `re.MULTILINE` flag is the tell — without it `(?<=^)` is
      width-0 and trivial
- [ ] Ground-truth the witness against the REAL pattern (build it exactly
      as the code does, flags included)
