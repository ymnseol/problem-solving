# 프로그래머스 - 점프와 순간 이동(12980)
# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    cnt = 0
    while n > 0:
        if n % 2:
            n -= 1
            cnt += 1
        else:
            n //= 2
    return cnt
