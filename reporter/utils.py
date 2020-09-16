import logging

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
