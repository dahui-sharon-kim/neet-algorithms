import sys


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {
            0: 0,
            1: 1,
            2: 2,
        }

        def calculate(n: int) -> int:
            if res := memo.get(n):
                return res
            memo[n] = calculate(n - 2) + calculate(n - 1)
            return memo[n]

        return calculate(n)


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(Solution().climbStairs(n))
