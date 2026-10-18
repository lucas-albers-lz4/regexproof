#!/usr/bin/env python3
"""Replay bounded research checks against explicitly pinned prepared sources."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parent
IMAGE = 'rocq/rocq-prover@sha256:9a1e969649a3cc3c6f310d5be5a842e2187384560337c6c0807aba9f8565efba'
WARBLRE = '87af3ccaea96015d4104c0b2d9de758fa8d9ee87'
DUNE = '6f6eee69eda59e355bae2ca4e3ad1af678271883'


def check_revision(directory, expected):
    """Reject a different checkout before executing any build code."""
    actual = subprocess.check_output(['git', '-C', str(directory), 'rev-parse', 'HEAD'], text=True).strip()
    if actual != expected:
        raise SystemExit(f'wrong source revision: {directory}: {actual}')
    if subprocess.check_output(['git', '-C', str(directory), 'diff', 'HEAD', '--'], text=True):
        raise SystemExit(f'modified tracked source: {directory}')


def main():
    """Run positive builds and required negative theorem failures separately."""
    work = Path(os.environ['WARBLRE_BUILD']).resolve()
    dune = Path(os.environ['DUNE_SOURCE']).resolve()
    check_revision(work, WARBLRE)
    check_revision(dune, DUNE)
    if not (dune / '_boot/dune.exe').is_file():
        raise SystemExit('bootstrap the pinned Dune source first; see README')
    example = work / 'examples/rocq_proof'
    inputs = {}
    for name in ('CanonicalizeBoundary.v', 'PrefixAstProbe.v'):
        data = (ROOT / name).read_bytes()
        inputs[name] = hashlib.sha256(data).hexdigest()
        (example / name).write_bytes(data)
    prefix = (ROOT / 'PrefixAstProbe.v').read_text()
    mutants = {
        'MutantAnchor': prefix.replace('Seq InputStart', 'Seq Empty'),
        'MutantHyphen': prefix.replace('(ClassAtomCR (SourceCharacter 45) EmptyCR)', 'EmptyCR'),
        'MutantCanonicalize': (ROOT / 'CanonicalizeBoundary.v').read_text().split('(* Crucially')[0].replace(
            'if (128 <=? ch) && (cu <? 128) then ch else cu', 'cu')
            + '\nExample preserved_guard_example :\n  non_u_canonicalize (fun _ => [83]) 383 = 383.\nProof. vm_compute. reflexivity. Qed.\n',
    }
    if any(text == prefix for name, text in mutants.items() if name != 'MutantCanonicalize'):
        raise SystemExit('mutation did not change the probe')
    records = []

    def run(label, command, expect_failure=False):
        """Capture status first; an arbitrary build failure is never a negative pass."""
        container = f'regexproof-653-{os.getpid()}-{label.lower()}'
        args = ['docker', 'run', '--rm', '--name', container, '--network', 'none',
                '--cpus', '4', '--memory', '8g', '-v', f'{dune}:/dune:ro',
                '-v', f'{work}:/work', '-w', '/work', IMAGE, 'bash', '-lc', command]
        started = time.monotonic()
        try:
            result = subprocess.run(args, capture_output=True, text=True, timeout=600)
            status, stdout, stderr = result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired as error:
            subprocess.run(['docker', 'rm', '-f', container], capture_output=True, timeout=30)
            raise SystemExit(f'{label}: timeout, not proven') from error
        record = {'label': label, 'command': args, 'exit_code': status,
                  'seconds': round(time.monotonic()-started, 3),
                  'stdout': stdout, 'stderr': stderr}
        records.append(record)
        (ROOT / 'rocq-results.json').write_text(json.dumps({
            'image': IMAGE, 'warblre_commit': WARBLRE, 'dune_commit': DUNE,
            'input_sha256': inputs, 'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'records': records}, indent=2) + '\n')
        if expect_failure:
            # Mutated .v must reach its theorem, not fail parsing/tool resolution.
            signature = ('Unable to unify "383" with "83"' if label == 'MutantCanonicalize'
                         else 'Unable to unify "Some false" with "Some true"')
            if status == 0 or signature not in stdout + stderr:
                raise SystemExit(f'{label}: missing expected theorem rejection')
        elif status != 0:
            raise SystemExit(f'{label}: build failed, not proven')
        print(f'{label}: expected outcome recorded')

    # Force positive proof outputs, including Print Assumptions, on every replay.
    run('positive', '/dune/_boot/dune.exe clean && /dune/_boot/dune.exe build -j 4 examples/rocq_proof')
    run('kernel-recheck', 'rocqchk -silent -Q _build/default/mechanization Warblre -R _build/default/examples/rocq_proof Example Example.Example Example.CanonicalizeBoundary Example.PrefixAstProbe')
    try:
        for name, text in mutants.items():
            path = example / (name + '.v')
            path.write_text(text)
            try:
                run(name, f'/dune/_boot/dune.exe build -j 4 examples/rocq_proof/{name}.vo', True)
            finally:
                path.unlink()
    finally:
        for name in mutants:
            (example / (name + '.v')).unlink(missing_ok=True)


if __name__ == '__main__':
    main()
