import logging
import sys

logger: logging.Logger = logging.getLogger('nonebot')
"""
NoneBot 全局的 logger。

用法:
    ```python
    logger.debug('Some log message here')
    ```
"""
default_handler = logging.StreamHandler(sys.stdout)
default_handler.setFormatter(
    logging.Formatter('[%(asctime)s %(name)s] %(levelname)s: %(message)s'))
logger.addHandler(default_handler)


__all__ = [
    'logger',
]
