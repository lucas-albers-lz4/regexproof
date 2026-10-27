# Issue #448: admission clone timeout investigation

## Scope and decision

Read issue #448 through GitHub (tracking-only, three timeout candidates), the
repository instructions, `docs/PIPELINE.md`, `sweep/corpus-admission-gate.md`,
and the trust-boundary/control sections of `docs/SECURITY-AUDIT.md`.

**Keep the default 300 seconds. Add an explicit operator retry option to the
single-repo probe, not a global increase.** Measurements below do not establish
that any particular larger default would fix the three candidates. No ledger,
gate, conversion, workflow, or harness changes are part of this work.

```bash
python3 -m regexproof.probe --single https://github.com/OWNER/REPO \
  --pin REVIEWED_SHA --clone-timeout-sec 900 -o /tmp/retry-draft.json
```

900 is an example operator-selected cap, not a recommendation derived from the
measurements. Positive integer seconds are required at the CLI; the Python API
accepts finite positive seconds. Each git command gets its own timeout. With a
pin there are four commands: clone, rev-parse, fetch, checkout. This is **not** a
total probe deadline or a disk hard limit. The default remains 300 per command.
Successful probes still enforce existing pre/post-walk disk checks.

Timeouts now raise `CloneTimeoutError` (a `CloneError`) with phase, configured
limit, and monotonic elapsed seconds. The CLI returns 1, prints an incomplete
probe diagnostic, cleans its temporary clone, and does not walk or write a
draft. Existing output files remain untouched: operators must check exit status,
not mistake a previous output for a successful retry. No timeout becomes zero
regex sites or NO-GO. Library callers still own clone cleanup.

## What the implementation actually did

Before this change, `_default_run` had a 300s timeout, but `partial_clone` did
not expose an override or pass an explicit budget to its injected runner.
`subprocess.TimeoutExpired` escaped the single CLI's `except CloneError`;
its `finally` cleanup already ran. This was an uncontrolled traceback, **not**
an auto-NO-GO. The change gives that failure a retryable, measured diagnostic.

`git clone --filter=blob:none` is neither shallow nor `--no-checkout`: initial
checkout can fetch default-branch blobs before the walker starts. Fetching and
checking out a mined pin are additional commands. Thus “partial clone” does
not mean the checkout costs only tree metadata. Walker skip directories cannot
prune clone-time materialization in the current sequence.

`--allow-stale-pin` is checked only after clone/fetch/checkout succeeds. It
changes the stale-pin decision, not any git command or its budget. Regression
tests cover timeout with and without this flag, and with default/custom limits.

The batch path already records `clone_timeout` on clone/fetch failure and
returns before `fold_auto_nogo`; it measures successful `clone_ms`. It uses a
separate bare clone cache, and `lease_registry.PROBE_TTL_S` is 300 before lease
promotion. **This change does not add a batch override.** Safely lengthening
that path requires coordinating lease lifetime/renewal, not just forwarding a
larger subprocess cap. Its handling and focused cache tests remain unchanged.

## Existing evidence, not newly re-probed claims

Committed `sweep/funnel-2026-08-15/probes/` artifacts already contain:

| Candidate | Recorded regex sites | Extractor errors | Recorded pin_probed |
|---|---:|---:|---|
| Speech | 256 | 2 | `71820fbc750b1623b7746958a03cb25788942f90` |
| langflow | 1051 | 4 | `9ad57adbb3dcd7c9eda9eff9da94e51df7d4f713` |
| eliza | 0 | 0 | empty |

Speech/langflow artifacts refute “timeout implies no regex surface”, but do
not record clone timings or prove current network behavior. Eliza's empty
walked/probed pin and empty corpus pin do **not** establish a successful pinned
zero-site probe; no admission conclusion is drawn from it. None were modified.

## Bounded live measurements

Executed 2026-10-04 UTC in this checkout, Git 2.43.0. No large candidate was
cloned. Three unauthenticated repository metadata GETs used an 8s timeout and a
1MB response read ceiling; the complete command had a 30s harness deadline.
GitHub's `size` is reported repository KiB, **not** checkout size or expected
partial-clone transfer size:

