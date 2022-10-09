# 백준 - 스타트와 링크(14889)
# https://www.acmicpc.net/problem/14889

import sys
from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    table = []
    all = set(range(N))
    for i in range(N):
        table.append(list(map(int, sys.stdin.readline().split())))
        table[i][i] = 101
    
    min_diff = float('inf')
    for pair in map(set, combinations(all, N // 2)):
        front = list(pair)
        rear = list(all - pair)
        front_sum = sum([table[front[i]][front[j]] + table[front[j]][front[i]] for i in range(len(front)) for j in range(i + 1, len(front))])
        rear_sum = sum([table[rear[i]][rear[j]] + table[rear[j]][rear[i]] for i in range(len(rear)) for j in range(i + 1, len(rear))])
        
        min_diff = min(abs(front_sum - rear_sum), min_diff)
    
    print(min_diff)
