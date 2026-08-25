"""Ground-truth replay adapters — run the REAL engine for (dialect, call_kind).

P1 (#425) Workstream A2: the shared replay library Workstream B's synthesis
and diff-fuzz will consume. The adapter owns the ``call_kind`` wrap semantics
(the engine helpers are bare search runners), the batch-replay framing
contract, and the mapping onto the existing ``ground_truth_status``
vocabulary.

Transport rule (repo-wide, AGENTS.md / fuzz phase-1 gate): argv-only, never
``shell=True``, always with a timeout. The per-dialect argv shapes below are
the canonical fuzz-helper transports (``regexproof/fuzz/adapters.py``:
``real_accepts_argv`` / ``real_accepts_argv_bytes`` / ``real_accepts_perl`` /
``real_accepts_yara``) reused verbatim — this module adds the distinct
``timeout`` and ``engine-error`` outcomes those bool helpers collapse, so a
timeout is never misreported as a rejection.

Helper exit-code contract (all ``helpers/*/match.*`` subprocess dialects,
single-witness and batch modes)::

    0 = accepted (match found)
    1 = rejected (no match)
    2 = engine/compile error (invalid pattern, runtime engine error)
    3 = helper unavailable (missing binary / bindings / version pin)

So a compile failure is never misreported as a rejection (finding 5).

Result vocabulary (``ReplayResult.verdict``):
  accepted | rejected | engine-error | timeout | no-adapter |
  refused-no-callback

``ReplayResult.ground_truth_status`` maps onto the existing batch
``ground_truth_status`` vocabulary:
  - accepted/rejected → engine ran (final reproduced/failed needs the model's
    claim; use ``status_for_claim(result, model_claims_accept)``)
  - engine-error / timeout → ``failed``
  - no-adapter            → ``no-adapter`` (dialect has no helper today;
    selection-time skipping + ``synth_skipped_no_gt_adapter`` is P3/B-side)
  - refused-no-callback   → ``refused-no-callback`` (a helper that returned
    no callback — a HARD FAILURE under --require-ground-truth; raise it via
    ``require_replayable``)

``substitution`` call_kind has no adapter mode in v1 (counted as
``synth_skipped_substitution_call_kind`` by P3); the adapter marks it
``no-adapter``. ``classify_replayability`` is the selection-time classifier
P3's selector consumes (posix-shell / yara fullmatch+match →
``skipped_no_gt_adapter``, substitution → ``skipped_substitution``).
Production wiring: the P3 synthesis selector (B2/B7) calls
``classify_replayability`` / ``skip_reason`` at selection time to count skip
buckets and enforces the ``refused-no-callback`` hard-fail via
``require_replayable`` under ``--require-ground-truth`` — no selector exists
before P3 (P3 depends-on P1); the APIs + tests are this phase's deliverable.

Batch framing protocol (``replay_batch``; B6 diff-fuzz contract): ONE helper
subprocess per batch. Witnesses are written to the helper's stdin as a single
byte stream — each witness is escaped byte-wise (0x00 → ``\\0``, ``\\`` →
``\\\\``), escaped segments are joined with a raw NUL (0x00) and the stream is
terminated by a final NUL. Because escaped segments contain no raw NUL, NUL is
an unambiguous witness delimiter and witnesses containing NUL round-trip
exactly. The helper emits one per-witness verdict channel line on stdout::

    <index>:<verdict>     verdict ∈ {0 = rejected, 1 = accepted}

and exits 0 on success or 2 on a compile/engine error. v1 lands the real
framing for two dialects: ``ecma`` (``helpers/ecma/match.mjs batch``) and
``py_re`` (``helpers/python/match.py batch``). The remaining subprocess
dialects run one argv session per witness via ``replay`` (identical per-witness
semantics; single-session framing is the designed protocol for all dialects).
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from regexproof.compiler.re2 import replay_argv as _re2_replay_argv

_ROOT = Path(__file__).resolve().parents[2]

_ECMA_MATCH = _ROOT / "helpers" / "ecma" / "match.mjs"
_PY_MATCH = _ROOT / "helpers" / "python" / "match.py"
_PCRE2_MATCH = _ROOT / "helpers" / "pcre2" / "match.py"
_PERL_MATCH = _ROOT / "helpers" / "perl" / "match.py"
_YARA_MATCH = _ROOT / "helpers" / "yara" / "match.py"

# Helper exit-code contract (documented above): 2 = engine/compile error,
# 3 = helper unavailable.
_COMPILE_ERROR_RC = frozenset({2})
_UNAVAILABLE_RC = frozenset({3})

_SUBSTITUTION_NOTE = (
    "substitution call_kind has no adapter mode in v1 — P3 counts these as "
    "synth_skipped_substitution_call_kind"
)
_POSIX_SHELL_NOTE = (
    "posix-shell has no ground-truth helper today — P3 counts these as "
    "synth_skipped_no_gt_adapter"
)
_YARA_WRAP_NOTE = (
    "yara replay is substring-search only; fullmatch/match wrap is not "
    "supported in v1 — P3 counts these as synth_skipped_no_gt_adapter"
)


class ReplayVerdict(StrEnum):
    """Outcome of a single-witness replay against the real engine."""

    ACCEPTED = "accepted"
    REJECTED = "rejected"
    ENGINE_ERROR = "engine-error"
    TIMEOUT = "timeout"
    NO_ADAPTER = "no-adapter"
    REFUSED_NO_CALLBACK = "refused-no-callback"


class Replayability(StrEnum):
    """Selection-time classification of a site under --require-ground-truth.

    P3's selector calls :func:`classify_replayability` BEFORE selecting a site
    for replay: ``replayable`` sites are selected, the two ``skipped_*``
    values are counted (``synth_skipped_no_gt_adapter`` /
    ``synth_skipped_substitution_call_kind``) and never silently dropped.
    """

    REPLAYABLE = "replayable"
    SKIPPED_NO_GT_ADAPTER = "skipped_no_gt_adapter"
    SKIPPED_SUBSTITUTION = "skipped_substitution"


@dataclass(frozen=True)
class ReplayResult:
    """Result of one ``replay`` / ``replay_batch`` witness."""

    verdict: ReplayVerdict
    detail: str = ""

    @property
    def accepted(self) -> bool:
        return self.verdict is ReplayVerdict.ACCEPTED

    @property
    def ground_truth_status(self) -> str:
        """Map onto the batch ``ground_truth_status`` vocabulary.

        accepted/rejected are a definitive engine verdict; whether it
        *reproduces* the model's claim is decided against the claim via
        ``matches`` / ``status_for_claim`` (the mirror says "accepts" — the
        engine must accept for ``reproduced``).
        """
        if self.verdict is ReplayVerdict.NO_ADAPTER:
            return "no-adapter"
        if self.verdict is ReplayVerdict.REFUSED_NO_CALLBACK:
            return "refused-no-callback"
        if self.verdict in (ReplayVerdict.ACCEPTED, ReplayVerdict.REJECTED):
            return "reproduced"
        return "failed"

    def matches(self, model_claims_accept: bool) -> bool:
        """True iff the real engine's verdict agrees with the model's claim.

        The mirror claims ``model_claims_accept`` (e.g. "this witness is
        accepted by the regex"); ``reproduced`` means the engine agrees.
        """
        if self.verdict not in (ReplayVerdict.ACCEPTED, ReplayVerdict.REJECTED):
            return False
        return self.accepted == model_claims_accept


def status_for_claim(result: ReplayResult, model_claims_accept: bool) -> str:
    """Resolve the final ``ground_truth_status`` given the model's claim."""
    if result.verdict is ReplayVerdict.REFUSED_NO_CALLBACK:
        return "refused-no-callback"
    if result.verdict is ReplayVerdict.NO_ADAPTER:
        return "no-adapter"
    if result.verdict in (ReplayVerdict.ACCEPTED, ReplayVerdict.REJECTED):
        return "reproduced" if result.matches(model_claims_accept) else "failed"
    return "failed"


class RefusedNoCallbackError(RuntimeError):
    """A selected site's ``replay`` returned no callback.

    Raised by :func:`require_replayable` — the HARD-FAIL seam under
    --require-ground-truth. A site that passed selection
    (``classify_replayability == replayable``) must produce a definitive
    engine verdict; a handler that declined to call back means the
    ground-truth gate cannot run and CI must fail rather than silently skip.
    """


def classify_replayability(dialect: str, call_kind: str) -> Replayability:
    """Classify a site for selection: replayable or a counted skip.

    - posix-shell          → ``skipped_no_gt_adapter`` (no helper today)
    - substitution         → ``skipped_substitution`` (no v1 adapter mode)
    - yara fullmatch/match → ``skipped_no_gt_adapter`` (substring-only helper)
    - unknown dialect      → ``skipped_no_gt_adapter``
    - otherwise            → ``replayable``
    """
    if call_kind == "substitution":
        return Replayability.SKIPPED_SUBSTITUTION
    if dialect == "posix-shell":
        return Replayability.SKIPPED_NO_GT_ADAPTER
    if dialect == "yara" and call_kind in ("fullmatch", "match"):
        return Replayability.SKIPPED_NO_GT_ADAPTER
    if dialect not in _DISPATCH:
        return Replayability.SKIPPED_NO_GT_ADAPTER
    return Replayability.REPLAYABLE


def skip_reason(dialect: str, call_kind: str) -> str | None:
    """Human-readable note for a skipped site; None when replayable."""
    if classify_replayability(dialect, call_kind) is Replayability.REPLAYABLE:
        return None
    if call_kind == "substitution":
        return _SUBSTITUTION_NOTE
    if dialect == "posix-shell":
        return _POSIX_SHELL_NOTE
    if dialect == "yara" and call_kind in ("fullmatch", "match"):
        return _YARA_WRAP_NOTE
    return f"no ground-truth adapter for dialect {dialect!r}"


def require_replayable(result_or_verdict) -> None:
    """Hard-fail seam: raise :class:`RefusedNoCallbackError` when a selected
    site's replay returned ``refused-no-callback``.

    Accepts a ``ReplayResult`` or a bare ``ReplayVerdict``. Other verdicts
    (accepted/rejected/engine-error/timeout/no-adapter) pass — engine-error
    and timeout surface as ``failed`` ground truth, and no-adapter is handled
    at selection time by :func:`classify_replayability`.
    """
    verdict = (
        result_or_verdict.verdict
        if isinstance(result_or_verdict, ReplayResult)
        else result_or_verdict
    )
    if verdict is ReplayVerdict.REFUSED_NO_CALLBACK:
        raise RefusedNoCallbackError(
            "a selected site's replay returned no callback (refused-no-callback) — "
            "hard failure under --require-ground-truth"
        )


# ---------------------------------------------------------------------------
# call_kind wrap semantics (docs/SEMANTICS.md): the engine helpers are bare
# search runners, so the adapter emulates fullmatch / match by wrapping the
# pattern string. py_re honors call_kind in a timed subprocess instead.
# ---------------------------------------------------------------------------
def _subprocess_wrap(pattern: str, call_kind: str) -> str:
    """Wrap for the non-ECMA subprocess dialects (bare search runners).

    fullmatch uses ``\\z`` (absolute end): ``$`` matches before a trailing
    line terminator in Perl/PCRE/RE2, so a ``$``-wrapped fullmatch wrongly
    accepted ``a\\n`` while Python fullmatch rejects it. ``\\z`` is the
    absolute-end anchor for perl/pcre/re2.
    """
    if call_kind == "fullmatch":
        return f"^(?:{pattern})\\z"
    if call_kind == "match":
        return f"^(?:{pattern})"
    # search / exec: membership is a bare search
    return pattern


# ECMA fullmatch sentinel, written as the 6-char ASCII escape ``\u0000`` in the
# pattern SOURCE (argv cannot carry a raw NUL byte). JS ``new RegExp`` parses
# the escape back into the NUL character; the witness gets a raw NUL appended
# on stdin. The sentinel forces end-of-input ("$" would match before a trailing
# line terminator, and the sentinel does not match "." / "$" constructs).
_ECMA_SENTINEL = "\\u0000"


def _ecma_materialize(pattern: str, call_kind: str, witnesses):
    """Return ``(wrapped_pattern, payloads)`` for the ECMA helper.

    ECMA has no absolute-end anchor; fullmatch is encoded with a NUL sentinel:
    the pattern is wrapped as ``^(?:pattern)\\u0000`` and each witness gets a
    trailing NUL appended, forcing end-of-input. Verified against ``a\\n`` and
    ``a\\n\\u0000`` witnesses.
    """
    if call_kind == "fullmatch":
        # The appended NUL sentinel + "$" forces absolute end-of-input: a
        # witness that already ends in NUL leaves a trailing NUL after the
        # sentinel match, so "$" cannot match there (no line terminator), and
        # the payload always ends in the sentinel NUL, so "$" is never a
        # trailing-newline match.
        return f"^(?:{pattern}){_ECMA_SENTINEL}$", [w + "\x00" for w in witnesses]
    return _subprocess_wrap(pattern, call_kind), list(witnesses)


# ---------------------------------------------------------------------------
# Batch framing — one helper subprocess per batch (single-session stdin,
# per-witness verdict channel on stdout, NUL-safe round-trip).
# ---------------------------------------------------------------------------
def _encode_witness(witness: str) -> bytes:
    """Escape one witness for NUL-delimited framing (0x00 → `\\0`, `\\` → `\\\\`).

    Escaped segments contain no raw NUL, so NUL is an unambiguous delimiter
    and witnesses carrying NUL round-trip exactly.
    """
    out = bytearray()
    for byte in witness.encode("utf-8"):
        if byte == 0x00:
            out += b"\\0"
        elif byte == 0x5C:
            out += b"\\\\"
        else:
            out.append(byte)
    return bytes(out)


def _frame_witnesses(witnesses) -> bytes:
    """NUL-delimited single-session stdin stream for a batch of witnesses."""
    return b"\x00".join(_encode_witness(w) for w in witnesses) + b"\x00"


def _parse_batch_lines(stdout: str, n: int) -> list[ReplayVerdict] | None:
    """Parse the per-witness verdict channel (``<index>:<verdict>``, 0/1).

    Returns the verdicts in witness order, or None if the channel is
    malformed or missing any witness.
    """
    verdicts: dict[int, ReplayVerdict] = {}
    for line in stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        idx_s, sep, verdict = line.partition(":")
        if not sep or not idx_s.isdigit():
            return None
        idx = int(idx_s)
        if idx in verdicts:  # duplicate index — malformed channel
            return None
        if verdict == "1":
            verdicts[idx] = ReplayVerdict.ACCEPTED
        elif verdict == "0":
            verdicts[idx] = ReplayVerdict.REJECTED
        else:
            return None
    if len(verdicts) != n or any(i not in verdicts for i in range(n)):
        return None
    return [verdicts[i] for i in range(n)]


def _broadcast(result: ReplayResult, n: int) -> list[ReplayResult]:
    """Replicate one ReplayResult across all witnesses of a failed batch."""
    return [ReplayResult(result.verdict, result.detail) for _ in range(n)]


# ---------------------------------------------------------------------------
# subprocess transport — argv-only, shell=False, always timeout
# ---------------------------------------------------------------------------
def _subprocess_verdict(argv, data, *, text: bool, timeout_s: float):
    """Run the canonical helper argv; return a ReplayResult or a CompletedProcess."""
    try:
        return subprocess.run(
            list(argv),
            input=data,
            capture_output=True,
            text=text,
            shell=False,
            timeout=timeout_s,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return ReplayResult(
            ReplayVerdict.TIMEOUT,
            f"timeout after {timeout_s:g}s on {argv[0]}",
        )
    except OSError as exc:
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, f"spawn failed: {exc}")
    except ValueError as exc:  # argv cannot embed NUL / encoding errors
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, str(exc))


