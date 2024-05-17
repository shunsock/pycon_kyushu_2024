def hello_with_isinstance(name: str) -> str:
    if isinstance(name, str) is False:
        raise TypeError(f"input type of name must be str: {type(name)}")
    return f"Hello {name}"
