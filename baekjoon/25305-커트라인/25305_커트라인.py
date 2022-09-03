# 백준 - 커트라인(25305)
# https://www.acmicpc.net/problem/25305

import sys

N, k = map(int, sys.stdin.readline().split())
x = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

print(x[k - 1])
