from typeguard import check_type


def run(name: str) -> str:
    check_type(name, str)
    return f"Hello {name}"
