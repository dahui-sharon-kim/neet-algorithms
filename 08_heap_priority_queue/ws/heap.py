from typing import List, Optional


class Heap:
    def __init__(self, numbers: List[int]) -> None:
        self.heap = numbers
        self.balance()

    def pop(self) -> Optional[int]:
        if not self.heap:
            return None

        result = self.heap.pop(0)
        self.heap.insert(0, self.heap.pop())
        self.balance()

        return result

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.balance()

    def balance(self):
        for index in range(len(self.heap) - 1, 0, -1):
            parent = index // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = (
                    self.heap[index],
                    self.heap[parent],
                )


if __name__ == "__main__":
    heap = Heap([7, 1, 6, 4, 5, 2])
    print(heap.heap)  # 1 7 2 4 5 6

    heap.push(3)
    print(heap.heap)  # 1 2 3 7 5 6 4

    print(heap.pop())  # 1
    print(heap.heap)  # 2 4 3 7 5 6
