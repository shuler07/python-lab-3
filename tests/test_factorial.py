import pytest
from src.errors import NonNaturalNumberError
from src.factorial import factorial, factorial_recursive


class TestFactorialRecursive:

    def test_negative_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            factorial_recursive(-1)

        assert exc.errisinstance(NonNaturalNumberError)

    def test_float_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            factorial_recursive(3.14)  # type: ignore

        assert exc.errisinstance(NonNaturalNumberError)

    def test_success_1(self) -> None:
        assert factorial_recursive(5) == 2 * 3 * 4 * 5

    def test_success_2(self) -> None:
        assert factorial_recursive(10) == 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10


class TestFactorial:

    def test_negative_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            factorial(-1)

        assert exc.errisinstance(NonNaturalNumberError)

    def test_float_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            factorial(3.14)  # type: ignore

        assert exc.errisinstance(NonNaturalNumberError)

    def test_success_1(self) -> None:
        assert factorial(5) == 2 * 3 * 4 * 5

    def test_success_2(self) -> None:
        assert factorial(10) == 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10


def test_factorial_equals_factorial_recursive() -> None:
    assert factorial(228) == factorial_recursive(228)
