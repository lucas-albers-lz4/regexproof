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
  NOTE (cumulative review finding #11): the ``len<2`` filter drops 1-char
  separators like ``-F ':'`` — a documented P1-frozen filter, not a bug.
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
    r"(?P<tail>(?:[ \t]+-[A-Za-z][A-Za-z0-9]*)*)"  # TRAILING flags (luna -r7 #1)
)
_SHELL_BASH = re.compile(
    r"\[\[[ \t]+(?:\"[^\"]*\"|'[^']*'|[^ \t'\"]+)[ \t]+=~[ \t]+"
    r"(?P<pat>[^ \t'\"]+)[ \t]*\]\]"
)
_SHELL_AWK_F = re.compile(r"(?<![A-Za-z0-9_\-])awk[ \t]+-F(?P<q>['\"])(?P<pat>.*?)(?P=q)")

def _sed_search(pat: str) -> str | None:
    """Search part of an ``s///`` substitution, honoring ``\\``-escaped
    delimiters (cumulative review finding #4: the old lazy regex stopped at
    the FIRST delimiter, truncating ``s/a\\/b/c/`` to ``a\\``).

    ``pat`` is the raw quoted arg (e.g. ``s/a\\/b/c/``). Returns the raw
    search text (backslash escapes preserved for the BRE/ERE normalize) or
    None when the arg is not an s/// substitution.  Unterminated forms
    (``sed 's'``, ``sed 's/foo'``) return None — GNU sed and busybox reject
    them (luna #276 finding #3).
    """
    if len(pat) < 2 or not pat.startswith("s"):
        return None
    d = pat[1]
    if d.isalnum() or d.isspace():
        return None
    out: list[str] = []
    closed = False
    i = 2
    while i < len(pat):
        c = pat[i]
        if c == "\\" and i + 1 < len(pat):
            out.append(c)
            out.append(pat[i + 1])
            i += 2
            continue
        if c == d:
            closed = True
            break
        out.append(c)
        i += 1
    if not closed:
        return None
    # the REPLACEMENT must have its own closing delimiter: s/foo/bar is
    # rejected by GNU sed AND busybox ("unterminated s command" — verified,
    # luna #276 -r6 finding #2); scan the remainder escape-aware
    i += 1
    while i < len(pat):
        if pat[i] == "\\" and i + 1 < len(pat):
            i += 2
            continue
        if pat[i] == d:
            return "".join(out)
        i += 1
    return None  # unterminated replacement


def _sed_addr(pat: str) -> str | None:
    """Regex of a ``/re/`` address form, honoring ``\\``-escaped
    delimiters; None for numeric addresses/ranges and unterminated forms."""
    if len(pat) < 2 or not pat.startswith("/"):
        return None
    out: list[str] = []
    i = 1
    while i < len(pat):
        c = pat[i]
        if c == "\\" and i + 1 < len(pat):
            out.append(c)
            out.append(pat[i + 1])
            i += 2
            continue
        if c == "/":
            return "".join(out)
        out.append(c)
        i += 1
    return None  # unterminated — GNU sed and busybox reject it

_FLAG_TOKEN = re.compile(r"-([A-Za-z][A-Za-z0-9]*)")

_HEREDOC_OPEN = re.compile(
    r"<<-?\s*(?:'([A-Za-z0-9_.-]+)'|\"([A-Za-z0-9_.-]+)\"|\\?([A-Za-z0-9_.-]+))")


