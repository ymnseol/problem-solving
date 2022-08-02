# 프로그래머스 - 나머지 한 점(1878)
# https://school.programmers.co.kr/learn/courses/18/lessons/1878?language=python3

def solution(v):
    xs = [x for x, _ in v]
    ys = [y for _, y in v]
    return [min(xs, key=xs.count), min(ys, key=ys.count)]
