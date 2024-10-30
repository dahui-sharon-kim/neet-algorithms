# https://leetcode.com/problems/valid-parenthesis-string/description/

from typing import List
from collections import Counter

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0 # 최소 ( 개수
        high = 0 # *도 (로 쳤을 때 -> 최다 ( 개수
        
        for char in s:
            if char == "(":
                low += 1
                high += 1
            elif char == ")":
                if low > 0:
                    low -= 1
                high -= 1
            elif char == "*":
                if low > 0:
                    low -= 1
                high += 1
            
            if high < 0: # ")"가 너무 많음
                return False
        
        return low == 0

print(Solution().checkValidString("()")) # True
print(Solution().checkValidString("(*)")) # True
print(Solution().checkValidString("(*))")) # True
print(Solution().checkValidString("()()")) # True
print(Solution().checkValidString("()())")) # False
print(Solution().checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()")) # True
print(Solution().checkValidString("(((((*)))**")) # True
print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")) # False
