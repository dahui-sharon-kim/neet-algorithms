# https://leetcode.com/problems/word-search/description/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def search(row, col, count):
            if count == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[count] or visited[row][col]:
                return False

            visited[row][col] = True
            
            found = (
                search(row+1, col, count+1) or  # down
                search(row-1, col, count+1) or  # up
                search(row, col+1, count+1) or  # right
                search(row, col-1, count+1)     # left
            )
            
            visited[row][col] = False 
            return found

        starting_points = []
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    starting_points.append([row, col])

        for [row, col] in starting_points:            
            if search(row, col, 0):
                return True
        
        return False
    
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
