from collections import defaultdict
import sys


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_freq = 0
        max_len = 0
        cache = defaultdict(int)
        for end, c in enumerate(s):
            cache[c] += 1
            max_freq = max(max_freq, cache[c])

            if (end - start + 1) - max_freq > k:
                cache[s[start]] -= 1
                start += 1

            max_len = max(max_len, (end - start + 1))

        return max_len


if __name__ == "__main__":
    s = sys.argv[1]
    k = int(sys.argv[2])
    print(Solution().characterReplacement(s, k))
