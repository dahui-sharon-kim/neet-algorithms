from typing import List
import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        h = [-1 * t for t in counter.values()]
        heapq.heapify(h)

        spaces = -1 * heapq.heappop(h) - 1
        idles = spaces * n
        while idles > 0 and h:
            others = -1 * heapq.heappop(h)
            mins = min(spaces, others)
            idles = max(idles - mins, 0)
        return len(tasks) + idles
