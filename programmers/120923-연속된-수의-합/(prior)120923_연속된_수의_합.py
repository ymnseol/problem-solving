# 프로그래머스 - 연속된 수의 합(120923)
# https://school.programmers.co.kr/learn/courses/30/lessons/120923


def solution(num, total):
    mid = total // num
    start_index = mid - num // 2 if num % 2 else mid - num // 2 + 1
    end_index = start_index + num
    return [i for i in range(start_index, end_index)]
