from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        total = 0
        for i, v in enumerate(zip(gas, cost)):
            total += v[0] - v[1]
            if total < 0:
                total = 0
                start = i + 1
        return start
