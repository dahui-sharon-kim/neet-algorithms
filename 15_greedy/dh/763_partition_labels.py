# https://leetcode.com/problems/partition-labels/

from typing import List
from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        partitions = []

        start = end = 0

        for i, char in enumerate(s):
            print(f"char: {char}, i: {i}, end = max({end}, {last_occurrence[char]})")
            end = max(end, last_occurrence[char])

            if i == end:
                partitions.append(end-start+1)
                start = i+1
        return partitions
        
print(Solution().partitionLabels("ababcbacadefegdehijhklij")) # [9,7,8]
print(Solution().partitionLabels("eccbbbbdec")) # [10]
