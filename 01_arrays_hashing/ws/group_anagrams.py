from collections import defaultdict
import sys
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = list(s)
        ref = list(t)
        second = list(t)
        for i in ref:
            try:
                first.remove(i)
                second.remove(i)
            except ValueError:
                return False

        if len(first) == 0 and len(second) == 0:
            return True
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            inserted = False
            for key in results:
                if self.isAnagram(key, s):
                    results[key].append(s)
                    inserted = True
            if not inserted:
                results[s].append(s)
        return list(results.values())


if __name__ == "__main__":
    strs = sys.argv[1:]
    print(Solution().groupAnagrams(strs))
