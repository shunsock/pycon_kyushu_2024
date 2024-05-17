from typing import List

from typeguard import check_type

from .name import Name


def hello_everyone(names: List[Name]) -> List[str]:
    check_type(names, List[Name])
    return [f"Hello {name.value}" for name in names]
