---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.log` 模块

日志
====

NoneBot 使用 `loguru`_ 来记录日志信息。

自定义 logger 请参考 `loguru`_ 文档。

.. _loguru:
    https://github.com/Delgan/loguru

## _var_ `logger`

- **类型:** 

- **说明**

:说明:

NoneBot 日志记录器对象。

:默认信息:

  * 格式: ``[%(asctime)s %(name)s] %(levelname)s: %(message)s``
  * 等级: ``DEBUG`` / ``INFO`` ，根据 config 配置改变
  * 输出: 输出至 stdout

:用法:

.. code-block:: python

    from nonebot.log import logger

## _var_ `default_filter`

- **类型:** 

## _class_ `Filter(self)`

## _class_ `LoguruHandler(self, level=0)`

- **说明**

Handler instances dispatch logging events to specific destinations.

The base handler class. Acts as a placeholder which defines the Handler
interface. Handlers can optionally use Formatter instances to format
records as desired. By default, no formatter is specified; in this case,
the 'raw' message as determined by record.message is logged.

- **参数**

    - `level`

### _method_ `emit(self, record)`

- **说明**

Do whatever it takes to actually log the specified logging record.

This version is intended to be implemented by subclasses and so
raises a NotImplementedError.

- **参数**

    - `record`

- **返回**

    - `Unknown`