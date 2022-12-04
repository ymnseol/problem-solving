# LeetCode - Find Peak Element(162)
# https://leetcode.com/problems/find-peak-element/description/

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if mid == 0 and nums[mid + 1] < nums[mid]:
                return mid
            if mid == len(nums) - 1 and nums[mid - 1] < nums[mid]:
                return mid
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return max((left, right), key=lambda i: nums[i])
