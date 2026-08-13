"""On-disk cache for compiled regular-expression mirrors.

Cache entries deliberately keep the mirror in SMT-LIB rather than pickling a
Z3 object.  Apart from making entries inspectable, this is the boundary that
keeps spawned batch workers independent of the parent's Z3 context.
"""

from __future__ import annotations

import hashlib
import json
import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import z3

from regexproof.io_atomic import atomic_write_text

DEFAULT_CACHE_DIR = Path(__file__).resolve().parents[2] / ".cache" / "mirrors"
_CACHE_FORMAT_VERSION = "regexproof-mirror-cache-v1"
_MIRROR_NAME = "mirror"
_METADATA_PREFIX = "; regexproof-metadata: "


def _canonical_value(value: Any) -> bytes:
    """Encode one key component without relying on string concatenation."""
    if value is None:
        return b"null"
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=True, separators=(",", ":")).encode(
            "utf-8"
        )
    return json.dumps(
        value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def canonical_length_prefixed(values: Iterable[Any]) -> bytes:
    """Return a canonical, unambiguous length-prefixed tuple encoding."""
    parts = [_canonical_value(value) for value in values]
    output = bytearray()
    output.extend(_CACHE_FORMAT_VERSION.encode("ascii"))
    output.extend(struct.pack(">Q", len(parts)))
    for part in parts:
        output.extend(struct.pack(">Q", len(part)))
        output.extend(part)
    return bytes(output)


def mirror_cache_key(
    normalized_pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    domain: str,
    shell_flags: dict[str, Any] | None,
    compiler_version: str,
    z3_version: str,
    max_length: int | None = None,
) -> str:
    """Hash the complete post-normalization compile-input tuple."""
    encoded = canonical_length_prefixed(
        (
            normalized_pattern,
            flags,
            dialect,
            call_kind,
            domain,
            shell_flags,
            compiler_version,
            z3_version,
            max_length,
        )
    )
    return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class MirrorArtifact:
    """A parsed cache value and its compiler metadata."""

    mirror: Any
    metadata: dict[str, Any]
    script: str


def serialize_mirror(
    mirror: Any,
    metadata: dict[str, Any] | None = None,
) -> str:
    """Serialize a regex AST as a complete parseable SMT-LIB script."""
    if mirror is None or not hasattr(mirror, "sexpr"):
        raise ValueError("cannot serialize an absent or non-Z3 mirror")
    # The assertion is intentional: parse_smt2_string returns assertions, not
    # define-fun declarations.  It also gives deserialize_mirror a typed,
    # context-independent path to recover the define-fun value.
    script = (
        "(set-logic QF_S)\n"
        f"(define-fun {_MIRROR_NAME} () (RegEx String) {mirror.sexpr()})\n"
        f'(assert (str.in_re "" {_MIRROR_NAME}))\n'
    )
    meta = dict(metadata or {})
    # M1 (luna gate 1 + re-gate 2): the KEY-BOUND digest of the mirror-only
    # script is added by MirrorCache.put(); get() re-computes it from the
    # requested key so a copied artifact under a different key is rejected.
    return script + _METADATA_PREFIX + json.dumps(
        meta, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ) + "\n"


def _metadata_from_script(script: str) -> dict[str, Any]:
    for line in script.splitlines():
        if line.startswith(_METADATA_PREFIX):
            metadata = json.loads(line[len(_METADATA_PREFIX) :])
            if isinstance(metadata, dict):
                return metadata
            break
    raise ValueError("mirror SMT-LIB script has no valid metadata")


def deserialize_mirror(script: str) -> Any:
    """Parse and validate one complete cached SMT-LIB mirror script."""
    if not isinstance(script, str) or "(define-fun" not in script:
        raise ValueError("cache value is not a mirror SMT-LIB script")
    assertions = z3.parse_smt2_string(script)
    if len(assertions) != 1:
        raise ValueError("mirror SMT-LIB script must contain one assertion")
    assertion = assertions[0]
    if not z3.is_app(assertion) or assertion.num_args() != 2:
        raise ValueError("mirror SMT-LIB assertion has the wrong shape")
    mirror = assertion.arg(1)
    if mirror.sort().kind() != z3.Z3_RE_SORT:
        raise ValueError("mirror SMT-LIB assertion does not expose a regex")
    return mirror


class MirrorCache:
    """Atomic filesystem cache for canonical mirror scripts."""

    def __init__(self, directory: Path | str = DEFAULT_CACHE_DIR) -> None:
        self.directory = Path(directory)

    def path_for(self, key: str) -> Path:
        if len(key) != 64 or any(ch not in "0123456789abcdef" for ch in key):
            raise ValueError("cache key must be a lowercase SHA-256 hex digest")
        return self.directory / f"{key}.smt2"

    def get(self, key: str) -> MirrorArtifact | None:
        """Return a valid artifact, treating every read/parse error as a miss."""
        try:
            script = self.path_for(key).read_text(encoding="utf-8")
            mirror = deserialize_mirror(script)
            metadata = _metadata_from_script(script)
            # M1 (luna gate 1): a parseable script under the right filename is
            # not enough — the metadata digest must match the mirror-only
            # script.  A swapped or partially-corrupted entry that still parses
            # triggers a fresh compile instead of serving a wrong mirror.
            expected = metadata.get("_script_sha256")
            core = script.split(_METADATA_PREFIX, 1)[0]
            actual = hashlib.sha256((key + ":" + core).encode("utf-8")).hexdigest()
            if not expected or expected != actual:
                return None
            # Minor (luna gate 1): metadata SIDECAR (the plan's "metadata
            # sidecars") — the .meta.json sibling is the authoritative source
            # when present; the comment-embedded copy is the legacy fallback.
            # Re-gate 3: the sidecar's own digest must match the key-bound
            # digest — a swapped sidecar (valid artifact from another key)
            # would otherwise smuggle different shape/mirror flags.
            sidecar = self.path_for(key).with_suffix(".smt2.meta.json")
            if sidecar.is_file():
                try:
                    side_meta = json.loads(sidecar.read_text(encoding="utf-8"))
                    if not isinstance(side_meta, dict):
                        return None
                    side_digest = side_meta.get("_script_sha256")
                    if not side_digest or side_digest != actual:
                        return None
                    metadata = side_meta
                except (OSError, json.JSONDecodeError):
                    return None
            return MirrorArtifact(mirror, metadata, script)
        except (OSError, ValueError, TypeError, json.JSONDecodeError, z3.Z3Exception):
            # A corrupt entry must never turn into a skipped compile.  The
            # caller recompiles and atomically replaces it.
            return None

    def put(
        self,
        key: str,
        mirror: Any,
        metadata: dict[str, Any] | None,
    ) -> str:
        """Atomically write one script + a metadata sidecar."""
        script = serialize_mirror(mirror, metadata or {})
        # Re-gate 2: the digest BINDS THE KEY — copying a valid artifact to
        # another key changes the digest and triggers a fresh compile.
        meta = dict(_metadata_from_script(script))
        core = script.split(_METADATA_PREFIX, 1)[0]
        meta["_script_sha256"] = hashlib.sha256(
            (key + ":" + core).encode("utf-8")
        ).hexdigest()
        script = script.split(_METADATA_PREFIX, 1)[0] + _METADATA_PREFIX + json.dumps(
            meta, ensure_ascii=True, sort_keys=True, separators=(",", ":")
        ) + "\n"
        atomic_write_text(self.path_for(key), script)
        # The sidecar carries the metadata (the plan's "metadata sidecars");
        # the comment-embedded copy remains for backward compatibility.
        atomic_write_text(self.path_for(key).with_suffix(".smt2.meta.json"),
                          json.dumps(meta, indent=2, sort_keys=True) + "\n")
        return script

    # Explicit aliases make the cache API convenient for tests and callers
    # that want to distinguish filesystem operations from AST reconstruction.
    load = get
    store = put


__all__ = [
    "DEFAULT_CACHE_DIR",
    "MirrorArtifact",
    "MirrorCache",
    "canonical_length_prefixed",
    "deserialize_mirror",
    "mirror_cache_key",
    "serialize_mirror",
]
