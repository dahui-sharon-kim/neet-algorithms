import sys
from typing import List
import itertools


class Solution:
    def valid(self, s: List[str]) -> bool:
        stack = []
        for p in s:
            if p == "(":
                stack.append(p)
            else:
                if not stack:
                    return False
                open = stack.pop()
                if open != "(":
                    return False
        if stack:
            return False
        return True

    def inefficientGenerateParenthesis(self, n: int) -> List[str]:
        pool = [*["(" for _ in range(n)], *[")" for _ in range(n)]]
        results = list(set(itertools.permutations(pool)))
        results = ["".join(x) for x in results if self.valid(list(x))]
        return results

    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def recur(stack: List[str], opens: int, closes: int):
            if not opens:
                results.append("".join(stack) + "".join([")" for _ in range(closes)]))
                return
            if opens <= closes:
                if opens:
                    recur([*stack, "("], opens - 1, closes)
                stack.append(")")
                recur(stack, opens, closes - 1)

        recur([], n, n)
        return results


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(Solution().generateParenthesis(n))
