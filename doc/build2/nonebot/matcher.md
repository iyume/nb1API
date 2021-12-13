---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.matcher` 模块

事件响应器
==========

该模块实现事件响应器的创建与运行，并提供一些快捷方法来帮助用户更好的与机器人进行对话 。

## _var_ `matchers`

- **类型:** 

- **说明**

:类型: ``Dict[int, List[Type[Matcher]]]``

:说明: 用于存储当前所有的事件响应器

## _var_ `current_bot`

- **类型:** 

## _var_ `current_event`

- **类型:** 

## _var_ `current_state`

- **类型:** 

## _class_ `MatcherMeta(self, /, *args, **kwargs)`

- **说明**

type(object_or_name, bases, dict)

type(object) -> the object's type
type(name, bases, dict) -> a new type

- **参数**

    - `args`

    - `kwargs`

## _class_ `Matcher(self)`

- **说明**

事件响应器类

### _instance-var_ `block`

- **类型:** bool

- **说明**

:类型: ``bool``

:说明: 事件响应器是否阻止事件传播

### _instance-var_ `expire_time`

- **类型:** datetime.datetime | None

- **说明**

:类型: ``Optional[datetime]``

:说明: 事件响应器过期时间点

### _instance-var_ `handlers`

- **类型:** list[nonebot.handler.Handler]

- **说明**

:类型: ``List[Handler]``

:说明: 事件响应器拥有的事件处理函数列表

### _instance-var_ `module`

- **类型:** module | None

- **说明**

:类型: ``Optional[ModuleType]``

:说明: 事件响应器所在模块

### _instance-var_ `module_name`

- **类型:** str | None

- **说明**

:类型: ``Optional[str]``

:说明: 事件响应器所在模块名

### _instance-var_ `module_prefix`

- **类型:** str | None

- **说明**

:类型: ``Optional[str]``

:说明: 事件响应器所在模块前缀

### _instance-var_ `permission`

- **类型:** nonebot.permission.Permission

- **说明**

:类型: ``Permission``

:说明: 事件响应器触发权限

### _instance-var_ `plugin_name`

- **类型:** str | None

- **说明**

:类型: ``Optional[str]``

:说明: 事件响应器所在插件名

### _instance-var_ `priority`

- **类型:** int

- **说明**

:类型: ``int``

:说明: 事件响应器优先级

### _instance-var_ `rule`

- **类型:** nonebot.rule.Rule

- **说明**

:类型: ``Rule``

:说明: 事件响应器匹配规则

### _instance-var_ `temp`

- **类型:** bool

- **说明**

:类型: ``bool``

:说明: 事件响应器是否为临时

### _instance-var_ `type`

- **类型:** str

- **说明**

:类型: ``str``

:说明: 事件响应器类型

### _instance-var_ `_default_state`

- **类型:** dict[Any, Any]

- **说明**

:类型: ``T_State``

:说明: 事件响应器默认状态

### _instance-var_ `_default_state_factory`

- **类型:** (Bot, Event) -> Awaitable[dict[Any, Any]] | None

- **说明**

:类型: ``Optional[T_State]``

:说明: 事件响应器默认工厂函数

### _instance-var_ `_default_parser`

- **类型:** (Bot, Event, dict[Any, Any]) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | None

- **说明**

:类型: ``Optional[T_ArgsParser]``

:说明: 事件响应器默认参数解析函数

### _instance-var_ `_default_type_updater`

- **类型:** (Bot, Event, dict[Any, Any], str) -> Awaitable[str] | None

- **说明**

:类型: ``Optional[T_TypeUpdater]``

:说明: 事件响应器类型更新函数

### _instance-var_ `_default_permission_updater`

- **类型:** (Bot, Event, dict[Any, Any], Permission) -> Awaitable[Permission] | None

- **说明**

:类型: ``Optional[T_PermissionUpdater]``

:说明: 事件响应器权限更新函数

### _classmethod_ `append_handler(cls, handler)`

- **参数**

    - `cls`

    - `handler` ((Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]))

- **返回**

    - `nonebot.handler.Handler`

### _classmethod_ `args_parser(cls, func)`

- **说明**

:说明:

装饰一个函数来更改当前事件响应器的默认参数解析函数

:参数:

  * ``func: T_ArgsParser``: 参数解析函数

- **参数**

    - `cls`

    - `func` ((Bot, Event, dict[Any, Any]) -> (Awaitable[NoneType] | Awaitable[NoReturn]))

- **返回**

    - `(Bot, Event, dict[Any, Any]) -> (Awaitable[NoneType] | Awaitable[NoReturn])`

### _async classmethod_ `check_perm(cls, bot, event)`

- **说明**

:说明:

检查是否满足触发权限

:参数:

  * ``bot: Bot``: Bot 对象
  * ``event: Event``: 上报事件

:返回:

  - ``bool``: 是否满足权限

- **参数**

    - `cls`

    - `bot` (Bot)

    - `event` (Event)

- **返回**

    - `bool`

### _async classmethod_ `check_rule(cls, bot, event, state)`

- **说明**

:说明:

检查是否满足匹配规则

:参数:

  * ``bot: Bot``: Bot 对象
  * ``event: Event``: 上报事件
  * ``state: T_State``: 当前状态

:返回:

  - ``bool``: 是否满足匹配规则

- **参数**

    - `cls`

    - `bot` (Bot)

    - `event` (Event)

    - `state` (dict[Any, Any])

- **返回**

    - `bool`

### _async classmethod_ `finish(cls, message=None, **kwargs)`

- **说明**

:说明:

发送一条消息给当前交互用户并结束当前事件响应器

:参数:

  * ``message: Union[str, Message, MessageSegment]``: 消息内容
  * ``**kwargs``: 其他传递给 ``bot.send`` 的参数，请参考对应 adapter 的 bot 对象 api

- **参数**

    - `cls`

    - `message` (str | Message | MessageSegment | nonebot.adapters._template.MessageTemplate | NoneType)

    - `kwargs`

- **返回**

    - `NoReturn`

### _classmethod_ `got(cls, key, prompt=None, args_parser=None)`

- **说明**

:说明:

装饰一个函数来指示 NoneBot 当要获取的 ``key`` 不存在时接收用户新的一条消息并经过 ``ArgsParser`` 处理后再运行该函数，如果 ``key`` 已存在则直接继续运行

:参数:

  * ``key: str``: 参数名
  * ``prompt: Optional[Union[str, Message, MessageSegment, MessageFormatter]]``: 在参数不存在时向用户发送的消息
  * ``args_parser: Optional[T_ArgsParser]``: 可选参数解析函数，空则使用默认解析函数

- **参数**

    - `cls`

    - `key` (str)

    - `prompt` (str | Message | MessageSegment | nonebot.adapters._template.MessageTemplate | NoneType)

    - `args_parser` ((Bot, Event, dict[Any, Any]) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | None)

- **返回**

    - `((Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn])) -> ((Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]))`

### _classmethod_ `handle(cls)`

- **说明**

:说明:

装饰一个函数来向事件响应器直接添加一个处理函数

:参数:

  * 无

- **参数**

    - `cls`

- **返回**

    - `((Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn])) -> ((Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]))`

### _classmethod_ `new(cls, type_='', rule=None, permission=None, handlers=None, temp=False, priority=1, block=False, *, module=None, expire_time=None, default_state=None, default_state_factory=None, default_parser=None, default_type_updater=None, default_permission_updater=None)`

- **说明**

:说明:

创建一个新的事件响应器，并存储至 `matchers <#matchers>`_

