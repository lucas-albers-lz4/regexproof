"""Argv-only differential-fuzz adapters (no shell=True)."""

from regexproof.fuzz.adapters import real_accepts_argv, reject_shell_subprocess_usage

__all__ = ["real_accepts_argv", "reject_shell_subprocess_usage"]
