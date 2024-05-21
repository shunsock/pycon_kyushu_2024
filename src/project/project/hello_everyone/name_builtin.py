class NameBuiltin:
    value: str

    def __init__(self, value: str):
        empty_name = len(value) < 1
        if empty_name:
            raise ValueError("Empty name")

        too_long_name = len(value) > 100
        if too_long_name:
            raise ValueError("Too long name")

        self.value = value
