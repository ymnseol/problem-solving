# 프로그래머스 - 멀쩡한 사각형(62048)
# https://school.programmers.co.kr/learn/courses/30/lessons/62048

def solution(w, h):
    a, b = max(w, h), min(w, h)
    while b > 0:
        r = a % b
        a = b
        b = r
    return w * h - (w + h - a)
