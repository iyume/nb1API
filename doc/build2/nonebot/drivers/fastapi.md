---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.drivers.fastapi` 模块

FastAPI 驱动适配
================

本驱动同时支持服务端以及客户端连接

后端使用方法请参考: `FastAPI 文档`_

.. _FastAPI 文档:
    https://fastapi.tiangolo.com/

## _class_ `Config(__pydantic_self__, _env_file='<object object>', _env_file_encoding=None, _secrets_dir=None, **values)`

- **说明**

FastAPI 驱动框架设置，详情参考 FastAPI 文档

- **参数**

    - `__pydantic_self__`

    - `_env_file` (pathlib.Path | str | NoneType)

    - `_env_file_encoding` (str | None)

    - `_secrets_dir` (pathlib.Path | str | NoneType)

    - `values` (Any)

### _class-var_ `WEBSOCKET_SETUP`

- **类型:** 

- **说明:** FastAPI 驱动框架设置，详情参考 FastAPI 文档

### _class-var_ `fastapi_openapi_url`

- **类型:** str | None

- **说明**

:类型:

``Optional[str]``

:说明:

  ``openapi.json`` 地址，默认为 ``None`` 即关闭

### _class-var_ `fastapi_docs_url`

- **类型:** str | None

- **说明**

:类型:

``Optional[str]``

:说明:

  ``swagger`` 地址，默认为 ``None`` 即关闭

### _class-var_ `fastapi_redoc_url`

- **类型:** str | None

- **说明**

:类型:

``Optional[str]``

:说明:

  ``redoc`` 地址，默认为 ``None`` 即关闭

### _class-var_ `fastapi_reload`

- **类型:** bool | None

- **说明**

:类型:

``Optional[bool]``

:说明:

  开启/关闭冷重载，默认会在配置了 app 的 debug 模式启用

### _class-var_ `fastapi_reload_dirs`

- **类型:** list[str] | None

- **说明**

:类型:

``Optional[List[str]]``

:说明:

  重载监控文件夹列表，默认为 uvicorn 默认值

### _class-var_ `fastapi_reload_delay`

- **类型:** float | None

- **说明**

:类型:

``Optional[float]``

:说明:

  重载延迟，默认为 uvicorn 默认值

### _class-var_ `fastapi_reload_includes`

- **类型:** list[str] | None

- **说明**

:类型:

``Optional[List[str]]``

:说明:

  要监听的文件列表，支持 glob pattern，默认为 uvicorn 默认值

### _class-var_ `fastapi_reload_excludes`

- **类型:** list[str] | None

- **说明**

:类型:

``Optional[List[str]]``

:说明:

  不要监听的文件列表，支持 glob pattern，默认为 uvicorn 默认值

## _class_ `Driver(self, env, config)`

- **说明**

FastAPI 驱动框架

:上报地址:

  * ``/{adapter name}/``: HTTP POST 上报
  * ``/{adapter name}/http/``: HTTP POST 上报
  * ``/{adapter name}/ws``: WebSocket 上报
  * ``/{adapter name}/ws/``: WebSocket 上报

- **参数**

    - `env` (nonebot.config.Env)

    - `config` (nonebot.config.Config)

### _property_ `asgi`

- **类型:** fastapi.applications.FastAPI

- **说明:** ``FastAPI APP`` 对象

### _property_ `logger`

- **类型:** logging.Logger

- **说明:** fastapi 使用的 logger

### _property_ `server_app`

- **类型:** fastapi.applications.FastAPI

- **说明:** ``FastAPI APP`` 对象

### _property_ `type`

- **类型:** str

- **说明:** 驱动名称: ``fastapi``

### _method_ `on_shutdown(self, func)`

- **说明**

参考文档: `Events <https://fastapi.tiangolo.com/advanced/events/#startup-event>`_

- **参数**

    - `func` (Callable)

- **返回**

    - `Callable`

### _method_ `on_startup(self, func)`

- **说明**

参考文档: `Events <https://fastapi.tiangolo.com/advanced/events/#startup-event>`_

- **参数**

    - `func` (Callable)

- **返回**

    - `Callable`

### _method_ `run(self, host=None, port=None, *, app=None, **kwargs)`

- **说明**

使用 ``uvicorn`` 启动 FastAPI

- **参数**

    - `host` (str | None)

    - `port` (int | None)

    - `app` (str | None)

    - `kwargs`

- **返回**

    - `Unknown`

### _method_ `setup_http_polling(self, setup)`

- **说明**

:说明:

注册一个 HTTP 轮询连接，如果传入一个函数，则该函数会在每次连接时被调用

:参数:

  * ``setup: Union[HTTPPollingSetup, Callable[[], Awaitable[HTTPPollingSetup]]]``

- **参数**

    - `setup` (nonebot.drivers.HTTPPollingSetup | () -> Awaitable[nonebot.drivers.HTTPPollingSetup])

- **返回**

    - `None`

### _method_ `setup_websocket(self, setup)`

- **说明**

:说明:

注册一个 WebSocket 连接，如果传入一个函数，则该函数会在每次重连时被调用

:参数:

  * ``setup: Union[WebSocketSetup, Callable[[], Awaitable[WebSocketSetup]]]``

- **参数**

    - `setup` (nonebot.drivers.WebSocketSetup | () -> Awaitable[nonebot.drivers.WebSocketSetup])

- **返回**

    - `None`

## _class_ `WebSocket(self, http_version, scheme, path, query_string=b'', headers=<factory>, websocket=None)`

- **说明**

WebSocket(http_version: str, scheme: str, path: str, query_string: bytes = b'', headers: Dict[str, str] = <factory>, websocket: Union[starlette.websockets.WebSocket, websockets.legacy.client.WebSocketClientProtocol] = None)

- **参数**

    - `http_version` (str)

    - `scheme` (str)

    - `path` (str)

    - `query_string` (bytes)

    - `headers` (dict[str, str])

    - `websocket` (starlette.websockets.WebSocket | websockets.legacy.client.WebSocketClientProtocol)

### _property_ `closed`

- **类型:** bool

- **说明**

:类型: ``bool``

:说明: 连接是否已经关闭

### _class-var_ `websocket`

- **类型:** starlette.websockets.WebSocket | websockets.legacy.client.WebSocketClientProtocol

### _async method_ `accept(self)`

- **说明**

接受 WebSocket 连接请求

- **参数**

    无

- **返回**

    - `Unknown`

### _async method_ `close(self, code=1000)`

- **说明**

关闭 WebSocket 连接请求

- **参数**

    - `code` (int)

- **返回**

    - `Unknown`

### _async method_ `receive(self)`

- **说明**

接收一条 WebSocket text 信息

- **参数**

    无

- **返回**

    - `str`

### _async method_ `receive_bytes(self)`

- **说明**

接收一条 WebSocket binary 信息

- **参数**

    无

- **返回**

    - `bytes`

### _async method_ `send(self, data)`

- **说明**

发送一条 WebSocket text 信息

- **参数**

    - `data` (str)

- **返回**

    - `None`

### _async method_ `send_bytes(self, data)`

- **说明**

发送一条 WebSocket binary 信息

- **参数**

    - `data` (bytes)

- **返回**

    - `None`