"""Wave 12 (#581): ``python -m regexproof.newgate FILE PATTERN``.

Scaffold a complete property gate (Z3 shape-1 mirror, Python ``re`` ground
truth, argv-only differential fuzz, mutation guard, CI stub).

Bad args fail closed with ``SystemExit`` and a message. Never ``shell=True``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from regexproof.newgate.scaffold import (
    DEFAULT_FORBIDDEN,
    DEFAULT_MUTATIONS,
    ScaffoldRequest,
    default_slug,
    family_ident,
    scaffold,
    validate_slug,
)

USAGE = """regexproof newgate — scaffold a property gate from FILE + PATTERN

  python -m regexproof.newgate path/to/validators.py '^[a-z0-9._-]+$'
  python -m regexproof.newgate path/to/validators.py:^[a-z0-9._-]+$
  regexproof newgate --out gates/username path/to/validators.py '^[a-z]+$'

Dialect for this first cut is Python re (py_re). Consumer adoption walkthrough:
docs/NEWGATE.md. Operator corpus funnel: docs/PIPELINE.md (not this command).
"""


def split_file_pattern(token: str) -> tuple[Path, str]:
    """Split ``FILE:PATTERN`` on the longest existing-file prefix before a colon."""
    idxs = [i for i, ch in enumerate(token) if ch == ":"]
    if not idxs:
        raise SystemExit(
            "newgate: need FILE PATTERN or FILE:PATTERN "
            f"(got {token!r})"
        )
    for i in reversed(idxs):
        cand = Path(token[:i])
        if cand.is_file():
            pattern = token[i + 1 :]
            if not pattern:
                raise SystemExit("newgate: empty pattern")
            return cand, pattern
    raise SystemExit(
        f"newgate: FILE:PATTERN {token!r} — no existing file prefix"
    )


def parse_targets(positional: list[str]) -> tuple[Path, str]:
    if len(positional) >= 2:
        path = Path(positional[0])
        if not path.is_file():
            raise SystemExit(f"newgate: not a file: {path}")
        pattern = positional[1]
        if not pattern:
            raise SystemExit("newgate: empty pattern")
        extra = positional[2:]
        if extra:
            raise SystemExit(
                f"newgate: unexpected extra arguments: {extra!r}"
            )
        return path, pattern
    if len(positional) == 1:
        return split_file_pattern(positional[0])
    raise SystemExit("newgate: need FILE PATTERN or FILE:PATTERN")


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    ap = argparse.ArgumentParser(
        prog="python -m regexproof.newgate",
        description=USAGE,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=False,
    )
    ap.add_argument("-h", "--help", action="store_true", help="show help")
    ap.add_argument(
        "--out",
        default=None,
        help="output directory (default: gates/<slug>/)",
    )
    ap.add_argument("--slug", default=None, help="directory slug under gates/")
    ap.add_argument("--family", default=None, help="harness family id")
    ap.add_argument(
        "--regexproof-ref",
        default=None,
        dest="regexproof_ref",
        help="git SHA/tag pinned in generated ci.yml (default: this checkout HEAD)",
    )
    ap.add_argument(
        "--dialect",
        default="py_re",
        help="regex dialect (v1: py_re only)",
    )
    ap.add_argument(
        "--call-kind",
        default="fullmatch",
        dest="call_kind",
        help="engine usage: fullmatch|match|search|exec",
    )
    ap.add_argument(
        "--flags",
        default="",
        help="py_re flags string (e.g. 'a' for re.ASCII)",
    )
    ap.add_argument(
        "--chars",
        default=DEFAULT_FORBIDDEN,
        help="forbidden chars for shape-1 (skipped if already in the alphabet)",
    )
    ap.add_argument("--fuzz-runs", type=int, default=50, dest="fuzz_runs")
    ap.add_argument(
        "--exhaust-max-len",
        type=int,
        default=2,
        dest="exhaust_max_len",
    )
    ap.add_argument(
        "--fuzz-max-len",
        type=int,
        default=8,
        dest="fuzz_max_len",
        help="differential-fuzz --max-len (random/mutation strings)",
    )
    ap.add_argument(
        "--mutations",
        default=DEFAULT_MUTATIONS,
        help="dangerous chars spliced by differential-fuzz",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing scaffold files",
    )
    ap.add_argument("targets", nargs="*", help="FILE PATTERN or FILE:PATTERN")
    try:
        args = ap.parse_args(argv)
    except SystemExit as exc:
        code = exc.code
        if code in (0, None):
            return 0
        if isinstance(code, int):
            return code
        print(code, file=sys.stderr)
        return 1
    if args.help or not argv:
        print(USAGE.strip())
        print()
        ap.print_help()
        return 0
    source, pattern = parse_targets(list(args.targets))
    slug = validate_slug(args.slug or default_slug(source, pattern))
    family = args.family or family_ident(slug)
    out = Path(args.out) if args.out else Path("gates") / slug
    flags = str(args.flags or "").lower()
    pin = args.regexproof_ref or _default_regexproof_ref()
    result = scaffold(
        ScaffoldRequest(
            source_file=source,
            pattern=pattern,
            out=out,
            slug=slug,
            family=family,
            dialect=args.dialect,
            call_kind=args.call_kind,
            flags=flags,
            forbidden=args.chars,
            fuzz_runs=args.fuzz_runs,
            exhaust_max_len=args.exhaust_max_len,
            fuzz_max_len=args.fuzz_max_len,
            mutations=args.mutations,
            force=args.force,
            regexproof_ref=pin,
        )
    )
    print(f"newgate: wrote {result.out}")
    for name in result.files:
        print(f"  {name}")
    return 0


def _default_regexproof_ref() -> str:
    """Pin CI to this checkout's HEAD when run from a git tree."""
    import subprocess
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=False,
            capture_output=True,
            text=True,
            shell=False,
            timeout=10,
        )
    except OSError as exc:
        raise SystemExit(
            f"newgate: cannot resolve --regexproof-ref via git ({exc}); "
            "pass --regexproof-ref SHA"
        ) from exc
    if proc.returncode != 0:
        raise SystemExit(
            "newgate: pass --regexproof-ref SHA/tag "
            "(not running inside a regexproof git checkout)"
        )
    return proc.stdout.strip()


if __name__ == "__main__":
    raise SystemExit(main())
