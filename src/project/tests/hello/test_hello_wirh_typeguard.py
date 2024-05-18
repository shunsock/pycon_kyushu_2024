import pytest
from typeguard import TypeCheckError

from project.hello.hello_with_typeguard import run


def test_hello_with_typeguard() -> None:
    response = run("Alice")
    assert response == "Hello Alice"


def test_hello_raise_error_with_invalid_input() -> None:
    with pytest.raises(TypeCheckError):
        run(123)
