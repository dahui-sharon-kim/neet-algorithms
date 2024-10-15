# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
    
print(Solution().findKthLargest([3,2,1,5,6,4],2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4))