---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.handler` 模块

事件处理函数
============

该模块实现事件处理函数的封装，以实现动态参数等功能。

## _class_ `Handler(self, func)`

- **说明**

事件处理函数类

- **参数**

    - `func` ((Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]))

### _property_ `bot_type`

- **类型:** Type[Bot] | inspect._empty

- **说明**

:类型: ``Union[Type["Bot"], inspect.Parameter.empty]``

:说明: 事件处理函数接受的 Bot 对象类型

### _property_ `event_type`

- **类型:** Type[Event] | inspect._empty | NoneType

- **说明**

:类型: ``Optional[Union[Type[Event], inspect.Parameter.empty]]``

:说明: 事件处理函数接受的 event 类型 / 不需要 event 参数

### _property_ `matcher_type`

- **类型:** Type[Matcher] | inspect._empty | NoneType

- **说明**

:类型: ``Optional[Union[Type["Matcher"], inspect.Parameter.empty]]``

:说明: 事件处理函数是否接受 matcher 参数

### _property_ `state_type`

- **类型:** dict[Any, Any] | inspect._empty | NoneType

- **说明**

:类型: ``Optional[Union[T_State, inspect.Parameter.empty]]``

:说明: 事件处理函数是否接受 state 参数

### _instance-var_ `func`

- **类型:** 

- **说明**

:类型: ``T_Handler``

:说明: 事件处理函数

### _instance-var_ `signature`

- **类型:** 

- **说明**

:类型: ``inspect.Signature``

:说明: 事件处理函数签名

### _method_ `get_signature(self)`

- **参数**

    无

- **返回**

    - `inspect.Signature`

### _method_ `update_signature(self, **kwargs)`

- **参数**

    - `kwargs` (NoneType | Type[Bot] | Type[Event] | Type[Matcher] | dict[Any, Any] | inspect._empty)

- **返回**

    - `None`