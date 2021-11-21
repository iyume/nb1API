---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.plugin` 模块 <Badge text="1.1.0+"/>

## _def_ `get_loaded_plugins()`

- **说明**

Get all plugins loaded.

:return: a set of Plugin objects

- **参数**

    无

- **返回**

    set[nonebot.plugin.Plugin]

## _def_ `load_builtin_plugins()`

- **说明**

Load built-in plugins distributed along with "nonebot" package.

- **参数**

    无

- **返回**

    set[nonebot.plugin.Plugin]

## _def_ `load_plugin(module_path)`

- **说明**

Load a module as a plugin

- **参数**

    - `module_path` (str) <Badge text="str"/>: path of module to import

- **返回**

    Optional[Plugin]: Plugin object loaded, which can be awaited if
                  the caller wishes to wait for async loading
                  callbacks if there is any, or None loading fails

## _def_ `load_plugins(plugin_dir, module_prefix)`

- **说明**

Find all non-hidden modules or packages in a given directory,

and import them with the given module prefix.

- **参数**

    - `plugin_dir` (str) <Badge text="str"/>: Plugin directory to search

    - `module_prefix` (str) <Badge text="str"/>: Module prefix used while importing

- **返回**

    Set[Plugin]: Set of plugin objects successfully loaded

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

## _def_ `on_natural_language(keywords=None, *, permission=Ellipsis, only_to_me=True, only_short_message=True, allow_empty_message=False)` <Badge text="1.6.0+"/>

- **说明**

将函数装饰为自然语言处理器。

- **参数**

    **重载:**

    1. `(__func) -> NLPHandler_T`

        - `__func` ((NLPSession) -> Awaitable[IntentCommand | None]): 被装饰函数，必须为 async 函数

    返回:

        - `NLPHandler_T`

    2. `(keywords=..., *, permission=..., only_to_me=..., only_short_message=..., allow_empty_message=...) -> (NLPHandler_T) -> NLPHandler_T`

        - `keywords` (Iterable[str] | str | NoneType): 要响应的关键词，若传入 `None`，则响应所有消息

        - `permission` ((SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool] | Iterable[(SenderRoles) -> bool | (SenderRoles) -> Awaitable[bool]]) <Badge text="1.9.0+"/>: 自然语言处理器所需要的权限，不满足权限的用户将无法触发该处理器。 若提供了多个，则默认使用 `aggregate_policy` 和其默认参数组合。 如果不传入该参数（即为默认的 `...`），则使用配置项中的 `DEFAULT_NLP_PERMISSION`

        - `only_to_me` (bool): 是否只响应确定是在和「我」（机器人）说话的消息（在开头或结尾 @ 了机器人，或在开头称呼了机器人昵称）

        - `only_short_message` (bool): 是否只响应短消息

        - `allow_empty_message` (bool): 是否响应内容为空的消息（只有 @ 或机器人昵称）

    返回:

        - `(NLPHandler_T) -> NLPHandler_T`

## _def_ `on_notice(arg=None, *events)`

- **参数**

    - `arg` (str | ~_Teh | NoneType)

    - `events` (str)

- **返回**

    (~_Teh) -> ~_Teh | ~_Teh

## _def_ `on_plugin(timing)`

- **说明**

Decorator to register a function as a callback for plugin lifetime events.

- **参数**

    - `timing` (str) <Badge text="str"/>: Either 'loading' or 'unloaded'

- **返回**

    (() -> Any | () -> Awaitable[Any]) -> (() -> Any | () -> Awaitable[Any])

## _def_ `on_request(arg=None, *events)`

- **参数**

    - `arg` (str | ~_Teh | NoneType)

    - `events` (str)

- **返回**

    (~_Teh) -> ~_Teh | ~_Teh

## _def_ `reload_plugin(module_path)`

- **说明**

A combination of unload and load of a plugin.

- **参数**

    - `module_path` (str) <Badge text="str"/>: import path to module, which is already imported

- **返回**

    Optional[Plugin]: The return value is special, please see the doc

## _def_ `unload_plugin(module_path)`

- **说明**

Unloads a plugin.

This deletes its entry in sys.modules if present. However, if the module
had additional side effects other than defining processors, they are not
undone.

- **参数**

    - `module_path` (str) <Badge text="str"/>: import path to module, which is already imported

- **返回**

    Optional[Plugin]: Stale Plugin (which can be awaited if the caller
                  wishes to wait for async unloaded callbacks if there
                  is any) if it was unloaded, None if it were not
                  loaded

## _class_ `Plugin(module, name=None, usage=None, userdata=None, commands=Ellipsis, nl_processors=Ellipsis, event_handlers=Ellipsis, msg_preprocessors=Ellipsis, lifetime_hooks=Ellipsis)`

用于包装已加载的插件模块的类。

- **参数**

    - `module` (module)

    - `name` (str | None)

    - `usage` (Any | None)

    - `userdata` (Any | None)

    - `commands` (set[nonebot.command.Command])

    - `nl_processors` (set[nonebot.natural_language.NLProcessor])

    - `event_handlers` (set[nonebot.notice_request.EventHandler])

    - `msg_preprocessors` (set[MessagePreprocessor])

    - `lifetime_hooks` (list[nonebot.plugin.LifetimeHook])

### _instance-var_ `commands` <Badge text="1.6.0+"/>

- **类型:** set[nonebot.command.Command]

- **说明:** 插件包含的命令，通过 `on_command` 装饰器注册。

### _instance-var_ `event_handlers` <Badge text="1.6.0+"/>

- **类型:** set[nonebot.notice_request.EventHandler]

- **说明:** 插件包含的事件处理器（包含通知、请求），通过 `on_notice` 以及 `on_request` 装饰器注册。

### _instance-var_ `lifetime_hooks` <Badge text="1.9.0+"/>

- **类型:** list[nonebot.plugin.LifetimeHook]

- **说明:** 插件包含的生命周期事件回调，通过 `on_plugin` 装饰器注册。

### _instance-var_ `module`

- **类型:** module

- **说明:** 已加载的插件模块（importlib 导入的 Python 模块）。

### _instance-var_ `msg_preprocessors` <Badge text="1.9.0+"/>

- **类型:** set[MessagePreprocessor]

- **说明:** 插件包含的消息预处理器，通过 `message_preprocessor` 装饰器注册。

### _instance-var_ `name`

- **类型:** str | None

- **说明:** 插件名称，从插件模块的 `__plugin_name__` 特殊变量获得，如果没有此变量，则为 `None`。

### _instance-var_ `nl_processors` <Badge text="1.6.0+"/>

- **类型:** set[nonebot.natural_language.NLProcessor]

- **说明:** 插件包含的自然语言处理器，通过 `on_natural_language` 装饰器注册。

### _instance-var_ `usage`

- **类型:** str | None

- **说明:** 插件使用方法，从插件模块的 `__plugin_usage__` 特殊变量获得，如果没有此变量，则为 `None`。

### _instance-var_ `userdata` <Badge text="1.9.0+"/>

- **类型:** Any | None

- **说明:** 插件作者可由此变量向外部暴露其他信息，从插件模块的 `__plugin_userdata__` 特殊变量获得，如果没有此变量，则为 `None`。

## _class_ `PluginManager()`

- **参数**

    无

### _def classmethod_ `add_plugin(module_path, plugin)`

- **说明**

Register a plugin

- **参数**

    - `module_path` (str) <Badge text="str"/>: module path

    - `plugin` (nonebot.plugin.Plugin) <Badge text="Plugin"/>: Plugin object

- **返回**

    None

### _def classmethod_ `get_plugin(module_path)`

- **说明**

Get plugin object by plugin module path

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

- **返回**

    Optional[Plugin]: Plugin object

### _def classmethod_ `remove_plugin(module_path)`

- **说明**

Remove a plugin by plugin module path

** Warning: This function not remove plugin actually! **
** Just remove command, nlprocessor, event handlers **
** and message preprocessors, and deletes it from PluginManager **

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

- **返回**

    - `bool`: Success or not

### _def classmethod_ `switch_command_global(module_path, state=None)`

- **说明**

Change plugin command state globally or simply switch it if `state` is None

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

    - `state` (bool | None) <Badge text="Optional[bool]"/>: State to change to. Defaults to None.

- **返回**

    None

### _def classmethod_ `switch_eventhandler_global(module_path, state=None)`

- **说明**

Change plugin event handler state globally or simply switch it if `state` is None

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

    - `state` (bool | None) <Badge text="Optional[bool]"/>: State to change to. Defaults to None.

- **返回**

    None

### _def classmethod_ `switch_messagepreprocessor_global(module_path, state=None)`

- **说明**

Change plugin message preprocessor state globally or simply switch it if `state`

is None

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

    - `state` (bool | None) <Badge text="Optional[bool]"/>: State to change to. Defaults to None.

- **返回**

    None

### _def classmethod_ `switch_nlprocessor_global(module_path, state=None)`

- **说明**

Change plugin nlprocessor state globally or simply switch it if `state` is None

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

    - `state` (bool | None) <Badge text="Optional[bool]"/>: State to change to. Defaults to None.

- **返回**

    None

### _def classmethod_ `switch_plugin_global(module_path, state=None)`

- **说明**

Change plugin state globally or simply switch it if `state` is None

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

    - `state` (bool | None) <Badge text="Optional[bool]"/>: State to change to. Defaults to None.

- **返回**

    None

### _def_ `switch_command(self, module_path, state=None)`

- **说明**

Change plugin command state or simply switch it if `state` is None

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

    - `state` (bool | None) <Badge text="Optional[bool]"/>: State to change to. Defaults to None.

- **返回**

    None

### _def_ `switch_nlprocessor(self, module_path, state=None)`

- **说明**

Change plugin nlprocessor state or simply switch it if `state` is None

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

    - `state` (bool | None) <Badge text="Optional[bool]"/>: State to change to. Defaults to None.

- **返回**

    None

### _def_ `switch_plugin(self, module_path, state=None)`

- **说明**

Change plugin state or simply switch it if `state` is None

Tips:
    This method will only change the state of the plugin's
    commands and natural language processors since changing
    state of the event handler for message and changing other message
    preprocessors are meaningless (needs discussion).

- **参数**

    - `module_path` (str) <Badge text="str"/>: Plugin module path

    - `state` (bool | None) <Badge text="Optional[bool]"/>: State to change to. Defaults to None.

- **返回**

    None