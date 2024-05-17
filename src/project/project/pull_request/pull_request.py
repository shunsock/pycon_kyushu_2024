class PullRequest:
    """
    このclassでは説明のためあえてPydanticを使用していません
    """

    branch_name: str

    def __init__(self, branch_name: str):
        if isinstance(branch_name, str) is False:
            raise TypeError(
                f"branch_nameはstrである必要があります。入力値の型: {type(branch_name)}"
            )
        self.branch_name = branch_name
