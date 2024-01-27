# 프로그래머스 - 저주의 숫자 3(120871)
# https://school.programmers.co.kr/learn/courses/30/lessons/120871


def solution(n):
    new_n = 0
    for _ in range(n):
        new_n += 1
        while ("3" in str(new_n)) or (new_n % 3 == 0):
            new_n += 1
    return new_n
