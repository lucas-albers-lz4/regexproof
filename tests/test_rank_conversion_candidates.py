"""Gate 1–2 conversion ranker: drop-before-score, density hijack, no z3."""

from __future__ import annotations

import ast
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "rank_conversion_candidates",
        ROOT / "scripts" / "rank-conversion-candidates.py",
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


rank = _load()


def test_ranker_does_not_import_z3():
    src = (ROOT / "scripts" / "rank-conversion-candidates.py").read_text(
        encoding="utf-8"
    )
    tree = ast.parse(src)
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module.split(".")[0])
    assert "z3" not in imported


def _rec(**kwargs):
    base = {
        "call_kind": "search",
        "pattern": "[a-z]+",
        "site": "net/pbr/files/etc/init.d/pbr:1:0",
        "file": "net/pbr/files/etc/init.d/pbr",
        "encodable": True,
        "compile_reason": None,
        "regex_id": "x",
    }
    base.update(kwargs)
    return base


def test_density_hijack_drops_tests_before_score():
    """Many net/pbr/tests rows must not outrank fewer init.d/pbr rows."""
    rows = []
    for i in range(40):
        rows.append(
            _rec(
                site=f"net/pbr/tests/08_dns/01_nftset_element:{i}:0",
                file="net/pbr/tests/08_dns/01_nftset_element",
                pattern=f"[a-z]{{3}}{i}",
            )
        )
    rows.append(
        _rec(
            site="net/pbr/files/etc/init.d/pbr:213:0",
            pattern="[. ~`!@#$%^&*()+=,<>?;:\\/\\\\-]",
            call_kind="substitution",
        )
    )
    result = rank.rank_rows(rows, vocab=rank.DEFAULT_VOCAB, limit=15)
    assert all(
        "tests/" not in str(k.get("file") or k.get("site") or "")
        for k in result["keep"]
    )
    assert any("init.d/pbr" in str(k.get("file") or "") for k in result["keep"])
    assert any(d["reason"].startswith("path-segment") for d in result["dropped"])


def test_drop_testdata_fixtures_segments_not_filename_substring():
    assert rank.drop_reason(
        _rec(site="pkg/latestest.sh:1:0", file="pkg/latestest.sh")
    ) is None
    assert rank.drop_reason(
        _rec(site="pkg/testdata/foo.sh:1:0", file="pkg/testdata/foo.sh")
    ) == "path-segment:tests|testdata|fixtures"
    assert rank.drop_reason(
        _rec(site="pkg/fixtures/bar.sh:1:0", file="pkg/fixtures/bar.sh")
    ) == "path-segment:tests|testdata|fixtures"


def test_drop_test_filenames():
    assert rank.drop_reason(
        _rec(site="net/x/foo.test.sh:1:0", file="net/x/foo.test.sh")
    ).startswith("test-filename")
    assert rank.drop_reason(
        _rec(site="net/x/test-version.sh:1:0", file="net/x/test-version.sh")
    ).startswith("test-filename")
    assert rank.drop_reason(
        _rec(site="net/x/run_tests.sh:1:0", file="net/x/run_tests.sh")
    ).startswith("test-filename")
    assert rank.drop_reason(_rec(site="net/x/test.sh:1:0", file="net/x/test.sh")) is None


def test_drop_interpolated_and_literal():
    assert rank.drop_reason(_rec(pattern="$IPv4_REGEX")) == "interpolated:$ident"
    assert rank.drop_reason(_rec(pattern="foo$BAR")) == "interpolated"
    assert rank.drop_reason(_rec(pattern="POINTOPOINT")) == "literal-no-metachar"


def test_drop_substitution_without_capture_or_charset():
    assert (
        rank.drop_reason(_rec(call_kind="substitution", pattern="foo.*bar"))
        == "substitution-no-capture-or-charset"
    )
    assert rank.drop_reason(
        _rec(call_kind="substitution", pattern=r".*dev \([^ ]*\).*")
    ) is None
    assert rank.drop_reason(
        _rec(call_kind="substitution", pattern="[.a-z]")
    ) is None


def test_ranker_deterministic_fixture(tmp_path: Path):
    ndjson = tmp_path / "in.ndjson"
    rows = [
        _rec(
            site="net/ddns-scripts/a.sh:1:0",
            file="net/ddns-scripts/a.sh",
            pattern="[0-9.]+",
        ),
        _rec(
            site="net/pbr/files/etc/init.d/pbr:2:0",
            pattern="[a-z0-9_]+",
        ),
        _rec(
            site="net/pbr/tests/x.sh:3:0",
            file="net/pbr/tests/x.sh",
            pattern="[a-z]+",
        ),
    ]
    ndjson.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    a = rank.rank_rows(rank.load_ndjson(ndjson), vocab=rank.DEFAULT_VOCAB, limit=15)
    b = rank.rank_rows(rank.load_ndjson(ndjson), vocab=rank.DEFAULT_VOCAB, limit=15)
    assert a["keep"] == b["keep"]


def test_frozen_openwrt_rank_has_15_keep_and_seed_reasons():
    path = ROOT / "properties" / "generated" / "openwrt_packages_rank.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert len(data["keep"]) == 15
    seeds = data["seeds"]
    assert seeds["pbr-sanitizer"]["status"] == "kept"
    assert seeds["mwan3-dev-capture"]["status"] == "kept"
    assert seeds["ddns-private-ip"]["status"] == "dropped"
    assert "unencodable" in seeds["ddns-private-ip"]["reason"]
    # Density: no tests/ path segment in the frozen keep list.
    assert all("tests/" not in str(k.get("file") or k.get("site") or "") for k in data["keep"])
