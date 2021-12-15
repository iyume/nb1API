---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.command.argfilter.converters` 模块 <Badge text="1.2.0+"/>

提供几种常用的转换器。

## _def_ `simple_chinese_to_bool(text)` {#simple_chinese_to_bool}

- **说明**

将中文（`好`、`不行` 等）转换成布尔值。

- **参数**

    - `text` (str)

- **返回**

    - `bool | None`

## _def_ `split_nonempty_lines(text)` {#split_nonempty_lines}

- **说明**

按行切割文本，并忽略所有空行。

- **参数**

    - `text` (str)

- **返回**

    - `list[str]`

## _def_ `split_nonempty_stripped_lines(text)` {#split_nonempty_stripped_lines}

- **说明**

按行切割文本，并对每一行进行 `str.strip`，再忽略所有空行。

- **参数**

    - `text` (str)

- **返回**

    - `list[str]`