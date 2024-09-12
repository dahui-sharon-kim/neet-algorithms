# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0
        letters = defaultdict(int)

        for right in range(len(s)):
            letters[s[right]] += 1

            while letters[s[right]] > 1:
                letters[s[left]] -= 1
                left += 1

            maximum = max(maximum, right-left+1)
            print(letters)

        return maximum

print(Solution().lengthOfLongestSubstring("abcabcbb"))
