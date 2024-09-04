# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length

        prefix = 1
        for i in range(length):
            products[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(length-1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
        
        return products
