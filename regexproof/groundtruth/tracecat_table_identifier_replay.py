"""Exact-pin replay helpers for Tracecat table/column identifier names."""

from __future__ import annotations

import ast
import copy
import hashlib
import subprocess
from functools import lru_cache
from pathlib import Path
from types import ModuleType

from regexproof.groundtruth.tracecat_replay import PIN, source_root as tracecat_source_root

REPOSITORY = "https://github.com/TracecatHQ/tracecat"
SCHEMA_FILE = "tracecat/tables/schemas.py"
SERVICE_FILE = "tracecat/tables/service.py"
ROUTER_FILE = "tracecat/tables/router.py"
INTERNAL_ROUTER_FILE = "tracecat/tables/internal_router.py"
SCHEMA_SHA256 = "3cf61426a27e200640ad55406dc3f67ee7cd445b2cf70d73205e0709b594e881"
IDENTIFIER_PATTERN = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
WEAKENED_PATTERN = r'^[a-zA-Z_][a-zA-Z0-9_"]*$'
QUOTE = '"'
MUTATION_NAME = 'a"'


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
    files = (SCHEMA_FILE, SERVICE_FILE, ROUTER_FILE, INTERNAL_ROUTER_FILE)
    digests = {
        name: hashlib.sha256(_source_bytes(root, name)).hexdigest() for name in files
    }
    if digests[SCHEMA_FILE] != SCHEMA_SHA256:
        raise RuntimeError("Tracecat table identifier schema digest changed")
    return digests


def _schema_module(root: Path, *, weaken: bool = False) -> ModuleType:
    source = _source_bytes(root, SCHEMA_FILE)
    tree = ast.parse(source, filename=SCHEMA_FILE)
    pattern_assignment = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "IDENTIFIER_PATTERN"
                for target in node.targets
            )
        ),
        None,
    )
    validator = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name == "_validate_identifier_name"
        ),
        None,
    )
    if pattern_assignment is None or validator is None:
        raise RuntimeError("pinned identifier pattern or validator is missing")
    pattern_assignment = copy.deepcopy(pattern_assignment)
    value = pattern_assignment.value
    if (
        not isinstance(value, ast.Call)
        or not isinstance(value.func, ast.Attribute)
        or not isinstance(value.func.value, ast.Name)
        or value.func.value.id != "re"
        or value.func.attr != "compile"
        or not value.args
        or not isinstance(value.args[0], ast.Constant)
        or value.args[0].value != IDENTIFIER_PATTERN
    ):
        raise RuntimeError("pinned identifier pattern declaration changed")
    if weaken:
        value.args[0].value = WEAKENED_PATTERN

    selected_classes: list[ast.ClassDef] = []
    for class_name, validator_name in (
        ("TableColumnCreate", "validate_column_name"),
        ("TableCreate", "validate_table_name"),
    ):
        source_class = next(
            (
                node
                for node in tree.body
                if isinstance(node, ast.ClassDef) and node.name == class_name
            ),
            None,
        )
        if source_class is None:
            raise RuntimeError(f"pinned schemas no longer define {class_name}")
        name_fields = [
            node
            for node in source_class.body
            if isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "name"
        ]
        methods = [
            node
            for node in source_class.body
            if isinstance(node, ast.FunctionDef) and node.name == validator_name
        ]
        if len(name_fields) != 1 or len(methods) != 1:
            raise RuntimeError(f"{class_name} name field/validator shape changed")
        field_node = copy.deepcopy(name_fields[0])
        method_node = copy.deepcopy(methods[0])
        if not isinstance(field_node.value, ast.Call) or not isinstance(
            field_node.value.func, ast.Name
        ) or field_node.value.func.id != "Field":
            raise RuntimeError(f"{class_name}.name is no longer a Field declaration")
        field_args = {
            keyword.arg: keyword.value
            for keyword in field_node.value.keywords
            if keyword.arg is not None
        }
        if not (
            isinstance(field_args.get("min_length"), ast.Constant)
            and field_args["min_length"].value == 1
            and isinstance(field_args.get("max_length"), ast.Constant)
            and field_args["max_length"].value == 100
        ):
            raise RuntimeError(f"{class_name}.name bounds changed")
        if not any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_validate_identifier_name"
            for node in ast.walk(method_node)
        ):
            raise RuntimeError(f"{class_name}.{validator_name} no longer calls helper")
        method_node.name = validator_name
        selected_classes.append(
            ast.ClassDef(
                name=f"{class_name}NameProbe",
                bases=[ast.Name(id="BaseModel", ctx=ast.Load())],
                keywords=[],
                body=[field_node, method_node],
                decorator_list=[],
            )
        )

    module_ast = ast.Module(
        body=[
            ast.Import(names=[ast.alias(name="re")]),
            ast.ImportFrom(
                module="pydantic",
                names=[
                    ast.alias(name="BaseModel"),
                    ast.alias(name="Field"),
                    ast.alias(name="field_validator"),
                ],
                level=0,
            ),
            pattern_assignment,
            validator,
            *selected_classes,
        ],
        type_ignores=[],
    )
    ast.fix_missing_locations(module_ast)
    namespace: dict[str, object] = {"__name__": f"tracecat_table_name_{PIN}"}
    exec(compile(module_ast, SCHEMA_FILE, "exec"), namespace)
    module = ModuleType(str(namespace["__name__"]), "exact pinned name models")
    module.__dict__.update(namespace)
    return module


