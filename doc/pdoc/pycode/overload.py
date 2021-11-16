import ast
import inspect
from typing import List, Dict, Union, Optional, Any
from copy import deepcopy
from inspect import Signature


def extract_all_overloads(source: str) -> 'OverloadPicker':
    picker = OverloadPicker(source)
    astmodule = ast.parse(source)
    picker.visit(astmodule)
    return picker


class OverloadPicker(ast.NodeVisitor):
    """
    Python source code parser to pick up overload function signatures.
    """

    def __init__(self, source: str) -> None:
        self.source: str = source
        self.globals: Dict[str, Any] = {}
        self.context: List[str] = []
        self.current_class: Optional[ast.ClassDef] = None
        self.overloads: Dict[str, List[Signature]] = {}
        self.implements: Dict[str, Any] = {}
        self.typing: Optional[str] = None
        self.typing_overload: Optional[str] = None
        super().__init__()
        # exec to get the module __globals__
        # aim to get function signature
        try:
            exec(self.source, self.globals)
        except Exception:
            return

    def get_qualname_for(self, name: str) -> Optional[List[str]]:
        if self.current_function:
            if self.current_class:
                return self.context[:-1] + [name]
            else:
                return None
        else:
            return self.context + [name]

    def is_overload(
        self,
        node: Union[ast.FunctionDef, ast.AsyncFunctionDef]
    ) -> bool:
        overload_ids = []
        if self.typing:
            overload_ids.append('%s.overload' % self.typing)
        if self.typing_overload:
            overload_ids.append(self.typing_overload)
        for decorator in node.decorator_list:
            if ast.unparse(decorator) in overload_ids:
                return True
        return False

    def add_overload_signature(
        self,
        node: Union[ast.FunctionDef, ast.AsyncFunctionDef]
    ) -> None:
        qualname = self.get_qualname_for(node.name)
        if qualname:
            overloads = self.overloads.setdefault(".".join(qualname), [])
        node = deepcopy(node)

    def visit_Import(self, node: ast.Import) -> None:
        for name in node.names:
            if name.name == 'typing':
                self.typing = name.asname or name.name
            elif name.name == 'typing.overload':
                self.typing_overload = name.asname or name.name

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for name in node.names:
            if node.module == 'typing' and name.name == 'overload':
                self.typing_overload = name.asname or name.name

    def visit_Try(self, node: ast.Try) -> None:
        return

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Handles ClassDef node and set context."""
        # ignore class inner class
        if self.current_class is None:
            self.current_class = node
            self.context.append(node.name)
            for child in node.body:
                self.visit(child)
            self.context.pop()
            self.current_class = None

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Handles FunctionDef node and set context."""
        # ignore function inner function
        if self.current_function is None:
            if self.is_overload(node):
                self.add_overload_signature(node)
            self.context.append(node.name)
            self.current_function = node
            for child in node.body:
                self.visit(child)
            self.context.pop()
            self.current_function = None

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        """Handles AsyncFunctionDef node and set context."""
        self.visit_FunctionDef(node)  # type: ignore
