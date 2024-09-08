from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()
        self.mins = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.mins[-1] if self.mins else val)
        self.mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(0)
    print(stack.getMin())
    print(stack.pop())
    print(stack.top())
    print(stack.getMin())
