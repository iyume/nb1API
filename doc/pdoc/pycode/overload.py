import ast
import inspect
from typing import Any, Callable, List, Dict, Union, Optional, get_args
from copy import deepcopy
from random import randint
from inspect import Signature

from pdoc.utils import signature_repr, convert_anno_new_style
from pdoc.schema import OverloadFunction


T_Function = Union[ast.FunctionDef, ast.AsyncFunctionDef]


def extract_all_overloads(
    source: str,
    *,
    globals: Optional[Dict[str, Any]] = None
) -> 'OverloadPicker':
    picker = OverloadPicker(globals or source)
    astmodule = ast.parse(source)
    picker.visit(astmodule)
    return picker


class OverloadPicker(ast.NodeVisitor):
    """
    Python ast visitor to pick up overload function signature and docstring.
    """

    def __init__(
        self,
        source: Union[Dict[str, Any], str],
        encoding: str = 'utf-8'
    ) -> None:
        self.encoding = encoding
        self.context: List[str] = []
        self.current_function: Optional[T_Function] = None
        self.current_class: Optional[ast.ClassDef] = None
        self.overloads: Dict[str, List[OverloadFunction]] = {}
        self.globals: Dict[str, Any] = {}
        self.typing: List[str] = []
        self.typing_overload: List[str] = []
        super().__init__()
        if isinstance(source, str):
            try:
                exec(source, self.globals)
            except Exception:
                pass
        elif isinstance(source, dict):
            self.globals = source.copy()

    def is_overload(
        self,
        node: T_Function
    ) -> bool:
        overload_ids = [f'{i}.overload' for i in self.typing] + self.typing_overload
        for decorator in node.decorator_list:
            if ast.unparse(decorator) in overload_ids:
                return True
        return False

    def exec_safety(
        self,
        node: T_Function
    ) -> Callable:
        """Safely exec source code by giving a random fake name."""
        node = deepcopy(node)
        newname = self.get_random_function_name()
        node.name = newname
        source = ast.unparse(node)
        globals = self.globals.copy()
        exec(source, globals)
        return globals[newname]

    def get_random_function_name(
        self,
        a: int = 0,
        b: int = 10000000
    ) -> str:
        """Generate random function name, maybe redundant."""
        s = f'nb1API{randint(a, b)}'
        while s in self.globals:
            s = f'nb1API{randint(a, b)}'
        return s

    def get_qualname_for(self, name: str) -> str:
        if self.current_class:
            return f'{self.current_class.name}.{name}'
        return name

    def add_overload_signature(self, overload: OverloadFunction) -> None:
        if not self.current_function:
            return
        node = self.current_function
        node = deepcopy(node)
        node.decorator_list.clear()
        unwrap_obj = self.exec_safety(node)
        if not callable(unwrap_obj):
            raise TypeError(f'Unknown type: {type(unwrap_obj)}')
        signature = inspect.signature(unwrap_obj)
        overload.signature = signature

    def add_overload_describe(self, overload: OverloadFunction) -> None:
        """Add signature_repr and returns for overload."""
        if (
            not self.current_function or
            overload.signature.return_annotation is Signature.empty
        ):
            return
        node = self.current_function
        if node.returns:
            if (isinstance(node.returns, ast.Subscript) and
                isinstance(node.returns.value, ast.Name) and
                node.returns.value.id == 'Union' and  # commonly
                isinstance(node.returns.slice, ast.Tuple)):
                returns = [ast.unparse(_) for _ in node.returns.slice.elts]
            else:
                returns = [ast.unparse(node.returns)]
            returns = [convert_anno_new_style(s) for s in returns]
            overload.title = signature_repr(overload.signature, returns)
            overload.returns = convert_anno_new_style(ast.unparse(node.returns))

    def add_overload_docstring(self, overload: OverloadFunction) -> None:
        if not self.current_function:
            return
        node = self.current_function.body[0]
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
            if isinstance(node.value.s, str):
                docstring = node.value.s
            else:
                docstring = node.value.s.decode(self.encoding)
            overload.docstring = inspect.cleandoc(docstring)

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
        # ignore class inner class and avoid recover
        if self.current_class is None:
            self.current_class = node
            self.context.append(node.name)
            for child in node.body:
                if isinstance(child, get_args(T_Function)):
                    self.visit(child)
            self.context.pop()
            self.current_class = None

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        # ignore function inner function and avoid recover
        if self.current_function is None:
            qualname = self.get_qualname_for(node.name)
            self.current_function = node
            self.context.append(node.name)
            if self.is_overload(node):
                overload = OverloadFunction(ast=node)
                self.add_overload_signature(overload)
                self.add_overload_describe(overload)  # must call after self.add_overload_signature
                self.add_overload_docstring(overload)
                self.overloads.setdefault(qualname, []).append(overload)
            self.context.pop()
            self.current_function = None

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.visit_FunctionDef(node)  # type: ignore
