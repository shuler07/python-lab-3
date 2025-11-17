from typing import Any
from src.errors import NonNaturalNumberError


def validate_natural(n: Any) -> None:
    if not isinstance(n, int) or n <= 0:
        raise NonNaturalNumberError(n)


def validate_number(n: Any) -> None:
    if not isinstance(n, (int, float)):
        raise TypeError("List contains non number objects")