def _rc_result(
    proc,
    *,
    compile_error: frozenset[int] = frozenset(),
    unavailable: frozenset[int] = frozenset(),
    label: str = "helper",
) -> ReplayResult:
    """Map a helper exit code onto the verdict vocabulary.

    Exit-code contract: 0 = accepted, 1 = rejected, 2 = engine/compile error,
    3 = helper unavailable. ``compile_error`` / ``unavailable`` let dialects
    opt out of the contract where a helper predates it.
    """
    if proc.returncode == 0:
        return ReplayResult(ReplayVerdict.ACCEPTED)
    if proc.returncode == 1:
        return ReplayResult(ReplayVerdict.REJECTED)
    err = (proc.stderr or "").strip()
    if proc.returncode in compile_error:
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, err or f"{label} compile error")
    if proc.returncode in unavailable:
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, f"{label} unavailable")
    return ReplayResult(
        ReplayVerdict.ENGINE_ERROR,
        f"{label} exit {proc.returncode}: {err}",
    )


# ---------------------------------------------------------------------------
# py_re — timed `python -c`-style runner (helpers/python/match.py). Routed
# through a subprocess so `timeout_s` is ALWAYS honored: a catastrophic
# pattern can never block the gate in-process (finding 3). call_kind is
# honored by the runner directly (re.fullmatch/match/search) — no wrapping.
# ---------------------------------------------------------------------------
def _py_re_rc_result(proc, *, label: str = "py_re/match.py") -> ReplayResult:
    out = (proc.stdout or b"").decode("utf-8", "replace").strip()
    err = (proc.stderr or b"").decode("utf-8", "replace").strip()
    if proc.returncode == 0 and out == "accepted":
        return ReplayResult(ReplayVerdict.ACCEPTED)
    if proc.returncode == 1 and out == "rejected":
        return ReplayResult(ReplayVerdict.REJECTED)
    if proc.returncode in (0, 1):
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, f"bad verdict {out!r}")
    if proc.returncode == 2:
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, err or f"{label} engine error")
    return ReplayResult(
        ReplayVerdict.ENGINE_ERROR, f"{label} exit {proc.returncode}: {err}"
    )


