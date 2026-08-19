"""Noodler CLI runner (design #213 D6 + S13, Phase 2 PR B).

Every mechanic below was measured and proven in Phase 1 (matrix_baseline.py,
blocker_probe.py, preflight.py — merged via #222/#224/#225):

- SMT-LIB input is written as RAW BYTES with quote-doubling only — never
  Python/JSON escapes (measured: Noodler reads ``\\t`` as literal backslash-t;
  the escape-input bug class, 4 occurrences root-caused in Phase 1).
- ``(set-logic QF_SLIA)`` always emitted (#344 hang class); ``(check-sat)``
  appended (sexpr emits none); ``model=true`` positional ONLY when witnesses
  are requested (get-model-after-unsat errors + exit 1).
- Process-group kill: ``Popen(start_new_session=True)`` + ``killpg`` on
  timeout (#171 timeout= discipline).
- Preamble-tolerant verdict parsing (``^(sat|unsat|unknown)$`` scan).
- S13 exit-code × verdict classification, literal: a signal-killed solver's
  output is UNTRUSTED even with a printed verdict (``rc < 0 or rc == 139`` →
  crash state); exit-1-with-verdict is VALID (get-model-after-unsat class);
  no-verdict states are explicit abstentions.
- Model parsing: Noodler CLI models have NO ``(model ...)`` wrapper — scan
  ``(define-fun NAME () String "..."`` directly with the quote-doubling /
  literal-backslash / ``\\xHH`` / ``\\u{}`` scanner.
"""

from __future__ import annotations

import os
import re
import subprocess
import time

NOODLER_ENV = "NOODLER"
DEFAULT_NOODLER = "/tmp/noodler/z3-noodler-ubuntu-24.04-x86_64-shared"
PIN_SHA256 = "22b19f123d3e7f54e10fdc46af3f91de23d89148c9a259eb072bc9e12f083464"
_VERIFIED_PATH = None  # cache: the sha256-verified binary for this process
MODEL_SCAN = re.compile(r'\(define-fun\s+(\S+)\s*\(\)\s*String\s*"')
HEX_ESC = re.compile(r"\\x([0-9a-fA-F]{2})")
UNI_ESC = re.compile(r"\\u\{([0-9a-fA-F]+)\}")


class NoodlerAbsent(Exception):
    """The Noodler binary is not available (env NOODLER unset and the default
    path missing). The harness records this as the triage_fallback state — an
    absence, never a failure and never a silent skip."""


def binary_path() -> str:
    """Resolve + sha256-verify the invoked binary (the pin is checked ONCE per
    process and cached — hashing 40 MB per query would dominate the wall clock).
    A binary whose hash does not match the pin is refused: an unverified binary
    is the exact risk the R8 pre-flight + R5 bump policy exist to prevent."""
    global _VERIFIED_PATH
    if _VERIFIED_PATH:
        return _VERIFIED_PATH
    import hashlib

    path = os.environ.get(NOODLER_ENV) or DEFAULT_NOODLER
    if not os.path.isfile(path):
        raise NoodlerAbsent(f"NOODLER binary not found at {path!r} "
                            "(set $NOODLER or run the Phase-1 pre-flight)")
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    if h != PIN_SHA256:
        raise NoodlerAbsent(
            f"NOODLER binary {path!r} sha256 {h[:16]}… does NOT match the pin "
            f"{PIN_SHA256[:16]}… — an unpinned binary is refused (R5 bump "
            "policy: run the pre-flight on the new binary and update the pin)"
        )
    _VERIFIED_PATH = path
    return path


def smt_string(s: str) -> str:
    """SMT-LIB string literal: RAW bytes with quote-doubling only. NO python
    escapes (measured: Noodler does not decode \\t/\\n short escapes)."""
    return '"' + s.replace('"', '""') + '"'


def decode_smt_string(text: str, i: int) -> tuple[str, int]:
    """Decode an SMT-LIB string literal starting at index i (which must point
    at a quote). Returns (value, next_index). Quote-doubling, literal
    backslash, \\xHH, \\u{...} — the measured scanner dialect."""
    assert text[i] == '"'
    i += 1
    out = []
    while i < len(text):
        c = text[i]
        if c == '"':
            if i + 1 < len(text) and text[i + 1] == '"':
                out.append('"')
                i += 2
                continue
            return "".join(out), i + 1
        if c == "\\" and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt == "x" and i + 4 < len(text):
                m = HEX_ESC.match(text, i)
                if m:
                    out.append(chr(int(m.group(1), 16)))
                    i += 4
                    continue
            if nxt == "u" and i + 3 < len(text) and text[i + 2] == "{":
                m = UNI_ESC.match(text, i)
                if m:
                    out.append(chr(int(m.group(1), 16)))
                    i = m.end()
                    continue
            # backslash is LITERAL in SMT-LIB input; the following char is
            # processed NORMALLY (it participates in quote-doubling — measured:
            # the P3-sed model `"\"""""""` decodes to backslash + 3 quotes only
            # when the quote after the backslash is doubled with the next one).
            out.append("\\")
            i += 1
            continue
        out.append(c)
        i += 1
    raise ValueError("unterminated SMT-LIB string literal")


