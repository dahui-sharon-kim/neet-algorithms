# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def helper(i: int, current: str):
            if i == len(digits):
                res.append(current)
                return 
            for c in map_digit_to_char[digits[i]]:
                helper(i+1, current+c)
        
        if digits:
            helper(0, "")
        
        return res

print(Solution().letterCombinations("23")) # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