@lru_cache(maxsize=4)
def _model_classes(root: Path, *, weaken: bool = False) -> tuple[type, type]:
    module = _schema_module(root, weaken=weaken)
    return (
        module.__dict__["TableColumnCreateNameProbe"],
        module.__dict__["TableCreateNameProbe"],
    )


@lru_cache(maxsize=4)
def _service_functions(root: Path):
    source = _source_bytes(root, SERVICE_FILE)
    tree = ast.parse(source, filename=SERVICE_FILE)
    selected = []
    for wanted in ("validate_identifier", "quote_identifier"):
        function = next(
            (
                node
                for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name == wanted
            ),
            None,
        )
        if function is None:
            raise RuntimeError(f"pinned service function {wanted} is missing")
        selected.append(function)
    module_ast = ast.Module(body=selected, type_ignores=[])
    ast.fix_missing_locations(module_ast)
    namespace: dict[str, object] = {"__name__": f"tracecat_table_service_{PIN}"}
    exec(compile(module_ast, SERVICE_FILE, "exec"), namespace)
    return namespace["validate_identifier"], namespace["quote_identifier"]


def current_model_accepts(value: str, *, kind: str, weaken: bool = False) -> bool:
    import pydantic

    if kind not in {"column", "table"}:
        raise ValueError(f"unsupported identifier kind: {kind}")
    root = source_root()
    column_model, table_model = _model_classes(root, weaken=weaken)
    model = column_model if kind == "column" else table_model
    try:
        model(name=value)
    except pydantic.ValidationError:
        return False
    return True


def current_service_accepts(value: str) -> bool:
    validate_identifier, _ = _service_functions(source_root())
    try:
        validate_identifier(value)
    except ValueError:
        return False
    return True


def current_quote_identifier(value: str) -> str:
    _, quote_identifier = _service_functions(source_root())
    return quote_identifier(value)


