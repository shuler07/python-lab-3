from functools import lru_cache
from src.validation import validate_natural


def fibonacci(n: int) -> int:
    """
    Find fibonacci number at position n using iterations
    Args:
        n (int): position
    Returns:
        int: fibonacci number at positon n
    Raises:
        NonNaturalNumberError: if n is not natural number
    """
    validate_natural(n)

    if n <= 2:
        return 1

    prev = cur = 1
    for _ in range(2, n):
        prev, cur = cur, prev + cur

    return cur


@lru_cache()
def fibonacci_recursive(n: int) -> int:
    """
    Find fibonacci number at position n using recursion
    Args:
        n (int): position
    Returns:
        int: fibonacci number at positon n
    Raises:
        NonNaturalNumberError: if n is not natural number
    """
    validate_natural(n)

    if n <= 2:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
