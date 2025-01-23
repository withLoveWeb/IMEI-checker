import logging
import os
import sys

from loguru import logger

from .config import config



logger_name_list = [
    "aiogram",
]


class InterceptHandler(logging.Handler):
    def emit(self, record):
        level = record.levelname
        logger.opt(depth=6).log(level, record.getMessage())


def setup_logger() -> None:
    """Set up logging configuration."""
    logger.remove()
    if config.DEBUG:
        format_string = (
            "<light-cyan>{time:HH:mm:ss}</light-cyan> | "
            "<level> {level} </level> | "
            "<white> {file}:{function} {line}</white> - "
            "<light-white>{message}</light-white>"
        )
        logger.add(
            sink=sys.stdout,
            level="DEBUG",
            format=format_string,
            colorize=True,
        )
    else:
        format_string = (
            "<light-cyan>{time:DD-MM HH:mm:ss}</light-cyan> | "
            "<level> {level: <8} </level> | "
            "<white> {function}</white> - "
            "<light-white>{message}</light-white>"
        )
        logger.add(
            sink=sys.stdout,
            level="INFO",
            format=format_string,
            colorize=True,
        )
        log_path = os.path.join(config.PATH_LOG, "fastapi.log")
        logger.add(
            sink=log_path,
            level="WARNING",
            format=format_string,
            colorize=True,
        )


logging.basicConfig(handlers=[InterceptHandler()], level=0)
for name in logger_name_list:
    logging.getLogger(name).setLevel(logging.DEBUG)
