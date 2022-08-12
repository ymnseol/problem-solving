import sys

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    dp = [n for n in nums]

    for i in range(1, n):
        dp[i] = max(dp[i], dp[i - 1] + dp[i])
    
    print(max(dp))
