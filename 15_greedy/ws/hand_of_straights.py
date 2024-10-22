from typing import List
import heapq
from collections import Counter


class Solution:
    def notGoodIsNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        heapq.heapify(hand)
        groups = [[] for _ in range(int(len(hand) / groupSize))]
        while hand:
            e = heapq.heappop(hand)
            inserted = False
            for group in groups:
                if len(group) == groupSize:
                    continue

                if not group or group[-1] + 1 == e:
                    group.append(e)
                    inserted = True

                if inserted:
                    break

            if not inserted:
                return False

        return True

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        h = list(count.keys())
        heapq.heapify(h)

        while h:
            first = h[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False

                count[i] -= 1

                if count[i] == 0:
                    if i != h[0]:
                        return False
                    heapq.heappop(h)
        return True
