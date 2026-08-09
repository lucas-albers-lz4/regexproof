# Wave-3 Phase 5 — testdata corpora (#116)

Three full-suite testdata corpora (not samples):

| Key | Upstream | Surface | Dialect | Expected files |
|---|---|---|---|---|
| `perl_tre` | Perl/perl5 `@6aef1e87…` | `t/re/*.t` + `re_tests` | perl | 81 |
| `go_regexp_tests` | golang/go `@e5ec1263…` | `src/regexp/**/*_test.go` | re2 | 9 |
| `v8_mjsunit` | v8/v8 `@15ce9d47…` | `test/mjsunit/**/regexp*.js` | ecma | 91 |

All are `corpus_type: testdata` — **exempt** from admission `gate_decision`
(same as `cpython_re` / `busybox` / `test262` / `pcre2_testdata` / `re2_testdata`).

## Fail-closed

- Missing `rules/` symlink root → `FileNotFoundError` / `SystemExit`
- Expected file count mismatch → `SystemExit HARD ERROR`
- Budget breach → `complete_run=false` on fraction artifact
- Unclassified `parse-error` reasons must stay at 0 (expected compile
  failures in `re_tests` are tagged `expected-compile-error`; helper
  stderr is mapped to named buckets via `_classify_perl_helper_error`)

## OOM hardening (measure) — fixed

Long suites (esp. `v8_mjsunit`) previously OOM-killed the host (~29 GiB)
when stacked agent measure processes ran without a hard cap. Mitigations
(verified: full v8 measure stays ~70 MiB RSS under the guarded path):

- `RLIMIT_AS` at 2× `max_mem_mb` inside `_compile_all`
- current VmRSS budget checks (`/proc/self/status`)
- `MemoryError` → `BudgetBreached`
- single-flight flock via `scripts/measure-p5-guarded.py`
- guarded path checks `max_patterns` on the full extract before chunking

Prefer the guarded wrapper for Wave-3 full-suite measures:

```bash
.venv/bin/python scripts/measure-p5-guarded.py perl_tre go_regexp_tests v8_mjsunit
```

## Mirror-fidelity

P1 fixtures `perl_re` / `go_regexp` unchanged. mjsunit mirror surface stays
deferred (issue non-goal for this slice).

## Measure

```bash
.venv/bin/python scripts/measure-p5-guarded.py perl_tre go_regexp_tests v8_mjsunit
# or (no flock / quieter progress):
# .venv/bin/python scripts/measure-corpus-fraction.py --corpus <name>
```
