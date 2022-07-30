# 백준 - 부분합(1806)
# https://www.acmicpc.net/problem/1806

if __name__ == '__main__':
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))

    left = right = 0
    partial_sum = seq[0]
    min_len = n + 1

    while left <= right and right < n:
        if partial_sum < s:
            right += 1
            if right < n:
                partial_sum += seq[right]
        else:
            min_len = min(min_len, right - left + 1)
            partial_sum -= seq[left]
            left += 1
    
    if min_len == n + 1:
        print(0)
    else:
        print(min_len)
