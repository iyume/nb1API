---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.command.argfilter.extractors` 模块 <Badge text="1.2.0+"/>

提供几种常用的提取器。

## _def_ `extract_text(arg)` {#extract_text}

- **说明**

提取消息中的纯文本部分（使用空格合并纯文本消息段）。

- **参数**

    - `arg` (str | dict[str, Any] | list[dict[str, Any]])

- **返回**

    - `str`

## _def_ `extract_image_urls(arg)` {#extract_image_urls}

- **说明**

提取消息中的图片 URL 列表。

- **参数**

    - `arg` (str | dict[str, Any] | list[dict[str, Any]])

- **返回**

    - `list[str]`

## _def_ `extract_numbers(arg)` {#extract_numbers}

- **说明**

提取消息中的所有数字（浮点数）。

- **参数**

    - `arg` (str | dict[str, Any] | list[dict[str, Any]])

- **返回**

    - `list[float]`