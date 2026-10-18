"""Exact-pin replay helpers for Tracecat custom RBAC scope names."""

from __future__ import annotations

import ast
import copy
import hashlib
import os
import subprocess
from functools import lru_cache
from pathlib import Path
from types import ModuleType

from regexproof.groundtruth.tracecat_replay import PIN, source_root as tracecat_source_root

REPOSITORY = "https://github.com/TracecatHQ/tracecat"
SOURCE_FILE = "tracecat/authz/controls.py"
SOURCE_SHA256 = "a63e61a139aeb35665b43f2a000095b42e8c6050778144f7c9f28af5c58ed32b"
SCHEMA_FILE = "packages/tracecat-ee/tracecat_ee/rbac/schemas.py"
SERVICE_FILE = "packages/tracecat-ee/tracecat_ee/rbac/service.py"
ROUTER_FILE = "packages/tracecat-ee/tracecat_ee/rbac/router.py"
SCOPE_PATTERN = r"^[a-z0-9:_.*-]+$"
WEAKENED_PATTERN = r"^[a-z0-9:_.*?-]+$"
ALLOWED_SCOPE_CHARS = frozenset(
    "abcdefghijklmnopqrstuvwxyz0123456789:_.*-"
)
NONSTAR_GLOB_CHARS = frozenset("?[]")
MUTATION_SCOPE = "action:tools?okta.*:execute"
MUTATION_REQUIRED_SCOPE = "action:toolsXokta.list_users:execute"


def source_root() -> Path:
    """Return the clean exact-pin Tracecat checkout used by this replay."""
    return tracecat_source_root()


def _source_bytes(root: Path, relative: str) -> bytes:
    path = root / relative
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"pinned Tracecat source is missing or symlinked: {path}")
    committed = subprocess.run(
        ["git", "-C", str(root), "show", f"{PIN}:{relative}"],
        check=True,
        capture_output=True,
        timeout=20,
    ).stdout
    actual = path.read_bytes()
    if actual != committed:
        raise RuntimeError(f"working source differs from {PIN}:{relative}")
    return actual


def source_digests(root: Path | None = None) -> dict[str, str]:
    root = root or source_root()
    files = (SOURCE_FILE, SCHEMA_FILE, SERVICE_FILE, ROUTER_FILE)
    result = {name: hashlib.sha256(_source_bytes(root, name)).hexdigest() for name in files}
    if result[SOURCE_FILE] != SOURCE_SHA256:
        raise RuntimeError("Tracecat scope validator digest differs from the adopted contract")
    return result


@lru_cache(maxsize=4)
def _class_scope_create(root: Path, *, weaken: bool = False) -> type:
    source = _source_bytes(root, SCHEMA_FILE)
    tree = ast.parse(source, filename=SCHEMA_FILE)
    declaration = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.ClassDef) and node.name == "ScopeCreate"
        ),
        None,
    )
    if declaration is None:
        raise RuntimeError("pinned RBAC schemas no longer define ScopeCreate")
    declaration = copy.deepcopy(declaration)
    fields = [
        node
        for node in declaration.body
        if isinstance(node, ast.AnnAssign)
        and isinstance(node.target, ast.Name)
        and node.target.id == "name"
    ]
    if len(fields) != 1 or not isinstance(fields[0].value, ast.Call):
        raise RuntimeError("ScopeCreate.name is no longer a single Field declaration")
    field_call = fields[0].value
    pattern_keywords = [keyword for keyword in field_call.keywords if keyword.arg == "pattern"]
    if (
        len(pattern_keywords) != 1
        or not isinstance(pattern_keywords[0].value, ast.Constant)
        or pattern_keywords[0].value.value != SCOPE_PATTERN
    ):
        raise RuntimeError("ScopeCreate.name no longer uses the expected scope allowlist")
    if weaken:
        pattern_keywords[0].value.value = WEAKENED_PATTERN

    module_ast = ast.Module(
        body=[
            ast.ImportFrom(
                module="__future__",
                names=[ast.alias(name="annotations")],
                level=0,
            ),
            ast.ImportFrom(
                module="pydantic",
                names=[ast.alias(name="BaseModel"), ast.alias(name="Field")],
                level=0,
            ),
            declaration,
        ],
        type_ignores=[],
    )
    ast.fix_missing_locations(module_ast)
    namespace: dict[str, object] = {"__name__": f"tracecat_rbac_schema_{PIN}"}
    exec(compile(module_ast, SCHEMA_FILE, "exec"), namespace)
    return namespace["ScopeCreate"]


