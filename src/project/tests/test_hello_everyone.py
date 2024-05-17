import pytest
from typeguard import TypeCheckError

from project.hello_everyone import Name, hello_everyone


def test_name_validation() -> None:
    # Test valid input
    name = Name(value="Alice")
    assert name.value == "Alice"

    # Test empty name
    with pytest.raises(ValueError):
        Name(value="")

    # Test name with length greater than 100
    with pytest.raises(ValueError):
        Name(value="A" * 101)

    # Test invalid attribute type
    with pytest.raises(ValueError):
        Name(value=123)


def test_hello_everyone() -> None:
    # Test valid input
    names = [Name(value="Alice"), Name(value="Bob")]
    response = hello_everyone(names)
    assert response == ["Hello Alice", "Hello Bob"]

    # Test invalid input type
    with pytest.raises(TypeCheckError):
        hello_everyone(["Alice", "Bob"])
