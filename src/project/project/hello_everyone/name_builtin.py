class NameBuiltin:
    value: str

    def __init__(self, value: str):
        if isinstance(value, str) is False:
            raise TypeError("Name must be a string")

        empty_name = len(value) < 1
        if empty_name:
            raise ValueError("Empty name")

        too_long_name = len(value) > 100
        if too_long_name:
            raise ValueError("Too long name")

        self.value = value
