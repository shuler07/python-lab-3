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
    Limits: max(*a*) - min(*a*) <= 10 ** 6\\
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
        # Validate first values of _min and _max is integer
        if isinstance(_a[0], int):
            _min = _max = _a[0]
        else:
            raise TypeError("List contains non integer objects")

        try:
            for _el in _a[1:]:
                _min = min(_min, _el)
                _max = max(_max, _el)
        except TypeError:
            # If any of elements in list are not integer, min function will raise TypeError
            raise TypeError("List contains non integer objects")

        return (_min, _max)

    el_min, el_max = _get_min_max_values(a)

    # Calculate range of list
    el_range = el_max - el_min + 1
    if el_range > 10**6:
        raise IrrationalListError(el_range)

    # Init list of needed size
    counts = [0] * el_range
    for el in a:
        counts[el - el_min] += 1

    # Create reversed range if list should be reversed
    _range = range(el_range) if not reverse else range(el_range - 1, -1, -1)

    # Fill sorted list
    a_sorted = []
    for i in _range:
        a_sorted.extend([i + el_min for _ in range(counts[i])])

    return a_sorted


def radix_sort(
    a: list[int],
    base: int = 10,
    reverse: bool = False,
) -> list[int]:
    """
    Radix sort list *a*\\
    It is rational to use this sort if max len of *a* elements is not big\\
    **Time complexity: O(nk), k = max len of *a* elements**
    Args:
        a (list[int]): list
        reverse (bool): is sorting reversed
    Returns:
        list[int]: sorted list
    Raises:
        TypeError: if list contains non integer objects
    """

    def _radix_sort(_a: list[int], _i: int, _c: int) -> list[int]:
        "Recursive radix sort until _i == 0"
        if _i == 0:
            return _a

        # Calculate values to cut _c digit of number from end
        _lcut, _rcut = base**_c, base ** (_c - 1)

        _ranks: list[list[int]] = [[] for _ in range(base)]
        for _el in _a:
            _ranks[_el % _lcut // _rcut].append(_el)

        _new_a = []
        step = 1 if not reverse else -1
        for _arr in _ranks[::step]:
            _new_a.extend(_arr)

        return _radix_sort(_new_a, _i - 1, _c + 1)

    # Divide by sign of number
    a_neg, a_pos = [], []
    try:
        for el in a:
            a_pos.append(el) if el >= 0 else a_neg.append(-el)
    except TypeError:
        raise TypeError("List contains non integer objects")

    # After sorting negative numbers as positive we need to return minus to it and reverse list
    a_neg_sorted = _radix_sort(a_neg, len(str(max(a_neg))), 1)
    a_neg_sorted = [-el for el in a_neg_sorted[::-1]]

    a_pos_sorted = _radix_sort(a_pos, len(str(max(a_pos))), 1)

    # Merging back to signle list
    return (
        [*a_neg_sorted, *a_pos_sorted]
        if not reverse
        else [*a_pos_sorted, *a_neg_sorted]
    )


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]: ...


def heap_sort(a: list[int]) -> list[int]: ...
