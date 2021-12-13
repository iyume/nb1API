---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.typing` 模块

类型
====

下面的文档中，「类型」部分使用 Python 的 Type Hint 语法，见 `PEP 484`_、`PEP 526`_ 和 `typing`_。

除了 Python 内置的类型，下面还出现了如下 NoneBot 自定类型，实际上它们是 Python 内置类型的别名。

以下类型均可从 nonebot.typing 模块导入。

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _PEP 526:
    https://www.python.org/dev/peps/pep-0526/

.. _typing:
    https://docs.python.org/3/library/typing.html

## _var_ `T_Wrapped`

- **类型:** 

## _var_ `T_State`

- **类型:** 

- **说明**

:类型: ``Dict[Any, Any]``

:说明:

  事件处理状态 State 类型

## _var_ `T_StateFactory`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Event], Awaitable[T_State]]``

:说明:

  事件处理状态 State 类工厂函数

## _var_ `T_BotConnectionHook`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot], Awaitable[None]]``

:说明:

  Bot 连接建立时执行的函数

## _var_ `T_BotDisconnectionHook`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot], Awaitable[None]]``

:说明:

  Bot 连接断开时执行的函数

## _var_ `T_CallingAPIHook`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, str, Dict[str, Any]], Awaitable[None]]``

:说明:

  ``bot.call_api`` 时执行的函数

## _var_ `T_CalledAPIHook`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Optional[Exception], str, Dict[str, Any], Any], Awaitable[None]]``

:说明:

  ``bot.call_api`` 后执行的函数，参数分别为 bot, exception, api, data, result

## _var_ `T_EventPreProcessor`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Event, T_State], Awaitable[None]]``

:说明:

  事件预处理函数 EventPreProcessor 类型

## _var_ `T_EventPostProcessor`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Event, T_State], Awaitable[None]]``

:说明:

  事件预处理函数 EventPostProcessor 类型

## _var_ `T_RunPreProcessor`

- **类型:** 

- **说明**

:类型: ``Callable[[Matcher, Bot, Event, T_State], Awaitable[None]]``

:说明:

  事件响应器运行前预处理函数 RunPreProcessor 类型

## _var_ `T_RunPostProcessor`

- **类型:** 

- **说明**

:类型: ``Callable[[Matcher, Optional[Exception], Bot, Event, T_State], Awaitable[None]]``

:说明:

  事件响应器运行前预处理函数 RunPostProcessor 类型，第二个参数为运行时产生的错误（如果存在）

## _var_ `T_RuleChecker`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Event, T_State], Union[bool, Awaitable[bool]]]``

:说明:

  RuleChecker 即判断是否响应事件的处理函数。

## _var_ `T_PermissionChecker`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Event], Union[bool, Awaitable[bool]]]``

:说明:

  RuleChecker 即判断是否响应消息的处理函数。

## _var_ `T_Handler`

- **类型:** 

- **说明**

:类型:

* ``Callable[[Bot, Event, T_State], Union[Awaitable[None], Awaitable[NoReturn]]]``
  * ``Callable[[Bot, Event], Union[Awaitable[None], Awaitable[NoReturn]]]``
  * ``Callable[[Bot, T_State], Union[Awaitable[None], Awaitable[NoReturn]]]``
  * ``Callable[[Bot], Union[Awaitable[None], Awaitable[NoReturn]]]``

:说明:

  Handler 即事件的处理函数。

## _var_ `T_ArgsParser`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Event, T_State], Union[Awaitable[None], Awaitable[NoReturn]]]``

:说明:

  ArgsParser 即消息参数解析函数，在 Matcher.got 获取参数时被运行。

## _var_ `T_TypeUpdater`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Event, T_State, str], Awaitable[str]]``

:说明:

  TypeUpdater 在 Matcher.pause, Matcher.reject 时被运行，用于更新响应的事件类型。默认会更新为 ``message``。

## _var_ `T_PermissionUpdater`

- **类型:** 

- **说明**

:类型: ``Callable[[Bot, Event, T_State, Permission], Awaitable[Permission]]``

:说明:

  PermissionUpdater 在 Matcher.pause, Matcher.reject 时被运行，用于更新会话对象权限。默认会更新为当前事件的触发对象。

## _def_ `overrides(InterfaceClass)`

- **参数**

    - `InterfaceClass` (object)

- **返回**

    - `Unknown`