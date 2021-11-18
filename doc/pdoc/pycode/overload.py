import ast
import inspect
from typing import Any, Callable, List, Dict, Union, Optional, get_args
from copy import deepcopy
from inspect import Signature


T_Function = Union[ast.FunctionDef, ast.AsyncFunctionDef]


def extract_all_overloads(source: str) -> 'OverloadPicker':
    picker = OverloadPicker(source)
    astmodule = ast.parse(source)
    picker.visit(astmodule)
    return picker


class OverloadPicker(ast.NodeVisitor):
    """
    Python ast visitor to pick up overload function source.
    """

    def __init__(self, source: str) -> None:
        self.context: List[str] = []
        self.current_class: Optional[ast.ClassDef] = None
        self.overloads: Dict[str, List[Signature]] = {}
        self.functions: Dict[str, List[T_Function]] = {}
        self.globals: Dict[str, Any] = {}
        self.implements: Dict[str, Callable] = {}
        self.typing: List[str] = []
        self.typing_overload: List[str] = []
        super().__init__()
        try:
            exec(source, self.globals)
        except Exception:
            return

    def is_overload(self, node: T_Function) -> bool:
        overload_ids = [f'{i}.overload' for i in self.typing] + self.typing_overload
        for decorator in node.decorator_list:
            if ast.unparse(decorator) in overload_ids:
                return True
        return False

    def add_implement_for(self, name: str) -> None:
        if name in self.globals:
            self.implements.setdefault(name, self.globals[name])

    def add_overload_signature(self, node: T_Function) -> None:
        qualname = node.name
        if self.current_class:
            qualname = f'{self.current_class.name}.{node.name}'
        overloads = self.overloads.setdefault(qualname, [])
        node = deepcopy(node)
        node.decorator_list.clear()
        unwrap_source = ast.unparse(node)
        self.add_implement_for(node.name)
        _globals = self.globals.copy()
        exec(unwrap_source, _globals)
        unwrap_obj = _globals[node.name]
        if not callable(unwrap_obj):
            raise TypeError(f'Unknown type: {type(unwrap_obj)}')
        signature = inspect.signature(_globals[node.name])
        overloads.append(signature)

    def visit_Import(self, node: ast.Import) -> None:
        for name in node.names:
            if name.name == 'typing':
                self.typing.append(name.asname or name.name)
            elif name.name == 'typing.overload':
                self.typing_overload.append(name.asname or name.name)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for name in node.names:
            if node.module == 'typing' and name.name == 'overload':
                self.typing_overload.append(name.asname or name.name)

    def visit_Try(self, node: ast.Try) -> None:
        # ignore try stmt special in module
        return

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Handles ClassDef node and set context."""
        # ignore class inner class
        if self.current_class is None:
            self.current_class = node
            self.context.append(node.name)
            for child in node.body:
                if isinstance(child, get_args(T_Function)):
                    self.visit(child)
            self.context.pop()
            self.current_class = None

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Handles FunctionDef node and set context."""
        self.context.append(node.name)
        lst = self.functions.setdefault(node.name, [])
        lst.append(node)
        if self.is_overload(node):
            self.add_overload_signature(node)
        self.context.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """Handles AsyncFunctionDef node and set context."""
        self.visit_FunctionDef(node)  # type: ignore
