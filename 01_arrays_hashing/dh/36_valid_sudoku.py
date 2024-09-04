# https://leetcode.com/problems/valid-sudoku/description/

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      rows = [set() for _ in range(9)]
      columns = [set() for _ in range(9)]
      sub_boxes = [set() for _ in range(9)]
      
      for i in range(9):
          for j in range(9):
              num = board[i][j]
              
              if num == '.':
                  continue
              
              if num in rows[i]:
                  return False
              rows[i].add(num)
              
              if num in columns[j]:
                  return False
              columns[j].add(num)
              
              sub_box_index = (i // 3) * 3 + (j // 3)
              if num in sub_boxes[sub_box_index]:
                  return False
              sub_boxes[sub_box_index].add(num)
      
      return True
