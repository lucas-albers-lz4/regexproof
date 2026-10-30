# dogfood_shell corpus — Smith intake decision (funnel #615)

**Decision:** GO to mine. The frozen shell source snapshot is materialized at
`rules/` and registered in `WAVE_CORPORA`; this run uses the provenance record
in `source-pins.json` and `source-files.json`.

## Pinned materialization

The snapshot is from the four dogfooding repositories at the exact commits in
[`source-pins.json`](source-pins.json), fetched from their public GitHub
repositories on 2026-10-29. Each repository tree was materialized with
`git archive`; only files admitted by the batch shell file filter
(`regexproof.batch.extract._is_shell_script`) and within `MAX_FILE_BYTES` were
copied under `rules/<repository>/`, preserving their repository-relative
paths. The source trees contained no symlinks. The resulting snapshot contains
260 files (2,194,905 bytes). `source-files.json` records each path, upstream
URL and commit, byte count, and SHA-256. [`licenses.json`](licenses.json) and
[`licenses/`](licenses/) preserve the applicable upstream license texts.

All four repository pins are recorded for provenance, including happycow;
that repository contributed zero shell files accepted by the shell filter, so
no happycow source files are copied into this corpus. The included files come
from usrmanage and fwlive (Apache License 2.0) and hermes-agent (MIT License).

To reproduce the source snapshot from the pin record, fetch each listed commit,
run `git archive <commit>`, preserve its repository name as the top-level
folder, and select files with the repository's `_is_shell_script` filter and
`MAX_FILE_BYTES` limit. The committed per-file manifest lets CI verify the
materialized bytes without network access.

## Measurement

Run from the repository root:

```sh
python scripts/measure-corpus-fraction.py --corpus dogfood_shell --assert-determinism
```

The 2026-10-29 full-corpus result is **910/977 = 0.9314 encodable**. It has
zero parse errors, `complete_run=true`, no budget breaches, and passes the
0.30 fraction threshold. The measurement is committed at
[`properties/generated/dogfood_shell_encodable_fraction.json`](../../../properties/generated/dogfood_shell_encodable_fraction.json)
and its deterministic inventory at
[`properties/generated/dogfood_shell-inventory.ndjson`](../../../properties/generated/dogfood_shell-inventory.ndjson).
The report records Python 3.12.13, Z3 5.0.0, compiler fingerprint
`35ea1f238a9e`, and the source-pin digest. The CI job reruns this measurement
on Linux against the checked-in snapshot.

The schema-valid Smith decision is recorded at
[`properties/generated/dogfood_shell_smith_decision.json`](../../../properties/generated/dogfood_shell_smith_decision.json).
Host, toolchain, source-manifest digests, and report hashes are in
[`measurement-provenance.json`](measurement-provenance.json).

The dynamic shell expansion guard changes some old static classifications:
40 extracted rows contain active shell expansion and are now marked
`dynamic-shell-expansion`; five were previously counted as encodable and now
fail closed. The remaining 35 were already non-encodable under other reasons.
The 977-row count matches extraction from the complete pinned source trees.

## Prior intake and scope

The original admission decision remains at
[`properties/generated/dogfood_shell_gate_decision.json`](../../../properties/generated/dogfood_shell_gate_decision.json).
The frozen pins above refresh that earlier `corpus_pin: local` decision for
this materialized mine; the historical gate record is unchanged.

This corpus is not a security tool. Findings follow the repository's
public-first disclosure policy. It covers the POSIX shell regex surface only;
it does not remeasure the ECMAScript or Python regexes from the four source
repositories.

## Acceptance

- [x] A1 fractions measured and recorded with zero parse errors
- [x] A2 local pin resolved by a source-pinned materialized snapshot
- [x] A3 Smith intake decision recorded
- [x] B1 fwlive normalize idempotency contract with mutation guards and
      `dash`/BusyBox ground truth (conversion wave 1)
- [x] B2 conversion ledger contains the dogfood_shell property rows
- [x] Materialized snapshot admitted to `WAVE_CORPORA` and measured as a full
      deterministic run
