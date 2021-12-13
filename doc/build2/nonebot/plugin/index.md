---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.plugin` 模块

插件
====

为 NoneBot 插件开发提供便携的定义函数。

## _var_ `plugins`

- **类型:** dict[str, Plugin]

- **说明**

:类型: ``Dict[str, Plugin]``

:说明: 已加载的插件

## _var_ `_plugin_matchers`

- **类型:** dict[str, set[Type[nonebot.matcher.Matcher]]]

## _var_ `PLUGIN_NAMESPACE`

- **类型:** str

## _def_ `on(type='', rule=..., permission=..., *, handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个基础事件响应器，可自定义类型。

:参数:

  * ``type: str``: 事件响应器类型
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `type` (str)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_metaevent(rule=..., *, handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个元事件响应器。

:参数:

  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_message(rule=..., permission=..., *, handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器。

:参数:

  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_notice(rule=..., *, handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个通知事件响应器。

:参数:

  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_request(rule=..., *, handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个请求事件响应器。

:参数:

  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_startswith(msg, rule=..., ignorecase=..., *, permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息的**文本部分**以指定内容开头时响应。

:参数:

  * ``msg: Union[str, Tuple[str, ...]]``: 指定消息开头内容
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``ignorecase: bool``: 是否忽略大小写
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `msg` (str | tuple[str, ...])

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `ignorecase` (bool)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_endswith(msg, rule=..., ignorecase=..., *, permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息的**文本部分**以指定内容结尾时响应。

:参数:

  * ``msg: Union[str, Tuple[str, ...]]``: 指定消息结尾内容
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``ignorecase: bool``: 是否忽略大小写
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `msg` (str | tuple[str, ...])

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `ignorecase` (bool)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_keyword(keywords, rule=..., *, permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息纯文本部分包含关键词时响应。

:参数:

  * ``keywords: Set[str]``: 关键词列表
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `keywords` (set[str])

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_command(cmd, rule=..., aliases=..., *, permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息以指定命令开头时响应。

  命令匹配规则参考: `命令形式匹配 <rule.html#command-command>`_

:参数:

  * ``cmd: Union[str, Tuple[str, ...]]``: 指定命令内容
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``aliases: Optional[Set[Union[str, Tuple[str, ...]]]]``: 命令别名
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `cmd` (str | tuple[str, ...])

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `aliases` (set[str | tuple[str, ...]] | None)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_shell_command(cmd, rule=..., aliases=..., parser=..., *, permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个支持 ``shell_like`` 解析参数的命令消息事件响应器。

  与普通的 ``on_command`` 不同的是，在添加 ``parser`` 参数时, 响应器会自动处理消息。

  并将用户输入的原始参数列表保存在 ``state["argv"]``, ``parser`` 处理的参数保存在 ``state["args"]`` 中

:参数:

  * ``cmd: Union[str, Tuple[str, ...]]``: 指定命令内容
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``aliases: Optional[Set[Union[str, Tuple[str, ...]]]]``: 命令别名
  * ``parser: Optional[ArgumentParser]``: ``nonebot.rule.ArgumentParser`` 对象
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `cmd` (str | tuple[str, ...])

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `aliases` (set[str | tuple[str, ...]] | None)

    - `parser` (nonebot.rule.ArgumentParser | None)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `on_regex(pattern, flags=..., rule=..., *, permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息匹配正则表达式时响应。

  命令匹配规则参考: `正则匹配 <rule.html#regex-regex-flags-0>`_

:参数:

  * ``pattern: str``: 正则表达式
  * ``flags: Union[int, re.RegexFlag]``: 正则匹配标志
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `pattern` (str)

    - `flags` (int | re.RegexFlag)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _def_ `load_plugin(module_path)`

- **说明**

:说明:

使用 ``PluginManager`` 加载单个插件，可以是本地插件或是通过 ``pip`` 安装的插件。

:参数:

  * ``module_path: str``: 插件名称 ``path.to.your.plugin``

:返回:

  - ``Optional[Plugin]``

- **参数**

    - `module_path` (str)

- **返回**

    - `nonebot.plugin.Plugin | None`

## _def_ `load_plugins(*plugin_dir)`

- **说明**

:说明:

导入目录下多个插件，以 ``_`` 开头的插件不会被导入！

:参数:

  - ``*plugin_dir: str``: 插件路径

:返回:

  - ``Set[Plugin]``

- **参数**

    - `plugin_dir` (str)

- **返回**

    - `set[nonebot.plugin.Plugin]`

## _def_ `load_all_plugins(module_path, plugin_dir)`

- **说明**

:说明:

导入指定列表中的插件以及指定目录下多个插件，以 ``_`` 开头的插件不会被导入！

:参数:

  - ``module_path: Set[str]``: 指定插件集合
  - ``plugin_dir: Set[str]``: 指定插件路径集合

:返回:

  - ``Set[Plugin]``

- **参数**

    - `module_path` (set[str])

    - `plugin_dir` (set[str])

- **返回**

    - `set[nonebot.plugin.Plugin]`

## _def_ `load_from_json(file_path, encoding=...)`

- **说明**

:说明:

导入指定 json 文件中的 ``plugins`` 以及 ``plugin_dirs`` 下多个插件，以 ``_`` 开头的插件不会被导入！

:参数:

  - ``file_path: str``: 指定 json 文件路径
  - ``encoding: str``: 指定 json 文件编码

:返回:

  - ``Set[Plugin]``

- **参数**

    - `file_path` (str)

    - `encoding` (str)

- **返回**

    - `set[nonebot.plugin.Plugin]`

## _def_ `load_from_toml(file_path, encoding=...)`

- **说明**

:说明:

导入指定 toml 文件 ``[nonebot.plugins]`` 中的 ``plugins`` 以及 ``plugin_dirs`` 下多个插件，
  以 ``_`` 开头的插件不会被导入！

:参数:

  - ``file_path: str``: 指定 toml 文件路径
  - ``encoding: str``: 指定 toml 文件编码

:返回:

  - ``Set[Plugin]``

- **参数**

    - `file_path` (str)

    - `encoding` (str)

- **返回**

    - `set[nonebot.plugin.Plugin]`

## _def_ `load_builtin_plugins(name=...)`

- **说明**

:说明:

导入 NoneBot 内置插件

:返回:

  - ``Plugin``

- **参数**

    - `name` (str)

- **返回**

    - `nonebot.plugin.Plugin | None`

## _def_ `get_plugin(name)`

- **说明**

:说明:

获取当前导入的某个插件。

:参数:

  * ``name: str``: 插件名，与 ``load_plugin`` 参数一致。如果为 ``load_plugins`` 导入的插件，则为文件(夹)名。

:返回:

  - ``Optional[Plugin]``

- **参数**

    - `name` (str)

- **返回**

    - `nonebot.plugin.Plugin | None`

## _def_ `get_loaded_plugins()`

- **说明**

:说明:

获取当前已导入的所有插件。

:返回:

  - ``Set[Plugin]``

- **参数**

    无

- **返回**

    - `set[nonebot.plugin.Plugin]`

## _def_ `require(name)`

- **说明**

:说明:

获取一个插件的导出内容

:参数:

  * ``name: str``: 插件名，与 ``load_plugin`` 参数一致。如果为 ``load_plugins`` 导入的插件，则为文件(夹)名。

:返回:

  - ``Optional[Export]``

- **参数**

    - `name` (str)

- **返回**

    - `nonebot.plugin.export.Export | None`

## _class_ `Plugin(self, name, module)`

- **说明**

Plugin(name: str, module: module)

- **参数**

    - `name` (str)

    - `module` (module)

### _property_ `export`

- **类型:** nonebot.plugin.export.Export

### _property_ `matcher`

- **类型:** set[Type[nonebot.matcher.Matcher]]

### _class-var_ `_plugin_matchers`

- **类型:** 

- **说明:** 存储插件信息

### _instance-var_ `name`

- **类型:** str

- **说明**

- **类型**: ``str``

- **说明**: 插件名称，使用 文件/文件夹 名称作为插件名

### _instance-var_ `module`

- **类型:** module

- **说明**

- **类型**: ``ModuleType``

- **说明**: 插件模块对象

## _class_ `CommandGroup(self, cmd, *, rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **参数**

    - `cmd` (str | tuple[str, ...])

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

### _instance-var_ `basecmd`

- **类型:** 

- **说明**

- **类型**: ``Tuple[str, ...]``

- **说明**: 命令前缀

### _instance-var_ `base_kwargs`

- **类型:** 

- **说明**

- **类型**: ``Dict[str, Any]``

- **说明**: 其他传递给 ``on_command`` 的参数默认值

### _method_ `command(self, cmd, *, aliases, rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个新的命令。

:参数:

  * ``cmd: Union[str, Tuple[str, ...]]``: 命令前缀
  * ``**kwargs``: 其他传递给 ``on_command`` 的参数，将会覆盖命令组默认值

:返回:

  - ``Type[Matcher]``

- **参数**

    - `cmd` (str | tuple[str, ...])

    - `aliases` (set[str | tuple[str, ...]] | None)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `shell_command(self, cmd, *, rule=..., aliases, parser=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个新的命令。

:参数:

  * ``cmd: Union[str, Tuple[str, ...]]``: 命令前缀
  * ``**kwargs``: 其他传递给 ``on_shell_command`` 的参数，将会覆盖命令组默认值

:返回:

  - ``Type[Matcher]``

- **参数**

    - `cmd` (str | tuple[str, ...])

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `aliases` (set[str | tuple[str, ...]] | None)

    - `parser` (nonebot.rule.ArgumentParser | None)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

## _class_ `MatcherGroup(self, *, type=..., rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **参数**

    - `type` (str)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

### _instance-var_ `matchers`

- **类型:** 

- **说明**

:类型: ``List[Type[Matcher]]``

:说明: 组内事件响应器列表

### _instance-var_ `base_kwargs`

- **类型:** 

- **说明**

- **类型**: ``Dict[str, Any]``

- **说明**: 其他传递给 ``on`` 的参数默认值

### _method_ `on(self, *, type=..., rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个基础事件响应器，可自定义类型。

:参数:

  * ``type: str``: 事件响应器类型
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `type` (str)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_command(self, cmd, aliases=..., *, rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息以指定命令开头时响应。

  命令匹配规则参考: `命令形式匹配 <rule.html#command-command>`_

:参数:

  * ``cmd: Union[str, Tuple[str, ...]]``: 指定命令内容
  * ``aliases: Optional[Set[Union[str, Tuple[str, ...]]]]``: 命令别名
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `cmd` (str | tuple[str, ...])

    - `aliases` (set[str | tuple[str, ...]] | None)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_endswith(self, msg, *, ignorecase=..., rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息的**文本部分**以指定内容结尾时响应。

:参数:

  * ``msg: Union[str, Tuple[str, ...]]``: 指定消息结尾内容
  * ``ignorecase: bool``: 是否忽略大小写
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `msg` (str | tuple[str, ...])

    - `ignorecase` (bool)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_keyword(self, keywords, *, rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息纯文本部分包含关键词时响应。

:参数:

  * ``keywords: Set[str]``: 关键词列表
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `keywords` (set[str])

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_message(self, *, rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器。

:参数:

  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_metaevent(self, *, rule=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个元事件响应器。

:参数:

  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_notice(self, *, rule=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个通知事件响应器。

:参数:

  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_regex(self, pattern, flags=..., *, rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息匹配正则表达式时响应。

  命令匹配规则参考: `正则匹配 <rule.html#regex-regex-flags-0>`_

:参数:

  * ``pattern: str``: 正则表达式
  * ``flags: Union[int, re.RegexFlag]``: 正则匹配标志
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `pattern` (str)

    - `flags` (int | re.RegexFlag)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_request(self, *, rule=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个请求事件响应器。

:参数:

  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_shell_command(self, cmd, aliases=..., parser=..., *, rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个支持 ``shell_like`` 解析参数的命令消息事件响应器。

  与普通的 ``on_command`` 不同的是，在添加 ``parser`` 参数时, 响应器会自动处理消息。

  并将用户输入的原始参数列表保存在 ``state["argv"]``, ``parser`` 处理的参数保存在 ``state["args"]`` 中

:参数:

  * ``cmd: Union[str, Tuple[str, ...]]``: 指定命令内容
  * ``aliases: Optional[Set[Union[str, Tuple[str, ...]]]]``: 命令别名
  * ``parser: Optional[ArgumentParser]``: ``nonebot.rule.ArgumentParser`` 对象
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `cmd` (str | tuple[str, ...])

    - `aliases` (set[str | tuple[str, ...]] | None)

    - `parser` (nonebot.rule.ArgumentParser | None)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`

### _method_ `on_startswith(self, msg, *, ignorecase=..., rule=..., permission=..., handlers=..., temp=..., priority=..., block=..., state=..., state_factory=...)`

- **说明**

:说明:

注册一个消息事件响应器，并且当消息的**文本部分**以指定内容开头时响应。

:参数:

  * ``msg: Union[str, Tuple[str, ...]]``: 指定消息开头内容
  * ``ignorecase: bool``: 是否忽略大小写
  * ``rule: Optional[Union[Rule, T_RuleChecker]]``: 事件响应规则
  * ``permission: Optional[Permission]``: 事件响应权限
  * ``handlers: Optional[List[Union[T_Handler, Handler]]]``: 事件处理函数列表
  * ``temp: bool``: 是否为临时事件响应器（仅执行一次）
  * ``priority: int``: 事件响应器优先级
  * ``block: bool``: 是否阻止事件向更低优先级传递
  * ``state: Optional[T_State]``: 默认 state
  * ``state_factory: Optional[T_StateFactory]``: 默认 state 的工厂函数

:返回:

  - ``Type[Matcher]``

- **参数**

    - `msg` (str | tuple[str, ...])

    - `ignorecase` (bool)

    - `rule` (nonebot.rule.Rule | (Bot, Event, dict[Any, Any]) -> (bool | Awaitable[bool]) | NoneType)

    - `permission` (nonebot.permission.Permission | None)

    - `handlers` (list[(Any, Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any, Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | (Any) -> (Awaitable[NoneType] | Awaitable[NoReturn]) | nonebot.handler.Handler] | None)

    - `temp` (bool)

    - `priority` (int)

    - `block` (bool)

    - `state` (dict[Any, Any] | None)

    - `state_factory` ((Bot, Event) -> Awaitable[dict[Any, Any]] | None)

- **返回**

    - `Type[nonebot.matcher.Matcher]`