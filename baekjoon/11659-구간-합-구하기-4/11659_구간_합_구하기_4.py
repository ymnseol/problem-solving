# 백준 - 구간 합 구하기 4(11659)
# https://www.acmicpc.net/problem/11659

import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    dp = [0] *  (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + nums[i - 1]
    
    for _ in range(M):
        s, d = map(int, sys.stdin.readline().split())
        print(dp[d] - dp[s - 1])
