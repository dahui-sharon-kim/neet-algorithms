from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        columns = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] != 1:
                return 0

            grid[i][j] = 0

            res = 0
            res += dfs(i + 1, j)
            res += dfs(i - 1, j)
            res += dfs(i, j + 1)
            res += dfs(i, j - 1)

            return res + 1

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
        return res
