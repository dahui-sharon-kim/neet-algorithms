# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = f"{n:032b}"
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)
