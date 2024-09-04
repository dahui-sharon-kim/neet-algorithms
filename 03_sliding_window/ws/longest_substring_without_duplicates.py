import sys


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        result = 0
        for c in s:
            while c in window:
                window.pop(0)
            window.append(c)
            result = max(result, len(window))
        return result


if __name__ == "__main__":
    s = sys.argv[1]
    print(Solution().lengthOfLongestSubstring(s))