def _blank_heredoc_bodies(src: str) -> str:
    """Blank heredoc body lines (cumulative review finding #7).

    Heredoc bodies are DATA, not shell code: ``cat <<'EOF'`` prints them
    literally; even an UNQUOTED delimiter (``<<EOF``) expands the body but
    never EXECUTES its lines, so a ``grep 'x'`` inside a body is not a
    site.  Line-oriented: an opener ``<<[-]?DELIM`` (quoted or not) blanks
    every following line until a line whose stripped content is DELIM.

    Body lines are replaced with SPACES (not removed) so every scan offset
    stays aligned with the original source (luna #276 finding #1).  Openers
    inside quoted strings/comments are ignored (guard re-use); the FIRST
    opener on a line wins; the delimiter charset is ``[A-Za-z0-9_-]+``
    (``EOF-1`` is a valid delimiter — luna finding #2).
    """
    lines = src.split("\n")
    line_offsets: list[int] = []
    acc = 0
    for ln in lines:
        line_offsets.append(acc)
        acc += len(ln) + 1
    i = 0
    while i < len(lines):
        line = lines[i]
        openers = []
        for m in _HEREDOC_OPEN.finditer(line):
            # ignore openers inside quotes/comments on the ORIGINAL line
            if not _in_comment_or_string(src, line_offsets[i] + m.start()):
                openers.append(m)
        # multiple openers on one line: `cat <<A <<B` — bodies are
        # SEQUENTIAL (luna #276 -r3 finding #4): each opener's body runs
        # until its own delimiter line
        for open_m in openers:
            delim = (open_m.group(1) or open_m.group(2)
                     or open_m.group(3))
            # quoted forms: 'EOF', "EOF", \EOF — pure data (blanked).
            # UNQUOTED (<<EOF) EXPANDS substitutions — $(grep 'x') in the
            # body is a REAL executed site, so those bodies stay live
            # (luna #276 -r6 finding #1); plain-line false positives in
            # unquoted bodies are a documented heuristic cost.
            after = open_m.group(0).split("<<", 1)[1].lstrip("-\t ")
            quoted = bool(open_m.group(1) or open_m.group(2)
                          or after[:1] == "\\")
            tab_ok = open_m.group(0).startswith("<<-")
            if not quoted:
                # unquoted body stays LIVE (expansions execute) — but still
                # ADVANCE past its terminator so a FOLLOWING opener's body
                # starts at the right line (mixed `cat <<A <<'B'` — luna
                # #276 -r7 finding #2)
                j = i + 1
                while j < len(lines):
                    if (lines[j].lstrip("\t") if tab_ok else lines[j]) == delim:
                        break
                    j += 1
                i = j
                continue
            j = i + 1
            while j < len(lines):
                # terminator must be EXACTLY the delimiter (no .strip():
                # ` EOF ` is NOT a valid terminator — luna #276 -r2 finding);
                # only the <<- form allows leading TABS
                if (lines[j].lstrip("\t") if tab_ok else lines[j]) == delim:
                    break
                lines[j] = " " * len(lines[j])  # keep offsets aligned
                j += 1
            i = j  # next opener's body starts after this terminator
        i += 1
    return "\n".join(lines)


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
    DOCUMENTED LIMITATION (cumulative review finding #6): a case-pattern
    terminator ``a)`` inside ``$( ... )`` pops the substitution frame early
    (the frame stack tracks ``(``/``)`` balance, not case-statement
    structure) — a full case parser is out of scope for this heuristic;
    such sites are undercounted.
    """
    line_start = src.rfind("\n", 0, pos) + 1
    quote: str | None = None  # None | "'" | '"'
    frames: list[tuple[str, str | None, int]] = []  # (kind, saved quote, depth)
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
                if i + 2 < pos and src[i + 2] == "(":
                    # $(( arithmetic — NOT a substitution; its `))` must not
                    # pop the outer $() frame (cumulative Reviewer B #4)
                    frames.append(("arith", quote, 0))
                    quote = None
                    i += 2  # consume "(("
                else:
                    frames.append(("sub", quote, 0))  # nested parse context
                    quote = None
                    i += 1  # consume "("
            elif c == "`":
                frames.append(("bt", quote, 0))
                quote = None
        elif frames and frames[-1][0] == "bt":
            if c == "`":
                _, saved, _ = frames.pop()
                quote = saved
            elif c in ("'", '"'):
                quote = c  # substitution body is shell code
            elif c == "$" and i + 1 < pos and src[i + 1] == "(":
                if i + 2 < pos and src[i + 2] == "(":
                    frames.append(("arith", quote, 0))
                    quote = None
                    i += 2
                else:
                    frames.append(("sub", quote, 0))
                    quote = None
                    i += 1
            elif c == "#" and (i == line_start or src[i - 1] in " \t;|&(){}"):
                return True
        elif frames and frames[-1][0] == "arith":
            # arithmetic body: close on `))` at the OUTER paren depth —
            # nested expression parens must not close it early (luna #276
            # -r3 finding #6: $((1+(2*3))) )
            depth = frames[-1][2]
            if c == "(":
                frames[-1] = ("arith", frames[-1][1], depth + 1)
            elif c == ")" and depth > 0:
                frames[-1] = ("arith", frames[-1][1], depth - 1)
            elif c == ")" and i + 1 < pos and src[i + 1] == ")":
                _, saved, _ = frames.pop()
                quote = saved
                i += 1  # consume the second ")"
            elif c == "$" and i + 1 < pos and src[i + 1] == "(":
                if i + 2 < pos and src[i + 2] == "(":
                    frames.append(("arith", quote, 0))
                    quote = None
                    i += 2
                else:
                    frames.append(("sub", quote, 0))
                    quote = None
                    i += 1
            elif c in ("'", '"'):
                quote = c
            elif c == "#" and (i == line_start or src[i - 1] in " \t;|&(){}"):
                return True
        elif frames and frames[-1][0] == "sub":
            # paren-depth tracking (luna #276 -r6 finding #4): a SUBSHELL
            # `( ... )` inside the substitution must not pop the $() frame
            # (x="$( (echo); grep 'real' f)" — the (echo) ) is balanced);
            # case-pattern `a)` terminators stay a documented limitation
            depth = frames[-1][2]
            if c == "(":
                frames[-1] = ("sub", frames[-1][1], depth + 1)
            elif c == ")" and depth > 0:
                frames[-1] = ("sub", frames[-1][1], depth - 1)
            elif c == ")":
                _, saved, _ = frames.pop()  # restore outer quote context
                quote = saved
            elif c == "$" and i + 1 < pos and src[i + 1] == "(":
                if i + 2 < pos and src[i + 2] == "(":
                    frames.append(("arith", quote, 0))
                    quote = None
                    i += 2
                else:
                    frames.append(("sub", quote, 0))
                    quote = None
                    i += 1
            elif c == "`":
                frames.append(("bt", quote, 0))
                quote = None
            elif c in ("'", '"'):
                quote = c  # substitution body is shell code
            elif c == "#" and (i == line_start or src[i - 1] in " \t;|&(){}"):
                return True
        elif c in ("'", '"'):
            quote = c
        elif c == "$" and i + 1 < pos and src[i + 1] == "(":
            if i + 2 < pos and src[i + 2] == "(":
                frames.append(("arith", quote, 0))
                quote = None
                i += 2
            else:
                frames.append(("sub", quote, 0))
                quote = None
                i += 1  # consume "("
        elif c == "`":
            frames.append(("bt", quote, 0))
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
    scan_src = _blank_heredoc_bodies(src)  # bodies are DATA, not code (#7)

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

    for m in _SHELL_CMD.finditer(scan_src):
        cmd, pat = m.group("cmd"), m.group("pat")
        if not pat:
            continue
        letters = (_flag_letters(m.group("flags"))
                   + _flag_letters(m.group("tail")))
        if cmd in ("grep", "egrep", "fgrep"):
            if "P" in letters:
                continue  # grep -P = PCRE-in-shell — documented false
                # negative (rebranched to a follow-on PCRE stream)
            mode = _grep_mode(cmd, letters)
            if mode == "fixed":
                continue  # fgrep / grep -F take LITERALS, not regexes
            flags = "i" if "i" in letters else ""
            shell_flags = {"syntax": "ere" if mode == "extended" else "bre",
                           "grep_mode": mode}
            add(m.start(), pat, flags, shell_flags, "search",
                src[m.start():m.end()])
        elif cmd == "sed":
            # -E/-r switch sed to ERE (GNU sed 4.x + busybox both support
            # -E; the mirror must match the executing engine, cumulative
            # review finding #1)
            sed_syntax = "ere" if ("E" in letters or "r" in letters) else "bre"
            # s/// = substitution; /re/ address form = search
            search = _sed_search(pat)
            if search is not None:
                add(m.start(), search, "",
                    {"syntax": sed_syntax, "grep_mode": "basic"},
                    "substitution", src[m.start():m.end()])
                continue
            addr = _sed_addr(pat)
            if not addr:
                continue  # numeric address / range — not a regex
            add(m.start(), addr, "",
                {"syntax": sed_syntax, "grep_mode": "basic"},
                "search", src[m.start():m.end()])
        else:  # awk
            if "F" in letters:
                # -F 'ERE' — the quoted arg is the field-separator regex
                pass
            elif pat.startswith("/"):
                am = _sed_addr(pat)
                if not am:
                    continue
                pat = am
            else:
                continue  # awk program text is not a regex literal
            add(m.start(), pat, "", {"syntax": "ere", "grep_mode": None},
                "search", src[m.start():m.end()])

    for m in _SHELL_AWK_F.finditer(scan_src):
        add(m.start(), m.group("pat"), "", {"syntax": "ere", "grep_mode": None},
            "search", src[m.start():m.end()])

    for m in _SHELL_BASH.finditer(scan_src):
        add(m.start(), m.group("pat"), "", {"syntax": "bash_ksh",
                                            "grep_mode": None},
            "search", src[m.start():m.end()])

    hits.sort(key=lambda h: h[0])
    return [r for _, r in hits]
