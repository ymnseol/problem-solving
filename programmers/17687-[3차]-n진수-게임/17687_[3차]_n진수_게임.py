# 프로그래머스 - [3차] n진수 게임(17687)
# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def convert(x, n):
    hex_range = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    new_x = ''
    if x == 0:
        return '0'
    while x > 0:
        new_x = hex_range[x % n] + new_x
        x = x // n
    return new_x

def solution(n, t, m, p):
    start = p - 1
    end = t * m + p - 1
    return ''.join([convert(x, n) for x in range(t * m)])[start:end:m]
