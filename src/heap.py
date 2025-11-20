from src.validation import validate_number, NUM


class Heap:
    """
    Structure that holds lowest element at the top of list (binary tree)\\
    If root = a[i], then its left child = a[i\\*2+1], right child = a[i\\*2+2]\\
    To store biggest element at the top of list, provide reversed=True
    Raises:
        TypeError: if list contains invalid objects
    """

    def __init__(self, a: list[NUM] = [], reversed: bool = False) -> None:
        heap = []
        for el in a:
            validate_number(el)
            heap.append(el)
        self.heap = heap  # type: ignore
        self.reversed = reversed

    def __compare__(self, el1: NUM, el2: NUM):
        if self.reversed:
            return el1 > el2
        return el1 < el2

    def heapify(self, n: int, ind: int) -> None:
        """
        Change the *ind* root if it is not valid
        Args:
            n (int): count of elements to heap
            ind (int): root ind in the heap
        """

        left, right = ind * 2 + 1, ind * 2 + 2
        largest = ind

        # Checking is left child of <ind> root exists and less (bigger) than <ind> root
        if left < n and self.__compare__(self.heap[left], self.heap[largest]):
            largest = left

        # Checking is right child of <ind> root exists and less (bigger) than <ind> root
        if right < n and self.__compare__(self.heap[right], self.heap[largest]):
            largest = right

        # If there child less (bigger) than root, swapping them and repeating it until biggest (least) child on bottom of heap
        if largest != ind:
            self.heap[largest], self.heap[ind] = self.heap[ind], self.heap[largest]

            self.heapify(n, largest)

    @staticmethod
    def create(a: list[NUM], reversed: bool = False) -> "Heap":
        heap = Heap(a, reversed)
        n = len(a)

        # Making heap from by heapifying every possible element
        for i in range(n // 2 - 1, -1, -1):
            heap.heapify(n, i)

        return heap
