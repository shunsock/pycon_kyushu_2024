import pytest

from project.hello_everyone.hello_everyone import Name


def test_name_validation() -> None:
    # Test valid input
    name = Name(value="Alice")
    assert name.value == "Alice"


def test_name_must_not_be_empty() -> None:
    with pytest.raises(ValueError):
        Name(value="")


def test_name_must_not_be_longer_than_100_characters() -> None:
    with pytest.raises(ValueError):
        Name(value="A" * 101)


def test_name_must_be_str() -> None:
    """
    PydanticのBaseModelを継承したクラスは、型ヒントに従って入力値の型を検証する。
    従って、valueにstr型以外の値を入力すると、Pydanticが自動的にエラーを発生させる。
    """
    with pytest.raises(ValueError):
        Name(value=123)
