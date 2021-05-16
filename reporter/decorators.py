import logging
import time

from .utils import format_args
from .utils import format_kwargs


def report_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger = logging.getLogger("reporter")
        logger.debug(
            f"{func.__name__} was executed with {format_args(args)}{format_kwargs(kwargs)}"
        )
        return result

    return wrapper


def report_call(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("reporter")
        logger.debug(
            f"{func.__name__} with {format_args(args)}{format_kwargs(kwargs)}, is about to be executed"
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
            f"{func.__name__} took {total_time:.5} seconds to execute with {format_args(args)}{format_kwargs(kwargs)}"
        )
        return result

    return wrapper


def report_mutation(variable):
    def mutation_decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger("reporter")
            logger.debug(f"Variable is {variable} before {func.__name__} execution")
            result = func(*args, **kwargs)
            logger.debug(f"Variable is {variable} after {func.__name__} execution")
            return result

        return wrapper

    return mutation_decorator


def report_str(obj):
    def str_decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger("reporter")
            logger.debug(f"{str(obj)} before {func.__name__} execution using `str`")
            result = func(*args, **kwargs)
            logger.debug(f"{str(obj)} after {func.__name__} execution using `str`")
            return result

        return wrapper

    return str_decorator


def report_repr(obj):
    def repr_decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger("reporter")
            logger.debug(f"{repr(obj)} before {func.__name__} execution using `repr`")
            result = func(*args, **kwargs)
            logger.debug(f"{repr(obj)} after {func.__name__} execution using `repr`")
            return result

        return wrapper

    return repr_decorator
