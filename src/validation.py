from typing import Any, TypeVar
from src.errors import NonNaturalNumberError


NUM = TypeVar("NUM", int, float)


def validate_natural(n: Any) -> None:
    if not isinstance(n, int) or n <= 0:
        raise NonNaturalNumberError(n)


def validate_number(
    n: Any, types: tuple[int, float] | type[int] | type[float] = NUM.__constraints__
) -> None:
    if not isinstance(n, types):  # type: ignore
        raise TypeError("List contains non number objects")
