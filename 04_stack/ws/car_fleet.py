import sys
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        stack = []

        for p, s in ps:
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


if __name__ == "__main__":
    target = int(sys.argv[1])
    n = int(sys.argv[2])
    position = list(map(int, sys.argv[3 : 3 + n]))
    speed = list(map(int, sys.argv[3 + n :]))
    print(Solution().carFleet(target, position, speed))
