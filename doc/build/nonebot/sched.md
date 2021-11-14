---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.sched` 模块

## _class_ `Scheduler(gconfig={}, **options)`

继承自 `apscheduler.schedulers.asyncio.AsyncIOScheduler` 类，功能不变。

当 Python 环境中没有安装 APScheduler 包时，此类不存在，`Scheduler` 为 `None`。

### 基类

* apscheduler.schedulers.asyncio.AsyncIOScheduler

* apscheduler.schedulers.base.BaseScheduler

- **参数**

    - `gconfig`

    - `options`