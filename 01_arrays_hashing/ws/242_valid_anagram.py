import sys


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


if __name__ == "__main__":
    first = sys.argv[1]
    second = sys.argv[2]
    s = Solution()
    print(s.isAnagram(first, second))
