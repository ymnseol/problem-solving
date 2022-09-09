# 프로그래머스 - 파괴되지 않은 건물(92344)
# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    cnt = 0
    n_rows = len(board)
    n_cols = len(board[0])
    
    diff = [[0] * (n_cols + 1) for _ in range(n_rows + 1)]
    
    for typ, r1, c1, r2, c2, deg in skill:
        diff[r1][c1] += (deg if typ == 2 else -deg)
        diff[r1][c2 + 1] -= (deg if typ == 2 else -deg)
        diff[r2 + 1][c1] -= (deg if typ == 2 else -deg)
        diff[r2 + 1][c2 + 1] += (deg if typ == 2 else -deg)
    
    for r in range(n_rows):
        for c in range(n_cols):
            diff[r][c + 1] += diff[r][c]
    
    for c in range(n_cols):
        for r in range(n_rows):
            diff[r + 1][c] += diff[r][c]
    
    for r in range(n_rows):
        for c in range(n_cols):
            board[r][c] += diff[r][c]
            if board[r][c] > 0:
                cnt += 1
    
    return cnt