def parse_noodler_model(out: str) -> dict | None:
    """Parse Noodler CLI model output into a witness dict. The model has NO
    (model ...) wrapper — define-fun list starts after the verdict."""
    w: dict = {}
    for m in MODEL_SCAN.finditer(out):
        name = m.group(1)
        try:
            val, _ = decode_smt_string(out, m.end() - 1)
        except ValueError:
            return None
        w[name] = val
    return w or None


def run_noodler(smt: str, timeout_ms: int = 30000, want_model: bool = False,
                binary: str | None = None) -> dict:
    """Run the Noodler CLI on the given SMT text. Returns the raw-evidence dict:

        {"verdict": "sat"|"unsat"|"unknown"|state, "rc": int,
         "wall_ms": float, "witness": dict|None, "state": "decided"|"abstain"}

    States (S13 literal): decided (verdict parsed, rc 0/1); ABSTAIN-TIMEOUT;
    ABSTAIN-SIGSEGV (signal death, rc < 0 or 139 — output untrusted);
    ABSTAIN-NO-VERDICT (rc 0, no verdict line); DISPATCH-ERROR (other rc).
    """
    import tempfile

    binary = binary or binary_path()
    # D6 wrapping, owned by the runner: set-logic prepended when absent (#344
    # hang class), (check-sat) appended (z3 sexpr emits none), (get-model)
    # appended ONLY when witnesses are requested (get-model-after-unsat errors).
    if not smt.lstrip().startswith("(set-logic"):
        smt = "(set-logic QF_SLIA)\n" + smt
    if not re.search(r"\(check-sat\)\s*$", smt):
        smt = smt + "(check-sat)\n"
    if want_model:
        smt = smt + "(get-model)\n"
    # RAW BYTES: write the exact text; quote-doubling handled by callers via
    # smt_string() — never json.dumps / repr escapes here.
    fd, path = tempfile.mkstemp(suffix=".smt2")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(smt)
    except Exception:
        os.unlink(path)
        raise
    args = [binary]
    if want_model:
        args.append("model=true")
    args.append(path)
    t0 = time.perf_counter()
    try:
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True, start_new_session=True)  # process-group
        try:
            out, _ = p.communicate(timeout=timeout_ms / 1000 + 5)
        except subprocess.TimeoutExpired:
            os.killpg(os.getpgid(p.pid), 9)  # process-group kill (D6)
            try:
                out, _ = p.communicate()
            except Exception:
                out = ""
            return {"verdict": "ABSTAIN-TIMEOUT", "rc": None, "wall_ms": None,
                    "witness": None, "state": "abstain"}
        rc = p.returncode
    except Exception as e:
        return {"verdict": f"DISPATCH-ERROR: {e}", "rc": None, "wall_ms": None,
                "witness": None, "state": "abstain"}
    finally:
        os.unlink(path)
    dt = round((time.perf_counter() - t0) * 1000, 1)
    if rc is not None and (rc < 0 or rc == 139):
        # signal death: output untrusted even with a printed verdict (S13)
        return {"verdict": f"ABSTAIN-SIGSEGV(rc={rc})", "rc": rc,
                "wall_ms": dt, "witness": None, "state": "abstain"}
    first = next((ln.strip() for ln in (out or "").splitlines()
                  if ln.strip() in ("sat", "unsat", "unknown")), None)
    if first is None:
        # S13: exit-1-no-verdict = dispatch error (the get-model-after-unsat
        # class is exit 1 WITH a verdict); exit-0-no-verdict = abstention.
        if rc == 1:
            return {"verdict": "DISPATCH-ERROR(rc=1)", "rc": rc,
                    "wall_ms": dt, "witness": None, "state": "abstain"}
        return {"verdict": f"ABSTAIN-NO-VERDICT(rc={rc})", "rc": rc,
                "wall_ms": dt, "witness": None, "state": "abstain"}
    if rc not in (0, 1):
        # S13 literal: only rc 0 or 1 with a verdict is a VALID result — a
        # crash/dispatch failure that printed a verdict line is still untrusted.
        return {"verdict": f"DISPATCH-ERROR(rc={rc})", "rc": rc,
                "wall_ms": dt, "witness": None, "state": "abstain"}
    witness = None
    if first == "sat" and want_model:
        witness = parse_noodler_model(out or "")
    return {"verdict": first, "rc": rc, "wall_ms": dt, "witness": witness,
            "state": "decided"}


def noodler_version(binary: str | None = None) -> str | None:
    """Record the INVOKED binary's version string (engine_versions). The
    caller MUST pass the resolved binary (binary_path()); None raises —
    never record a version for a binary that was not invoked
    (cumulative zen-MCR finding, mimo #3)."""
    if binary is None:
        raise ValueError("noodler_version requires the invoked binary path")
    try:
        p = subprocess.run([binary, "-version"], capture_output=True, text=True,
                           timeout=15)
        return (p.stdout + p.stderr).strip().splitlines()[0][:80] or None
    except Exception:
        return None
