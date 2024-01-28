# 프로그래머스 - 주사위 게임 3(181916)
# https://school.programmers.co.kr/learn/courses/30/lessons/181916

from collections import Counter


def solution(a, b, c, d):
    counter = Counter((a, b, c, d))
    if len(counter) == 1:  # 네 주사위에서 나온 숫자가 모두 같은 경우
        return 1111 * a

    mcs = counter.most_common()
    fmc, fmc_count = mcs[0]
    smc, smc_count = mcs[1]  # 이전 조건문에서 숫자가 오로지 한 종류인 경우를 이미 처리함
    print(fmc, smc)
    if fmc_count == 1:  # 네 주사위에 적힌 숫자가 모두 다른 경우
        return min(counter.keys())
    if fmc_count == 3:  # 세 주사위에서 나온 숫자가 같은 경우
        return (10 * fmc + smc) ** 2
    if fmc_count == smc_count:
        # 두 주사위끼리 나온 숫자가 같은 경우 (이전 조건문에서 모두 다른 숫자인 경우를 이미 처리함)
        return (fmc + smc) * abs(fmc - smc)
    return smc * mcs[-1][0]
