from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        pacifics, atlantics = set(), set()

        def bfs(i, j, visited, prev_height):
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= columns
                or (i, j) in visited
                or heights[i][j] < prev_height
            ):
                return

            visited.add((i, j))

            bfs(i - 1, j, visited, heights[i][j])
            bfs(i, j - 1, visited, heights[i][j])
            bfs(i + 1, j, visited, heights[i][j])
            bfs(i, j + 1, visited, heights[i][j])

        for row in range(rows):
            bfs(row, 0, pacifics, heights[row][0])
            bfs(row, columns - 1, atlantics, heights[row][columns - 1])

        for col in range(columns):
            bfs(0, col, pacifics, heights[0][col])
            bfs(rows - 1, col, atlantics, heights[rows - 1][col])

        return list(map(list, list(atlantics.intersection(pacifics))))
