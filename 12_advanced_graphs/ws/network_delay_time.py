from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append([v, t])

        heap = [[0, k]]
        visit = set()
        res = 0
        while heap:
            t, i = heapq.heappop(heap)
            if i in visit:
                continue
            visit.add(i)
            res = t

            for i2, t2 in adj[i]:
                if i2 not in visit:
                    heapq.heappush(heap, [t + t2, i2])

        return res if len(visit) == n else -1
