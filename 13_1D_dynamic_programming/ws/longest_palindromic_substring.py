class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxlen = 0

        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if maxlen < r - l + 1:
                    res = s[l : r + 1]
                    maxlen = max(maxlen, len(res))
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if maxlen < r - l + 1:
                    res = s[l : r + 1]
                    maxlen = max(maxlen, len(res))
                l -= 1
                r += 1
        return res
