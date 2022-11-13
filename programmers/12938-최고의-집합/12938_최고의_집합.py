# 프로그래머스 - 최고의 집합(12938)
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if s < n: return [-1]
    if s == n: return [1] * n
    q, r = s // n, s % n
    return [q if n - i > r else q + 1 for i in range(n)]
