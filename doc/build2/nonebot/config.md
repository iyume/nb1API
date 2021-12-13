---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.config` 模块

配置
====

NoneBot 使用 `pydantic`_ 以及 `python-dotenv`_ 来读取配置。

配置项需符合特殊格式或 json 序列化格式。详情见 `pydantic Field Type`_ 文档。

.. _pydantic:
    https://pydantic-docs.helpmanual.io/
.. _python-dotenv:
    https://saurabh-kumar.com/python-dotenv/
.. _pydantic Field Type:
    https://pydantic-docs.helpmanual.io/usage/types/

## _class_ `CustomEnvSettings(self, env_file, env_file_encoding)`

- **参数**

    - `env_file` (pathlib.Path | str | NoneType)

    - `env_file_encoding` (str | None)

## _class_ `BaseConfig(__pydantic_self__, _env_file='<object object>', _env_file_encoding=None, _secrets_dir=None, **values)`

- **说明**

Base class for settings, allowing values to be overridden by environment variables.

This is useful in production for secrets you do not wish to save in code, it plays nicely with docker(-compose),
Heroku and any 12 factor app design.

- **参数**

    - `__pydantic_self__`

    - `_env_file` (pathlib.Path | str | NoneType)

    - `_env_file_encoding` (str | None)

    - `_secrets_dir` (pathlib.Path | str | NoneType)

    - `values` (Any)

## _class_ `Env(__pydantic_self__, _env_file='<object object>', _env_file_encoding=None, _secrets_dir=None, **values)`

- **说明**

运行环境配置。大小写不敏感。

将会从 ``nonebot.init 参数`` > ``环境变量`` > ``.env 环境配置文件`` 的优先级读取配置。

- **参数**

    - `__pydantic_self__`

    - `_env_file` (pathlib.Path | str | NoneType)

    - `_env_file_encoding` (str | None)

    - `_secrets_dir` (pathlib.Path | str | NoneType)

    - `values` (Any)

### _class-var_ `environment`

- **类型:** str

- **说明**

- **类型**: ``str``

- **默认值**: ``"prod"``

:说明:
  当前环境名。 NoneBot 将从 ``.env.{environment}`` 文件中加载配置。

## _class_ `Config(__pydantic_self__, _env_file='<object object>', _env_file_encoding=None, _secrets_dir=None, **values)`

- **说明**

NoneBot 主要配置。大小写不敏感。

除了 NoneBot 的配置项外，还可以自行添加配置项到 ``.env.{environment}`` 文件中。
这些配置将会在 json 反序列化后一起带入 ``Config`` 类中。

- **参数**

    - `__pydantic_self__`

    - `_env_file` (pathlib.Path | str | NoneType)

    - `_env_file_encoding` (str | None)

    - `_secrets_dir` (pathlib.Path | str | NoneType)

    - `values` (Any)

### _class-var_ `driver`

- **类型:** str

- **说明**

- **类型**: ``str``

- **默认值**: ``"nonebot.drivers.fastapi"``

:说明:

  NoneBot 运行所使用的 ``Driver`` 。继承自 ``nonebot.driver.BaseDriver`` 。

  配置格式为 ``<module>[:<class>]``，默认类名为 ``Driver``。

### _class-var_ `host`

- **类型:** pydantic.networks.IPvAnyAddress

- **说明**

- **类型**: ``IPvAnyAddress``

- **默认值**: ``127.0.0.1``

:说明:

  NoneBot 的 HTTP 和 WebSocket 服务端监听的 IP/主机名。

### _class-var_ `port`

- **类型:** int

- **说明**

- **类型**: ``int``

- **默认值**: ``8080``

:说明:

  NoneBot 的 HTTP 和 WebSocket 服务端监听的端口。

### _class-var_ `debug`

- **类型:** bool

- **说明**

- **类型**: ``bool``

- **默认值**: ``False``

:说明:

  是否以调试模式运行 NoneBot。

### _class-var_ `log_level`

- **类型:** int | str | NoneType

- **说明**

- **类型**: ``Union[int, str]``

- **默认值**: ``None``

:说明:

  配置 NoneBot 日志输出等级，可以为 ``int`` 类型等级或等级名称，参考 `loguru 日志等级`_。

:示例:

.. code-block:: default

    LOG_LEVEL=25
    LOG_LEVEL=INFO

.. _loguru 日志等级:
    https://loguru.readthedocs.io/en/stable/api/logger.html#levels

### _class-var_ `api_root`

- **类型:** dict[str, str]

- **说明**

- **类型**: ``Dict[str, str]``

- **默认值**: ``{}``

:说明:

  以机器人 ID 为键，上报地址为值的字典，环境变量或文件中应使用 json 序列化。

:示例:

.. code-block:: default

    API_ROOT={"123456": "http://127.0.0.1:5700"}

### _class-var_ `api_timeout`

- **类型:** float | None

- **说明**

- **类型**: ``Optional[float]``

- **默认值**: ``30.``

:说明:

  API 请求超时时间，单位: 秒。

### _class-var_ `access_token`

- **类型:** str | None

- **说明**

- **类型**: ``Optional[str]``

- **默认值**: ``None``

:说明:

  API 请求以及上报所需密钥，在请求头中携带。

:示例:

.. code-block:: http

    POST /cqhttp/ HTTP/1.1
    Authorization: Bearer kSLuTF2GC2Q4q4ugm3

### _class-var_ `secret`

- **类型:** str | None

- **说明**

- **类型**: ``Optional[str]``

- **默认值**: ``None``

:说明:

  HTTP POST 形式上报所需签名，在请求头中携带。

:示例:

.. code-block:: http

    POST /cqhttp/ HTTP/1.1
    X-Signature: sha1=f9ddd4863ace61e64f462d41ca311e3d2c1176e2

### _class-var_ `superusers`

- **类型:** set[str]

- **说明**

- **类型**: ``Set[str]``

- **默认值**: ``set()``

:说明:

  机器人超级用户。

:示例:

.. code-block:: default

    SUPERUSERS=["12345789"]

### _class-var_ `nickname`

- **类型:** set[str]

- **说明**

- **类型**: ``Set[str]``

- **默认值**: ``set()``

:说明:

  机器人昵称。

### _class-var_ `command_start`

- **类型:** set[str]

- **说明**

- **类型**: ``Set[str]``

- **默认值**: ``{"/"}``

:说明:

  命令的起始标记，用于判断一条消息是不是命令。

### _class-var_ `command_sep`

- **类型:** set[str]

- **说明**

- **类型**: ``Set[str]``

- **默认值**: ``{"."}``

:说明:

  命令的分隔标记，用于将文本形式的命令切分为元组（实际的命令名）。

### _class-var_ `session_expire_timeout`

- **类型:** datetime.timedelta

- **说明**

- **类型**: ``timedelta``

- **默认值**: ``timedelta(minutes=2)``

:说明:

  等待用户回复的超时时间。

:示例:

.. code-block:: default

    SESSION_EXPIRE_TIMEOUT=120  # 单位: 秒
    SESSION_EXPIRE_TIMEOUT=[DD ][HH:MM]SS[.ffffff]
    SESSION_EXPIRE_TIMEOUT=P[DD]DT[HH]H[MM]M[SS]S  # ISO 8601