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

## _var_ `ACCESS_TOKEN`

- **类型:** str

## _var_ `API_ROOT`

- **类型:** str

## _var_ `APSCHEDULER_CONFIG`

- **类型:** dict[str, Any]

## _var_ `COMMAND_SEP`

- **类型:** Iterable[str | Pattern]

## _var_ `COMMAND_START`

- **类型:** Iterable[str | Pattern]

## _var_ `DEBUG`

- **类型:** bool

## _var_ `DEFAULT_VALIDATION_FAILURE_EXPRESSION`

- **类型:** str | Sequence[str] | (*Any, **Any) -> str

## _var_ `HOST`

- **类型:** str

## _var_ `MAX_VALIDATION_FAILURES`

- **类型:** int

## _var_ `NICKNAME`

- **类型:** str | Iterable[str]

## _var_ `PORT`

- **类型:** int

## _var_ `SECRET`

- **类型:** str

## _var_ `SESSION_CANCEL_EXPRESSION`

- **类型:** str | Sequence[str] | (*Any, **Any) -> str

## _var_ `SESSION_EXPIRE_TIMEOUT`

- **类型:** datetime.timedelta | None

## _var_ `SESSION_RUNNING_EXPRESSION`

- **类型:** str | Sequence[str] | (*Any, **Any) -> str

## _var_ `SESSION_RUN_TIMEOUT`

- **类型:** datetime.timedelta | None

## _var_ `SHORT_MESSAGE_MAX_LENGTH`

- **类型:** int

## _var_ `SUPERUSERS`

- **类型:** Collection[int]

## _var_ `TOO_MANY_VALIDATION_FAILURES_EXPRESSION`

- **类型:** str | Sequence[str] | (*Any, **Any) -> str

## _def_ `DEFAULT_COMMAND_PERMISSION(_)`

- **参数**

    - `_`

- **返回**

    unknown

## _def_ `DEFAULT_NLP_PERMISSION(_)`

- **参数**

    - `_`

- **返回**

    unknown