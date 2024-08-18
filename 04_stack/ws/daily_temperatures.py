import sys
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, index = stack.pop()
                results[index] = i - index
            stack.append((t, i))

        return results


if __name__ == "__main__":
    temps = list(map(int, sys.argv[1:]))
    print(Solution().dailyTemperatures(temps))
