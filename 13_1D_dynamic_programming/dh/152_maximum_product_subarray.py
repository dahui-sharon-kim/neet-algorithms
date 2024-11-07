# https://leetcode.com/problems/maximum-product-subarray/description/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = min_product = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            result = max(result, max_product)
        return result

print(Solution().maxProduct([2,3,-2,4])) # 6
print(Solution().maxProduct([-2,0,-1])) # 0