def _py_re_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    proc = _subprocess_verdict(
        [sys.executable, str(_PY_MATCH), "match", call_kind, pattern, flags or ""],
        data=witness.encode("utf-8"),
        text=False,
        timeout_s=timeout_s,
    )
    if isinstance(proc, ReplayResult):
        return proc
    return _py_re_rc_result(proc)


# ---------------------------------------------------------------------------
# ecma — helpers/ecma/match.mjs is a bare .test() runner
# ---------------------------------------------------------------------------
def _ecma_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    wrapped, payloads = _ecma_materialize(pattern, call_kind, [witness])
    proc = _subprocess_verdict(
        ["node", str(_ECMA_MATCH), wrapped, flags or ""],
        data=payloads[0],
        text=True,
        timeout_s=timeout_s,
    )
    if isinstance(proc, ReplayResult):
        return proc
    return _rc_result(
        proc, compile_error=_COMPILE_ERROR_RC, label="ecma/match.mjs"
    )


# ---------------------------------------------------------------------------
# re2 — helpers/go-re2 (compiler.re2.replay_argv), MatchString = search
# ---------------------------------------------------------------------------
def _re2_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    wrapped = _subprocess_wrap(pattern, call_kind)
    try:
        argv = _re2_replay_argv(wrapped, flags or "")
    except RuntimeError as exc:
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, str(exc))
    proc = _subprocess_verdict(argv, data=witness, text=True, timeout_s=timeout_s)
    if isinstance(proc, ReplayResult):
        return proc
    return _rc_result(proc, compile_error=_COMPILE_ERROR_RC, label="go-re2")


