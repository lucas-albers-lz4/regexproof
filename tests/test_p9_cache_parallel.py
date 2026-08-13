"""P9 mirror-cache and spawn-worker contracts."""

from __future__ import annotations

from pathlib import Path

import json

import z3

from regexproof.batch.compile_records import compile_records
from regexproof.compiler import COMPILER_VERSION, compile_pattern, compiler_source_fingerprint
from regexproof.compiler.cache import (
    deserialize_mirror,
    mirror_cache_key,
    serialize_mirror,
)


def _record(regex_id: str, pattern: str, **extra):
    return {
        "regex_id": regex_id,
        "pattern": pattern,
        "flags": "",
        "dialect": extra.pop("dialect", "re2"),
        "call_kind": "fullmatch",
        "site": f"fixture:{regex_id}",
        "domain": "ascii",
        **extra,
    }


def test_cache_key_length_prefix_blocks_ambiguous_splits():
    first = mirror_cache_key("a", "bc", "re2", "fullmatch", "ascii", None, "v", "z")
    second = mirror_cache_key("ab", "c", "re2", "fullmatch", "ascii", None, "v", "z")
    assert first != second
    # Dict ordering is not part of shell flag identity.
    assert mirror_cache_key(
        "x", "", "posix-shell", "search", "ascii", {"grep_mode": "basic", "syntax": "bre"}, "v", "z"
    ) == mirror_cache_key(
        "x", "", "posix-shell", "search", "ascii", {"syntax": "bre", "grep_mode": "basic"}, "v", "z"
    )


def test_smtlib_round_trip_and_bre_key_uses_normalized_pattern(tmp_path: Path):
    cache_dir = tmp_path / "mirrors"
    result = compile_pattern(
        r"a\+b",
        dialect="posix-shell",
        call_kind="search",
        shell_flags={"syntax": "bre", "grep_mode": "basic"},
        cache_dir=str(cache_dir),
    )
    assert result.encodable
    assert result.pattern == "a+b"
    script_paths = list(cache_dir.glob("*.smt2"))
    assert len(script_paths) == 1
    script = script_paths[0].read_text(encoding="utf-8")
    assert "define-fun mirror" in script
    parsed = deserialize_mirror(script)
    assert z3.is_true(z3.simplify(z3.InRe(z3.StringVal("aab"), parsed)))


def test_corrupt_cache_entry_recompiles(tmp_path: Path):
    cache_dir = tmp_path / "mirrors"
    stats = {}
    first = compile_pattern("^[a-z]+$", dialect="re2", call_kind="fullmatch", cache_dir=str(cache_dir), cache_stats=stats)
    assert first.encodable and stats == {"misses": 1}
    entry = next(cache_dir.glob("*.smt2"))
    entry.write_text("not SMT-LIB", encoding="utf-8")
    stats = {}
    second = compile_pattern("^[a-z]+$", dialect="re2", call_kind="fullmatch", cache_dir=str(cache_dir), cache_stats=stats)
    assert second.encodable and stats == {"misses": 1}
    assert "define-fun mirror" in entry.read_text(encoding="utf-8")


def test_compiler_version_tracks_source_contents(tmp_path: Path):
    # P9 (luna gate 1): the test must PROVE the fingerprint reacts to a
    # compiler-source change, not just compare a value with itself.
    before = compiler_source_fingerprint()
    target = Path(compiler_source_fingerprint.__globals__["__file__"]).resolve().parent
    extra = target / "_fingerprint_probe_sentinel.py"
    assert not extra.exists()
    try:
        extra.write_text("# sentinel for fingerprint reactivity\n", encoding="utf-8")
        after = compiler_source_fingerprint()
        assert after != before, "fingerprint must react to a source change"
        assert len(after) == 64
    finally:
        extra.unlink(missing_ok=True)
    assert compiler_source_fingerprint() == before


def test_spawn_workers_return_same_sorted_rows_and_mirrors(tmp_path: Path):
    records = [
        _record("c", "^[c]+$"),
        _record("a", "^[a]+$"),
        _record("b", "^[b]+$"),
    ]
    serial = compile_records(records, lift_inline=False, corpus_slug="p9", jobs=1, cache_dir=tmp_path / "serial")
    parallel = compile_records(records, lift_inline=False, corpus_slug="p9", jobs=2, cache_dir=tmp_path / "parallel")
    assert [row["regex_id"] for row, _mirror, _meta in serial] == ["a", "b", "c"]
    assert [row for row, _mirror, _meta in serial] == [row for row, _mirror, _meta in parallel]
    # P9 (luna gate 1): byte-identical serialization, not just equal row
    # dicts — the mirror SMT-LIB scripts must be stable across worker modes.
    def _ndjson(rows):
        out = []
        for row, mirror, meta in rows:
            from regexproof.compiler.cache import serialize_mirror

            script = serialize_mirror(mirror, meta) if mirror is not None else None
            out.append((row, script))
        return out

    s_bytes = json.dumps(_ndjson(serial), sort_keys=True)
    p_bytes = json.dumps(_ndjson(parallel), sort_keys=True)
    assert s_bytes == p_bytes, "serial and spawned worker output must be byte-identical"
    for (_serial_row, serial_mirror, serial_meta), (_parallel_row, parallel_mirror, parallel_meta) in zip(serial, parallel, strict=True):
        assert serialize_mirror(serial_mirror) == serialize_mirror(parallel_mirror)
        assert serial_meta == parallel_meta
