"""Versioned JSON Schema loaders for Phase-1/4 artifact contracts."""

from __future__ import annotations

import json
from pathlib import Path

SCHEMA_DIR = Path(__file__).resolve().parent

EXTRACTOR_SCHEMA_VERSION = "1"
COMPILED_SCHEMA_VERSION = "1"
REDOS_FINDING_SCHEMA_VERSION = "1"


def load_schema(name: str) -> dict:
    path = SCHEMA_DIR / name
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def extractor_schema() -> dict:
    return load_schema("extractor_record.schema.json")


def compiled_pattern_schema() -> dict:
    return load_schema("compiled_pattern.schema.json")


def redos_finding_schema() -> dict:
    return load_schema("redos_finding.schema.json")
