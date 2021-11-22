import ast
from typing import Optional, Union
from dataclasses import dataclass, field
from inspect import Signature


@dataclass
class OverloadFunction:
    ast: Union[ast.FunctionDef, ast.AsyncFunctionDef]
    signature: Signature = field(default_factory=Signature)
    title: str = ''
    docstring: Optional[str] = None
    returns: str = ''
