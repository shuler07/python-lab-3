from typing import Callable, TypeVar
from functools import cmp_to_key
from sys import setrecursionlimit
from src.validation import validate_number
from src.errors import IrrationalListError


NUM = TypeVar("NUM", int, float)


def get_key_function(
    key: Callable[[NUM], NUM] | None, cmp: Callable[[NUM, NUM], NUM] | None
) -> Callable[[NUM], NUM]:
    """
    Check is cmp function present and return key function from cmp, otherwise check is key function present and return it.\\
    If cmp and key functions not present, returns default ascending sort key function
    Args:
        key (Callable[[int | float], int | float]): sorting key function
        cmp (Callable[[int | float, int | float], int | float]): sorting cmp function
    Returns:
        Callable[[int | float], int | float]: sorting key function
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


def get_validated_list_copy(a: list[NUM]) -> list[NUM]:
    """
    Validate every element of list is number and make copy of list
    Args:
        a (list[int | float]): list
    Returns:
        list[int | float]: shallow copied list of numbers
    Raises:
        TypeError: if non number found in list
    """
    a_sorted = []
    for elem in a:
        validate_number(elem)
        a_sorted.append(elem)
    return a_sorted


def bubble_sort(
    a: list[NUM],
    key: Callable[[NUM], NUM] | None = None,
    cmp: Callable[[NUM, NUM], NUM] | None = None,
    reverse: bool = False,
) -> list[NUM]:
    """
    Bubble sort list *a*\\
    If key and cmp both are present, cmp will replace key function\\
    **Time complexity: O(n^2)**
    Args:
        a (list[int | float]): list
        key (Callable[[int | flaot], int | float]): sorting key function
        cmp (Callable[[int | float, int | float], int | float]): sorting compare function
        reverse (bool): is sorting reversed
    Returns:
        list[int | float]: sorted list
    Raises:
        TypeError: if list contains non number objects or key / cmp functions use wrong methods
    """

    key = get_key_function(key=key, cmp=cmp)
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
    a: list[NUM],
    key: Callable[[NUM], NUM] | None = None,
    cmp: Callable[[NUM, NUM], NUM] | None = None,
    reverse: bool = False,
) -> list[NUM]:
    """
    Quick sort list *a*\\
    If key and cmp both are present, cmp will replace key function\\
    **Time complexity: from O(n*log n) to O(n^2)**
    Args:
        a (list[int | float]): list
        key (Callable[[int | float], int | float]): sorting key function
        cmp (Callable[[int | float, int | float], int | float]): sorting compare function
        reverse (bool): is sorting reversed
    Returns:
        list[int | float]: sorted list
    Raises:
        TypeError: if list contains non number objects or key / cmp functions use wrong methods
    """

    key = get_key_function(key=key, cmp=cmp)
    a_sorted = get_validated_list_copy(a)

    # to avoid raising exception
    setrecursionlimit(max(1000, len(a)))

    def _quick_sort(_a: list[NUM]) -> list[NUM]:
        if len(_a) == 0:
            return []
        _less, _pivot, _more = [], _a[-1], []
        for _el in _a[:-1]:
            if not reverse:
                _less.append(_el) if key(_el) < key(_pivot) else _more.append(_el)
            else:
                _less.append(_el) if key(_el) > key(_pivot) else _more.append(_el)

        return [*_quick_sort(_less), _pivot, *_quick_sort(_more)]  # type: ignore

    try:
        return _quick_sort(a_sorted)
    except TypeError:
        raise TypeError("Wrong method for object of this type")


def counting_sort(
    a: list[int],
    reverse: bool = False,
) -> list[int]:
    """
    Count sort list *a*\\
    It is rational to use this sort if range of *a* less than list size\\
    Limits: range of elements <= 10 ** 6\\
    **Time complexity: O(n+k), k = range of *a***
    Args:
        a (list[int]): list
        reverse (bool): is sorting reversed
    Returns:
        list[int]: sorted list
    Raises:
        TypeError: if list contains non integer objects
    """

    def _get_min_max_values(_a: list[int]) -> tuple[int, int]:
        if isinstance(_a[0], int):
            _min = _max = _a[0]
        else:
            raise TypeError("List contains non integer objects")

        try:
            for _el in _a[1:]:
                _min = min(_min, _el)
                _max = max(_max, _el)
        except TypeError:
            raise TypeError("List contains non integer objects")
        return (_min, _max)

    el_min, el_max = _get_min_max_values(a)
    el_range = el_max - el_min + 1

    if el_range > 10**6:
        raise IrrationalListError(el_range)

    counts = [0] * el_range

    for el in a:
        counts[el - el_min] += 1

    a_sorted = []
    _range = range(el_range) if not reverse else range(el_range - 1, -1, -1)

    for i in _range:
        a_sorted.extend([i + el_min for _ in range(counts[i])])

    return a_sorted


def radix_sort(a: list[int], base: int = 10) -> list[int]: ...


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]: ...


def heap_sort(a: list[int]) -> list[int]: ...
