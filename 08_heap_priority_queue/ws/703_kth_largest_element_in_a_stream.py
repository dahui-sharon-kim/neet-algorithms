import sys
from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.smallers = []
        heapq.heapify(self.smallers)
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for num in nums[k:]:
            out = num
            if num > self.heap[0]:
                out = heapq.heappushpop(self.heap, num)
            heapq.heappush(self.smallers, out)

    def add(self, val: int) -> int:
        if not self.heap:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        if val <= self.heap[0]:
            heapq.heappush(self.smallers, val)
        elif len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            out = heapq.heappushpop(self.heap, val)
            heapq.heappush(self.smallers, out)
        return self.heap[0]


if __name__ == "__main__":
    k = int(sys.argv[1])
    init_len = int(sys.argv[2])
    stream = list(map(int, sys.argv[3 : 3 + init_len]))
    adds = list(map(int, sys.argv[3 + init_len :]))

    results = []
    kth = KthLargest(k, stream)
    for i in adds:
        results.append(kth.add(i))

    print(["null", *results])