def _helper_match_replay(
    match_script: Path,
    label: str,
    pattern,
    flags,
    call_kind,
    witness,
    *,
    timeout_s: float,
):
    """Template Method for pcre2/perl helpers/*/match.py stdin runners."""
    wrapped = _subprocess_wrap(pattern, call_kind)
    proc = _subprocess_verdict(
        [sys.executable, str(match_script), "match", wrapped, flags or ""],
        data=witness,
        text=True,
        timeout_s=timeout_s,
    )
    if isinstance(proc, ReplayResult):
        return proc
    return _rc_result(
        proc,
        compile_error=_COMPILE_ERROR_RC,
        unavailable=_UNAVAILABLE_RC,
        label=label,
    )


# ---------------------------------------------------------------------------
# pcre / perl — helpers/*/match.py, stdin search runners
# ---------------------------------------------------------------------------
def _pcre_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    return _helper_match_replay(
        _PCRE2_MATCH, "pcre2/match.py", pattern, flags, call_kind, witness,
        timeout_s=timeout_s,
    )


def _perl_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    return _helper_match_replay(
        _PERL_MATCH, "perl/match.py", pattern, flags, call_kind, witness,
        timeout_s=timeout_s,
    )


# ---------------------------------------------------------------------------
# yara — helpers/yara/match.py, temp-file replay (NUL-safe). YARA regex
# strings are substring-search only; fullmatch/match wrap is not expressible
# in v1 → no-adapter for those call_kinds (see classify_replayability).
# ---------------------------------------------------------------------------
def _yara_rule_src(pattern: str, flags: str) -> str:
    mods = []
    if "i" in flags:
        mods.append("nocase")
    if "W" in flags:
        mods.append("fullword")
    mod = (" " + " ".join(mods)) if mods else ""
    return f"rule gt_replay {{ strings: $a = /{pattern}/{mod} condition: $a }}"


