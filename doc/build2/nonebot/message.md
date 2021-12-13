---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.message` 模块

事件处理
========

NoneBot 内部处理并按优先级分发事件给所有事件响应器，提供了多个插槽以进行事件的预处理等。

## _var_ `_event_preprocessors`

- **类型:** 

## _var_ `_event_postprocessors`

- **类型:** 

## _var_ `_run_preprocessors`

- **类型:** 

## _var_ `_run_postprocessors`

- **类型:** 

## _def_ `event_preprocessor(func)`

- **说明**

:说明:

事件预处理。装饰一个函数，使它在每次接收到事件并分发给各响应器之前执行。

:参数:

  事件预处理函数接收三个参数。

  * ``bot: Bot``: Bot 对象
  * ``event: Event``: Event 对象
  * ``state: T_State``: 当前 State

- **参数**

    - `func` ((Bot, Event, dict[Any, Any]) -> Awaitable[NoneType])

- **返回**

    - `(Bot, Event, dict[Any, Any]) -> Awaitable[NoneType]`

## _def_ `event_postprocessor(func)`

- **说明**

:说明:

事件后处理。装饰一个函数，使它在每次接收到事件并分发给各响应器之后执行。

:参数:

  事件后处理函数接收三个参数。

  * ``bot: Bot``: Bot 对象
  * ``event: Event``: Event 对象
  * ``state: T_State``: 当前事件运行前 State

- **参数**

    - `func` ((Bot, Event, dict[Any, Any]) -> Awaitable[NoneType])

- **返回**

    - `(Bot, Event, dict[Any, Any]) -> Awaitable[NoneType]`

## _def_ `run_preprocessor(func)`

- **说明**

:说明:

运行预处理。装饰一个函数，使它在每次事件响应器运行前执行。

:参数:

  运行预处理函数接收四个参数。

  * ``matcher: Matcher``: 当前要运行的事件响应器
  * ``bot: Bot``: Bot 对象
  * ``event: Event``: Event 对象
  * ``state: T_State``: 当前 State

- **参数**

    - `func` ((Matcher, Bot, Event, dict[Any, Any]) -> Awaitable[NoneType])

- **返回**

    - `(Matcher, Bot, Event, dict[Any, Any]) -> Awaitable[NoneType]`

## _def_ `run_postprocessor(func)`

- **说明**

:说明:

运行后处理。装饰一个函数，使它在每次事件响应器运行后执行。

:参数:

  运行后处理函数接收五个参数。

  * ``matcher: Matcher``: 运行完毕的事件响应器
  * ``exception: Optional[Exception]``: 事件响应器运行错误（如果存在）
  * ``bot: Bot``: Bot 对象
  * ``event: Event``: Event 对象
  * ``state: T_State``: 当前 State

- **参数**

    - `func` ((Matcher, Exception | None, Bot, Event, dict[Any, Any]) -> Awaitable[NoneType])

- **返回**

    - `(Matcher, Exception | None, Bot, Event, dict[Any, Any]) -> Awaitable[NoneType]`

## _async def_ `handle_event(bot, event)`

- **说明**

:说明:

处理一个事件。调用该函数以实现分发事件。

:参数:

  * ``bot: Bot``: Bot 对象
  * ``event: Event``: Event 对象

:示例:

.. code-block:: python

    import asyncio
    asyncio.create_task(handle_event(bot, event))

- **参数**

    - `bot` (Bot)

    - `event` (Event)

- **返回**

    - `None`