# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        
        for i in range(n + 1):
            xor ^= i
        
        for num in nums:
            xor ^= num
        
        return xor
