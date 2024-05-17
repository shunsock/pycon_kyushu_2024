from pydantic import BaseModel, StrictStr, field_validator


class Name(BaseModel):
    value: StrictStr

    @field_validator("value")
    def name_length(cls, value: str) -> str:
        empty_name = len(value) == 0
        if empty_name:
            raise ValueError("Empty name")

        too_long_name = len(value) >= 100
        if too_long_name:
            raise ValueError("Too long name")

        return value
