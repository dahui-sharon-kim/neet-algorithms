from collections import defaultdict
import sys
import json
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(list)
        columns = defaultdict(list)

        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                columns[j].append(elem)
                squares[(i // 3, j // 3)].append(elem)

            numbers = [elem for elem in row if elem.isalnum()]
            if len(numbers) != len(set(numbers)):
                return False

        for column in columns.values():
            numbers = [elem for elem in column if elem.isalnum()]
            if len(numbers) != len(set(numbers)):
                return False

        for square in squares.values():
            numbers = [elem for elem in square if elem.isalnum()]
            if len(numbers) != len(set(numbers)):
                return False

        return True


if __name__ == "__main__":
    user_input = sys.argv[1]
    board = json.loads(user_input)

    print(Solution().isValidSudoku(board))
