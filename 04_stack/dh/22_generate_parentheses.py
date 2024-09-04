# https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    def __init__(self):
        self.stack = []
        
    def backtrack(self, current: str, open: int, close: int):
        if open == 0 and close == 0:
            self.stack.append(current)
            return
        
        if open > 0:
            self.backtrack(current + "(", open - 1, close)
        
        if close > open:
            self.backtrack(current + ")", open, close - 1)
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack("", n, n)
        return self.stack