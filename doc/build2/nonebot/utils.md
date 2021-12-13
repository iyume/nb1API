---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.utils` 模块

## _def_ `escape_tag(s)`

- **说明**

:说明:

用于记录带颜色日志时转义 ``<tag>`` 类型特殊标签

:参数:

  * ``s: str``: 需要转义的字符串

:返回:

  - ``str``

- **参数**

    - `s` (str)

- **返回**

    - `str`

## _def_ `run_sync(func)`

- **说明**

:说明:

一个用于包装 sync function 为 async function 的装饰器

:参数:

  * ``func: Callable[..., Any]``: 被装饰的同步函数

:返回:

  - ``Callable[..., Awaitable[Any]]``

- **参数**

    - `func` ((*Any, **Any) -> Any)

- **返回**

    - `(*Any, **Any) -> Awaitable[Any]`

## _def_ `logger_wrapper(logger_name)`

- **说明**

:说明:

用于打印 adapter 的日志。

:log 参数:

* ``level: Literal['WARNING', 'DEBUG', 'INFO']``: 日志等级
* ``message: str``: 日志信息
* ``exception: Optional[Exception]``: 异常信息

- **参数**

    - `logger_name` (str)

- **返回**

    - `Unknown`

## _class_ `DataclassEncoder(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)`

- **说明**

:说明:

在JSON序列化 ``Message`` (List[Dataclass]) 时使用的 ``JSONEncoder``

- **参数**

    - `skipkeys`

    - `ensure_ascii`

    - `check_circular`

    - `allow_nan`

    - `sort_keys`

    - `indent`

    - `separators`

    - `default`

### _method_ `default(self, o)`

- **说明**

Implement this method in a subclass such that it returns

a serializable object for ``o``, or calls the base implementation
(to raise a ``TypeError``).

For example, to support arbitrary iterators, you could
implement default like this::

    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Let the base class default method raise the TypeError
        return JSONEncoder.default(self, o)

- **参数**

    - `o`

- **返回**

    - `Unknown`