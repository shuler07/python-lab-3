import pytest
from src.sort import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort
from src.generators import rand_int_array, rand_float_array
from src.errors import IrrationalListError


@pytest.fixture
def int_list():
    yield rand_int_array(10**3, -(10**7), 10**7, seed=3)


@pytest.fixture
def float_list():
    yield rand_float_array(10**3, -(10**7), 10**7, seed=3)


@pytest.fixture
def random_low_range_list():
    yield rand_int_array(10**3, -100, 100, seed=3)


@pytest.fixture
def str_list():
    yield ["hello", "world", "its", "not", "numbers"]


class TestBubbleSort:

    def test_with_key(self, int_list) -> None:
        assert bubble_sort(int_list, key=lambda x: -x) == sorted(
            int_list, key=lambda x: -x
        )

    def test_with_key_reversed(self, int_list) -> None:
        assert bubble_sort(int_list, key=lambda x: -(-(-x)), reverse=True) == sorted(
            int_list, key=lambda x: -(-(-x)), reverse=True
        )

    def test_with_float(self, float_list) -> None:
        assert bubble_sort(float_list) == sorted(float_list)

    def test_with_wrong_key(self, int_list) -> None:
        with pytest.raises(TypeError) as exc:
            bubble_sort(int_list, key=lambda x: -len(x))  # type: ignore

        assert exc.errisinstance(TypeError)
        assert exc.match("Wrong method for object of this type")

    def test_with_str_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            bubble_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains non number objects")

    def test_with_cmp(self, int_list) -> None:
        def compare_func(a, b):
            return a - b

        assert bubble_sort(int_list, cmp=compare_func) == sorted(int_list)

    def test_with_key_and_cmp(self, int_list) -> None:
        def compare_func(a, b):
            return b - a

        assert bubble_sort(int_list, key=lambda x: x, cmp=compare_func) == sorted(
            int_list, reverse=True
        )


class TestQuickSort:

    def test_with_key(self, int_list) -> None:
        assert quick_sort(int_list, key=lambda x: -x) == sorted(
            int_list, key=lambda x: -x
        )

    def test_with_key_reversed(self, int_list) -> None:
        assert quick_sort(int_list, key=lambda x: -(-(-x)), reverse=True) == sorted(
            int_list, key=lambda x: -(-(-x)), reverse=True
        )

    def test_with_float(self, float_list) -> None:
        assert quick_sort(float_list) == sorted(float_list)

    def test_with_wrong_key(self, int_list) -> None:
        with pytest.raises(TypeError) as exc:
            quick_sort(int_list, key=lambda x: -len(x))  # type: ignore

        assert exc.errisinstance(TypeError)
        assert exc.match("Wrong method for object of this type")

    def test_with_str_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            quick_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains non number objects")

    def test_with_cmp(self, int_list) -> None:
        def compare_func(a, b):
            return a - b

        assert quick_sort(int_list, cmp=compare_func) == sorted(int_list)

    def test_with_key_and_cmp(self, int_list) -> None:
        def compare_func(a, b):
            return b - a

        assert quick_sort(int_list, key=lambda x: x, cmp=compare_func) == sorted(
            int_list, reverse=True
        )


class TestCountingSort:

    def test_simple(self, random_low_range_list) -> None:
        assert counting_sort(random_low_range_list) == sorted(random_low_range_list)

    def test_with_reverse(self, random_low_range_list) -> None:
        assert counting_sort(random_low_range_list, reverse=True) == sorted(
            random_low_range_list, reverse=True
        )

    def test_with_float(self, float_list) -> None:
        with pytest.raises(TypeError) as exc:
            counting_sort(float_list) == sorted(float_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains invalid objects")

    def test_with_str_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            counting_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains invalid objects")

    def test_with_irrational_list(self, int_list) -> None:
        with pytest.raises(IrrationalListError) as exc:
            counting_sort(int_list)

        assert exc.errisinstance(IrrationalListError)
        assert exc.match(
            r"Irrational list for such type of sorting. Max range - 10 \*\* 6, got - \d+"
        )


class TestRadixSort:

    def test_simple(self, int_list) -> None:
        assert radix_sort(int_list) == sorted(int_list)

    def test_with_reverse(self, int_list) -> None:
        assert radix_sort(int_list, reverse=True) == sorted(int_list, reverse=True)

    def test_with_float(self, float_list) -> None:
        with pytest.raises(TypeError) as exc:
            radix_sort(float_list) == sorted(float_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains invalid objects")

    def test_with_str_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            radix_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains invalid objects")

    def test_with_base_different_base(self, int_list) -> None:
        assert radix_sort(int_list, base=100) == sorted(int_list)


class TestBucketSort:

    def test_simple(self, int_list) -> None:
        assert bucket_sort(int_list) == sorted(int_list)

    def test_with_reverse(self, int_list) -> None:
        assert bucket_sort(int_list, reverse=True) == sorted(int_list, reverse=True)

    def test_with_float(self, float_list) -> None:
        assert bucket_sort(float_list) == sorted(float_list)

    def test_with_str_list(self, str_list) -> None:
        with pytest.raises(TypeError) as exc:
            bucket_sort(str_list)

        assert exc.errisinstance(TypeError)
        assert exc.match("List contains invalid objects")
