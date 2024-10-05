from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, columns = len(board), len(board[0])

        def draw(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or board[i][j] != "O":
                return

            board[i][j] = "S"

            draw(i + 1, j)
            draw(i - 1, j)
            draw(i, j + 1)
            draw(i, j - 1)

        for row in range(rows):
            draw(row, 0)
            draw(row, columns - 1)
        for col in range(columns):
            draw(0, col)
            draw(rows - 1, col)

        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "S":
                    board[row][col] = "O"