@lru_cache(maxsize=4)
def _controls_module(root: Path, *, weaken: bool = False) -> ModuleType:
    source = _source_bytes(root, SOURCE_FILE)
    tree = ast.parse(source, filename=SOURCE_FILE)
    selected: list[ast.stmt] = []
    found_pattern = False
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "SCOPE_PATTERN"
            for target in node.targets
        ):
            value = node.value
            if (
                not isinstance(value, ast.Call)
                or not isinstance(value.func, ast.Attribute)
                or not isinstance(value.func.value, ast.Name)
                or value.func.value.id != "re"
                or value.func.attr != "compile"
                or not value.args
                or not isinstance(value.args[0], ast.Constant)
                or value.args[0].value != SCOPE_PATTERN
            ):
                raise RuntimeError("pinned SCOPE_PATTERN declaration changed")
            node = copy.deepcopy(node)
            if weaken:
                node.value.args[0].value = WEAKENED_PATTERN
            selected.append(node)
            found_pattern = True
        elif isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "_ACTION_IMPLIES"
            for target in node.targets
        ):
            selected.append(node)
        elif isinstance(node, ast.FunctionDef) and node.name in {
            "_implied_scopes",
            "validate_scope_string",
            "scope_matches",
        }:
            selected.append(node)
    if not found_pattern or not {"validate_scope_string", "scope_matches"}.issubset(
        {
            node.name for node in selected if isinstance(node, ast.FunctionDef)
        }
    ):
        raise RuntimeError("pinned scope validator or matcher is missing")

    module_ast = ast.Module(
        body=[
            ast.Import(names=[ast.alias(name="re")]),
            ast.ImportFrom(module="fnmatch", names=[ast.alias(name="fnmatch")], level=0),
            *selected,
        ],
        type_ignores=[],
    )
    ast.fix_missing_locations(module_ast)
    namespace: dict[str, object] = {"__name__": f"tracecat_rbac_scope_{PIN}"}
    exec(compile(module_ast, SOURCE_FILE, "exec"), namespace)
    module = ModuleType(str(namespace["__name__"]))
    module.__dict__.update(namespace)
    return module


@lru_cache(maxsize=2)
def _route_scope_shape(root: Path) -> tuple[bool, bool, bool]:
    """Check the pinned route, schema/service call, and service validation order."""
    router = ast.parse(_source_bytes(root, ROUTER_FILE), filename=ROUTER_FILE)
    route = next(
        (
            node
            for node in router.body
            if isinstance(node, ast.AsyncFunctionDef) and node.name == "create_scope"
        ),
        None,
    )
    if route is None:
        raise RuntimeError("pinned RBAC router no longer defines create_scope")
    route_guard = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "require_scope"
        and any(
            isinstance(arg, ast.Constant) and arg.value == "org:rbac:create"
            for arg in node.args
        )
        for decorator in route.decorator_list
        for node in ast.walk(decorator)
    )
    route_uses_scope_schema = any(
        arg.arg == "params"
        and isinstance(arg.annotation, ast.Name)
        and arg.annotation.id == "ScopeCreate"
        for arg in (*route.args.posonlyargs, *route.args.args, *route.args.kwonlyargs)
    )
    route_calls_service_with_name = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "service"
        and node.func.attr == "create_scope"
        and any(
            keyword.arg == "name"
            and isinstance(keyword.value, ast.Attribute)
            and isinstance(keyword.value.value, ast.Name)
            and keyword.value.value.id == "params"
            and keyword.value.attr == "name"
            for keyword in node.keywords
        )
        for node in ast.walk(route)
    )

    service = ast.parse(_source_bytes(root, SERVICE_FILE), filename=SERVICE_FILE)
    service_class = next(
        (
            node
            for node in service.body
            if isinstance(node, ast.ClassDef) and node.name == "RBACService"
        ),
        None,
    )
    method = next(
        (
            child
            for child in service_class.body
            if isinstance(child, ast.AsyncFunctionDef) and child.name == "create_scope"
        ),
        None,
    ) if service_class is not None else None
    if method is None:
        raise RuntimeError("pinned RBAC service no longer defines create_scope")
    final_colon_parse = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "name"
        and node.func.attr == "rsplit"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == ":"
        for node in ast.walk(method)
    )
    service_validates_name = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "validate_scope_string"
        and node.args
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == "name"
        for node in ast.walk(method)
    )
    scope_constructor = next(
        (
            node
            for node in ast.walk(method)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "Scope"
        ),
        None,
    )
    validation_before_persist = bool(
        service_validates_name
        and scope_constructor is not None
        and any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "validate_scope_string"
            and node.lineno < scope_constructor.lineno
            for node in ast.walk(method)
        )
    )
    return (
        route_guard,
        route_uses_scope_schema and route_calls_service_with_name,
        final_colon_parse and validation_before_persist,
    )


