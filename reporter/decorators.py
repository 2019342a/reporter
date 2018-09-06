import logging


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
