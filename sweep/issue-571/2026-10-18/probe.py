#!/usr/bin/env python3
"""Reproducible, bounded Noodler diagnostics for regexproof issue 571.

Requires explicit PROBE_DIR, SOURCE_FILE, FWLIVE_REPO, REGEXPROOF_REPO,
NOODLER_BIN, and NOODLER_SHA256 environment variables. It writes only text
artifacts beneath PROBE_DIR, disables core dumps, and never changes a repo.
"""
import hashlib
import json
import os
import pathlib
import resource
import signal
import subprocess
import sys
import time

FROZEN_SOURCE_SHA256 = '52983d7c0a629de4ee23a13873e5ac54cf7d08dfaf03383614fceb59a4d1da12'
FROZEN_SOURCE_GIT_BLOB = 'cc77bc663fc1bae0b2cb473eca2f10b2eedc2079'
APPROVED_NOODLER_BINARIES = {
    '22b19f123d3e7f54e10fdc46af3f91de23d89148c9a259eb072bc9e12f083464': {
        'label': 'Noodler 1.6.1 issue-comment baseline',
        'version': 'Z3 version 4.16.0 - 64 bit - build hashcode dcce9d2d129e1ecc101946ef257aa7ed246dfe61 - mata hashcode 8db4279ce9910b2c12589fabffebf8265a75b558',
    },
    '4a39a2b9e9066a8bfbe8b5363a85de82e43e27688b7dff456f4cd577bb47bab6': {
        'label': 'Noodler 1.8.0 verified release asset',
        'version': 'Z3 version 5.1.0 - 64 bit - build hashcode 06e5c132a1a59fb61eaf4e5f7094860b5aec7c21 - mata hashcode d28368a6957a1606162aea3fbe77345f6e1e13d5',
    },
}
PER_PROCESS_LIMIT_S = 8.0
INVOCATION_LIMIT_S = 20.0
STARTED = time.monotonic()


def env_path(name):
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f'{name} must be set explicitly')
    return pathlib.Path(value).expanduser().resolve()


PROBE_DIR = env_path('PROBE_DIR')
SOURCE_FILE = env_path('SOURCE_FILE')
FWLIVE_REPO = env_path('FWLIVE_REPO')
REGEXPROOF_REPO = env_path('REGEXPROOF_REPO')
NOODLER_BIN = env_path('NOODLER_BIN')
EXPECTED_NOODLER_SHA256 = os.environ.get('NOODLER_SHA256', '').lower()
if len(EXPECTED_NOODLER_SHA256) != 64 or any(c not in '0123456789abcdef' for c in EXPECTED_NOODLER_SHA256):
    raise SystemExit('NOODLER_SHA256 must be an explicit 64-character SHA-256 pin')
if EXPECTED_NOODLER_SHA256 not in APPROVED_NOODLER_BINARIES:
    raise SystemExit('unsupported research binary pin; this snapshot covers only the two recorded releases')