@lru_cache(maxsize=8192)
def exact_scope_name_acceptance(value: str, *, weaken: bool = False) -> bool:
    """Replay the pinned request model plus service validator and name parser."""
    root = source_root()
    model = _class_scope_create(root, weaken=weaken)
    controls = _controls_module(root, weaken=weaken)
    route_guard, route_calls_service, service_validates = _route_scope_shape(root)
    if not route_guard or not route_calls_service or not service_validates:
        raise RuntimeError("pinned scope creation path or validation order changed")
    try:
        parsed = model(name=value)
    except Exception:
        return False
    if not controls.validate_scope_string(parsed.name):
        return False
    return len(parsed.name.rsplit(":", maxsplit=1)) == 2


def current_model_accepts(value: str) -> bool:
    try:
        _class_scope_create(source_root())(name=value)
        return True
    except Exception:
        return False


def current_helper_accepts(value: str) -> bool:
    return bool(_controls_module(source_root()).validate_scope_string(value))


def rbac_scope_question_mark_mutation_reproduces(witness: dict[str, object]) -> bool:
    """Mutate both exact allowlists and replay the broadened fnmatch grant."""
    scope_name = witness.get("scope_name")
    if scope_name != MUTATION_SCOPE:
        return False
    root = source_root()
    route_guard, route_calls_service, service_validates = _route_scope_shape(root)
    if not route_guard or not route_calls_service or not service_validates:
        return False
    if current_model_accepts(MUTATION_SCOPE) or current_helper_accepts(MUTATION_SCOPE):
        return False
    model = _class_scope_create(root, weaken=True)
    controls = _controls_module(root, weaken=True)
    try:
        parsed = model(name=MUTATION_SCOPE)
    except Exception:
        return False
    if not controls.validate_scope_string(parsed.name):
        return False
    if len(parsed.name.rsplit(":", maxsplit=1)) != 2:
        return False
    return bool(
        controls.scope_matches(
            parsed.name,
            MUTATION_REQUIRED_SCOPE,
        )
    )


__all__ = [
    "ALLOWED_SCOPE_CHARS",
    "MUTATION_REQUIRED_SCOPE",
    "MUTATION_SCOPE",
    "NONSTAR_GLOB_CHARS",
    "PIN",
    "REPOSITORY",
    "ROUTER_FILE",
    "SCHEMA_FILE",
    "SERVICE_FILE",
    "SOURCE_FILE",
    "SOURCE_SHA256",
    "SCOPE_PATTERN",
    "WEAKENED_PATTERN",
    "current_helper_accepts",
    "current_model_accepts",
    "exact_scope_name_acceptance",
    "rbac_scope_question_mark_mutation_reproduces",
    "source_digests",
    "source_root",
]
