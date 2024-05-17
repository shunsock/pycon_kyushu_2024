def run(name: str) -> str:
    if isinstance(name, str) is False:
        raise TypeError(
            f"nameはstr型であることが期待されています。入力値の型: {type(name)}"
        )
    return f"Hello {name}"
