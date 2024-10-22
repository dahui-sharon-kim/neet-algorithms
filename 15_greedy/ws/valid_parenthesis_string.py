class Solution:
    def checkValidString(self, s: str) -> bool:
        l, r = 0, 0

        for c in s:
            if c == "(":
                l, r = l + 1, r + 1
            elif c == ")":
                l, r = l - 1, r - 1
            else:
                l, r = l - 1, r + 1
            if r < 0:
                return False
            if l < 0:
                l = 0
        return l == 0
