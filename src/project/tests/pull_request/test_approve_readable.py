import pytest

from project.pull_request.approve_readable import approve_pull_request
from project.pull_request.approved_pull_request import ApprovedPullRequest
from project.pull_request.pull_request import PullRequest


def test_approve_pull_request() -> None:
    pull_request = PullRequest(branch_name="branch_name")
    approved_pull_request = approve_pull_request(pull_request=pull_request)

    # 戻り値の型が正しいことを確認
    assert isinstance(approved_pull_request, ApprovedPullRequest)

    # 戻り値の型の中身が正しいことを確認
    assert approved_pull_request.branch_name == "branch_name"


def test_approve_pull_request_raise_error_with_invalid_input() -> None:
    """
    PullRequest型以外の入力がある場合にTypeErrorが発生する
    """
    with pytest.raises(TypeError):
        approve_pull_request(pull_request="hoge")
