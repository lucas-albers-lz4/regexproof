"""Console-script dispatcher. Wave 12 (#581): ``regexproof newgate …``.

Does not wrap ``python -m regexproof.batch`` / ``probe`` / ``redos`` — those
stay module entry points. Unknown subcommands fail closed.
"""

from __future__ import annotations

import sys

USAGE = """regexproof — prove security properties of regexes with Z3

  regexproof newgate FILE PATTERN
  python -m regexproof.newgate FILE PATTERN

Consumer adoption (one regex → a CI gate): docs/NEWGATE.md
Operator corpus funnel (mine → rank → probe → gate → wave): docs/PIPELINE.md
"""


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in {"-h", "--help"}:
        print(USAGE.strip())
        return 0
    if argv[0] != "newgate":
        print(
            f"regexproof: unknown command {argv[0]!r} (expected newgate)",
            file=sys.stderr,
        )
        return 2
    from regexproof.newgate.cli import main as newgate_main

    try:
        rc = newgate_main(argv[1:])
    except SystemExit as exc:
        code = exc.code
        if code is None:
            return 0
        if isinstance(code, int):
            return code
        print(code, file=sys.stderr)
        return 1
    return int(rc)


if __name__ == "__main__":
    raise SystemExit(main())
