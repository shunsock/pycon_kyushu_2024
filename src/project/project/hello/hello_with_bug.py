def run(name: str) -> str:
    # 実行時に型ヒントは評価されないのでstr型以外が入りバグが発生する可能性がある
    return f"Hello {name}"
