---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.experimental.plugin` 模块 <Badge text="1.8.0+"/>

为了保持向前的兼容，在 1.9.0 后此模块仅导出与主包完全相同的 `on_command` 和 `on_natural_language` 两个函数。会在未来版本中移除。

[aiocqhttp]: https://github.com/nonebot/aiocqhttp/

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