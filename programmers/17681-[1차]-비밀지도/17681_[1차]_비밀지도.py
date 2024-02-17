# 프로그래머스 - [1차] 비밀지도(17681)
# https://school.programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    return [
        bin(num1 | num2).replace("0b", "").zfill(n).replace("0", " ").replace("1", "#")
        for num1, num2 in zip(arr1, arr2)
    ]
