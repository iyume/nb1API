from typing import Union, overload
from contextvars import ContextVar

from test_pkg.overload.typing import T_Type


@overload
def func(arg: ContextVar[int]) -> T_Type: ...


@overload
def func(arg: int) -> T_Type: ...


def func(arg: Union[ContextVar[int], int]) -> T_Type: ...
