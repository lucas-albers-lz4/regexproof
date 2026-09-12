# Calibration close-out

- Decision: **inconclusive**
- Cohort: `2026-09-12-calibration-10`
- Manifest digest: `17fe9320b68cda053032a0d517a452149409854c869d0de2aefbbef5e3d2a6e6`
- Continue to 20: **true**
- Continue to 30: **pending_20_repo_run**

Reason: incomplete calibration; rerun skipped repositories at their pins

Per-family outcomes:

- `ecma`: observed_but_closeout_blocked (3 repos)
- `go_re`: insufficient_data (1 repos)
- `posix-shell`: observed_but_closeout_blocked (2 repos)
- `py_re`: insufficient_data (1 repos)

Skipped/failed repositories:

- `Mininglamp-OSS/octo-server`: failed — inventory skipped 11 oversized file(s)
- `eReader/detekt`: failed — Missing parentheses in call to 'print'. Did you mean print(...)? (<unknown>, line 676)
- `x41x41x90/pm_shredder`: failed — Missing parentheses in call to 'print'. Did you mean print(...)? (<unknown>, line 9)
