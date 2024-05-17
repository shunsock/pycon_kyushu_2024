import pytest

from project.pull_request.approved_pull_request import ApprovedPullRequest


def test_raise_type_error_with_invalid_input_type() -> None:
    """
    ApprovedPullRequest型以外の入力がある場合にTypeErrorが発生する
    """
    with pytest.raises(TypeError):
        ApprovedPullRequest(branch_name=123)
