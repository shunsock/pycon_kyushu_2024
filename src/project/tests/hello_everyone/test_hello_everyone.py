import pytest
from typeguard import TypeCheckError

from project.hello_everyone.hello_everyone import Name, hello_everyone


def test_hello_everyone() -> None:
    # Test valid input
    names = [Name(value="Alice"), Name(value="Bob")]
    response = hello_everyone(names)
    assert response == ["Hello Alice", "Hello Bob"]


def test_hello_everyone_raise_error_with_invalid_input_type() -> None:
    # Test invalid input type
    with pytest.raises(TypeCheckError):
        hello_everyone(["Alice", "Bob"])
