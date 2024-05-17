from .approved_pull_request import ApprovedPullRequest
from .pull_request import PullRequest


def approve_pull_request(pull_request: PullRequest) -> ApprovedPullRequest:
    """
    Pull Requestを承認する

    Parameters
    ----------
    pull_request: PullRequest
        承認するPull Request

    Returns
    -------
    ApprovedPullRequest
        承認されたPull Request
    """
    if isinstance(pull_request, PullRequest) is False:
        raise TypeError(
            f"pull_requestはPullRequest型である必要があります。入力値の型: {type(pull_request)}"
        )

    return ApprovedPullRequest(
        branch_name=pull_request.branch_name,
    )
