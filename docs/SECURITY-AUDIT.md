# Security-audit playbook for regexproof

How to audit **this repo's own security** (not the regexes it verifies) without
re-deriving the same context every time. Written after the 2026-08 audit wave
(issues #169–#177), where most of the elapsed time went to answering three
questions that this document now answers up front:

1. Is this input operator-supplied or attacker-supplied?
2. Is there already a guard for this, somewhere else in the tree?
3. Was this already looked at and deliberately declined?

For the *disclosure* policy on findings against third-party scanners, see
[`SECURITY.md`](../SECURITY.md). This file is about auditing regexproof itself.

---

## 1. Trust-boundary map — read this first

Almost every severity call in this repo reduces to "where did this string come
from". The answer is not obvious from the call site, so it is written down here.

| Input | Trust | Reaches | Audit as |
|---|---|---|---|
| Cloned repo file contents (admission probe) | **untrusted** | `admission/walk.py`, `admission/draft.py` | attacker-controlled bytes + attacker-controlled *filesystem layout* (symlinks, sizes, names) |
| Corpus regex patterns (`batch/corpora/`, mined repos) | **untrusted** | `compiler/*.py`, `helpers/*`, `redos/` | attacker-controlled argv to helper subprocesses; self-ReDoS and hang vectors |
| GitHub Code Search / API responses | **untrusted** | `mine/search.py` → `candidate-ledger.json`, `mine-queue.json` | attacker-influenced repo names, URLs, descriptions |
| `candidate-ledger.json` / `mine-queue.json` | **machine-written, auto-committed** | `admission/clone.py` (clone targets) | *not* human-reviewed — treat as untrusted, not as config |
| CLI arguments to `scripts/*.py` | **operator** | everywhere | operator input; `eval`/`RegExp` construction here is not a boundary |
| `ci/toolchain.toml`, `ci/python-matrix.toml` | **repo config** | `ci-assert-toolchain.py` | trusted; changes go through PR review |
| Environment variables (`REGEXPROOF_*`, `GITHUB_TOKEN`) | **operator / CI secret** | helpers, mine | assume env integrity; still validate paths that select executables |

**The load-bearing distinction:** an untrusted *pattern* is only ever passed as
a list-argv element (never through a shell), so the risk is **hang / resource
exhaustion**, not command injection. An untrusted *repo layout* is the opposite:
argv is irrelevant, and the risk is path traversal via symlinks. Classify the
finding by which of these two it is before reaching for a severity.

---

## 2. Controls that already exist — check before filing

A finding that one of these already covers is a false positive. Check here
first; it is faster than reading the call site.

| Control | Where | Covers |
|---|---|---|
| `reject_shell_subprocess_usage()` | `regexproof/fuzz/adapters.py:132` | static AST ban on `shell=True` in fuzz/ReDoS paths; wired into CI (`ci.yml:83-84`, `ci.yml:205-207`) |
| `ci-assert-toolchain.py --job {proof,golden,redos}` | `scripts/ci-assert-toolchain.py` | z3 5.0.x, Python/Node/Go majors, pcre2/yara/perl presence, npm + regexploit pins — **per CI job env** |
| z3 pin guard (exit 3) | `scripts/z3-verify.py:88-95`, `differential-fuzz.py:51`, `mirror-fidelity-gate.py:577` | refuses non-5.0.x solver at runtime |
| `default_output_path()` containment | `regexproof/admission/author.py:234-245` | `is_relative_to(properties/generated)` on the *default* path |
| Clone destination guard | `regexproof/admission/clone.py:70-76` | probe clones cannot land under `batch/corpora/` |
| `_MAX_FILE_BYTES` (2 MB) | `regexproof/admission/walk.py:26,54-58` | per-file read cap — **admission walk only**, not batch |
| Atomic write (temp + fsync + `os.replace`) | `regexproof/mine/ledger.py:53-66`, `regexproof/mine/queue.py:46-62` | ledger/queue only — batch NDJSON writers do *not* use this |
| Evidence gates | `regexproof/batch/evidence.py:12-35` | Z3 `timeout`/`unknown` is a hard fail for property kinds |
| Disclosure gate | `regexproof/batch/disclose.py:30-75` | `private_first` on security-tool corpora; no network publish |
| Witness redaction | `scripts/rule-diff-pilot.py:228-247` | long solver strings redacted in committed artifacts |
| Secret-scanning path ignores | `.github/secret_scanning.yml` | `paths-ignore` for fixture/pilot paths (gitleaks pilot artifacts) |
| GitHub search backoff | `regexproof/mine/search.py:73-109` | 429 retry — `search_code()` only, *not* `enrich_repo()` |

**Known asymmetries** (each is a real gap, each already has an issue — do not
re-file): admission walk has a size cap but batch extraction does not (#175);
ledger writes are atomic but batch NDJSON writes are not; `search_code` retries
but `enrich_repo` does not.

---

## 3. Settled decisions — do not re-file

These were examined and deliberately declined. Re-filing them wastes a review
cycle and erodes trust in the audit output. If you believe one should be
reopened, argue against the recorded rationale explicitly.

| Item | Decision | Rationale / where recorded |
|---|---|---|
| Floating action tags (`@v5`, `@v6`, `@v2`) not SHA-pinned | **won't fix** | Deliberate major-tag pinning, fleet standard. Code-scanning alert 6, dismissed 2026-08-09 |
| `new RegExp(pattern, flags)` from argv in `helpers/ecma/match.mjs` | **not a boundary** | Operator-supplied CLI args to a ground-truth replay harness. Comment at `match.mjs:7-9` |
| `eval()` on `--mirror-expr` | **not a boundary** | Same reasoning; 9-symbol namespace (`differential-fuzz.py:62-72`); `eval(..., {"__builtins__": {}}, MIRROR_NS)` at `differential-fuzz.py:168` |
| daily-mine commits after mine exit 1 | **deliberate** | Preserves partial progress; comment at `daily-mine.yml:76`. Hardening tracked in #173, but the behavior is intentional |
| Dependabot version updates disabled repo-wide | **deliberate** | `open-pull-requests-limit: 0` + ignore-all; security updates come from the repo-level setting instead |
| ReDoS analysis via Z3 | **out of scope** | Complexity analysis of the engine, not language membership — see `AGENTS.md` and `docs/REDOS.md` |

Suppression mechanics worth knowing: this repo uses CodeQL **default setup**
(weekly schedule, `extended` suite). In-file `// codeql[rule-id]` comments do
**not** clear alerts here — dismiss via the API instead:

```bash
gh api -X PATCH repos/lucas-albers-lz4/regexproof/code-scanning/alerts/<N> \
  -f state=dismissed -f dismissed_reason="won't fix" -f dismissed_comment="<why>"
```

---

## 4. Machine-checkable sweeps

Run these first. They are cheap, they produce file:line evidence, and they
cover the finding classes that have actually occurred in this repo.

```bash
# Prior art: existing alerts, and which were already dismissed and why.
gh api repos/lucas-albers-lz4/regexproof/code-scanning/alerts --paginate \
  | python3 -c 'import json,sys; [print(a["state"], a["rule"]["id"], a["most_recent_instance"]["location"]["path"], a.get("dismissed_reason")) for a in json.load(sys.stdin)]'

# Did a scan actually run since the last fix? (results_count > 0 = still firing)
gh api "repos/lucas-albers-lz4/regexproof/code-scanning/analyses?per_page=10" \
  | python3 -c 'import json,sys; [print(a["created_at"], a["commit_sha"][:8], a["results_count"], a["category"]) for a in json.load(sys.stdin)]'

# Don't re-file: search the full issue history, not just open issues.
gh issue list --state all --limit 200 --json number,title,state
```

```bash
# subprocess calls missing an explicit timeout= (hang / self-ReDoS surface)
python3 - <<'PY'
import ast, pathlib
for r in ("regexproof", "helpers", "scripts"):
    for f in sorted(pathlib.Path(r).rglob("*.py")):
        if "__pycache__" in str(f):
            continue
        try:
            tree = ast.parse(f.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        for n in ast.walk(tree):
            if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                    and isinstance(n.func.value, ast.Name) and n.func.value.id == "subprocess"
                    and n.func.attr in ("run", "check_output", "call", "Popen", "check_call")
                    and "timeout" not in {k.arg for k in n.keywords}):
                print(f"{f}:{n.lineno} subprocess.{n.func.attr}")
PY
```

```bash
# CI gates that cannot fail: a script run as a gate with no sys.exit/SystemExit.
for f in $(rg -o 'python scripts/[a-z0-9-]+\.py' .github/workflows/ | sed 's/.*python //' | sort -u); do
  rg -q 'sys\.exit|SystemExit' "$f" || echo "GATE CANNOT FAIL: $f"
done

# Fail-open shapes: error handlers that return success.
rg -n 'except[^:]*:\s*$' -A 3 regexproof/ | rg -n '"ok":\s*True|return True'

# Symlink-following reads over untrusted trees.
rg -n 'is_file\(\)|read_text\(' regexproof/admission/

# Silent failure: bare excepts that drop data inside loops.
rg -n 'except Exception:\s*$' -A 1 regexproof/ | rg -B1 'continue|pass'
```

These are not hypothetical. Every sweep above was run against `main` at the
close of the 2026-08 wave and reproduced a filed finding — and the fail-open
sweep found **one more** than manual review had: `compiler/ecma.py:38` carries
the same `{"ok": True, "helper": "…-missing"}` shape as `compiler/re2.py:51`
(both now on #172). Run the sweeps before reading code, not after.

---

## 5. Severity calibration for this repo

Standard CVSS intuitions mis-rank findings here, because regexproof is a
verification tool run by an operator on a workstation or in CI — not a network
service. Rank by these instead:

1. **A gate that cannot fail.** The product is trust in a proof. A green CI
   step that can never go red is the highest-severity class in this repo, above
   any conventional memory-safety or injection issue. `AGENTS.md` states the
   doctrine ("a harness that can't fail proves nothing"); audit against it.
   This is what #169 is.
2. **Fail-open on a soundness gate.** A helper that returns `ok: True` when it
   could not actually check anything (#172) produces *wrong proofs*, which is
   worse than producing no proof.
3. **Untrusted-repo → host filesystem or network egress.** Symlink reads (#170),
   unvalidated clone URLs (#174).
4. **Hang / resource exhaustion on untrusted patterns** (#171, #175). Real, but
   the blast radius is a stuck CI job.
5. **Supply-chain and credential scope** (#173, #176).

A finding that only matters if the operator is already compromised (env-var
control, malicious CLI args) is **low** — say so explicitly rather than filing
it at medium and letting the reader discover the caveat.

---

## 6. Filing convention

- Labels: `security` plus `audit-YYYY-MM` for the wave, and `reliability` /
  `bug` where they also apply.
- Every finding carries **file:line evidence and a reproduction command**. Cite
  code with fenced blocks including line ranges so the reader does not have to
  go looking.
- **Ground-truth before filing.** Same rule as for SAT witnesses in `AGENTS.md`:
  run the sweep, read the surrounding code, and confirm the guard is actually
  absent. The 2026-08 wave initially over-ranked "batch does not enforce the z3
  pin" before finding that `ci-assert-toolchain.py --job golden` already asserts
  it in the CI env — the remaining gap is local runs only, which is a different
  and much smaller finding.
- **State what you disproved**, not just what you found. A finding list without
  a "checked and clean" section is not auditable.
- Group genuinely-minor items into one batch issue (as #176 does) rather than
  filing five issues that each need their own triage.
- Non-trivial fixes follow the PR cycle in
  `.cursor/rules/pr-bugbot-before-merge.mdc`: CI green, then Bugbot on branch
  changes, then merge.

## 6a. Keeping this current

This playbook is only useful if citations stay true. Maintenance rule:

1. **Date-stamp the wave** in §7 when a new audit runs; do not silently rewrite
   history.
2. **Update controls / settled-decisions / asymmetries in the same PR** that
   lands a fix changing them (e.g. adding a size cap to batch extraction must
   edit the known-asymmetry row, not leave it stale).
3. **Re-run §4 sweeps** before filing a new wave; if a sweep no longer reproduces
   a listed finding, move that item from "open gap" to the audit-log outcome
   rather than leaving a false positive in the text.
4. Accept that line numbers drift — when a citation is wrong, fix the citation
   in the next touch; do not invent a separate CI job for line pins.

---

## 7. Audit log

| Wave | Scope | Outcome |
|---|---|---|
| 2026-08 | Full repo: command injection, code exec, path traversal, untrusted parsing, network/supply chain, secrets, GitHub Actions, DoS | 9 issues (#169–#177). Clean: no `shell=True` in production paths, no `pull_request_target`, no `pickle`/unsafe `yaml.load`, no archive extraction, no hardcoded credentials, `contents: read` default on the verify workflow |

Findings from the 2026-08 wave, for orientation on what this repo's issues
actually look like: #169 CI gate cannot fail · #170 symlink read from cloned
repo · #171 untimed subprocess (45 sites) · #172 compiler fail-open on missing
helper · #173 daily-mine write PAT · #174 unvalidated clone URL · #175 unbounded
batch reads · #176 low-severity hardening batch · #177 CodeQL suppression not in
effect.

Doc-review (#185) signed off 2026-08-10: citations corrected (`eval` line,
secret-scanning wording); severity ordering and settled-decisions registry
kept; mine ledger stays classified untrusted; maintenance = same-PR updates +
wave date-stamps (§6a).
