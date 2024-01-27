# 프로그래머스 - 최빈값 구하기(120812)
# https://school.programmers.co.kr/learn/courses/30/lessons/120812

from collections import Counter


def solution(array):
    if len(set(array)) == 1:
        return array[0]
    most_common_elements = Counter(array).most_common(2)
    if most_common_elements[0][1] == most_common_elements[1][1]:
        return -1
    return most_common_elements[0][0]
