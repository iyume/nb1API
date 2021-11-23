---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot` 模块

## 子模块

* [nonebot.argparse](argparse/)

* [nonebot.command](command/)

* [nonebot.default_config](default_config/)

* [nonebot.exceptions](exceptions/)

* [nonebot.experimental](experimental/)

* [nonebot.helpers](helpers/)

* [nonebot.log](log/)

* [nonebot.message](message/)

* [nonebot.natural_language](natural_language/)

* [nonebot.notice_request](notice_request/)

* [nonebot.permission](permission/)

* [nonebot.plugin](plugin/)

* [nonebot.sched](sched/)

* [nonebot.session](session/)

* [nonebot.typing](typing/)

## _var_ `_bot`

- **类型:** nonebot.NoneBot | None

## _var_ `scheduler`

- **类型:** 

## _def_ `context_id(event, *, mode='default', use_hash=False)`

- **说明**

获取事件对应的上下文的唯一 ID。

- **参数**

    - `event` (aiocqhttp.event.Event): 事件对象

    - `mode` (str): ID 的计算模式 - `'default'`: 默认模式，任何一个上下文都有其唯一 ID - `'group'`: 群组模式，同一个群组或讨论组的上下文（即使是不同用户）具有相同 ID - `'user'`: 用户模式，同一个用户的上下文（即使在不同群组）具有相同 ID

    - `use_hash` (bool): 是否将计算出的 ID 使用 MD5 进行哈希

- **返回**

    - `str`: 事件对应的上下文的唯一 ID

- **用法**

```python
ctx_id = context_id(session.event, use_hash=True)
```

获取当前 Session 的事件对应的上下文的唯一 ID，并进行 MD5 哈希，得到的结果可用于图灵机器人等 API 的调用。

## _def_ `get_bot()`

- **说明**

Get the NoneBot instance.

The result is ensured to be not None, otherwise an exception will
be raised.

:raise ValueError: instance not initialized

- **参数**

    无

- **返回**

    nonebot.NoneBot

## _def_ `get_loaded_plugins()`

- **说明**

获取已经加载的插件集合。

- **参数**

    无

- **返回**

    Set[Plugin]: 加载成功的 Plugin 对象

- **用法**

```python
plugins = nonebot.plugin.get_loaded_plugins()
await session.send('我现在支持以下功能：\n\n' +
                    '\n'.join(map(lambda p: p.name, filter(lambda p: p.name, plugins))))
```

## _def_ `init(config_object=None, start_scheduler=True)`

- **说明**

Initialize NoneBot instance.

This function must be called at the very beginning of code,
otherwise the get_bot() function will return None and nothing
will work properly.

:param config_object: configuration object

- **参数**

    - `config_object` (Any | None)

    - `start_scheduler` (bool)

- **返回**

    None

## _def_ `load_builtin_plugins()`

- **说明**

加载内置插件。

- **参数**

    无

- **返回**

    Set[Plugin]: 加载成功的 Plugin 对象

- **用法**

```python
nonebot.plugin.load_builtin_plugins()
```

## _def_ `load_plugin(module_path)`

- **说明**

加载插件（等价于导入模块）。

此函数会调用插件中由 `on_plugin('loading')` 装饰器注册的函数（下称 「加载回调」），之后再添加插件中注册的处理器（如命令等）。

- **参数**

    - `module_path` (str): 模块路径

- **返回**

    Optional[Plugin]: 加载后生成的 `Plugin` 对象。根据插件组成不同，返回值包含如下情况：
        - 插件没有定义加载回调，或只定义了同步的加载回调（此为 1.9.0 前的唯一情况）：此函数会执行回调，在加载完毕后返回新的插件对象，其可以被 await，行为为直接返回插件本身。如果发生异常，则返回 `None`
        - 插件定义了异步加载回调，但 `load_plugin` 是在 NoneBot 启动前调用的：此函数会阻塞地运行异步函数，其余表现和上一致
        - 插件定义了异步加载回调，但 `load_plugin` 是在异步的情况下调用的（比如在 NoneBot 运行的事件循环中）：此函数会先执行部分同步的加载回调
            - 如果成功，返回一个插件对象。返回值可以被 await，行为为等待剩余的异步加载完毕然后返回插件本身，或如果在 await 中发生了错误，返回 `None`
            - 如果失败，返回 `None`

- **用法**

```python
nonebot.plugin.load_plugin('ai_chat')
```

加载 `ai_chat` 插件。

```python
# 此写法是通用的，即使插件没有异步的加载回调
p = nonebot.plugin.load_plugin('my_own_plugin')
if p is not None and await p is not None:
    # 插件成功加载完成
else:
    # 插件加载失败
```
加载 `my_own_plugin` 插件，并且等待其异步的加载回调（如果有）执行完成。

## _def_ `load_plugins(plugin_dir, module_prefix)`

- **说明**

查找指定路径（相对或绝对）中的非隐藏模块（隐藏模块名字以 `_` 开头）并通过指定的模块前缀导入。其返回值的表现与 `load_plugin` 一致。

- **参数**

    - `plugin_dir` (str): 插件目录

    - `module_prefix` (str): 模块前缀

- **返回**

    Set[Plugin]: 加载成功的 Plugin 对象

- **用法**

```python
nonebot.plugin.load_plugins(path.join(path.dirname(__file__), 'plugins'), 'plugins')
```

加载 `plugins` 目录下的插件。

## _def_ `message_preprocessor(func)`

- **说明**

将函数装饰为消息预处理器。

- **要求** <Badge text="1.6.0+"/>

被装饰函数必须是一个 async 函数，且必须接收且仅接收三个位置参数，类型分别为 `NoneBot` 、 `aiocqhttp.Event` 和 `nonebot.plugin.PluginManager`，即形如：

```python
async def func(bot: NoneBot, event: aiocqhttp.Event, plugin_manager: PluginManager):
    pass
