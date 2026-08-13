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
    no callback — a HARD FAILURE under --require-ground-truth)

``substitution`` call_kind has no adapter mode in v1 (counted as
``synth_skipped_substitution_call_kind`` by P3); the adapter marks it
``no-adapter``.
"""

from __future__ import annotations

import re as _re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from regexproof.compiler.re2 import replay_argv as _re2_replay_argv

_ROOT = Path(__file__).resolve().parents[2]

_ECMA_MATCH = _ROOT / "helpers" / "ecma" / "match.mjs"
_PCRE2_MATCH = _ROOT / "helpers" / "pcre2" / "match.py"
_PERL_MATCH = _ROOT / "helpers" / "perl" / "match.py"
_YARA_MATCH = _ROOT / "helpers" / "yara" / "match.py"

_SUBSTITUTION_NOTE = (
    "substitution call_kind has no adapter mode in v1 — P3 counts these as "
    "synth_skipped_substitution_call_kind"
)
_POSIX_SHELL_NOTE = (
    "posix-shell has no ground-truth helper today — P3 counts these as "
    "synth_skipped_no_gt_adapter"
)


class ReplayVerdict(StrEnum):
    """Outcome of a single-witness replay against the real engine."""

    ACCEPTED = "accepted"
    REJECTED = "rejected"
    ENGINE_ERROR = "engine-error"
    TIMEOUT = "timeout"
    NO_ADAPTER = "no-adapter"
    REFUSED_NO_CALLBACK = "refused-no-callback"


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


# ---------------------------------------------------------------------------
# call_kind wrap semantics (docs/SEMANTICS.md): the engine helpers are bare
# search runners, so the adapter emulates fullmatch / match by wrapping the
# pattern string. py_re honors call_kind in-process instead.
# ---------------------------------------------------------------------------
def _wrap_pattern(pattern: str, call_kind: str) -> str:
    if call_kind == "fullmatch":
        return f"^(?:{pattern})$"
    if call_kind == "match":
        return f"^(?:{pattern})"
    # search / exec: membership is a bare search
    return pattern


# ---------------------------------------------------------------------------
# py_re — in-process `re`, call_kind honored directly
# ---------------------------------------------------------------------------
_PY_RE_FLAG_MAP = {
    "i": _re.IGNORECASE,
    "m": _re.MULTILINE,
    "s": _re.DOTALL,
    "x": _re.VERBOSE,
    "a": _re.ASCII,
    "u": _re.UNICODE,
}


def _py_re_flags(flags: str) -> int | None:
    bits = 0
    for ch in flags or "":
        if ch not in _PY_RE_FLAG_MAP:
            return None
        bits |= _PY_RE_FLAG_MAP[ch]
    return bits


def _py_re_match(rx, call_kind: str, witness: str) -> bool:
    # exec maps to search for membership (SEMANTICS.md).
    if call_kind == "fullmatch":
        return rx.fullmatch(witness) is not None
    if call_kind == "match":
        return rx.match(witness) is not None
    return rx.search(witness) is not None


def _py_re_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    fbits = _py_re_flags(flags)
    if fbits is None:
        return ReplayResult(
            ReplayVerdict.ENGINE_ERROR, f"unknown py_re flag in {flags!r}"
        )
    try:
        rx = _re.compile(pattern, fbits)
    except _re.error as exc:
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, f"re.compile: {exc}")
    try:
        return ReplayResult(
            ReplayVerdict.ACCEPTED
            if _py_re_match(rx, call_kind, witness)
            else ReplayVerdict.REJECTED
        )
    except _re.error as exc:  # e.g. catastrophic backtracking raised
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, str(exc))


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
# ecma — helpers/ecma/match.mjs is a bare .test() runner
# ---------------------------------------------------------------------------
def _ecma_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    wrapped = _wrap_pattern(pattern, call_kind)
    proc = _subprocess_verdict(
        ["node", str(_ECMA_MATCH), wrapped, flags or ""],
        data=witness,
        text=True,
        timeout_s=timeout_s,
    )
    if isinstance(proc, ReplayResult):
        return proc
    return _rc_result(proc, compile_error=frozenset({2}), label="ecma/match.mjs")


# ---------------------------------------------------------------------------
# re2 — helpers/go-re2 (compiler.re2.replay_argv), MatchString = search
# ---------------------------------------------------------------------------
def _re2_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    wrapped = _wrap_pattern(pattern, call_kind)
    try:
        argv = _re2_replay_argv(wrapped, flags or "")
    except RuntimeError as exc:
        return ReplayResult(ReplayVerdict.ENGINE_ERROR, str(exc))
    proc = _subprocess_verdict(argv, data=witness, text=True, timeout_s=timeout_s)
    if isinstance(proc, ReplayResult):
        return proc
    return _rc_result(proc, compile_error=frozenset({2}), label="go-re2")


# ---------------------------------------------------------------------------
# pcre / perl — helpers/*/match.py, stdin search runners
# ---------------------------------------------------------------------------
def _pcre_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    wrapped = _wrap_pattern(pattern, call_kind)
    proc = _subprocess_verdict(
        [sys.executable, str(_PCRE2_MATCH), "match", wrapped, flags or ""],
        data=witness,
        text=True,
        timeout_s=timeout_s,
    )
    if isinstance(proc, ReplayResult):
        return proc
    return _rc_result(proc, unavailable=frozenset({2}), label="pcre2/match.py")


def _perl_replay(pattern, flags, call_kind, witness, *, timeout_s: float):
    wrapped = _wrap_pattern(pattern, call_kind)
    proc = _subprocess_verdict(
        [sys.executable, str(_PERL_MATCH), "match", wrapped, flags or ""],
        data=witness,
        text=True,
        timeout_s=timeout_s,
    )
    if isinstance(proc, ReplayResult):
        return proc
    return _rc_result(
        proc,
        compile_error=frozenset({3}),
        unavailable=frozenset({2}),
        label="perl/match.py",
    )


# ---------------------------------------------------------------------------
# yara — helpers/yara/match.py, temp-file replay (NUL-safe). YARA regex
# strings are substring-search only; fullmatch/match wrap is not expressible
# in v1 → no-adapter for those call_kinds.
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
            "yara replay is substring-search only; fullmatch/match wrap is "
            "not supported in v1",
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
    return _rc_result(proc, unavailable=frozenset({2}), label="yara/match.py")


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
    --require-ground-truth.
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

    Batch framing (B6 diff-fuzz contract): witnesses are NUL-delimited on a
    single stdin session and the helper emits one ``<index>:<verdict>`` token
    per line on stdout. v1 implements the framing semantics in-process for
    ``py_re`` — compile the pattern once and loop (the reference framing:
    multi-witness, per-witness verdict channel, NUL-safe). Subprocess
    dialects run one full argv session per witness via ``replay``; the
    NUL-delimited single-session stdin transport is the designed protocol and
    is dispatched to when a framing-aware helper mode exists (B6).
    """
    witnesses = list(witnesses)
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
    return [
        replay(pattern, flags, dialect, call_kind, w, timeout_s=timeout_s) for w in witnesses
    ]


def _replay_batch_py_re(pattern, flags, call_kind, witnesses, *, timeout_s: float):
    """py_re batch framing reference: compile once, per-witness verdicts.

    NUL-safe (Python strings carry NUL); in-process, so ``timeout_s`` bounds
    each subprocess session, not the in-process match (callers must bound
    pattern/witness against in-process ReDoS).
    """
    fbits = _py_re_flags(flags)
    if fbits is None:
        return [
            ReplayResult(ReplayVerdict.ENGINE_ERROR, f"unknown py_re flag in {flags!r}")
            for _ in witnesses
        ]
    try:
        rx = _re.compile(pattern, fbits)
    except _re.error as exc:
        return [
            ReplayResult(ReplayVerdict.ENGINE_ERROR, f"re.compile: {exc}")
            for _ in witnesses
        ]
    out: list[ReplayResult] = []
    for w in witnesses:
        try:
            accepted = _py_re_match(rx, call_kind, w)
        except _re.error as exc:
            out.append(ReplayResult(ReplayVerdict.ENGINE_ERROR, str(exc)))
            continue
        out.append(
            ReplayResult(ReplayVerdict.ACCEPTED if accepted else ReplayVerdict.REJECTED)
        )
    return out
