import sys


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join([i for i in s if i.isalnum()]).lower()
        filtered = list(filtered)
        one = 0
        two = int(len(filtered)) - 1
        while one < two:
            if filtered[one] != filtered[two]:
                return False
            one += 1
            two -= 1
        return True


if __name__ == "__main__":
    s = sys.argv[1]
    print(Solution().isPalindrome(s))
