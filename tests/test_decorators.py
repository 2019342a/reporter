from unittest.mock import patch

from pytest import fixture

from .context import create_reporter
from .context import report_call
from .context import report_execution
from .context import report_mutation
from .context import report_time


class TestSimpleDecorators:
    @fixture
    def reporter(self):
        create_reporter()
        return None

    @patch("logging.Logger.debug")
    def test_execution(self, mock_process, reporter):
        @report_execution
        def add(a: int, b: int) -> int:
            return a + b

        add(1, 2)
        assert mock_process.called

    @patch("logging.Logger.debug")
    def test_call(self, mock_process, reporter):
        @report_call
        def substract(a: int, b: int) -> int:
            return a - b

        substract(2, 1)
        assert mock_process.called

    @patch("logging.Logger.debug")
    def test_time(self, mock_process, reporter):
        @report_time
        def multiply(a: int, b: int) -> int:
            return a * b

        multiply(2, 6)
        assert mock_process.called

    @patch("logging.Logger.debug")
    def test_mutation(self, mock_process, reporter):
        variable = [1, 2, 3]

        @report_mutation(variable)
        def mutate(var):
            var[0] = 2

        mutate(variable)
        assert mock_process.called
