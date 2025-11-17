import pytest
from src.sort import bubble_sort


@pytest.fixture
def unsorted_list():
    yield [
        1,
        2942,
        0.24,
        -0.51,
        103,
        1023912490,
        -123901294,
        0,
        0.0000001,
        -12412941294124,
        92,
        1,
    ]


@pytest.fixture
def str_list():
    yield ["hello", "world", "its", "not", "integers"]


class TestBubbleSort:

    def test_bubble_sort_with_key(self, unsorted_list) -> None:
        assert bubble_sort(unsorted_list, key=lambda x: -x) == sorted(
            unsorted_list, key=lambda x: -x
        )

    def test_bubble_sort_with_key_reversed(self, unsorted_list) -> None:
        assert bubble_sort(
            unsorted_list, key=lambda x: -(-(-x)), reverse=True
        ) == sorted(unsorted_list, key=lambda x: -(-(-x)), reverse=True)

    def test_bubble_sort_with_wrong_key(self, unsorted_list) -> None:
        with pytest.raises(TypeError) as exc:
            bubble_sort(unsorted_list, key=lambda x: -len(x))  # type: ignore

        assert exc.errisinstance(TypeError)
        assert exc.match("Wrong method for object of this type")

    def test_bubble_sort_with_wrong_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            bubble_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains non number objects")

    def test_bubble_sort_with_cmp(self, unsorted_list) -> None:
        def compare_func(a, b):
            return a - b

        assert bubble_sort(unsorted_list, cmp=compare_func) == sorted(unsorted_list)

    def test_bubble_sort_with_key_and_cmp(self, unsorted_list) -> None:
        def compare_func(a, b):
            return b - a

        assert bubble_sort(unsorted_list, key=lambda x: x, cmp=compare_func) == sorted(
            unsorted_list, reverse=True
        )
