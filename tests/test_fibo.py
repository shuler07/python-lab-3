import pytest
from src.errors import NonNaturalNumberError
from src.fibonacci import fibonacci, fibonacci_recursive


class TestFibonacciRecursive:

    def test_negative_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            fibonacci_recursive(-1)

        assert exc.errisinstance(NonNaturalNumberError)

    def test_float_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            fibonacci_recursive(3.14)  # type: ignore

        assert exc.errisinstance(NonNaturalNumberError)

    def test_success_1(self) -> None:
        assert fibonacci_recursive(5) == 5

    def test_success_2(self) -> None:
        assert fibonacci_recursive(10) == 55


class TestFibonacci:

    def test_negative_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            fibonacci(-1)

        assert exc.errisinstance(NonNaturalNumberError)

    def test_float_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            fibonacci(3.14)  # type: ignore

        assert exc.errisinstance(NonNaturalNumberError)

    def test_success_1(self) -> None:
        assert fibonacci(5) == 5

    def test_success_2(self) -> None:
        assert fibonacci(10) == 55


def test_fibonacci_equals_fibonacci_recursive() -> None:
    assert fibonacci(228) == fibonacci_recursive(228)
