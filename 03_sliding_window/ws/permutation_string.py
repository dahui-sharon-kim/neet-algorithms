import sys


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref = {}
        for c in s1:
            ref[c] = ref.get(c, 0) + 1

        permu = {}
        window = list(s2[: len(s1)])
        for c in window:
            permu[c] = permu.get(c, 0) + 1

        if ref == permu:
            return True

        for c in range(len(s2) - len(s1)):
            if first := window.pop(0):
                if permu[first] == 1:
                    del permu[first]
                else:
                    permu[first] -= 1

            char = s2[c + len(s1)]
            window.append(char)
            permu[char] = permu.get(char, 0) + 1

            if ref == permu:
                return True

        return False


if __name__ == "__main__":
    s1 = sys.argv[1]
    s2 = sys.argv[2]

    print(Solution().checkInclusion(s1, s2))
