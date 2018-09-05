import logging


def report_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger = logging.getLogger('reporter')
        logger.debug('function/method {} was executed'.format(func))
        return result
    return wrapper
