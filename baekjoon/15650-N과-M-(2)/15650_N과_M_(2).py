import sys
from itertools import combinations

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    [print(e) if i == M - 1 else print(e, end=" ") for c in list(combinations(range(1, N + 1), M)) for i, e in enumerate(c)]
