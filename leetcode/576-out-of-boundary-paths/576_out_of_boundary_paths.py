# LeetCode - Out of Boundary Paths(576)(Daily LeetCoding Challenge July, Day 16)
# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def __init__(self):
        self.n_rows = -1
        self.n_cols = -1
    
    @cache
    def track(self, r: int, c: int, moves_left: int):
        if moves_left < 0:
            return 0
        elif (r < 0 or r >= self.n_rows) or (c < 0 or c >= self.n_cols):
            return 1
        else:
            return self.track(r - 1, c, moves_left - 1) + self.track(r + 1, c, moves_left - 1) + self.track(r, c - 1, moves_left - 1) + self.track(r, c + 1, moves_left - 1)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Initialize
        self.n_rows = m
        self.n_cols = n

        return self.track(startRow, startColumn, maxMove) % 1000000007
