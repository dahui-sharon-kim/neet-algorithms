# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        ans = ""
        ansLen = 0
        for i in range(length):
            l = r = i
            while l >= 0 and r < length and s[l] == s[r]:
                if r-l+1 > ansLen:
                    ans = s[l:r+1]
                    ansLen = r-l+1
                l, r = l-1, r+1

            l, r = i, i+1
            while l >= 0 and r < length and s[l] == s[r]:
                if r-l+1 > ansLen:
                    ans = s[l:r+1]
                    ansLen = r-l+1
                l, r = l-1, r+1
            
        
        return ans
