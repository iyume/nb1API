---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.plugin.manager` 模块

## _var_ `_current_plugin`

- **类型:** 

## _var_ `_manager_stack`

- **类型:** 

## _class_ `PluginManager(self, namespace, plugins=None, search_path=None, *, id=None)`

- **参数**

    - `namespace` (str)

    - `plugins` (Iterable[str] | None)

    - `search_path` (Iterable[str] | None)

    - `id` (str | None)

### _method_ `list_plugins(self)`

- **参数**

    无

- **返回**

    - `set[str]`

### _method_ `load_all_plugins(self)`

- **参数**

    无

- **返回**

    - `list[module]`

### _method_ `load_plugin(self, name)`

- **参数**

    - `name`

- **返回**

    - `module`

### _method_ `search_plugins(self)`

- **参数**

    无

- **返回**

    - `list[str]`

## _class_ `PluginFinder(self, /, *args, **kwargs)`

- **说明**

Abstract base class for import finders on sys.meta_path.

- **参数**

    - `args`

    - `kwargs`

### _method_ `find_spec(self, fullname, path, target)`

- **参数**

    - `fullname` (str)

    - `path`

    - `target`

- **返回**

    - `Unknown`

## _class_ `PluginLoader(self, manager, fullname, path)`

- **说明**

Concrete implementation of SourceLoader using the file system.

- **参数**

    - `manager` (nonebot.plugin.manager.PluginManager)

    - `fullname` (str)

    - `path`

### _method_ `create_module(self, spec)`

- **说明**

Use default semantics for module creation.

- **参数**

    - `spec`

- **返回**

    - `module | None`

### _method_ `exec_module(self, module)`

- **说明**

Execute the module.

- **参数**

    - `module` (module)

- **返回**

    - `None`