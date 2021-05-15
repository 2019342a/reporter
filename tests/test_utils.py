from unittest.mock import patch

from .context import create_reporter
from .context import format_args
from .context import format_kwargs


@patch("logging.Logger.addHandler")
def test_create_reporter(mock_process):
    create_reporter()
    assert mock_process.called


def test_format_args():
    integers = [1, 2, 3]
    strings = ["a", "b", "c"]
    assert format_args(integers) == "args 1 2 3"
    assert format_args(strings) == "args a b c"


def test_format_kwargs():
    kwargs = {1: 2, 2: 3}
    assert format_kwargs({}) == ""
    assert format_kwargs(kwargs) == ", kwargs 1=2 2=3"
