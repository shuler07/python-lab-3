from typing import Callable
from functools import cmp_to_key
from src.validation import validate_number


def bubble_sort(
    a: list[int],
    key: Callable[[int], int] | None = None,
    cmp: Callable[[int, int], int] | None = None,
    reverse: bool = False,
) -> list[int]:
    """
    Bubble sort list a for O(n^2)
    If key and cmp both are present, cmp will replace key function
    Args:
        a (list[int]): list to sort
        key (Callable[[T], int]): key function used for custom sorting
        cmp (Callable[[T, T], int]): compare function user for custom sorting
        reverse (bool): is sorting reversed
    Returns:
        list[int]: sorted list
    """

    # If key is ommited, use value as it
    if key is None:
        key = lambda x: x

    if cmp is not None:
        key = cmp_to_key(cmp)  # type: ignore

    # Make shallow copy of list and validate numbers
    a_sorted = []
    for elem in a:
        validate_number(elem)
        a_sorted.append(elem)

    end = len(a) - 1

    try:
        while end > 0:
            for i in range(end):
                if not reverse:
                    if key(a_sorted[i]) > key(a_sorted[i + 1]):
                        a_sorted[i], a_sorted[i + 1] = a_sorted[i + 1], a_sorted[i]
                else:
                    if key(a_sorted[i]) < key(a_sorted[i + 1]):
                        a_sorted[i], a_sorted[i + 1] = a_sorted[i + 1], a_sorted[i]
            end -= 1
    except TypeError:
        raise TypeError("Wrong method for object of this type")

    return a_sorted


def quick_sort(a: list[int]) -> list[int]: ...


def counting_sort(a: list[int]) -> list[int]: ...


def radix_sort(a: list[int], base: int = 10) -> list[int]: ...


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]: ...


def heap_sort(a: list[int]) -> list[int]: ...
