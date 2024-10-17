from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            dist = x**2 + y**2
            h.append((dist, x, y))

        heapq.heapify(h)

        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(h)
            res.append([x, y])
        return res
