"""Registered POSIX-shell regex extractor (dialect ``posix-shell``).

Extracts regex sites from shell code: grep/egrep/sed/awk quoted arguments,
``awk -F`` ERE field separators, and bash/ksh ``[[ $x =~ ERE ]]`` tests.
The extraction semantics are the P1-frozen heuristic (PR #259): a labeled
scanner, not a parser — false positives distort the P(compiles) distribution,
so precision guards are part of the contract.

Semantics (verified on GNU grep 3.11 + busybox 1.37, 2026-08-12):
- grep/egrep quoted args are BRE/ERE patterns; fgrep / ``grep -F`` args are
  LITERALS and are skipped; ``-i`` maps to the record ``flags`` field.
  ``egrep``/``-E`` → ``shell_flags.syntax = "ere"``; bare grep → ``"bre"``.
- sed contributes the search part of ``s///`` (any delimiter, call_kind
  ``substitution``) and ``/re/`` address forms only (call_kind ``search``);
  numeric addresses/ranges (e.g. ``1,20p``) are rejected.
  ``sed -i`` is in-place editing, NOT caseless — never mapped to flags.
- awk program text is skipped; ``awk '/re/'`` address forms and
  ``awk -F'ERE'`` field separators (spaced and glued) are extracted (ERE).
- ``[[ $x =~ PAT ]]`` extracts the UNQUOTED single-token RHS only (bash 3.2+:
  a quoted RHS is a literal string match, not a regex).  The LHS may be
  quoted (``[[ "$v" =~ ^[0-9]+$ ]]``).
- Matches inside comments (``#`` at line start / after whitespace or a shell
  separator) and quoted strings are NOT sites (context guard).
- No VERBOSE handling: literal spaces are load-bearing.

Known false negatives (documented, not code paths): ``-qE'pat'`` glued
flags+quote; ``[[ $x =~ foo\\ bar ]]`` escaped-space RHS; ``grep -P``
(PCRE-in-shell, rebranched); ``grep -qE'pat'`` whitespace gap.

Precision profile: the context guard is a labeled heuristic (quote/comment
state per line, backslash escapes outside single quotes — POSIX single
quotes treat backslash literally).  ``init.d/`` symlinks and extensionless
shebang files are covered by the registry glob + shebang sniff at the
registry/caller level, not here (this extractor receives ``src`` as a
string).
"""

from __future__ import annotations

import bisect
import re

from regexproof.extractors.record import make_record

# --- scanner regexes (frozen at P1, PR #259) --------------------------------

_SHELL_CMD = re.compile(
    r"(?<![A-Za-z0-9_\-])(?P<cmd>grep|egrep|fgrep|sed|awk)"  # shell token
    r"(?P<flags>(?:[ \t]+-[A-Za-z][A-Za-z0-9]*)*)"  # flag runs incl. separate flags
    r"[ \t]+(?P<e>-e[ \t]+|--regexp=[ \t]*)?"
    r"(?P<q>['\"])(?P<pat>.*?)(?P=q)"
)
_SHELL_BASH = re.compile(
    r"\[\[[ \t]+(?:\"[^\"]*\"|'[^']*'|[^ \t'\"]+)[ \t]+=~[ \t]+"
    r"(?P<pat>[^ \t'\"]+)[ \t]*\]\]"
)
_SHELL_AWK_F = re.compile(r"(?<![A-Za-z0-9_\-])awk[ \t]+-F(?P<q>['\"])(?P<pat>.*?)(?P=q)")

_SED_S = re.compile(r"^s(?P<d>[^A-Za-z0-9])(?P<search>.*?)(?P=d)")
_SED_ADDR = re.compile(r"^/(?P<re>[^/]+)/")

_FLAG_TOKEN = re.compile(r"-([A-Za-z][A-Za-z0-9]*)")


def _in_comment_or_string(src: str, pos: int) -> bool:
    """True if ``pos`` sits inside a shell comment or quoted string on its line.

    Labeled heuristic (P1-frozen + P3 command-substitution fix): scans the
    line from its start to ``pos`` tracking quote state (single/double),
    backslash escapes (unquoted/double-quoted/backtick context; POSIX single
    quotes treat backslash literally), comment markers (``#`` at line start
    or after whitespace or a shell separator ``; | & ( ) { }``, outside
    quotes — ``echo ok;# grep 'x'`` starts a comment), and COMMAND
    SUBSTITUTION: ``$( ... )`` (nested) and backticks are SHELL CODE — a
    ``"$(grep 'pat')"`` site is a real grep, not a string literal, so quotes
    open/close normally inside the substitution (P3 reconcile finding:
    the pre-fix guard suppressed every ``"$(cmd 'pat')"`` site — 80 phantom
    removals in the OpenWrt feed probe, e.g. golang-build.sh 6 real sites).
    """
    line_start = src.rfind("\n", 0, pos) + 1
    quote: str | None = None  # None | "'" | '"'
    frames: list[tuple[str, str | None]] = []  # (kind, saved quote) — sub/bt
    i = line_start
    while i < pos:
        c = src[i]
        if quote == "'":
            # POSIX: backslash is LITERAL inside single quotes — only the
            # closing quote matters (no substitution inside single quotes)
            if c == "'":
                quote = None
        elif c == "\\":
            i += 1  # escape — literal in unquoted/double-quoted/backtick
        elif quote == '"':
            if c == '"':
                quote = None
            elif c == "$" and i + 1 < pos and src[i + 1] == "(":
                frames.append(("sub", quote))  # nested parse context
                quote = None
                i += 1  # consume "("
            elif c == "`":
                frames.append(("bt", quote))
                quote = None
        elif frames and frames[-1][0] == "bt":
            if c == "`":
                _, saved = frames.pop()
                quote = saved
            elif c in ("'", '"'):
                quote = c  # substitution body is shell code
            elif c == "$" and i + 1 < pos and src[i + 1] == "(":
                frames.append(("sub", quote))
                quote = None
                i += 1
            elif c == "#" and (i == line_start or src[i - 1] in " \t;|&(){}"):
                return True
        elif frames and frames[-1][0] == "sub":
            if c == "$" and i + 1 < pos and src[i + 1] == "(":
                frames.append(("sub", quote))
                quote = None
                i += 1
            elif c == ")":
                _, saved = frames.pop()  # restore outer quote context
                quote = saved
            elif c == "`":
                frames.append(("bt", quote))
                quote = None
            elif c in ("'", '"'):
                quote = c  # substitution body is shell code
            elif c == "#" and (i == line_start or src[i - 1] in " \t;|&(){}"):
                return True
        elif c in ("'", '"'):
            quote = c
        elif c == "$" and i + 1 < pos and src[i + 1] == "(":
            frames.append(("sub", quote))
            quote = None
            i += 1  # consume "("
        elif c == "`":
            frames.append(("bt", quote))
            quote = None
        elif c == "#" and (i == line_start or src[i - 1] in " \t;|&(){}"):
            return True
        i += 1
    # frames exist only to make quote+comment state CORRECT inside command
    # substitutions — the position itself is SHELL CODE there, so only the
    # quote/comment state suppresses (P3 reconcile fix).
    return quote is not None


