# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for x,y in points:
            distance = -(x**2 + y**2)
            heapq.heappush(heap, (distance, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point for _, point in heap]
    
print(Solution().kClosest([[1,3],[-2,2]], 1))
print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))