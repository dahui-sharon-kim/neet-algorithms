import sys
from typing import List
import time
import random


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        cache = {}

        def calculate(n):
            if n <= 1:
                return cost[n]
            if res := cache.get(n):
                return res
            res = cost[n] + min(calculate(n - 1), calculate(n - 2))
            cache[n] = res
            return res

        return calculate(n)

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        one, two = cost[0], cost[1]
        cost.append(0)

        for i in range(2, len(cost)):
            next = cost[i] + min(one, two)
            one = two
            two = next

        return min(one, two)


if __name__ == "__main__":
    cost = list(map(int, sys.argv[1:]))
    # cost = [random.randint(1, 100) for _ in range(100)]
    # print(cost)

    start = time.process_time()
    print(Solution().minCostClimbingStairs(cost))
    print(time.process_time() - start)

    start = time.process_time()
    print(Solution().minCostClimbingStairs2(cost))
    print(time.process_time() - start)
