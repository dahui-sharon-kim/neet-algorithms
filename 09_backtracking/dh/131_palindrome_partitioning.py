# https://leetcode.com/problems/palindrome-partitioning/
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def dfs(i):
            if i >= len(s):
                print(f"dfs({i}), End")
                res.append(temp.copy())
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j): # s[i:j+1]이 회문인지 체크
                    temp.append(s[i:j+1])
                    dfs(j+1) # 회문이면 j+1부터 backtrack
                    temp.pop()
        
        dfs(0)
        return res

    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

print(Solution().partition("aab")) # [["a","a","b"],["aa","b"]]
print(Solution().partition("a")) # [["a"]]