def _yara_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    if call_kind not in ("search", "exec"):
        return ReplayResult(
            ReplayVerdict.NO_ADAPTER,
            _YARA_WRAP_NOTE,
        )
    if not _YARA_MATCH.is_file():
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, "yara helper missing")
    with tempfile.TemporaryDirectory(prefix="gt-replay-yara-") as tmp:
        tdir = Path(tmp)
        rule_path = tdir / "rule.yar"
        sample_path = tdir / "sample.bin"
        rule_path.write_text(_yara_rule_src(pattern, flags), encoding="utf-8")
        sample_path.write_bytes(witness if isinstance(witness, bytes) else witness.encode())
        proc = _subprocess_verdict(
            [sys.executable, str(_YARA_MATCH), "match", str(rule_path), str(sample_path)],
            data=None,
            text=False,
            timeout_s=timeout_s,
        )
    if isinstance(proc, ReplayResult):
        return proc
    return _rc_result(
        proc,
        compile_error=_COMPILE_ERROR_RC,
        unavailable=_UNAVAILABLE_RC,
        label="yara/match.py",
    )


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------
_DISPATCH = {
    "py_re": _py_re_replay,
    "ecma": _ecma_replay,
    "re2": _re2_replay,
    "pcre": _pcre_replay,
    "perl": _perl_replay,
    "yara": _yara_replay,
}


