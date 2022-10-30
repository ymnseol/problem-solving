# LeetCode - Search a 2D Matrix II(240)
# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0
        
        while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            if target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                return True
        return False
