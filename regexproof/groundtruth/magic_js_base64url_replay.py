"""Exact-pin Node replay for Magic JS Base64URL substitutions."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

from regexproof.contract_adoption import contract_digest, contract_is_adopted

PIN = "e9fb233763160316989863b4739c4656133d45b0"
REPOSITORY = "https://github.com/magiclabs/magic-js"
REPO_ID = "magiclabs/magic-js"
SLICE = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-p2-magic-js-source-review"
)
CONTRACT_PATH = SLICE / "contracts.json"
REVIEW_PATH = SLICE / "reviews.json"
DEFAULT_SOURCE_ROOT = Path("/tmp/regexproof-pinned-sources") / f"magic-js-{PIN}"

QUESTION_IDS = (
    "ME-oauth2-pkce-s256-base64url",
    "ME-rn-bare-pkce-s256-base64url",
    "ME-rn-expo-pkce-s256-base64url",
    "ME-oauth2-webauthn-base64url",
    "ME-passkey-base64url",
    "ME-wallet-kit-base64url",
    "ME-webauthn-base64url",
    "ME-provider-webauthn-base64url",
    "ME-rn-bare-dpop-base64url",
    "ME-provider-dpop-base64url",
)
MUTATION_ID = "ME-base64url-mutated-plus-leaks"

_MODULES = {
    "ME-oauth2-webauthn-base64url": (
        "packages/@magic-ext/oauth2/src/utils/base64.ts", "Base64URL", "encode"
    ),
    "ME-passkey-base64url": (
        "packages/@magic-ext/passkey/src/utils/base64.ts", "Base64URL", "encode"
    ),
    "ME-wallet-kit-base64url": (
        "packages/@magic-ext/wallet-kit/src/utils/base64.ts", "Base64URL", "encode"
    ),
    "ME-webauthn-base64url": (
        "packages/@magic-ext/webauthn/src/utils/base64.ts", "Base64URL", "encode"
    ),
    "ME-provider-webauthn-base64url": (
        "packages/@magic-sdk/provider/src/util/base64-json.ts", "Base64URL", "encode"
    ),
    "ME-rn-bare-dpop-base64url": (
        "packages/@magic-sdk/react-native-bare/src/native-crypto/utils/uint8.ts",
        "toBase64Url",
        None,
    ),
}
_CHAIN_ONLY = {
    "ME-oauth2-pkce-s256-base64url": (
        "packages/@magic-ext/oauth2/src/crypto.ts", 22, "input.toString(CryptoJS.enc.Base64)"
    ),
    "ME-rn-bare-pkce-s256-base64url": (
        "packages/@magic-ext/react-native-bare-oauth/src/crypto.ts", 25,
        "input.toString(CryptoJS.enc.Base64)",
    ),
    "ME-rn-expo-pkce-s256-base64url": (
        "packages/@magic-ext/react-native-expo-oauth/src/crypto.ts", 25,
        "input.toString(CryptoJS.enc.Base64)",
    ),
    "ME-provider-dpop-base64url": (
        "packages/@magic-sdk/provider/src/util/web-crypto.ts", 106, "btoa(bin)"
    ),
}


def source_root(root: Path | None = None) -> Path:
    if root is not None:
        return root.resolve()
    configured = os.environ.get("REGEXPROOF_MAGIC_JS_CHECKOUT")
    return Path(configured).resolve() if configured else DEFAULT_SOURCE_ROOT


def _contracts() -> dict[str, dict[str, Any]]:
    value = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, list):
        raise RuntimeError("Magic JS contracts artifact must be an array")
    by_site = {contract.get("site"): contract for contract in value}
    if len(by_site) != len(value):
        raise RuntimeError("Magic JS contracts artifact has duplicate sites")
    reviews = json.loads(REVIEW_PATH.read_text(encoding="utf-8"))
    qid_site = {
        row["question_id"]: _contract_site(row["site"])
        for row in reviews["reviews"]
        if row.get("decision") == "adopted"
    }
    result = {}
    for question_id in QUESTION_IDS:
        contract = by_site.get(qid_site.get(question_id))
        if not _valid_product_contract(contract):
            raise RuntimeError(f"{question_id}: contract is not validly adopted")
        result[question_id] = contract
    if len(result) != len(value):
        raise RuntimeError("contracts artifact question identities do not match the harness")
    return result


def _contract_site(review_site: str) -> str:
    source_file, line, column = review_site.rsplit(":", 2)
    return f"{REPO_ID}@{PIN}:{source_file}:{line}:column-{column}"


def _valid_product_contract(contract: Any) -> bool:
    return bool(
        isinstance(contract, dict)
        and contract_is_adopted(contract)
        and isinstance(contract.get("site"), str)
        and isinstance(contract.get("guarantee"), str)
        and contract["guarantee"].strip()
        and isinstance(contract.get("declared_domain"), str)
        and contract["declared_domain"].strip()
    )


def _parse_replace_operations(line: str) -> list[dict[str, str]]:
    operations: list[dict[str, str]] = []
    marker = ".replace("
    offset = 0
    while True:
        start = line.find(marker, offset)
        if start < 0:
            break
        i = start + len(marker)
        if i >= len(line) or line[i] != "/":
            raise RuntimeError("replacement source is not a regex literal")
        i += 1
        pattern: list[str] = []
        escaped = False
        while i < len(line):
            char = line[i]
            if char == "/" and not escaped:
                i += 1
                break
            pattern.append(char)
            if char == "\\" and not escaped:
                escaped = True
            else:
                escaped = False
            i += 1
        else:
            raise RuntimeError("unterminated regex literal in source replacement")
        flag_start = i
        while i < len(line) and line[i].isalpha():
            i += 1
        flags = line[flag_start:i]
        if line[i : i + 1] != ",":
            raise RuntimeError("regex replacement has no comma after flags")
        i += 1
        while i < len(line) and line[i].isspace():
            i += 1
        quote = line[i : i + 1]
        if quote not in {"'", '"'}:
            raise RuntimeError("replacement string must be a quoted literal")
        i += 1
        replacement: list[str] = []
        while i < len(line):
            char = line[i]
            if char == quote:
                i += 1
                break
            if char == "\\" and i + 1 < len(line):
                i += 1
                char = line[i]
                replacement.append({"n": "\n", "r": "\r", "t": "\t"}.get(char, char))
            else:
                replacement.append(char)
            i += 1
        else:
            raise RuntimeError("unterminated replacement string")
        operations.append({
            "pattern": "".join(pattern),
            "flags": flags,
            "replacement": "".join(replacement),
        })
        offset = i
    if len(operations) != 3:
        raise RuntimeError(f"expected three source replacements, found {len(operations)}")
    return operations


def verify_source(root: Path | None = None) -> tuple[Path, dict[str, dict[str, Any]], dict[str, list[dict[str, str]]]]:
    checkout = source_root(root)
    if not checkout.is_dir() or checkout.is_symlink():
        raise RuntimeError(f"exact pinned checkout is unavailable: {checkout}")
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=checkout, check=True,
        capture_output=True, text=True, timeout=10,
    ).stdout.strip()
    if head != PIN:
        raise RuntimeError(f"source pin mismatch: expected {PIN}, found {head}")
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=checkout, check=True,
        capture_output=True, text=True, timeout=10,
    ).stdout
    if status:
        raise RuntimeError("exact pinned checkout is not clean")

    contracts = _contracts()
    source_text: dict[str, str] = {}
    for question_id, contract in contracts.items():
        adoption = contract["adoption"]
        path = adoption["source_file"]
        if adoption["source_url"] != REPOSITORY or adoption["source_pin"] != PIN:
            raise RuntimeError(f"{question_id}: adoption source identity mismatch")
        source_path = checkout / path
        if source_path.is_symlink() or not source_path.is_file():
            raise RuntimeError(f"{question_id}: source file is missing or a symlink")
        raw = source_path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != adoption["source_sha256"]:
            raise RuntimeError(f"{question_id}: pinned source hash changed")
        committed = subprocess.run(
            ["git", "show", f"{PIN}:{path}"], cwd=checkout, check=True,
            capture_output=True, timeout=10,
        ).stdout
        if raw != committed:
            raise RuntimeError(f"{question_id}: checkout bytes differ from pinned Git blob")
        source_text[path] = raw.decode("utf-8")

    operations: dict[str, list[dict[str, str]]] = {}
    for question_id, (path, _class_name, method_name) in _MODULES.items():
        line_number = next(
            int(contract["site"].rsplit(":", 1)[0].rsplit(":", 1)[-1])
            for qid, contract in contracts.items()
            if qid == question_id
        )
        line = source_text[path].splitlines()[line_number - 1]
        if method_name == "encode" and "return base64.replace(" not in line:
            raise RuntimeError(f"{question_id}: reviewed encoder expression changed")
        if method_name is None and "return base64.replace(" not in line:
            raise RuntimeError(f"{question_id}: reviewed DPoP expression changed")
        operations[question_id] = _parse_replace_operations(line)

    for question_id, (path, line_number, prefix) in _CHAIN_ONLY.items():
        line = source_text[path].splitlines()[line_number - 1]
        if "return " not in line or prefix not in line:
            raise RuntimeError(f"{question_id}: reviewed encoder expression changed")
        operations[question_id] = _parse_replace_operations(line)
    return checkout, contracts, operations


def _node_payload(
    *, operations: dict[str, list[dict[str, str]]], import_paths: dict[str, str],
    selected_ids: tuple[str, ...], mutation: bool,
) -> dict[str, Any]:
    return {
        "operations": operations,
        "import_paths": import_paths,
        "question_ids": list(selected_ids),
        "mutation": mutation,
    }


def _run_node(payload: dict[str, Any], checkout: Path, timeout_seconds: int = 300) -> dict[str, Any]:
    source = r'''import crypto from 'node:crypto';
import { pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
const payload = JSON.parse(process.env.REGEXPROOF_MAGIC_JS_PAYLOAD);
const modules = {};
for (const [id, url] of Object.entries(payload.import_paths)) {
  modules[id] = await import(url);
}
const applyOps = (value, ops) => {
  for (const op of ops) value = value.replace(new RegExp(op.pattern, op.flags), op.replacement);
  return value;
};
const fail = (id, input, actual, expected) => ({ id, input, actual, expected });
const counts = Object.fromEntries(payload.question_ids.map(id => [id, 0]));
const firstMismatch = [];
const checkEncoded = (id, bytes) => {
  let actual;
  if (modules[id]) {
    const buffer = new Uint8Array(bytes).buffer;
    if (id === 'ME-rn-bare-dpop-base64url') actual = modules[id].toBase64Url(new Uint8Array(bytes));
    else actual = modules[id].Base64URL.encode(buffer);
  } else {
    const binary = String.fromCharCode(...bytes);
    actual = applyOps(btoa(binary), payload.operations[id]);
  }
  const expected = Buffer.from(bytes).toString('base64url');
  counts[id]++;
  if (actual !== expected && firstMismatch.length < 10) firstMismatch.push(fail(id, [...bytes], actual, expected));
};
const samples = [new Uint8Array(0)];
for (let a = 0; a < 256; a++) samples.push(Uint8Array.of(a));
for (let a = 0; a < 256; a++) for (let b = 0; b < 256; b++) samples.push(Uint8Array.of(a, b));
let seed = 0x4d454a53;
const random = () => { seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0; return seed; };
for (let n = 0; n < 2048; n++) {
  const bytes = new Uint8Array(3 + random() % 254);
  for (let i = 0; i < bytes.length; i++) bytes[i] = random() & 0xff;
  samples.push(bytes);
}
for (const id of payload.question_ids) {
  if (id.includes('pkce-s256')) {
    const vectorVerifier = 'dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk';
    const vectorDigest = crypto.createHash('sha256').update(vectorVerifier, 'ascii').digest();
    const vectorActual = applyOps(vectorDigest.toString('base64'), payload.operations[id]);
    const vectorExpected = 'E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM';
    counts[id]++;
    if (vectorActual !== vectorExpected && firstMismatch.length < 10) firstMismatch.push(fail(id, vectorVerifier, vectorActual, vectorExpected));
    for (let n = 0; n < 2048; n++) {
      const verifier = `regexproof-pkce-${n}-${random().toString(16)}`;
      const digest = crypto.createHash('sha256').update(verifier, 'ascii').digest();
      const actual = applyOps(digest.toString('base64'), payload.operations[id]);
      const expected = digest.toString('base64url');
      counts[id]++;
      if (actual !== expected && firstMismatch.length < 10) firstMismatch.push(fail(id, verifier, actual, expected));
    }
    continue;
  }
  for (const bytes of samples) checkEncoded(id, bytes);
}
let mutationPlus = false;
if (payload.mutation) {
  const id = 'ME-oauth2-webauthn-base64url';
  const weakened = payload.operations[id].map(op => ({ ...op }));
  const plus = weakened.find(op => op.pattern === '\\+' && op.replacement === '-');
  if (!plus) throw new Error('cannot locate exact source plus replacement to weaken');
  plus.replacement = '+';
  const mutated = applyOps(btoa(String.fromCharCode(0xfb)), weakened);
  mutationPlus = mutated.includes('+') && mutated === '+w';
}
process.stdout.write(JSON.stringify({ counts, firstMismatch, mutationPlus, nodeVersion: process.version }));
'''
    env = os.environ.copy()
    env["REGEXPROOF_MAGIC_JS_PAYLOAD"] = json.dumps(payload, ensure_ascii=True)
    result = subprocess.run(
        ["node", "--experimental-strip-types", "--input-type=module", "-e", source],
        cwd=checkout,
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        env=env,
    )
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Node Base64URL gate returned invalid JSON: {exc}") from exc


def run_differential_gate(root: Path | None = None) -> dict[str, Any]:
    checkout, contracts, operations = verify_source(root)
    import_paths = {
        question_id: (checkout / source_file).resolve().as_uri()
        for question_id, (source_file, _class_name, _method_name) in _MODULES.items()
    }
    result = _run_node(_node_payload(
        operations=operations,
        import_paths=import_paths,
        selected_ids=QUESTION_IDS,
        mutation=True,
    ), checkout)
    if result.get("firstMismatch"):
        raise RuntimeError(f"exact-source Base64URL mismatch: {result['firstMismatch'][0]}")
    if result.get("mutationPlus") is not True:
        raise RuntimeError("weakened exact-source plus replacement did not reproduce")
    counts = result.get("counts")
    if not isinstance(counts, dict) or set(counts) != set(QUESTION_IDS):
        raise RuntimeError("Node gate omitted a contracted question")
    if any(type(count) is not int or count < 1 for count in counts.values()):
        raise RuntimeError("Node gate did not replay every product question")
    if sum(counts.values()) < 450_000:
        raise RuntimeError("Node gate completed too few differential cases")
    if any(not _valid_product_contract(contracts[qid]) for qid in QUESTION_IDS):
        raise RuntimeError("product contract became invalid during the gate")
    return {
        "schema_version": "1",
        "gate_id": "magic-js-base64url-output-image",
        "repository": REPOSITORY,
        "source_pin": PIN,
        "question_ids": list(QUESTION_IDS),
        "product_engine_replay_question_ids": list(QUESTION_IDS),
        "differential_case_counts": counts,
        "differential_cases": sum(counts.values()),
        "node_version": result["nodeVersion"],
        "mutation_guard_question_id": MUTATION_ID,
        "mutation_guard_passed": True,
        "mutation_witness": "bytes fb -> base64 +w== -> weakened output +w",
        "contract_sha256s": {
            qid: contract_digest(contracts[qid]) for qid in QUESTION_IDS
        },
    }


def mutation_reproduces(witness: dict[str, Any]) -> bool:
    character = witness.get("base64_character")
    if character != "+":
        return False
    checkout, _contracts_by_id, operations = verify_source()
    result = _run_node(_node_payload(
        operations=operations,
        import_paths={},
        selected_ids=("ME-oauth2-webauthn-base64url",),
        mutation=True,
    ), checkout, timeout_seconds=30)
    return result.get("mutationPlus") is True


__all__ = [
    "CONTRACT_PATH", "DEFAULT_SOURCE_ROOT", "MUTATION_ID", "PIN",
    "QUESTION_IDS", "REPO_ID", "REPOSITORY", "mutation_reproduces",
    "run_differential_gate", "source_root", "verify_source",
]
