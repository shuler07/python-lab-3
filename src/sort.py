from typing import Callable
from functools import cmp_to_key
from src.validation import validate_number


def get_key_from_key_and_cmp(
    key: Callable[[int], int] | None, cmp: Callable[[int, int], int] | None
) -> Callable[[int], int]:
    """
    Check is cmp function present and return key function from cmp, otherwise check is key function present and return it.
    If cmp and key functions not present, returns default ascending sort key function
    Args:
        key (Callable[[int], int]): sorting key function
        cmp (Callable[[int, int], int]): sorting cmp function
    Returns:
        Callable[[int], int]: sorting key function
    """
    # If cmp is present, returns key function from it
    if cmp is not None:
        return cmp_to_key(cmp)  # type: ignore
    else:
        if (
            key is None
        ):  # If key is ommited, returns default ascending sort key function
            return lambda x: x
        return key  # If key is present, returns it


def get_validated_list_copy(a: list[int]) -> list[int]:
    """
    Validate every element of list is number and make copy of list
    Args:
        a (list[int]): list
    Returns:
        list[int]: shallow copied list of numbers
    Raises:
        TypeError: if non number found in list
    """
    a_sorted = []
    for elem in a:
        validate_number(elem)
        a_sorted.append(elem)
    return a_sorted


def bubble_sort(
    a: list[int],
    key: Callable[[int], int] | None = None,
    cmp: Callable[[int, int], int] | None = None,
    reverse: bool = False,
) -> list[int]:
    """
    Bubble sort list 'a' for O(n^2)
    If key and cmp both are present, cmp will replace key function
    Args:
        a (list[int]): list
        key (Callable[[T], int]): sorting key function
        cmp (Callable[[T, T], int]): sorting compare function
        reverse (bool): is sorting reversed
    Returns:
        list[int]: sorted list
    """

    key = get_key_from_key_and_cmp(key=key, cmp=cmp)
    a_sorted = get_validated_list_copy(a)

    try:
        end = len(a) - 1
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


def quick_sort(
    a: list[int],
    key: Callable[[int], int] | None = None,
    cmp: Callable[[int, int], int] | None = None,
    reverse: bool = False,
) -> list[int]:
    """
    Quick sort list 'a' for O(n*log n)
    If key and cmp both are present, cmp will replace key function
    Args:
        a (list[int]): list
        key (Callable[[T], int]): sorting key function
        cmp (Callable[[T, T], int]): sorting compare function
        reverse (bool): is sorting reversed
    Returns:
        list[int]: sorted list
    """

    key = get_key_from_key_and_cmp(key=key, cmp=cmp)
    a_sorted = get_validated_list_copy(a)

    def _quick_sort(_a: list[int]):
        if len(_a) == 0:
            return []
        _less, _pivot, _more = [], _a[-1], []
        for _el in _a[:-1]:
            if not reverse:
                _less.append(_el) if key(_el) < key(_pivot) else _more.append(_el)
            else:
                _less.append(_el) if key(_el) > key(_pivot) else _more.append(_el)

        return [*_quick_sort(_less), _pivot, *_quick_sort(_more)]

    try:
        return _quick_sort(a_sorted)
    except TypeError:
        raise TypeError("Wrong method for object of this type")


def counting_sort(a: list[int]) -> list[int]: ...


def radix_sort(a: list[int], base: int = 10) -> list[int]: ...


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]: ...


def heap_sort(a: list[int]) -> list[int]: ...
