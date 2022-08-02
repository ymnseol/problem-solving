# 프로그래머스 - 위장(42578)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from functools import reduce

def solution(clothes):
    op = dict()
    for _, t in clothes:
        try:
            op[t] += 1
        except:
            op[t] = 1
    
    return reduce(lambda x, y: x * y, [v + 1 for _, v in op.items()]) - 1
