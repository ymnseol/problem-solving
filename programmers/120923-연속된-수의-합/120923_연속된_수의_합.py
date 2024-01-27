# 프로그래머스 - 연속된 수의 합(120923)
# https://school.programmers.co.kr/learn/courses/30/lessons/120923


def solution(num, total):
    if num % 2:
        return list(range(total // num - num // 2, total // num + num // 2 + 1))
    return list(range(total // num - num // 2 + 1, total // num + num // 2 + 1))