:参数:

  * ``type_: str``: 事件响应器类型，与 ``event.get_type()`` 一致时触发，空字符串表示任意
  * ``rule: Optional[Rule]``: 匹配规则
  * ``permission: Optional[Permission]``: 权限
  * ``handlers: Optional[List[T_Handler]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器，即触发一次后删除
  * ``priority: int``: 响应优先级
  * ``block: bool``: 是否阻止事件向更低优先级的响应器传播
  * ``module: Optional[str]``: 事件响应器所在模块名称
  * ``default_state: Optional[T_State]``: 默认状态 ``state``
  * ``default_state_factory: Optional[T_StateFactory]``: 默认状态 ``state`` 的工厂函数
  * ``expire_time: Optional[datetime]``: 事件响应器最终有效时间点，过时即被删除

:返回:

  - ``Type[Matcher]``: 新的事件响应器类

- **参数**

    - `cls`

    - `type_` (str)

    - `rule` (nonebot.rule.Rule | None)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn])] | list[nonebot.handler.Handler] | list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | NoneType)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `module` (module | None)

    - `expire_time` (datetime.datetime | None)

    - `default_state` (dict[Any, Any] | None)

    - `default_state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

    - `default_parser` ((Bot, Event, dict[Any, Any]) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | None)

    - `default_type_updater` ((Bot, Event, dict[Any, Any], str) -> Awaitable[str] | None)

    - `default_permission_updater` ((Bot, Event, dict[Any, Any], Permission) -> Awaitable[Permission] | None)

- **返回**

    - `Type[Matcher]`

### _async classmethod_ `pause(cls, prompt=None, **kwargs)`

- **说明**

:说明:

发送一条消息给当前交互用户并暂停事件响应器，在接收用户新的一条消息后继续下一个处理函数

:参数:

  * ``prompt: Union[str, Message, MessageSegment]``: 消息内容
  * ``**kwargs``: 其他传递给 ``bot.send`` 的参数，请参考对应 adapter 的 bot 对象 api

- **参数**

    - `cls`

    - `prompt` (str | Message | MessageSegment | nonebot.adapters._template.MessageTemplate | NoneType)

    - `kwargs`

- **返回**

    - `NoReturn`

### _classmethod_ `permission_updater(cls, func)`

- **说明**

:说明:

装饰一个函数来更改当前事件响应器的默认会话权限更新函数

:参数:

  * ``func: T_PermissionUpdater``: 会话权限更新函数

- **参数**

    - `cls`

    - `func` ((Bot, Event, dict[Any, Any], Permission) -> Awaitable[Permission])

- **返回**

    - `(Bot, Event, dict[Any, Any], Permission) -> Awaitable[Permission]`

### _classmethod_ `receive(cls)`

- **说明**

:说明:

装饰一个函数来指示 NoneBot 在接收用户新的一条消息后继续运行该函数

:参数:

  * 无

- **参数**

    - `cls`

- **返回**

    - `((Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn])) -> ((Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]))`

### _async classmethod_ `reject(cls, prompt=None, **kwargs)`

- **说明**

:说明:

发送一条消息给当前交互用户并暂停事件响应器，在接收用户新的一条消息后重新运行当前处理函数

:参数:

  * ``prompt: Union[str, Message, MessageSegment]``: 消息内容
  * ``**kwargs``: 其他传递给 ``bot.send`` 的参数，请参考对应 adapter 的 bot 对象 api

- **参数**

    - `cls`

    - `prompt` (str | Message | MessageSegment | NoneType)

    - `kwargs`

- **返回**

    - `NoReturn`

### _async method_ `run(self, bot, event, state)`

- **参数**

    - `bot` (Bot)

    - `event` (Event)

    - `state` (dict[Any, Any])

- **返回**

    - `Unknown`

### _async classmethod_ `send(cls, message, **kwargs)`

- **说明**

:说明:

发送一条消息给当前交互用户

:参数:

  * ``message: Union[str, Message, MessageSegment]``: 消息内容
  * ``**kwargs``: 其他传递给 ``bot.send`` 的参数，请参考对应 adapter 的 bot 对象 api

- **参数**

    - `cls`

    - `message` (str | Message | MessageSegment | nonebot.adapters._template.MessageTemplate)

    - `kwargs`

- **返回**

    - `Any`

### _method_ `stop_propagation(self)`

- **说明**

:说明:

阻止事件传播

- **参数**

    无

- **返回**

    - `Unknown`

### _classmethod_ `type_updater(cls, func)`

- **说明**

:说明:

装饰一个函数来更改当前事件响应器的默认响应事件类型更新函数

:参数:

  * ``func: T_TypeUpdater``: 响应事件类型更新函数

- **参数**

    - `cls`

    - `func` ((Bot, Event, dict[Any, Any], str) -> Awaitable[str])

- **返回**

    - `(Bot, Event, dict[Any, Any], str) -> Awaitable[str]`