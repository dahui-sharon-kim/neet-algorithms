# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l, r = 0, length-1

        # 가장 작은 값(회전하기 전 nums의 첫 번째 값) 찾기
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
        
        rotation_i = l

        l, r = 0, length -1
        while l <= r:
            mid = (l+r)//2
            real_mid = (mid+rotation_i) % length

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
