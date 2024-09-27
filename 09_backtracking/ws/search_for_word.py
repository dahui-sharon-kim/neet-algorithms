from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        def check_neighbor(cur, index):
            i, j = cur
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= columns
                or board[i][j] != word[index]
            ):
                return False
            if index == len(word) - 1:
                return True

            board[i][j] = "*"

            if (
                check_neighbor((i - 1, j), index + 1)
                or check_neighbor((i + 1, j), index + 1)
                or check_neighbor((i, j - 1), index + 1)
                or check_neighbor((i, j + 1), index + 1)
            ):
                return True

            board[i][j] = word[index]
            return False

        for row in range(rows):
            for col in range(columns):
                if board[row][col] == word[0]:
                    if check_neighbor((row, col), 0):
                        return True

        return False
