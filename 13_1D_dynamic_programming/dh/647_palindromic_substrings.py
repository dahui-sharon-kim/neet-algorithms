# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        length = len(s)

        ans = 0
        for i in range(length):
            l = r = i
            while l >= 0 and r < length and s[l] == s[r]:
                ans += 1
                l, r = l-1, r+1

            l, r = i, i+1
            while l >= 0 and r < length and s[l] == s[r]:
                ans += 1
                l, r = l-1, r+1
        
        return ans

print(Solution().countSubstrings("abc")) # 3
print(Solution().countSubstrings("aaa")) # 6
