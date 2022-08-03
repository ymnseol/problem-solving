# 프로그래머스 - 124 나라의 숫자(12899)
# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    digit = ['4', '1', '2']
    ans = ''
    while n:
        ans = digit[n % 3] + ans
        n = n // 3 - (not n % 3)
    return ans
