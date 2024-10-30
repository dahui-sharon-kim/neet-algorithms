# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/

from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        achievable = [False, False, False]

        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(3)):
                continue

            for i in range(3):
                if triplet[i] == target[i]:
                    achievable[i] = True

            # 이미 조건을 만족하면 return True
            if all(achievable):
                return True

        return all(achievable)