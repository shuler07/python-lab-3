class NonNaturalNumberError(Exception):
    def __init__(self, non_natural: int) -> None:
        super().__init__(f"Natural numbers allowed only. Got: {non_natural}")


class IrrationalListError(Exception):
    def __init__(self, size: int) -> None:
        super().__init__(
            f"Irrational list for such type of sorting. Max range - 10 ** 6, got - {size}"
        )
