class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char not in mapping:
                stack.append(char)
            elif not stack or mapping[char] != stack.pop():
                return False
        return len(stack) == 0
