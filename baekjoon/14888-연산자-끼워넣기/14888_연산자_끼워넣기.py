# 백준 - 연산자 끼워넣기(14888)
# https://www.acmicpc.net/problem/14888

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
n_ops = list(map(int, sys.stdin.readline().split()))
ops = ['+', '-', '*', '//']

max_dp = {i: set() for i in range(N)}
min_dp = {i: set() for i in range(N)}

for num_idx, num in enumerate(nums):
    if not num_idx: # Initialize
        max_dp[0].add((num, tuple(n_ops[:])))
        min_dp[0].add((num, tuple(n_ops[:])))
        continue

    for prev_num, prev_ops in max_dp[num_idx - 1]:
        for op_idx, op_left in enumerate(prev_ops):
            if op_left:
                if op_idx == 3:
                    curr_num = int(prev_num / num)
                else:
                    curr_num = eval(f'{prev_num} {ops[op_idx]} {num}')
                curr_ops = list(prev_ops[:])
                curr_ops[op_idx] -= 1
                max_dp[num_idx].add((curr_num, tuple(curr_ops)))
    
    for prev_num, prev_ops in min_dp[num_idx - 1]:
        for op_idx, op_left in enumerate(prev_ops):
            if op_left:
                if op_idx == 3:
                    curr_num = int(prev_num / num)
                else:
                    curr_num = eval(f'{prev_num} {ops[op_idx]} {num}')
                curr_ops = list(prev_ops[:])
                curr_ops[op_idx] -= 1
                min_dp[num_idx].add((curr_num, tuple(curr_ops)))

print(max(max_dp[N - 1], key=lambda x: x[0])[0])
print(min(min_dp[N - 1], key=lambda x: x[0])[0])
