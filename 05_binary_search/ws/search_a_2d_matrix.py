import sys
import json
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if matrix[mid][-1] < target:
                start = mid + 1
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                break

        if start > end:
            return False

        row = matrix[start + (end - start) // 2]
        start, end = 0, len(row) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if row[mid] < target:
                start = mid + 1
            elif row[mid] > target:
                end = mid - 1
            else:
                return True

        return False


if __name__ == "__main__":
    target = int(sys.argv[1])
    matrix = json.loads(sys.argv[2])
    print(Solution().searchMatrix(matrix, target))
