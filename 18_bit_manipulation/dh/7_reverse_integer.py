# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1]) # int() 씌워서 첫째 자리의 0을 없앨 수 있음

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return sign * reversed_num

print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
