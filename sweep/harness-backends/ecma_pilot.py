#!/usr/bin/env python3
"""R9 ECMA-route pilot: fwlive classifier patterns (core/fwlive-log.js CLASSIFY_SPEC,
fetched 2026-08-11, master) through three routes:

  R1 real implementation  — node, pattern AS WRITTEN with its flags (ground truth)
  R2 ECMA route           — Noodler re.from_ecma2020, ASCII case-expanded (U4
                            explicit expansion; from_ecma2020 has no flags),
                            search-wrapped (full-match semantics)
  R3 mirror route         — stock z3 standard encoding, same case-expanded words

Probe corpus: exhaustive short strings over a boundary-focused alphabet + targeted
strings (the words, KV forms, boundary cases). Divergence = any disagreement between
routes. Declared input domain: ASCII (D14 scoping; \s gap NBSP/U+2028 noted).

Writes sweep/harness-backends/p1-baseline/ecma-pilot.json + ecma-pilot.md
"""
import sys, os, re, json, time, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import z3
from z3 import (String, InRe, Concat, Star, Union, Range, Re,
                StringVal)

NOODLER = os.environ.get("NOODLER", "/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared")
OUT = os.path.join(ROOT, "sweep", "harness-backends", "p1-baseline")

# ---- patterns (from fwlive core/fwlive-log.js, verbatim) ----
PREFIXES = "dnsmasq|procd|ubusd|netifd|odhcpd|logd|dropbear|uhttpd|hostapd|wpad"
HINTS = "fw4|nft|iptables|kernel|firewall"
ACTIONS = "ACCEPT|ALLOW|PASS|DROP|REJECT|DENY|BLOCK"
DENIES = "DROP|REJECT|DENY|BLOCK"
FLAGS = "SYN|ACK|FIN|RST|PSH|URG"
KVS = "IN|OUT|SRC|DST|PROTO|SPT|DPT|LEN|MAC|TYPE|CODE|TTL|TOS|PREC|DF"

PATTERNS = [
    ("NON_FIREWALL_PREFIX",
     r"^(" + PREFIXES + r")([^A-Za-z0-9_]|$)", "i"),
    ("FIREWALL_HINT",
     r"(^|[^A-Za-z0-9_])(" + HINTS + r")([^A-Za-z0-9_]|$)", "i"),
    ("ACTION_RE",
     r"(^|[^A-Za-z0-9_])(" + ACTIONS + r")([^A-Za-z0-9_]|$)", "i"),
    ("DENY_ACTION",
     r"(^|[^A-Za-z0-9_])(" + DENIES + r")([^A-Za-z0-9_]|$)", "i"),
    ("TCP_FLAG_TAIL",
     r"\b(" + FLAGS + r")(?:\s+(?:" + FLAGS + r"))*\s*$", "i"),
    ("NETFILTER_KV_GLUE",
     r"([^\s])(?=(IN|OUT|SRC|DST|PROTO|SPT|DPT|LEN|MAC|TYPE|CODE|TTL|TOS|PREC|DF)=)", "g"),
]

NONWORD = Union(Range("\x00", "/"), Range(":", "@"), Range("[", "^"),
                Re("`"), Range("{", "\x7f"))
SPACE = Union(Re(" "), Re("\t"), Re("\n"), Re("\r"), Re("\v"), Re("\f"))

def ci_word_str(w):
    return "".join(f"[{c}{c.swapcase()}]" for c in w)

def ci_alt_str(words):
    return "|".join(ci_word_str(w) for w in words.split("|"))

def ci_word_re(w):
    return Concat(*[Union(Re(c), Re(c.swapcase())) for c in w])

def alt_re(words):
    parts = [ci_word_re(w) for w in words.split("|")]
    return parts[0] if len(parts) == 1 else Union(*parts)

def ecma_pattern(name, pat, flags):
    """Search-wrapped from_ecma2020 form. i-flag: explicit ASCII expansion (U4).
    g-flag: search semantics already; the wrap makes full-match == search."""
    if "i" in flags:
        # expand the word alternations; boundary classes already case-complete
        pat2 = pat
        for words, expanded in ((PREFIXES, ci_alt_str(PREFIXES)), (HINTS, ci_alt_str(HINTS)),
                                (ACTIONS, ci_alt_str(ACTIONS)), (DENIES, ci_alt_str(DENIES)),
                                (FLAGS, ci_alt_str(FLAGS))):
            pat2 = pat2.replace("(" + words + ")", "(" + expanded + ")")
        pat = pat2
    return ".*" + pat + ".*"