```

- **参数**

    - `func` ((NoneBot, CQEvent, PluginManager) -> Awaitable[Any])

- **返回**

    (nonebot.NoneBot, aiocqhttp.event.Event, nonebot.plugin.PluginManager) -> Awaitable[Any]

- **用法**

```python
@message_preprocessor
async def _(bot: NoneBot, event: aiocqhttp.Event, plugin_manager: PluginManager):
    event["preprocessed"] = True

    # 关闭某个插件，仅对当前消息生效
    plugin_manager.switch_plugin("path.to.plugin", state=False)
```

在所有消息处理之前，向消息事件对象中加入 `preprocessed` 字段。

## _def_ `on_command(name, *, aliases=(), patterns=(), permission=Ellipsis, only_to_me=True, privileged=False, shell_like=False, expire_timeout=Ellipsis, run_timeout=Ellipsis, session_class=None)` <Badge text="1.6.0+"/>

- **说明**

将函数装饰为命令处理器 `CommandHandler_T` 。

被装饰的函数将会获得一个 `args_parser` 属性，是一个装饰器，下面会有详细说明。

- **要求**

被装饰函数必须是一个 async 函数，且必须接收且仅接收一个位置参数，类型为 `CommandSession`，即形如：

```python
async def func(session: CommandSession):
    pass
