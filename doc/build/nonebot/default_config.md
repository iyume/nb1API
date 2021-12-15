---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.default_config` 模块

Default configurations.

Any derived configurations must import everything from this module
at the very beginning of their code, and then set their own value
to override the default one.

For example:

>>> from nonebot.default_config import *
>>> PORT = 9090
>>> DEBUG = False
>>> SUPERUSERS.add(123456)
>>> NICKNAME = '小明'

## _def_ `DEFAULT_COMMAND_PERMISSION(_)` {#DEFAULT_COMMAND_PERMISSION}

- **参数**

    - `_`

- **返回**

    - `Unknown`

## _def_ `DEFAULT_NLP_PERMISSION(_)` {#DEFAULT_NLP_PERMISSION}

- **参数**

    - `_`

- **返回**

    - `Unknown`