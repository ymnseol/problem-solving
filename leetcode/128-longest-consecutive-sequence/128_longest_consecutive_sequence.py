# LeetCode - Longest Consecutive Sequence(128)
# https://leetcode.com/problems/longest-consecutive-sequence

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_l = 0
        for n in nums:
            if n - 1 in nums:
                continue
            l = 1
            curr = n
            while curr + 1 in nums:
                l += 1
                curr += 1
            max_l = max(l, max_l)
        return max_l
