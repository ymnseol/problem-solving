# 백준 - 상어 초등학교(21608)
# https://www.acmicpc.net/problem/21608

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    pref = dict()
    seat = [[0] * N for _ in range(N)]
    for _ in range(N ** 2):
        stu, *prefs = list(map(int, sys.stdin.readline().split()))
        pref[stu] = prefs

    for stu, prefs in pref.items():
        best_r, best_c = -1, -1
        best_score = -1
        best_empty = -1

        for i in range(N):
            for j in range(N):
                score = 0
                empty = 0
                if seat[i][j]:
                    continue
                if i:
                    score += seat[i - 1][j] in prefs
                    empty += not seat[i - 1][j]
                if j:
                    score += seat[i][j - 1] in prefs
                    empty += not seat[i][j - 1]
                if i < N - 1:
                    score += seat[i + 1][j] in prefs
                    empty += not seat[i + 1][j]
                if j < N - 1:
                    score += seat[i][j + 1] in prefs
                    empty += not seat[i][j + 1]
                
                if score > best_score:
                    best_r, best_c = i, j
                    best_score = score
                    best_empty = empty
                elif score == best_score:
                    if empty > best_empty:
                        best_r, best_c = i, j
                        best_score = score
                        best_empty = empty
        seat[best_r][best_c] = stu

    total_score = 0
    for i in range(N):
        for j in range(N):
            stu = seat[i][j]
            prefs = pref[stu]
            n_prefs = 0
            if i:
                n_prefs += seat[i - 1][j] in prefs
            if j:
                n_prefs += seat[i][j - 1] in prefs
            if i < N - 1:
                n_prefs += seat[i + 1][j] in prefs
            if j < N - 1:
                n_prefs += seat[i][j + 1] in prefs
            total_score += (10 ** (n_prefs - 1) if n_prefs else 0)
    print(total_score)
