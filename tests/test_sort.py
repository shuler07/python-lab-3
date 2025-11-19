import pytest
from src.sort import bubble_sort, quick_sort, counting_sort, radix_sort
from src.generators import rand_int_array
from src.errors import IrrationalListError


@pytest.fixture
def random_list():
    yield rand_int_array(10**3, -(10**7), 10**7, seed=3)


@pytest.fixture
def random_low_range_list():
    yield rand_int_array(10**3, -100, 100, seed=3)


@pytest.fixture
def str_list():
    yield ["hello", "world", "its", "not", "numbers"]


class TestBubbleSort:

    def test_with_key(self, random_list) -> None:
        assert bubble_sort(random_list, key=lambda x: -x) == sorted(
            random_list, key=lambda x: -x
        )

    def test_with_key_reversed(self, random_list) -> None:
        assert bubble_sort(random_list, key=lambda x: -(-(-x)), reverse=True) == sorted(
            random_list, key=lambda x: -(-(-x)), reverse=True
        )

    def test_with_wrong_key(self, random_list) -> None:
        with pytest.raises(TypeError) as exc:
            bubble_sort(random_list, key=lambda x: -len(x))  # type: ignore

        assert exc.errisinstance(TypeError)
        assert exc.match("Wrong method for object of this type")

    def test_with_wrong_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            bubble_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains non number objects")

    def test_with_cmp(self, random_list) -> None:
        def compare_func(a, b):
            return a - b

        assert bubble_sort(random_list, cmp=compare_func) == sorted(random_list)

    def test_with_key_and_cmp(self, random_list) -> None:
        def compare_func(a, b):
            return b - a

        assert bubble_sort(random_list, key=lambda x: x, cmp=compare_func) == sorted(
            random_list, reverse=True
        )


class TestQuickSort:

    def test_with_key(self, random_list) -> None:
        assert quick_sort(random_list, key=lambda x: -x) == sorted(
            random_list, key=lambda x: -x
        )

    def test_with_key_reversed(self, random_list) -> None:
        assert quick_sort(random_list, key=lambda x: -(-(-x)), reverse=True) == sorted(
            random_list, key=lambda x: -(-(-x)), reverse=True
        )

    def test_with_wrong_key(self, random_list) -> None:
        with pytest.raises(TypeError) as exc:
            quick_sort(random_list, key=lambda x: -len(x))  # type: ignore

        assert exc.errisinstance(TypeError)
        assert exc.match("Wrong method for object of this type")

    def test_with_wrong_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            quick_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains non number objects")

    def test_with_cmp(self, random_list) -> None:
        def compare_func(a, b):
            return a - b

        assert quick_sort(random_list, cmp=compare_func) == sorted(random_list)

    def test_with_key_and_cmp(self, random_list) -> None:
        def compare_func(a, b):
            return b - a

        assert quick_sort(random_list, key=lambda x: x, cmp=compare_func) == sorted(
            random_list, reverse=True
        )


class TestCountingSort:

    def test_simple(self, random_low_range_list) -> None:
        assert counting_sort(random_low_range_list) == sorted(random_low_range_list)

    def test_with_reverse(self, random_low_range_list) -> None:
        assert counting_sort(random_low_range_list, reverse=True) == sorted(
            random_low_range_list, reverse=True
        )

    def test_with_wrong_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            counting_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains non integer objects")

    def test_with_irrational_list(self, random_list) -> None:
        with pytest.raises(IrrationalListError) as exc:
            counting_sort(random_list)

        assert exc.errisinstance(IrrationalListError)
        assert exc.match(
            r"Irrational list for such type of sorting. Max range - 10 \*\* 6, got - \d+"
        )


class TestRadixSort:

    def test_simple(self, random_list) -> None:
        assert radix_sort(random_list) == sorted(random_list)

    def test_with_reverse(self, random_list) -> None:
        assert radix_sort(random_list, reverse=True) == sorted(
            random_list, reverse=True
        )

    def test_with_wrong_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            radix_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains non integer objects")

    def test_with_base_different_base(self, random_list) -> None:
        assert radix_sort(random_list, base=100) == sorted(random_list)
