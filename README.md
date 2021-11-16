# NoneBot v1 API 文档自动生成

目前 NoneBot v1 的文档中“API”部分是手动编写的，在更新代码接口的同时需要手动更新文档，可能造成文档与代码不匹配，形成额外的维护成本。我们希望将 API 文档改为直接编写在 Python docstring 中，通过工具自动生成 API 文档。

## TODO

- [x] pyi

    **在此问题的解决上，我对 pyi resolver 定义了一下几点行为**

    1. 若同一个 obj 在 real module 和 pyi 内同时写了 docstring，则使用 pyi 的 docstring

    2. 若同一个 obj 在 real module 和 pyi 内有一个写了 docstring，则使用那个 docstring (IDE behavior)

    3. pyi 内的 `__pdoc__` 是无效的，必须在 real module 定义

    4. 根据 PEP-484，当 stub file 存在时，real module annotation 将被完全忽视

    5. get_source 会获取 real module 的源码

    结合上面定义的行为，得出对于 pyi object 两种处理方式

    1. 将 pyi object `__annotation__` (class `__annotations__`) patch 到 real object，丢弃 pyi object

    > patch `__signature__` on real function

    2. 将 real object 一些特性 patch 到 pyi object，使其保持某些性质不变，并丢弃 real object

    > patch `__code__` on pyi function

    **WARNING:**

    1. stub file 禁止出现 relative import，原因是 `exec()` 无法得知当前文件的 parent package

- [ ] overload

    **overload 问题上，有以下几点特点**

    1. 一个 type overload function 应当只有 `@overload` 一个装饰器

    **解决方法**

    1. 移除 ast.FunctionDef.decorator_list 后 unparse 源码，使用 exec 获得的 globals 执行去除装饰器的源码获取函数对象

    2. 对函数对象签名，保存

    3. 存在 globals 的对应对象应该是一个函数的 implement，提取出来为 docstring resolver 作准备

- [ ] decorator

- [ ] url link

## NoneBot 文档修正

- [ ] nonebot

- [x] nonebot.argparse

- [ ] nonebot.default_config

- [x] nonebot.exceptions

- [x] nonebot.helpers

- [x] nonebot.log

- [x] nonebot.message

- [x] nonebot.natural_language

- [x] nonebot.notice_request

- [x] nonebot.permission

- [ ] nonebot.plugin (relate to `overload` problem)

- [x] nonebot.sched

- [x] nonebot.session

- [ ] nonebot.typing

- [x] nonebot.command

- [ ] nonebot.command.group (relate to `pyi` problem)

- [x] nonebot.command.argfilter

- [x] nonebot.command.argfilter.controllers

- [x] nonebot.command.argfilter.converters

- [x] nonebot.command.argfilter.extractors

- [x] nonebot.command.argfilter.validators

- [x] nonebot.experimental

- [x] nonebot.experimental.permission

- [x] nonebot.experimental.plugin

- [x] nonebot.plugins

- [x] nonebot.plugins.base

## 遗留问题

- 类文档的继承。目前的方案沿用 pdoc，它的主要表现为 1. 如果当前类没有 docstring，则从 mro 寻找替换；2. 从 mro 遍历 attr，为当前类加上没有的 attr doc。

- 类变量的文档获取。当文档没写但是我们希望此变量输出时，`__doc__` 获取的是 descriptor 的内置文档（比如 `__get__`, `_tuplegetter`）导致非预期的描述输出。在类下以 annotation 形式标注的 var docstring 并不会正确覆盖 `__doc__`，而若是写在比如说 property 的文档时，`__doc__` 可以正确覆盖。fd557d 暂时性修复了此问题。

    - `Return an attribute of instance, which is of type owner.`(default `__get__`), `Alias for field number 0`(NamedTuple) 都不应出现在自动生成的文档中。

- 函数的隐性参数。目前 API 自动生成旨在输出文档与源码保持一致，而隐性的参数传递，如通过 kwargs 传递的参数并不会写在源码，因此即便写了对应参数的文档也不会输出。

- 变量的文档获取。当 `get_type_hints` 参数为模块，且模块下的变量含有 `ForwardRef` 会直接解析错误。`inspect.signature` 只适用函数。当前问题保留。

## Feature TODO

- [ ] resolve ForwardRef