```

- **参数**

    - `name` (str | tuple[str, ...]): 命令名，如果传入的是字符串则会自动转为元组

    - `aliases` (Iterable[str] | str): 命令别名

    - `patterns` (Iterable[str] | str | Iterable[Pattern[str]] | Pattern[str]) <Badge text="1.7.0+"/>: 正则匹配，可以传入正则表达式或正则表达式组，来对整条命令进行匹配 **注意:** 滥用正则表达式可能会引发性能问题，请优先使用普通命令。 另外一点需要注意的是，由正则表达式匹配到的匹配到的命令，`session` 中的 `current_arg` 会是整个命令，而不会删除匹配到的内容，以满足一些特殊需求。

    - `permission` ((SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool] | Iterable[(SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool]]) <Badge text="1.9.0+"/>: 命令所需要的权限，不满足权限的用户将无法触发该命令。 若提供了多个，则默认使用 `aggregate_policy` 和其默认参数组合。 如果不传入该参数（即为默认的 `...`），则使用配置项中的 `DEFAULT_COMMAND_PERMISSION`

    - `only_to_me` (bool): 是否只响应确定是在和「我」（机器人）说话的命令（在开头或结尾 @ 了机器人，或在开头称呼了机器人昵称）

    - `privileged` (bool): 是否特权命令，若是，则无论当前是否有命令会话正在运行，都会运行该命令，但运行不会覆盖已有会话，也不会保留新创建的会话

    - `shell_like` (bool): 是否使用类 shell 语法，若是，则会自动使用 `shlex` 模块进行分割（无需手动编写参数解析器），分割后的参数列表放入 `session.args['argv']`

    - `expire_timeout` (datetime.timedelta | None) <Badge text="1.8.2+"/>: 命令过期时间。如果不传入该参数（即为默认的 `...`），则使用配置项中的 `SESSION_EXPIRE_TIMEOUT`，如果提供则使用提供的值。

    - `run_timeout` (datetime.timedelta | None) <Badge text="1.8.2+"/>: 命令会话的运行超时时长。如果不传入该参数（即为默认的 `...`），则使用配置项中的 `SESSION_RUN_TIMEOUT`，如果提供则使用提供的值。

    - `session_class` (Type[nonebot.command.CommandSession] | None) <Badge text="1.7.0+"/>: 自定义 `CommandSession` 子类，若传入此参数，则命令处理函数的参数 `session` 类型为 `session_class`

- **返回**

    ((CommandSession) -> Awaitable[Any]) -> (CommandSession) -> Awaitable[Any]

- **用法**

```python
@on_command('echo', aliases=('复读',), permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    await session.send(session.current_arg)
```

一个仅对超级用户生效的复读命令。

## _def_ `on_natural_language(keywords=None, *, permission=Ellipsis, only_to_me=True, only_short_message=True, allow_empty_message=False)` <Badge text="1.6.0+"/>

- **说明**

将函数装饰为自然语言处理器。

- **参数**

    - `keywords` (Iterable[str] | NoneType | str | (NLPSession) -> Awaitable[IntentCommand | None])

    - `permission` ((SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool] | Iterable[(SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool]])

    - `only_to_me` (bool)

    - `only_short_message` (bool)

    - `allow_empty_message` (bool)

- **返回**

    Unknown

## _def_ `on_notice(arg=None, *events)` <Badge text="1.6.0+"/>

- **说明**

将函数装饰为通知处理器。

- **要求**

被装饰函数必须是一个 async 函数，且必须接收且仅接收一个位置参数，类型为 `NoticeSession`，即形如：

```python
async def func(session: NoticeSession):
    pass
```

- **参数**

    - `arg` (str | ~_Teh | NoneType)

    - `events` (str): 要处理的通知类型（`notice_type`），若不传入，则处理所有通知

- **返回**

    (~_Teh) -> ~_Teh | ~_Teh

- **用法**

```python
@on_notice
async def _(session: NoticeSession):
    logger.info('有新的通知事件：%s', session.event)

@on_notice('group_increase')
async def _(session: NoticeSession):
    await session.send('欢迎新朋友～')
```

收到所有通知时打日志，收到新成员进群通知时除了打日志还发送欢迎信息。

## _def_ `on_request(arg=None, *events)` <Badge text="1.6.0+"/>

- **说明**

将函数装饰为请求处理器。

- **要求**

被装饰函数必须是一个 async 函数，且必须接收且仅接收一个位置参数，类型为 `RequestSession`，即形如：

```python
async def func(session: RequestSession):
    pass
```

- **参数**

    - `arg` (str | ~_Teh | NoneType)

    - `events` (str): 要处理的请求类型（`request_type`），若不传入，则处理所有请求

- **返回**

    (~_Teh) -> ~_Teh | ~_Teh

- **用法**

```python
@on_request
async def _(session: RequestSession):
    logger.info('有新的请求事件：%s', session.event)

@on_request('group')
async def _(session: RequestSession):
    await session.approve()
```

收到所有请求时打日志，收到群请求时除了打日志还同意请求。

## _def_ `on_startup(func)`

- **说明**

Decorator to register a function as startup callback.

- **参数**

    - `func` (() -> Awaitable[NoneType])

- **返回**

    () -> Awaitable[NoneType]

## _def_ `on_websocket_connect(func)`

- **说明**

Decorator to register a function as websocket connect callback.

Only work with CQHTTP v4.14+.

- **参数**

    - `func` ((aiocqhttp.event.Event) -> Awaitable[NoneType])

- **返回**

    () -> Awaitable[NoneType]

## _def_ `run(host=None, port=None, *args, **kwargs)`

- **说明**

Run the NoneBot instance.

- **参数**

    - `host` (str | None)

    - `port` (int | None)

    - `args`

    - `kwargs`

- **返回**

    None

## _class_ `CommandGroup(name, **kwargs)`

Group a set of commands with same name prefix.

- **参数**

    - `name` (str | tuple[str, ...])

    - `kwargs`

### _instance-var_ `base_kwargs`

- **类型:** 

### _instance-var_ `basename`

- **类型:** 

### _def_ `command(self, name, **kwargs)`

- **说明**

Decorator to register a function as a command. Its has the same usage as

`on_command`.

:param kwargs: keyword arguments will be passed to `on_command`. For each
               argument in the signature of this method here, if it is not
               present when calling, default value for the command group is
               used (e.g. `self.permission`). If that value is also not set,
               default value for `on_command` is used.

- **参数**

    - `name` (str | tuple[str, ...])

    - `kwargs`

- **返回**

    ((CommandSession) -> Awaitable[Any]) -> (CommandSession) -> Awaitable[Any]

## _class_ `CommandSession(bot, event, cmd, *, current_arg='', args=None)`

基础 session 类，`CommandSession` 等均继承自此类。

### 基类

* nonebot.session.BaseSession

- **参数**

    - `bot` (nonebot.NoneBot)

    - `event` (aiocqhttp.event.Event)

    - `cmd` (nonebot.command.Command)

    - `current_arg` (str | None)

    - `args` (dict[str, Any] | None)

### _property_ `argv`

- **类型:** list[str]

- **说明:** 命令参数列表，类似于 `sys.argv`，本质上是 `session.state.get('argv', [])`，**需要搭配 `on_command(..., shell_like=True)` 使用**。

- **用法**

```python
@on_command('some_cmd', shell_like=True)
async def _(session: CommandSession):
    argv = session.argv
```

### _instance-var_ `bot`

- **类型:** nonebot.NoneBot

- **说明:** Session 对应的 NoneBot 对象。

- **用法**

```python
await session.bot.send('hello')
```

在当前 Session 对应的上下文中发送 `hello`。

### _instance-var_ `cmd`

- **类型:** 

### _property_ `ctx` <Badge text="1.5.0-" type="error"/>

- **类型:** aiocqhttp.event.Event

- **说明:** CQHTTP 上报的事件数据对象，或称事件上下文，具体请参考 [事件上报](https://cqhttp.cc/docs/#/Post)。

- **用法**

```python
user_id = session.ctx['user_id']
```

获取当前事件的 `user_id` 字段。

### _instance-var_ `current_arg`

- **类型:** str | None

- **说明:** 命令会话当前参数。实际上是 酷 Q 收到的消息去掉命令名的剩下部分，因此可能存在 CQ 码。

### _instance-var_ `current_arg_filters`

- **类型:** list[(Any) -> (Any | Awaitable[Any])] | None

### _property_ `current_arg_images`

- **类型:** list[str]

- **说明:** `current_arg` 属性中所有图片的 URL 的列表，如果参数中没有图片，则为 `[]`。

### _property_ `current_arg_text`

- **类型:** str

- **说明:** `current_arg` 属性的纯文本部分（不包含 CQ 码），各部分使用空格连接。

### _instance-var_ `current_key`

- **类型:** str | None

- **说明:** 命令会话当前正在询问用户的参数的键（或称参数的名字）。第一次运行会话时，该属性为 `None`。

### _instance-var_ `event` <Badge text="1.5.0+"/>

- **类型:** aiocqhttp.event.Event

- **说明:** CQHTTP 上报的事件数据对象，具体请参考 [`aiocqhttp.Event`](https://aiocqhttp.nonebot.dev/module/aiocqhttp/index.html#aiocqhttp.Event) 和 [事件上报](https://cqhttp.cc/docs/#/Post)。

- **用法**

```python
user_id = session.event['user_id']
group_id = session.event.group_id
```

获取当前事件的 `user_id` 和 `group_id` 字段。

### _property_ `expire_timeout`

- **类型:** datetime.timedelta | None

- **说明:** INTERNAL API

### _property_ `is_first_run`

- **类型:** bool

- **说明:** 命令会话是否第一次运行。

### _property_ `is_valid`

- **类型:** bool

- **说明**

INTERNAL API

Check whether the session has expired or not.

### _property_ `run_timeout`

- **类型:** datetime.timedelta | None

- **说明:** INTERNAL API

### _property_ `running`

- **类型:** bool

- **说明:** INTERNAL API

### _property_ `self_id` <Badge text="1.1.0+"/>

- **类型:** int

- **说明**

当前 session 对应的 QQ 机器人账号，在多个机器人账号使用同一个 NoneBot 后端时可用于区分当前收到消息或事件的是哪一个机器人。

等价于 `session.event.self_id`。

- **用法**

```python
await bot.send_private_msg(self_id=session.self_id, user_id=12345678, message='Hello')
```

### _property_ `state` <Badge text="1.2.0+"/>

- **类型:** dict[str, Any]

- **说明**

命令会话的状态数据（包括已获得的所有参数）。

属性本身只读，但属性中的内容可读写。

- **用法**

```python
if not session.state.get('initialized'):
    # ... 初始化工作
    session.state['initialized'] = True
```
在命令处理函数的开头进行**每次命令调用只应该执行一次的初始化操作**。

### _property_ `waiting`

- **类型:** bool

- **说明:** INTERNAL API

### _async def_ `aget(self, key=Ellipsis, *, prompt=None, arg_filters=None, force_update=Ellipsis, **kwargs)` <Badge text="1.8.0+"/>

- **说明**

从 `state` 属性获取参数，如果参数不存在，则异步地暂停当前会话，向用户发送提示，并等待用户的进一步交互。

当用户再次输入时，不会重新运行命令处理器，而是回到此函数调用之处继续执行。

注意，一旦传入 `arg_filters` 参数（参数过滤器），则等用户再次输入时，_command_func._`args_parser` 所注册的参数解析函数将不会被运行，而会在对 `current_arg` 依次运行过滤器之后直接将其放入 `state` 属性中。

- **参数**

    - `key` (str): 参数的键，若不传入则使用默认键值

    - `prompt` (str | dict[str, Any] | list[dict[str, Any]] | NoneType): 提示的消息内容

    - `arg_filters` (list[(Any) -> (Any | Awaitable[Any])] | None): 用于处理和验证用户输入的参数的过滤器

    - `force_update` (bool): 是否强制获取用户新的输入，若是，则会忽略已有的当前参数，若 `key` 不传入则为真，否则默认为假

    - `kwargs`: 其它传入 `BaseSession.send()` 的命名参数

- **返回**

    Any

- **用法**

```python
from nonebot.command.argfilter import extractors, validators

note = await session.aget(
    'note', prompt='你需要我提醒你什么呢',
    arg_filters=[
        extractors.extract_text,  # 取纯文本部分
        controllers.handle_cancellation(session),  # 处理用户可能的取消指令
        str.strip  # 去掉两边空白字符
    ]
)

time = await session.aget(
    'time', prompt='你需要我在什么时间提醒你呢？',
    arg_filters=[
        extractors.extract_text,  # 取纯文本部分
        controllers.handle_cancellation(session),  # 处理用户可能的取消指令
        str.strip,  # 去掉两边空白字符
        # 正则匹配输入格式
        validators.match_regex(r'^\d{4}-\d{2}-\d{2}$', '格式不对啦，请重新输入')
    ]
)
```

连续获取多个参数，如果当前还不知道，则询问用户，等待用户输入之后，会依次运行 `arg_filters` 参数中的过滤器，以确保参数内容和格式符合要求。

### _async def_ `apause(self, message=None, **kwargs)` <Badge text="1.8.0+"/>

- **说明**

异步地暂停当前命令会话，并发送消息。

当用户再次输入时，不会重新运行命令处理器，而是回到此函数调用之处继续执行。

- **参数**

    - `message` (str | dict[str, Any] | list[dict[str, Any]] | NoneType): 要发送的消息，若不传入则不发送

    - `kwargs`: 其它传入 `BaseSession.send()` 的命名参数

- **返回**

    None

- **用法**

```python
while True:
    await session.apause('请继续发送要处理的图片，发送 done 结束')
    if session.current_arg_text.strip() == 'done':
        session.finish('处理完成')
    process_images(session.current_arg_images)
```

需要连续接收用户输入，并且过程中不需要改变 `current_key` 时，使用此函数暂停会话。

### _def_ `finish(self, message=None, **kwargs)`

- **说明**

结束当前命令会话，并发送消息。此函数调用之后的语句将不会被执行（除非捕获了此函数抛出的特殊异常）。

调用此函数后，命令将被视为已经完成，当前命令会话将被移除。

- **参数**

    - `message` (str | dict[str, Any] | list[dict[str, Any]] | NoneType): 要发送的消息，若不传入则不发送

    - `kwargs`: 其它传入 `BaseSession.send()` 的命名参数

- **返回**

    NoReturn

- **用法**

```python
session.finish('感谢您的使用～')
```

### _def_ `get(self, key, *, prompt=None, arg_filters=None, **kwargs)`

- **说明**

从 `state` 属性获取参数，如果参数不存在，则暂停当前会话，向用户发送提示，并等待用户的新一轮交互。

如果需要暂停当前会话，则命令处理器中，此函数调用之后的语句将不会被执行（除非捕获了此函数抛出的特殊异常）。

注意，一旦传入 `arg_filters` 参数（参数过滤器），则等用户再次输入时，_command_func._`args_parser` 所注册的参数解析函数将不会被运行，而会在对 `current_arg` 依次运行过滤器之后直接将其放入 `state` 属性中。

- **参数**

    - `key` (str): 参数的键

    - `prompt` (str | dict[str, Any] | list[dict[str, Any]] | NoneType): 提示的消息内容

    - `arg_filters` (list[(Any) -> (Any | Awaitable[Any])] | None): 用于处理和验证用户输入的参数的过滤器

    - `kwargs`: 其它传入 `BaseSession.send()` 的命名参数

- **返回**

    Any

- **用法**

```python
location = session.get('location', prompt='请输入要查询的地区')
```

获取位置信息，如果当前还不知道，则询问用户。

```python
from nonebot.command.argfilter import extractors, validators

time = session.get(
    'time', prompt='你需要我在什么时间提醒你呢？',
    arg_filters=[
        extractors.extract_text,  # 取纯文本部分
        controllers.handle_cancellation(session),  # 处理用户可能的取消指令
        str.strip,  # 去掉两边空白字符
        # 正则匹配输入格式
        validators.match_regex(r'^\d{4}-\d{2}-\d{2}$', '格式不对啦，请重新输入')
    ]
)
```

获取时间信息，如果当前还不知道，则询问用户，等待用户输入之后，会依次运行 `arg_filters` 参数中的过滤器，以确保参数内容和格式符合要求。

### _def_ `pause(self, message=None, **kwargs)`

- **说明**

暂停当前命令会话，并发送消息。此函数调用之后的语句将不会被执行（除非捕获了此函数抛出的特殊异常）。

- **参数**

    - `message` (str | dict[str, Any] | list[dict[str, Any]] | NoneType): 要发送的消息，若不传入则不发送

    - `kwargs`: 其它传入 `BaseSession.send()` 的命名参数

- **返回**

    NoReturn

- **用法**

```python
session.pause('请继续发送要处理的图片，发送 done 结束')
```

需要连续接收用户输入，并且过程中不需要改变 `current_key` 时，使用此函数暂停会话。

### _def_ `refresh(self, event, *, current_arg='')`

- **说明**

INTERNAL API

Refill the session with a new message event.

:param event: new message event
:param current_arg: new command argument as a string

- **参数**

    - `event` (aiocqhttp.event.Event)

    - `current_arg` (str | None)

- **返回**

    None

### _async def_ `send(self, message, *, at_sender=False, ensure_private=False, ignore_failure=True, **kwargs)`

- **说明**

发送消息到 Session 对应的上下文中。

- **参数**

    - `message` (str | dict[str, Any] | list[dict[str, Any]]): 要发送的消息内容

    - `at_sender` (bool): 是否 @ 发送者，对私聊不起作用

    - `ensure_private` (bool): 确保消息发送到私聊，对于群组和讨论组消息上下文，会私聊发送者

    - `ignore_failure` (bool): 发送失败时忽略 `CQHttpError` 异常

    - `kwargs`: 其它传入 `CQHttp.send()` 的命名参数

- **返回**

    - `Any` <Badge text="1.1.0+"/>: 返回 CQHTTP 插件发送消息接口的调用返回值，具体见 aiocqhttp 的 [API 调用](https://aiocqhttp.nonebot.dev/#/what-happened#api-%E8%B0%83%E7%94%A8)

- **异常**

    - `CQHttpError`: 发送失败时抛出，实际由 [aiocqhttp] 抛出，等价于 `aiocqhttp.Error`

- **用法**

```python
await session.send('hello')
```

在当前 Session 对应的上下文中发送 `hello`。

### _def_ `switch(self, new_message)`

- **说明**

结束当前会话，改变当前消息事件中的消息内容，然后重新处理消息事件。

此函数可用于从一个命令中跳出，将用户输入的剩余部分作为新的消息来处理，例如可实现以下对话：

```
用户：帮我查下天气
Bot：你要查询哪里的天气呢？
用户：算了，帮我查下今天下午南京到上海的火车票吧
Bot：今天下午南京到上海的火车票有如下班次：blahblahblah
```

这里进行到第三行时，命令期待的是一个地点，但实际发现消息的开头是「算了」，于是调用 `switch('帮我查下今天下午南京到上海的火车票吧')`，结束天气命令，将剩下来的内容作为新的消息来处理（触发火车票插件的自然语言处理器，进而调用火车票查询命令）。

- **参数**

    - `new_message` (str | dict[str, Any] | list[dict[str, Any]]): 要覆盖消息事件的新消息内容

- **返回**

    NoReturn

- **用法**

```python
@my_cmd.args_parser
async def _(session: CommandSession)
    if not session.is_first_run and session.current_arg.startswith('算了，'):
        session.switch(session.current_arg[len('算了，'):])
```

使用「算了」来取消当前命令，转而进入新的消息处理流程。这个例子比较简单，实际应用中可以使用更复杂的 NLP 技术来判断。

## _class_ `IntentCommand(confidence, name, args=None, current_arg='')` <Badge text="1.2.0+"/>

用于表示自然语言处理之后得到的意图命令，是一个 namedtuple，由自然语言处理器返回。

### 基类

* builtins.tuple

- **参数**

    - `args`

    - `kwargs`

### _instance-var_ `args`

- **类型:** dict[str, Any] | None

- **说明:** 命令的（初始）参数。

### _instance-var_ `confidence`

- **类型:** float

- **说明:** 意图的置信度，即表示对当前推测的用户意图有多大把握。

### _instance-var_ `current_arg`

- **类型:** str

- **说明:** 命令的当前输入参数。

### _instance-var_ `name`

- **类型:** str | tuple[str, ...]

- **说明:** 命令的名字。

## _class_ `NLPSession(bot, event, msg)`

继承自 `BaseSession` 类，表示自然语言处理 Session。

### 基类

* nonebot.session.BaseSession

- **参数**

    - `bot` (nonebot.NoneBot)

    - `event` (aiocqhttp.event.Event)

    - `msg` (str)

### _instance-var_ `bot`

- **类型:** nonebot.NoneBot

- **说明:** Session 对应的 NoneBot 对象。

- **用法**

```python
await session.bot.send('hello')
```

在当前 Session 对应的上下文中发送 `hello`。

### _property_ `ctx` <Badge text="1.5.0-" type="error"/>

- **类型:** aiocqhttp.event.Event

- **说明:** CQHTTP 上报的事件数据对象，或称事件上下文，具体请参考 [事件上报](https://cqhttp.cc/docs/#/Post)。

- **用法**

```python
user_id = session.ctx['user_id']
```

获取当前事件的 `user_id` 字段。

### _instance-var_ `event` <Badge text="1.5.0+"/>

- **类型:** aiocqhttp.event.Event

- **说明:** CQHTTP 上报的事件数据对象，具体请参考 [`aiocqhttp.Event`](https://aiocqhttp.nonebot.dev/module/aiocqhttp/index.html#aiocqhttp.Event) 和 [事件上报](https://cqhttp.cc/docs/#/Post)。

- **用法**

```python
user_id = session.event['user_id']
group_id = session.event.group_id
```

获取当前事件的 `user_id` 和 `group_id` 字段。

### _instance-var_ `msg`

- **类型:** str

- **说明:** 以字符串形式表示的消息内容，已去除开头的 @ 和机器人称呼，可能存在 CQ 码。

### _instance-var_ `msg_images`

- **类型:** list[str]

- **说明:** 消息内容中所有图片的 URL 的列表，如果消息中没有图片，则为 `[]`。

### _instance-var_ `msg_text`

- **类型:** str

- **说明:** 消息内容的纯文本部分，已去除所有 CQ 码／非 `text` 类型的消息段。各纯文本消息段之间使用空格连接。

### _property_ `self_id` <Badge text="1.1.0+"/>

- **类型:** int

- **说明**

当前 session 对应的 QQ 机器人账号，在多个机器人账号使用同一个 NoneBot 后端时可用于区分当前收到消息或事件的是哪一个机器人。

等价于 `session.event.self_id`。

- **用法**

```python
await bot.send_private_msg(self_id=session.self_id, user_id=12345678, message='Hello')
```

### _async def_ `send(self, message, *, at_sender=False, ensure_private=False, ignore_failure=True, **kwargs)`

- **说明**

发送消息到 Session 对应的上下文中。

- **参数**

    - `message` (str | dict[str, Any] | list[dict[str, Any]]): 要发送的消息内容

    - `at_sender` (bool): 是否 @ 发送者，对私聊不起作用

    - `ensure_private` (bool): 确保消息发送到私聊，对于群组和讨论组消息上下文，会私聊发送者

    - `ignore_failure` (bool): 发送失败时忽略 `CQHttpError` 异常

    - `kwargs`: 其它传入 `CQHttp.send()` 的命名参数

- **返回**

    - `Any` <Badge text="1.1.0+"/>: 返回 CQHTTP 插件发送消息接口的调用返回值，具体见 aiocqhttp 的 [API 调用](https://aiocqhttp.nonebot.dev/#/what-happened#api-%E8%B0%83%E7%94%A8)

- **异常**

    - `CQHttpError`: 发送失败时抛出，实际由 [aiocqhttp] 抛出，等价于 `aiocqhttp.Error`

- **用法**

```python
await session.send('hello')
```

在当前 Session 对应的上下文中发送 `hello`。

## _class_ `NoneBot(config_object=None)`

OneBot (CQHTTP) 机器人的主类，负责控制整个机器人的运行、事件处理函数的注册、OneBot

API 的调用等。

内部维护了一个 `Quart` 对象作为 web 服务器，提供 HTTP 协议的 ``/`` 和 WebSocket
协议的 ``/ws/``、``/ws/api/``、``/ws/event/`` 端点供 OneBot 连接。

由于基类 `api.AsyncApi` 继承了 `api.Api` 的 `__getattr__`
魔术方法，因此可以在 bot 对象上直接调用 OneBot API，例如：

```py
await bot.send_private_msg(user_id=10001000, message='你好')
friends = await bot.get_friend_list()
```

也可以通过 `CQHttp.call_action` 方法调用 API，例如：

```py
await bot.call_action('set_group_whole_ban', group_id=10010)
```

两种调用 API 的方法最终都通过 `CQHttp.api` 属性来向 OneBot
发送请求并获取调用结果。

### 基类

* aiocqhttp.CQHttp

* aiocqhttp.api.AsyncApi

* aiocqhttp.api.Api

- **参数**

    - `config_object` (Any | None)

### _def_ `run(self, host=None, port=None, *args, **kwargs)`

- **说明**

运行 bot 对象，实际就是运行 Quart app，参数与 `Quart.run` 一致。

- **参数**

    - `host` (str | None)

    - `port` (int | None)

    - `args`

    - `kwargs`

- **返回**

    None

## _class_ `NoticeSession(bot, event)`

继承自 `BaseSession` 类，表示通知类事件的 Session。

### 基类

* nonebot.session.BaseSession

- **参数**

    - `bot` (nonebot.NoneBot)

    - `event` (aiocqhttp.event.Event)

### _instance-var_ `bot`

- **类型:** nonebot.NoneBot

- **说明:** Session 对应的 NoneBot 对象。

- **用法**

```python
await session.bot.send('hello')
```

在当前 Session 对应的上下文中发送 `hello`。

### _property_ `ctx` <Badge text="1.5.0-" type="error"/>

- **类型:** aiocqhttp.event.Event

- **说明:** CQHTTP 上报的事件数据对象，或称事件上下文，具体请参考 [事件上报](https://cqhttp.cc/docs/#/Post)。

- **用法**

```python
user_id = session.ctx['user_id']
```

获取当前事件的 `user_id` 字段。

### _instance-var_ `event` <Badge text="1.5.0+"/>

- **类型:** aiocqhttp.event.Event

- **说明:** CQHTTP 上报的事件数据对象，具体请参考 [`aiocqhttp.Event`](https://aiocqhttp.nonebot.dev/module/aiocqhttp/index.html#aiocqhttp.Event) 和 [事件上报](https://cqhttp.cc/docs/#/Post)。

- **用法**

```python
user_id = session.event['user_id']
group_id = session.event.group_id
```

获取当前事件的 `user_id` 和 `group_id` 字段。

### _property_ `self_id` <Badge text="1.1.0+"/>

- **类型:** int

- **说明**

当前 session 对应的 QQ 机器人账号，在多个机器人账号使用同一个 NoneBot 后端时可用于区分当前收到消息或事件的是哪一个机器人。

等价于 `session.event.self_id`。

- **用法**

```python
await bot.send_private_msg(self_id=session.self_id, user_id=12345678, message='Hello')
```

### _async def_ `send(self, message, *, at_sender=False, ensure_private=False, ignore_failure=True, **kwargs)`

- **说明**

发送消息到 Session 对应的上下文中。

- **参数**

    - `message` (str | dict[str, Any] | list[dict[str, Any]]): 要发送的消息内容

    - `at_sender` (bool): 是否 @ 发送者，对私聊不起作用

    - `ensure_private` (bool): 确保消息发送到私聊，对于群组和讨论组消息上下文，会私聊发送者

    - `ignore_failure` (bool): 发送失败时忽略 `CQHttpError` 异常

    - `kwargs`: 其它传入 `CQHttp.send()` 的命名参数

- **返回**

    - `Any` <Badge text="1.1.0+"/>: 返回 CQHTTP 插件发送消息接口的调用返回值，具体见 aiocqhttp 的 [API 调用](https://aiocqhttp.nonebot.dev/#/what-happened#api-%E8%B0%83%E7%94%A8)

- **异常**

    - `CQHttpError`: 发送失败时抛出，实际由 [aiocqhttp] 抛出，等价于 `aiocqhttp.Error`

- **用法**

```python
await session.send('hello')
```

在当前 Session 对应的上下文中发送 `hello`。

## _class_ `RequestSession(bot, event)`

继承自 `BaseSession` 类，表示请求类事件的 Session。

### 基类

* nonebot.session.BaseSession

- **参数**

    - `bot` (nonebot.NoneBot)

    - `event` (aiocqhttp.event.Event)

### _instance-var_ `bot`

- **类型:** nonebot.NoneBot

- **说明:** Session 对应的 NoneBot 对象。

- **用法**

```python
await session.bot.send('hello')
```

在当前 Session 对应的上下文中发送 `hello`。

### _property_ `ctx` <Badge text="1.5.0-" type="error"/>

- **类型:** aiocqhttp.event.Event

- **说明:** CQHTTP 上报的事件数据对象，或称事件上下文，具体请参考 [事件上报](https://cqhttp.cc/docs/#/Post)。

- **用法**

```python
user_id = session.ctx['user_id']
```

获取当前事件的 `user_id` 字段。

### _instance-var_ `event` <Badge text="1.5.0+"/>

- **类型:** aiocqhttp.event.Event

- **说明:** CQHTTP 上报的事件数据对象，具体请参考 [`aiocqhttp.Event`](https://aiocqhttp.nonebot.dev/module/aiocqhttp/index.html#aiocqhttp.Event) 和 [事件上报](https://cqhttp.cc/docs/#/Post)。

- **用法**

```python
user_id = session.event['user_id']
group_id = session.event.group_id
```

获取当前事件的 `user_id` 和 `group_id` 字段。

### _property_ `self_id` <Badge text="1.1.0+"/>

- **类型:** int

- **说明**

当前 session 对应的 QQ 机器人账号，在多个机器人账号使用同一个 NoneBot 后端时可用于区分当前收到消息或事件的是哪一个机器人。

等价于 `session.event.self_id`。

- **用法**

```python
await bot.send_private_msg(self_id=session.self_id, user_id=12345678, message='Hello')
```

### _async def_ `approve(self, remark='')`

- **说明**

同意当前请求。

- **参数**

    - `remark` (str): 好友备注，只在好友请求时有效

- **返回**

    None

- **异常**

    - `CQHttpError`: 发送失败时抛出，实际由 [aiocqhttp] 抛出，等价于 `aiocqhttp.Error`

- **用法**

```python
await session.approve()
```

### _async def_ `reject(self, reason='')`

- **说明**

拒绝当前请求。

- **参数**

    - `reason` (str): 拒绝理由，只在群请求时有效

- **返回**

    None

- **异常**

    - `CQHttpError`: 发送失败时抛出，实际由 [aiocqhttp] 抛出，等价于 `aiocqhttp.Error`

- **用法**

```python
await session.reject()
```

### _async def_ `send(self, message, *, at_sender=False, ensure_private=False, ignore_failure=True, **kwargs)`

- **说明**

发送消息到 Session 对应的上下文中。

- **参数**

    - `message` (str | dict[str, Any] | list[dict[str, Any]]): 要发送的消息内容

    - `at_sender` (bool): 是否 @ 发送者，对私聊不起作用

    - `ensure_private` (bool): 确保消息发送到私聊，对于群组和讨论组消息上下文，会私聊发送者

    - `ignore_failure` (bool): 发送失败时忽略 `CQHttpError` 异常

    - `kwargs`: 其它传入 `CQHttp.send()` 的命名参数

- **返回**

    - `Any` <Badge text="1.1.0+"/>: 返回 CQHTTP 插件发送消息接口的调用返回值，具体见 aiocqhttp 的 [API 调用](https://aiocqhttp.nonebot.dev/#/what-happened#api-%E8%B0%83%E7%94%A8)

- **异常**

    - `CQHttpError`: 发送失败时抛出，实际由 [aiocqhttp] 抛出，等价于 `aiocqhttp.Error`

- **用法**

```python
await session.send('hello')
```

在当前 Session 对应的上下文中发送 `hello`。

## _class_ `SenderRoles(bot, event, sender)` <Badge text="1.9.0+"/>

封装了原生的 `CQEvent` 便于权限检查。此类的实例一般会传入 `PermissionPolicy_T` 作为参数。

### 基类

* builtins.tuple

- **参数**

    - `args`

    - `kwargs`

### _instance-var_ `bot`

- **类型:** nonebot.NoneBot

### _instance-var_ `event`

- **类型:** aiocqhttp.event.Event

### _property_ `is_admin`

- **类型:** bool

- **说明:** 发送者是群管理员。

### _property_ `is_anonymous`

- **类型:** bool

- **说明:** 消息是匿名消息。

### _property_ `is_discusschat`

- **类型:** bool

- **说明:** 消息是讨论组消息。

### _property_ `is_groupchat`

- **类型:** bool

- **说明:** 消息是群聊消息。

### _property_ `is_owner`

- **类型:** bool

- **说明:** 发送者是群主。

### _property_ `is_private_discuss`

- **类型:** bool

- **说明:** 消息是讨论组私聊消息。

### _property_ `is_private_friend`

- **类型:** bool

- **说明:** 消息是好友私聊消息。

### _property_ `is_private_group`

- **类型:** bool

- **说明:** 消息是群私聊消息。

### _property_ `is_privatechat`

- **类型:** bool

- **说明:** 消息是私聊消息。

### _property_ `is_superuser`

- **类型:** bool

- **说明:** 发送者是配置文件中设置的超级用户。

### _instance-var_ `sender`

- **类型:** dict[str, Any] | None

- **说明:** 只有消息是群消息的时候才会有这个属性，其内容是 `/get_group_member_info` API 调用的返回值。

### _async def staticmethod_ `create(bot, event)`

- **说明**

构造 `SenderRoles`。

- **参数**

    - `bot` (nonebot.NoneBot): 接收事件的 NoneBot 对象

    - `event` (aiocqhttp.event.Event): 上报事件

- **返回**

    nonebot.permission.SenderRoles

- **用法**

```python
sender = await SenderRoles.create(session.bot, session.event)
if sender.is_groupchat:
    if sender.is_owner:
        await process_owner(session)
    elif sender.is_admin:
        await process_admin(session)
    else:
        await process_member(session)
```

根据发送者的身份决定相应命令处理方式。

### _def_ `from_group(self, group_id)`

- **说明**

表示发送者是否来自于群 `group_id`。

- **参数**

    - `group_id` (int | Container[int]): 群号码，可以为多个群号。

- **返回**

    bool

### _def_ `sent_by(self, sender_id)`

- **说明**

表示发送者 QQ 号是否是 `sender_id`。

- **参数**

    - `sender_id` (int | Container[int]): 表示发送者 QQ 号是否是 `sender_id`。

- **返回**

    bool

### _library-attr_ `CQHttpError`

三方库 API

### _library-attr_ `Message`

三方库 API

### _library-attr_ `MessageSegment`

三方库 API