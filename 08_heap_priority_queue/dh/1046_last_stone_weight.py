from typing import List
import heapq

# Max-Heap

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones] # max heap 구현을 위해 마이너스로 바꿔서 넣음
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first != second:
                heapq.heappush(max_heap, -(first - second))
            
        return -max_heap[0] if max_heap else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])) # 1
print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1, 1])) # 0
