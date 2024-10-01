# https://leetcode.com/problems/number-of-islands/description/

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_r, num_c = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque([(r,c)])
            visited.add((r,c))
            directions = [[-1,0], [1,0], [0,1], [0,-1]]
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    adjacent_r, adjacent_c = row+dr, col+dc
                    if (adjacent_r in range(num_r) and
                        adjacent_c in range(num_c) and  
                        grid[adjacent_r][adjacent_c] == "1" and
                        (adjacent_r,adjacent_c) not in visited):
                        q.append((adjacent_r, adjacent_c))
                        visited.add((adjacent_r, adjacent_c))

        for row in range(num_r):
            for col in range(num_c):
                if grid[row][col] == "1" and (row, col) not in visited:
                  bfs(row, col)
                  islands += 1
        
        return islands