def _flag_letters(flags_src: str) -> str:
    """All short-flag letters from a flag run, e.g. ' -i -q' -> 'iq'."""
    return "".join(_FLAG_TOKEN.findall(flags_src or ""))


def _grep_mode(cmd: str, letters: str) -> str:
    """grep syntax selector: fixed (literal) > extended > basic (BRE)."""
    if cmd == "fgrep" or "F" in letters:
        return "fixed"
    if cmd == "egrep" or "E" in letters:
        return "extended"
    return "basic"


def extract_shell_posix(
    src: str, *, repo: str, file: str, dialect: str
) -> list[dict]:
    """Extract regex-site records from shell source text.

    ``dialect`` is REQUIRED by the registry wrapper (``dialect_kw=True``);
    callers pass ``"posix-shell"``.  ``column`` is the line-relative match
    offset (``match.start() - line_start``), feeding ``site`` = ``file:line:column``
    and the ``regex_id``.
    """
    nl = [m.start() for m in re.finditer("\n", src)]
    hits: list[tuple[int, dict]] = []

    def add(pos: int, pat: str, flags: str, shell_flags: dict,
            call_kind: str, snippet: str) -> None:
        if _in_comment_or_string(src, pos):
            return  # inside a comment or quoted string — not a real site
        if not pat or len(pat) < 2:
            return  # empty / 1-char patterns carry no signal
        line_start = src.rfind("\n", 0, pos) + 1
        rec = make_record(
            repo=repo,
            pattern=pat,
            flags=flags,
            dialect=dialect,
            call_kind=call_kind,
            file=file,
            line=bisect.bisect_left(nl, pos) + 1,
            column=pos - line_start,
            context_snippet=snippet[:500],
            extra_fields={"shell_flags": shell_flags},
        )
        hits.append((pos, rec))

    for m in _SHELL_CMD.finditer(src):
        cmd, pat = m.group("cmd"), m.group("pat")
        if not pat:
            continue
        letters = _flag_letters(m.group("flags"))
        if cmd in ("grep", "egrep", "fgrep"):
            mode = _grep_mode(cmd, letters)
            if mode == "fixed":
                continue  # fgrep / grep -F take LITERALS, not regexes
            flags = "i" if "i" in letters else ""
            shell_flags = {"syntax": "ere" if mode == "extended" else "bre",
                           "grep_mode": mode}
            add(m.start(), pat, flags, shell_flags, "search",
                src[m.start():m.end()])
        elif cmd == "sed":
            # s/// = substitution; /re/ address form = search
            sm = _SED_S.match(pat)
            if sm:
                add(m.start(), sm.group("search"), "",
                    {"syntax": "bre", "grep_mode": "basic"},
                    "substitution", src[m.start():m.end()])
                continue
            addr = _SED_ADDR.match(pat)
            if not addr:
                continue  # numeric address / range — not a regex
            add(m.start(), addr.group("re"), "",
                {"syntax": "bre", "grep_mode": "basic"},
                "search", src[m.start():m.end()])
        else:  # awk
            if "F" in letters:
                # -F 'ERE' — the quoted arg is the field-separator regex
                pass
            elif pat.startswith("/"):
                am = _SED_ADDR.match(pat)
                if not am:
                    continue
                pat = am.group("re")
            else:
                continue  # awk program text is not a regex literal
            add(m.start(), pat, "", {"syntax": "ere", "grep_mode": None},
                "search", src[m.start():m.end()])

    for m in _SHELL_AWK_F.finditer(src):
        add(m.start(), m.group("pat"), "", {"syntax": "ere", "grep_mode": None},
            "search", src[m.start():m.end()])

    for m in _SHELL_BASH.finditer(src):
        add(m.start(), m.group("pat"), "", {"syntax": "bash_ksh",
                                            "grep_mode": None},
            "search", src[m.start():m.end()])

    hits.sort(key=lambda h: h[0])
    return [r for _, r in hits]
