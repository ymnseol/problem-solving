# LeetCode - Wiggle Sort II(324)
# https://leetcode.com/problems/wiggle-sort-ii/
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums[::2], nums[1::2] = nums[:((len(nums) + 1) // 2)][::-1], nums[((len(nums) + 1) // 2):][::-1]
