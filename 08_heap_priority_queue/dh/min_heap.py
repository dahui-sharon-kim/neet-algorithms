from typing import Optional

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index: int) -> Optional[int]:
        return (index - 1) // 2 if index != 0 else None

    def left_child(self, index) -> Optional[int]:
        left = 2 * index + 1
        return left if left < len(self.heap) else None # heap list의 bounds를 넘어가면 None

    def right_child(self, index):
        right = 2 * index + 2
        return right if right < len(self.heap) else None # heap list의 bounds를 넘어가면 None

    def insert(self, key):
        self.heap.append(key)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, index):
        # Move the element at index up to its proper position.
        parent_idx = self.parent(index)
        while parent_idx is not None and self.heap[index] < self.heap[parent_idx]: # swap이 계속 진행되어야 하는 조건
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            # 원래 node의 부모로 올라감
            index = parent_idx
            parent_idx = self.parent(index)

    def extract_min(self):
        if not self.heap:
            raise IndexError("extract_min(): empty heap")
        min_elem = self.heap[0]
        last_elem = self.heap.pop()  # Remove the last element
        if self.heap:
            self.heap[0] = last_elem  # Move the last element to the root
            self.sift_down(0)         # Restore the heap property
        return min_elem

    def sift_down(self, index):
        # Move the element at index down to its proper position.
        # size = len(self.heap)
        while True:
            left_idx = self.left_child(index)
            right_idx = self.right_child(index)
            smallest = index

            if left_idx is not None and self.heap[left_idx] < self.heap[smallest]:
                smallest = left_idx
            if right_idx is not None and self.heap[right_idx] < self.heap[smallest]:
                smallest = right_idx

            if smallest != index:
                # Swap the current node with the smallest child.
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def peek_min(self):
        if not self.heap:
            raise IndexError("peek_min(): empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, iterable):
        # Build a heap from an iterable in O(n) time.
        self.heap = list(iterable)
        # Start from the last non-leaf node and sift down each node.
        for i in reversed(range(len(self.heap) // 2)):
            self.sift_down(i)

    def __str__(self):
        return str(self.heap)

# Example Usage:
if __name__ == "__main__":
    heap = MinHeap()
    elements = [5, 3, 8, 1, 2, 9]
    for elem in elements:
        heap.insert(elem)
        print(f"Inserted {elem}: Heap -> {heap}")

    print(f"Minimum element: {heap.peek_min()}")

    while not heap.is_empty():
        min_elem = heap.extract_min()
        print(f"Extracted {min_elem}: Heap -> {heap}")

    test_cases = [
        [],
        [10],
        [5, 3, 8, 1, 2, 9],
        [1, 2, 3, 4, 5, 6],
        [6, 5, 4, 3, 2, 1],
        [4, 4, 4, 4, 4],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
    ]

    for test in test_cases:
        print(f"{test} -> ", end="")
        heap.build_heap(test)
        print(heap)