def mirror_re(name, pat, flags):
    """Stock z3 standard encoding of the search language (full-match form).
    Boundary semantics: (X|$) means X OR END-OF-STRING — the end branch is NOT
    followed by anything (the epsilon-boundary bug class, fixed run 2)."""
    ANY = Star(Range("\x00", "\x7f"))
    if name == "NON_FIREWALL_PREFIX":
        pre = alt_re(PREFIXES)
        return Union(Concat(pre, NONWORD, ANY), pre)
    if name in ("FIREWALL_HINT", "ACTION_RE", "DENY_ACTION"):
        words = {"FIREWALL_HINT": HINTS, "ACTION_RE": ACTIONS, "DENY_ACTION": DENIES}[name]
        w = alt_re(words)
        return Union(Concat(w, NONWORD, ANY),           # W at start, boundary after
                     Concat(ANY, NONWORD, w, NONWORD, ANY),  # nonword before, boundary after
                     w,                                  # W alone (start + end boundary)
                     Concat(ANY, NONWORD, w))            # nonword before, W to end
    if name == "TCP_FLAG_TAIL":
        f = alt_re(FLAGS)
        one_or_more = lambda r: Concat(r, Star(r))
        tail = Star(Concat(one_or_more(SPACE), f))
        return Union(Concat(f, tail, Star(SPACE)),       # flag seq at start
                     Concat(ANY, NONWORD, f, tail, Star(SPACE)))  # nonword before
    if name == "NETFILTER_KV_GLUE":
        kv = alt_re(KVS)
        NS = Union(Range("\x00", "\x08"), Range("\x0e", "\x1f"), Range("\x21", "\x7f"))
        return Concat(ANY, NS, kv, Re("="), ANY)
    raise KeyError(name)

def probe_corpus():
    """Exhaustive short strings over a boundary-focused alphabet + targeted."""
    alpha = ["a", "A", "0", "_", " ", "\t", ".", ":"]
    strs = {""}
    for L in (1, 2, 3):
        for s in _gen(alpha, L):
            strs.add(s)
    # targeted: the words + boundary compositions + KV forms
    words = (PREFIXES + "|" + HINTS + "|" + ACTIONS + "|" + FLAGS).split("|") + ["IN=", "OUT=", "SRC="]
    for w in words:
        strs.update([w, w + " ", " " + w, w + "a", "a" + w, w + w, w + ":", w + "=",
                     "\t" + w, w + "\t", w.lower(), w.upper()])
    strs.update(["xIN=", "x IN=", "\tIN=", "x\nIN=", "eth0IN=", "a=bSRC=", "SYN ACK FIN",
                 "SYN  ACK", "x SYN", "SYN x", "drop", "DROP", "kernel:", "fw4",
                 "dnsmasq[1234]:", "procd:", "hostapd", "wpad.", "ACCEPT", "reject"])
    return sorted(strs, key=lambda s: (len(s), s))

def _gen(alpha, L):
    if L == 1:
        yield from alpha
    else:
        for p in _gen(alpha, L - 1):
            for c in alpha:
                yield p + c

def node_verdicts(pat, flags, strs):
    """R1: real JS implementation. A /g regex's .test() is STATEFUL — lastIndex
    must be reset per string or later tests start mid-string (luna finding)."""
    js = []
    for s in strs:
        js.append(json.dumps(s))
    src = f"""const r = new RegExp({json.dumps(pat)}, {json.dumps(flags)});
const strs = [{','.join(js)}];
for (const s of strs) {{ r.lastIndex = 0; process.stdout.write(r.test(s) ? '1' : '0'); }}
"""
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(src)
        path = f.name
    try:
        p = subprocess.run(["node", path], capture_output=True, text=True, timeout=60)
        bits = p.stdout.strip()
        if len(bits) != len(strs):
            raise RuntimeError(f"node bitstream mismatch: {len(bits)} vs {len(strs)}: {p.stderr[:200]}")
        return {s: b == "1" for s, b in zip(strs, bits)}
    finally:
        os.unlink(path)

