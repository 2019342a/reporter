import logging
from typing import Dict
from typing import List

import colorlog


def create_reporter():
    logger = colorlog.getLogger("reporter")
    logger.setLevel(logging.DEBUG)

    handler = colorlog.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = colorlog.ColoredFormatter(
        "%(thin_blue)s%(asctime)s - %(reset)s%(white)s%(name)s - %(bold)s%(log_color)s%(levelname)s - %(reset)s%(purple)s%(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)


def format_args(args: List):
    s = " ".join(map(str, args))
    return f"args {s}"


def format_kwargs(kwargs: Dict):
    s = ""
    for k, v in kwargs.items():
        s = f"{s} {k}={v}"
    return f", kwargs{s}" if len(s) > 0 else s
