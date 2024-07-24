import sys
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = list(s)
        if len(parentheses) % 2 != 0:
            return False

        opens = set(["{", "(", "["])
        closes = set(["}", ")", "]"])
        pairs = {
            "{": "}",
            "(": ")",
            "[": "]",
        }

        stack = deque()
        for i in parentheses:
            if i in opens:
                stack.append(i)
            if i in closes:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if pairs[top] != i:
                    return False

        if len(stack) != 0:
            return False
        return True


if __name__ == "__main__":
    s = sys.argv[1]
    print(Solution().isValid(s))