def smt_string(s):
    """SMT-LIB string literal for the Noodler/Z3 dialect: RAW bytes, quote-doubling
    for quotes, NO python-style escapes. MEASURED: Noodler does NOT decode \\t/\\n
    short escapes in input (literal backslash-t) — writing raw bytes is the only
    faithful encoding (the escape-artifact bug class, found by this pilot)."""
    return '"' + s.replace('"', '""') + '"'

def noodler_ecma(pat_ecma, strs):
    """R2: from_ecma2020 membership per string. Records the first-line verdict AND
    the return code so abstentions are classified (unknown vs empty-output vs
    crash) — the report claims only what the committed JSON proves."""
    out = {}
    smt = ("(set-logic QF_SLIA)\n(declare-const s String)\n"
           f"(assert (str.in_re s (re.from_ecma2020 '{pat_ecma}')))\n")
    for s in strs:
        body = smt + f"(assert (= s {smt_string(s)}))\n(check-sat)\n"
        with tempfile.NamedTemporaryFile("w", suffix=".smt2", delete=False) as f:
            f.write(body)
            path = f.name
        try:
            p = subprocess.run([NOODLER, path], capture_output=True, text=True, timeout=35)
            first = p.stdout.strip().splitlines()[0] if p.stdout.strip() else "EMPTY"
            out[s] = (True if first == "sat" else
                      False if first == "unsat" else
                      f"{first}/rc={p.returncode}")
        finally:
            os.unlink(path)
    return out

def stock_mirror(mir, strs):
    """R3: stock z3 membership per string."""
    out = {}
    s = String("s")
    solver = z3.Solver()
    solver.add(InRe(s, mir))
    for st in strs:
        solver.push()
        solver.add(s == StringVal(st))
        r = solver.check()
        out[st] = (r == z3.sat)
        solver.pop()
    return out

def main():
    corpus = probe_corpus()
    print(f"corpus: {len(corpus)} strings")
    rows = []
    for name, pat, flags in PATTERNS:
        pat_ecma = ecma_pattern(name, pat, flags)
        mir = mirror_re(name, pat, flags)
        print(f"--- {name} ---")
        r1 = node_verdicts(pat, flags, corpus)
        r2 = noodler_ecma(pat_ecma, corpus)
        r3 = stock_mirror(mir, corpus)
        r3 = {s: (v if isinstance(v, bool) else v) for s, v in r3.items()}
        # classify
        d12 = [(s, r1[s], r2[s]) for s in corpus if r1[s] != r2[s] and isinstance(r2[s], bool)]
        d13 = [(s, r1[s], r3[s]) for s in corpus if r1[s] != r3[s] and isinstance(r3[s], bool)]
        d23 = [(s, r2[s], r3[s]) for s in corpus if r2[s] != r3[s] and isinstance(r2[s], bool) and isinstance(r3[s], bool)]
        abstains = [s for s in corpus if not isinstance(r2[s], bool)]
        rows.append({"pattern": name, "source": pat, "flags": flags,
                     "corpus": len(corpus),
                     "real_vs_ecma": [list(d) for d in d12],
                     "real_vs_mirror": [list(d) for d in d13],
                     "ecma_vs_mirror": [list(d) for d in d23],
                     "ecma_abstains": abstains[:10], "ecma_abstain_count": len(abstains)})
        print(f"  real-vs-ecma: {len(d12)} | real-vs-mirror: {len(d13)} | ecma-vs-mirror: {len(d23)} | ecma abstains: {len(abstains)}")
        for s, a, b in d12[:3]:
            print(f"    R1/R2: {s!r} real={a} ecma={b}")
        for s, a, b in d13[:3]:
            print(f"    R1/R3: {s!r} real={a} mirror={b}")
        for s, a, b in d23[:3]:
            print(f"    R2/R3: {s!r} ecma={a} mirror={b}")
    with open(os.path.join(OUT, "ecma-pilot.json"), "w") as f:
        json.dump(rows, f, indent=1, default=str)
    print(f"wrote {OUT}/ecma-pilot.json")

if __name__ == "__main__":
    main()
