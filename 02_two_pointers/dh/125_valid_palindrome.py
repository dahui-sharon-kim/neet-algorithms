# https://leetcode.com/problems/valid-palindrome/description/
import collections
from typing import Deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for i in s:
            if (i.isalnum()):
                strs.append(i.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True