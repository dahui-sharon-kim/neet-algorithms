import sys
from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = f"{result}{len(s)}_*_{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            count = 0
            for i in range(len(s)):
                if s[i : i + 3] == "_*_":
                    count = int(s[:i])
                    break
            count_len = len(str(count))
            result.append(s[count_len + 3 : count_len + count + 3])
            s = s[count + count_len + 3 :]
        return result


if __name__ == "__main__":
    strs = sys.argv[1:]
    encoded = Solution().encode(strs)
    print(encoded)
    decoded = Solution().decode(encoded)
    print(decoded)
