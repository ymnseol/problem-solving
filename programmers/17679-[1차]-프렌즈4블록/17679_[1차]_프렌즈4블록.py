# 프로그래머스 - [1차] 프렌즈4블록(17679)
# https://school.programmers.co.kr/learn/courses/30/lessons/17679

from collections import deque

class Board:
    def __init__(self, n_rows, n_cols, board):
        self.board = board
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_erased = 0
    
    def build(self):
        self.board = [list(row) for row in self.board]
        self.board = [deque([self.board[row][col] for row in range(self.n_rows)]) for col in range(self.n_cols)]
        self.n_rows, self.n_cols = self.n_cols, self.n_rows
    
    def check(self, row, col, target):
        if target:
            return sum([True for r in range(row, row + 2) for c in range(col, col + 2) if target == self.board[r][c]]) == 4
        return False
    
    def erase(self):
        to_erase = set()
        for row in range(self.n_rows - 1):
            for col in range(self.n_cols - 1):
                if self.check(row, col, self.board[row][col]):
                    to_erase.add((row, col))
                    to_erase.add((row, col + 1))
                    to_erase.add((row + 1, col))
                    to_erase.add((row + 1, col + 1))
        for row, col in to_erase:
            self.board[row][col] = ''
        self.n_erased += len(to_erase)
        return self.board
    
    def push_down(self):
        for i, col in enumerate(list(self.board)):
            for j, block in enumerate(list(col)):
                if not block:
                    del self.board[i][j]
                    self.board[i].appendleft('')
        return self.board
    
    def play_game(self):
        old_n_erased = self.n_erased
        self.erase()
        self.push_down()
        if self.n_erased == old_n_erased:
            return self.n_erased
        self.play_game()

def solution(m, n, board):
    game = Board(m, n, board)
    game.build()
    game.play_game()
    return game.n_erased
