# https://leetcode.com/problems/hand-of-straights/

from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        count = Counter(hand)

        for i in hand:
            print(count)
            if count[i] > 0:
                for j in range(groupSize):
                    if count[i+j] > 0:
                        count[i+j] -= 1
                    else:
                        return False
        return True

print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3))