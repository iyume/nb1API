---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.plugin.export` 模块

## _var_ `_export`

- **类型:** 

## _def_ `export()`

- **说明**

:说明:

获取插件的导出内容对象

:返回:

  - ``Export``

- **参数**

    无

- **返回**

    - `nonebot.plugin.export.Export`

## _class_ `Export(self, /, *args, **kwargs)`

- **说明**

:说明:

插件导出内容以使得其他插件可以获得。

:示例:

.. code-block:: python

    nonebot.export().default = "bar"

    @nonebot.export()
    def some_function():
        pass

    # this doesn't work before python 3.9
    # use
    # export = nonebot.export(); @export.sub
    # instead
    # See also PEP-614: https://www.python.org/dev/peps/pep-0614/
    @nonebot.export().sub
    def something_else():
        pass

- **参数**

    - `args`

    - `kwargs`

### _class-var_ `_export`

- **类型:** 

- **说明**

:说明:

插件导出内容以使得其他插件可以获得。

:示例:

.. code-block:: python

    nonebot.export().default = "bar"

    @nonebot.export()
    def some_function():
        pass

    # this doesn't work before python 3.9
    # use
    # export = nonebot.export(); @export.sub
    # instead
    # See also PEP-614: https://www.python.org/dev/peps/pep-0614/
    @nonebot.export().sub
    def something_else():
        pass