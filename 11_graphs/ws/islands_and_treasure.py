from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def dfs(i, j):
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= columns
                or grid[i][j] == -1
                or (i, j) in visited
            ):
                return

            visited.add((i, j))
            q.append((i, j))

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))

        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
            dist += 1
