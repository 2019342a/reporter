import logging
import time


def report_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger = logging.getLogger("reporter")
        logger.debug(
            "{} was executed with {} {}".format(func.__name__, *args, **kwargs)
        )
        return result

    return wrapper


def report_call(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("reporter")
        logger.debug(
            "{} whith arguments {} {} is about to be executed".format(
                func.__name__, *args, **kwargs
            )
        )
        result = func(*args, **kwargs)
        return result

    return wrapper


def report_time(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("reporter")
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        end_time = time.monotonic()
        total_time = end_time - start_time
        logger.debug(
            "{} took {:.5} seconds to execute with arguments {} {}".format(
                func.__name__,
                total_time,
                *args,
                **kwargs,
            )
        )
        return result

    return wrapper


def report_mutation(variable):
    def mutation_decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger("reporter")
            logger.debug(
                "Variable is {} before {} execution".format(variable, func.__name__)
            )
            result = func(*args, **kwargs)
            logger.debug(
                "Variable is {} after {} execution".format(variable, func.__name__)
            )
            return result

        return wrapper

    return mutation_decorator


def report_str(obj):
    def str_decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger("reporter")
            logger.debug(
                "{} before {} execution using `str`".format(str(obj), func.__name__)
            )
            result = func(*args, **kwargs)
            logger.debug(
                "{} after {} execution using `str`".format(str(obj), func.__name__)
            )
            return result

        return wrapper

    return str_decorator


def report_repr(obj):
    def repr_decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger("reporter")
            logger.debug(
                "{} before {} execution using `repr`".format(repr(obj), func.__name__)
            )
            result = func(*args, **kwargs)
            logger.debug(
                "{} after {} execution using `repr`".format(repr(obj), func.__name__)
            )
            return result

        return wrapper

    return repr_decorator
