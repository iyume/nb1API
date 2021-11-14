---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.experimental.plugin` 模块 <Badge text="1.8.0+"/>

为了保持向前的兼容，在 1.9.0 后此模块仅导出与主包完全相同的 `on_command` 和 `on_natural_language` 两个函数。会在未来版本中移除。

[aiocqhttp]: https://github.com/nonebot/aiocqhttp/

## _def_ `on_command(name, *, aliases=(), patterns=(), permission=Ellipsis, only_to_me=True, privileged=False, shell_like=False, expire_timeout=Ellipsis, run_timeout=Ellipsis, session_class=None)`

- **说明**

Decorator to register a function as a command.

:param name: command name (e.g. 'echo' or ('random', 'number'))
:param aliases: aliases of command name, for convenient access
:param patterns: custom regex pattern for the command.
       Please use this carefully. Abuse may cause performance problem.
       Also, Please notice that if a message is matched by this method,
       it will use the full command as session current_arg.
:param permission: permission required by the command
:param only_to_me: only handle messages to me
:param privileged: can be run even when there is already a session
:param shell_like: use shell-like syntax to split arguments
:param expire_timeout: will override SESSION_EXPIRE_TIMEOUT if provided
:param run_timeout: will override SESSION_RUN_TIMEOUT if provided
:param session_class: session class

- **参数**

    - `name` (str | tuple[str, ...])

    - `aliases` (Iterable[str] | str)

    - `patterns` (Iterable[str] | str | Iterable[Pattern[str]] | Pattern[str])

    - `permission` ((SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool] | Iterable[(SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool]])

    - `only_to_me` (bool)

    - `privileged` (bool)

    - `shell_like` (bool)

    - `expire_timeout` (datetime.timedelta | None)

    - `run_timeout` (datetime.timedelta | None)

    - `session_class` (Type[nonebot.command.CommandSession] | None)

- **返回**

    ((CommandSession) -> Awaitable[Any]) -> (CommandSession) -> Awaitable[Any]

## _def_ `on_natural_language(keywords=None, *, permission=Ellipsis, only_to_me=True, only_short_message=True, allow_empty_message=False)`

- **说明**

Implementation of on_natural_language overloads.

- **参数**

    - `keywords` (Iterable[str] | NoneType | str | (NLPSession) -> Awaitable[IntentCommand | None])

    - `permission` ((SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool] | Iterable[(SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool]])

    - `only_to_me` (bool)

    - `only_short_message` (bool)

    - `allow_empty_message` (bool)

- **返回**

    unknown