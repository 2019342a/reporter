from unittest.mock import patch

from pytest import fixture

from .context import create_reporter
from .context import report_call
from .context import report_execution
from .context import report_mutation
from .context import report_repr
from .context import report_str
from .context import report_time


class TestSimpleDecorators:
    class DummyClass:
        def __str__(self) -> str:
            return "str method"

        def __repr__(self) -> str:
            return "repr method"

    @fixture
    def reporter(self):
        create_reporter()
        return None

    @patch("logging.Logger.debug")
    def test_execution(self, mock_process, reporter):
        @report_execution
        def add(a: int, b: int, c=1) -> int:
            return a + b + c

        add(1, 2)
        add(1, 2, c=2)
        assert mock_process.called
        mock_process.assert_any_call("add was executed with args 1 2")
        mock_process.assert_called_with("add was executed with args 1 2, kwargs c=2")

    @patch("logging.Logger.debug")
    def test_call(self, mock_process, reporter):
        @report_call
        def substract(a: int, b: int, c=1) -> int:
            return a - b - c

        substract(2, 1)
        substract(2, 1, c=1)
        assert mock_process.called
        mock_process.assert_any_call("substract with args 2 1, is about to be executed")
        mock_process.assert_called_with(
            "substract with args 2 1, kwargs c=1, is about to be executed"
        )

    @patch("logging.Logger.debug")
    def test_time(self, mock_process, reporter):
        @report_time
        def multiply(a: int, b: int, c=1) -> int:
            return a * b * c

        multiply(2, 6, c=2)
        assert mock_process.called

    @patch("logging.Logger.debug")
    def test_mutation(self, mock_process, reporter):
        variable = [1, 2, 3]

        @report_mutation(variable)
        def mutate(var):
            var[0] = 2

        mutate(variable)
        assert mock_process.called
        mock_process.assert_any_call(
            f"Variable is {str([1,2,3])} before mutate execution"
        )
        mock_process.assert_called_with(
            f"Variable is {str(variable)} after mutate execution"
        )

    @patch("logging.Logger.debug")
    def test_str(self, mock_process, reporter):
        obj = self.DummyClass()

        @report_str(obj)
        def nothing():
            ...

        nothing()
        assert mock_process.called
        mock_process.assert_called_with(
            f"{str(obj)} after nothing execution using `str`"
        )

    @patch("logging.Logger.debug")
    def test_repr(self, mock_process, reporter):
        obj = self.DummyClass()

        @report_repr(obj)
        def nothing():
            ...

        nothing()
        assert mock_process.called
        mock_process.assert_called_with(
            f"{repr(obj)} after nothing execution using `repr`"
        )
