---
contentSidebar: true
sidebarDepth: 0
---

# `nonebot.drivers` 模块

后端驱动适配基类
=================

各驱动请继承以下基类

## _abstract class_ `Driver(self, env, config)`

- **说明**

Driver 基类。

- **参数**

    - `env` (nonebot.config.Env)

    - `config` (nonebot.config.Config)

### _property_ `bots`

- **类型:** dict[str, Bot]

- **说明**

:类型:

``Dict[str, Bot]``
:说明:

  获取当前所有已连接的 Bot

### _property_ `logger`

- **类型:** 

- **说明:** 驱动专属 logger 日志记录器

### _property_ `type`

- **类型:** 

- **说明:** 驱动类型名称

### _class-var_ `_adapters`

- **类型:** dict[str, Type[Bot]]

- **说明**

:类型: ``Dict[str, Type[Bot]]``

:说明: 已注册的适配器列表

### _class-var_ `_bot_connection_hook`

- **类型:** set[(Bot) -> Awaitable[NoneType]]

- **说明**

:类型: ``Set[T_BotConnectionHook]``

:说明: Bot 连接建立时执行的函数

### _class-var_ `_bot_disconnection_hook`

- **类型:** set[(Bot) -> Awaitable[NoneType]]

- **说明**

:类型: ``Set[T_BotDisconnectionHook]``

:说明: Bot 连接断开时执行的函数

### _class-var_ `env`

- **类型:** 

- **说明**

:类型: ``str``

:说明: 环境名称

### _class-var_ `config`

- **类型:** 

- **说明**

:类型: ``Config``

:说明: 配置对象

### _class-var_ `_clients`

- **类型:** 

- **说明**

:类型: ``Dict[str, Bot]``

:说明: 已连接的 Bot

### _method_ `on_bot_connect(self, func)`

- **说明**

:说明:

装饰一个函数使他在 bot 通过 WebSocket 连接成功时执行。

:函数参数:

  * ``bot: Bot``: 当前连接上的 Bot 对象

- **参数**

    - `func` ((Bot) -> Awaitable[NoneType])

- **返回**

    - `(Bot) -> Awaitable[NoneType]`

### _method_ `on_bot_disconnect(self, func)`

- **说明**

:说明:

装饰一个函数使他在 bot 通过 WebSocket 连接断开时执行。

:函数参数:

  * ``bot: Bot``: 当前连接上的 Bot 对象

- **参数**

    - `func` ((Bot) -> Awaitable[NoneType])

- **返回**

    - `(Bot) -> Awaitable[NoneType]`

### _method_ `on_shutdown(self, func)`

- **说明**

注册一个在驱动停止时运行的函数

- **参数**

    - `func` (Callable)

- **返回**

    - `Callable`

### _method_ `on_startup(self, func)`

- **说明**

注册一个在驱动启动时运行的函数

- **参数**

    - `func` (Callable)

- **返回**

    - `Callable`

### _method_ `register_adapter(self, name, adapter, **kwargs)`

- **说明**

:说明:

注册一个协议适配器

:参数:

  * ``name: str``: 适配器名称，用于在连接时进行识别
  * ``adapter: Type[Bot]``: 适配器 Class
  * ``**kwargs``: 其他传递给适配器的参数

- **参数**

    - `name` (str)

    - `adapter` (Type[Bot])

    - `kwargs`

- **返回**

    - `Unknown`

### _method_ `run(self, *args, **kwargs)`

- **说明**

:说明:

启动驱动框架

:参数:
  * ``*args``
  * ``**kwargs``

- **参数**

    - `args`

    - `kwargs`

- **返回**

    - `Unknown`

## _abstract class_ `ForwardDriver(self, env, config)`

- **说明**

Forward Driver 基类。将客户端框架封装，以满足适配器使用。

- **参数**

    - `env` (nonebot.config.Env)

    - `config` (nonebot.config.Config)

### _method_ `setup_http_polling(self, setup)`

- **说明**

:说明:

注册一个 HTTP 轮询连接，如果传入一个函数，则该函数会在每次连接时被调用

:参数:

  * ``setup: Union[HTTPPollingSetup, Callable[[], Awaitable[HTTPPollingSetup]]]``

- **参数**

    - `setup` (HTTPPollingSetup | () -> Awaitable[HTTPPollingSetup])

- **返回**

    - `None`

### _method_ `setup_websocket(self, setup)`

- **说明**

:说明:

注册一个 WebSocket 连接，如果传入一个函数，则该函数会在每次重连时被调用

:参数:

  * ``setup: Union[WebSocketSetup, Callable[[], Awaitable[WebSocketSetup]]]``

- **参数**

    - `setup` (WebSocketSetup | () -> Awaitable[WebSocketSetup])

- **返回**

    - `None`

## _abstract class_ `ReverseDriver(self, env, config)`

- **说明**

Reverse Driver 基类。将后端框架封装，以满足适配器使用。

- **参数**

    - `env` (nonebot.config.Env)

    - `config` (nonebot.config.Config)

### _property_ `asgi`

- **类型:** Any

- **说明:** 驱动 ASGI 对象

### _property_ `server_app`

- **类型:** Any

- **说明:** 驱动 APP 对象

## _abstract class_ `HTTPConnection(self, http_version, scheme, path, query_string=b'', headers=<factory>)`

- **说明**

HTTPConnection(http_version: str, scheme: str, path: str, query_string: bytes = b'', headers: Dict[str, str] = <factory>)

- **参数**

    - `http_version` (str)

    - `scheme` (str)

    - `path` (str)

    - `query_string` (bytes)

    - `headers` (dict[str, str])

### _class-var_ `query_string`

- **类型:** bytes

- **说明:** URL portion after the ``?``, percent-encoded.

### _property_ `type`