| Candidate | API size (KiB) | GET wall seconds |
|---|---:|---:|
| NVIDIA-NeMo/Speech | 531415 | 0.439 |
| elizaOS/eliza | 2099148 | 0.431 |
| langflow-ai/langflow | 1598389 | 0.458 |

For a small control, two fresh clones of `octocat/Hello-World` were run
sequentially with a 20s per-clone cap (45s whole-command deadline), measured
with `time.monotonic`, and automatically deleted:

| Clone mode | Exit | Wall seconds | Materialized file bytes including .git |
|---|---:|---:|---:|
| `--filter=blob:none` | 0 | 1.101 | 31882 |
| full | 0 | 0.556 | 30612 |

The filtered control was slower and slightly larger in this single trial.
This demonstrates reachability and that filtering has overhead on tiny repos,
**not** that full clones are preferable for the large candidates. No transport
byte measurement was made. Disk bytes are summed file lengths, not allocated
blocks. Network/cache variability prevents extrapolating these times.

Reproduce the bounded small-clone comparison (do not substitute the large
candidates without a separate resource plan):

```bash
python3 - <<'PY'
import json, pathlib, subprocess, tempfile, time
for filtered in (True, False):
    with tempfile.TemporaryDirectory(prefix='rp448-small-') as d:
        dest = pathlib.Path(d) / 'repo'
        argv = ['git', 'clone'] + (['--filter=blob:none'] if filtered else [])
        argv += ['https://github.com/octocat/Hello-World.git', str(dest)]
        started = time.monotonic()
        try:
            p = subprocess.run(argv, capture_output=True, text=True, timeout=20)
            result = {'filtered': filtered, 'returncode': p.returncode,
                      'stderr': p.stderr[-1000:]}
        except subprocess.TimeoutExpired:
            result = {'filtered': filtered, 'result': 'timeout'}
        result['wall_sec'] = round(time.monotonic() - started, 3)
        result['disk_bytes'] = sum(p.stat().st_size for p in dest.rglob('*')
                                   if p.is_file()) if dest.exists() else 0
        print(json.dumps(result))
PY
```

Reproduce metadata only (at most three requests, no clone):

```bash
python3 - <<'PY'
import json, time, urllib.request
for repo in ['NVIDIA-NeMo/Speech', 'elizaOS/eliza', 'langflow-ai/langflow']:
    started = time.monotonic()
    try:
        req = urllib.request.Request('https://api.github.com/repos/' + repo,
            headers={'User-Agent': 'regexproof-issue-448-investigation'})
        with urllib.request.urlopen(req, timeout=8) as response:
            data = json.loads(response.read(1000000))
        print(repo, data.get('size'), round(time.monotonic() - started, 3))
    except Exception as exc:
        print(repo, type(exc).__name__, str(exc))
PY
```

## Regression gate and remaining issue criteria

```bash
.venv/bin/python -m pytest -q tests/test_admission_clone_timeout.py \
  tests/test_probe_admission_walker.py tests/test_lease_cache_batch.py
# 87 passed
.venv/bin/ruff check regexproof/admission/clone.py \
  scripts/probe-corpus-admission.py tests/test_admission_clone_timeout.py
# All checks passed
```

New coverage includes all four timed phases, default 300 and custom 900
propagation, finite-positive API validation before destination mutation, CLI
usage errors, a real bounded subprocess timeout, canonical CLI forwarding,
cleanup/no-walk/no-output on timeout, stale-pin independence, and preservation
of existing output. Tests do not use the network.

Still unresolved for full issue closure:

- Re-probe each candidate at an explicitly reviewed pin with recorded cap,
  phase times, resulting pins, materialized size, and extraction errors.
- Measure filtered versus full behavior on the actual candidates under an
  approved disk/time budget; tiny-control measurements are not that comparison.
- Determine whether their bottleneck is fetch, checkout/materialization,
  network, or walking before proposing a global cap increase or sparse checkout.
- If a batch override is needed, separately address its 300s probe lease and
  keep timeout failures outside the admission decision path.

This is a bounded operator-control improvement, not evidence that #448's three
large-repository retry criteria are complete.
