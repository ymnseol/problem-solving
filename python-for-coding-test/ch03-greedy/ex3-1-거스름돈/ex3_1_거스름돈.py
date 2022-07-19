# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 거스름돈

if __name__ == '__main__':
    change = int(input())
    n_coins = 0

    for c in [500, 100, 50, 10]:
        n_coins += change // c
        change %= c

    print(n_coins)
