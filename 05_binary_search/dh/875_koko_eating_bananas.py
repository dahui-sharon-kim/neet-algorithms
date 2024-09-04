# https://leetcode.com/problems/koko-eating-bananas/

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def canAssign(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                if hours > h:
                    return False
            return True

        while left < right:
            mid = (left + right) // 2
            if canAssign(mid):
                right = mid
            else:
                left = mid + 1
        return left

print(Solution().minEatingSpeed([3, 6, 7, 11], 8))