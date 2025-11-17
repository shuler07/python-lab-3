import pytest
from src.errors import NonNaturalNumberError
from src.fibo import fibo, fibo_recursive


class TestFiboRecursive:

    def test_negative_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            fibo_recursive(-1)

        assert exc.errisinstance(NonNaturalNumberError)

    def test_float_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            fibo_recursive(3.14)  # type: ignore

        assert exc.errisinstance(NonNaturalNumberError)

    def test_success_1(self) -> None:
        assert fibo_recursive(5) == 5

    def test_success_2(self) -> None:
        assert fibo_recursive(10) == 55


class TestFibo:

    def test_negative_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            fibo(-1)

        assert exc.errisinstance(NonNaturalNumberError)

    def test_float_n(self) -> None:
        with pytest.raises(NonNaturalNumberError) as exc:
            fibo(3.14)  # type: ignore

        assert exc.errisinstance(NonNaturalNumberError)

    def test_success_1(self) -> None:
        assert fibo(5) == 5

    def test_success_2(self) -> None:
        assert fibo(10) == 55


def test_fibo_equals_fibo_recursive() -> None:
    assert fibo(228) == fibo_recursive(228)
