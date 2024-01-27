# 프로그래머스 - 겹치는 선분의 길이(120876)
# https://school.programmers.co.kr/learn/courses/30/lessons/120876


def solution(lines):
    overlapped = [0] * 200
    for start, end in lines:
        overlapped[start + 100 : end + 100] = [
            i + 1 for i in overlapped[start + 100 : end + 100]
        ]
    return len([i for i in overlapped if i > 1])
