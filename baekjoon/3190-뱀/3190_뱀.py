# 백준 - 뱀(3190)
# https://www.acmicpc.net/problem/3190

import sys
from collections import deque

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    apples = [[False] * N for _ in range(N)]
    body = [[False] * N for _ in range(N)]
    for _ in range(K):
        r, c = tuple(map(int, sys.stdin.readline().split()))
        apples[r - 1][c - 1] = True
    L = int(sys.stdin.readline())
    moves = deque([sys.stdin.readline().split() for _ in range(L)])
    df = {'N': (-1, 0), 'E': (0, 1), 'W': (0, -1), 'S': (1, 0)}
    dt = {
        'N': {'L': 'W', 'D': 'E'},
        'E': {'L': 'N', 'D': 'S'},
        'W': {'L': 'S', 'D': 'N'},
        'S': {'L': 'E', 'D': 'W'}
    }
    X = 0
    C = 'E'
    snake = deque([(0, 0)])
    while True:
        # 방향 전환
        while moves and int(moves[0][0]) == X:
            _, t = moves.popleft()
            C = dt[C][t]

        head = (snake[-1][0] + df[C][0], snake[-1][1] + df[C][1])

        # 벽이나 몸에 부딪히는 경우
        if (0 <= head[0] < N) and (0 <= head[1] < N) and not body[head[0]][head[1]]:
            pass
        else:
            break

        snake.append(head)
        body[head[0]][head[1]] = True

        if apples[head[0]][head[1]]:
            apples[head[0]][head[1]] = False
        else:
            tail = snake.popleft()
            body[tail[0]][tail[1]] = False
        X += 1
    print(X + 1)
