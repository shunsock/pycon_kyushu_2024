from typing import List


def run(names: List[str]) -> List[str]:
    for name in names:
        if isinstance(name, str) is False:
            raise TypeError(
                f"nameの型はstrが期待されています。入力値の型: {type(name)}"
            )
        if len(name) == 0:
            raise ValueError("空の文字列は許可されていません")
        if len(name) >= 100:
            raise ValueError("文字列は100文字以下である必要があります")

    return [f"Hello {name}" for name in names]
