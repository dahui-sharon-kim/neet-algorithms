from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        columns = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != "1":
                return

            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        return count
