from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maximum = 0
        
        def bfs(row, col):
            q = deque([(row,col)])
            visited.add((row,col))
            count = 1
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    adj_row, adj_col = r+dr, c+dc
                    if (adj_row in range(rows) and
                        adj_col in range(cols) and
                        grid[adj_row][adj_col] == 1 and
                        (adj_row,adj_col) not in visited):
                        q.append((adj_row,adj_col))
                        visited.add((adj_row, adj_col))
                        count += 1

            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maximum = max(maximum, bfs(row, col))
        
        return maximum