def has_adapter(dialect: str) -> bool:
    """True iff ``replay`` can reach a real engine for this dialect.

    posix-shell has no helper today (P3/B-side counts skipped sites as
    ``synth_skipped_no_gt_adapter``); the return here is the selection-time
    signal.
    """
    return dialect in _DISPATCH


def replay(
    pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    witness: str,
    *,
    timeout_s: float = 10.0,
) -> ReplayResult:
    """Run the real engine for (dialect, call_kind) on a single witness.

    Returns a ``ReplayResult`` (accepted/rejected/engine-error/timeout/
    no-adapter/refused-no-callback). A dialect handler returning no callback
    surfaces as ``refused-no-callback`` — a HARD FAILURE under
    --require-ground-truth (see :func:`require_replayable`).
    """
    if call_kind == "substitution":
        return ReplayResult(ReplayVerdict.NO_ADAPTER, _SUBSTITUTION_NOTE)
    if dialect == "posix-shell":
        return ReplayResult(ReplayVerdict.NO_ADAPTER, _POSIX_SHELL_NOTE)
    fn = _DISPATCH.get(dialect)
    if fn is None:
        return ReplayResult(
            ReplayVerdict.NO_ADAPTER, f"no ground-truth adapter for dialect {dialect!r}"
        )
    try:
        result = fn(pattern, flags, call_kind, witness, timeout_s=timeout_s)
    except Exception as exc:  # the adapter must never raise
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, f"{type(exc).__name__}: {exc}")
    if result is None:
        return ReplayResult(
            ReplayVerdict.REFUSED_NO_CALLBACK,
            f"dialect {dialect!r} handler returned no callback",
        )
    if not isinstance(result, ReplayResult):
        return ReplayResult(
            ReplayVerdict.ENGINE_ERROR,
            f"dialect {dialect!r} handler returned {type(result).__name__}",
        )
    return result


