from unittest.mock import patch

from pytest import fixture

from .context import create_reporter
from .context import report_execution


class TestSimpleDecorators(object):

    @fixture
    def reporter(self):
        create_reporter()
        return None

    @patch('logging.Logger.debug')
    def test_execution(self, mock_process, reporter):
        @report_execution
        def add(a: int, b: int) -> int:
            return a + b

        add(1, 2)
        assert mock_process.called
