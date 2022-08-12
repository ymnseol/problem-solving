# LeetCode - N-Queens II(52)
# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def __init__(self):
        self.n_queens = -1
        self.row = []
        self.n_cases = 0
        
    def build(self, n: int):
        self.n_queens = n
        self.row = [-1] * self.n_queens
    
    def promising(self, col: int) -> bool:
        for i in range(col):
            if self.row[col] == self.row[i] or abs(self.row[col] - self.row[i]) == col - i:
                return False
        return True
    
    def nQueens(self, n: int) -> int:
        if n == self.n_queens:
            self.n_cases += 1
            return
        
        for i in range(self.n_queens):
            self.row[n] = i
            if self.promising(n):
                self.nQueens(n + 1)
    
    def totalNQueens(self, n: int) -> int:
        self.build(n)
        self.nQueens(0)
        return self.n_cases
