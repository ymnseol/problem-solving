# LeetCode - Unique Paths(62)
# https://leetcode.com/problems/unique-paths

from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))
