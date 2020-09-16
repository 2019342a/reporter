from unittest.mock import patch

from .context import create_reporter


class TestUtils:
    """
    Test the utils module
    """

    @patch("logging.Logger.addHandler")
    def test_create_reporter(self, mock_process):
        create_reporter()
        assert mock_process.called
