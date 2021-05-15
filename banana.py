from reporter.utils import create_reporter
from reporter.decorators import report_execution

create_reporter()


@report_execution
def add(a, b):
    return a + b


add(1, 2)
