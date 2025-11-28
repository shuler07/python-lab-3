import random


def rand_int_array(n: int, lo: int, hi: int, distinct=False, seed=None) -> list[int]:
    """
    Generate random integer array
    Args:
        n (int): array size
        lo (int): minimum value of elements
        hi (int): maximum value of elements
        distinct (bool): are values distinct
        seed (int | float | str | bytes | bytearray | None): array seed
    Returns:
        list[int]: array of n integer elements within [lo, hi]
    """

    def _get_disctinct_array():
        _a: set[int] = set()
        nonlocal n, lo, hi
        n = min(n, hi - lo + 1)
        while len(_a) < n:
            _a.add(random.randint(lo, hi))
        return list(_a)

    def _get_array():
        _a: list[int] = []
        nonlocal n, lo, hi
        while len(_a) < n:
            _a.append(random.randint(lo, hi))
        return _a

    random.seed(seed)

    return _get_array() if not distinct else _get_disctinct_array()


def reverse_sorted(
    n: int, lo: int, hi: int, isInt=True, distinct=False, seed=None
) -> list[int]:
    """
    Generate random array in descending order
    Args:
        n (int): array size
        lo (int): minimum value of elements
        hi (int): maximum value of elements
        isInt (bool): is integer array or float
        distinct (bool): are values distinct
        seed (int | float | str | bytes | bytearray | None): array seed
    Returns:
        list[int]: array of n elements within [lo, hi]
    """

    if isInt:
        return sorted(rand_int_array(n, lo, hi, distinct, seed), reverse=True)
    else:
        return sorted(rand_float_array(n, lo, hi, seed), reverse=True)  # type: ignore


def rand_float_array(n: int, lo=0.0, hi=1.0, seed=None) -> list[float]:
    """
    Generate random float array
    Args:
        n (int): array size
        lo (int): minimum value of elements
        hi (int): maximum value of elements
        seed (int | float | str | bytes | bytearray | None): array seed
    Returns:
        list[int]: array of n float elements within [lo, hi]
    """

    random.seed(seed)

    a: list[float] = []
    while len(a) < n:
        a.append(lo + (hi - lo) * random.random())
    return a
