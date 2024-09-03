# https://leetcode.com/problems/search-a-2d-matrix/description/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        while matrix:
            mid = len(matrix) // 2
            if target in matrix[mid]:
                return True
            if target < matrix[mid][0]:
                matrix = matrix[:mid]
            elif target > matrix[mid][-1]:
                matrix = matrix[mid + 1:]
            else:
                return False
        return False