def replay_batch(
    pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    witnesses,
    *,
    timeout_s: float = 10.0,
) -> list[ReplayResult]:
    """Run the real engine over many witnesses; results align with input.

    Batch framing (B6 diff-fuzz contract): witnesses are NUL-escaped and
    NUL-delimited on a SINGLE stdin session and the helper emits one
    ``<index>:<verdict>`` token per line on stdout. v1 lands the real
    single-session framing for ``ecma`` and ``py_re``; the other subprocess
    dialects run one argv session per witness via ``replay`` (identical
    per-witness semantics). NUL witnesses round-trip exactly in every mode.
    """
    witnesses = list(witnesses)
    if not witnesses:
        return []
    if call_kind == "substitution":
        return [ReplayResult(ReplayVerdict.NO_ADAPTER, _SUBSTITUTION_NOTE) for _ in witnesses]
    if dialect == "posix-shell":
        return [ReplayResult(ReplayVerdict.NO_ADAPTER, _POSIX_SHELL_NOTE) for _ in witnesses]
    if dialect not in _DISPATCH:
        return [
            ReplayResult(
                ReplayVerdict.NO_ADAPTER, f"no ground-truth adapter for dialect {dialect!r}"
            )
            for _ in witnesses
        ]
    if dialect == "py_re":
        return _replay_batch_py_re(
            pattern, flags, call_kind, witnesses, timeout_s=timeout_s
        )
    if dialect == "ecma":
        return _ecma_replay_batch(
            pattern, flags, call_kind, witnesses, timeout_s=timeout_s
        )
    return [
        replay(pattern, flags, dialect, call_kind, w, timeout_s=timeout_s) for w in witnesses
    ]


def _replay_batch_py_re(pattern, flags, call_kind, witnesses, *, timeout_s: float):
    """py_re batch framing: one timed subprocess, NUL-framed stdin, verdicts
    on stdout. ``timeout_s`` bounds the whole session (the timeout contract
    wins over the plan's "in-process" wording — see finding 3)."""
    proc = _subprocess_verdict(
        [sys.executable, str(_PY_MATCH), "--batch", call_kind, pattern, flags or ""],
        data=_frame_witnesses(witnesses),
        text=False,
        timeout_s=timeout_s,
    )
    if isinstance(proc, ReplayResult):
        return _broadcast(proc, len(witnesses))
    if proc.returncode != 0:
        return _broadcast(_py_re_rc_result(proc), len(witnesses))
    parsed = _parse_batch_lines(
        (proc.stdout or b"").decode("utf-8", "replace"), len(witnesses)
    )
    if parsed is None:
        return _broadcast(
            ReplayResult(ReplayVerdict.ENGINE_ERROR, "malformed batch verdict channel"),
            len(witnesses),
        )
    return [ReplayResult(v) for v in parsed]


def _ecma_replay_batch(pattern, flags, call_kind, witnesses, *, timeout_s: float):
    """ecma batch framing: one node subprocess, NUL-framed stdin, verdicts on
    stdout (helpers/ecma/match.mjs batch)."""
    wrapped, payloads = _ecma_materialize(pattern, call_kind, witnesses)
    proc = _subprocess_verdict(
        ["node", str(_ECMA_MATCH), "--batch", wrapped, flags or ""],
        data=_frame_witnesses(payloads),
        text=False,
        timeout_s=timeout_s,
    )
    if isinstance(proc, ReplayResult):
        return _broadcast(proc, len(witnesses))
    if proc.returncode != 0:
        return _broadcast(
            _rc_result(proc, compile_error=_COMPILE_ERROR_RC, label="ecma/match.mjs"),
            len(witnesses),
        )
    parsed = _parse_batch_lines(
        (proc.stdout or b"").decode("utf-8", "replace"), len(witnesses)
    )
    if parsed is None:
        return _broadcast(
            ReplayResult(ReplayVerdict.ENGINE_ERROR, "malformed batch verdict channel"),
            len(witnesses),
        )
    return [ReplayResult(v) for v in parsed]
