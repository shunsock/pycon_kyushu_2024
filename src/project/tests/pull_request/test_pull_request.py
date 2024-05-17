import pytest

from project.pull_request.pull_request import PullRequest


def test_raise_type_error_with_invalid_input_type() -> None:
    """
    PullRequest型以外の入力がある場合にTypeErrorが発生する
    """
    with pytest.raises(TypeError):
        PullRequest(branch_name=123)
