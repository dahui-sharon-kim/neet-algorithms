import sys
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ordered = []
        heapq.heapify(ordered)

        for s in stones:
            heapq.heappush(ordered, s * -1)

        while ordered:
            one = heapq.heappop(ordered)
            if not ordered:
                return one * -1

            two = heapq.heappop(ordered)

            if one < two:
                heapq.heappush(ordered, one - two)

        return 0


if __name__ == "__main__":
    stones = list(map(int, sys.argv[1:]))

    print(Solution().lastStoneWeight(stones))
