# 프로그래머스 - 유한소수 판별하기(120878)
# https://school.programmers.co.kr/learn/courses/30/lessons/120878


def get_gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a


def solution(a, b):
    gcd = get_gcd(a, b)
    numerator, denominator = a // gcd, b // gcd
    while denominator % 2 == 0:
        denominator >>= 1
    while denominator % 5 == 0:
        denominator //= 5
    if denominator == 1:
        return 1
    return 2
