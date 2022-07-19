# 백준 - 거스름돈(5585)
# https://www.acmicpc.net/problem/5585

change = 1000 - int(input())
n_coins = 0

for c in [500, 100, 50, 10, 5, 1]:
    n_coins += change // c
    change %= c

print(n_coins)
