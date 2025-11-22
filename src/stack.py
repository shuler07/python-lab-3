from src.errors import EmptyStackError


class Stack:
    """
    Structure that represents stack
    It allows you to push new value, pop last value, get last value, get min value and check is stack empty
    Args:
        a (list[int | float]): list to create stack from
    Raises:
        EmptyStackError: if trying to get element from empty stack
    """

    def __init__(self, a: list[int | float] = []) -> None:
        self._stack: list[int | float] = a.copy()
        self._mins: list[int | float] = []

        if len(a) != 0:
            self.__fill_mins__()

    def __fill_mins__(self):
        self._mins.append(self._stack[0])
        for el in self._stack[1:]:
            self._mins.append(min(self._mins[-1], el))

    def push(self, x: int | float) -> None:
        "Add *x* value to the end of stack"
        self._stack.append(x)
        if len(self._mins) != 0:
            self._mins.append(min(self._mins[-1], x))
        else:
            self._mins.append(x)

    def pop(self) -> int | float:
        "Remove last value from stack"
        try:
            self._mins.pop()
            return self._stack.pop()
        except IndexError:
            raise EmptyStackError()

    def peek(self) -> int | float:
        "Get last value from stack"
        try:
            return self._stack[-1]
        except IndexError:
            raise EmptyStackError()

    def is_empty(self) -> bool:
        "Check is stack empty"
        return len(self) == 0

    def __len__(self) -> int:
        return len(self._stack)

    def min(self) -> int | float:
        "Get min value of stack"
        if len(self._mins) != 0:
            return self._mins[-1]
        else:
            raise EmptyStackError()