def _route_and_sink_shape(root: Path) -> dict[str, bool]:
    router_tree = ast.parse(_source_bytes(root, ROUTER_FILE), filename=ROUTER_FILE)
    internal_tree = ast.parse(
        _source_bytes(root, INTERNAL_ROUTER_FILE), filename=INTERNAL_ROUTER_FILE
    )
    service_tree = ast.parse(_source_bytes(root, SERVICE_FILE), filename=SERVICE_FILE)

    def route_has_model(tree: ast.Module, function_name: str, model_name: str) -> bool:
        fn = next(
            (
                node
                for node in ast.walk(tree)
                if isinstance(node, ast.AsyncFunctionDef) and node.name == function_name
            ),
            None,
        )
        if fn is None:
            return False
        params = next(
            (
                arg
                for arg in (*fn.args.args, *fn.args.kwonlyargs)
                if arg.arg == "params"
            ),
            None,
        )
        has_scope = any(
            isinstance(dec, ast.Call)
            and isinstance(dec.func, ast.Name)
            and dec.func.id == "require_scope"
            and dec.args
            and isinstance(dec.args[0], ast.Constant)
            and dec.args[0].value == "table:create"
            for dec in fn.decorator_list
        )
        return (
            params is not None
            and isinstance(params.annotation, ast.Name)
            and params.annotation.id == model_name
            and has_scope
            and any(
                isinstance(node, ast.Await)
                and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Attribute)
                and node.value.func.attr == function_name
                and any(
                    isinstance(arg, ast.Name) and arg.id == "params"
                    for arg in node.value.args
                )
                for node in ast.walk(fn)
            )
        )

    internal_column_route = route_has_model(
        internal_tree, "create_column", "TableColumnCreate"
    )
    internal_table_route = next(
        (
            node
            for node in ast.walk(internal_tree)
            if isinstance(node, ast.AsyncFunctionDef) and node.name == "create_table"
        ),
        None,
    )
    internal_table_scope = bool(
        internal_table_route
        and any(
            isinstance(dec, ast.Call)
            and isinstance(dec.func, ast.Name)
            and dec.func.id == "require_scope"
            and dec.args
            and isinstance(dec.args[0], ast.Constant)
            and dec.args[0].value == "table:create"
            for dec in internal_table_route.decorator_list
        )
    )
    internal_table_create = bool(
        internal_table_route
        and internal_table_scope
        and any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "TableCreate"
            and any(
                keyword.arg == "name"
                and isinstance(keyword.value, ast.Attribute)
                and isinstance(keyword.value.value, ast.Name)
                and keyword.value.value.id == "params"
                and keyword.value.attr == "name"
                for keyword in node.keywords
            )
            for node in ast.walk(internal_table_route)
        )
        and any(
            isinstance(node, ast.Await)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Attribute)
            and node.value.func.attr == "create_table"
            and any(
                isinstance(arg, ast.Call)
                and isinstance(arg.func, ast.Name)
                and arg.func.id == "TableCreate"
                for arg in node.value.args
            )
            for node in ast.walk(internal_table_route)
        )
    )
    service_class = next(
        (
            node
            for node in service_tree.body
            if isinstance(node, ast.ClassDef) and node.name == "BaseTablesService"
        ),
        None,
    )
    service_methods = {
        node.name: node
        for node in service_class.body
        if isinstance(node, ast.AsyncFunctionDef)
    } if service_class else {}
    create_table = service_methods.get("create_table")
    create_column = service_methods.get("create_column")

    def calls_validate_params_name(fn: ast.AsyncFunctionDef | None) -> bool:
        return bool(
            fn
            and any(
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "validate_identifier"
                and node.args
                and isinstance(node.args[0], ast.Attribute)
                and isinstance(node.args[0].value, ast.Name)
                and node.args[0].value.id == "params"
                and node.args[0].attr == "name"
                for node in ast.walk(fn)
            )
        )

    return {
        "public_table_create_route_uses_schema_and_scope": route_has_model(
            router_tree, "create_table", "TableCreate"
        ),
        "public_column_create_route_uses_schema_and_scope": route_has_model(
            router_tree, "create_column", "TableColumnCreate"
        ),
        "internal_table_create_route_requires_scope_and_reconstructs_schema": internal_table_create,
        "internal_column_create_route_uses_schema_and_scope": internal_column_route,
        "service_table_create_validates_name": calls_validate_params_name(create_table),
        "service_column_create_validates_name_and_quotes_column": calls_validate_params_name(
            create_column
        )
        and bool(
            create_column
            and any(
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "quote_identifier"
                for node in ast.walk(create_column)
            )
        ),
    }


def exact_table_path_shape(root: Path | None = None) -> dict[str, bool]:
    root = root or source_root()
    source_digests(root)
    if hashlib.sha256(_source_bytes(root, SCHEMA_FILE)).hexdigest() != SCHEMA_SHA256:
        raise RuntimeError("Tracecat identifier schema differs from adopted source")
    if b"IDENTIFIER_PATTERN.match(value)" not in _source_bytes(root, SCHEMA_FILE):
        raise RuntimeError("identifier helper no longer executes the compiled regex")
    result = _route_and_sink_shape(root)
    if not all(result.values()):
        missing = [key for key, value in result.items() if not value]
        raise RuntimeError(f"pinned table create path changed: {missing}")
    return result


def table_identifier_quote_mutation_reproduces(witness: object = None) -> bool:
    """Show a weakened request check admits quote while sink validation blocks it."""
    if isinstance(witness, dict) and witness.get("mutated_identifier_name") != MUTATION_NAME:
        return False
    exact_table_path_shape()
    return (
        current_model_accepts(MUTATION_NAME, kind="table", weaken=True)
        and current_model_accepts(MUTATION_NAME, kind="column", weaken=True)
        and not current_model_accepts(MUTATION_NAME, kind="table")
        and not current_model_accepts(MUTATION_NAME, kind="column")
        and not current_service_accepts(MUTATION_NAME)
        and current_quote_identifier(MUTATION_NAME) == '"a""'
    )
