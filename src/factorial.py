from src.validation import validate_natural
from functools import lru_cache


def factorial(n: int) -> int:
    """
    Find factorial of number n using iterations
    Args:
        n (int): position
    Returns:
        int: factorial of number n
    Raises:
        NonNaturalNumberError: if n is not natural number
    """
    validate_natural(n)

    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact


@lru_cache()
def factorial_recursive(n: int) -> int:
    """
    Find factorial of number n using recursion
    Args:
        n (int): position
    Returns:
        int: factorial of number n
    Raises:
        NonNaturalNumberError: if n is not natural number
    """
    validate_natural(n)

    if n == 2:
        return 2

    return n * factorial_recursive(n - 1)
