import sys
from typing import List


class Solution:
    operators = ["+", "-", "*", "/"]

    def operate(self, first: int, second: int, operator: str) -> int:
        if operator == "+":
            return first + second
        elif operator == "-":
            return first - second
        elif operator == "*":
            return first * second
        elif operator == "/":
            return int(float(first) / second)
        raise ValueError()

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while tokens:
            val = tokens.pop(0)
            if val not in self.operators:
                stack.append(int(val))
            else:
                second = stack.pop()
                first = stack.pop()
                res = self.operate(first, second, val)
                stack.append(res)

        return stack.pop()


if __name__ == "__main__":
    tokens = sys.argv[1:]
    print(Solution().evalRPN(tokens))
