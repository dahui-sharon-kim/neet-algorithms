from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(s):
                res.append(subset.copy())
                return
            for j in range(i, len(s)):
                if is_palin(s[i : j + 1]):
                    subset.append(s[i : j + 1])
                    dfs(j + 1)
                    subset.pop()

        def is_palin(s: str) -> bool:
            start, end = 0, len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        dfs(0)
        return res
