from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def bfs(i, j):
            nonlocal fresh
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] == 0:
                return

            if grid[i][j] == 1:
                fresh -= 1
                grid[i][j] = 2
                q.append((i, j))

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        if not q:
            return -1

        count = -1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                bfs(i + 1, j)
                bfs(i - 1, j)
                bfs(i, j + 1)
                bfs(i, j - 1)
            count += 1

        return count if fresh == 0 else -1
