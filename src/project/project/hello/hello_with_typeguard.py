from typeguard import check_type


def hello_with_type_guard(name: str) -> str:
    check_type(name, str)
    return f"Hello {name}"
