def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    dr = [1, 0, -1] # 0: top to down, 1: left to right, 2: down to top
    dc = [0, 1, -1]
    turn = r = c = 0
    num = 1
    
    for limit in range(n):
        for _ in range(n - limit):
            answer[r][c] = num
            num += 1
            r += dr[turn]
            c += dc[turn]
        r -= dr[turn]
        c -= dc[turn]
        turn = (turn + 1) % 3
        r += dr[turn]
        c += dc[turn]

    return sum(answer, []) # flatten
