import pytest
from typeguard import TypeCheckError

from project.hello.hello_with_typeguard import run


def test_hello_with_typeguard() -> None:
    response = run("Alice")
    assert response == "Hello Alice"


def test_hello_raise_error_with_invalid_input() -> None:
    """
    Pythonは動的型付け言語なので、型ヒントは実行時に評価されない。
    そのため、型ヒントがstr型であるにも関わらずint型を入力してもエラーが発生しない。

    そこで、この関数は、期待されていない型の入力値に対して、2行目・3行目でTypeErrorを発生させる
    ```python
    if isinstance(name, str) is False:
        raise TypeError(f"nameはstr型であることが期待されています。入力値の型: {type(name)}")
    ```
    """
    with pytest.raises(TypeCheckError):
        run(123)
