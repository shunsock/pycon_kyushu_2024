from project.hello.hello_with_bug import run


def test_hello_with_bug() -> None:
    response = run("Alice")
    assert response == "Hello Alice"


def test_hello_does_not_raise_error_with_invalid_input() -> None:
    """
    Pythonは動的型付け言語なので、型ヒントは実行時に評価されない。
    そのため、型ヒントがstr型であるにも関わらずint型を入力してもエラーが発生しない。
    この場合は、Castが発生している。
    """
    response = run(123)
    assert response == "Hello 123"
