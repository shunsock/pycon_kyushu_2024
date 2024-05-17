import pytest

from project.hello_everyone.hello_everyone_hard_mode import run


def test_hello_everyone_hard_mode() -> None:
    # Test valid input
    assert run(["Alice", "Bob"]) == ["Hello Alice", "Hello Bob"]


def test_hello_everyone_hard_mode_raises_type_error() -> None:
    # Test invalid input
    with pytest.raises(TypeError):
        run([123])


def test_hello_everyone_hard_mode_raises_value_error_empty_string() -> None:
    # Test invalid input
    with pytest.raises(ValueError):
        run([""])


def test_hello_everyone_hard_mode_raises_value_error_long_string() -> None:
    # Test invalid input
    with pytest.raises(ValueError):
        run(["A" * 101])
