import pytest

from project.hello.hello_with_isinstance import run


def test_hello_with_isinstance() -> None:
    response = run("Alice")
    assert response == "Hello Alice"


def test_hello_raise_error_with_invalid_input() -> None:
    with pytest.raises(TypeError):
        run(123)
