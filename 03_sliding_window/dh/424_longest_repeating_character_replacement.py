# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        letters = defaultdict(int)

        if (len(s) == 1):
            return 1

        for right in range(len(s)):
            print(s[right])
            letters[s[right]] += 1
            while letters[s[right]] > 1:
                letters[s[left]] -= 1
                if letters[s[left]] == 0:
                    del letters[s[left]]
                left += 1
            ans = max(ans, right-left+1)

        return ans
