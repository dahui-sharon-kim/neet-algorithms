from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()

        for triplet in triplets:
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue
            for i, t in enumerate(triplet):
                if target[i] == t:
                    res.add(i)
        return len(res) == 3
