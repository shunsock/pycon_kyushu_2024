from typeguard import check_type


def hello_with_bug(name: str) -> str:
    # 実行時に型ヒントは評価されないのでstr型以外が入りバグが発生する可能性がある
    return f"Hello {name}"


def hello_with_isinstance(name: str) -> str:
    if isinstance(name, str) is False:
        raise TypeError(f"input type of name must be str: {type(name)}")
    return f"Hello {name}"


def hello_with_check_type(name: str) -> str:
    check_type(name, str)
    return f"Hello {name}"
