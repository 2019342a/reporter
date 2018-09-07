import logging
import time


def report_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger = logging.getLogger('reporter')
        logger.debug(
            '{} was executed with {} {}'.format(
                func.__name__,
                *args,
                **kwargs
            )
        )
        return result
    return wrapper


def report_call(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('reporter')
        logger.debug(
            '{} whith arguments {} {} is about to be executed'.format(
                func.__name__,
                *args,
                **kwargs
            )
        )
        result = func(*args, **kwargs)
        return result
    return wrapper


def report_time(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('reporter')
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        end_time = time.monotonic()
        total_time = end_time - start_time
        logger.debug(
            '{} took {:.5} seconds to execute with arguments {} {}'.format(
                func.__name__,
                total_time,
                *args,
                **kwargs,
            )
        )
        return result
    return wrapper
