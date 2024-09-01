# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stack = []
      for token in tokens:
          if token in "+-*/":
              back = stack.pop()
              front = stack.pop()

              if token == "+":
                  result = front + back
              elif token == "-":
                  result = front - back
              elif token == "*":
                  result = front * back
              elif token == "/":
                  result = int(front / back)

              stack.append(result)
          else:
              stack.append(int(token))

      return stack[0]
    
print(Solution().evalRPN(["2","1","+","3","*"]))
print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))