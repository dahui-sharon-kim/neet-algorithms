from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        number_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        subset = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(subset))
                return

            for c in number_map[digits[i]]:
                subset.append(c)
                dfs(i + 1)
                subset.pop()

        dfs(0)
        return res
