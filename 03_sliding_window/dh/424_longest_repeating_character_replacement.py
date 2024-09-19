# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = defaultdict(int)
        maximum = 0
        left = 0
        maximum_length = 0

        for right in range(len(s)):
            letters[s[right]] += 1
            maximum = max(maximum, letters[s[right]])

            if (right - left + 1) - maximum > k:
                if letters[s[left]] > 1:
                    defaultdict[s[left]] -= 1
                else:
                    del defaultdict[s[left]]
                left += 1

            maximum_length = max(maximum_length, right - left + 1) # 어렵다..
        

