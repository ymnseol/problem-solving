# 프로그래머스 - 키패드 누르기(67256)
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

from itertools import product


def solution(numbers, hand):
    answer = ""
    coords = list(product(range(0, 4), range(0, 3)))
    distances = [
        [abs(r1 - r2) + abs(c1 - c2) for n2, (r2, c2) in enumerate(coords)]
        for n1, (r1, c1) in enumerate(coords)
    ]
    lkey, rkey = 9, 11
    for num in numbers:
        num = num - 1 if num else 10
        if num % 3 == 0:
            answer += "L"
            lkey = num
        elif num % 3 == 2:
            answer += "R"
            rkey = num
        elif (distances[lkey][num] < distances[rkey][num]) or (
            (distances[lkey][num] == distances[rkey][num]) and hand == "left"
        ):
            answer += "L"
            lkey = num
        else:
            answer += "R"
            rkey = num
    return answer
