import sys
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate(piles: List[int], k: int) -> int:
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total

        result = max(piles)
        low, high = 1, max(piles)
        while high >= low:
            k = low + (high - low) // 2

            hour = calculate(piles, k)
            if hour > h:
                low = k + 1
            elif hour < h:
                result = min(result, k)
                high = k - 1
            else:
                return k

        return result


if __name__ == "__main__":
    h = int(sys.argv[1])
    piles = list(map(int, sys.argv[2:]))
    print(Solution().minEatingSpeed(piles, h))