- **类型:** str

- **说明:** Connection type.

### _class-var_ `http_version`

- **类型:** str

- **说明:** One of ``"1.0"``, ``"1.1"`` or ``"2"``.

### _class-var_ `scheme`

- **类型:** str

- **说明:** URL scheme portion (likely ``"http"`` or ``"https"``).

### _class-var_ `path`

- **类型:** str

- **说明**

HTTP request target excluding any query string,

with percent-encoded sequences and UTF-8 byte sequences
decoded into characters.

### _class-var_ `headers`

- **类型:** dict[str, str]

- **说明**

A dict of name-value pairs,

where name is the header name, and value is the header value.

Order of header values must be preserved from the original HTTP request;
order of header names is not important.

Header names must be lowercased.

## _class_ `HTTPRequest(self, http_version, scheme, path, query_string=b'', headers=<factory>, method='GET', body=b'')`

- **说明**

HTTP 请求封装。参考 `asgi http scope`_。

.. _asgi http scope:
    https://asgi.readthedocs.io/en/latest/specs/www.html#http-connection-scope

- **参数**

    - `http_version` (str)

    - `scheme` (str)

    - `path` (str)

    - `query_string` (bytes)

    - `headers` (dict[str, str])

    - `method` (str)

    - `body` (bytes)

### _class-var_ `body`

- **类型:** bytes

- **说明**

Body of the request.

Optional; if missing defaults to ``b""``.

### _class-var_ `method`

- **类型:** str

- **说明:** The HTTP method name, uppercased.

### _property_ `type`

- **类型:** str

- **说明:** Always ``http``

## _class_ `HTTPResponse(self, status, body=None, headers=<factory>)`

- **说明**

HTTP 响应封装。参考 `asgi http scope`_。

.. _asgi http scope:
    https://asgi.readthedocs.io/en/latest/specs/www.html#http-connection-scope

- **参数**

    - `status` (int)

    - `body` (bytes | None)

    - `headers` (dict[str, str])

### _instance-var_ `body`

- **类型:** bytes | None

- **说明**

HTTP body content.

Optional; if missing defaults to ``None``.

### _property_ `type`

- **类型:** str

- **说明:** Always ``http``

### _instance-var_ `status`

- **类型:** int

- **说明:** HTTP status code.

### _instance-var_ `headers`

- **类型:** dict[str, str]

- **说明**

A dict of name-value pairs,

where name is the header name, and value is the header value.

Order must be preserved in the HTTP response.

Header names must be lowercased.

Optional; if missing defaults to an empty dict.

## _abstract class_ `WebSocket(self, http_version, scheme, path, query_string=b'', headers=<factory>)`

- **说明**

WebSocket 连接封装。参考 `asgi websocket scope`_。

.. _asgi websocket scope:
    https://asgi.readthedocs.io/en/latest/specs/www.html#websocket-connection-scope

- **参数**

    - `http_version` (str)

    - `scheme` (str)

    - `path` (str)

    - `query_string` (bytes)

    - `headers` (dict[str, str])

### _property_ `closed`

- **类型:** bool

- **说明**

:类型: ``bool``

:说明: 连接是否已经关闭

### _property_ `type`

- **类型:** str

- **说明:** Always ``websocket``

### _async method_ `accept(self)`

- **说明**

接受 WebSocket 连接请求

- **参数**

    无

- **返回**

    - `Unknown`

### _async method_ `close(self, code)`

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

    - `Unknown`

### _async method_ `send_bytes(self, data)`

- **说明**

发送一条 WebSocket binary 信息

- **参数**

    - `data` (bytes)

- **返回**

    - `Unknown`

## _class_ `HTTPPollingSetup(self, adapter, self_id, url, method, body, headers, http_version, poll_interval)`

- **说明**

HTTPPollingSetup(adapter: str, self_id: str, url: str, method: str, body: bytes, headers: Dict[str, str], http_version: str, poll_interval: float)

- **参数**

    - `adapter` (str)

    - `self_id` (str)

    - `url` (str)

    - `method` (str)

    - `body` (bytes)

    - `headers` (dict[str, str])

    - `http_version` (str)

    - `poll_interval` (float)

### _instance-var_ `adapter`

- **类型:** str

- **说明:** 协议适配器名称

### _instance-var_ `self_id`

- **类型:** str

- **说明:** 机器人 ID

### _instance-var_ `url`

- **类型:** str

- **说明:** URL

### _instance-var_ `method`

- **类型:** str

- **说明:** HTTP method

### _instance-var_ `body`

- **类型:** bytes

- **说明:** HTTP body

### _instance-var_ `headers`

- **类型:** dict[str, str]

- **说明:** HTTP headers

### _instance-var_ `http_version`

- **类型:** str

- **说明:** HTTP version

### _instance-var_ `poll_interval`

- **类型:** float

- **说明:** HTTP 轮询间隔

## _class_ `WebSocketSetup(self, adapter, self_id, url, headers=<factory>, reconnect_interval=3.0)`

- **说明**

WebSocketSetup(adapter: str, self_id: str, url: str, headers: Dict[str, str] = <factory>, reconnect_interval: float = 3.0)

- **参数**

    - `adapter` (str)

    - `self_id` (str)

    - `url` (str)

    - `headers` (dict[str, str])

    - `reconnect_interval` (float)

### _instance-var_ `reconnect_interval`

- **类型:** float

- **说明:** WebSocket 重连间隔

### _instance-var_ `adapter`

- **类型:** str

- **说明:** 协议适配器名称

### _instance-var_ `self_id`

- **类型:** str

- **说明:** 机器人 ID

### _instance-var_ `url`

- **类型:** str

- **说明:** URL

### _instance-var_ `headers`

- **类型:** dict[str, str]

- **说明:** HTTP headers