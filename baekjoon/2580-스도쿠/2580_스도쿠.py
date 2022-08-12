import sys

class Sudoku:
    def __init__(self, board):
        self.board = board
        self.blank = []
        self.flag = False
    
    def find_blank(self):
        for i in range(9):
            for j in range(9):
                if not self.board[i][j]:
                    self.blank.append((i, j))

    def promising(self, target, row, col):
        for i in range(9):
            if target == self.board[row][i]:
                return False
        
        for r in range(9):
            if target == self.board[r][col]:
                return False
        
        row = row // 3 * 3
        col = col // 3 * 3

        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if target == self.board[r][c]:
                    return False
        
        return True

    def fill(self, n):
        if n == len(self.blank):
            self.flag = True
            return
        
        for i in range(1, 10):
            if self.promising(i, self.blank[n][0], self.blank[n][1]):
                self.board[self.blank[n][0]][self.blank[n][1]] = i
                self.fill(n + 1)
                if not self.flag:
                    self.board[self.blank[n][0]][self.blank[n][1]] = 0
    
    def print_board(self):
        for r in self.board:
            for i, c in enumerate(r):
                if i:
                    print(" ", end="")
                print(c, end="")
            print()

if __name__ == '__main__':
    unfilled_sudoku = []
    for _ in range(9):
        unfilled_sudoku.append(list(map(int, sys.stdin.readline().split())))

    sudoku = Sudoku(unfilled_sudoku)
    sudoku.find_blank()
    sudoku.fill(0)

    sudoku.print_board()
    