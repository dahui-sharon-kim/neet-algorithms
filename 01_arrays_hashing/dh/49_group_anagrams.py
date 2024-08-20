# https://leetcode.com/problems/group-anagrams/description/
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 아직 존재하지 않는 key에 접근하려고 하면 해당 key를 생성하고 value를 빈 리스트로 초기화
        grouped_keys = defaultdict(list)
        for s in strs:
            sorted_str = tuple(sorted(s))
            grouped_keys[sorted_str].append(s)
        return list(grouped_keys.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams(["", ""]))