def sha256(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def child_preexec():
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def run_bounded(argv, *, cwd=PROBE_DIR, timeout=PER_PROCESS_LIMIT_S):
    remaining = INVOCATION_LIMIT_S - (time.monotonic() - STARTED)
    if remaining <= 0:
        return {
            'argv': [str(item) for item in argv], 'timeout_seconds': 0,
            'elapsed_ms': 0, 'returncode': None, 'timed_out': False,
            'classification': 'not_started_invocation_budget_exhausted',
            'stdout': '', 'stderr': '',
        }
    timeout = min(timeout, remaining)
    started = time.monotonic()
    process = subprocess.Popen(
        [str(item) for item in argv], cwd=cwd, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True, start_new_session=True,
        preexec_fn=child_preexec,
    )
    timed_out = False
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        stdout, stderr = process.communicate()
    elapsed_ms = round((time.monotonic() - started) * 1000, 3)
    if timed_out:
        classification = 'timeout_not_proven'
    elif process.returncode < 0:
        classification = f'crash_signal_{-process.returncode}'
    elif process.returncode != 0:
        classification = 'nonzero_backend_or_parser_error'
    else:
        first = stdout.strip().splitlines()[0] if stdout.strip() else ''
        classification = first if first in {'sat', 'unsat', 'unknown'} else 'zero_exit_without_verdict'
    return {
        'argv': [str(item) for item in argv], 'timeout_seconds': timeout,
        'elapsed_ms': elapsed_ms, 'returncode': process.returncode,
        'timed_out': timed_out, 'classification': classification,
        'stdout': stdout, 'stderr': stderr,
    }


def git(*args):
    result = subprocess.run(
        ['git', *map(str, args)], check=True, capture_output=True,
        text=True, timeout=min(PER_PROCESS_LIMIT_S, max(0.1, INVOCATION_LIMIT_S - (time.monotonic() - STARTED))),
    )
    return result.stdout.strip()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def initialize():
    PROBE_DIR.mkdir(parents=True, exist_ok=True)
    if not SOURCE_FILE.is_file() or not NOODLER_BIN.is_file():
        raise SystemExit('SOURCE_FILE and NOODLER_BIN must name existing files')
    if not os.access(NOODLER_BIN, os.X_OK):
        raise SystemExit('NOODLER_BIN is not executable')

    actual_source_sha256 = sha256(SOURCE_FILE)
    if actual_source_sha256 != FROZEN_SOURCE_SHA256:
        raise SystemExit(f'frozen fwlive source SHA-256 mismatch: {actual_source_sha256}')
    actual_binary_sha256 = sha256(NOODLER_BIN)
    if actual_binary_sha256 != EXPECTED_NOODLER_SHA256:
        raise SystemExit(f'Noodler binary SHA-256 mismatch: {actual_binary_sha256}')

    source_relative = SOURCE_FILE.relative_to(FWLIVE_REPO).as_posix()
    source_git_blob = git('-C', FWLIVE_REPO, 'hash-object', SOURCE_FILE)
    if source_git_blob != FROZEN_SOURCE_GIT_BLOB:
        raise SystemExit(f'frozen fwlive Git blob mismatch: {source_git_blob}')
    fwlive_head = git('-C', FWLIVE_REPO, 'rev-parse', 'HEAD')
    head_blob = git('-C', FWLIVE_REPO, 'rev-parse', f'HEAD:{source_relative}')
    if head_blob != source_git_blob:
        raise SystemExit('SOURCE_FILE bytes do not match the selected FWLIVE_REPO HEAD tree')
    source_last_changed_commit = git('-C', FWLIVE_REPO, 'log', '-1', '--format=%H', '--', source_relative)
    changed_commit_blob = git('-C', FWLIVE_REPO, 'rev-parse', f'{source_last_changed_commit}:{source_relative}')
    if changed_commit_blob != source_git_blob:
        raise SystemExit('latest source-changing commit does not contain the frozen source blob')

    regexproof_head = git('-C', REGEXPROOF_REPO, 'rev-parse', 'HEAD')
    runner_sha256 = sha256(pathlib.Path(__file__).resolve())
    node_src = r'''const fs=require('fs'),crypto=require('crypto');
const p=process.argv[1],m=require(p),b=fs.readFileSync(p),r=m.ACTION_RE,n=m.NETFILTER_KV_GLUE;
if(!(r instanceof RegExp)||!(n instanceof RegExp))throw new Error('regex export missing');
const values=['ACCEPT','aCcEpT','accept','x aCcEpT!'];
console.log(JSON.stringify({node:process.version,path:p,file_sha256:crypto.createHash('sha256').update(b).digest('hex'),pattern:r.source,flags:r.flags,observations:Object.fromEntries(values.map(s=>[s,r.test(s)])),netfilterPattern:n.source,netfilterFlags:n.flags}));'''
    node_observation = run_bounded(['node', '-e', node_src, str(SOURCE_FILE)])
    if node_observation['returncode'] != 0:
        raise SystemExit(f'Node source observation failed: {node_observation}')
    node_record = json.loads(node_observation['stdout'])
    if node_record.get('file_sha256') != actual_source_sha256:
        raise SystemExit('Node loaded bytes differ from the frozen source bytes')
    pattern = node_record['pattern']
    prefix = '(^|[^A-Za-z0-9_])('
    suffix = ')([^A-Za-z0-9_]|$)'
    if not pattern.startswith(prefix) or not pattern.endswith(suffix):
        raise SystemExit(f'unexpected ACTION_RE source shape: {pattern}')
    words = pattern[len(prefix):-len(suffix)].split('|')
    expected_words = ['ACCEPT', 'ALLOW', 'PASS', 'DROP', 'REJECT', 'DENY', 'BLOCK']
    if words != expected_words or node_record['flags'] != 'i':
        raise SystemExit('ACTION_RE words or flags differ from the frozen diagnostic assumptions')
    expected_observations = {
        'ACCEPT': True, 'aCcEpT': True, 'accept': True, 'x aCcEpT!': True,
    }
    if node_record['observations'] != expected_observations:
        raise SystemExit(f'unexpected native Node ACTION_RE observations: {node_record["observations"]}')
    case_expanded_words = [''.join(f'[{char.upper()}{char.lower()}]' for char in word) for word in words]
    expanded_mirror = prefix + '(' + '|'.join(case_expanded_words) + ')' + suffix
    version = run_bounded([NOODLER_BIN, '-version'])
    if version['returncode'] != 0 or version['classification'] != 'zero_exit_without_verdict':
        raise SystemExit(f'Noodler version probe did not exit cleanly: {version}')
    trusted_binary = APPROVED_NOODLER_BINARIES.get(actual_binary_sha256)
    if trusted_binary and version['stdout'].strip() != trusted_binary['version']:
        raise SystemExit('Noodler binary version text does not match the trusted SHA mapping')

    diagnostic_path = pathlib.Path(__file__).resolve().with_name('issue571-diagnostic.js')
    if not diagnostic_path.is_file():
        raise SystemExit(f'missing finite Node diagnostic script: {diagnostic_path}')
    diagnostic = run_bounded(['node', diagnostic_path, SOURCE_FILE])
    if diagnostic['returncode'] != 0:
        raise SystemExit(f'finite Node diagnostic failed: {diagnostic}')
    diagnostic_record = json.loads(diagnostic['stdout'])
    if diagnostic_record.get('ok') is not True or len(diagnostic_record.get('rows', [])) != 28:
        raise SystemExit('finite Node diagnostic did not report all 28 rows passing')

    manifest = {
        'scope': 'bounded backend diagnostics only; no harness, policy, or product changes',
        'runner_path': str(pathlib.Path(__file__).resolve()),
        'runner_sha256': runner_sha256,
        'fwlive_repo': str(FWLIVE_REPO),
        'fwlive_head': fwlive_head,
        'source_path': str(SOURCE_FILE),
        'source_basename': SOURCE_FILE.name,
        'source_relative_path': source_relative,
        'source_sha256': actual_source_sha256,
        'source_git_blob': source_git_blob,
        'source_last_changed_commit': source_last_changed_commit,
        'source_last_changed_commit_blob': changed_commit_blob,
        'regexproof_repo': str(REGEXPROOF_REPO),
        'regexproof_head': regexproof_head,
        'node_version': node_record['node'],
        'action_regex_source': pattern,
        'action_regex_flags_in_node': node_record['flags'],
        'action_words_extracted_from_source': words,
        'action_node_observations': node_record['observations'],
        'current_netfilter_regex_source': node_record['netfilterPattern'],
        'current_netfilter_regex_flags': node_record['netfilterFlags'],
        'finite_node_diagnostic': {
            'script_path': str(diagnostic_path),
            'script_sha256': sha256(diagnostic_path),
            'kind': diagnostic_record.get('evidence_kind'),
            'product': diagnostic_record.get('product'),
            'formal_proof': diagnostic_record.get('formal_proof'),
            'row_count': len(diagnostic_record.get('rows', [])),
            'all_rows_ok': diagnostic_record.get('ok'),
        },
        'noodler_binary': str(NOODLER_BIN),
        'noodler_binary_sha256': actual_binary_sha256,
        'noodler_expected_sha256': EXPECTED_NOODLER_SHA256,
        'noodler_trusted_binary_mapping': trusted_binary,
        'noodler_version_result': version,
        'timeout_seconds_per_process_max': PER_PROCESS_LIMIT_S,
        'invocation_seconds_max': INVOCATION_LIMIT_S,
        'core_dumps': 'disabled for child processes',
        'artifacts': 'text and JSON only; generated beneath PROBE_DIR',
        'control_note': 'Historical negation crash control is separate from current ACTION_RE and establishes no current product property.',
    }
    write_json(PROBE_DIR / 'baseline.json', manifest)
    write_json(PROBE_DIR / 'node-action-baseline.json', node_record)
    write_json(PROBE_DIR / 'issue571-node-diagnostic.json', diagnostic_record)
    (PROBE_DIR / 'issue571-node-diagnostic.stdout').write_text(diagnostic['stdout'], encoding='utf-8')
    (PROBE_DIR / 'expanded-action-ascii-mirror.txt').write_text(expanded_mirror + '\n', encoding='utf-8')
    write_json(PROBE_DIR / 'initialize-result.json', {
        'node_run': node_observation,
        'version_run': version,
        'finite_node_diagnostic_run': {
            'returncode': diagnostic['returncode'],
            'elapsed_ms': diagnostic['elapsed_ms'],
            'classification': diagnostic['classification'],
        },
    })
    print(json.dumps({
        'probe_dir': str(PROBE_DIR), 'runner_sha256': runner_sha256,
        'node_version': node_record['node'], 'source_sha256': actual_source_sha256,
        'source_basename': SOURCE_FILE.name, 'source_last_changed_commit': source_last_changed_commit,
        'action_flags': node_record['flags'], 'finite_node_rows': len(diagnostic_record['rows']),
        'noodler_sha256': actual_binary_sha256, 'noodler_version': version['stdout'].strip(),
        'noodler_trusted_binary_mapping': trusted_binary,
    }, indent=2))


def smt_quote(value):
    return '"' + value.replace('"', '""') + '"'


def historical_negation_control():
    words = 'IN|OUT|SRC|DST|PROTO|SPT|DPT|LEN|MAC|TYPE|CODE|TTL|TOS|PREC|DF'.split('|')

    def ci_word(word):
        parts = [f'(re.union (str.to_re "{char}") (str.to_re "{char.lower()}"))' for char in word]
        return '(re.++ ' + ' '.join(parts) + ')'

    alternatives = [ci_word(word) for word in words]
    key = '(re.union ' + ' '.join(alternatives) + ')'
    any_ascii = '(re.* (re.range "\\u{0}" "\\u{7f}"))'
    nonspace = '(re.union (re.range "\\u{0}" "\\u{8}") (re.range "\\u{e}" "\\u{1f}") (re.range "!" "\\u{7f}"))'
    mirror = f'(re.++ {any_ascii} {nonspace} {key} (str.to_re "=") {any_ascii})'
    pattern = r'.*([^\s])(?=(IN|OUT|SRC|DST|PROTO|SPT|DPT|LEN|MAC|TYPE|CODE|TTL|TOS|PREC|DF)=).*'
    smt = '\n'.join([
        '(set-logic QF_SLIA)', '(declare-const s String)',
        f'(assert (str.in_re s {any_ascii}))', f'(assert (str.in_re s {mirror}))',
        f"(assert (not (str.in_re s (re.from_ecma2020 '{pattern}'))))",
        '(check-sat)', '',
    ])
    return smt, pattern


def run_case(case):
    baseline_path = PROBE_DIR / 'baseline.json'
    if not baseline_path.is_file():
        raise SystemExit('run `init` first')
    manifest = json.loads(baseline_path.read_text(encoding='utf-8'))
    actual_runner_sha256 = sha256(pathlib.Path(__file__).resolve())
    if actual_runner_sha256 != manifest.get('runner_sha256'):
        raise SystemExit('probe runner changed after baseline initialization')
    actual_source_sha256 = sha256(SOURCE_FILE)
    if actual_source_sha256 != FROZEN_SOURCE_SHA256 or actual_source_sha256 != manifest.get('source_sha256'):
        raise SystemExit('frozen source changed after baseline initialization')
    actual_binary_sha256 = sha256(NOODLER_BIN)
    if (actual_binary_sha256 != EXPECTED_NOODLER_SHA256 or
            actual_binary_sha256 != manifest.get('noodler_expected_sha256') or
            str(NOODLER_BIN) != manifest.get('noodler_binary')):
        raise SystemExit(f'Noodler binary pin or path changed: {actual_binary_sha256}')
    pattern = manifest['action_regex_source']
    fixed_inputs = {
        'source-upper': 'ACCEPT', 'source-mixed': 'aCcEpT',
        'ascii-mirror-mixed': 'aCcEpT', 'negative-membership': 'ACCEPT',
        'flags-second-argument': 'aCcEpT', 'inline-i-flag': 'aCcEpT',
        'property-escape-non-u-literal': 'p{L}',
        'property-escape-letter': 'A', 'property-escape-u-argument': 'A',
        'non-u-dot-astral': '\U0001f600',
    }
    if case in {'source-upper', 'source-mixed'}:
        term = f"(re.from_ecma2020 '{pattern}')"
        assertions = [f'(assert (str.in_re s {term}))']
    elif case == 'ascii-mirror-mixed':
        mirror = (PROBE_DIR / 'expanded-action-ascii-mirror.txt').read_text(encoding='utf-8').rstrip('\n')
        term = f"(re.from_ecma2020 '{mirror}')"
        assertions = [f'(assert (str.in_re s {term}))']
    elif case in {'negative-membership', 'negative-membership-unconstrained'}:
        term = f"(re.from_ecma2020 '{pattern}')"
        assertions = [f'(assert (not (str.in_re s {term})))']
    elif case == 'm2e-diff':
        mirror = (PROBE_DIR / 'expanded-action-ascii-mirror.txt').read_text(encoding='utf-8').rstrip('\n')
        assertions = [
            f"(assert (str.in_re s (re.from_ecma2020 '{mirror}')))",
            f"(assert (not (str.in_re s (re.from_ecma2020 '{pattern}'))))",
        ]
    elif case == 'flags-second-argument':
        term = f"(re.from_ecma2020 '{pattern}' \"i\")"
        assertions = [f'(assert (str.in_re s {term}))']
    elif case == 'inline-i-flag':
        term = "(re.from_ecma2020 '(?i)ACCEPT')"
        assertions = [f'(assert (str.in_re s {term}))']
    elif case in {'property-escape-non-u-literal', 'property-escape-letter'}:
        term = r"(re.from_ecma2020 '^\p{L}$')"
        assertions = [f'(assert (str.in_re s {term}))']
    elif case == 'property-escape-u-argument':
        term = r'''(re.from_ecma2020 '^\p{L}$' "u")'''
        assertions = [f'(assert (str.in_re s {term}))']
    elif case == 'non-u-dot-astral':
        term = "(re.from_ecma2020 '^.$')"
        assertions = [f'(assert (str.in_re s {term}))']
    elif case == 'historical-negation-crash-control':
        smt, historical_pattern = historical_negation_control()
        return run_one(case, smt, None, historical_pattern,
                       'historical blocker-probe control, not current ACTION_RE proof input')
    else:
        raise SystemExit(f'unknown case: {case}')

    lines = ['(set-logic QF_SLIA)', '(declare-const s String)', *assertions]
    input_value = fixed_inputs.get(case)
    if input_value is not None:
        lines.append(f'(assert (= s {smt_quote(input_value)}))')
    lines.extend(['(check-sat)', ''])
    smt = '\n'.join(lines)
    interpretation = (
        'fixed-string membership; converter call has no source /i flag'
        if case.startswith('source-') else
        'ASCII case-expanded mirror control; not the source regex with /i'
        if case.startswith('ascii-') else
        'API/parser or solver diagnostic only; no theorem or product-property inference'
    )
    return run_one(case, smt, input_value, pattern, interpretation)


def run_one(case, smt, input_value, pattern, interpretation):
    smt_path = PROBE_DIR / f'{case}.smt2'
    smt_path.write_text(smt, encoding='utf-8')
    result = run_bounded([NOODLER_BIN, smt_path])
    result.update({
        'case': case,
        'runner_sha256': sha256(pathlib.Path(__file__).resolve()),
        'noodler_sha256': sha256(NOODLER_BIN),
        'noodler_trusted_binary_mapping': APPROVED_NOODLER_BINARIES.get(EXPECTED_NOODLER_SHA256),
        'smt_path': str(smt_path),
        'smt_sha256': sha256(smt_path),
        'fixed_input': input_value,
        'pattern_or_control_source': pattern,
        'interpretation_limit': interpretation,
    })
    (PROBE_DIR / f'{case}.stdout').write_text(result['stdout'], encoding='utf-8')
    (PROBE_DIR / f'{case}.stderr').write_text(result['stderr'], encoding='utf-8')
    write_json(PROBE_DIR / f'{case}.result.json', result)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: portable_probe.py init|CASE')
    if sys.argv[1] == 'init':
        initialize()
    else:
        run_case(sys.argv[1])
