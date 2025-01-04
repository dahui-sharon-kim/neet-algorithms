from collections import defaultdict
import heapq
from typing import List


class Solution:
    def calculateDist(self, one, two):
        return abs(one[0] - two[0]) + abs(one[1] - two[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                dist = self.calculateDist(p1, p2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        heap = [[0, 0]]
        while len(visit) < n:
            cost, i = heapq.heappop(heap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for adjCost, adjIndex in adj[i]:
                if adjIndex not in visit:
                    heapq.heappush(heap, [adjCost, adjIndex])

        return res
