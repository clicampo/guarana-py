import logging
from pickle import FALSE
from loguru import logger
import sys

class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def init_loging():
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(logging.DEBUG)
    logger.add(sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}", level="DEBUG", serialize=True)

    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logger.remove()
    logger.configure(
        handlers=[
             {
                "sink": sys.stdout,
                "serialize": True,
                "level": "DEBUG",
            },
            {
                "sink": sys.stdout,
                "serialize": True,
                "filter": lambda record: record["level"].no < 40,
                "level": "INFO",
            },
            {
                "sink": sys.stderr,
                "serialize": True,
                "filter": lambda record: record["level"].no >= 40,
                "level": "ERROR",
            },
        ]
    )