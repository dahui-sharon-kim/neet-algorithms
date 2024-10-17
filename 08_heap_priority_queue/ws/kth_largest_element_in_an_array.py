from typing import List
import heapq


# Or use quick sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [n * -1 for n in nums]
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)
        return -1 * heapq.heappop(nums)
