# 프로그래머스 - 카펫(42842)
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

from math import sqrt

def solution(brown, yellow):
    for i in range(1, int(sqrt(yellow)) + 1):
        if yellow % i == 0 and brown == (i + 1 + yellow // i + 1) * 2:
            return [yellow // i + 2, i + 2]
